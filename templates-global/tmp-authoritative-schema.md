---
document: "{Project Name} — Authoritative Database Schema"
doc-id: global-0086
state: Live
date-created: 2026-07-25
---
# {Project Name} — Authoritative Database Schema

**Date:** **[PROJECT]**
**Version:** **[PROJECT]**
**Total Tables:** **[PROJECT]** — count and state this explicitly; it's the fastest sanity
check anyone reviewing this document has.
**Platform:** Anvil.works
**Source:** **[PROJECT]** — if this schema was consolidated from other working documents
(a scaffold plan, a build plan), name them. If this is a fresh build, state that instead.

**Table status convention:** mark each table `[DONE]` once its Anvil Data Table actually
exists and matches this specification; leave unmarked while still planned. This document
is the schema of record — the `[DONE]` marker tracks build progress against it, it does
not replace the ledger's own step tracking (Step 17/18). If a table's real, built
structure ever diverges from what's written here, this document is wrong until corrected
— never silently let the two drift.

---

## Field Type Conventions

Anvil's Data Table field types, and this operation's standing conventions for using them.
This section is fixed — it documents the platform, not this project — keep it in every
copy of this template unmodified unless the underlying convention genuinely changes.

| Type | Use for | Convention |
|---|---|---|
| `string` | Text fields | |
| `number` | Numeric fields | State units in the Notes column if not obvious (currency, seconds, etc.) |
| `bool` | Flags | |
| `datetime` | Any timestamp | **Always stored as UTC.** Conversion to a user's local time happens at display time in server code, never at storage time. State the project's timezone-per-instance source (typically `business_profile.timezone`, an IANA string) if this project has one. |
| `date` | Calendar dates with no time component | |
| `link → {table}` | A relationship to a single row in another table | |
| `links → {table}` | A relationship to multiple rows in another table | |
| `media` | File/image uploads | |
| `simpleObject` | Arbitrary JSON — use when the shape is genuinely dynamic, not as a substitute for defining real columns | Overuse of `simpleObject` in place of real columns is a smell — flag it as a finding if you see many, not a default choice |

---

## Table Groups Overview

**[PROJECT]** — list every table group in this project's schema, table count per group,
one-line description. Grand total must match the header's stated table count exactly —
check this before calling the document complete.

| Group | Tables | Description |
|---|---|---|
| Core & Configuration | **[PROJECT]** | Users, settings, vault, business profile — see starter set below |
| **[PROJECT]** | | |
| **Total** | **[PROJECT]** | |

### Core & Configuration — starter set

Nearly every project this operation builds needs some version of these. Adapt, don't
reinvent from nothing:

- `business_profile` — the client's business info: name, contact details, address,
  `timezone` (IANA string), `system_currency` (ISO 4217, set at onboarding, immutable
  after first transaction per this operation's standard currency ADR).
- `vault` — encrypted credential storage. Every payment gateway key, SMTP key, or other
  secret goes here, never in plain columns elsewhere. Retrieved via `get_vault_secret()`
  in server code, never read directly.
- `config` — key-value configuration storage, for settings that don't warrant their own
  dedicated table.
- `activity_log` — user action audit trail: who, what, when, from where.

**[PROJECT]** — add or remove from this starter set as the project actually needs; state
explicitly if a project genuinely has no need for one of these (e.g. no payment gateway →
no need for gateway keys in `vault`, but `vault` itself likely still holds SMTP
credentials).

---

## {N}. {Group Name} Tables ({count})

Repeat this section per group. Per-table entry format:

### **[status]** {N.M} `{table_name}`
{One-line purpose statement.}

| Field | Type | Notes |
|---|---|---|
| **[PROJECT]** | | |

**[PROJECT]** — if fields were added after the table's initial design (a later audit, a
design-doc revision), keep that history visible as a sub-block rather than silently
merging it in — this operation's own real schema does this ("Onboarding fields (added per
plan-tune audit)") and it's worth preserving as a convention: **schema history is not
overwritten, it's appended and dated.**

---

## Key Architectural Patterns

Cross-cutting rules that don't belong to any single table. The four below are this
operation's standing platform decisions, backed by existing ADRs — keep them in every
project's schema document, don't genericize them away:

### UTC Storage & Timezone Display
All datetimes stored as UTC. Conversion to a user's local timezone happens at display
time in server functions, using the relevant instance's configured timezone. Never store
a localized datetime.

### Data Isolation
**[PROJECT]** — if this project is a standalone app, state that directly: no cross-app
data isolation concern. If this project is one instance of the dependency-based
multi-instance model, state it inherits structural isolation — one instance cannot access
another's tables — per `dependency-based-not-multi-tenant` ADR.

### Secret Management
Payment gateway keys, SMTP keys, and other credentials live in the `vault` table only,
encrypted at rest, retrieved via `get_vault_secret()`. Never stored in plain columns, never
hardcoded.

### {Project-specific patterns}
**[PROJECT]** — add this project's own cross-cutting decisions here, each tied to the ADR
that justifies it, same pattern as the three above. Do not invent a new pattern here
without a decision behind it — if there's no ADR, that's a sign the decision hasn't
actually been made yet, not a gap in this document.

---

## Version Scope (if applicable)

**[PROJECT]** — if this project ships in versions with deferred features, split them
explicitly. If this is a single-release project, remove this section rather than leaving
it as an empty shell.

### {Current version}
**[PROJECT]**

### {Deferred}
**[PROJECT]**

---

*This is the global starter model. Copy into a new project's `docs-local/`, fill every
**[PROJECT]** marker, and remove this closing note. The Field Type Conventions and the
three standing Key Architectural Patterns above are hard-won operational learning — keep
them, adapt only genuinely project-specific sections. Relationship to PDLF's own process:
Step 17 (create Anvil data tables) is where this document's plan becomes the real,
physical schema — that step should read this document as its plan, not the other way
around. If the two ever diverge, this document is the one that's wrong until corrected.*
