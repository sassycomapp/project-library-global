---
document: "Rule: No Verification Tampering"
doc-id: no_verification_tampering
state: Live
date-created: 2026-09-05
---

# Rule: No Verification Tampering

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
known verification-infrastructure file — CI/CD pipeline definitions
(e.g. `.github/workflows/*`, `.gitlab-ci.yml`), test-runner
configuration (e.g. `pytest.ini`, `jest.config.*`, `vitest.config.*`),
or a coverage-threshold configuration file — unless the developer has
explicitly approved that specific change in the current session.

## Decision
Block (deny). Do not allow the change to proceed without explicit
approval.

## Message shown to the agent on block
"Verification infrastructure is protected. Do not modify CI/CD pipeline
definitions, test-runner configuration, or coverage requirements without
explicit developer approval. Fix the underlying problem instead."

## Reason
Verification must remain independent of the work being verified. An
agent must not be able to modify the mechanism that judges its own
success. This rule covers the specific, known files where that
mechanism is configured — it does not, and cannot, detect whether a
given edit to an otherwise-unlisted file was made "to pass more
easily," which is not a pattern Cupcake can evaluate.
