---
title: "sec-requirements-third-party-integration"
doc-id: "mb-f6f30b31"
updated: "2026-11-07"
---
# Requirement — New Third-Party Integration

## Applicable Threat

A new external service integration (a new payment gateway, a new email provider, any new webhook source) is added without the same baseline checks already applied to Stripe, Paystack, PayPal and Amazon SES, leaving a gap the existing patterns already know how to close.

## Security Requirement

Before a new third-party integration is considered complete, all of the following are explicitly true:

1. Its credentials are stored in the Vault, per `[[spec-vault-system]]` — never hardcoded, never in `payment_config` or an equivalent plain table, never in Anvil Secrets.
2. Any inbound webhook validates its signature before processing, per the shared webhook handler requirements of `[[spec-api-specification]]` §2.5.
3. Idempotency is checked before processing an inbound event, per the same section.
4. The service and its dependency reviewed per `[[sec-review-before-trust]]` and `[[sec-dependency-skill-supply-chain]]` before being trusted.
5. If it's a payment or data processor, its regulatory scope is checked per `[[sec-regulatory-compliance-cloud-processors]]`.

## Approved Pattern

The existing Stripe, Paystack, PayPal and Amazon SES integrations as the working reference — each follows this pattern, per `[[spec-api-specification]]` §2 and `[[adr-webhook-architecture]]`.

## Prohibited Pattern

Adding a new integration's webhook handler without signature validation, on the reasoning that "it's just for now" or "it's low-risk."

## Implementation Guidance

Treat every new integration as inheriting the full weight of this requirement, regardless of how minor it initially seems — the existing integrations set the real bar.

## Verification Requirements

For each new integration, confirm items 1–5 explicitly before considering it complete.

## Authoritative Sources

- `[[spec-api-specification]]` §2, `[[adr-webhook-architecture]]`, `[[spec-vault-system]]`, `[[sec-review-before-trust]]`, `[[sec-dependency-skill-supply-chain]]`, `[[sec-regulatory-compliance-cloud-processors]]`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
