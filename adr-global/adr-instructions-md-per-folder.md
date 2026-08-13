---
document: Instructions.md — Per-Folder Purpose File
doc-id: instructions-md-per-folder-purpose-file
state: Live
date-created: 2026-08-12T000000+0200
---
# Instructions.md — Per-Folder Purpose File

Date: 2026-08-12
Status: Accepted (concept only — format not yet designed)
Source: Master Task List Task 2.2

---

## Context

Folders can carry non-obvious rules, purpose, or nuances that aren't captured anywhere else — a reader with no other context has no way to discover them locally. `Instructions.md` was introduced, on a per-folder basis, to hold exactly that.

---

## Decision

**`Instructions.md` is adopted as a per-folder file whose purpose is to clarify that folder's purpose and any non-obvious nuances relevant to working within it** — frontmatter requirements are one example of the kind of nuance it covers, not the only one.

This decision is concept-level only. It establishes that the file exists and what it is for. It does not specify format, whether every folder requires one, or the finalized filename/capitalization.

---

## Rationale

A per-folder purpose file makes local context discoverable at the point of use, rather than relying on institutional memory or a separate document someone has to already know to check.

---

## Consequences

- The standing freeze on creating further `Instructions.md` files (Master Task List Task 2.2) remains in effect — this ADR establishes the concept, not the finalized format. Do not create additional `Instructions.md` files based on this ADR alone.
- Format, scope (which folders require one), and final naming remain open, to be resolved separately.
- This ADR does not address the separate frontmatter exemption question — see `frontmatter-exemption-transient-files` ADR.

---

*End of `instructions-md-per-folder-purpose-file` ADR*
