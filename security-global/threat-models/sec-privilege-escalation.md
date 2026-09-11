---
document: "Threat Model — Privilege Escalation"
doc-id: sec-privilege-escalation
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Privilege Escalation

**Scope note:** distinct from `[[sec-broken-access-control-within-instance]]`, which covers one user seeing *another user at the same role level's* own data (horizontal). This document covers a role gaining capabilities *above* its own level (vertical) — a Staff account acting as Admin, an Admin acting as Owner.

## Applicable Threat

A server function's role check is written to require "any logged-in user" or a broader role than actually intended, letting a lower-privileged role perform an action reserved for a higher one — e.g. a Staff account successfully calling a function meant for Manager-level operational management.

## Security Requirement

Every server function's role decorator matches the specific role(s) intended, per `[[spec-security-architecture]]` §1's role table — never a broader check "for convenience" during development that's left in place.

## Approved Pattern

```python
@anvil.server.callable
@require_role('manager', 'owner')
def approve_refund(booking_id):
    ...
```

Explicit, specific roles matching the RBAC table exactly.

## Prohibited Pattern

```python
@anvil.server.callable
@require_role()  # or a decorator checking only "is logged in"
def approve_refund(booking_id):
    ...
```

A role check broader than the RBAC table actually specifies for this action.

## Implementation Guidance

When a role check is written, cross-reference it directly against `[[spec-security-architecture]]` §1's role table for the specific action — never assume "logged in" is sufficient for anything beyond a role's own self-scoped data.

## Verification Requirements

Log in as each lower-privileged role in turn; attempt every higher-privileged action; confirm each is rejected.

## Authoritative Sources

- `[[spec-security-architecture]]` §1 — RBAC role limits

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
