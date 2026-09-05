# Rule: No Cross-Project Filesystem Access by Default

## Harness
opencode

## What to block
Any tool call whose target file path resolves to a project root
different from the project root of the current working directory
(`cwd`), unless the developer has made a separate, explicit request and
granted approval for that specific occasion, in the current session.

A prior approval, for a prior occasion, does not authorise a further
access to the same or a different external project.

## Decision
Block (deny). Do not allow cross-project access without a fresh,
explicit approval for this specific occasion.

## Message shown to the agent on block
"This path is outside the current project. Cross-project access requires
a separate, explicit developer request and approval on every occasion.
Do not proceed based on a previous access or an assumed standing
permission."

## Reason
Project boundaries limit accidental damage, information exposure, and
scope expansion. Access to one project must never be interpreted as
standing authority to access another, and each occasion is treated as
genuinely new.
