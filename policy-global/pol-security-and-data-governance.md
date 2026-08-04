---
document: Policy — Security and Data Governance
doc-id: global-0053
state: Live
date-created: 2026-07-25T150027+0200
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

A client's data is theirs. On offboarding, they receive a full, usable export of
everything — Data Tables, encryption key, decrypted Vault contents — and this operation
retains nothing after the export is confirmed received. See [[sop-offboarding|Offboarding SOP]] for the
procedure; this policy states the underlying principle it must never violate.

### Client-Facing Data Exposure

No server function returns more data to the client than that specific request needs.
Returning an entire row when only two fields are needed is a data-exposure risk, not just
an inefficiency — treat it accordingly.

### Enforcement Severity

Security issues are always Critical, per [[pol-anvil-first-development|Policy — Anvil-First Development]]'s enforcement
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
