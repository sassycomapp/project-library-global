---
document: "Principle — Defense in Depth"
doc-id: sec-defense-in-depth
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Defense in Depth

## Statement

A genuinely important control is enforced at more than one independent layer, so a failure or misconfiguration in one layer alone does not remove the protection entirely.

## Real Precedent in This Project

- `task` tool denial: enforced at native config, Cupcake policy, and a standing procedural review — three independent layers, per `structural-compliance-enforcement-architecture-v3.md` Section 6.1, deliberately designed so a mistake in one does not silently remove the others.
- Webhook and destructive-command handling: Cupcake policy and native permission config both independently check the same class of risk.

## Why This Matters

A single-layer control has a single point of failure. If that one layer is misconfigured, has a bug, or is bypassed, the entire protection disappears at once. Independent layers mean a failure in one is caught by another.

## Application

For any genuinely important control, ask: if this one mechanism failed silently, would anything else catch it? If not, a second, independently-implemented layer is needed.

## Known Exceptions

Not every control needs multiple layers — this applies specifically to controls where a silent failure would have serious consequences, not routine or low-stakes checks.
