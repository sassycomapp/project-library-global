---
document: "Database Access Control"
doc-id: sec-database-access-control
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Database Access Control

## Applicable Threat

This project runs multiple real, separate PostgreSQL instances — the PDLF ledger (`pdlf` database, `pdlf_agent` role), GBrain's own database, and the memory governor's own database. A role with broader access than it needs, or a credential reused across instances, would let a compromise of one system reach another it was never meant to touch.

## Security Requirement

Each database instance has its own, separately scoped role with the minimum privilege that instance's writer actually needs. Credentials are never shared across instances. Confirmed real precedent: the memory governor's own RLS enforcement, live-tested, correctly blocked the `ledger_writer` role from inserting `override`-type events it wasn't scoped for.

## Approved Pattern

Role-per-instance, privilege-scoped to that instance's actual writers — the same pattern already built and verified for the memory governor's `ledger_writer` role.

## Prohibited Pattern

A single, broadly-privileged database role used across multiple unrelated systems, or a role granted superuser/owner privileges when only insert/update on specific tables is actually needed.

## Implementation Guidance

Before granting a new role any privilege, confirm it matches exactly what that specific writer needs — no broader "just in case" grants.

## Verification Requirements

For each real database role, confirm it can perform only its intended operations, and confirm attempting an out-of-scope operation is rejected — the same live-test discipline already applied to `ledger_writer`.

## Authoritative Sources

- `spec-postgres-ledger.md` — PDLF ledger connection and schema
- Memory governor's own live RLS test (this session)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
