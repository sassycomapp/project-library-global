---
document: "Secret Exposure Response"
doc-id: sec-secret-exposure-response
state: Live
date-created: 2026-08-27
category: secrets
---
# Secret Exposure Response

**Scope note:** `[[spec-vault-system]]` is the authoritative document for how secrets are correctly stored and enforced. This document covers a different question: what happens when a secret is exposed anyway, despite correct storage — logged accidentally, committed to git, printed in an error message, or read out by a manipulated AI action.

## Applicable Threat

A secret that was correctly stored in the Vault is exposed through a different channel: an exception handler that prints full request data including a secret field; a debug log statement left in code; a secret accidentally included in a git commit; an AI agent asked, directly or through a crafted request, to reveal Vault contents.

## Security Requirement

No code path may log, print, or include a Vault secret in any output — error message, log line, or API response — under any circumstance, including exception handling. This extends the existing masking rule in `[[spec-vault-system]]` §2 to cover error paths specifically, which that document does not explicitly address.

## Approved Pattern

```python
try:
    result = gateway.charge(secret=get_vault_secret('stripe_secret_key'))
except GatewayError as e:
    anvil.server.log(f"Gateway charge failed: {e.code}")  # error code only, never the secret
    raise
```

## Prohibited Pattern

```python
try:
    result = gateway.charge(secret=get_vault_secret('stripe_secret_key'))
except Exception as e:
    anvil.server.log(f"Charge failed: {e}")  # e may include the request, secret included
```

A broad exception handler logging the full exception object, which may include the secret if it was part of the failed request.

## Implementation Guidance

- Exception handlers in any function that reads a Vault secret must log only a code or message, never the exception object in full, unless independently confirmed not to contain secret material.
- If a secret is ever confirmed exposed (git history, a log file, a support ticket), it must be rotated immediately — the exposure itself, not just the fix, is the trigger.
- Git history is a real, permanent exposure channel — a secret committed once remains recoverable from history even after being removed in a later commit. Rotation, not deletion alone, is the correct response.

## Verification Requirements

- Review exception handlers in every function that reads a Vault secret; confirm none log the raw exception object.
- Grep git history for known secret patterns (API key prefixes, etc.) before treating a repository as clean.

## Authoritative Sources

- `[[spec-vault-system]]` §2 — secret enforcement and masking (storage-side; this document covers the exposure-response gap it doesn't address)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
