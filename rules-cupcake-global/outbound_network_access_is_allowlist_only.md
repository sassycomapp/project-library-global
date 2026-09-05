# Rule: Outbound Network Access Is Allowlist-Only

## Harness
opencode

## What to block
Any tool call that performs an outbound network request (e.g. a fetch or
webfetch tool call) to a domain not present on the explicit,
maintained network allowlist for this environment.

## Decision
Block (deny). Do not allow the outbound request to proceed.

## Message shown to the agent on block
"Outbound network access is restricted to explicitly authorised
destinations. This destination is not on the current allowlist. Do not
retry through an alternative endpoint or service. Stop and obtain
explicit developer approval if network access is genuinely required."

## Reason
Outbound network access can create channels for unintended data
disclosure, prompt injection through external services, unauthorised
downloads, and other uncontrolled interactions. Explicit allowlisting
preserves control over where the environment may communicate — including
against an already-trusted domain being used as a covert channel, a real
documented case.
