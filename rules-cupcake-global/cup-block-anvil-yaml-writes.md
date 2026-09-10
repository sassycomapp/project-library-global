---
document: "Rule: Block Writes to anvil.yaml"
doc-id: cup-block-anvil-yaml-writes
state: Live
date-created: 2026-09-05
---

# Rule: Block Writes to anvil.yaml

## Harness
opencode

## What to block
Any tool call where the tool is a file-writing tool (edit, write, or
equivalent) and the target file path ends in "anvil.yaml", in any
Anvil project, regardless of the specific project or folder.

## Decision
Block (deny). Do not allow the write to proceed under any circumstance.

## Message shown to the agent on block
"anvil.yaml is Anvil-managed metadata. Direct writes are prohibited.
If a task genuinely requires a change here, stop and ask the developer
for explicit approval before proceeding by any other means."

## Reason
Per AGENTS.md Hard Rule 1: anvil.yaml is treated as Anvil-managed
configuration. It must never be created, edited, reformatted,
regenerated, normalized, merge-edited, or patched by an agent. Anvil
itself is the sole authoritative writer.
