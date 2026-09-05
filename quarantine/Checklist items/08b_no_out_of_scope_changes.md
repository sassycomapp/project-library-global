# Rule: No Out-of-Scope Changes

## Harness
opencode

## What to block
Any tool call that modifies files, components, or functionality not
reasonably necessary to complete the explicitly approved task.

Unrelated defects, improvements, cleanup, optimisation, or refactoring must
not be implemented unless separately approved by the developer.

## Decision
Block (deny). Do not allow unrelated changes to proceed.

## Message shown to the agent on block
"This change is outside the explicitly approved task scope. Do not implement
unrelated fixes, cleanup, improvements, or refactoring. Report the finding
to the developer and wait for separate approval."

## Reason
AI agents can interpret unrelated changes as helpful or necessary and expand
a task beyond its intended scope. Restricting changes to the approved scope
preserves developer control and reduces unintended consequences.
