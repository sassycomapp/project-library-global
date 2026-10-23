---
title: "adr-client-r2-storage-and-exit-handover"
updated: "2026-10-23"
doc-id: "mb-f9c1cc3d"
---
# `client-r2-storage-and-exit-handover` ADR — Each Client Has Its Own R2 Storage, and Leaves With It

**Status:** Accepted
**Applies to:** Every Mybizz application and every client instance (App 4)

---

## Context

A client instance accumulates data that does not belong in its operational Data Tables: raw webhook payloads from payment gateways and other services, execution logs, and backups. Kept in Data Tables, this data grows without limit and slows the instance down.

A client's data belongs to the client. When a client leaves Mybizz, the client must leave with all of its data, in a form it can use without Mybizz.

Every client already has its own Anvil account and its own database. Shared storage for any client data would break that isolation.

---

## Decision

1. **Each client instance has one or two Cloudflare R2 buckets of its own,** created at onboarding. The number is set at onboarding. No bucket is shared between clients, and no client's data is kept as a folder in a shared bucket or a shared account.
2. **The buckets sit in a Cloudflare account dedicated to that client,** held by Mybizz and named after the client's business, the same way the client's Anvil account is.
3. **The bucket credentials are kept in the client's Vault.** They never appear in code, in Anvil Secrets or in any document.
4. **The buckets hold the client's cold data:** raw webhook payloads, execution logs and backups. The client's Data Tables keep only an index row for each item (what it is, its status and its R2 key). Index rows older than the retention period are pruned; the item itself stays in R2.
5. **When the client exits Mybizz, all the client's data is written to its R2 bucket:** a full export of every Data Table, the client's `encryption_key`, and the Vault contents in decrypted form, beside everything the bucket already holds.
6. **Ownership of the Cloudflare account holding the bucket is then transferred to the client.** The client leaves in possession of its R2 bucket with all its data.
7. After the transfer is confirmed, Mybizz retains nothing of the client's data, except the records Mybizz is legally required to keep in Mybizz_management.

---

## Why

- **Isolation.** One client, one app, one database, one storage. A shared bucket or account would be the one place where clients' data meets.
- **The client owns its data.** Handing over the bucket itself gives the client its data in a working store, not a file it must find a home for.
- **No lock-in.** A client can leave at any time with everything.
- **Lean databases.** Cold data in R2 keeps each instance's Data Tables small and fast.
- **Free retrieval.** R2 charges nothing for reading data out, so the client and the instance can retrieve old data at no cost.

---

## Consequences

- Provisioning a client creates its Cloudflare account and buckets, and enters the bucket credentials in its Vault ([[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)).
- Every Mybizz application writes to R2 through the S3-compatible API from App 2's server code. The library it uses must run on Anvil's server Python, confirmed before it is adopted.
- Offboarding follows this ADR ([[[default:standard-operating-procedures-global/sop-offboarding|Offboarding SOP]]](C:/dev/project-library-global/standard-operating-procedures-global/sop-offboarding.md), [[[default:specifications-global/spec-regulatory-compliance-baseline|Regulatory Compliance Baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md)).
- The exit export is a function of every Mybizz application, proven on the test client before the application's first release.

