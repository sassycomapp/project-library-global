---
document: Filename and Front-Matter Numbering Policy
doc-id: adr-filename-and-frontmatter-numbering-policy
state: Live
date-created: 20260910T103452+0200
---
# Filename and Front-Matter Numbering Policy

Date: 2026-09-10
Status: Accepted
Source: Developer decision, 2026-09-10 (numbering investigation with OpenCode)

---

## Context

The numbering of documents was decided in different directions at different times:
an earlier era used numeric document identifiers (`global-0037`-style doc-ids,
`DOC-INDEX` numbering), while the later regime moved to name-based identity
(`doc-id` = the filename's own slug, per the register convention). The two regimes
coexisted uneasily: file numbering and front-matter numbering drifted apart, citations
by number broke when documents moved between registers, and the numbers added no
indexing value — search and the registers resolve by name and folder, not by
sequence position. A numeric identifier is a second, fragile identity layered on top
of the filename, which is the thing that already keeps silently breaking elsewhere.

An investigation of the full scaffold (2026-09-10) confirmed the current state: the
live planning corpus contains **zero sequence-numbered files** — every apparent hit
was a product name (Material 3, Kubernetes), a version marker (`v1`), a date-stamped
report, or non-live content in quarantine/retired folders. No front-matter field in
the live corpus carries a numeric identifier, and no live file cites a numeric
document id (the last known citation, `global-0037`, was removed 2026-09-10).

---

## Decision

**Files are not numbered — anywhere in the scaffold, in filenames or in front
matter.** Numbering is an exception, never the rule. Specifically:

1. **No sequence numbers in filenames.** A document's identity is its descriptive
   filename (e.g. `[[adr-design-rules]]`), permanent and never reused. Ordering, where
   it matters, comes from dates or from content structure — never from a leading
   counter.
2. **No numeric identifiers in front matter.** `doc-id` is the filename's own slug.
   No `doc-number`/sequence field exists now and none is added later; front matter
   stays identity-only and small (see the front-matter schema and the register's
   field definitions).
3. **References cite by filename**, never by number.

### Standing exceptions

- **`{slug}-project-library\stepwise\`** — a sequence of numbered *steps*. This is
  content that is inherently ordinal (a procedure's execution order), not
  file-numbering for indexing. It is not a violation of this policy and not a
  precedent for numbering elsewhere.
- **Quarantine, retired, and archived folders** — numbered files surviving from the
  old regime are historical material outside the live corpus. They are documented,
  not renamed; renaming retired content is pointless churn and conflicts with the
  identity-immutability rule.

---

## Consequences

- A sequence-numbered file appearing in the **live** corpus is an anomaly — a
  genuine finding for the documentation-management skills (mb-docs-manager flags it;
  mb-align-docs treats it as an identity/lifecycle defect), with this ADR as the
  policy to point to.
- The skills' false-positive risk is bounded by the two carve-outs above: stepwise
  content and non-live folders are never flagged.
- Any future proposal to introduce numbered files or numeric ids must amend or
  supersede this ADR — it cannot be introduced silently as a local convenience.
