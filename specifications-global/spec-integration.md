---
title: "spec-integration"
doc-id: "mb-a1d9a710"
updated: "2026-11-11"
---
# Mybizz — Integration Specification

**Scope:** Mybizz-wide. Covers all external service integrations — Amazon SES (all email), Stripe (card payments), PayPal (optional second payment method).

---

## 1. Integration Architecture

All external service integrations follow the same pattern:

1. **Credentials stored in Vault** — secret keys encrypted at rest, never in config tables
2. **Server-side only** — integration code lives in server modules, never client code
3. **Response envelope** — all integration calls return `{'success': bool, 'data': ...}` or `{'success': bool, 'error': ...}`
4. **Error logging** — all integration failures logged to `error_log` table
5. **Retry logic** — exponential backoff for transient failures

---

## 2. Amazon SES Integration

Amazon SES is the single email service: every email received and sent. The CRM is built into the application; no outside CRM is integrated ([[[default:adr-global/adr-brevo-email-and-crm|Amazon SES for Email; CRM Built In]]](C:/dev/project-library-global/adr-global/adr-brevo-email-and-crm.md)).

### 2.1 Credentials

| Vault Key | Purpose | Used By |
|---|---|---|
| `aws_access_key_id`, `aws_secret_access_key` | SES API and the client's received-email prefix in S3, scoped to this client | Sending, receiving |
| `ses_smtp_password` | Anvil's Custom Mail Server | System email |

All three are written by Mybizz_management at provisioning. Each client has its own SES tenant and domain identity in Mybizz's AWS account, region `eu-west-1`.

### 2.2 Sending

**SMTP constants (identical for all clients, not stored):**
- Host: `email-smtp.eu-west-1.amazonaws.com`
- Port: `587` (STARTTLS)

**Client-specific configuration (in `email_config` table):**
- `from_email` — an address on the client's domain
- `from_name` — sender display name

**Emails sent through the SES API:**
- Booking confirmations
- Appointment reminders (24h and 1h)
- Invoice delivery
- Payment receipts
- Welcome emails (post-onboarding)
- Marketing sequences and broadcasts

**Error handling:**
- Connection failures → retry 3 times with exponential backoff
- Authentication failures → log to `error_log`, alert owner
- Throttling → queue and retry on next scheduled run

### 2.3 Receiving

MX record on the client's domain → SES → the client's S3 prefix → SNS → `[base_url]/_/api/email/inbound` → a background task reads the email from S3, stores it in the instance and deletes it from S3. An S3 lifecycle rule deletes any received email file 7 days after it arrives, so no file stays in S3 if its processing fails.

### 2.4 Events and Unsubscribe

- SES reports deliveries, bounces, complaints, opens and clicks through SNS to `[base_url]/_/api/email/events`.
- A hard bounce or a complaint adds the address to the suppression list; no email is sent to a suppressed address.
- Every marketing email carries an unsubscribe link to `[base_url]/_/api/email/unsubscribe` and the `List-Unsubscribe` and `List-Unsubscribe-Post` headers.

### 2.5 Marketing Email

**Campaign types:**
- **Sequences** — automated email sequences triggered by events (new client welcome, appointment follow-up, re-engagement, referral request)
- **Broadcasts** — one-time email announcements sent to selected segments

**Integration pattern:**
1. The application's campaign tables hold the campaign and its enrolled contacts
2. An hourly background task sends the next email of each enrolment through SES
3. Opens and clicks arrive as SES events (2.4)
4. Unsubscribes are handled automatically (2.4)

**Error handling:**
- Throttling → skip contact, retry on next hourly run
- API errors → log to `error_log`, continue with next contact
- Maximum 3 retries per contact per campaign run

### 2.6 Volume and Reputation Limits

Each client's sending is limited so that one client cannot harm the shared SES account ([[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)):

| Limit | Warning | Hard limit | At the hard limit |
|---|---|---|---|
| Marketing email | 20,000 a month | 25,000 a month | Marketing sends pause until the next month; booking, invoice and sign-in emails continue |
| All email | 40,000 a month | 50,000 a month | All sending except sign-in email pauses until the next month; the developer is notified |

- **Tenant reputation policy:** each client's SES tenant carries SES's standard reputation policy. When that client's bounce or complaint rate reaches the policy's pause level, SES pauses that client's sending alone. App 5 notifies the client and the developer.
- **Account alarms:** two AWS CloudWatch alarms on Mybizz's SES account warn the developer at a 4% bounce rate and a 0.08% complaint rate, below Amazon's review levels of 5% and 0.1%.

### 2.7 DNS Records

