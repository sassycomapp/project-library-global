---
title: "adr-no-free-trial"
doc-id: "mb-4d9be554"
updated: "2026-11-01"
---
# No Free Trial

**Status:** Accepted

---

## Context

A Mybizz application does nothing useful until it is configured: Vault, payment gateway, email domain, business profile and services. A trial instance would cost Mybizz a Business account for a prospect who may never pay, and would show a half-configured product.

---

## Decision

**No Mybizz application offers a free trial or a money-back guarantee.** Prospects use two demo apps instead.

| Demo app | What it holds | Use |
|---|---|---|
| `demo.{domain}` | A complete sample business with sample data | The prospect sees the product working, in every role |
| `try.{domain}` | An empty instance | The prospect sets up a business of their own with the onboarding wizard |

- Both run the current release, in demo mode: email goes only to the visitor's own address, payments use the gateways' test mode, and the Vault and account settings are read-only.
- Both are reset every night.
- Both run on Mybizz's own account; no client data is ever in them.

Every paying client receives its own instance on its own Mybizz-owned Anvil Business account from the first day.

---

## Consequences

- ✅ The prospect sees the real product, fully working, before paying
- ✅ One provisioning process for every client; no trial-to-paid transition
- ✅ No account is paid for a prospect who does not buy
- ⚠️ Every application builds demo mode and the nightly reset
- ⚠️ Mybizz keeps the sample business of `demo.{domain}` current with each release

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-tiers-model\|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) | The price and the setup services |
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Provisioning process applies to all clients from day one |
