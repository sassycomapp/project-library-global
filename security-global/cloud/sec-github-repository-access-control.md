---
title: "sec-github-repository-access-control"
doc-id: "mb-a2ae334b"
updated: "2026-11-08"
---
# GitHub Repository Access Control

## Applicable Threat

`master_template`, `blank_client_template` and the business's `{slug}-app4` repository together make the release image that every client instance runs — per `[[spec-five-app-architecture-model]]` and `[[spec-client-instance-hosting]]`. Unauthorized or unreviewed write access to any of them, or to the Container Registry, would carry malicious or broken code to every live client instance at the next release, without any per-client review step.

## Security Requirement

Write access to `master_template`, `blank_client_template` and `{slug}-app4` is restricted to the developer directly. No automated process or AI agent pushes a release into `master_template` or changes `blank_client_template`; only the developer does, after approving the release. The release image is built only by the image build workflow in `{slug}-app4`, from a release tag, and only that workflow writes to the business's Container Registry repository. Every MyBizz repository is GitHub-backed. — a local-only working tree is not an acceptable end state for either repository.

## Approved Pattern

Development happens in App 1; pushing App 1's tagged release into `master_template` (Step 42) is a deliberate, manual action by the developer, per `[[spec-five-app-architecture-model]]`'s Update Deployment Model. High-risk releases use a staged rollout — a subset of clients moved to the release image first.

## Prohibited Pattern

An AI agent pushing to `master_template`'s repository, committing directly to `blank_client_template`'s table definitions without the explicit review the schema-change process requires, or pushing an image to the Container Registry.

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
