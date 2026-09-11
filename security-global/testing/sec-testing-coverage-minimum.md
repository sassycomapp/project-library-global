---
document: "Security Test Coverage Minimum"
doc-id: sec-testing-coverage-minimum
state: Live
date-created: 2026-08-27
category: testing
---
# Security Test Coverage Minimum

## Applicable Threat

A feature is considered complete without any explicit decision about which security tests it needs, leaving coverage to chance rather than a deliberate check against this library's own documents.

## Security Requirement

Every new server function or Data Table is checked against the relevant `requirements/` documents (`[[sec-requirements-server-function]]`, `[[sec-requirements-data-table-creation]]`) and, where it touches a documented threat class, has at least one real test corresponding to that threat-model document's own Verification Requirements.

## Approved Pattern

A feature's test plan explicitly lists which `security-global` documents it was checked against, and which of their Verification Requirements were actually executed — a real, traceable link, not an implicit assumption of coverage.

## Prohibited Pattern

Writing functional tests only, with no explicit consideration of which security documents in this library apply to the feature.

## Implementation Guidance

This is the concrete coverage check underneath `[[sec-requirements-release-readiness]]` — confirming, before release, that every relevant document's testing requirement was actually addressed, not just that no `triage_findings` row happens to be open.

## Verification Requirements

For a sample of recently completed features, confirm an explicit record exists of which security documents were checked and which tests were run against them.

## Authoritative Sources

- `[[sec-requirements-server-function]]`, `[[sec-requirements-data-table-creation]]`, `[[sec-requirements-release-readiness]]`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
