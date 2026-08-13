---
document: Frontmatter Exemption for Transient Files
doc-id: frontmatter-exemption-transient-files
state: Live
date-created: 2026-08-12T000000+0200
---
# Frontmatter Exemption for Transient Files

Date: 2026-08-12
Status: Accepted
Source: Master Task List Task 2.2

---

## Context

GBrain's `frontmatter validate` flags 5 template files in `templates-global` as `[MISSING_OPEN]`: `tmp-authoritative-schema.md`, `tmp-chklist-anvil-app-testing.md`, `tmp-chklist-screen.md`, `tmp-chklist-wireframe.md`, `tmp-custom-component-requirements-matrix.md`. All five are `tmp-`-prefixed, transient/scratch working files, not part of the permanent, registered document corpus.

---

## Decision

**Transient files are exempt from frontmatter requirements.** A file is transient, for this purpose, if it is a working/scratch document not intended for permanent registration — identified by the `tmp-` filename prefix as the standing convention.

---

## Rationale

1. Frontmatter (`doc-id`, `state`, `date-created`) exists to support permanent identity and registration. Transient files, by definition, are not part of that permanent corpus and have no identity to track.
2. Requiring frontmatter on scratch files adds overhead with no corresponding benefit.
3. `gbrain doctor`'s general `frontmatter_integrity` summary does not surface `project-library-global` at all — this exemption does not rely on that check clearing; the targeted `gbrain frontmatter validate` command remains the correct verification tool regardless.

---

## Consequences

- The 5 named `tmp-*.md` files in `templates-global` are exempt. They should not be treated as requiring a frontmatter fix.
- This unblocks Master Task List Task 3.1, previously gated on this decision.
- Any future file using the `tmp-` prefix inherits this same exemption automatically — the rule is prefix-based, not a one-off list.
- This ADR does not address the separate, related `Instructions.md` question — see `instructions-md-per-folder-purpose-file` ADR.

---

*End of `frontmatter-exemption-transient-files` ADR*
