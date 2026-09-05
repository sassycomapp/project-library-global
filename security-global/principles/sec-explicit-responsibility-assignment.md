---
document: "Principle — Explicit Responsibility Assignment"
doc-id: sec-explicit-responsibility-assignment
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Explicit Responsibility Assignment

## Statement

Every security control is explicitly assigned to a specific layer or party — the platform, the application code, a specific process. Nothing is left as an assumption that "something else" must be handling it.

## Real Precedent in This Project

- `sec-anvil-platform-responsibility-boundary.md` — built specifically because this exact ambiguity is a real risk: a control assumed to be Anvil's that was actually the application's responsibility, or the reverse.
- `sec-broken-access-control-within-instance.md`'s own scope note — explicitly distinguishing cross-client isolation (Anvil's responsibility, structural) from within-instance role separation (the application's responsibility, not automatic) — precisely to prevent this kind of unassigned gap.

## Why This Matters

A control nobody has explicitly claimed responsibility for is a control nobody is actually maintaining. It looks covered until the moment it matters.

## Application

For any new feature or system, every real security concern it touches should be traceable to an explicit owner — a named platform guarantee, or a named piece of application logic. If it can't be traced to either, it's an unassigned gap, not a covered one.

## Known Exceptions

None identified.
