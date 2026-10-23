---
title: "adr-document-frontmatter-and-identity"
doc-id: "mb-f5f31745"
updated: "2026-10-23"
---
# Document Frontmatter and Identity

Status: Accepted

---

## Context

Every MyBizz documentation repository is linked together and indexed by GBrain. A document is renamed, moved or rewritten many times in its life, and every link to it must survive. The commit hook `mb-doc-check` runs at every commit in every documentation repository and keeps frontmatter and links correct as documents enter history.

---

## Decision

1. **Every document carries three frontmatter fields: `title`, `doc-id`, `updated`.**
2. **`doc-id` is a permanent random code** of the form `mb-` followed by eight hexadecimal characters, for example `mb-3fa91c2e`. It is created once, never changes, is never reused and is unique across every documentation repository. It is not derived from the filename.
3. **`title`** is the filename without `.md`, a YAML string, always quoted.
4. **`updated`** is the date `"YYYY-MM-DD"` of the last real change to the document. It moves only when the document is new, moved, or changed in anything other than its date line or its line endings.
5. **Nobody writes or changes `doc-id` or `updated` by hand.** `mb-doc-check` adds and maintains both at commit, in WSL. A field is never named `date`.
6. **The exemptions are exactly these,** applied mechanically by the program: files whose names start with `tmp-`; folders named `stencils`, `quarantine`, `backups`, `catalogue` or `logs`; folders whose names start with `.` or `tmp-`; any folder that contains `anvil.yaml` (an Anvil app root) and everything below it; installed skills (`SKILL.md`, which carry `name` and `description`); and empty files. Further fields (for example `state` and `date-created` on fact files) are allowed where a document type defines them; the hook leaves them alone.
7. **No sequence numbers in filenames or in frontmatter.** A document's identity is its descriptive filename and its `doc-id`. Ordering, where it matters, comes from dates or from content structure, never from a leading counter. The one exception is the app factory's steps, whose numbers are the order of a procedure, not an index.
8. **References cite by name, never by number.** Authors write `[[name]]`, and the hook stores the link as source id, page name and path.

---

## Rationale

1. A permanent code is the only identity that survives a rename, a move or a complete rewrite. Because `mb-doc-check` can always recognise the document, it repairs every link to it automatically, in every repository.
2. The code is random and opaque, not a counter. There is nothing to coordinate between repositories or between agents writing at the same time, no order is implied, and nothing in it ever needs to change. The filename remains the document's visible name.
3. A number in a filename or a field is a second, fragile identity: it drifts from the filename, and a citation by number breaks when the document moves.
4. `updated` lets a reader or an agent judge how current a document is. It is set by the program so that it can be trusted. It is not called `date` because GBrain reads a field with that name as the page's own date and can use it to rank search results.
5. The exemptions are by name and by folder, never by judgment, so an agent never has to decide whether a file is exempt.
6. Enforcement at commit guarantees every document is correct at the moment it enters history. No periodic cleanup is needed.

---

## Consequences

- A sequence-numbered file in a documentation repository is an anomaly. `mb-doc-check` does not check filenames, so this ADR is the rule to point to.
- A commit made outside WSL, or with `--no-verify`, bypasses the hook and leaves a document without these fields until its next commit.
