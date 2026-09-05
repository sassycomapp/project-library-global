# Rule: No Privilege Escalation or Authority Expansion

## Harness
opencode

## What to block
Any action that grants the agent additional permissions, disables approval
mechanisms, weakens sandboxing, alters access controls, expands filesystem or
network access, or otherwise increases the agent's authority beyond the
current explicitly authorised scope.

## Decision
Block (deny). Do not allow the agent to expand its own permissions or
authority.

## Message shown to the agent on block
"You may not grant yourself additional permissions or expand your authority.
Do not weaken sandboxing, disable approval mechanisms, alter access controls,
or increase your filesystem, network, tool, or other access. Stop and obtain
explicit developer approval for any required change in authority."

## Reason
An agent must operate within the authority explicitly granted to it. Allowing
the agent to expand its own permissions would permit it to remove the
boundaries intended to govern its behaviour.
