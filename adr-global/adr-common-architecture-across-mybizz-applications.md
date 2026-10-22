---
title: "adr-common-architecture-across-mybizz-applications"
updated: "2026-10-22"
doc-id: "mb-035ff93b"
---
# `common-architecture-across-mybizz-applications` ADR — Mybizz Applications Share Everything They Can

**Status:** Accepted
**Date:** 2026-10-21
**Applies to:** Every Mybizz application: `mb-3-cs`, `mb-4-ecom` and every later one
**Authority:** [[[default:policy-global/pol-common-aspects-for-mybizz-anvil-applications|Common Aspects for Mybizz Anvil Applications]]](C:/dev/project-library-global/policy-global/pol-common-aspects-for-mybizz-anvil-applications.md) policy

---

## Context

Mybizz builds several applications, each its own Mybizz business: `mb-3-cs` for consulting and services businesses, `mb-4-ecom` for e-commerce businesses, and others to follow. They differ in their business domain: `mb-3-cs` centres on scheduling and bookings, `mb-4-ecom` on catalogue, cart and orders. Underneath, they need the same things: the five-app structure, client isolation, secrets, payments, webhooks, email, storage, management and compliance.

Built separately, the same need would be solved differently in each application. Each difference doubles maintenance, stops lessons from carrying over, and makes PDLF's steps branch by application.

---

## Decision

1. **Whatever can be common between Mybizz applications is kept common.** Each common aspect is defined once, in `project-library-global`, and implemented the same way in every application.
2. **The common aspects are listed in** [[[default:policy-global/pol-common-aspects-for-mybizz-anvil-applications|Common Aspects for Mybizz Anvil Applications]]](C:/dev/project-library-global/policy-global/pol-common-aspects-for-mybizz-anvil-applications.md).
3. **An application deviates from a common aspect only where its business domain requires it.** The deviation and its reason are recorded as an ADR in that application's project library.
4. **The rule works in both directions.** An improvement to a common aspect made while building one application is written back to `project-library-global` and applied to every other application in its next release. Neither `mb-3-cs` nor `mb-4-ecom` is the master of the other.
5. **A project library holds only what is particular to its application.** Anything it holds that is common moves to `project-library-global`.

---

## Why

- **One method.** PDLF builds every application the same way, and its steps do not branch by application.
- **One maintenance.** A common aspect fixed once is fixed for every application.
- **Lessons carry over.** What one application teaches improves the others.
- **Minimal deviation.** Every difference between applications is deliberate and recorded, never accidental.

---

## Consequences

- PDLF's Step 12 states what an application shares and what is particular to it; Step 15 checks the plan against the common aspects; Steps 34 and 37 check the built code against them.
- A lesson about a common aspect, captured at Step 46, is written to `project-library-global`.
- Content in `project-library-global` that is particular to one application moves to that application's project library.

---

*End of `common-architecture-across-mybizz-applications` ADR*
