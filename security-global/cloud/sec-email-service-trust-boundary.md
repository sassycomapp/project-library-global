---
title: "sec-email-service-trust-boundary"
doc-id: "mb-c25dc5f1"
updated: "2026-11-07"
---
# Email Service Trust Boundary

## Applicable Threat

Amazon SES is the single email service of every Mybizz application, for every email sent and received, per `[[adr-brevo-email-and-crm]]`. SES reports received email, deliveries, bounces, complaints, opens and clicks to the instance through Amazon SNS, and marketing email carries an unsubscribe link, per `[[spec-api-specification]]` §2.4. A forged notification or a forged unsubscribe could falsely suppress a real contact, falsify engagement data, or plant a false email in the shared inbox.

## Security Requirement

1. Every SNS message to `/_/api/email/inbound` and `/_/api/email/events` has its SNS message signature checked with Amazon's signing certificate before anything else is done with it.
2. The SNS subscription confirmation is accepted only for the client's own topic.
3. The unsubscribe link is a signed link; a link whose signature fails changes nothing.
4. Every SES notification follows the shared webhook handler requirements of `[[spec-api-specification]]` §2.5: validate, check idempotency through `webhook_log`, log, dispatch, return HTTP 200. An invalid signature gets HTTP 400, no `webhook_log` row and an `error_log` entry.

## Approved Pattern

- The AWS access keys and the SES SMTP password are read only from the Vault, per `[[spec-vault-system]]` and `[[adr-brevo-email-and-crm]]`; Mybizz_management writes them, scoped to the client's own SES tenant and S3 prefix.
- A received email is read from the client's own S3 prefix only after its SNS notification has been validated.
- The instance calls SES only through its one email service module.

## Prohibited Pattern

- Processing a received email, a bounce, a complaint, a tracking event or an unsubscribe before its signature is validated.
- Accepting an SNS subscription confirmation for any topic other than the client's own.
- AWS keys or the SES SMTP password in code, in Anvil Secrets, in logs or in any document.

## Implementation Guidance

Treat SES notifications with the same seriousness as payment webhooks. A bounce, complaint or unsubscribe adds the address to the suppression list, which has real business and consent consequences (`[[spec-security-architecture]]` §3).

## Verification Requirements

1. Send an SNS message with an invalid signature to each email endpoint; confirm HTTP 400, no `webhook_log` row and no state change.
2. Send a subscription confirmation for another topic; confirm it is refused.
3. Open an unsubscribe link with an altered signature; confirm the contact is not suppressed.
4. Confirm the AWS keys and the SES SMTP password never appear in logs.

## Authoritative Sources

- `[[adr-brevo-email-and-crm]]` — Amazon SES, its flows and its Vault credentials
- `[[spec-api-specification]]` §2.4, §2.5 — the SES endpoints and the shared webhook handler requirements
- `[[adr-webhook-architecture]]` — `webhook_log` and dispatch
- `[[spec-vault-system]]` — credential storage

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
