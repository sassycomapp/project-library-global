---
document: "Management Service Authentication"
doc-id: sec-management-service-authentication
state: Live
date-created: 2026-08-27
category: cloud
---
# Management Service Authentication

## Applicable Threat

`Mybizz_management` communicates with every client instance via bearer-token-authenticated HTTP endpoints (`spec-api-specification.md` §3). A leaked or guessable token would let an attacker suspend a client instance, push false notifications, or query its health/status data.

## Security Requirement

Per `spec-security-architecture.md` §2: a unique bearer token per client instance, stored encrypted in the `Mybizz_management` registry, validated server-side on every management endpoint call, with invalid tokens rejected at HTTP 403.

## Approved Pattern

Per-client token isolation — compromise of one client's token does not affect any other client, since each is independently generated and independently revocable.

## Prohibited Pattern

A shared token across multiple client instances, or a management endpoint that trusts the request without validating the token first.

## Implementation Guidance

Token rotation is manual in V1, via re-provisioning, per `spec-security-architecture.md` §2. This is a real, current limitation, not an oversight — confirm any suspected compromise triggers manual rotation promptly, since no automated rotation exists to fall back on.

## Verification Requirements

Attempt a management endpoint call with an invalid or missing token; confirm HTTP 403 and no state change. Confirm one client's token cannot be used to act on a different client's instance.

## Authoritative Sources

- `spec-api-specification.md` §3 — management endpoints
- `spec-security-architecture.md` §2 — token security, lifecycle

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
