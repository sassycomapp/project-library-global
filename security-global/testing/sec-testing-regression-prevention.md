---
document: "Security Regression Prevention"
doc-id: sec-testing-regression-prevention
state: Live
date-created: 2026-08-27
category: testing
---
# Security Regression Prevention

## Applicable Threat

A security vulnerability is found and fixed once, then reintroduced later — by a different change, a different agent session, or a refactor that doesn't know the original reason a pattern was avoided.

## Security Requirement

Every real, confirmed security finding (a `triage_findings` row resolved, not `wontfix`'d) gets a permanent, automated test proving the specific fixed behavior, so the same regression is caught automatically if it ever recurs — the same REGRESSION RULE already established for engineering review generally, per `step-15-plan-eng-review.md` Section 9's mandatory REGRESSION RULE, applied here specifically to security findings.

## Approved Pattern

A resolved Sentinel finding's fix ships together with a test that would fail if the specific vulnerability it describes were reintroduced — not just a fix with no corresponding permanent test.

## Prohibited Pattern

Closing a `triage_findings` row as resolved with no test added that would catch the same issue recurring.

## Implementation Guidance

Treat a resolved security finding the same way any other confirmed regression risk is treated, per the existing REGRESSION RULE — this is not a new practice, it's the existing one applied consistently to security findings specifically.

## Verification Requirements

For a sample of resolved `triage_findings` rows, confirm a corresponding permanent test exists and genuinely fails if the original issue is reintroduced.

## Authoritative Sources

- `step-15-plan-eng-review.md` Section 9 — REGRESSION RULE (mandatory, no `AskUserQuestion` required)
- `spec-postgres-ledger.md` — `triage_findings` schema

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
