# Rule: The AI May Never Weaken the Controls Governing Itself

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
file that configures the controls governing the agent itself —
`opencode.json`'s `permission` section, or
`~/.config/opencode/spawn-tools-denylist.json` — unless the developer's
current-turn instruction explicitly names that exact file for that
specific edit.

**Known overlap, checked before deployment, not assumed:** the
`.cupcake/` directory itself, and Cupcake's own policy files, are
already protected by the `rulebook_security_guardrails` builtin,
installed by default. This rule exists specifically for the two files
above, which are outside that builtin's default protected-path list —
confirm this remains accurate before deploying, since the builtin's own
configuration could change.

## Decision
Block (deny). Do not allow the change to proceed without an explicit,
specific developer instruction naming this file.

## Message shown to the agent on block
"This file configures the controls that govern your own authority. Do
not modify it unless the developer has explicitly instructed you to
make that specific change to this specific file."

## Reason
The governing controls must remain independent of the agent they
constrain. If an agent can weaken the permission configuration or the
spawn-tool denylist that governs itself, the remaining protections built
around them can no longer be relied upon.
