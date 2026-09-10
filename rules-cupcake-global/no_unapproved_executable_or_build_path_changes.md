---
document: "Rule: No Unapproved Executable or Build-Path Changes"
doc-id: no_unapproved_executable_or_build_path_changes
state: Live
date-created: 2026-09-05
---

# Rule: No Unapproved Executable or Build-Path Changes

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
known executable-infrastructure file — a CI/CD workflow file (e.g.
`.github/workflows/*`), a `Dockerfile`, a deployment configuration file,
or `package.json` — unless the developer has explicitly approved that
specific change in the current session.

## Decision
Block (deny). Do not allow the change to proceed without explicit
approval.

## Message shown to the agent on block
"Executable and build-path infrastructure may not be changed
autonomously. Do not modify this file without explicit developer
approval."

## Reason
Executable infrastructure can alter what runs, when it runs, and with
what permissions. This rule blocks writes to the whole file at these
known paths. It does not separately distinguish a change to, for
example, `package.json`'s lifecycle-script section from any other
change within that same file — that level of content-specific detection
is a real, stated limitation, not attempted here.
