---
title: "spec-client-activation-runbook"
doc-id: "mb-b575e9fd"
updated: "2026-11-01"
---
# Client Instance Activation Runbook

**Applies to:** Every new client onboarding. No exceptions. Complete all steps in order.

---

## Prerequisites

Before beginning activation:

- [ ] The client has registered, accepted the subscription terms ($150 a month, month to month) and paid the first month ([[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md))
- [ ] Mybizz_management has created the client record and the client reference number
- [ ] The client's primary contact email and phone number are recorded in Mybizz_management
- [ ] The client owns its domain
- [ ] The client has opened a free Cloudflare account in its own name, on its own email address, added a payment method, switched R2 on, added its domain to Cloudflare DNS, and invited Mybizz's Cloudflare user as a member with the roles R2 Admin and DNS
- [ ] `blank_client_template` is up to date with the current schema

---

## Phase 1 — Provision the Anvil Instance

### Step 1 — Clone blank_client_template

1. Open a new Anvil Business account for the client, owned by Mybizz and named after the client's business ([[[default:policy-global/pol-common-aspects-for-mybizz-anvil-applications|Common Aspects for Mybizz Anvil Applications]]](C:/dev/project-library-global/policy-global/pol-common-aspects-for-mybizz-anvil-applications.md))
2. Clone `blank_client_template` into that account
3. Rename the clone to the client identifier format: `[client-name]-{vertical}` (e.g. `acme-cs`)
4. Verify the clone contains:
   - [ ] Every Data Table of the released schema (empty)
   - [ ] Startup module present (one client module only — opens first form from master_template)
   - [ ] master_template set as dependency (current release)
   - [ ] No server modules of its own
   - [ ] No forms of its own
   - [ ] No Anvil Secrets set yet

### Step 2 — Set Anvil Secrets

In the new client instance, set the following in Anvil Secrets (IDE only):

- [ ] `encryption_key` — generate a new Fernet symmetric key; do not reuse from any other instance

> ⚠️ This is the only item that ever goes in Anvil Secrets. See [[[default:adr-global/adr-payment-security-boundary-vault|`payment-security-boundary-vault`]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) ADR and [[[default:specifications-global/spec-vault-system|The Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md).

### Step 3 — Set the Email Service

- [ ] In the instance's Users service, set Anvil's email to Custom Mail Server: `email-smtp.eu-west-1.amazonaws.com`, port `587` (STARTTLS); the password is the client's SES SMTP password from Step 5

---

## Phase 2 — Client Services (Mybizz_management)

### Step 4 — Client Storage

Mybizz_management:

1. Accepts the client's Cloudflare invitation
2. Creates the client's R2 bucket
3. Creates a token limited to that bucket and writes it into the instance's Vault (`r2_access_key_id`, `r2_secret_access_key`)

See [[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md).

### Step 5 — Client Email

Mybizz_management creates in Mybizz's AWS account, for this client only:

1. The client's SES tenant and domain identity
2. The receipt rule that stores the client's received email in the client's S3 prefix
3. The SNS topics that call the instance's `/_/api/email/inbound` and `/_/api/email/events`
4. AWS keys scoped to this client, written into the instance's Vault (`aws_access_key_id`, `aws_secret_access_key`, `ses_smtp_password`)

See [[[default:adr-global/adr-brevo-email-and-crm|Amazon SES for Email; CRM Built In]]](C:/dev/project-library-global/adr-global/adr-brevo-email-and-crm.md).

### Step 6 — Generate Management Token

1. Generate a unique Bearer token for this client instance (use a cryptographically secure method)
2. Store the token in the Mybizz_management client registry (encrypted field)
3. Store the token in the client instance's Vault (`app5_bearer_token`)

### Step 7 — Register in Client Registry

In Mybizz_management, complete the client registry entry:

| Field | Value |
|---|---|
| `client_id` | Unique identifier (e.g. UUID) |
| `app_name` | Anvil app name (e.g. `acme-cs`) |
| `base_url` | Client instance URL |
| `management_token` | Token generated in Step 6 (encrypted) |
| `subscription_status` | `active` |
| `plan` | $150 a month; whether assisted setup was bought |
| `onboarded_date` | Today's date |

### Step 8 — Verify Management Endpoints

Call the client instance's health endpoint to confirm it responds correctly:

```
GET [base_url]/management/health
Authorization: Bearer [management_token]
```

Expected: HTTP 200 with health payload.

- [ ] Health endpoint verified

---

## Phase 3 — Create Owner Account

### Step 9 — Create Owner User

In the client instance:

1. Create the Owner user account with the client's confirmed email address
2. Assign the `Owner` role
3. Confirm only one Owner account exists in the instance
4. The Owner sets their own password from the emailed link; no password is ever sent by email

> The Owner role is the only role with access to the Vault. On the first open of the Vault, the Owner enrols an authenticator app. See [[[default:specifications-global/spec-vault-system|The Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md).

---

## Phase 4 — Owner Setup

The Owner completes the onboarding wizard in the instance, helped by its help videos. A client that bought assisted setup ($200) does the wizard with Mybizz on a call.

### Step 10 — Domain

- [ ] The wizard's domain step has Mybizz_management write the client's DNS records through the Cloudflare API: the website record, MX `inbound-smtp.eu-west-1.amazonaws.com`, the three DKIM CNAME records, MAIL FROM `mail.{domain}` with MX `feedback-smtp.eu-west-1.amazonses.com`, SPF `v=spf1 include:amazonses.com ~all` and DMARC `v=DMARC1; p=quarantine; adkim=r; aspf=r`
- [ ] The instance's environment is switched to the client's domain
- [ ] SES shows the domain identity as verified

### Step 11 — Payment Gateway

The Owner enters the gateway keys in the Vault; Mybizz never handles them:

- [ ] `stripe_secret_key` and `stripe_webhook_secret`, or `paystack_secret_key`
- [ ] `paypal_client_secret` and `paypal_webhook_id`, if PayPal is used

The Owner registers the webhook URLs in each gateway's dashboard:

- **Stripe:** `[base_url]/_/api/webhooks/stripe` — `payment_intent.succeeded`, `payment_intent.payment_failed`, `customer.subscription.updated`, `customer.subscription.deleted`
- **Paystack:** `[base_url]/_/api/webhooks/paystack` — `charge.success`, `subscription.disable`, `invoice.payment_failed`
- **PayPal:** `[base_url]/_/api/webhooks/paypal` — `PAYMENT.CAPTURE.COMPLETED`, `PAYMENT.CAPTURE.DENIED`, `PAYMENT.CAPTURE.REFUNDED`

### Step 12 — Business Profile and Branding

- [ ] Business name
- [ ] Business address and contact details
- [ ] Logo uploaded
- [ ] Brand colours configured (if applicable)
- [ ] Time zone set (stored as IANA identifier; UTC used for all Data Table storage)
- [ ] Currency and locale settings confirmed

### Step 13 — Services and Team Setup

- [ ] At least one service category created
- [ ] At least one service created
- [ ] Team members invited (if applicable)

### Step 14 — Email Test

- [ ] A test email sent from the instance arrives
- [ ] A test email sent to an address on the client's domain arrives in the instance's inbox

---

## Phase 5 — Completion

### Step 15 — Send Welcome Communication

Send the client, through the instance's email:

- [ ] Welcome email
- [ ] Platform URL
- [ ] Link to the help videos
- [ ] The subscription terms: $150 a month, month to month, cancel at any time

### Step 16 — Internal Records

- [ ] Client activation date recorded in the client registry
- [ ] Subscription billing confirmed active
- [ ] Activation checklist filed in Mybizz_management

---

## Post-Activation Notes

- The client instance receives all master_template updates automatically — server logic, UI, and forms — as each release is pushed into master_template. No client action is required. The only exception is Data Table schema changes, which must be applied manually per instance in the Anvil IDE.
- Release notification emails are sent by Mybizz_management.
- The client never has access to the Anvil IDE. All management of the instance is through the application UI (Owner role) or through Mybizz_management.
- Schema migrations to this instance must be applied manually if the Data Table schema changes after activation. This includes new tables, new columns, modified columns, and deleted columns.

---

## Rollback

If activation cannot be completed (client withdraws, payment fails, technical blocker):

1. Delete the client instance app and close its Anvil account
2. Delete the client's R2 bucket; Mybizz's Cloudflare user leaves the client's Cloudflare account
3. Delete the client's SES tenant, identity, receipt rule, SNS topics and AWS keys, and empty the client's S3 prefix
4. Revoke the management token
5. Mark the client record as withdrawn in Mybizz_management, with the reason
