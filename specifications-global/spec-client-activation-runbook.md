---
title: "spec-client-activation-runbook"
doc-id: "mb-b575e9fd"
updated: "2026-11-08"
---
# Client Instance Activation Runbook

**Applies to:** Every new client onboarding. No exceptions. Complete all steps in order.

---

## Platform Set-Up (Once per Business)

Done once, before the business's first client, as [[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 7 sets out:

- [ ] The business's DigitalOcean project exists, in Mybizz's DigitalOcean account
- [ ] The business's Managed PostgreSQL cluster runs in `LON1`
- [ ] The business's repository exists in the Container Registry, holding the current release image
- [ ] The test client instance runs the current release image and passes its smoke test
- [ ] A DigitalOcean API token, scoped to the business's project, is in App 5's Vault
- [ ] The four conditions of section 10 of Client Instance Hosting are met

---

## Prerequisites

Before beginning activation:

- [ ] The client has registered, accepted the subscription terms ($99 a month, month to month) and paid the first month ([[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md))
- [ ] Mybizz_management has created the client record and the client reference number
- [ ] The client's primary contact email and phone number are recorded in Mybizz_management
- [ ] The client owns its domain
- [ ] The client has opened a free Cloudflare account in its own name, on its own email address, added a payment method, switched R2 on, added its domain to Cloudflare DNS, and invited Mybizz's Cloudflare user as a member with the roles R2 Admin and DNS
- [ ] The cluster has room for one more client (App 5's capacity view)

---

## Phase 1 — Provision the Client Instance

### Step 1 — Create the Instance

Mybizz_management's **New client** action:

1. Creates the client's database and database user in the business's cluster
2. Generates the client's `encryption_key` (a new Fernet symmetric key; never reused from any other instance) and the two container keys (`secret.key`, `anvil-live-object-key.txt`)
3. Creates the client's App Platform app, named in the client identifier format `[client-name]-{vertical}` (e.g. `acme-cs`), from the current release image, with every App Server setting of Client Instance Hosting section 3
4. Starts the container

Verify:

- [ ] The container runs the current release image
- [ ] Every table of the released schema exists in the client's database, empty
- [ ] The instance opens its first form from master_template

> ⚠️ `encryption_key` is the only App Secret. See [[[default:adr-global/adr-payment-security-boundary-vault|`payment-security-boundary-vault`]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) ADR and [[[default:specifications-global/spec-vault-system|The Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md).

### Step 2 — Set the Email Service

- [ ] The container's SMTP settings hold `email-smtp.eu-west-1.amazonaws.com`, port `587` (STARTTLS), and the client's SES SMTP credentials, which Mybizz_management sets in Step 5

### Step 3 — Confirm the Instance's Settings

- [ ] Every App Server setting of Client Instance Hosting section 3 is present in the container's encrypted environment values
- [ ] No value is shared with any other client instance

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
4. AWS keys scoped to this client, written into the instance's Vault (`aws_access_key_id`, `aws_secret_access_key`, `ses_smtp_password`); the SES SMTP credentials are also set as the container's SMTP settings

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
| `app_name` | App Platform app name (e.g. `acme-cs`) |
| `base_url` | Client instance URL |
| `management_token` | Token generated in Step 6 (encrypted) |
| `subscription_status` | `active` |
| `plan` | $99 a month; whether assisted setup was bought |
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
5. At first sign-in the Owner enrols a FIDO2 second factor: a security key or the device's passkey

> The Owner role is the only role with access to the Vault. On the first open of the Vault, the Owner enrols an authenticator app. See [[[default:specifications-global/spec-vault-system|The Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md).

---

## Phase 4 — Owner Setup

The Owner completes the onboarding wizard in the instance, helped by its help videos. A client that bought assisted setup ($200) does the wizard with Mybizz on a call.

### Step 10 — Domain

- [ ] The wizard's domain step has Mybizz_management write the client's DNS records through the Cloudflare API: the website record, MX `inbound-smtp.eu-west-1.amazonaws.com`, the three DKIM CNAME records, MAIL FROM `mail.{domain}` with MX `feedback-smtp.eu-west-1.amazonses.com`, SPF `v=spf1 include:amazonses.com ~all` and DMARC `v=DMARC1; p=quarantine; adkim=r; aspf=r`
- [ ] Mybizz_management adds the client's domain to the instance's App Platform app and sets the App Server's `origin` to it
- [ ] SES shows the domain identity as verified

### Step 11 — Payment Gateway

The Owner enters the gateway keys in the Vault; Mybizz never handles them:

- [ ] `stripe_secret_key` and `stripe_webhook_secret`, or `paystack_secret_key`
- [ ] `paypal_client_secret`, if PayPal is used; the application registers its PayPal webhook itself and stores `paypal_webhook_id` ([[[default:specifications-global/spec-integration|Integration Specification]]](C:/dev/project-library-global/specifications-global/spec-integration.md), section 5.3)

The Owner registers the Stripe or Paystack webhook URL in that gateway's dashboard:

- **Stripe:** `[base_url]/_/api/webhooks/stripe` — `payment_intent.succeeded`, `payment_intent.payment_failed`, `customer.subscription.updated`, `customer.subscription.deleted`
- **Paystack:** `[base_url]/_/api/webhooks/paystack` — `charge.success`, `subscription.disable`, `invoice.payment_failed`

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

### Step 14 — Legal Documents

The Owner is responsible for the content of all three documents ([[[default:adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture|Legal Policy Responsibility]]](C:/dev/project-library-global/adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md)).

- [ ] The Owner has reviewed the seeded clauses of the Privacy Policy, the Terms and Conditions and the Cookie Policy in the Clause Builder, and accepted or changed each one
- [ ] All three documents are published to their public pages
- [ ] The Owner's acknowledgement of responsibility is recorded
- [ ] The cookie banner shows on a first visit to the public site, and Refuse all loads no embedded content ([[[default:specifications-global/spec-legal-documents-and-consent|Legal Documents and Consent]]](C:/dev/project-library-global/specifications-global/spec-legal-documents-and-consent.md), section 12)

### Step 15 — Email Test

- [ ] A test email sent from the instance arrives
- [ ] A test email sent to an address on the client's domain arrives in the instance's inbox

---

## Phase 5 — Completion

### Step 16 — Send Welcome Communication

Send the client, through the instance's email:

- [ ] Welcome email
- [ ] Platform URL
- [ ] Link to the help videos
- [ ] The subscription terms: $99 a month, month to month, cancel at any time, effective at the end of the paid month

### Step 17 — Internal Records

- [ ] Client activation date recorded in the client registry
- [ ] Subscription billing confirmed active
- [ ] Activation checklist filed in Mybizz_management

---

## Post-Activation Notes

- The client instance receives every release — server logic, UI, forms and new tables and columns — when App 5's Release action moves it to the release image. No client action is required.
- Release notification emails are sent by Mybizz_management.
- The client has no access to the container, the database or the repositories. All management of the instance is through the application UI (Owner role) or through Mybizz_management.

---

## Rollback

If activation cannot be completed (client withdraws, payment fails, technical blocker):

1. Mybizz_management's **Remove** action deletes the client's App Platform app, database and database user
2. Delete the client's R2 bucket; Mybizz's Cloudflare user leaves the client's Cloudflare account
3. Delete the client's SES tenant, identity, receipt rule, SNS topics and AWS keys, and empty the client's S3 prefix
4. Revoke the management token
5. Mark the client record as withdrawn in Mybizz_management, with the reason
