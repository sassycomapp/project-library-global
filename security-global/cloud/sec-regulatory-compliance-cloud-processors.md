---
title: "sec-regulatory-compliance-cloud-processors"
doc-id: "mb-c1321a2c"
updated: "2026-11-10"
---
# Regulatory Compliance Scope of Third-Party Cloud Processors

## Applicable Threat

Each third-party cloud service a Mybizz application depends on carries its own regulatory implication, per `[[spec-security-architecture]]` §3. Treating this as a single, generic "compliance" concern rather than naming each processor's specific obligation risks missing one.

## The Processors

| Processor | What it handles | Regulatory implication |
|---|---|---|
| DigitalOcean, `LON1` | Runs every client instance and holds its database: every record the instance holds (`[[spec-client-instance-hosting]]`) | Holds all personal information of the client's customers and staff, processed outside South Africa (POPIA cross-border transfer; GDPR where it applies) |
| Anvil | Hosts App 5, which holds each client business's registry record, contacts and billing status | Personal information of the client business's contacts (POPIA; GDPR where it applies) |
| Paddle | Mybizz's subscription billing, as Merchant of Record: each client business's billing name, address, email, business tax number and payment card (`[[spec-client-billing]]`) | Personal information of the client business's contacts, processed outside South Africa (POPIA cross-border transfer; GDPR where it applies). Card data stays with Paddle, which carries PCI DSS for Mybizz's subscription payments |
| Stripe, Paystack, PayPal | Card and PayPal payments, on the gateway's own hosted page or embedded fields | PCI DSS, SAQ A scope (`[[spec-regulatory-compliance-baseline]]`) |
| Amazon Web Services: SES, SNS, S3 | Every email sent and received; received email stored in the client's own S3 prefix; SES runs in `eu-west-1` (`[[adr-brevo-email-and-crm]]`) | Personal information in email content and addresses, processed outside South Africa (POPIA cross-border transfer; GDPR where it applies) |
| Cloudflare: R2 and DNS | The client's files in an R2 bucket in the client's own Cloudflare account (`[[adr-client-r2-storage-and-exit-handover]]`); the client's DNS records; Mybizz's own R2 bucket, holding Paddle's billing notifications (`[[spec-client-billing]]`) | Personal information in stored files (POPIA; GDPR where it applies) |

## Security Requirement

1. Per `[[spec-security-architecture]]` §3: PCI DSS applies (SAQ A scope) through the payment gateways. GDPR applies conditionally, determined by the actual client base, not fixed at build time — so it is re-checked as real clients are onboarded, not assumed settled once.
2. Every processor in the table above is named in the regulatory scope of every client instance. A new processor is added to this table before it handles any client data, per `[[sec-requirements-third-party-integration]]`.

## Approved Pattern

Regulatory scope treated as a live, re-checked fact tied to the real client base and the real processor list at any given time — not a one-time determination made at build time and never revisited.

## Prohibited Pattern

- Assuming GDPR does not apply because it did not apply at initial build time, without re-checking as new clients with EU customers are onboarded.
- A processor handling client data while missing from the table above.

## Implementation Guidance

When onboarding a new client, confirm whether the client's own customer base introduces new regulatory scope (for example EU customers triggering GDPR) as part of that onboarding, not as a separate, easily-forgotten task.

## Verification Requirements

1. For each active client instance, confirm its regulatory scope (GDPR applicability specifically) has been checked against its actual, current customer base, not assumed from build time.
2. Confirm every outside service the application calls appears in the table above.

## Authoritative Sources

- `[[spec-security-architecture]]` §3 — regulatory compliance
- `[[spec-regulatory-compliance-baseline]]` — POPIA, GDPR, PCI DSS and retention
- `[[adr-brevo-email-and-crm]]` — Amazon SES
- `[[adr-client-r2-storage-and-exit-handover]]` — Cloudflare R2
- `[[spec-client-instance-hosting]]` — DigitalOcean

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
