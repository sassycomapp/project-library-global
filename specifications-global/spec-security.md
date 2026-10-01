---
title: "spec-security"
doc-id: "mb-d16f800e"
updated: "2026-10-01"
---
# PDLF Standards Library — Security Specification

**Location:** `C:\dev\project-library-global\specifications-global\spec-security.md`
**Vault System:** [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md) — the single authoritative Vault document.
**Scope:** Project-agnostic security patterns. A project's specific role limits, regulatory
posture, and implementation details belong in that project's own canonical security document.

---

**The Vault System:** The two-level secrets model, enforcement/masking pattern, and Vault implementation are now the single authoritative document [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md). This file does not duplicate that content — reference [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md) for all Vault-related patterns.

## 1. RBAC and Data Access

- Every server function operating on application data carries an RBAC decorator.
- Role enforcement is always server-side. Client-side navigation visibility is a UX convenience
  only.
- All Data Tables are set to "No access" for client code — all data access goes through server
  functions.

## 2. Rate Limiting

Enforce via a Data Table, not an in-memory counter, so limits survive server restarts and work
across a multi-server environment.

## 3. Shared Numeric Security Standards

| Standard | Value |
|---|---|
| Password minimum length | 8 characters |
| Password complexity | At least one uppercase, one lowercase, one number |
| Rate limit — unauthenticated | 10 requests/minute/IP |
| Rate limit — authenticated | 100 requests/minute/user |
| Session inactivity timeout | 30 minutes |
| Audit log retention | 2 years |

---

*Security Specification v1.1 — Vault content (two-level secrets model, enforcement/masking) moved to [[[default:specifications-global/spec-vault-system|Vault System Specification]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md). Remaining content: RBAC/data access, rate limiting, shared numeric security standards.*
