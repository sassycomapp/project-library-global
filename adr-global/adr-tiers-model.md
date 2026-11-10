---
title: "adr-tiers-model"
doc-id: "mb-beb7c182"
updated: "2026-11-10"
---
# Tiers Model
Status: Accepted

---

## Context

Every Mybizz application sells a subscription to its clients. Clients can also buy help with setup. The two must not be confused: one is the price of the product, the other is a one-off service.

Competitors sell in tiers, charge for extra staff and add-ons, and lock clients into contracts. Mybizz sells one offer that holds everything. The subscription terms match the terms of Mybizz's hosting supplier, DigitalOcean: monthly billing, no contract and no lock-in.

---

## Decision

**Every Mybizz application has one price: $99 a month per client.**

| Item | Rule |
|---|---|
| Price | $99 a month per client, before tax |
| Term | Month to month; no contract and no minimum period |
| Billing | Monthly, in advance, through Paddle as Merchant of Record ([[[default:specifications-global/spec-client-billing\|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md)) |
| Cancellation | At any time, effective at the end of the paid month; no refund for part of a month |
| Features | Every feature of the application; no tiers |
| Staff | Unlimited staff logins |
| Add-ons | None; nothing is sold on top of the subscription |
| Hosting | Each client instance on its own container and its own database, included in the price ([[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)) |
| Trial | None; prospects use the demo apps ([[[default:adr-global/adr-no-free-trial\|No Free Trial]]](C:/dev/project-library-global/adr-global/adr-no-free-trial.md)) |

### Setup services

- **Self-setup** with the onboarding wizard and help videos: included.
- **Assisted setup:** $200 once. Mybizz sets up the instance with the client.
- Setup services are separate from the subscription and never change its price or features.

### Architectural rules

1. The application holds no tier logic, feature limits or staff limits.
2. The client registry in Mybizz_management records the subscription status and whether assisted setup was bought.
3. A price change is a business decision recorded here; it needs no code change.

---

## Consequences

### Positive
- One offer to explain, sell and support
- No tier, feature-limit or upgrade code to build or test
- No lock-in: the client stays because the product is worth it

### Negative
- Each client's container and database put a hosting cost on Mybizz from the first day
- The price must cover that hosting cost for every client; break-even is two clients ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 11)

### Neutral
- No effect on the technical architecture beyond the client registry

---

## Related Documents

- [[[default:specifications-global/spec-onboarding-implementation-plan|Onboarding System — Engineering Plan]]](C:/dev/project-library-global/specifications-global/spec-onboarding-implementation-plan.md) — Onboarding flow
- [[[default:adr-global/adr-no-free-trial|No Free Trial]]](C:/dev/project-library-global/adr-global/adr-no-free-trial.md) — The demo apps
- [[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) — How the subscription is billed and collected
