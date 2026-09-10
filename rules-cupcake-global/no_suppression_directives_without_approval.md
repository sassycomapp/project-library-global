---
document: "Rule: No Suppression Directives Without Explicit Approval"
doc-id: no_suppression_directives_without_approval
state: Live
date-created: 2026-09-05
---

# Rule: No Suppression Directives Without Explicit Approval

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) where the content
being written adds a lint, type-check, compiler, or security suppression
directive — including but not limited to `eslint-disable`,
`eslint-disable-next-line`, `# type: ignore`, `# noqa`, `@ts-ignore`,
`@ts-expect-error`, or an equivalent compiler warning suppression comment
— unless the developer has explicitly approved that specific suppression
in the current session.

## Decision
Block (deny). Do not allow the change to proceed without explicit
approval.

## Message shown to the agent on block
"Suppression directives may not be added to silence a warning or finding.
Fix the underlying problem instead. If suppression is genuinely
necessary, stop and ask the developer for explicit approval for that
specific suppression."

## Reason
Suppression directives can conceal defects, security findings, and
incorrect code while making automated checks appear successful. They must
therefore not be used as an autonomous escape mechanism.
