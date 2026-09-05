---
document: "Master Encryption Key Protection"
doc-id: sec-master-encryption-key-protection
state: Live
date-created: 2026-08-27
category: secrets
---
# Master Encryption Key Protection

## Applicable Threat

Per `spec-vault-system.md` §1, exactly one item lives in Anvil Secrets: the master encryption key, used exclusively to encrypt and decrypt everything else in the Vault. Its compromise is categorically worse than any single Vault secret's compromise — it exposes every secret the Vault holds, at once, retroactively, for as long as those encrypted values have existed.

## Security Requirement

The master key is never rotated, per `spec-vault-system.md` §1 — this is intentional, since rotating it would require re-encrypting every Vault secret. Its protection instead relies entirely on Anvil Secrets' own platform-level guarantee (`sec-anvil-platform-responsibility-boundary.md`) and on no application code ever calling `anvil.secrets.get_secret()` directly outside the one dedicated vault-service module.

## Approved Pattern

Exactly one module in the entire codebase calls `anvil.secrets.get_secret()` for this key, per `spec-vault-system.md` §1 — no other code path touches it at all.

## Prohibited Pattern

Any code outside the dedicated vault-service module calling `anvil.secrets.get_secret()` — even for debugging, even temporarily.

## Implementation Guidance

Treat any new code that calls `anvil.secrets.get_secret()` as a Sentinel-relevant finding automatically, regardless of intent — this key's isolation to one module is the entire basis of the Vault's own security model.

## Verification Requirements

Grep the full codebase for `anvil.secrets.get_secret()`; confirm exactly one real call site exists, inside the designated vault-service module.

## Authoritative Sources

- `spec-vault-system.md` §1 — two-level secrets model

## Known Exceptions

None — this is the one absolute rule in the entire secrets architecture.

## Lessons Learned

None yet. Populated as real findings occur.
