# Rule: No False Completion Claims

## Harness
opencode

## What to block
Any agent response or completion report that presents a task as complete,
fully resolved, or successfully finished when work remains incomplete,
verification remains outstanding, or required actions were not performed.

## Decision
Block (deny). Do not allow an incomplete result to be presented as complete.

## Message shown to the agent on block
"Do not claim completion unless the approved task has actually been
completed. Clearly distinguish between completed work, partially completed
work, proposed work, and work that has not been performed."

## Reason
A development environment depends on accurate reporting of task status.
An agent must not represent partial progress, assumptions, or intended work
as a completed result.
