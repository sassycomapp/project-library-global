# Rule: No Access to Known Secret Files Unless Explicitly Required

## Harness
opencode

## What to block
Any tool call that reads a file matching a known secret-file pattern —
`.env`, `.env.*`, `id_rsa`, `id_ed25519`, `*.pem`, `*.key`, or an
equivalent — unless the developer has explicitly authorised access for
a defined purpose in the current session.

## Decision
Block (deny). Do not allow access to a known secret file unless
explicitly required and authorised.

## Message shown to the agent on block
"This file matches a known secret or credential pattern. Do not read it
unless explicitly required and authorised for the approved task."

## Reason
Secrets can be exposed through source code, logs, tool output, or
subsequent network requests once read into context. This rule blocks
the read at its known, checkable source. It does not, and cannot, catch
a secret value already in context being copied, logged, or transmitted
onward through some other means — that risk is not addressable by a
tool-call pattern and remains a separate, real limitation.
