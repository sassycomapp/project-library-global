---
document: "Requirement — New Data Table Creation"
doc-id: sec-requirements-data-table-creation
state: Live
date-created: 2026-08-27
category: requirements
---
# Requirement — New Data Table Creation

Maps to Sentinel's own step-intensity table (`the retired sentinel-security-system-plan.md` Section 9), Step 17 — High scrutiny: "What data exists? Who can access it? What isolation is required?"

## Applicable Threat

A new Data Table is created without its access pattern being deliberately decided, leaving it open to whatever the first server function written against it happens to do.

## Security Requirement

Before a new Data Table is considered complete, all of the following are explicitly true:

1. Which roles (per `[[spec-security-architecture]]` §1) can read it, and which can write it, is explicitly decided — not left to whatever the first function happens to implement.
2. If it holds role-scoped data (each user should only see their own rows), the ownership-filtering requirement in `[[sec-broken-access-control-within-instance]]` is confirmed to apply.
3. No column intended to hold a secret (API key, credential) is a plain column — it goes through the Vault, per `[[spec-vault-system]]`.
4. Table-level access is set to "No access" for client code, per `[[spec-security]]` §1 — all access goes through server functions.

## Approved Pattern

Access pattern decided and documented before the first server function is written against the table, not inferred afterward from whatever was implemented.

## Prohibited Pattern

Creating a Data Table and writing server functions against it without having explicitly decided who can access what.

## Implementation Guidance

This is a Sentinel checkpoint, per Section 9 — treat it as a real gate, not a formality.

## Verification Requirements

For each new Data Table, confirm items 1–4 above are each explicitly answered, not silently assumed.

## Authoritative Sources

- `the retired sentinel-security-system-plan.md` Section 9 — Step 17
- `[[spec-security-architecture]]` §1, `[[spec-vault-system]]`, `[[sec-broken-access-control-within-instance]]`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
