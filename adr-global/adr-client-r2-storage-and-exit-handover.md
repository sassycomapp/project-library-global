---
title: "adr-client-r2-storage-and-exit-handover"
updated: "2026-11-08"
doc-id: "mb-f9c1cc3d"
---
# `client-r2-storage-and-exit-handover` ADR — Each Client Has Its Own R2 Storage, and Leaves With It

**Status:** Accepted
**Applies to:** Every Mybizz application and every client instance (App 4)

---

## Context

A client instance accumulates data that does not belong in its operational Data Tables: raw webhook payloads from payment gateways and other services, execution logs, and backups. Kept in Data Tables, this data grows without limit and slows the instance down.

A client's data belongs to the client. When a client leaves Mybizz, the client must leave with all of its data, in a form it can use without Mybizz.

Every client instance already has its own container and its own database. Shared storage for any client data would break that isolation.

---

## Decision

1. **Each client instance has one Cloudflare R2 bucket of its own,** created at onboarding. No bucket is shared between clients, and no client's data is kept as a folder in a shared bucket or a shared account.
2. **The bucket sits in a free Cloudflare account in the client's own name, on the client's own email address.** The client creates the account and invites Mybizz's Cloudflare user as a member with the roles R2 Admin and DNS. Mybizz_management creates the bucket and a token for that bucket only.
3. **The bucket token is kept in the client's Vault.** They never appear in code, in Anvil Secrets or in any document.
4. **The bucket holds the client's cold data:** raw webhook payloads, the archived audit log, archived rows, email bodies and attachments, and backups. The client's Data Tables keep only an index row for each item (what it is, its status and its R2 key). Index rows older than the retention period are pruned; the item itself stays in R2.
5. **When the client leaves Mybizz, all the client's data is written to its R2 bucket:** a full export of every Data Table, the client's `encryption_key`, and the Vault contents in decrypted form, beside everything the bucket already holds.
6. **The client confirms the export is in the bucket; Mybizz's Cloudflare user then leaves the client's account.** Nothing is transferred: the account and the bucket were always the client's.
7. After Mybizz leaves the account, Mybizz retains nothing of the client's data, except the records Mybizz is legally required to keep in Mybizz_management.

---

## Why

- **Isolation.** One client, one app, one database, one storage. A shared bucket or account would be the one place where clients' data meets.
- **The client owns its data.** The bucket is in the client's own account from the first day, so the client leaves with its data in a working store, not a file it must find a home for.
- **No lock-in.** A client can leave at any time with everything.
- **Lean databases.** Cold data in R2 keeps each instance's Data Tables small and fast.
- **Free retrieval.** R2 charges nothing for reading data out, so the client and the instance can retrieve old data at no cost.

---

## Consequences

- Provisioning a client accepts its Cloudflare invitation, creates its bucket and token, and enters the token in its Vault ([[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)).
- Every Mybizz application writes to R2 through the S3-compatible API from App 2's server code. The library it uses must run on Anvil's server Python, confirmed before it is adopted.
- Offboarding follows this ADR; each application's project library holds its offboarding procedure ([[[default:specifications-global/spec-regulatory-compliance-baseline|Regulatory Compliance Baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md)).
- The exit export is a function of every Mybizz application, proven on the test client before the application's first release.

