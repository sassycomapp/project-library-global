---
title: "adr-lead-capture-simultaneous-creation"
doc-id: "mb-c6554efe"
updated: "2026-10-23"
---
# Lead Capture: Simultaneous leads + contacts Creation
Status: Accepted

---

## Context

When a visitor submits a landing page lead capture form, two data entities are
relevant: a `leads` record (the capture event) and a `contacts` record (the person).
A lead can be recorded alone and converted to a contact later by hand, or both records
can be created at once.

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

- The application's schema defines `leads`, `contacts` and `lead_captures` with the relationship above.
- The lead capture server function creates both rows in one operation and enrols the contact in the welcome sequence.
- No manual conversion step exists anywhere in the application.
