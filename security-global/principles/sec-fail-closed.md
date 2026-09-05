---
document: "Principle — Fail Closed"
doc-id: sec-fail-closed
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Fail Closed

## Statement

When a security check cannot be performed, or its result is uncertain, the default action is to deny — never to allow and hope the omission is caught later.

## Real Precedent in This Project

- `task` tool denial removes the tool from the model's visible set entirely, rather than attempting a check-then-allow approach that could be bypassed if the check itself failed.
- Sentinel's own ESCALATE outcome — when there isn't enough evidence to decide, the result is a stop-and-ask, not a default clear, per `sentinel-security-system-plan.md` Section 6.
- `mb-submit-memory`'s own rule: if the governor's API is unreachable, the skill stops and reports rather than proceeding or retrying silently.

## Why This Matters

A system that defaults to "allow" when uncertain will, over time, allow exactly the cases that were never actually checked. Defaulting to "deny" means an uncertain case is caught and reviewed, not silently passed through.

## Application

For any check that can fail, time out, or be inconclusive, the default outcome on that failure must be denial or a stop, never a pass.

## Known Exceptions

None identified.
