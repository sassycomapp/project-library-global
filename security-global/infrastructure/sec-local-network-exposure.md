---
document: "Local Network Exposure of Internal Services"
doc-id: sec-local-network-exposure
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Local Network Exposure of Internal Services

## Applicable Threat

Internal services in this environment — the memory governor's API, real PostgreSQL instances — could be exposed beyond the local machine if bound to the wrong network interface. Confirmed real, correct configuration this session: the governor's `uvicorn` process runs bound specifically to `127.0.0.1:8321`, not `0.0.0.0`, confirmed directly this session.

## Security Requirement

Every internal service that has no legitimate reason to be reached from outside this machine is bound explicitly to the loopback address, verified directly, not assumed from the launch command's intent.

## Approved Pattern

`--host 127.0.0.1` explicitly specified at launch, confirmed via `ss -tlnp` showing the bind address, exactly as done for the governor this session.

## Prohibited Pattern

Binding an internal-only service to `0.0.0.0` for convenience, or omitting the host flag and trusting a default that may not be loopback-only.

## Implementation Guidance

For any new internal service introduced to this environment, confirm its actual bind address directly, the same way the governor's was confirmed this session, rather than trusting the launch command's apparent intent.

## Verification Requirements

For each internal service, run `ss -tlnp` and confirm the listening address is `127.0.0.1`, not `0.0.0.0` or a real external interface, unless external access is a genuine, deliberate requirement.

## Authoritative Sources

- This session's own direct confirmation of the governor's bind address

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