Written on the client's domain at onboarding: MX `inbound-smtp.eu-west-1.amazonaws.com`; the three DKIM CNAME records; MAIL FROM `mail.{domain}` with MX `feedback-smtp.eu-west-1.amazonses.com`; SPF `v=spf1 include:amazonses.com ~all`; DMARC `v=DMARC1; p=quarantine; adkim=r; aspf=r`.

---

## 3. Stripe Integration

### 3.1 Credentials

| Vault Key | Purpose |
|---|---|
| `stripe_secret_key` | Server-side payment processing |
| `stripe_webhook_secret` | Webhook signature verification |

**Public key** (safe for client-side): stored in `payment_config.stripe_publishable_key`

### 3.2 Payment Processing

**Flow:**
1. Client confirms booking
2. Server creates Stripe PaymentIntent
3. Client completes payment (Stripe Elements or redirect)
4. Stripe sends webhook to `/_/api/webhooks/stripe`
5. Webhook handler dispatches to background task
6. Background task updates booking status, generates invoice

**Test mode:** `payment_config.test_mode` flag. Test keys vs live keys distinguished by key prefix (`sk_test_` vs `sk_live_`).

### 3.3 Webhook Events

| Event | Action |
|---|---|
| `payment_intent.succeeded` | Mark booking CONFIRMED, generate invoice |
| `payment_intent.payment_failed` | Mark booking failed, notify customer |

