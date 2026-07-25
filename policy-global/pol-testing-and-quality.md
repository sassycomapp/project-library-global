---
document: Policy — Testing and Quality
doc-id: global-0054
state: Live
date-created: 2026-07-25T150027+0200
---
# Policy — Testing and Quality

**Binding.** All feature development on any Anvil.works project under this operation must
conform. No exceptions without documented justification.

---

## What

### Testing Methodology Is Mandatory, Not Advisory

Every feature is built and verified per `spec-testing-methodology-standards.md` — the
three-level testing model (pure logic, Uplink integration, manual verification), in
strict sequence, no level skipped.

### Two Backups Per Feature, Both Mandatory

A pre-integration backup, before any integration code touches the live app, and a
post-success backup, once integration testing passes. Neither is optional; neither
substitutes for the other. Never back up a failing state.

### Feature Signoff

A feature is not complete until it has passed the full testing sequence and the developer
has explicitly signed off. After signoff, the feature is a known-good baseline — later
breakage is attributable to something done after this point, not to this feature.

### RBAC Verification Is Part of Testing, Not Separate

Per `spec-testing-methodology-standards.md` §7, every feature with role-based access
gets both a manual per-role walkthrough and a mechanical grep for missing auth decorators.
Neither alone is sufficient — the manual pass catches UX leaks (a disabled-but-visible
link); the grep catches what a manual pass misses.

### A Finding Is Not Resolved Until Verified

A test failure, a review finding, or a QA finding is not closed by the fix being written —
it's closed once the fix is verified against the original failure condition.

---

## Why

Untested integration work is where this operation's own experience says real damage
happens — a change that touches the live app without prior verification is "a fast way to
land in trouble... deep trouble you cannot dig your way out of." The two-backup rule looks
redundant until the first time the integration attempt itself, not the code being
integrated, is what goes wrong — the pre-integration backup is what protects against that
specific failure mode, not the post-success one.

---

## Where

Every project this operation builds on Anvil.works, from the first feature onward.

**Source:** `spec-testing-methodology-standards.md`; testing discipline validated across
prior project practice, not invented fresh for this policy.
