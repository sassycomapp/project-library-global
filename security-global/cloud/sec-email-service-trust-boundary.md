---
document: "Email Service Trust Boundary"
doc-id: sec-email-service-trust-boundary
state: Live
date-created: 2026-08-27
category: cloud
---
# Email Service Trust Boundary

## Applicable Threat

Brevo is a third-party cloud service handling this project's outbound email and inbound webhooks (open tracking, click tracking, unsubscribe events), per `spec-api-specification.md` §2.3. A forged or unauthenticated webhook could falsely mark a real contact as unsubscribed, or falsify engagement data.

## Security Requirement

Brevo webhook signature validation applies with the same rigor as payment webhooks, per `spec-api-specification.md` §2.4's shared handler requirements — validate, check idempotency via `webhook_log`, log, dispatch, return 200.

## Approved Pattern

SMTP credentials and the Brevo API key retrieved only from the Vault, per `spec-vault-system.md` §3. Webhook signature checked before any event (open, click, unsubscribe) is processed.

## Prohibited Pattern

Processing an unsubscribe or tracking event without first validating the webhook's signature — an unauthenticated unsubscribe event could be used to falsely suppress legitimate communication to a real customer.

## Implementation Guidance

Treat Brevo webhooks with the same seriousness as payment webhooks — an unsubscribe event has real business consequences (per `spec-security-architecture.md`'s regulatory context, consent state matters for compliance, not just marketing reach).

## Verification Requirements

Send a Brevo webhook with an invalid signature; confirm rejection. Confirm the SMTP credentials never appear in logs.

## Authoritative Sources

- `spec-api-specification.md` §2.3, §2.4 — Brevo webhooks, shared handler requirements
- `spec-vault-system.md` §3 — SMTP/Brevo credential storage

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
