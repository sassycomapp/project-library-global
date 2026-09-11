---
document: "AI Agent Secret Visibility"
doc-id: sec-ai-agent-secret-visibility
state: Live
date-created: 2026-08-27
category: secrets
---
# AI Agent Secret Visibility

**Scope note:** distinct from `[[sec-secret-exposure-response]]`, which covers secrets leaking through logs, git, or errors. This document covers the AI agent's own direct visibility to real secret values during ordinary operation.

## Applicable Threat

The AI agent building and maintaining this project reads files, runs commands, and debugs issues directly. Confirmed real, this session: `PGPASSWORD` was read directly from `.env` and used in a live PowerShell command. A real secret was, correctly and necessarily, made visible to the agent to accomplish a real task — this is not always avoidable, but it is a real exposure surface that needs its own explicit handling.

## Security Requirement

When an agent must read or use a real secret to accomplish a legitimate task, the exposure is minimized: the value is used for the immediate purpose and not echoed, logged, or repeated back in the conversation or any output beyond what's operationally necessary.

## Approved Pattern

Confirmed this session: `PGPASSWORD`'s real value was read, used directly in a command, and not otherwise repeated, echoed, or included in any output beyond the single command that needed it.

## Prohibited Pattern

An agent printing a secret's value in a status report, a log, or a summary "for confirmation," when the value itself was never actually needed in that output.

## Implementation Guidance

When a task genuinely requires a real secret, scope the agent's access to exactly what's needed for that task, and treat any output containing the secret's actual value as something to avoid unless the immediate action itself requires it.

## Verification Requirements

Review any session transcript or log where a real secret was used; confirm the value itself does not appear anywhere beyond the specific command or call that required it.

## Authoritative Sources

- This session's own real handling of `PGPASSWORD` as the working example

## Known Exceptions

A secret's value necessarily appears in the specific command or API call that uses it — this is unavoidable and not itself a violation; the requirement is about avoiding *unnecessary* repetition beyond that.

## Lessons Learned

None yet. Populated as real findings occur.
