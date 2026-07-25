---
document: "{Project Name} — SOP: Client Offboarding"
doc-id: global-0084
state: Live
date-created: 2026-07-25T150027+0200
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
4. Deliver the export to the client, via **[PROJECT]** — state the actual delivery
   method (secure download link, direct transfer, etc.)
5. Confirm the client has received and can access the export
6. Delete or deprovision the client's instance, per **[PROJECT]** this project's actual
   deprovisioning mechanism

**Verification:**
- [ ] Client confirms receipt of a complete, usable export
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
