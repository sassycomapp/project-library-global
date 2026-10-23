---
title: "pol-testing-and-quality"
doc-id: "mb-b7965794"
updated: "2026-10-23"
---
# Policy — Testing and Quality

**Binding.** All feature development on any Anvil.works project under this operation must
conform. No exceptions without documented justification.

---

## What

### Testing Follows the Test Suite

Every step and every feature is tested as the test suite in `C:\dev\project-library-global\test-suite\` sets out: [[[default:test-suite/ts-method]]](C:/dev/project-library-global/test-suite/ts-method.md) says how, [[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md) holds the tests, and each step's `{step}-test-spec.md` names the tests it runs. [[[default:specifications-global/spec-testing-methodology-standards]]](C:/dev/project-library-global/specifications-global/spec-testing-methodology-standards.md) describes the levels of testing. No level is skipped.

### Tests Run Locally First

Tests run first on the Anvil App Server on the developer's computer, with an empty database, so nothing live is touched. Only what needs Anvil's hosted service is tested on hosted App 1, with `TEST_` data removed afterwards. The local runtime and the test client take the place of a staging environment; the Hobby plan has none.

### Two Uplink Keys

A server Uplink key sets up and inspects test data only, because it passes every access check. A client Uplink key, signed in as a `TEST_` user of each role, is the only way access rules are proven. Both keys live only in `.env`, never committed.

### Backups Around Hosted Runs

App 1 is backed up before any test run against hosted App 1, because the integration attempt itself can go wrong, and again once it passes, as the known-good checkpoint. Local runs need no backup. Never back up a failing state.

### Feature Signoff

A feature is not complete until it has passed the full testing sequence and the developer
has explicitly signed off. The Step Receipt records the sign-off. After sign-off, the feature
is a known-good baseline: later breakage is attributable to something done after this point,
not to this feature. The next feature starts only after sign-off.

### RBAC Verification Is Part of Testing, Not Separate

Per [[[default:specifications-global/spec-testing-methodology-standards|Testing Methodology Standards]]](C:/dev/project-library-global/specifications-global/spec-testing-methodology-standards.md) §7, every feature with role-based access
is proven by calling every server function as every role through the client Uplink key (test IN-02), by the scanner's check for a missing access rule on any server function (test ST-02), and by a browser walkthrough of each role's navigation (test BR-03).

### A Finding Is Not Resolved Until Verified

A test failure, a review finding, or a QA finding is not closed by the fix being written —
it's closed once the fix is verified against the original failure condition.

---

## Why

Untested integration work is where this operation's own experience says real damage
happens — a change that touches the live app without prior verification is "a fast way to
land in trouble... deep trouble you cannot dig your way out of." The backup rule looks
redundant until the first time the integration attempt itself, not the code being
integrated, is what goes wrong — the backup before a hosted run protects against that
specific failure mode. Running locally first keeps attacks and broken code away from every hosted app.

---

## Where

Every project this operation builds on Anvil.works, from the first feature onward.
