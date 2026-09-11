---
document: "Principle — Least Privilege"
doc-id: sec-least-privilege
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Least Privilege

## Statement

Every role, credential, and process is granted the minimum access it needs to do its actual job — never more, never "in case it's needed later."

## Real Precedent in This Project

- RBAC: Owner (full access), Manager (operational, no Vault/financial config), Admin (bookings/customers only), Staff (own calendar only) — each role's access is explicitly bounded, per `[[spec-security-architecture]]` §1.
- Vault access restricted to Owner role only, with step-up authentication, per `[[spec-vault-system]]` §1.
- Database roles scoped per-instance, per-writer, per `[[sec-database-access-control]]` — confirmed live, `ledger_writer` correctly blocked from an operation outside its scope.

## Why This Matters

A credential or role with more access than it needs is a larger target — its compromise causes more damage than necessary. Every excess privilege is risk carried for no benefit.

## Application

Before granting any new access, ask: what is the minimum this specific role/process/credential actually needs to do its real job. Grant exactly that, nothing broader.

## Known Exceptions

None — this principle has no legitimate exception; broader access is always a specific, justified grant (e.g. Owner's full access), never a default.
