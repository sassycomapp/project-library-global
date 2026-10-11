---
title: "adr-document-frontmatter-and-identity"
doc-id: "mb-f5f31745"
updated: "2026-10-11"
---
# Document Frontmatter and Identity

Date: 2026-10-01
Status: Accepted
Source: Developer decision, 2026-10-01
Supersedes: [[[default:adr-global/adr-frontmatter-exemption-transient-files]]](C:/dev/project-library-global/adr-global/adr-frontmatter-exemption-transient-files.md) (in part: its list of frontmatter fields); [[[default:adr-global/adr-filename-and-frontmatter-numbering-policy]]](C:/dev/project-library-global/adr-global/adr-filename-and-frontmatter-numbering-policy.md) (in part — see Consequences)

---

## Context

The earlier ADRs made a document's identity its filename: `doc-id` was the filename's own slug, and `tmp-`-prefixed files were exempt from frontmatter. That identity cannot survive the one event that matters most: when a document is renamed or moved, its name — its identity — changes, and every link by name breaks. Nothing could recognise the renamed file as the same document.

One program, `mb-doc-check` ([[[mybizz-config-docs:mb-doc-check/doc-check-explainer]]](C:/mybizz/mybizz-config-docs/mb-doc-check/doc-check-explainer.md)), runs at every commit in the fifteen documentation repositories listed in [[[mybizz-os-docs:os-reference-docs/repo-organization]]](C:/mybizz/mybizz-os-docs/os-reference-docs/repo-organization.md). It keeps frontmatter and links correct as the documents enter history.

---

## Decision

1. **Every document in the documentation repositories listed in [[[mybizz-os-docs:operating-procedures/commit-all-repositories]]](C:/mybizz/mybizz-os-docs/operating-procedures/commit-all-repositories.md) carries three frontmatter fields: `title`, `doc-id`, `updated`.**
2. **`doc-id` is a permanent random code** of the form `mb-` followed by eight hexadecimal characters, for example `mb-3fa91c2e`. It is created once, never changes, is never reused and is unique across the documentation repositories listed in [[[mybizz-os-docs:operating-procedures/commit-all-repositories]]](C:/mybizz/mybizz-os-docs/operating-procedures/commit-all-repositories.md). It is not derived from the filename. This replaces "`doc-id` is the filename's own slug".
3. **`title`** is the filename without `.md`, a YAML string, always quoted.
4. **`updated`** is the date `"YYYY-MM-DD"` of the last real change to the document. It moves only when the document is new, moved, or changed in anything other than its date line or its line endings.
5. **Nobody writes or changes `doc-id` or `updated` by hand.** `mb-doc-check` adds and maintains both at commit, in WSL. A field is never named `date`.
6. **The exemptions are exactly these.** The program applies them mechanically: files whose names start with `tmp-`; folders named `stencils`, `quarantine`, `backups`, `catalogue` or `logs`; folders whose names start with `.` or `tmp-`; any folder that contains `anvil.yaml` (an Anvil app root) and everything below it; anything inside an `obsolete` folder (indexed as a link target, never edited); installed skills (`SKILL.md`, which carry `name` and `description`); and empty files. Every other document in the documentation repositories listed in [[[mybizz-os-docs:operating-procedures/commit-all-repositories]]](C:/mybizz/mybizz-os-docs/operating-procedures/commit-all-repositories.md) carries the three fields. Further fields (for example `state` and `date-created` on fact files) are allowed where a document type defines them; the hook leaves them alone.
7. **Retained from the numbering policy:** no sequence numbers in filenames or in frontmatter, with the same standing exceptions (`C:\pdlf\app-factory\` and the quarantine, retired and archived folders). References cite by name: authors write `[[name]]`, and the hook stores the link as source id, page name and path ([[[mybizz-os-docs:os-reference-docs/documentation-linking-explainer]]](C:/mybizz/mybizz-os-docs/os-reference-docs/documentation-linking-explainer.md)).

---

## Rationale

1. A permanent code is the only identity that survives a rename, a move or a complete rewrite. Because `mb-doc-check` can always recognise the document, it repairs every link to it automatically, in every repository.
2. The code is random and opaque, not a counter. There is nothing to coordinate between repositories or between agents writing at the same time, no order is implied, and nothing in it ever needs to change. The numbering policy objected to numbers that carry meaning and drift away from filenames; this code carries no meaning, is assigned once by a program, and the filename remains the document's visible name.
3. `updated` lets a reader or an agent judge how current a document is. It is set by the program so that it can be trusted. It is not called `date` because GBrain reads a field with that name as the page's own date and can use it to rank search results.
4. The exemptions are by name and by folder, never by judgment: the program applies them mechanically, so an agent never has to decide whether a file is "transient".
5. Enforcement at commit guarantees every document is correct at the moment it enters history. No periodic cleanup is needed, and no skill has to be run to find drift.

---

## Consequences

- **[[[default:adr-global/adr-frontmatter-exemption-transient-files]]](C:/dev/project-library-global/adr-global/adr-frontmatter-exemption-transient-files.md) is superseded in part.** Its list of frontmatter fields (`doc-id`, `state`, `date-created`) is replaced by the three fields above. Its exemption of `tmp-` files stays in force and is restated in Decision item 6; the five `tmp-*.md` files in `templates-global` still carry no frontmatter and are not treated as needing a fix.
- **[[[default:adr-global/adr-filename-and-frontmatter-numbering-policy]]](C:/dev/project-library-global/adr-global/adr-filename-and-frontmatter-numbering-policy.md) is superseded in part.** Its Decision item 2 ("`doc-id` is the filename's own slug") is replaced by Decision items 2 and 3 above. Its items 1 and 3, its standing exceptions and its rule that numbered files need an ADR to be introduced remain in force. Its documentation-skill Consequences are void. A sequence-numbered file in the live corpus is still an anomaly, but no tool flags it; `mb-doc-check` does not check filenames.
- The rules a document must meet are stated in [[[mybizz-config-docs:gbrain/gbrain-doc-contract]]](C:/mybizz/mybizz-config-docs/gbrain/gbrain-doc-contract.md) and [[[mybizz-os-docs:os-reference-docs/frontmatter-conventions]]](C:/mybizz/mybizz-os-docs/os-reference-docs/frontmatter%20conventions.md), which carry the same three fields.
- A commit made outside WSL, or with `--no-verify`, bypasses the hook and leaves a document without these fields until its next commit.

---

*End of `document-frontmatter-and-identity` ADR*
