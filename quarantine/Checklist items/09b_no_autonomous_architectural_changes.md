# Rule: No Autonomous Architectural Changes

## Harness
opencode

## What to block
Any significant architectural change made without explicit developer
approval, including replacing major components, introducing new architectural
patterns, restructuring major application boundaries, or materially changing
established system design.

## Decision
Block (deny). Do not allow the architectural change to proceed without
explicit approval.

## Message shown to the agent on block
"Significant architectural changes require explicit developer approval. Do
not replace major components, introduce new architecture, or materially
restructure the system autonomously. Present the proposed change and wait
for approval."

## Reason
Architectural decisions have consequences beyond the immediate task and can
affect security, maintainability, compatibility, and future development.
Those decisions remain under explicit developer authority.
