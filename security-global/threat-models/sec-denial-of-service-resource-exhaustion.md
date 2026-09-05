---
document: "Threat Model — Denial of Service and Resource Exhaustion"
doc-id: sec-denial-of-service-resource-exhaustion
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Denial of Service and Resource Exhaustion

## Applicable Threat

A user or attacker sends a high volume of requests, or a single expensive request (a large report generation, an unbounded search), consuming enough server resources to degrade or deny service to legitimate users.

## Security Requirement

Rate limits already defined in `spec-security.md` §3 (10/minute/IP unauthenticated, 100/minute/user authenticated) are enforced on every endpoint, including background-task-triggering ones, not only on obviously public-facing forms.

## Approved Pattern

Rate limiting enforced via a Data Table, per `spec-security.md` §2, so limits survive server restarts and work across a multi-server environment — already the documented approach.

## Prohibited Pattern

A new endpoint or server function added without confirming it falls under the existing rate-limiting mechanism, on the assumption that "it's internal" or "only logged-in users can reach it."

## Implementation Guidance

Any function that triggers real computational or database work proportional to user input (a report, a bulk export, a search with no result limit) should have an explicit bound on the work it can do per request, in addition to the general rate limit.

## Verification Requirements

For each new endpoint or server function, confirm it falls under rate limiting; for any function doing potentially expensive work, confirm a bound exists on that work's scale.

## Authoritative Sources

- `spec-security.md` §2, §3 — rate limiting, shared numeric standards
- `spec-api-specification.md` §5 — rate limiting on HTTP endpoints

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
