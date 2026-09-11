---
document: "Threat Model — Broken Access Control Within a Client Instance"
doc-id: sec-broken-access-control-within-instance
state: Live
date-created: 2026-08-27
category: threat-models
---

# Threat Model — Broken Access Control Within a Client Instance

**Scope note, stated first, to avoid confusion with a different, already-solved problem:** this is NOT cross-client data exposure. Cross-client isolation is structural — separate Anvil app, separate database, per client instance, per `[[spec-five-app-architecture-model]]`. Architecturally impossible to breach from application code. This document concerns a different, real risk: one user seeing or changing another user's own role-scoped data *within the same client instance*.

## Applicable Threat

An AI-implemented server function omits, or incorrectly implements, the ownership check for role-scoped data. Example: a Staff member's own-bookings query returns another Staff member's bookings too. A Customer's own-invoices query returns another Customer's invoice. The vulnerability class is Broken Access Control (OWASP #1) — not a secrets leak, not a platform gap. It is application logic, written by an agent that does not personally verify its own output.

## Security Requirement

Every server function returning or modifying role-scoped data must derive the scope from the authenticated user's own server-side identity, never from a client-supplied identifier. Client-side filtering is a UX convenience only — per `[[spec-security]]` §1, all data access goes through server functions, and role enforcement is always server-side.

## Approved Pattern

```python
@anvil.server.callable
@require_role('staff')
def get_my_bookings():
    user = anvil.users.get_user()
    return app_tables.bookings.search(assigned_staff=user)
```

Scope is derived from `anvil.users.get_user()`, server-side, not from any argument the client passed in.

## Prohibited Pattern

```python
@anvil.server.callable
@require_role('staff')
def get_bookings(staff_id):
    return app_tables.bookings.search(assigned_staff=staff_id)
```

`staff_id` is accepted directly from the client and used to filter data, with no check that it matches the requesting user's own identity. Any Staff-role user could pass another Staff member's ID and receive their bookings.

**Exception:** this pattern is correct, not prohibited, for roles the RBAC table explicitly grants broader access — Owner (full access) and Manager (operational management across bookings/customers), per `[[spec-security-architecture]]` §1. The prohibition applies to roles scoped to their own data only (Staff, Customer).

## Implementation Guidance

- Every server function handling role-scoped data carries the RBAC decorator per `[[spec-security]]` §1, AND derives ownership server-side via `anvil.users.get_user()`.
- A function accepting a client-supplied identifier for "whose data" is a signal to check: does this role's own RBAC entry actually permit accessing other users' data? If not, the identifier should not exist as a parameter at all — scope comes from the authenticated user, not an argument.

## Verification Requirements

For each RBAC-scoped Data Table: log in as User A (a role scoped to own-data-only), attempt to access or modify User B's own-scoped record via the relevant server function, confirm the call is rejected or returns nothing. Repeat for every role scoped to own-data-only (Staff, Customer) against every table it touches.

## Authoritative Sources

- `[[spec-security]]` §1 — RBAC and Data Access
- `[[spec-security-architecture]]` §1 — RBAC Role Limits
- `[[spec-five-app-architecture-model]]` — confirms cross-client isolation is a separate, already-solved problem; this document does not duplicate that scope

## Known Exceptions

Owner and Manager roles' broader access, per the RBAC table, is by design — not a violation of this document's rule.

## Lessons Learned

None yet. Populated as real findings occur.
