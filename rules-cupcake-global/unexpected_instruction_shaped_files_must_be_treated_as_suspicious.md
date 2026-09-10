---
document: "Rule: Unexpected Instruction-Shaped Files Must Not Be Created Outside Approved Locations"
doc-id: unexpected_instruction_shaped_files_must_be_treated_as_suspicious
state: Live
date-created: 2026-09-05
---

# Rule: Unexpected Instruction-Shaped Files Must Not Be Created Outside Approved Locations

## Harness
opencode

## What to block
Any file-writing tool call that creates a new file matching a known
instruction-shaped filename — `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, or
an equivalent — at any path outside the specific, known locations where
such a file is expected for this project.

## Decision
Block (deny). Do not allow the file to be created at this location.

## Message shown to the agent on block
"A file with this name is only expected at specific, known locations in
this project. Creating it here is not permitted. Report this to the
developer rather than proceeding."

## Reason
Unexpected instruction-shaped files can be used to introduce persistent
or indirect instructions into an AI development environment — a real,
documented attack path. This rule blocks the file's creation at the
point it would appear; it cannot separately verify that an agent, having
since encountered such a file through some other means, correctly
declined to treat its contents as authoritative — that remains a
behavioral expectation, not something Cupcake can check.
