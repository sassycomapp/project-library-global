# Rule: Protected AI Governance Files May Not Be Modified

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
protected AI governance file — `AGENTS.md`, `CLAUDE.md`, or an equivalent
persistent steering/rules file, in any project — unless the developer's
current-turn instruction explicitly names that exact file for that
specific edit.

## Decision
Block (deny). Do not allow the change to proceed without an explicit,
specific developer instruction naming this file.

## Message shown to the agent on block
"AI governance files are protected. Do not create, edit, rewrite,
reformat, regenerate, patch, or delete them unless the developer has
explicitly instructed you to make that specific change to this specific
file."

## Reason
Persistent AI governance files influence the instructions, boundaries,
and behaviour of the development agent. Allowing an agent to alter its
own governing instructions creates a direct path for authority expansion
or instruction manipulation — a real, documented failure mode in a
competing tool.
