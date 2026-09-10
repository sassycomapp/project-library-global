---
document: "Rule: Outbound Network Access Is Allowlist-Only"
doc-id: outbound_network_access_is_allowlist_only
state: Live
date-created: 2026-09-05
---

# Rule: Outbound Network Access Is Allowlist-Only

## Harness
opencode

## What to block
Any tool call that performs an outbound network request (e.g. a fetch or
webfetch tool call) to a domain not present on the explicit,
maintained network allowlist for this environment.

**Exemption — loopback (amended 2026-09-08):** requests to the machine's
own addresses (`127.0.0.1`, `localhost`, `::1`) are never blocked by this
rule. This rule governs EXTERNAL destinations — traffic between this
environment's own tools on the same machine (e.g. the memory-governor API
at `127.0.0.1:8321`) is internal service communication, not outbound
access, and must remain functional while enforcement is active.

## Decision
Block (deny). Do not allow the outbound request to proceed — except for
loopback destinations, which are always allowed per the exemption above.

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
