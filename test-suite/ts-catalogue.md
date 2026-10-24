---
title: "ts-catalogue"
updated: "2026-10-24"
doc-id: "mb-2b95aede"
---
# Test Suite — Catalogue

## What it is

Every test a Mybizz application is proven by, with its ID. Steps name these IDs in their test specifications. How tests are run, where, and with what evidence is in [[[default:test-suite/ts-method]]](C:/dev/project-library-global/test-suite/ts-method.md). "Basis" names the rule or standard the test proves: ASVS numbers refer to OWASP ASVS 5.0.

| Family | Tests | What it proves |
|---|---|---|
| `DC` | 15 | Plans, designs and documents are complete, consistent and testable |
| `ST` | 13 | The code and schema obey Mybizz's rules (scanner and static tools) |
| `LG` | 7 | Business rules are right |
| `IN` | 18 | Server code, data, access, services and endpoints work together |
| `SC` | 18 | Attacks fail; the security target is met |
| `BR` | 9 | Features work for real users |
| `RL` | 12 | Releases are safe and reversible; instances stay healthy |
| `DM` | 10 | The business domains (bookings and services; catalogue, cart and orders) behave correctly |
| **Total** | **102** | |

---

## DC — Documents and designs

| ID | Test | Passes when | Level · where | Basis |
|---|---|---|---|---|
| DC-01 | Success is measurable and requirements are testable | Every success criterion has a metric, a threshold and a method; no requirement uses a vague term (fast, easy, secure, etc.) or bundles two needs | D · design doc, plans, tickets | ISO/IEC/IEEE 29148 |
| DC-02 | The design doc is complete | It has every section of its fixed structure; its constraints state one app and one database per client, server authority, public client code, the Hobby plan and POPIA; it lists the 14 common aspects as shared or deviating | D · design doc | [[[default:policy-global/pol-common-aspects-for-mybizz-anvil-applications]]](C:/dev/project-library-global/policy-global/pol-common-aspects-for-mybizz-anvil-applications.md); [[[default:specifications-global/spec-regulatory-compliance-baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md) |
| DC-03 | The CEO review settles scope, data and law | Goals, non-goals and out-of-scope are clear; every kind of data has its owner, readers, writers, protection level and retention; POPIA, GDPR and PCI SAQ A are decided; the client's exit is planned; a typical client fits the Hobby limits | D · reviewed plan | ASVS 14.1; [[[default:specifications-global/spec-security-architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md) section 4; [[[default:adr-global/adr-client-r2-storage-and-exit-handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md) |
| DC-04 | The test plan is complete | Every critical flow has its steps and expected results, edge cases, error paths, performance budget and the catalogue test IDs it uses; every lifecycle is a state machine with allowed and forbidden transitions | D · test plan | [[[default:specifications-global/spec-testing-methodology-standards]]](C:/dev/project-library-global/specifications-global/spec-testing-methodology-standards.md) section 6 |
| DC-05 | The access matrix is complete | `access-matrix.yaml` lists every server function, form and settings tab against every role (all rows, own rows, none), with the fields each role may read and change, and it parses | D · project library | ASVS 8.1; [[[default:specifications-global/spec-security-architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md) section 1 |
| DC-06 | The threat model is complete | Every trust boundary (browser to server, server to each service, App 5 to the instance, role to role, instance to its storage) lists its threats, its control, who owns the control (Anvil or the app) and its test IDs | D · threat model | [[[default:security-global/requirements/sec-requirements-architecture-review]]](C:/dev/project-library-global/security-global/requirements/sec-requirements-architecture-review.md); [[[default:security-global/cloud/sec-anvil-platform-responsibility-boundary]]](C:/dev/project-library-global/security-global/cloud/sec-anvil-platform-responsibility-boundary.md) |
| DC-07 | Security decisions are written down | The plan states: sign-in and second-factor rules, session periods, secrets and where each lives with its maximum age, security events to log, limits on expensive functions, outbound hosts, and every server package with its review | D · reviewed plan | ASVS 6.1, 7.1, 11.1, 13.1, 15.1, 16.1; [[[default:security-global/infrastructure/sec-dependency-skill-supply-chain]]](C:/dev/project-library-global/security-global/infrastructure/sec-dependency-skill-supply-chain.md) |
| DC-08 | The plan obeys the common aspects and the rules | Each of the 14 common aspects is met or has its ADR; the conformance checks that apply are selected; any contradiction between rules is settled at its source | D · reviewed plan | [[[default:test-suite/ts-conformance-checks]]](C:/dev/project-library-global/test-suite/ts-conformance-checks.md) |
| DC-09 | The vocabulary is sound | Every term has one meaning; every entity has an owner and a place in the data design; shared terms match `spec-nomenclature`; "multi-tenant" is never used for the five-app model | D · `CONTEXT.md` | [[[default:specifications-global/spec-nomenclature]]](C:/dev/project-library-global/specifications-global/spec-nomenclature.md) |
| DC-10 | The tickets cover the plan, in order | No cycle in their order; every feature has a ticket and every ticket a feature; shared components first; each ticket names its acceptance and security tests by ID | D · `pdlf-tickets\` | The application's plan |
| DC-11 | The concept has no contradictions | Every pair of concept documents was checked and the report names each pair | D · Step 21 inputs | Consistency of the concept documents |
| DC-12 | The design system is readable and in bounds | Every text and control colour pair reaches WCAG 2.2 AA contrast (4.5:1 text, 3:1 controls) in light and dark mode; all seven dark tokens are defined; excluded components are named | D · `DESIGN.md` | WCAG 2.2; [[[default:adr-global/adr-dark-mode]]](C:/dev/project-library-global/adr-global/adr-dark-mode.md) |
| DC-13 | Wireframes and screens are faithful and conform | Stage 1: exactly the components needed, nothing extra. Stage 2: no hard-coded colour, only Material 3 components, naming prefixes, dark mode and reduced motion, none of the forbidden documentation patterns; a picture exists for every screen | D/0 · wireframes, screens | [[[default:specifications-global/spec-screen-and-wireframe-production-standards]]](C:/dev/project-library-global/specifications-global/spec-screen-and-wireframe-production-standards.md); [[[default:adr-global/adr-design-rules]]](C:/dev/project-library-global/adr-global/adr-design-rules.md) |
| DC-14 | The release is documented | Release notes; a migration plan for any schema change, with its rollback; before the first release, the Privacy Policy, Terms of Service and Cookie Policy | D · project library | [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md); [[[default:specifications-global/spec-regulatory-compliance-baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md) |
| DC-15 | Lessons are written back | Every fault that escaped has its root cause, its new test and the corrected source document | D · lessons | [[[default:adr-global/adr-common-architecture-across-mybizz-applications]]](C:/dev/project-library-global/adr-global/adr-common-architecture-across-mybizz-applications.md) (lessons written back) |

## ST — Static checks

Run by `tools\ts_scan.py`, except ST-01 and ST-13.

| ID | Test | Passes when | Level · where | Basis |
|---|---|---|---|---|
| ST-01 | The app validates | `anvil --json validate .` reports no error | 0 · app folder | Anvil's skills |
| ST-02 | Every server function carries its access rule | Every callable has the access decorator or is on the public list; its roles equal the access matrix; every entry point is rate-limited | 0 · scanner | [[[default:policy-global/pol-security-and-data-governance]]](C:/dev/project-library-global/policy-global/pol-security-and-data-governance.md); [[[default:specifications-global/spec-security]]](C:/dev/project-library-global/specifications-global/spec-security.md) |
| ST-03 | Secrets stay secret | Only the vault module reads Anvil Secrets, once; no key or password is in code, client code, theme or git history | 0 · scanner, gitleaks | [[[default:security-global/secrets/sec-master-encryption-key-protection]]](C:/dev/project-library-global/security-global/secrets/sec-master-encryption-key-protection.md); [[[default:specifications-global/spec-vault-system]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md) |
| ST-04 | No dangerous code | No `eval`, `exec`, `pickle`, shell commands or SQL built from strings; no `random` for tokens; email headers and uploads checked | 0 · scanner | ASVS 1.2, 1.3, 1.5, 11.5 |
| ST-05 | Errors are handled | No bare or silent `except`; the Vault guard's error is never swallowed; no exception text is returned to the client; no `print` in server code | 0 · scanner | [[[default:specifications-global/spec-anvil-platform-standards]]](C:/dev/project-library-global/specifications-global/spec-anvil-platform-standards.md) section 2; ASVS 16.5 |
| ST-06 | Nothing separates clients by filtering | No tenant-style column or code (`tenant`, `client_id`, `org_id`, `instance_id`) | 0 · scanner | [[[default:adr-global/adr-dependency-based-not-multi-tenant]]](C:/dev/project-library-global/adr-global/adr-dependency-based-not-multi-tenant.md) |
| ST-07 | The schema obeys the data rules | Every table refuses client access; has `created_at`; core tables have a `metadata` column; the five log and control tables exist; no secret column; times are datetimes | 0 · scanner | [[[default:specifications-global/spec-anvil-platform-standards]]](C:/dev/project-library-global/specifications-global/spec-anvil-platform-standards.md) sections 10, 13 |
| ST-08 | Money and time are exact | No floating-point money; times made in UTC on the server | 0 · scanner | [[[default:adr-global/adr-timezone-utc-storage-display-conversion]]](C:/dev/project-library-global/adr-global/adr-timezone-utc-storage-display-conversion.md) |
| ST-09 | Integrations follow the patterns | Webhook handlers verify, log, hand off and return; outbound calls use the shared caller; searches are bounded; exports are audited | 0 · scanner | [[[default:adr-global/adr-webhook-architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md); [[[default:specifications-global/spec-integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md) |
| ST-10 | The structure is right | Pure modules are pure; nothing test-only in the app; `.gitignore` covers `.env` and caches; only approved dependency apps; packages pinned; App 3 and client instances hold no code; App 2 equals App 1's release tag | 0 · scanner | [[[default:adr-global/adr-client-instance-architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) |
| ST-11 | Forms obey the UI rules | Only Material 3 components; no `HTMLTemplate`, `Label` or Anvil Extras; no hard-coded colour; `wrap_on` instead of pixel breakpoints; loop handlers bind their variables; no `navigate_to`; no server call inside a loop | 0 · scanner | [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md); [[[default:adr-global/adr-htmltemplate-use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md) |
| ST-12 | Sign-in settings are right | "Require secure passwords", "Require 2-factor authentication" and email confirmation are on; remember-me and remembered second factor at most 7 days; embedding off | 0 · scanner | ASVS 6.2, 6.3.3, 7.3 |
| ST-13 | Static analysis and dependencies are clean | bandit finds no high issue; pip-audit finds no known vulnerability past its fix window (Critical 7 days, High 30); `/cso` findings are decided | 0 · WSL | ASVS 15.2; OWASP Top 10 A03 |

## LG — Logic

Local Python, against pure modules.

| ID | Test | Passes when | Basis |
|---|---|---|---|
| LG-01 | Each behaviour is built test-first | Its test is saved failing before the code and passing after | `tdd` |
| LG-02 | Every rule is tested at its edges | Each function is tested with valid input, values just below, at and above each limit, empty and odd input, and the hostile corpus | ISTQB boundary analysis |
| LG-03 | Lifecycles allow only their transitions | Every allowed transition succeeds when its guard holds; every forbidden one is refused | DC-04 |
| LG-04 | Money is exact | Totals equal the sum of lines; rounding follows the set rule; discounts never go below zero; refunds never exceed payments; amounts are in the system currency | [[[default:adr-global/adr-system-currency-selection-and-immutability]]](C:/dev/project-library-global/adr-global/adr-system-currency-selection-and-immutability.md) |
| LG-05 | Time is right everywhere | Rules hold at midnight, month and year ends, 29 February and a daylight-saving change; UTC converts to the client's zone for display | [[[default:adr-global/adr-timezone-utc-storage-display-conversion]]](C:/dev/project-library-global/adr-global/adr-timezone-utc-storage-display-conversion.md) |
| LG-06 | Tests test the real code | Modules load from their own files without Anvil; no test holds a copy of the code | [[[default:test-suite/ts-method]]](C:/dev/project-library-global/test-suite/ts-method.md) rule 3 |
| LG-07 | Every fixed fault has its test | The test fails on the code before the fix and passes after | [[[default:security-global/testing/sec-testing-regression-prevention]]](C:/dev/project-library-global/security-global/testing/sec-testing-regression-prevention.md) |

## IN — Integration

Local runtime unless "hosted" is stated. Access is always proven through a client connection.

| ID | Test | Passes when | Basis |
|---|---|---|---|
| IN-01 | The app runs on the local runtime | It starts on an empty database and answers a call | [[[default:test-suite/ts-method]]](C:/dev/project-library-global/test-suite/ts-method.md) section 3 |
| IN-02 | Every role reaches exactly what the matrix allows | Every function, called as every role and signed out, succeeds or is refused as `access-matrix.yaml` says, and a refused call changes nothing | ASVS 8.2, 8.3; [[[default:security-global/threat-models/sec-privilege-escalation]]](C:/dev/project-library-global/security-global/threat-models/sec-privilege-escalation.md) |
| IN-03 | Users reach only their own records | A Staff member or Customer cannot list, fetch by id, change or download another's records | [[[default:security-global/threat-models/sec-broken-access-control-within-instance]]](C:/dev/project-library-global/security-global/threat-models/sec-broken-access-control-within-instance.md); [[[default:security-global/threat-models/sec-insecure-direct-object-reference]]](C:/dev/project-library-global/security-global/threat-models/sec-insecure-direct-object-reference.md) |
| IN-04 | Functions give and take only allowed fields | Each function returns only its allowed fields (never password hashes, second factors, secrets or other people's data) and ignores fields the caller may not set (role, owner, price, status) | ASVS 8.2.3, 15.3.1, 15.3.3 |
| IN-05 | Operations are safe under failure and contention | A multi-step operation leaves nothing half-done when it fails; two requests at once for the same limited thing (slot, stock, code, refund) let exactly one succeed | ASVS 2.3.3, 2.3.4; [[[default:security-global/threat-models/sec-business-logic-race-conditions]]](C:/dev/project-library-global/security-global/threat-models/sec-business-logic-race-conditions.md) |
| IN-06 | The server sets every amount and every order of steps | Payment functions ignore amounts sent by the caller; flows cannot skip a step; documented limits hold | [[[default:security-global/threat-models/sec-payment-manipulation]]](C:/dev/project-library-global/security-global/threat-models/sec-payment-manipulation.md); ASVS 2.3.1, 2.3.2 |
| IN-07 | Webhooks are verified, quick and exactly-once | A valid event gets 200 within 5 seconds, is processed once and its payload stored with its index row; a forged, altered or old event gets 400 and changes nothing; a repeat changes nothing; events out of order end correctly; an event that could not be handed off is reconciled (local; hosted with real test-mode deliveries) | [[[default:adr-global/adr-webhook-architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md); [[[default:specifications-global/spec-api-specification]]](C:/dev/project-library-global/specifications-global/spec-api-specification.md) 2.4 |
| IN-08 | Outside services can fail safely | A 429 is retried with growing waits; a 500 or time-out is logged and reported; a retried payment never charges twice | [[[default:specifications-global/spec-integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md); ASVS 16.5.2 |
| IN-09 | Emails are right | Each email has the right recipient, sender, content and unsubscribe link (local mail catcher); sign-up and reset emails arrive on hosted App 1 | [[[default:specifications-global/spec-integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md) section 6 |
| IN-10 | Storage works and stays the client's | Objects are stored, read and listed in the client's bucket with index rows; retention removes old index rows only | [[[default:adr-global/adr-client-r2-storage-and-exit-handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md) |
| IN-11 | Background and scheduled tasks work | Each finishes, is safe to run twice, logs failures and fits its time budget; each scheduled task acts correctly at its times (clock passed in) and runs as scheduled on hosted App 1 | [[[default:adr-global/adr-real-time-and-background-tasks]]](C:/dev/project-library-global/adr-global/adr-real-time-and-background-tasks.md) |
| IN-12 | Mybizz's links to the instance are secure | The heartbeat reports health, release version and schema fingerprint, and never blocks when App 5 is down; management endpoints obey only that instance's token and refuse others with 403 | [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md); [[[default:security-global/cloud/sec-management-service-authentication]]](C:/dev/project-library-global/security-global/cloud/sec-management-service-authentication.md) |
| IN-13 | The Vault keeps secrets secret | Stored values are encrypted; reads show `***`; only the Owner opens it, with a fresh second factor each time; each access is audited and notified; saving a secret anywhere else fails loudly | [[[default:specifications-global/spec-vault-system]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md); [[[default:adr-global/adr-payment-security-boundary-vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) |
| IN-14 | Clients' and people's data rights work | The exit export holds every table in full, the key and the Vault contents, in files standard tools open; one person's data can be exported, corrected and erased (transactions kept for 7 years); retention deletes on time | [[[default:specifications-global/spec-regulatory-compliance-baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md); [[[default:adr-global/adr-client-data-management-rights-and-mybizz-retention-boundary]]](C:/dev/project-library-global/adr-global/adr-client-data-management-rights-and-mybizz-retention-boundary.md) |
| IN-15 | The record of events is complete and safe | Every security event writes who, what, when (UTC), before and after; no secret or card data is logged; the audit log cannot be changed by any role | ASVS 16.2–16.4; [[[default:security-global/infrastructure/sec-audit-log-integrity]]](C:/dev/project-library-global/security-global/infrastructure/sec-audit-log-integrity.md) |
| IN-16 | The app fails safely | Rate limits hold (10 a minute signed out, 100 signed in) and survive a restart; a missing table gives a plain message and an alert; no error shows internal detail | [[[default:specifications-global/spec-security]]](C:/dev/project-library-global/specifications-global/spec-security.md); [[[default:specifications-global/spec-anvil-platform-standards]]](C:/dev/project-library-global/specifications-global/spec-anvil-platform-standards.md) section 26 |
| IN-17 | The app holds up as a client grows | Lists, searches, reports and exports stay within budget with ten times a typical client's data | ISO/IEC 25010 |
| IN-18 | Hosted test data is gone | No `TEST_` row or test user remains on hosted App 1, and configuration rows match their saved copies | [[[default:specifications-global/spec-testing-methodology-standards]]](C:/dev/project-library-global/specifications-global/spec-testing-methodology-standards.md) section 4 |

## SC — Security

Each test attempts the attack. Local runtime unless stated.

| ID | Test | Passes when | Basis |
|---|---|---|---|
| SC-01 | Passwords and sign-in resist guessing | 8 characters minimum, 64 allowed, breached passwords refused, no composition rules; ten failures lock the account; sign-in, sign-up and reset never reveal whether an account exists | ASVS 6.2, 6.3.1, 6.3.8 |
| SC-02 | A second factor is required; the Owner's is phishing-resistant | Nobody signs in with a password alone; the Owner's high-value functions are refused while any non-FIDO2 factor is enrolled (FIDO2 success tested in the browser on hosted App 1) | ASVS 6.3.3 (L3 for Owner) |
| SC-03 | High-value actions need a fresh second factor | Vault, refunds above the limit, role changes, exports, gateway and price changes are refused without a second factor in the last five minutes | ASVS 7.5.3 (L3) |
| SC-04 | Sessions end when they should | Idle sessions end after 30 minutes; sign-out ends the session; a disabled user is shut out at once; the Owner can end a user's sessions; credential changes need the current password and send a notice | ASVS 7.3, 7.4, 6.3.7 |
| SC-05 | Client checks are never the only checks | Every check a form makes is also enforced when the server function is called directly | ASVS 2.2.2, 8.3.1 |
| SC-06 | Hostile input is harmless | The hostile corpus is stored and shown as plain text everywhere; rich text keeps only allowed tags; exported spreadsheet cells starting `=`, `+`, `-` or `@` are neutralised | ASVS 1.2, 1.3, 1.2.10 (L3); [[[default:security-global/threat-models/sec-injection-unsafe-input]]](C:/dev/project-library-global/security-global/threat-models/sec-injection-unsafe-input.md) |
| SC-07 | Files, links and redirects are safe | Uploads are checked by content and size and stored under generated names; server fetches of user-given addresses are limited to an allow-list; redirects go only to allowed places (each when the app has the feature) | ASVS 5.2–5.4, 1.3.6, 3.7.2 |
| SC-08 | The three planes are separate | A Customer cannot call any back-office function; signed-out users reach only public functions; nothing of App 5's credentials is in App 2 or App 3 | ASVS 8.4.2 (L3, in part), 3.5.4 |
| SC-09 | The browser side is safe | Headers and TLS on hosted pages are recorded and the app's own endpoints send safe headers; embedding is off; no sensitive value is in an address or left in browser storage after sign-out | ASVS 3.3, 3.4, 12.2, 14.2.1, 14.3 |
| SC-10 | Card data never touches the app | Payment is taken only on the gateway's page or fields; every script on payment pages is approved; no card number is found in code, tables, logs or payloads | PCI DSS SAQ A (2025); [[[default:security-global/cloud/sec-payment-gateway-trust-boundary]]](C:/dev/project-library-global/security-global/cloud/sec-payment-gateway-trust-boundary.md) |
| SC-11 | Refunds and discounts cannot be abused | No double refund, no refund above the payment, no reuse of a single-use code, no forbidden stacking; only permitted roles refund | [[[default:security-global/threat-models/sec-business-logic-race-conditions]]](C:/dev/project-library-global/security-global/threat-models/sec-business-logic-race-conditions.md) |
| SC-12 | Sensitive actions leave a full audit trail | Price changes, refunds, role changes, exports, payment actions, gateway changes and Vault access each have an audit row with actor, role, object, before and after; failed sign-ins and refused calls are logged too | ASVS 16.3.2 (L3); [[[default:security-global/threat-models/sec-data-exfiltration-bulk-export]]](C:/dev/project-library-global/security-global/threat-models/sec-data-exfiltration-bulk-export.md) |
| SC-13 | Security checks fail closed | When the role lookup, Vault, rate limit or second-factor check fails, access is refused and logged | [[[default:security-global/principles/sec-fail-closed]]](C:/dev/project-library-global/security-global/principles/sec-fail-closed.md) |
| SC-14 | Clients are isolated from each other | Two instances on the local runtime cannot reach each other's data; every client's management token, encryption key and storage key are unique; a storage key opens only its own bucket | [[[default:security-global/threat-models/sec-multi-tenant-assumption-leakage]]](C:/dev/project-library-global/security-global/threat-models/sec-multi-tenant-assumption-leakage.md); [[[default:security-global/cloud/sec-client-provisioning-security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md) |
| SC-15 | Security changes are reviewed independently | Each security-relevant change was reviewed by `code-review`, `/cso --diff` and Sentinel, each in its own session | [[[default:security-global/testing/sec-testing-independent-review]]](C:/dev/project-library-global/security-global/testing/sec-testing-independent-review.md); NIST SSDF PW.7 |
| SC-16 | An independent penetration test is passed | An outside tester, working to ASVS Level 2, finds no open critical or high issue, before the first public launch, every year and before an enterprise sale | Mybizz assurance set |
| SC-17 | The threat model is current | Every trust boundary a release adds or changes is analysed, with its tests | [[[default:security-global/requirements/sec-requirements-architecture-review]]](C:/dev/project-library-global/security-global/requirements/sec-requirements-architecture-review.md) |
| SC-18 | The running app passes a dynamic scan | Every threat model's own attack is run with real output (Level 2); one OWASP ZAP passive scan of hosted App 1 per release leaves no high or medium alert open | [[[default:security-global/testing/sec-testing-adversarial-verification]]](C:/dev/project-library-global/security-global/testing/sec-testing-adversarial-verification.md); DAST |

## BR — Browser

Hosted App 1, with GStack `browse` and `/qa-only`.

| ID | Test | Passes when | Basis |
|---|---|---|---|
| BR-01 | Every flow works end to end | Each critical flow's steps and data checks match, at desktop (1440 px) and mobile (390 px) width | DC-04 |
| BR-02 | Edge cases and errors behave as designed | Declined card, gateway failure, expired session, lost connection: each shows its message and leaves no half record | The application's test plan (Step 15), error paths |
| BR-03 | Each role sees only its own forms | Refused forms are hidden from navigation and, opened directly, refused | [[[default:specifications-global/spec-testing-methodology-standards]]](C:/dev/project-library-global/specifications-global/spec-testing-methodology-standards.md) section 7 |
| BR-04 | The feature looks as approved | Each form matches its approved screen at both widths, in light and dark mode | [[[default:specifications-global/spec-screen-and-wireframe-production-standards]]](C:/dev/project-library-global/specifications-global/spec-screen-and-wireframe-production-standards.md) |
| BR-05 | The feature is accessible | Every flow can be done by keyboard, focus is visible, icon buttons have names, errors say what to fix | WCAG 2.2 AA |
| BR-06 | The feature is fast enough | Each flow step within its budget (3 seconds by default); public pages reach Largest Contentful Paint 2.5 s and layout shift 0.1 | ISO/IEC 25010; Core Web Vitals |
| BR-07 | Earlier features still work | Every signed-off feature's flows pass again; the console shows no error; only approved hosts are contacted | Regression of every signed-off feature |
| BR-08 | Payments work end to end in test mode | Successful, declined and authentication-required test payments each end in their designed state, with webhooks and invoices | [[[default:specifications-global/spec-integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md) sections 3, 4 |
| BR-09 | The developer accepts the feature | The developer signs it off against its ticket and screens | [[[default:test-suite/ts-method]]](C:/dev/project-library-global/test-suite/ts-method.md) |

## RL — Release and operations

| ID | Test | Passes when | Basis |
|---|---|---|---|
| RL-01 | The release is ready | Every feature passed `build-verified`; the whole suite passes; no High or Critical finding is open; every ASVS Level 2 requirement and adopted Level 3 control has passing tests; the developer approves | [[[default:security-global/requirements/sec-requirements-release-readiness]]](C:/dev/project-library-global/security-global/requirements/sec-requirements-release-readiness.md) |
| RL-02 | Every client can be restored | Every client instance is backed up to its own bucket before the release; a backup restores completely in a drill (before the first release, then quarterly) | [[[default:security-global/infrastructure/sec-backup-recovery-integrity]]](C:/dev/project-library-global/security-global/infrastructure/sec-backup-recovery-integrity.md) |
| RL-03 | Schema changes are safe | The migration plan is applied to the test client first and its smoke test passes; App 3's schema equals App 1's | [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) sections 5, 7 |
| RL-04 | App 2 is exactly the release | App 2's code equals App 1's release tag | [[[default:adr-global/adr-dependency-update-model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md) |
| RL-05 | Every client instance runs the release correctly | Each reports the release version and the right schema; each passes a smoke test (sign in, read, write, clean up); each answers its own management token only | [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) section 8 |
| RL-06 | The release regression passes | Every feature's flows pass on App 2; public pages and checkout work in Chrome, Firefox and Safari | [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) |
| RL-07 | Rollback works | Re-pointing to the previous release and back succeeds, with smoke tests after each (before the first release) | [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) section 4 |
| RL-08 | A client could leave today | The exit export lands in the test client's bucket complete and usable (first release and each schema change) | [[[default:adr-global/adr-client-r2-storage-and-exit-handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md) |
| RL-09 | The release stays healthy | Against the baseline: errors below 5%, response times within 20%, every heartbeat arrives; above 10% errors or broken payments or sign-in, rollback at once | [[[default:specifications-global/spec-deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) section 9 |
| RL-10 | A new client starts secure | At activation: the clone holds no code, a new key and token, storage scoped to its own bucket, one Owner with FIDO2, no leftover accounts, webhooks registered, health endpoint answering | [[[default:specifications-global/spec-client-activation-runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) |
| RL-11 | Periodic checks are done | Monthly: dependency audit, Vault access review, retention check. Quarterly: restore drill, secret ages, review of who has access. Yearly: penetration test, each client's GDPR scope, policy review | SOC 2 readiness; [[[default:security-global/secrets/sec-secret-access-audit]]](C:/dev/project-library-global/security-global/secrets/sec-secret-access-audit.md) |
| RL-12 | Clients stay within their plan | App 5 flags any client above 80% of its rows, storage or monthly emails | [[[default:policy-global/pol-common-aspects-for-mybizz-anvil-applications]]](C:/dev/project-library-global/policy-global/pol-common-aspects-for-mybizz-anvil-applications.md) aspect 9 |

## DM — Business domains

Run at Level 1 and 2 when the feature touches the domain.

| ID | Test | Passes when | Domain |
|---|---|---|---|
| DM-01 | No double booking | Two customers booking the same provider and slot at once: one succeeds | Bookings and services |
| DM-02 | Availability and time are right | Slots respect provider rules, exceptions, the client's time zone and daylight-saving changes; reminders are sent once, at the right time | Bookings and services |
| DM-03 | Cancellations and fees follow the rules | Each cancellation window charges or refunds exactly as set | Bookings and services |
| DM-04 | Stock is never oversold | Two checkouts of the last item at once: one succeeds; reserved stock returns when a cart is abandoned or a payment fails | Catalogue, cart and orders |
| DM-05 | The server reprices at checkout | Prices, promotions, tax and shipping are recalculated on the server when the order is confirmed; a changed price or expired promotion is applied, not the cart's old figure | Catalogue, cart and orders |
| DM-06 | Promotions follow their rules | Eligibility, stacking, single-use and usage limits hold, including under simultaneous use | Catalogue, cart and orders |
| DM-07 | Tax and currency are right per region | Tax per region and line rounding follow the rules; display currency never changes the stored amount | Catalogue, cart and orders |
| DM-08 | Orders, fulfilment and returns follow their lifecycles | Partial shipments, shipping webhooks, returns, restocking and store credit follow the state machines; refunds never exceed payments | Catalogue, cart and orders |
| DM-09 | B2B accounts are controlled | Company buyers see only their company's orders, prices and catalogue; spending limits and approvals hold; payment terms and purchase-order checkout work | Catalogue, cart and orders |
| DM-10 | Marketplace sync is safe | A repeated or retried sync never duplicates orders or stock changes; failures are logged and retried | Catalogue, cart and orders (when used) |
