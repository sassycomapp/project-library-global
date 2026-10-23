---
title: "sec-github-repository-access-control"
doc-id: "mb-a2ae334b"
updated: "2026-10-23"
---
# GitHub Repository Access Control

## Applicable Threat

`master_template` and `blank_client_template` are trusted, compiled dependencies — per `[[spec-five-app-architecture-model]]`, every client instance inherits code and logic from `master_template` automatically. Unauthorized or unreviewed write access to either repository would propagate malicious or broken code to every live client instance at once, without any per-client review step.

## Security Requirement

Write access to `master_template` and `blank_client_template` is restricted to the developer directly. No automated process or AI agent pushes a release into `master_template` or changes `blank_client_template`; only the developer does, after approving the release. Every MyBizz repository is GitHub-backed. — a local-only working tree is not an acceptable end state for either repository.

## Approved Pattern

Development happens in App 1; pushing App 1's tagged release into `master_template` (Step 42) is a deliberate, manual action by the developer, per `[[spec-five-app-architecture-model]]`'s Update Deployment Model. High-risk releases use version tags for staged rollout — a subset of clients updated first.

## Prohibited Pattern

An AI agent pushing to `master_template`'s repository, or committing directly to `blank_client_template`'s schema without the explicit review the schema-change process requires.

## Implementation Guidance

Confirm branch protection rules on the branch `master_template` publishes from block pushes by anyone but the developer, not just discourage them by convention. Confirm this is enforced by GitHub itself, not only by developer discipline.

## Verification Requirements

Attempt a push to `master_template`'s published branch with an agent's credentials; confirm it's rejected at the GitHub level, not merely against a written rule.

## Authoritative Sources

- `[[spec-five-app-architecture-model]]` — Update Deployment Model

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
