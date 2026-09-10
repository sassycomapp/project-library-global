---
document: "Rule: Block Task and Spawn Tools"
doc-id: cup-block-task-tool
state: Live
date-created: 2026-09-05
---

# Rule: Block Task and Spawn Tools

## Harness
opencode

## What to block
Any tool call where the tool name is one of:
- task
- delegate
- call_omo_agent
- agent_session_create

This list is also maintained separately at ~/.config/opencode/spawn-tools-denylist.json.
Both should be kept in sync when a new spawn-capable tool name is discovered.

## Decision
Block (deny). Do not allow the call to proceed under any circumstance.

## Message shown to the agent on block
"Sub-agent creation is prohibited in this environment. This tool has been
permanently disabled. Do not retry with a different tool name without
first checking whether it needs to be added to the denylist."

## Reason
The tool.execute.before interception mechanism this environment relies on
does not catch actions taken by a spawned sub-agent. Rather than attempt
to monitor sub-agent behavior after creation, sub-agent creation itself is
blocked at the source. This is Layer 2 of a three-layer design; Layer 1
is a native opencode.json permission deny on "task" specifically. This
rule is the layer that also covers any other tool name with the same
spawning capability.
