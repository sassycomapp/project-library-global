---
document: "Principle — Simplicity as a Security Property"
doc-id: sec-simplicity-as-security-property
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Simplicity as a Security Property

## Statement

A simpler control that is correctly understood and consistently applied is more secure than a complex one that is partially understood or inconsistently applied. Minimum necessary complexity is not just an engineering preference — it is itself a security property.

## Real Precedent in This Project

- `sentinel-security-system-plan.md` Section 4: "five controls that genuinely work beats fifteen that don't" — the explicit, stated design principle behind the whole compliance architecture.
- The sub-agent delegation resolution: eliminating the capability entirely, rather than attempting a more complex, only-partially-reliable monitoring scheme, per `structural-compliance-enforcement-architecture-v3.md` Section 6.1.

## Why This Matters

Every additional layer of complexity is a new place a control can be misconfigured, misunderstood, or silently fail. A large number of partially-effective controls can create a false sense of security while leaving real gaps unnoticed.

## Application

Before adding a new control, ask: does this genuinely close a real gap, or does it add complexity without a proportional benefit? Prefer the simpler design that actually works over the more elaborate one that might.

## Known Exceptions

None — this principle applies as a standing test for every new control considered.
