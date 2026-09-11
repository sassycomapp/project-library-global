---
document: "Threat Model — AI-Agent-Introduced Vulnerabilities"
doc-id: sec-ai-agent-introduced-vulnerabilities
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — AI-Agent-Introduced Vulnerabilities

This document is the direct reason Sentinel exists. Every other threat-model document in this folder describes a specific vulnerability *class*. This one describes the specific *cause* common to all of them in this project: code is written by an AI agent that does not personally verify its own output, and reviewed by a developer who cannot personally verify every line either.

## Applicable Threat

An AI agent implements a feature that looks correct, passes a casual read, and is subtly wrong — most commonly: a security check present in one similar function is silently missing from a new one; a client-supplied value is trusted somewhere it shouldn't be; a change made "to fix" one thing quietly reintroduces a risk closed elsewhere. The failure mode is not malice — it is an agent producing plausible-looking code without the equivalent of a human's felt sense that "this looks like the risky part."

## Security Requirement

No security-relevant code (anything touching auth, RBAC, payment, secrets, or cross-user data access) is treated as complete because it was written and looks correct. It is complete only once checked against this library's real documents — the specific pattern it should match, and the specific pattern it must not.

## Approved Pattern

- New code implementing a pattern already documented in this library (e.g. `[[sec-broken-access-control-within-instance]]`, `[[sec-payment-manipulation]]`) is checked directly against that document's Approved/Prohibited pattern pair before being considered done.
- Sentinel's own step-triggered review (per the Sentinel plan, Section 9) runs at the step where this kind of code is introduced — not left to a general, unscoped "review everything" pass.

## Prohibited Pattern

- Treating "the code runs and does the intended thing in the happy path" as equivalent to "the code is secure."
- An agent asserting a security check was performed without a real, verifiable action behind that claim — this is a documented, real failure mode (see the retired `the retired structural-compliance-enforcement-architecture-v2.md`, Scope and Threat Model), not a hypothetical.

## Implementation Guidance

- When implementing anything touching an area covered by this library, the relevant document(s) are read first, not consulted only if something later looks wrong.
- A Sentinel finding is never resolved by an agent's own re-assertion that it's fine — resolution requires the developer's explicit decision, per the Sentinel plan's core loop (Section 5).

## Verification Requirements

- For any feature touching a documented threat class, confirm the relevant threat-model document was actually consulted — not inferred from the code happening to look correct.
- Confirm every Sentinel finding in `triage_findings` for a given feature has either `triage_label = 'wontfix'` (an explicit, recorded decision) or `resolved_at IS NOT NULL` (a verified resolution) before that feature is considered complete — this is already the real, enforced condition on PDLF's own `build-verified` gate, per `[[spec-postgres-ledger]]`.

## Authoritative Sources

- `the retired sentinel-security-system-plan.md` — Sentinel's own design and trigger model
- the retired `the retired structural-compliance-enforcement-architecture-v2.md` — the broader problem of AI actions and claims not being independently verifiable by default

## Known Exceptions

None. This document's requirement applies to every other document in this library equally.

## Lessons Learned

None yet. Populated as real findings occur.
