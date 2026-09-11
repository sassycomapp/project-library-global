---
document: "Regulatory Compliance Scope of Third-Party Cloud Processors"
doc-id: sec-regulatory-compliance-cloud-processors
state: Live
date-created: 2026-08-27
category: cloud
---
# Regulatory Compliance Scope of Third-Party Cloud Processors

## Applicable Threat

Each third-party cloud service this project depends on (Stripe, Paystack, Brevo, Anvil itself) carries its own regulatory implication, per `[[spec-security-architecture]]` §3. Treating this as a single, generic "compliance" concern rather than naming each processor's specific obligation risks missing one.

## Security Requirement

Per `[[spec-security-architecture]]` §3: PCI DSS applies (SAQ A scope) via Stripe/Paystack. GDPR applies conditionally, determined by actual client base, not fixed at build time — meaning this must be re-checked as real clients are onboarded, not assumed settled once.

## Approved Pattern

Regulatory scope treated as a live, re-checked fact tied to the real client base at any given time, per the existing spec's own framing — not a one-time determination made at build time and never revisited.

## Prohibited Pattern

Assuming GDPR doesn't apply because it didn't apply at initial build time, without re-checking as new clients with EU customers are onboarded.

## Implementation Guidance

When onboarding a new client, confirm whether their own customer base introduces new regulatory scope (e.g. EU customers triggering GDPR) as part of that onboarding, not as a separate, easily-forgotten task.

## Verification Requirements

For each active client instance, confirm its regulatory scope (GDPR applicability specifically) has been checked against its actual, current customer base, not assumed from build time.

## Authoritative Sources

- `[[spec-security-architecture]]` §3 — regulatory compliance
- `[[spec-regulatory-compliance-baseline]]` (referenced, not yet reviewed directly)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
