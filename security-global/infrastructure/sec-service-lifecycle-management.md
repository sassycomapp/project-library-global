---
document: "Service Lifecycle Management"
doc-id: sec-service-lifecycle-management
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Service Lifecycle Management

## Applicable Threat

Critical services in this environment (the memory governor's API, its worker process) run as manually-started processes, not managed services. Confirmed real incident, this session: the governor was launched once without its `.env` loaded, silently unable to reach its database or resolve any writer credential, and had to be manually killed and relaunched. A security-relevant service can be down, or misconfigured, with nobody aware.

## Security Requirement

Before relying on any security-relevant service being active, its actual running state is verified directly — not assumed from a prior start command having been issued.

## Approved Pattern

Direct verification before use: `ss -tlnp` to confirm the process is actually listening, a real request to confirm it responds correctly — the same verification actually performed this session before trusting the governor was genuinely reachable.

## Prohibited Pattern

Assuming a service is running and correctly configured because it was started earlier in the session, without re-verifying, especially after any environment change.

## Implementation Guidance

Any workflow step that depends on the governor, or any other manually-managed service, should verify that service's real state immediately before depending on it, not rely on an earlier confirmation from earlier in the same session.

## Verification Requirements

Before any governed submission, confirm the governor process is actually listening and its credential resolution actually works — the same check already performed this session after the misconfigured first launch was discovered.

## Authoritative Sources

- This session's own real incident: the governor's first launch, missing `.env`, silent failure, manual restart

## Known Exceptions

None identified — no supervisor or service-manager currently exists for these processes; this is a real, open gap, not a resolved one.

## Lessons Learned

Confirmed this session: a service appearing to have started successfully does not guarantee it is correctly configured. `.env` must be explicitly sourced before launch, verified, not assumed.
