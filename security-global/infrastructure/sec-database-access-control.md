---
title: "sec-database-access-control"
doc-id: "mb-53d4575a"
updated: "2026-11-11"
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

### Client instance databases

Each Mybizz business's client databases sit in one DigitalOcean Managed PostgreSQL cluster (`[[spec-client-instance-hosting]]` §4):

- **One user per client,** able to reach only that client's database.
- **Limits on each user:** a connection limit of 3, a statement timeout of 60 seconds and an idle-in-transaction timeout of 120 seconds, so one client's heavy use cannot slow every other client (`[[adr-fair-use-limits]]`).
- **Trusted sources:** the cluster accepts connections only from the business's client containers and its test client instance. A leaked database password cannot be used from outside DigitalOcean.
- **Encrypted connections:** every connection uses TLS with full certificate verification (`sslmode=verify-full`).
- **Created inside DigitalOcean:** client users and their limits are created by the provisioning job, which runs inside DigitalOcean (`[[sec-client-provisioning-security]]`).

## Verification Requirements

For each real database role, confirm it can perform only its intended operations, and confirm attempting an out-of-scope operation is rejected — the same live-test discipline already applied to `ledger_writer`.

For client instance databases, confirm: each client user is refused by every other client's database; each carries its three limits; and a connection attempt from outside DigitalOcean is refused.

## Authoritative Sources

- PDLF ledger connection and schema — specified in the PDLF (`spec-postgres-ledger.md` there)
- Memory governor's own live RLS test (this session)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
