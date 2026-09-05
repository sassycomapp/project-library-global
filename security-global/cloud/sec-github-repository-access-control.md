---
document: "GitHub Repository Access Control"
doc-id: sec-github-repository-access-control
state: Live
date-created: 2026-08-27
category: cloud
---
# GitHub Repository Access Control

## Applicable Threat

`master_template` and `blank_client_template` are trusted, compiled dependencies — per `spec-five-app-architecture-model.md`, every client instance inherits code and logic from `master_template` automatically. Unauthorized or unreviewed write access to either repository would propagate malicious or broken code to every live client instance at once, without any per-client review step.

## Security Requirement

Write access to `master_template` and `blank_client_template` is restricted to the developer directly. No automated process merges to `stable` without an explicit human action. Every dev-tooling source repository is GitHub-backed, per `dev-tooling-source-repos-must-be-github-backed.md` — a local-only working tree is not an acceptable end state for either repository.

## Approved Pattern

Development happens on `develop`; merge to `stable` is a deliberate, manual, reviewed action, per `spec-five-app-architecture-model.md`'s Update Deployment Model. High-risk releases use version tags for staged rollout — a subset of clients updated first.

## Prohibited Pattern

An AI agent merging directly to `stable`, or committing directly to `blank_client_template`'s schema without the explicit review the schema-change process requires.

## Implementation Guidance

Confirm branch protection rules on `stable` actually block direct pushes, not just discourage them by convention. Confirm this is enforced by GitHub itself, not only by developer discipline.

## Verification Requirements

Attempt a direct push to `stable`; confirm it's rejected at the GitHub level, not merely against a written rule.

## Authoritative Sources

- `spec-five-app-architecture-model.md` — Update Deployment Model
- `dev-tooling-source-repos-must-be-github-backed.md`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
