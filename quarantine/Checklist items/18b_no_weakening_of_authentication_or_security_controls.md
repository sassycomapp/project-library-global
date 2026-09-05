# Rule: No Weakening of Authentication or Security Controls

## Harness
opencode

## What to block
Any action that bypasses, removes, weakens, disables, or downgrades
authentication, authorisation, encryption, input validation, access control,
or other security controls merely to make functionality work or simplify the
implementation.

## Decision
Block (deny). Do not allow security controls to be weakened by the agent.

## Message shown to the agent on block
"Security controls may not be bypassed, removed, weakened, disabled, or
downgraded to make functionality work. Preserve the security boundary and
address the underlying implementation problem instead."

## Reason
Security controls exist to enforce trusted boundaries. An agent must not treat
those boundaries as obstacles that may be removed merely to achieve functional
success.
