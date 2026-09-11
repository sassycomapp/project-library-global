---
document: "AI Agent Execution Sandbox"
doc-id: sec-ai-agent-execution-sandbox
state: Live
date-created: 2026-08-27
category: infrastructure
---
# AI Agent Execution Sandbox

## Applicable Threat

The AI agent's own actions — which tools it can call, which sub-agents it can spawn, which directories it can reach — are not automatically constrained by good intentions. Confirmed real, structural gap (this session): sub-agent-spawned tool calls bypass the `tool.execute.before` interception mechanism entirely.

## Security Requirement

Per the retired `the retired structural-compliance-enforcement-architecture-v3.md` Section 6.1: the `task` tool (the sole real mechanism for sub-agent creation) is denied globally, at three independent layers — native config, Cupcake policy hook, and a standing review habit for any new tool discovered to have the same capability.

## Approved Pattern

`opencode.json` global `task: deny`, confirmed to remove the tool from the model's visible tool set entirely — not merely to block the call after it's attempted.

## Prohibited Pattern

Relying on a single layer (e.g. the Cupcake policy alone) without the redundant config-level deny, since a config mistake in one layer should not silently remove all protection.

## Implementation Guidance

Any new skill or plugin considered for this environment is checked for a tool that creates an isolated session before being trusted, per the standing habit already established.

## Verification Requirements

Confirm `task` does not appear in the agent's visible tool set. Confirm any known third-party spawn-tool name is refused by the Cupcake policy.

## Authoritative Sources

- the retired `the retired structural-compliance-enforcement-architecture-v3.md` Section 6.1 — full three-layer design and its real, confirmed limitation (an unrecognized third-party spawn-tool name)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
