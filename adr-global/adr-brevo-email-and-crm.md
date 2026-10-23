---
title: "adr-brevo-email-and-crm"
doc-id: "mb-9399478f"
updated: "2026-10-23"
---
# Brevo for Email and CRM
Status: Accepted

---

## Context

Every Mybizz application sends transactional email (booking confirmations, reminders, invoices), runs marketing email (sequences, broadcasts, lead capture) and keeps a contact database with interaction history and a deal pipeline. Every client starts on free tiers, so each of these must work on a free plan from the first day.

---

## Decision

**Brevo is the single platform for transactional email, marketing email and CRM in every Mybizz application.** No other email or CRM product is integrated.

System emails (sign-in links, password reset) use Anvil's built-in email service. They are platform-level emails, not controlled by the client, and are outside Brevo's scope.

---

## Why Brevo

The criteria are: a free tier that works from the first day, the client owning their own account, a start-free-upgrade-when-ready model, the simplest integration to maintain, and the best combined coverage of transactional email, marketing and CRM. Brevo meets all of them.

**Its free tier works from the first day:**
- 300 emails a day (9,000 a month), SMTP included, no credit card required
- 100,000 contacts stored
- Marketing automation workflows, full API access, open and click tracking, unsubscribe management
- A built-in CRM: contacts, interaction history, deals and pipeline

**One integration covers three concerns.** One platform, one set of credentials, one settings screen, one onboarding step. The client creates one Brevo account and connects it to Mybizz once.

**The client owns it.** Each client creates and manages their own Brevo account. Mybizz neither provisions nor administers it. When a client leaves Mybizz, the Brevo account and its contacts are entirely theirs.

**Upgrades need no code change.** SMTP credentials, the API key structure and the integration code are the same on every Brevo tier. Upgrading is between the client and Brevo.

**Rejected alternatives.** Google Workspace, Microsoft Outlook, SendGrid, Mailgun, Postmark and Zoho were assessed against the same criteria. Zoho is the cautionary case: its free mail plan has no SMTP access, so transactional email would not work for a new client, and splitting email, marketing and CRM across separate products multiplies credentials, settings and failure points.

---

## What Brevo Provides

| Concern | Brevo |
|---|---|
| Transactional email (SMTP) | Brevo SMTP relay |
| Marketing campaigns and automation | Brevo Campaigns and Automation |
| Contact database, interaction history, deal pipeline | Brevo CRM (built-in) |
| Contact sync from the application | Brevo API |
| System email (sign-in, password reset) | Anvil's built-in email |

---

## Vault Credentials

Two secrets per client instance:

| Vault key | Purpose |
|---|---|
| `brevo_smtp_key` | SMTP authentication for transactional email |
| `brevo_api_key` | REST API for CRM sync, campaigns, automation and webhooks |

**SMTP constants** (the same for every client, held in the transactional email service module, not in the Vault or the database):
- Host: `smtp-relay.brevo.com`
- Port: `587` (STARTTLS)

---

## Business Email Addresses

Mybizz does not provision business mailboxes (admin@clientdomain.com and the like). Clients use any mail provider they choose.

Brevo sends on behalf of the client's domain by SMTP relay or API. The from-address and display name are set in Brevo's sender settings. With DKIM and SPF records on the client's domain, email is sent authenticated from that domain; without them, Brevo sends from a @brevosend.com relay address. Domain authentication is the recommended setup, and Mybizz can guide clients through it during premium onboarding.

---

## Consequences

- Any reference to a Zoho product in a document, rule or code is an error and is corrected.
- Every application's email and CRM code calls Brevo only, through one service module, so it can be replaced in tests.
