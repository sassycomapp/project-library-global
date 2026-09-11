---
document: "Requirement — Pre-Merge to master_template"
doc-id: sec-requirements-pre-merge-master-template
state: Live
date-created: 2026-08-27
category: requirements
---
# Requirement — Pre-Merge to master_template

## Applicable Threat

A merge to `stable` propagates automatically to every live client instance, per `[[spec-five-app-architecture-model]]`'s Update Deployment Model. A security gap merged here reaches every client at once, with no per-client review step to catch it.

## Security Requirement

Before merging to `stable`, all of the following are explicitly true:

1. Every new or modified server function meets `[[sec-requirements-server-function]]` in full.
2. Every new Data Table meets `[[sec-requirements-data-table-creation]]` in full.
3. Every open Sentinel finding (`triage_findings`) tied to this change has `triage_label = 'wontfix'` or `resolved_at IS NOT NULL` — the same real condition PDLF's own `build-verified` gate already enforces, per `[[spec-postgres-ledger]]`.
4. High-risk releases use the staged-rollout, version-tagged path described in `[[spec-five-app-architecture-model]]`, not a direct full rollout.

## Approved Pattern

Merge only after items 1–4 are confirmed, in that order, not merged first and verified after.

## Prohibited Pattern

Merging to `stable` because the feature works correctly in testing, without confirming the four items above explicitly.

## Implementation Guidance

This document exists specifically because a merge here is the single highest-consequence action in the whole deployment model — everything before it can be caught locally; this cannot be un-propagated cleanly once client instances have picked it up.

## Verification Requirements

Before any merge to `stable`, confirm items 1–4 directly, not from memory of having done them earlier.

## Authoritative Sources

- `[[spec-five-app-architecture-model]]` — Update Deployment Model
- `[[spec-postgres-ledger]]` — `build-verified` gate condition
- `[[sec-requirements-server-function]]`, `[[sec-requirements-data-table-creation]]`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