**Webhook URL:** `[base_url]/_/api/webhooks/stripe`
**Signature verification:** Required on every webhook. See [[[default:adr-global/adr-webhook-architecture|Webhook Architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md) ADR.

### 3.4 Error Handling

| Error | Action |
|---|---|
| Card declined | Show error to customer, allow retry |
| API timeout | Retry once, then fail booking gracefully |
| Invalid API key | Log to `error_log`, alert owner via notification |
| Webhook signature failure | Return HTTP 400, log to `webhook_log` |

---

## 4. PayPal Integration

PayPal is an optional second payment method beside the card gateway. The integration is PayPal's standard checkout: PayPal's JavaScript buttons for the buyer's approval, and PayPal's Orders API v2 called from server code for every money operation. PayPal's invoicing and subscription products are not used; invoices are the application's own.

### 4.1 Availability

PayPal is offered only when the system currency is one of PayPal's supported currencies (AUD, BRL, CAD, CNY, CZK, DKK, EUR, HKD, HUF, ILS, JPY, MYR, MXN, TWD, NZD, NOK, PHP, PLN, GBP, RUB, SGD, SEK, CHF, THB, USD). For any other currency (for example ISK), Settings shows PayPal as unavailable, with the reason.

### 4.2 Credentials

| Where | Value | Purpose |
|---|---|---|
| `payment_config` | `paypal_client_id` | Loads PayPal's buttons in the browser (public) |
| Vault | `paypal_client_secret` | Server calls to PayPal's API |
| Vault | `paypal_webhook_id` | Webhook signature verification |

### 4.3 Setup

1. The Owner opens a PayPal Business account and creates a REST app in PayPal's developer dashboard.
2. The Owner enters the client ID in Settings and the secret in the Vault.
3. The application registers its own webhook with PayPal's Webhooks API, at `[base_url]/_/api/webhooks/paypal`, for the events in 5.5, and stores the returned webhook ID in the Vault. The Owner has no webhook step.
4. `paypal_test_mode` selects PayPal's sandbox or live API. Demo apps always use the sandbox.

### 4.4 Checkout

1. One custom component, `PayPalButtonComponent`, loads PayPal's JavaScript SDK with the client ID, the system currency, `intent=capture` and the app language as `locale`, and renders PayPal's buttons.
2. **createOrder:** the button calls a server function with the record to be paid (booking, order, invoice or package). The server reads the amount from the database, never from the browser, and creates the order with `POST /v2/checkout/orders`, setting `reference_id` and `invoice_id` to the record's identity so PayPal refuses a duplicate.
3. **onApprove:** the button calls a server function with the order ID. The server captures with `POST /v2/checkout/orders/{id}/capture`, sending a `PayPal-Request-Id` header so a repeated call never captures twice. A `COMPLETED` capture is recorded by the payment service, with PayPal's fee from `seller_receivable_breakdown.paypal_fee` (section 6).
4. **onCancel or onError:** the customer sees a message in the app language; the record stays unpaid (a pending booking keeps its hold).
5. Pay links in emails (invoices, pending bookings) open the application's own pay page, which shows the same component beside the card option.

### 4.5 Webhook Events

| Event | Action |
|---|---|
| `CHECKOUT.ORDER.APPROVED` | Capture the order when the browser closed before capture |
| `PAYMENT.CAPTURE.COMPLETED` | Confirm the payment (recorded once) |
| `PAYMENT.CAPTURE.PENDING` | Record the payment as pending |
| `PAYMENT.CAPTURE.DENIED` | Mark the payment failed |
| `PAYMENT.CAPTURE.REFUNDED` | Confirm the refund |
| `CUSTOMER.DISPUTE.CREATED` | Notify the Owner |

**Webhook URL:** `[base_url]/_/api/webhooks/paypal`
**Signature verification:** PayPal's verify-webhook-signature call with `paypal_webhook_id`, as [[[default:adr-global/adr-webhook-architecture|Webhook Architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md) sets out.

### 4.6 Refunds

A full or partial refund is made from the application through the payment service with `POST /v2/payments/captures/{capture_id}/refund` and a `PayPal-Request-Id` header. The `PAYMENT.CAPTURE.REFUNDED` webhook confirms it.

---

## 5. Gateway-Agnostic Service Layer

Stripe and PayPal use the same underlying service interface. Stripe is the card gateway; PayPal is switched on or off beside it in Settings.

**Service interface:**
```python
def create_payment(amount, currency, description, metadata) -> dict
def verify_payment(payment_id) -> dict
def refund_payment(payment_id, amount=None) -> dict
```

Switching PayPal on or off does not require reconfiguring services or bookings. The service layer routes each payment to the gateway the customer chose: a card payment to Stripe, a PayPal payment to PayPal.

**Accounting:** every payment and refund, by any gateway or recorded by hand, is one row in the payments table, which the application's accounts read. The gateway's fee for each payment is recorded on the payment's row (`gateway_fee`), taken from the gateway's own response: Stripe's balance transaction, PayPal's `paypal_fee`. Accounts show the gross payment as income and the fee as an expense.

**Language:** Stripe Elements and PayPal's buttons are given the app language as `locale`.

---

## 6. Secret Management

All integration secrets follow the two-level model defined in [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md):
1. **Anvil Secrets** holds exactly one item: `encryption_key`
2. **Vault** holds all integration credentials (Amazon SES, Stripe, PayPal, R2)
3. **`payment_config`** holds only publishable keys (safe for client-side)
4. **`email_config`** holds only sender name and email (not credentials)

**Enforcement:** Any server function that saves payment config must assert that secret key columns are not present. See [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md) §2.

---

## 7. Integration Error Logging

All integration failures are logged to the `error_log` table with:

- `function_name` — the integration function that failed
- `error_type` — exception class
- `error_message` — error details
- `severity` — "error" for transient failures, "critical" for configuration failures

---

## 8. Three-Tier Email Architecture

Email communications are deliberately classified into three distinct tiers, each using a
separate stream appropriate to its purpose:

| Tier | Purpose | Mechanism | Examples | Sender identity |
|---|---|---|---|---|
| 1 — System | Sign-in and account email | Anvil's Users service through SES (Custom Mail Server) | Login confirmations, password resets, email verification | Client's business domain (noreply) |
| 2 — Transactional | Business-operational, client's identity | SES API, transactional stream | Booking confirmations, reminders, invoices, payment receipts | Client's business domain |
| 3 — Marketing | Campaign sequences, newsletters | SES API, marketing stream | Broadcast emails, automated sequences, newsletters | Client's business domain |

**Tier 3 additional requirements:**
- Unsubscribe management per contact
- Open and click tracking
- Campaign performance reporting
- Separation from transactional stream (marketing failures do not block transactional delivery)

This tier model ensures transactional delivery reliability is never compromised by marketing
volume or reputation issues.

---

## 9. Client Domain Protection

Each client's website record is proxied through Cloudflare, in the client's own Cloudflare account, with Cloudflare's free web application firewall managed rules, DDoS protection and bot blocking switched on. App 5 writes the record through the Cloudflare API at onboarding ([[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) Step 10). The email records (2.7) stay unproxied, because mail cannot pass through Cloudflare's proxy. Cached public pages also lower the container's data transfer.

---

## 10. Mybizz's Own Integrations

These serve Mybizz-Live Ltd, not client instances, and are used by App 5 only:

| Service | Use | Decision |
|---|---|---|
| Paddle | Client subscriptions and billing | [[[default:specifications-global/spec-client-billing\|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) |
| FreeAgent | Read-only: tax and accounts deadlines, Corporation Tax returns, the Wise bank feed check, monthly income and costs | [[[default:adr-global/adr-freeagent-integration]]](C:/dev/project-library-global/adr-global/adr-freeagent-integration.md) |
| DigitalOcean | Provisioning, releases, resizing and checks | [[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) |
| Groq | AI and voice for every client, with an organisation spend limit of £1,700 a month and alerts at 50%, 75% and 90% | [[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md) |

