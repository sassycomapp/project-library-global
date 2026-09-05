---
document: "Development Environment Credential Hygiene"
doc-id: sec-development-environment-credential-hygiene
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Development Environment Credential Hygiene

## Applicable Threat

Real database and service credentials are stored in plaintext `.env` files across this development environment — confirmed directly, this session, reading `PGPASSWORD` from `C:\dev\dev-makepdlf\makepdlf-project-library\.env`. A `.env` file accidentally committed to git, or read by an unintended process, exposes the credential immediately.

## Security Requirement

`.env` files are never committed to a tracked repository. Every repository containing one must have it explicitly excluded via `.gitignore`, verified, not assumed.

## Approved Pattern

`.env` present locally, excluded from git tracking, read only by the specific processes that need it (e.g. the PowerShell bridge reading `PGPASSWORD` for a direct database connection).

## Prohibited Pattern

A `.env` file with no corresponding `.gitignore` entry, or a credential value hardcoded directly into a script instead of read from `.env` at runtime.

## Implementation Guidance

For every real `.env` file in this environment, confirm its parent repository's `.gitignore` actually excludes it — check directly, don't assume the standard pattern was applied.

## Verification Requirements

For each repository containing a `.env` file, run `git status` and confirm the file does not appear as trackable; check `git log` for the filename to confirm it was never previously committed.

## Authoritative Sources

- This session's own direct read of `spec-postgres-ledger.md`'s Connection table, confirming `.env`-based credential storage as the current, real pattern

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
