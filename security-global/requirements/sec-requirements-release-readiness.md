---
document: "Requirement — Release Readiness"
doc-id: sec-requirements-release-readiness
state: Live
date-created: 2026-08-27
category: requirements
---
# Requirement — Release Readiness

Maps to Sentinel's own step-intensity table, Step 45 — real release/canary scrutiny.

## Applicable Threat

A release proceeds while a real, known security finding remains genuinely unresolved, because nothing explicitly checked this before release, only before individual steps along the way.

## Security Requirement

Before a release proceeds, all of the following are explicitly true:

1. `[[sec-requirements-pre-merge-master-template]]` was satisfied for everything included in this release.
2. No `triage_findings` row tied to this release has a severity of `High` or `Critical` with no `resolved_at` and no `wontfix` label.
3. Monitoring for the release (per `the retired sentinel-security-system-plan.md` Section 9, Step 45) is confirmed active before traffic reaches the new release.

## Approved Pattern

A real query against `triage_findings`, scoped to this release's step IDs, confirming item 2 directly — not a recollection of "nothing serious was found."

## Prohibited Pattern

Releasing because no new problems were reported recently, without a real, direct check of open findings at the severity levels that matter.

## Implementation Guidance

This is the last real checkpoint before real users are affected — treat it with the same rigor as `[[sec-requirements-pre-merge-master-template]]`, not as a formality once that step has already passed.

## Verification Requirements

Run a real query against `triage_findings` before every release; confirm the result directly, not from memory.

## Authoritative Sources

- `the retired sentinel-security-system-plan.md` Section 9 — Step 45
- `[[spec-postgres-ledger]]` — `triage_findings` schema
- `[[sec-requirements-pre-merge-master-template]]`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
