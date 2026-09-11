---
document: "Payment Gateway Trust Boundary"
doc-id: sec-payment-gateway-trust-boundary
state: Live
date-created: 2026-08-27
category: cloud
---
# Payment Gateway Trust Boundary

## Applicable Threat

Stripe and Paystack are external, third-party cloud services this project depends on for real financial transactions. Per `[[spec-security-architecture]]` §3, processing payments through them places this project in PCI DSS SAQ A scope — a real regulatory obligation, not an internal design choice.

## Security Requirement

Only publishable keys are ever stored client-accessible (`payment_config` table); secret keys are Vault-only, per `[[spec-vault-system]]`. SAQ A scope must be maintained — meaning card data itself is never handled or stored by this project's own code, only passed through the gateway's own hosted checkout/API flow.

## Approved Pattern

Gateway secret keys retrieved only via `get_vault_secret()`, never hardcoded or logged. Card data never touches application code directly — the gateway's own SDK/hosted flow handles it, preserving SAQ A eligibility.

## Prohibited Pattern

Any code path that receives, stores, or logs raw card data directly, which would move this project out of SAQ A into a materially heavier compliance scope.

## Implementation Guidance

Before adding any new payment-related feature, confirm it doesn't introduce a code path that touches raw card data — if it does, this is an architecture-level decision requiring explicit review, not a routine implementation choice.

## Verification Requirements

Confirm no application code, log, or error message ever contains raw card data. Confirm all payment secret keys resolve only through `get_vault_secret()`.

## Authoritative Sources

- `[[spec-security-architecture]]` §3 — regulatory compliance, PCI DSS SAQ A scope
- `[[spec-vault-system]]` — secret storage

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
