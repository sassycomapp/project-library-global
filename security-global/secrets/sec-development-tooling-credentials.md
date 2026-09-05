---
document: "Development Tooling Credentials"
doc-id: sec-development-tooling-credentials
state: Live
date-created: 2026-08-27
category: secrets
---
# Development Tooling Credentials

**Scope note:** `spec-vault-system.md` governs secrets belonging to the *application* (e.g. mb-3-cs's own Stripe key). This document covers a distinct, real set: credentials belonging to the *development tooling itself* — `PGPASSWORD`, the memory governor's writer credentials (`manual_submission`, `pdlf_step_sync`, `self_healing`), GitHub push credentials. None of these live in any application's Vault; none should.

## Applicable Threat

Development-tooling credentials are real, powerful, and currently governed by no single document — each was handled ad hoc as it came up this session (`.env` files, governor `.env`, GitHub's own auth). No consolidated inventory of what they are or how they're protected currently exists.

## Security Requirement

Every real development-tooling credential in this environment is identified, its storage location confirmed, and its exposure risk assessed — the same rigor already applied to application secrets, applied here too.

## Approved Pattern

`.env`-based storage, excluded from git per `sec-development-environment-credential-hygiene.md`, read only by the specific process that needs it.

## Prohibited Pattern

A development-tooling credential hardcoded into a script, or stored with no corresponding `.gitignore` protection.

## Implementation Guidance

Build a real, explicit inventory of every development-tooling credential in this environment — confirmed real ones from this session alone: PDLF's `PGPASSWORD`, the governor's four writer credentials, GitHub push authentication. Confirm each one's storage location and exclusion from version control directly, not assumed from convention.

## Verification Requirements

For each real development-tooling credential, confirm its storage location and confirm it is excluded from any tracked repository.

## Authoritative Sources

- This session's own real credential handling: `spec-postgres-ledger.md`'s `.env`-based `PGPASSWORD`, the governor's own `.env`-based writer credentials

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
