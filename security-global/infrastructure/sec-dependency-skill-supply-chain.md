---
document: "Dependency and Skill Supply Chain"
doc-id: sec-dependency-skill-supply-chain
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Dependency and Skill Supply Chain

## Applicable Threat

A third-party Python package, OpenCode skill, or plugin introduces a vulnerability, or malicious behavior, that this project's own code never wrote but now depends on. GStack's own `/cso` tool already names this class of risk directly — skill supply-chain security — as part of its real, existing scan scope.

## Security Requirement

Any new dependency or skill is checked before being trusted — for its actual publisher, its licensing (per the real precedent set by Cupcake's own review: free, Apache 2.0, active maintenance, named security-research backing), and, per the AI-agent-execution-sandbox document, whether it introduces any session-spawning capability.

## Approved Pattern

The review already performed for Cupcake before adopting it: real license confirmed, real maintenance activity confirmed, real security-research affiliation confirmed (Trail of Bits), before being trusted as part of this environment's own enforcement layer.

## Prohibited Pattern

Installing a skill or package because it appears to solve an immediate problem, without the same review already applied to Cupcake.

## Implementation Guidance

`/cso`'s own daily/monthly audit modes already cover dependency supply-chain scanning at the codebase level, per the Sentinel plan Section 3 — this document's requirement applies specifically to the decision point of adopting something new, before `/cso` would ever see it running in production.

## Verification Requirements

For any new dependency or skill under consideration, confirm: real publisher/maintainer identity, real license, real evidence of active maintenance, and a check against the spawn-tool list per `[[sec-ai-agent-execution-sandbox]]`.

## Authoritative Sources

- `the retired sentinel-security-system-plan.md` Section 3 — `/cso`'s real, confirmed scan scope
- This session's own Cupcake adoption review, as the real precedent for what "checked" looks like

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
