---
document: "{Project Name} — Software Requirements Specification (SRS)"
doc-id: global-0047
state: Live
date-created: 2026-07-25
---
# {Project Name} — Software Requirements Specification (SRS)

**Status:** **[PROJECT]** Draft / Approved
**Date:** **[PROJECT]**
**Author:** **[PROJECT]**
**Derived from:** **[PROJECT]** this project's PRD — every requirement below should trace
back to a functional or non-functional requirement there.

**Certainty tags** (use on every requirement): `[CLEAR]` / `[PARTIAL]` / `[INFERRED]` /
`[MISSING]` — same discipline as the BRD and PRD.

---

## 1. Introduction

### 1.1 Purpose
**[PROJECT]** What this document specifies, and who it's for (developers, QA — a
technical audience, distinct from the PRD's product audience).

### 1.2 Scope
**[PROJECT]** What system/subsystem this SRS covers. Cross-reference the PRD's scope
section rather than restating it.

### 1.3 Definitions and Acronyms
**[PROJECT]** Project-specific terminology. If `CONTEXT.md` already exists for this
project (produced at PDLF Step 16), reference it directly rather than duplicating — this
section should only hold terms specific to this SRS that aren't already in the domain
glossary. Do not let this section and `CONTEXT.md` silently diverge on the same term.

### 1.4 References
**[PROJECT]** — this project's BRD, PRD, ADRs, and any external standards this SRS
depends on.

---

## 2. Overall Description

### 2.1 Product Perspective
**[PROJECT]** Where this fits relative to other systems. State explicitly: standalone
Anvil app, or a dependent instance of the multi-instance model (tracking a template app)?
This single fact governs a large share of Sections 3.1–3.4 below.

### 2.2 Product Functions
**[PROJECT]** High-level summary of major functions — one line each, detail lives in
Section 3.

### 2.3 User Characteristics
**[PROJECT]** Technical proficiency, accessibility needs, or other characteristics of the
intended users that constrain design.

### 2.4 Constraints
Anvil's own platform constraints apply by default — no programmatic Data Table schema API
(schema changes are manual, per instance); no self-hosted fallback; deployment via named
Deployment Environments. **[PROJECT]** — add anything specific to this project beyond the
platform default.

### 2.5 Assumptions and Dependencies
**[PROJECT]** Anything assumed true for these requirements to hold; anything this depends
on that's outside this project's control.

---

## 3. Specific Requirements

### 3.1 Functional Requirements

One row per requirement, each traceable to the PRD.

| # | Requirement | Traces to PRD | Verification Method | Certainty |
|---|---|---|---|---|
| SR-1 | *Booking creation writes a row to the bookings table with status='confirmed' and triggers a confirmation email.* | FR-1 | *Level 2 Uplink test — see `chk-anvil-app-testing.md` §1* | [CLEAR] |
| SR-2 | **[PROJECT]** | | | |

**Enforcement, not just format:** every PRD functional requirement this SRS is meant to
cover must appear in this table at least once. A PRD requirement with no corresponding SR
row is a gap — walk the two documents side by side before marking this complete.

### 3.2 External Interface Requirements

**[PROJECT]** — user interfaces, hardware interfaces (if any), software interfaces
(APIs/integrations consumed or exposed — cite this project's integration SOP rather than
restating vendor details), communication interfaces.

### 3.3 Performance Requirements

**[PROJECT]** Response time, throughput, capacity — concrete numbers, not "fast" or
"scalable." Any operation expected to exceed 22 seconds must use
`@anvil.server.background_task` (Anvil platform constraint — not a project-specific
choice, state it here as inherited).

### 3.4 Design Constraints

**[PROJECT]** Constraints imposed by standards, hardware limitations, or existing
architecture decisions (cite the relevant ADR by name rather than restating its content).

### 3.5 Non-Functional Requirements

If the PRD's Section 6 already covers this at product level, this section adds only the
implementation-level detail the PRD doesn't specify — e.g. the PRD says "RBAC required,"
this section specifies the actual decorator pattern and which roles exist.

**[PROJECT]** — reliability, availability, security, maintainability, at implementation
level.

---

## 4. Appendices

**[PROJECT]** Supporting diagrams, data models, or analysis referenced above but too
detailed to inline.

---

*This is the global starter model. Copy into a new project's `docs-local/`, fill every
**[PROJECT]** marker and replace the worked example with this project's real content,
remove this closing note. Relationship to PDLF's own process: Step 15
(`/plan-eng-review`) performs the pipeline's own deep architecture/edge-case review — this
SRS is the standard, portable technical artifact; it complements that review, it does not
substitute for it, and the two should be reconciled, not left to silently diverge.*