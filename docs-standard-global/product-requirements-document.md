---
document: "{Project Name} — Product Requirements Document (PRD)"
doc-id: global-0046
state: Live
date-created: 2026-07-25T150027+0200
---
# {Project Name} — Product Requirements Document (PRD)

**Status:** **[PROJECT]** Draft / Approved
**Date:** **[PROJECT]**
**Author:** **[PROJECT]**
**Derived from:** **[PROJECT]** this project's BRD — every functional requirement below
should trace back to a business requirement there, directly or indirectly.

**Certainty tags** (use on every requirement): `[CLEAR]` / `[PARTIAL]` / `[INFERRED]` /
`[MISSING]` — same discipline as the BRD. Never upgrade a tag without actual confirmation.

---

## 1. Overview

**[PROJECT]** What is being built, in product terms — not business terms (that's the BRD)
and not implementation terms (that's design/architecture docs downstream).

---

## 2. Goals and Non-Goals

### Goals
**[PROJECT]** What this product release is trying to achieve.

### Non-Goals
**[PROJECT]** Explicitly state what's deliberately excluded from this release, even if it
seems like an obvious extension. Prevents scope creep during build.

**Worked example (mb0test):** *Goal: "Enable self-service booking end to end." Non-goal:
"Provider-side calendar sync with external calendars — deferred, tracked as a future
enhancement, not silently forgotten."*

---

## 3. Target Users

**[PROJECT]** Who uses this. If there are multiple roles/personas, list each with their
primary need.

| User type | Primary need | Frequency of use |
|---|---|---|
| *(example: Customer)* | *(Book/cancel an appointment without calling)* | *(Occasional)* |
| *(example: Provider)* | *(See and manage their own schedule)* | *(Daily)* |
| **[PROJECT]** | | |

**Anvil-specific prompt:** if this project has more than one user type, does it need
role-based access control? If yes, that's a Non-Functional Requirement (Section 6) and an
RBAC access matrix belongs in this project's own test plan, per
`chk-anvil-app-testing.md` §5.

---

## 4. User Stories / Use Cases

Standard shape: *As a [user type], I want [capability], so that [benefit].*

| # | User Story | Priority (Must/Should/Could) | Certainty |
|---|---|---|---|
| US-1 | *As a customer, I want to see available time slots, so that I can book without calling.* | Must | [CLEAR] |
| US-2 | **[PROJECT]** | | |

---

## 5. Functional Requirements

One row per discrete, testable requirement. Each traces to a user story above.

| # | Requirement | Satisfies User Story | Acceptance Criteria | Certainty |
|---|---|---|---|---|
| FR-1 | *Customer can select an available slot and confirm a booking in one flow.* | US-1 | *A confirmed booking record exists; slot no longer shown as available.* | [CLEAR] |
| FR-2 | **[PROJECT]** | | | |

**Enforcement, not just format:** every user story must have at least one functional
requirement satisfying it, and every requirement must cite a real user story that exists.
Walk this cross-check before marking the document complete — an orphaned requirement or an
unsatisfied story is a gap, not a formatting nicety.

---

## 6. Non-Functional Requirements

Pre-populated with the categories that come up on nearly every Anvil app this operation
builds, per its own ADRs and testing standards. State explicitly if a category genuinely
doesn't apply — don't leave a row blank without saying why.

| Category | Requirement | Certainty |
|---|---|---|
| Performance | **[PROJECT]** | |
| Security | **[PROJECT]** — at minimum: does this project use Vault for credentials? TOTP step-up? | |
| Accessibility | **[PROJECT]** | |
| Availability | **[PROJECT]** — single Anvil account is a single point of failure; state if this is an accepted risk (see deployment-procedures SOP) | |
| Access control (RBAC) | **[PROJECT]** — does this project have roles? If yes, every server function needs an auth decorator per `chk-anvil-app-testing.md` §5 | |
| Timezone handling | **[PROJECT]** — default assumption: UTC storage, display-time conversion, per-instance IANA timezone. State if this project deviates. | |
| Currency handling | **[PROJECT]** — default assumption: single system currency, immutable after first transaction. State if this project deviates. | |
| Color/theming compliance | **[PROJECT]** — M3 theme + approved overlay, no hardcoded colors ([[AGENTS|AGENTS.md]] Hard Rule 2) — confirm no project-specific exception needed |

---

## 7. Out of Scope

**[PROJECT]** Distinct from Non-Goals (Section 2) — this is feature-level detail
specifically deferred to a later release, not excluded from the product's vision entirely.

---

## 8. Dependencies

**[PROJECT]** External systems, other in-progress work, or platform constraints this
depends on. If this project depends on the dependency-based multi-instance model
(tracking a template app's `stable` branch), state that explicitly here — it affects how
every later release is delivered.

---

## 9. Open Questions

**[PROJECT]** Anything genuinely undecided at the time this document was written. Do not
silently resolve these by omission — an open question stays listed, tagged `[MISSING]`,
until it's actually answered and the document updated.

---

## 10. Success Metrics

**[PROJECT]** How will this specific release's success be measured, post-launch. May be a
subset of the BRD's broader KPIs, scoped to what this release specifically changes.

---

*This is the global starter model. Copy into a new project's `docs-local/`, fill every
**[PROJECT]** marker and replace every worked example with this project's real content,
remove this closing note. Relationship to PDLF's own process: Steps 14–15 (CEO review, Eng
review) perform a deeper, adversarial version of Sections 5–6 as part of the pipeline
itself — this PRD is the standard, portable artifact suitable for external reference; it
does not replace that review, and should be reconciled against it, not treated as a
substitute for it. If they diverge, resolve the divergence, don't let both stand.*