# Rule: No Weakening of Acceptance Criteria

## Harness
opencode

## What to block
Any action that redefines, reinterprets, lowers, bypasses, or weakens the
requirements, tests, security criteria, acceptance criteria, or success
conditions established for the approved task in order to make the agent's
solution appear successful.

## Decision
Block (deny). Do not allow the acceptance criteria to be weakened by the
agent.

## Message shown to the agent on block
"Acceptance criteria are fixed by the developer and the approved task. Do
not redefine, lower, reinterpret, or weaken the conditions of success to
make your solution appear successful. Meet the criteria or report that they
have not been met."

## Reason
The agent must solve the task against the established definition of success.
It must not be allowed to change that definition in order to declare its own
work successful.
