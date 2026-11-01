---
title: "spec-integration"
doc-id: "mb-a1d9a710"
updated: "2026-11-01"
---
# Mybizz — Integration Specification

**Scope:** Mybizz-wide. Covers all external service integrations — Amazon SES (all email), Stripe and Paystack (card payments), PayPal (optional second payment method).

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

MX record on the client's domain → SES → the client's S3 prefix → SNS → `[base_url]/_/api/email/inbound` → a background task reads the email from S3, stores it in the instance and deletes it from S3.

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

### 2.6 DNS Records

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

## 4. Paystack Integration

### 4.1 Credentials

| Vault Key | Purpose |
|---|---|
| `paystack_secret_key` | Server-side payment processing |

**Public key** (safe for client-side): stored in `payment_config` table.

### 4.2 Payment Processing

**Flow:** Same as Stripe — create transaction, customer pays, webhook confirms.

**Currency:** Paystack processes in NGN, GHS, ZAR, KES, and other African currencies.

### 4.3 Webhook Events

| Event | Action |
|---|---|
| `charge.success` | Mark payment successful |
| `invoice.payment_failed` | Mark payment failed |

**Webhook URL:** `[base_url]/_/api/webhooks/paystack`

---

## 5. PayPal Integration

PayPal is an optional second payment method beside the card gateway.

### 5.1 Credentials

| Vault Key | Purpose |
|---|---|
| `paypal_client_secret` | Server-side order and capture calls |
| `paypal_webhook_id` | Webhook signature verification |

**Client ID** (safe for client-side): stored in `payment_config` table.

### 5.2 Webhook Events

| Event | Action |
|---|---|
| `PAYMENT.CAPTURE.COMPLETED` | Mark payment successful |
| `PAYMENT.CAPTURE.DENIED` | Mark payment failed |
| `PAYMENT.CAPTURE.REFUNDED` | Record the refund |

**Webhook URL:** `[base_url]/_/api/webhooks/paypal`
**Signature verification:** PayPal's verify-webhook-signature call with `paypal_webhook_id`.

---

## 6. Gateway-Agnostic Service Layer

Stripe, Paystack and PayPal use the same underlying service interface. The active card gateway is selected in Settings (`payment_config.active_gateway`); PayPal is switched on or off beside it.

**Service interface:**
```python
def create_payment(amount, currency, description, metadata) -> dict
def verify_payment(payment_id) -> dict
def refund_payment(payment_id, amount=None) -> dict
```

Switching gateways later does not require reconfiguring services or bookings. The service layer routes to the correct gateway based on `payment_config.active_gateway`.

---

## 7. Secret Management

All integration secrets follow the two-level model defined in [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md):
1. **Anvil Secrets** holds exactly one item: `encryption_key`
2. **Vault** holds all integration credentials (Amazon SES, Stripe, Paystack, PayPal, R2)
3. **`payment_config`** holds only publishable keys (safe for client-side)
4. **`email_config`** holds only sender name and email (not credentials)

**Enforcement:** Any server function that saves payment config must assert that secret key columns are not present. See [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md) §2.

---

## 8. Integration Error Logging

All integration failures are logged to the `error_log` table with:

- `function_name` — the integration function that failed
- `error_type` — exception class
- `error_message` — error details
- `severity` — "error" for transient failures, "critical" for configuration failures

---

## 9. Three-Tier Email Architecture

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

