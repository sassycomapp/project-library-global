---
title: "sec-requirements-pre-merge-master-template"
doc-id: "mb-5b61d0dc"
updated: "2026-10-22"
---
# Requirement — Before a Release into master_template

## Applicable Threat

A release pushed into `master_template` (Step 42) propagates automatically to every live client instance, per `[[spec-five-app-architecture-model]]`'s Update Deployment Model. A security gap released here reaches every client at once, with no per-client review step to catch it.

## Security Requirement

Before a release is pushed into `master_template`, all of the following are explicitly true:

1. Every new or modified server function meets `[[sec-requirements-server-function]]` in full.
2. Every new Data Table meets `[[sec-requirements-data-table-creation]]` in full.
3. Every open Sentinel finding (`triage_findings`) tied to this change has `triage_label = 'wontfix'` or `resolved_at IS NOT NULL` — the same real condition PDLF's own `build-verified` gate already enforces, per `[[[pdlf:pdlf-library/specifications-local/spec-postgres-ledger]]](C:/pdlf/pdlf-library/specifications-local/spec-postgres-ledger.md).md` (PDLF).
4. High-risk releases use the staged-rollout, version-tagged path described in `[[spec-five-app-architecture-model]]`, not a direct full rollout.
5. The whole test suite passes for the release, and every ASVS Level 2 requirement and adopted Level 3 control has passing evidence (test RL-01).

## Approved Pattern

Release only after items 1–5 are confirmed, in that order, not released first and verified after.

## Prohibited Pattern

Releasing because the feature works correctly in testing, without confirming the five items above explicitly.

## Implementation Guidance

This document exists specifically because a release here is the single highest-consequence action in the whole deployment model — everything before it can be caught locally; this cannot be un-propagated cleanly once client instances have picked it up.

## Verification Requirements

Before any release into `master_template`, confirm items 1–5 directly, not from memory of having done them earlier.

## Authoritative Sources

- `[[spec-five-app-architecture-model]]` — Update Deployment Model
- `spec-postgres-ledger.md` (PDLF) — `build-verified` gate condition
- `[[sec-requirements-server-function]]`, `[[sec-requirements-data-table-creation]]`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
