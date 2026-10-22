---
title: "pol-security-and-data-governance"
doc-id: "mb-e779e1b8"
updated: "2026-10-22"
---
# Policy — Security and Data Governance

**Binding.** All development work on any Anvil.works project under this operation must
conform. No exceptions without documented justification.

---

## What

### Secrets Never Leave the Vault

Every credential — payment gateway keys, SMTP keys, API keys, any third-party secret —
lives in the Vault only, encrypted at rest, retrieved via `get_vault_secret()` in server
code. Never stored in plain columns, never hardcoded, never logged in plaintext.

### RBAC Is Mandatory, Not Optional

Every server function that isn't intentionally and documentedly public carries an
explicit auth decorator. A function with neither a decorator nor a documented reason for
being public is a Critical finding, full stop — not a style note, not a "get to it later"
item. The mechanical check: grep every server module for the decorator; any function
missing one is a finding.

### Data Belongs to the Client

A client's data is theirs. Each client has its own R2 storage. On offboarding, a full,
usable export of everything — Data Tables, encryption key, decrypted Vault contents — is
written to the client's own R2 bucket, the client leaves in possession of that bucket, and
this operation retains nothing after the handover is confirmed. See [[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md). See [[[default:standard-operating-procedures-global/sop-offboarding|Offboarding SOP]]](C:/dev/project-library-global/standard-operating-procedures-global/sop-offboarding.md) for the
procedure; this policy states the underlying principle it must never violate.

### Client-Facing Data Exposure

No server function returns more data to the client than that specific request needs.
Returning an entire row when only two fields are needed is a data-exposure risk, not just
an inefficiency — treat it accordingly.

### Enforcement Severity

Security issues are always Critical, per [[[default:policy-global/pol-anvil-first-development|Policy — Anvil-First Development]]](C:/dev/project-library-global/policy-global/pol-anvil-first-development.md)'s enforcement
table. RBAC violations, secret-handling errors, and over-broad client-facing data returns
are Critical without exception.

---

## Why

The operation's whole model depends on client trust — each client instance holds one
business's real operational and customer data. A security or data-governance failure in
one instance is a trust failure for the whole platform, not a contained incident. The
Vault-only rule exists because Anvil Secrets requires IDE access clients cannot be given.
The RBAC mechanical check exists because a manual review misses what a function
accidentally left unprotected; a grep does not.

---

## Where

Every project this operation builds on Anvil.works. Applies to every server function,
every credential, every offboarding event, without exception.

**Source:** consolidated from prior project practice and this operation's Vault
architecture.
