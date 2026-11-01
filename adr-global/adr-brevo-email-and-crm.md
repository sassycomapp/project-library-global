---
title: "adr-brevo-email-and-crm"
doc-id: "mb-9399478f"
updated: "2026-11-01"
---
# Amazon SES for Email; CRM Built In
Status: Accepted (replaces the earlier Brevo decision; the file name is kept so existing links hold)

---

## Context

Every Mybizz application receives and sends email on the client's own domain: a shared inbox, transactional email (booking confirmations, reminders, invoices), marketing email and system email (sign-in, password reset). It also keeps a contact database with interaction history and a deal pipeline.

An outside email-and-CRM product per client means a second account the client must open, a second set of credentials, plan limits that change, and contacts held outside the application.

---

## Decision

1. **Amazon SES is the single email service in every Mybizz application,** for every email received and sent. Mybizz holds one AWS account and gives each client its own SES tenant, domain identity and scoped keys, created by Mybizz_management at provisioning. SES runs in `eu-west-1`.
2. **Anvil's Users service sends its system email through SES** too, with Anvil's Custom Mail Server set to the SES SMTP endpoint.
3. **The CRM is built into the application:** contacts, interaction history, deals and campaigns are the application's own tables ([[[default:adr-global/adr-single-contacts-table|Single Contacts Table]]](C:/dev/project-library-global/adr-global/adr-single-contacts-table.md)). No outside CRM is integrated.
4. **Brevo and Zoho are not used.** Any reference to them in a document, rule or code is an error and is corrected.

---

## How it works

| Concern | Means |
|---|---|
| Received email | MX record on the client's domain → SES → the client's S3 prefix → SNS → the instance's `/_/api/email/inbound` |
| Transactional and marketing email | SES API from the instance's email service module |
| System email (sign-in, password reset) | Anvil's Users service, Custom Mail Server: `email-smtp.eu-west-1.amazonaws.com`, port `587` (STARTTLS) |
| Deliveries, bounces, complaints, opens, clicks | SES → SNS → the instance's `/_/api/email/events` ([[[default:adr-global/adr-webhook-architecture\|Webhook Architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md)) |
| Unsubscribe | The instance's `/_/api/email/unsubscribe` |

### DNS records on the client's domain

Written by Mybizz_management through the client's Cloudflare DNS, or copied by the Owner into another DNS provider:

| Record | Value |
|---|---|
| MX | `inbound-smtp.eu-west-1.amazonaws.com` |
| DKIM | The three CNAME records SES gives for the identity |
| MAIL FROM | `mail.{domain}`, MX `feedback-smtp.eu-west-1.amazonses.com` |
| SPF | `v=spf1 include:amazonses.com ~all` |
| DMARC | `v=DMARC1; p=quarantine; adkim=r; aspf=r` |

### Vault credentials

| Vault key | Purpose |
|---|---|
| `aws_access_key_id`, `aws_secret_access_key` | SES sending and the client's received-email prefix in S3 |
| `ses_smtp_password` | Anvil's Custom Mail Server |

All three are written by Mybizz_management. The SMTP host and port are the same for every client and are not stored in the Vault.

---

## Why

- **One service for every email,** on the client's own domain, with no account for the client to open.
- **Contacts stay in the application,** in the client's own database, and leave with the client at exit.
- **Cost per email is low and predictable;** there is no per-client plan to outgrow.
- **Isolation:** one SES tenant per client, so one client's sending reputation does not affect another's.

---

## Consequences

- Mybizz requests SES production access once, for its AWS account.
- Each client's bounce and complaint rates are watched in Mybizz_management; a client above the thresholds has its marketing email paused.
- The library used for SES on Anvil's server Python is confirmed before the first step that uses it.
- Every application's email code calls SES only through one service module, so it can be replaced in tests.
