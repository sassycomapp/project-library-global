# {Project Name} — Business Requirements Document (BRD)

**Status:** **[PROJECT]** Draft / Approved
**Date:** **[PROJECT]**
**Author:** **[PROJECT]**

**How to use this document:** every **[PROJECT]** marker must be filled before this
document is considered complete. An unfilled marker is a failure condition, same as a
stale doc. Every requirement in Section 6 must carry a certainty tag (see below) — this is
not optional formatting, it's how a reader distinguishes what's actually decided from what
you're still guessing at.

**Certainty tags** (use on every requirement, every assumption, every KPI):
`[CLEAR]` — stated explicitly, no interpretation needed. `[PARTIAL]` — direction is set,
specifics aren't. `[INFERRED]` — your best judgment, not yet confirmed by a stakeholder.
`[MISSING]` — known gap, not yet addressed. Never silently upgrade an `[INFERRED]` item to
`[CLEAR]` by dropping the tag once it feels obvious — re-tag it only once actually
confirmed.

---

## 1. Executive Summary

**[PROJECT]** 2–4 sentences: what this project is, why it's being undertaken, expected
business outcome. Written for a non-technical stakeholder — no implementation detail.

**Worked example (project `mb0test`):** *"mb0test replaces manual appointment scheduling
(currently phone + paper diary) with a self-service booking system. The business loses an
estimated 3 bookings/week to scheduling friction. Target outcome: online booking available
within one business quarter, no back-office headcount increase required to operate it."*

---

## 2. Business Problem / Opportunity

**[PROJECT]** What business problem does this solve, or what opportunity does it capture?
State the cost of doing nothing — what happens if this isn't built.

**Worked example (mb0test):** *"Problem: 30% of prospective bookings are lost because the
only booking channel is a phone call during business hours. Cost of inaction: continued
lost revenue, estimated at [$X]/month, compounding as the business's marketing spend
increases traffic to a channel that can't convert it."*

---

## 3. Business Objectives

Numbered, each measurable or at least verifiable — not aspirational language.

| # | Objective | How success is measured | Certainty |
|---|---|---|---|
| BO-1 | *(example: Reduce lost bookings due to scheduling friction)* | *(example: Booking abandonment rate, tracked monthly)* | *(e.g. [CLEAR])* |
| BO-2 | **[PROJECT]** | | |

---

## 4. Stakeholders

| Role | Name/Group | Interest |
|---|---|---|
| Sponsor | **[PROJECT]** | |
| Primary user(s) | **[PROJECT]** | |
| Other affected parties | **[PROJECT]** | |

---

## 5. Scope

### In Scope
**[PROJECT]** — bullet list, business-language, not feature-level detail (that's the
PRD's job).

### Out of Scope
**[PROJECT]** — explicitly state what this project will NOT address, even if related. An
unstated exclusion invites scope creep later.

**Worked example (mb0test) — Out of Scope:** *"Multi-provider scheduling (this business has
one practitioner); payment processing at time of booking (handled at point of service);
customer-facing mobile app (responsive web only)."*

---

## 6. Business Requirements

Numbered, one requirement per row, each traceable to an objective in Section 3. Every row
carries a certainty tag.

| # | Requirement | Satisfies Objective | Priority (Must/Should/Could) | Certainty |
|---|---|---|---|---|
| BR-1 | *(example: Customer can view available time slots and book without a phone call)* | BO-1 | Must | [CLEAR] |
| BR-2 | **[PROJECT]** | | | |

**Enforcement, not just format:** before this document is marked complete, walk this table
against Section 3 — every objective must have at least one requirement satisfying it, and
every requirement must cite a real objective number that exists. A requirement citing
nothing, or an objective satisfied by nothing, is an unresolved gap, not a formatting
choice to skip.

---

## 7. Assumptions and Constraints

**[PROJECT]** — anything assumed true that, if false, changes the requirements. Anything
constraining the solution (budget, timeline, platform, regulatory). Tag each with a
certainty level — an assumption is often exactly the kind of thing that's `[INFERRED]`
rather than `[CLEAR]`, and that distinction matters more here than almost anywhere else in
this document.

**Anvil-specific prompts, address explicitly rather than leaving to be discovered later:**
- Is this a single-instance app, or does it join the dependency-based multi-instance model
  (client instances tracking a template app)? This changes almost every downstream document.
- Single currency and immutable after first transaction, or does this project need
  multi-currency? (Most projects in this operation default to single-currency, immutable —
  state explicitly if this one differs.)
- Single timezone per instance, UTC storage with display-time conversion — confirm this is
  the assumption, or state the deviation.

---

## 8. Success Criteria / KPIs

**[PROJECT]** — how will you know, after launch, that this was worth doing? Distinct from
Section 3's objectives — this is the measurable, post-launch verification. Tag each with
certainty.

---

## 9. Risks

| Risk | Likelihood | Impact | Mitigation | Certainty |
|---|---|---|---|---|
| | | | | |

**Anvil-specific prompt:** if this project will host multiple client instances on a single
Anvil account, consider account-level failure scenarios explicitly (suspension,
compromise, platform outage) — see this operation's deployment-procedures SOP for the
standard treatment, don't reinvent it here.

---

## 10. Approval

| Role | Name | Date | Signature/Confirmation |
|---|---|---|---|

---

*This is the global starter model. Copy into a new project's `docs-local/`, fill every
**[PROJECT]** marker and replace every worked example with this project's real content,
remove this closing note. Relationship to PDLF's own artifacts: this document is the
business-language complement to Step 12's `design-doc.md` — the BRD is the standard,
portable artifact suitable for stakeholders outside the PDLF process itself;
`design-doc.md` is PDLF's internal working artifact. They should not contradict each
other, but they are not the same document and one does not replace the other. If they
diverge, that divergence is itself a finding to resolve, not something to leave open.*
