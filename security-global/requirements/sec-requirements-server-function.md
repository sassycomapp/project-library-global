---
document: "Requirement — New Server Function"
doc-id: sec-requirements-server-function
state: Live
date-created: 2026-08-27
category: requirements
---
# Requirement — New Server Function

Maps to Sentinel's own step-intensity table, Step 35 (Build) — High scrutiny.

## Applicable Threat

A new server function is written without the baseline security checks any function touching real data must have, because those checks were never made an explicit, checkable requirement.

## Security Requirement

Before a new server function handling application data is considered complete, all of the following are explicitly true:

1. It carries the RBAC decorator appropriate to the roles allowed to call it, per `spec-security.md` §1.
2. If it returns or modifies role-scoped data, its scope is derived server-side, per `sec-server-side-authority.md` and `sec-broken-access-control-within-instance.md` — never from a client-supplied identifier, unless the calling role is explicitly permitted broader access.
3. If it reads a secret, it reads it via `get_vault_secret()`, never hardcoded, per `spec-vault-system.md`.
4. Any exception handler within it does not log the raw exception if the function touches a secret, per `sec-secret-exposure-response.md`.

## Approved Pattern

Each of the four items above checked explicitly, item by item, before the function is treated as done — not inferred from "it looks right."

## Prohibited Pattern

Marking a server function complete because it runs correctly in the happy-path case, without the four items above being explicitly confirmed.

## Implementation Guidance

This requirement is the concrete, checkable form of `sec-ai-agent-introduced-vulnerabilities.md`'s own general warning — a specific checklist, not just an abstract caution.

## Verification Requirements

For each new server function touching application data, confirm items 1–4 explicitly, individually.

## Authoritative Sources

- `sentinel-security-system-plan.md` Section 9 — Step 35
- `sec-server-side-authority.md`, `sec-broken-access-control-within-instance.md`, `spec-vault-system.md`, `sec-secret-exposure-response.md`

## Known Exceptions

Functions that touch no application data and no secret (e.g. a pure utility function) are exempt from items 2–3.

## Lessons Learned

None yet. Populated as real findings occur.
