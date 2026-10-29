---
title: "no_agent_gate_approval"
doc-id: "mb-e1b30994"
updated: "2026-10-29"
---
# Rule: No Agent Gate Approval

## Harness
opencode

## What to block
Any bash tool call whose command does either of the following:

1. Runs the developer's gate script, `pdlf-gate.sh`, in any form (`bash pdlf-gate.sh`, `bash /mnt/c/mybizz/scripts/pdlf-gate.sh`, `./pdlf-gate.sh`, `sh pdlf-gate.sh`), except with its `--check` argument, which only reads.
2. Writes to the PDLF ledger's `gates` table: the command contains, in any letter case, `INSERT INTO gates`, `INSERT INTO public.gates`, `UPDATE gates`, `UPDATE public.gates`, `DELETE FROM gates` or `DELETE FROM public.gates`, with or without double quotes around the table name and with any whitespace between the words.

Reading the `gates` table (`SELECT ... FROM gates`) is never blocked: the orchestrator reads it to know whether a gate has passed.

## Decision
Block (deny), always. No grant or allowance unlocks it.

## Message shown to the agent on block
"A PDLF gate is approved only by the developer. Present the gate summary, give the developer the pdlf-gate.sh command for this gate and run, wait for the developer to confirm, then read the gates table to check the approval. Never write a gate row yourself."

## Reason
A gate is the hard stop at which the developer commits to everything built before it. If the agent could write its own approval, the gate would rest on the agent's good behaviour, which is exactly what PDLF's control exists to replace. The developer records each approval with `pdlf-gate.sh`; this rule makes that the only way a gate row can be written, so a passed gate in the ledger is always the developer's decision. PDLF's test PR-03 proves it: an agent's attempt to write a gate is blocked.
