---
document: "Requirement — New Third-Party Integration"
doc-id: sec-requirements-third-party-integration
state: Live
date-created: 2026-08-27
category: requirements
---
# Requirement — New Third-Party Integration

## Applicable Threat

A new external service integration (a new payment gateway, a new email provider, any new webhook source) is added without the same baseline checks already applied to Stripe, Paystack, and Brevo, leaving a gap the existing patterns already know how to close.

## Security Requirement

Before a new third-party integration is considered complete, all of the following are explicitly true:

1. Its credentials are stored in the Vault, per `spec-vault-system.md` — never hardcoded, never in `payment_config` or an equivalent plain table.
2. Any inbound webhook validates its signature before processing, per `spec-api-specification.md` §2.4's shared handler requirements.
3. Idempotency is checked before processing an inbound event, per the same section.
4. The service and its dependency reviewed per `sec-review-before-trust.md` and `sec-dependency-skill-supply-chain.md` before being trusted.
5. If it's a payment or data processor, its regulatory scope is checked per `sec-regulatory-compliance-cloud-processors.md`.

## Approved Pattern

The existing Stripe/Paystack/Brevo integrations as the working reference — each already follows this exact pattern.

## Prohibited Pattern

Adding a new integration's webhook handler without signature validation, on the reasoning that "it's just for now" or "it's low-risk."

## Implementation Guidance

Treat every new integration as inheriting the full weight of this requirement, regardless of how minor it initially seems — the existing integrations set the real bar.

## Verification Requirements

For each new integration, confirm items 1–5 explicitly before considering it complete.

## Authoritative Sources

- `spec-api-specification.md` §2.4, `spec-vault-system.md`, `sec-review-before-trust.md`, `sec-dependency-skill-supply-chain.md`, `sec-regulatory-compliance-cloud-processors.md`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
