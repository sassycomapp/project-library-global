---
document: "Live Verification Standard"
doc-id: sec-testing-live-verification-standard
state: Live
date-created: 2026-08-27
category: testing
---
# Live Verification Standard

**Scope note:** the testing-specific application of `sec-verify-dont-trust-claims.md` — that principle stated generally; this document states what it means specifically for security testing.

## Applicable Threat

A security test exists as a written plan or description but was never actually executed against real, running code — indistinguishable, on paper, from a test that genuinely passed.

## Security Requirement

A security test is not considered complete until it has been run for real, against real, running code, with a real, observed result — not merely written, described, or reasoned through.

## Approved Pattern

This session's own repeated standard: a claim ("this is fixed," "this is blocked") is followed by a real, independent action confirming it — a direct query, a live attempt, a real command — not accepted from the claim alone.

## Prohibited Pattern

Describing a test plan in prose and treating that description as equivalent to having run it.

## Implementation Guidance

For any security test, the actual, real output of running it is what gets recorded — not a restatement of what the test was intended to check.

## Verification Requirements

For any claimed security test, confirm real, observed output exists — a real error message, a real HTTP status, a real query result — not a description of expected behavior.

## Authoritative Sources

- `sec-verify-dont-trust-claims.md` — the general principle this document specializes

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
