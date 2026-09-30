# Rule: No Fabricated Verification

## Harness
opencode

## What to block
Any agent response or completion claim stating or implying that code was
tested, a build succeeded, a command was executed, a file was inspected, or
a problem was resolved when the claimed action did not actually occur or is
not supported by available evidence.

## Decision
Block (deny). Do not allow a fabricated verification claim to be presented
as a factual result.

## Message shown to the agent on block
"Verification claims must be factual and evidence-based. Do not state or
imply that a test, build, command, inspection, or resolution occurred unless
it actually occurred and the available evidence supports the claim."

## Reason
AI-assisted development depends on trustworthy reporting. A claim of
successful verification is not a substitute for verification itself.
