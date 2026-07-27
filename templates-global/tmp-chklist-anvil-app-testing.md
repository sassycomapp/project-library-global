---
document: Checklist — Anvil App Testing Suite
doc-id: global-0041
state: Live
date-created: 2026-07-25T150027+0200
---
# Checklist — Anvil App Testing Suite

**Location:** `specifications-global\checklists-global\chk-anvil-app-testing.md`

**Scope:** Tests an Anvil.works application that `C:\pdlf` builds — any project (`mb3cons`,
future projects), not PDLF itself. For testing PDLF's own orchestration, see
`chk-pdlf-self-test.md` (local, `dev-pdlf\checklists-local\`).

**Why this is global, not local:** every check here is reusable across any Anvil project
PDLF builds, regardless of which project. It doesn't reference dev-pdlf's own step numbers,
ledger, or orchestration mechanics — those live in the companion local checklist. This
document operationalizes `specifications-global\spec-testing-methodology-standards.md`
into a runnable checklist; it does not restate that document's rationale, only turns its
standards into pass/fail items.

**Relationship to `pol-testing-and-quality.md`:** that PDLF-local policy already covers
Sections 1–3 below (the three testing levels, pure-function characteristics, the two-backup
protocol) — this checklist operationalizes the same standard as runnable items, not new
content. Sections 4–5 below (Test Plan Shape, RBAC Verification) come from
`spec-testing-methodology-standards.md` §6–7, which `pol-testing-and-quality.md` does not
yet cover locally — closing that gap was the reason this document exists.

**Cadence:** run per feature, inside the Step 35 build loop (Levels 1–3 continuously during
build; the full checklist at Steps 35A/36–39). Continuous, same principle as Suite A — not
a one-time pass.

**Deferred integration, not yet done:** this checklist's content needs to be woven directly
into the relevant stepwise step files — Steps 35A, 36, 37, 38, and 39 specifically — so
that running those steps actually exercises these checks, rather than this document sitting
separately from the pipeline that should use it. That work is deferred along with the rest
of Steps 17–46, addressed when Phase D is reached, not now. This checklist is usable
standalone in the meantime.

---

## 1. Testing Level Conformance

Per feature, during Step 35's build.

| # | Check | Method |
|---|---|---|
| 1.1 | Level 1 (pure logic) tests have zero `import anvil`, no Data Tables access, no server calls, no side effects, fully deterministic | Grep the test file's imports and the function under test |
| 1.2 | Level 1 runs continuously — on every change, not just at milestones | Confirm a `run_all_tests()`-style runner exists and is actually invoked during development, not only before signoff |
| 1.3 | A failing Level 1 test is fixed immediately, not logged and deferred | Check there is no "known failing test" left in the suite at signoff |
| 1.4 | Level 2 (Uplink integration) only begins after Level 1 passes AND a pre-integration backup exists | Confirm the backup timestamp precedes the first Level 2 test run |
| 1.5 | Level 2 uses a Server Uplink key, never Client, never hardcoded — read from environment variable | Grep for the Uplink key source |
| 1.6 | Level 2 test data is marked `source='Test'` and cleanup is verified, not assumed | Query the table after cleanup, confirm zero `source='Test'` rows remain |
| 1.7 | A second backup exists after Level 2 passes, before Level 3 begins | Confirm two distinct backup timestamps, not one |
| 1.8 | Level 3 (manual E2E) only begins after both prior levels pass | Confirm sequence, not parallel or reordered execution |

## 2. Pure Function / Server Module Discipline

Per feature, code-review time (Step 37 or equivalent).

| # | Check | Method |
|---|---|---|
| 2.1 | Pure Logic Modules have zero `import anvil`, no Data Tables, no server calls, deterministic | Same as 1.1, applied to the module, not just its tests |
| 2.2 | Server Modules are thin wrappers around Pure Logic Modules — auth and persistence only, business rules live in the pure module | Read the server module; flag any business-rule logic that isn't a call-through |
| 2.3 | Test structure matches the standard: `test_[feature]_[scenario]` naming, snake_case, Arrange/Act/Assert, plain `assert` | Spot-check test file structure against the pattern |
| 2.4 | Boundary conditions (zero, minimum, maximum) are tested explicitly, not just typical inputs | Check test coverage for boundary cases per function |
| 2.5 | Error-handling tests exist per named failure scenario, with a specific expected exception/message, not a bare `except` | Check each error path has its own test, not one catch-all |

## 3. Backup Discipline

Per feature.

| # | Check | Method |
|---|---|---|
| 3.1 | Pre-integration backup exists before any Level 2 test touches the live app | Confirm backup timestamp precedes first Uplink write |
| 3.2 | Post-success backup exists after Level 2 passes | Confirm second backup timestamp |
| 3.3 | Neither backup was skipped as "redundant" | Confirm two distinct backups per feature cycle, not one combined |

## 4. Test Plan Shape

Per project, or per major feature requiring its own test specification (typically produced
in response to a specific review finding, not written speculatively).

| # | Check | Method |
|---|---|---|
| 4.1 | E2E happy-path specs exist per critical flow: preconditions, numbered steps table (action → expected result), performance gate where relevant, explicit data-validation checks | Review the test plan document against this shape |
| 4.2 | Edge cases are listed separately from the happy path, not mixed in | Check document structure |
| 4.3 | Error-path test cases exist, one per named failure scenario, each with its own specific expected behavior | Check coverage against known failure scenarios |
| 4.4 | If the project has roles, an RBAC/access coverage matrix exists | Check for a form/tab × role matrix |

## 5. RBAC Verification

Per project with roles, at QA time.

| # | Check | Method |
|---|---|---|
| 5.1 | For each form/tab in the access matrix, log in as each role and attempt access; verify granted/denied matches the matrix | Manual role-by-role walkthrough |
| 5.2 | The navigation link is hidden, not merely disabled, for restricted roles | Visual check per role — a disabled-but-visible link is a finding, not a pass |
| 5.3 | Every server function carries the required auth decorator, or is explicitly documented as intentionally public | Grep all server modules for the decorator; any function without one and without documented public status is a finding |
| 5.4 | The grep-based check (5.3) is run in addition to the manual walkthrough (5.1), not instead of it | Confirm both were actually performed — the grep catches what a manual pass can miss, and vice versa |

---

*chk-anvil-app-testing.md v1.0. Created 2026-07-18 as part of the testing-strategy
housekeeping pass. Operationalizes `spec-testing-methodology-standards.md` §1–7 into a
runnable checklist. Companion document: `chk-pdlf-self-test.md` (local,
`dev-pdlf\checklists-local\`). Integration into Steps 35A/36–39 deferred to Phase D.*