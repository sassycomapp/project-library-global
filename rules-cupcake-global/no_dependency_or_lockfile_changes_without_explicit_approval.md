---
document: "Rule: No Lockfile Changes Without Explicit Approval"
doc-id: no_dependency_or_lockfile_changes_without_explicit_approval
state: Live
date-created: 2026-09-05
---

# Rule: No Lockfile Changes Without Explicit Approval

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
known dependency lockfile — `package-lock.json`, `yarn.lock`,
`pnpm-lock.yaml`, `poetry.lock`, `Pipfile.lock`, `Cargo.lock`, `go.sum`,
or an equivalent — unless the developer has explicitly approved that
specific change in the current session.

## Decision
Block (deny). Do not allow the lockfile change to proceed without
explicit approval.

## Message shown to the agent on block
"Lockfiles may not be changed without explicit developer approval for
the specific change. Do not add, remove, upgrade, downgrade, replace, or
regenerate a lockfile autonomously."

## Reason
Lockfile changes can introduce supply-chain risk, compatibility
problems, and unexpected transitive changes that are easy to miss in
review. They are consequential changes and must remain under explicit
developer control. See also the separate rule covering the install
commands that typically produce these changes.
