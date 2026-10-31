---
title: "adr-common-and-trade-modules"
doc-id: "mb-992d6531"
updated: "2026-10-31"
---
# `common-and-trade-modules` ADR — Every Mybizz Application Is a Common Part and a Trade Part

**Status:** Accepted
**Applies to:** Every Mybizz application: `mb-1-edu`, `mb-2-subs`, `mb-3-cs`, `mb-4-ecom`, `mb-5-hosp` and every later one

---

## Context

Mybizz builds five businesses, each its own application. Most of each application is the same in every business: sign-in and the second factor, roles and access rules, client instances, the management app, tiers, notifications, observability, legal documents, the test suite and the screens' layout. Only the trade differs: bookings for consulting, products and orders for e-commerce, courses for education, plans and renewals for subscriptions, rooms and tables for hospitality.

[[[default:adr-global/adr-common-architecture-across-mybizz-applications]]](C:/dev/project-library-global/adr-global/adr-common-architecture-across-mybizz-applications.md) keeps the common aspects common. This decision sets how an application is built so that its trade part can be taken out and another put in without touching the rest.

---

## Decision

1. **Every application has two parts.** The **common part** is what every Mybizz business needs. The **trade part** is the business's own trade.
2. **One direction only.** The trade part may use the common part. The common part never uses the trade part.
3. **Code.** Client code and server code each keep the common part and the trade part in separate Anvil packages.
4. **Data.** The data design keeps the common tables and the trade tables in separate groups. No common table holds a link to a trade table.
5. **Design.** From Step 12 on, every feature, table, glossary term and decision of a run is marked `common` or `trade`.
6. **Template.** When a business is finished, its `common` items that are not yet in the project template are made general and placed there.

---

## Why

- **Pluggable.** A trade part can be replaced without touching the common part, because nothing in the common part depends on it.
- **Built once.** The common part is designed, built and tested once and reused by every business.
- **Fast template work.** The marking done during design makes the common items easy to collect after each business.

---

## Consequences

- Steps 12, 15 and 16 mark every feature, table, term and decision `common` or `trade`.
- The scaffold (Phase D) creates separate common and trade packages in each app.
- A review that finds a common item using a trade item reports it as a finding.
