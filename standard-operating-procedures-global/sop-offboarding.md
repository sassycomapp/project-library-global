---
title: "sop-offboarding"
doc-id: "mb-472dfcb2"
updated: "2026-10-22"
---
# {Project Name} — SOP: Client Offboarding

**Authority:** **[PROJECT]** — cite this project's data-rights/retention ADR.

---

## Procedure — Offboarding a Client

**Trigger:** A client ends their subscription or otherwise exits the platform.

**Preconditions:**
- Client's identity and instance confirmed
- **[PROJECT]** any contractual or notice-period requirement satisfied before this
  procedure begins

**Steps:**
1. Export a full copy of all the client's Data Tables
2. Export the client's `encryption_key`
3. Export the client's Vault contents in decrypted form
4. Write items 1 to 3 to the client's own R2 bucket, beside the webhook payloads, logs and
   backups it already holds
5. Transfer ownership of the Cloudflare account holding the bucket to the client, and
   confirm the client can access the bucket and its contents ([[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md))
6. Delete or deprovision the client's instance, per **[PROJECT]** this project's actual
   deprovisioning mechanism

**Verification:**
- [ ] Client confirms it holds its R2 bucket and that the export in it is complete and usable
- [ ] No client data remains retained anywhere after this procedure completes —
  **[PROJECT]** state explicitly what "nothing retained" covers (Data Tables, Vault,
  backups, logs) and confirm each is actually cleared, not just the primary instance
- [ ] Deprovisioning confirmed complete

**Escalation:** if the client disputes the completeness of the export, or if any data is
found retained after this procedure was marked complete, treat as a data-rights incident —
**[PROJECT]** cite this project's incident-escalation path, do not resolve informally.

---

*This is the global starter model. Copy into a new project's
`standard-operating-procedures-local/`, fill every **[PROJECT]** marker, remove this
closing note. The core commitment — full export, nothing retained — is a standing
principle from this operation's existing practice; keep it as the default posture unless
this project has an explicit, documented reason to retain something.*
