---
document: "Threat Model — Authentication and Session Threats"
doc-id: sec-authentication-session
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Authentication and Session Threats

## Applicable Threat

Weak password policy, session tokens that never expire, or a login/session mechanism an AI agent implements slightly wrong — e.g. a session check that passes when it shouldn't, or a password reset flow that leaks whether an email address exists in the system.

## Security Requirement

Real, existing numeric standards already apply and are binding, per `spec-security.md` §3: password minimum length 8 characters, at least one uppercase/lowercase/number, session inactivity timeout 30 minutes. Every server function requiring a logged-in user must verify this server-side, never trust a client-side "is logged in" flag alone.

## Approved Pattern

```python
@anvil.server.callable
def get_my_invoices():
    user = anvil.users.get_user()
    if user is None:
        raise anvil.server.PermissionDenied()
    return app_tables.invoices.search(customer=user)
```

Session validity checked server-side, every call, via `anvil.users.get_user()` — not cached or assumed from a prior check.

## Prohibited Pattern

```python
@anvil.server.callable
def get_my_invoices(is_logged_in, customer_id):  # trusts client-asserted state
    if is_logged_in:
        return app_tables.invoices.search(customer=customer_id)
```

Trusting a client-supplied flag or identifier for authentication state, instead of checking the real, server-side session.

## Implementation Guidance

- Never accept a boolean or identifier from the client as proof of authentication.
- Password reset and login-failure messages must not reveal whether a given email address has an account — use identical wording for "wrong password" and "no such account."
- Session timeout (30 minutes) is enforced by Anvil's own session mechanism; confirm this has not been overridden or extended anywhere in code.

## Verification Requirements

- Attempt a role-scoped server call with no active session; confirm rejection.
- Attempt a password reset for a non-existent email; confirm the response is identical to a valid email's response.
- Confirm no server function accepts a client-supplied "am I logged in" or "which user am I" parameter as its sole authentication check.

## Authoritative Sources

- `spec-security.md` §1, §3 — RBAC/data access, shared numeric security standards

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
