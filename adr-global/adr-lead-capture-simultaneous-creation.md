---
document: "Lead Capture: Simultaneous leads + contacts Creation"
doc-id: adr-lead-capture-simultaneous-creation
state: Live
date-created: 2026-07-25T150027+0200
---
# Lead Capture: Simultaneous leads + contacts Creation
Date: 2026-03-21
Status: Accepted
Source: Devlog #34 — cs-architectural-specification-D.md §13

---

## Context

When a visitor submits a landing page lead capture form, two data entities are
relevant: a `leads` record (the capture event) and a `contacts` record (the person).
The question was whether to create only a `leads` record at capture time and convert
it to a contact later (manual conversion model), or to create both simultaneously.

---

## Decision

**Captured leads create records in both `leads` and `contacts` simultaneously at
capture time.**

The server function creates both rows in a single operation and sets
`leads.converted_to_contact_id` to link them immediately. The contact is enrolled
in the welcome sequence without any manual conversion step.

- `leads` row = the capture event record
- `contacts` row = the person record, created immediately

This is the industry-standard model used by HubSpot, ActiveCampaign, and similar
platforms. It ensures CRM machinery (activity timeline, campaigns, lifecycle
tracking) works from day one without a manual conversion step.

### Table relationship
`leads.converted_to_contact_id` is a link to `contacts`. It is set immediately on
lead creation — it is never null for a successfully captured lead.

`lead_captures` is the configuration table defining form fields and welcome sequence.
`leads` is the output table of captured submissions.

---

## Consequences

### Rules files affected

| File | Required content |
|---|---|
| `spec_crm.md` | Lead capture flow, simultaneous creation ruling, contact enrollment |
| `spec_crm_contacts.md` | Contact auto-creation from lead capture |
| `spec_website.md` [NEW] | Landing page lead capture implementation — §13 flow |
| `spec_database.md` / `spec_database_schema.md` | `leads`, `contacts`, `lead_captures` table relationships |

---

## Old-material pointers (added 2026-09-20, developer instruction, mb-wikilinks run 20260920T100155)

Material referenced by this document but not present in the current corpus, with developer-provided locations:
- spec_crm.md — old-iteration backup: /mnt/c/mybizz/backup-before/project-library/rules-library-old/spec_crm.md
- spec_crm_contacts.md — old-iteration backup: /mnt/c/mybizz/backup-before/project-library/rules-library-old/spec_crm_contacts.md
- spec_website.md — no backup located; confirmed does not exist (developer, 2026-09-20)
- spec_database.md — old-iteration backup: /mnt/c/mybizz/backup-before/project-library/rules-library-refactored/spec_database.md
- spec_database_schema.md — old-iteration backup: /mnt/c/mybizz/backup-before/project-library/rules-library-old/spec_database_schema.md
*End of `lead-capture-simultaneous-creation` ADR*
