---
title: "adr-tiers-model"
doc-id: "mb-beb7c182"
updated: "2026-11-12"
---
# Tiers Model
Status: Accepted

---

## Context

Every Mybizz application sells a subscription to its clients. Clients can also buy help with setup. The two must not be confused: one is the price of the product, the other is a one-off service.

Competitors sell in tiers, charge for extra staff and add-ons, and lock clients into contracts. Mybizz sells one offer that holds everything. The monthly plan matches the terms of Mybizz's hosting supplier, DigitalOcean: monthly billing, no contract and no lock-in. The annual plan rewards a client who commits for a year with two months free, and gives Mybizz a year's revenue up front.

---

## Decision

**Every Mybizz application has one price: £119 a month per client, or £1,190 a year on the annual plan, charged in the client's own currency.**

| Item | Rule |
|---|---|
| Price | £119 a month per client, before tax; charged at the fixed price for the client's currency (below) |
| Annual plan | 12 months for the price of 10: £1,190 a year, before tax, paid up front |
| Term | Monthly plan: month to month, with no contract and no minimum period. Annual plan: one year, renewed each year |
| Billing | Monthly or yearly, in advance, through Paddle as Merchant of Record ([[[default:specifications-global/spec-client-billing\|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md)) |
| Cancellation | At any time, effective at the end of the paid month or the paid year; no refund for part of a month or a year |
| Features | Every feature of the application; no tiers |
| Staff | Unlimited staff logins |
| Add-ons | None; nothing is sold on top of the subscription |
| Hosting | Each client instance on its own container and its own database, included in the price ([[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)) |
| Trial | None; prospects use the demo apps ([[[default:adr-global/adr-no-free-trial\|No Free Trial]]](C:/dev/project-library-global/adr-global/adr-no-free-trial.md)) |

### Price in each currency

Mybizz's reference currency is the pound sterling (GBP). Each market pays a fixed, round price in its own currency, close to £119. The annual price is always 10 times the monthly price.

| Currency | Markets | Monthly price, before tax | Annual price, before tax |
|---|---|---|---|
| GBP | United Kingdom | £119 | £1,190 |
| USD | United States | $149 | $1,490 |
| CAD | Canada | C$199 | C$1,990 |
| EUR | European Union, Norway, Iceland | €139 | €1,390 |
| CHF | Switzerland, Liechtenstein | CHF 139 | CHF 1,390 |

### Setup services

- **Self-setup** with the onboarding wizard and help videos: included.
- **Assisted setup:** one month's subscription, once, in the client's currency: £119. Mybizz sets up the instance with the client.
- Setup services are separate from the subscription and never change its price or features.

### Referral credit

- A client on the annual plan that refers a new client, which then buys the annual plan, earns one credit.
- Each credit takes one month's price off the referring client's next annual renewal.
- A renewal carries at most 5 credits. The referring client then still pays more than its yearly cost to Mybizz: the container, usage and a share of the database, about £293 a year.
- Credits not used at a renewal are not carried forward. A credit is never paid out in cash.
- A referral by or to a client on the monthly plan earns no credit.

### Architectural rules

1. The application holds no tier logic, feature limits or staff limits.
2. The client registry in Mybizz_management records the subscription status, the plan (monthly or annual), whether assisted setup was bought, which client referred the client, and the credits earned for the next renewal.
3. A price change is a business decision recorded here; it needs no code change.

---

## Consequences

### Positive
- One offer to explain, sell and support
- No tier, feature-limit or upgrade code to build or test
- No lock-in: the client stays because the product is worth it

### Negative
- Each client's container and database put a hosting cost on Mybizz from the first day
- The price must cover that hosting cost for every client; break-even is 9 clients ([[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md))
- An annual plan earns 10 months' revenue for 12 months of hosting

### Neutral
- No effect on the technical architecture beyond the client registry

---

## Related Documents

- [[[default:specifications-global/spec-onboarding-implementation-plan|Onboarding System — Engineering Plan]]](C:/dev/project-library-global/specifications-global/spec-onboarding-implementation-plan.md) — Onboarding flow
- [[[default:adr-global/adr-no-free-trial|No Free Trial]]](C:/dev/project-library-global/adr-global/adr-no-free-trial.md) — The demo apps
- [[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) — How the subscription is billed and collected
