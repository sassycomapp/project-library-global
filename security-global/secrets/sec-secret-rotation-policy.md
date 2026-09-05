---
document: "Secret Rotation Policy"
doc-id: sec-secret-rotation-policy
state: Live
date-created: 2026-08-27
category: secrets
---
# Secret Rotation Policy

**Scope note:** `sec-secret-exposure-response.md` covers rotation triggered by a confirmed exposure. This document covers rotation as a routine practice, independent of any known incident.

## Applicable Threat

A secret that has never been rotated remains valid indefinitely. If it was ever exposed without detection — through a channel nobody caught — it stays usable by whoever obtained it, forever, with no expiry to limit the damage.

## Security Requirement

Every secret has a defined maximum age before rotation is required, even with no known incident. Management service tokens are explicitly documented as manual-rotation-only in V1, per `spec-security-architecture.md` §2 — a real, current limitation, not silently assumed to be handled.

## Approved Pattern

A real, tracked rotation schedule per secret type, checked periodically — not left indefinite because nothing has gone wrong yet.

## Prohibited Pattern

Treating "no known compromise" as equivalent to "no need to rotate" — the two are different facts; the first cannot be verified with certainty, which is exactly why routine rotation exists.

## Implementation Guidance

For each secret type in the Vault (`spec-vault-system.md` §3) and each dev-tooling credential (`sec-development-tooling-credentials.md`), assign a real maximum age. Management tokens, currently manual-only, need this tracked explicitly until automated rotation exists.

## Verification Requirements

For each secret, confirm its actual age against its defined maximum; confirm any secret past its maximum age is flagged, not silently carried forward.

## Authoritative Sources

- `spec-security-architecture.md` §2 — token lifecycle, manual rotation in V1
- `spec-vault-system.md` §3 — Vault contents

## Known Exceptions

The master encryption key in Anvil Secrets is explicitly never rotated, per `spec-vault-system.md` §1 — this is a deliberate design decision, not an oversight; see `sec-master-encryption-key-protection.md` for why.

## Lessons Learned

None yet. Populated as real findings occur.
