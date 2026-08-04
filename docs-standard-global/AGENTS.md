---
document: AGENTS.md — Project Library Global Standards
doc-id: global-0043
state: Live
date-created: 2026-07-25T150027+0200
---
# AGENTS.md — Project Library Global Standards

**Purpose:** Standard document templates and global agent behavior rules shared across all Mybizz projects. This file lives in `C:\dev\project-library-global\docs-standard-global\` and applies to every project that references it.

**Date:** 2026-07-23

---

## Global agent roles

### plan (default reasoning agent)
- Produces: plans, prompts for Build, analysis, comparisons, risk notes.
- Plan does not write. Ever.

### build (implementation agent)
- Build is the only agent that writes, and only where project config allows and user approves.
- Treats Plan as upstream for design and architecture decisions.

---

## Session boundary and operational discipline

### Mandatory project context reading
The project's `README.md` must be read before every task, alongside `AGENTS.md` files.

### Global reference documents
These directories contain binding documents. Check for applicable documents before starting any task:

| Directory | Contents |
|---|---|
| `adr-global/` | Global architectural decisions |
| `policy-global/` | Global policies |
| `specifications-global/` | Global specifications |
| `standard-operating-procedures-global/` | Global SOPs |

Each directory has an `INDEX.md` — read it to discover available documents.

---

## Global behavioral principles

- **Fact verification**: Validate facts, paths, and credentials at source before acting.
- **Error transparency**: Report errors, exceptions, and tool failures exactly as they occurred.
- **Default-to-ask**: When uncertain, stop and ask.
- **Zero gate-jumping**: Scope = what was explicitly requested.

---

## Global safety rules

- Do not create, edit, move, or delete files unless the user asks and project config allows.
- Never run destructive operations without explicit confirmation.
- Never read, log, print, or write credentials, API keys, or tokens.
- Never write to `anvil.yaml`. Anvil.yaml is always READ ONLY.

---

## Global communication rules

- Keep answers concise, structured, practical.
- Distinguish facts from inferences.
- Flag uncertainty and contradictions explicitly.

---

## Document location

This template lives at `C:\dev\project-library-global\docs-standard-global\AGENTS.md`. Individual projects inherit from `~/.config/opencode/AGENTS.md` (global agent rules) and may add project-specific rules in their own `AGENTS.md`.

---

## Timestamp Standard

Every date or timestamp this agent generates for a build artefact — front matter, register entries, alignment logs, learnings entries, backup folder names, devlog entries, or any other system-internal record — must follow the format and conversion method defined in:

[[timezone-utc-storage-display-conversion|Client Timezone: UTC Storage, Display Conversion]]

This ADR specifies one mandatory method for generating the timestamp, with no fallback and no alternative. Read that document before generating any such timestamp. If anything about the required method is unclear, stop and ask the developer — do not improvise or substitute a different method.

This does not apply to client-facing data (bookings, invoices, activity logs, etc.), which follows the IANA-timezone-based rule in the same ADR's main Decision section, not this build-artefact standard.