---
title: "adr-single-contacts-table"
doc-id: "mb-c307af98"
updated: "2026-10-23"
---
# Single Contacts Table
**Consolidated Contact Model for CRM**

Status: Accepted

---

## Context

A person appears across an application in many roles: a lead, a customer who books or buys, a recipient of invoices and notes. Two overlapping person tables (one for CRM, one for bookings and invoices) force every query to know which table to join, and split one person's history in two.

Leads and contacts are created together at capture time ([[[default:adr-global/adr-lead-capture-simultaneous-creation|Lead Capture Simultaneous Creation]]](C:/dev/project-library-global/adr-global/adr-lead-capture-simultaneous-creation.md)), so the contact exists from the person's first interaction.

---

## Decision

**A single `contacts` table is the person record for the entire application.** All customers are contacts; not all contacts are customers. There is no `customers` table.

Every table that refers to a person does so with `contact_id`, a link to `contacts` (for example `bookings.contact_id`, `invoice.contact_id`, `time_entries.contact_id`, `client_notes.contact_id`).

### `contacts` table fields:
- Identity: `contact_id`, `first_name`, `last_name`, `email`, `phone`
- CRM: `status`, `source`, `lifecycle_stage`, `tags`, `internal_notes`, `preferences`
- Financial: `total_spent`, `total_transactions`, `average_order_value`
- Tracking: `date_added`, `last_contact_date`, `created_at`, `updated_at`

---

## Consequences

- One source of truth for every person record
- Simpler queries: no join between two person tables
- Brevo's CRM sync targets one table ([[[default:adr-global/adr-brevo-email-and-crm|Brevo for Email and CRM]]](C:/dev/project-library-global/adr-global/adr-brevo-email-and-crm.md))
- A column named `customer_id`, or a `customers` table, is a defect
