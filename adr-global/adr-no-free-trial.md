---
title: "adr-no-free-trial"
doc-id: "mb-4d9be554"
updated: "2026-10-23"
---
# No Free Trial

**Status:** Accepted

---

## Context

A Mybizz application does nothing useful until it is fully configured: Vault, payment gateway credentials, Brevo, business profile and services must all be set up first. A free trial on Anvil's free tier would also lack background and scheduled tasks, so reminders, campaign enrollment and other core features would not work. A trial would show prospective clients a crippled, misleading product.

---

## Decision

**No Mybizz application offers a free trial.**

| Need | How it is met |
|---|---|
| A prospective client wants to see the product | A live guided demo on Mybizz's own fully configured instance |
| A new client needs help getting started | A 30-minute guided onboarding session after signup |
| A new client wants confidence before committing | A 30-day money-back guarantee on the first paid subscription |

Every paying client receives a properly provisioned instance on their own Anvil account, on the Hobby plan, from the first day. No client instance ever runs on Anvil's free tier.

---

## Consequences

- ✅ Every client instance has full feature access from the first day, including background and scheduled tasks
- ✅ The demo shows the real product
- ✅ One provisioning process for every client; no trial-to-paid transition
- ⚠️ Mybizz maintains a well-configured demo instance
- ⚠️ The money-back guarantee terms are defined and shown clearly at signup

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Provisioning process applies to all clients from day one |

