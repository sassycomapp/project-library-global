---
document: "Principle — Server-Side Authority"
doc-id: sec-server-side-authority
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Server-Side Authority

## Statement

Client-supplied data is never trusted as the basis for a security decision. The server always independently determines identity, ownership, and permission — never accepts a client's assertion of any of these as fact.

## Real Precedent in This Project

- `[[sec-broken-access-control-within-instance]]` — scope derived from `anvil.users.get_user()`, never a client-supplied identifier.
- `[[sec-payment-manipulation]]` — amount computed server-side from the real record, never accepted as a client-supplied argument.
- `[[sec-authentication-session]]` — session validity checked server-side every call, never trusted from a client-side flag.
- `[[spec-security]]` §1 — role enforcement is always server-side; client-side navigation visibility is a UX convenience only.

## Why This Matters

Anything sent from the client can be altered by whoever controls that client — a browser, a direct API call, a manipulated request. If a security decision depends on client-supplied data, it depends on something the server cannot actually verify.

## Application

Before trusting any value in a security-relevant decision, ask: did this value originate on the server, or was it supplied by the client? If the client supplied it, it cannot be the basis for the decision.

## Known Exceptions

None — this principle applies universally to every security-relevant server function in this project.
