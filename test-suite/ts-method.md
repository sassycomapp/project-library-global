---
title: "ts-method"
updated: "2026-10-24"
doc-id: "mb-2fad9223"
---
# Test Suite — Method

## What the test suite is

The test suite is how Mybizz proves that every application it builds on Anvil is secure, works fully, keeps its data intact and obeys Mybizz's own rules. It is sized for one developer building on Anvil's Hobby plan, and it produces the evidence a business customer's security questionnaire asks for: SOC 2 Type II readiness, an annual independent penetration test, PCI DSS SAQ A and POPIA and GDPR documentation.

The suite is held once, in `project-library-global\test-suite\`, and serves every Mybizz application (`mb-3-cs`, `mb-4-ecom` and every later one). Every PDLF step names the tests it runs in its own test specification, `{step}-test-spec.md`, the seventh file of the step.

| File | What it holds |
|---|---|
| `ts-method.md` (this file) | How testing is done |
| [[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md) | Every test, with its ID |
| [[[default:test-suite/ts-conformance-checks]]](C:/dev/project-library-global/test-suite/ts-conformance-checks.md) | Every binding Mybizz rule, with the tests that prove it |
| [[[default:test-suite/ts-rule-soundness-register]]](C:/dev/project-library-global/test-suite/ts-rule-soundness-register.md) | Rules found contradictory or out of date, and the fix the tests apply |
| `tools\ts_scan.py` | The scanner: automatic checks of Mybizz's rules over an Anvil app folder |
| `tools\ts_report.py` | Produces a receipt's test counts from saved evidence, and checks a receipt against it |
| `tools\ts_local.sh` | Writes an app's `.env`, starts and stops its local runtime, and runs test commands with `.env` loaded |
| `templates\` | `conftest.py`, `pytest.ini`, `ts-config.yaml` and `test_pr09_environment.py`, copied into each app that holds code at Step 11; `access-matrix.yaml`, copied into the project library at Step 15 as `docs-local\design\app{n}\access-matrix.yaml` |

## 1. The security target

Every application is **designed and reviewed against OWASP ASVS 5.0 Level 2 principles**, with Level 3 controls on payment, administration and high-value transaction paths. Mybizz states it in exactly those words. Mybizz never claims to be "ASVS certified", because ASVS has no certification.

| Level 3 control | What it means here | Tests |
|---|---|---|
| Phishing-resistant sign-in for owners | Every user signs in with a second factor; the Owner of a client instance uses only a hardware key or the device's own passkey (FIDO2) | SC-02 |
| Detailed audit trail | Price changes, refunds, role changes, exports, payment actions, gateway changes and Vault access each record who, what, when, before and after | SC-12 |
| Separate planes | Customers, the client's staff and Mybizz's own administration (App 5) cannot reach each other's functions | SC-08 |
| Independent testing | A threat model at Step 15; an independent penetration test before the first public launch, every year, and before an enterprise sale | DC-06, SC-16, SC-17 |
| Secure development controls | Code review gate, static analysis (SAST), dynamic testing of the running app (DAST), dependency scanning, developer approval of every release | SC-15, ST-13, SC-18, RL-01 |
| Fresh second factor for high-value actions | Vault, refunds above the set limit, role changes, exports, gateway and price changes | SC-03 |

Shoppers buy as guests, without an account. Anvil can require a second factor only for every account in an app, so every account holder (staff, Owner, Mybizz) has one, and shoppers never need one.

## 2. Rules

1. **Every step is tested.** A step ends only when the tests in its test specification pass.
2. **Proof, not claims.** A test counts only when its raw output is saved. Receipt counts are produced from that output by `ts_report.py`, never written by hand.
3. **Test the real code.** A test loads the module it tests; it never holds a copy of it.
4. **Business rules live in pure modules,** with no Anvil imports, no data access and no side effects, so they can be tested on their own. Server modules are thin wrappers around them: the server module handles access and storage, the pure module the business rule.
5. **Attacks are attempted, not reasoned about.** Each security control is proven by trying the attack it stops.
6. **Never weaken a test to make it pass.** The code is fixed. A test is changed only with the developer's recorded approval.
7. **Nothing test-only in the application.** Tests reach the app from outside, through Uplink connections and a browser.
8. **A failure stops the work.** At Step 35 it is fixed at once. From Step 35A on it is a finding: recorded, triaged at Step 39, fixed at Step 35.
9. **Tests are permanent.** The whole suite runs before every release. Every fault found later gets a test before it is fixed.
10. **Levels run in order.** For a feature, Level 2 starts only after Level 1 passes, and Level 3 only after Level 2 passes, so each level tests what the one before has proven.

## 3. Levels and places

| Level | What it proves | Where it runs |
|---|---|---|
| D — Documents | Plans and designs are complete, consistent and testable | The project library |
| 0 — Static | The code and schema obey the rules before they run | The local code folder |
| 1 — Logic | Business rules are right | Local Python (pytest) |
| 2 — Integration | Server code, data, access, services and endpoints work together, securely | The local Anvil runtime; hosted App 1 for hosted services |
| 3 — Browser | Features work for real users | Hosted App 1 |
| 4 — Release | The release works for every client and can be undone | App 2, App 3, the test client and every client instance |

**The local runtime.** The Hobby plan gives App 1 one database and no test environment. Integration tests therefore run first on the Anvil App Server in WSL, started on an empty database each run. Nothing live is touched, and attacks can be tried freely.

`tools\ts_local.sh` is the one way the local runtime is handled:

- `bash ts_local.sh APP_FOLDER init` writes the app's `.env` with new random local keys and a test password. The developer runs it, because no agent reads or writes `.env`. It never overwrites an existing `.env`.
- `bash ts_local.sh APP_FOLDER start` starts the mail catcher on port 8025 and the App Server for the app on `http://localhost:3030`, on a new empty database, with the keys from `.env`.
- `bash ts_local.sh APP_FOLDER run COMMAND` runs a test command in the app folder with `.env` loaded, so a test reads its keys without anyone seeing them.
- `bash ts_local.sh APP_FOLDER stop` stops both.

The app's Users service must be switched on before the runtime can sign in a `TEST_` user. The local keys open only the local runtime; the keys for hosted App 1 are separate.

**Hosted App 1.** Only what needs Anvil's hosted service is tested there: sign-up and reset emails, real webhooks from gateways in test mode, scheduled tasks, headers and certificates. Every test value starts with `TEST_` and is removed afterwards. Attacks and load tests are never aimed at Anvil's hosted service.

**Two connections.** A server connection sets up and inspects data. A client connection, signed in as a test user of a role, acts exactly like a browser and is the only way access rules are proven. Each connection reads its key from `.env`, disconnects when its operation ends, and is reopened after the runtime is restarted whenever the app was changed in the Anvil editor.

**Hobby limits.** At most five hosted emails per run (the plan allows 1,000 a month). Volume tests run locally. Hosted concurrency tests use at most 20 parallel calls.

## 4. How tests are written

- One test file per module; one behaviour per test; names say what is tested.
- Each function is tested with valid input, its boundaries, empty and odd input, hostile input (the corpus in `conftest.py`) and, at Level 2, every role that must be refused.
- Time is passed in as an input, so tests can set it. Money is whole cents.
- Access tests are generated from the application's `access-matrix.yaml`.
- Every outside service (gateways, email, storage, AI, App 5) sits behind one small module, so tests can replace it locally.
- Tests live in each app repository in `tests\logic\`, `tests\integration\` and `tests\security\`. Secrets come only from `.env`, which is never committed.

## 5. Evidence and findings

- Evidence goes to `{slug}-project-library\pdlf-outputs\{step}\`: JUnit XML from pytest and the scanner, tool reports, review files and browser reports.
- A failure from Step 35A on is recorded in the ledger's `triage_findings` with the test ID and its evidence.
- Severity follows [[[default:specifications-global/spec-anvil-platform-standards]]](C:/dev/project-library-global/specifications-global/spec-anvil-platform-standards.md) section 21: anything touching security, money or client data is Critical or High.
- Every fixed finding gets a permanent test that fails without the fix.
- Steps 36, 37 and 38 each write a findings file, `{slug}-{step}-{run}-findings.md`, that states every finding or, when there is none, a clean pass. A step whose findings file is missing has failed.

## 6. Gates

| Gate | The tests must show |
|---|---|
| `domain-locked` (16), `concept-locked` (21), `wireframes-approved` (26) | Every test of the steps before the gate passed |
| `architecture-verified` (34) | The skeleton passes every scan and implements the threat model's controls |
| `build-verified` (39) | Levels 0 to 3 pass for the feature, the whole suite still passes, every finding is decided, the developer signed off |
| `production-released` (44) | Level 4 passes on App 2, App 3 and every client instance |
| `released` (46) | Every fault that escaped has its test |

## 7. Evidence for business customers

The suite's saved evidence answers the questions a business customer asks. Nothing extra is built for it.

| Assurance | What answers it |
|---|---|
| SOC 2 Type II readiness (security, availability, confidentiality) | Change control: every release approved at its gate, with code review and test evidence (RL-01, SC-15). Access control: role tests and second factors (IN-02, SC-02). Monitoring: heartbeats and watch after release (RL-09). Backup and recovery: restore drills (RL-02). Vendor review: package and service inventory (ST-13, DC-07). Periodic reviews: the operations cadence (RL-11). Kept over time in the ledger and the evidence folders, which is what a Type II audit samples. |
| Annual penetration test | SC-16 |
| PCI DSS SAQ A | Card details are taken only by the gateway; payment-page scripts are approved; amounts are set by the server; webhooks are verified (SC-10, IN-06, IN-07) |
| POPIA and GDPR | Data inventory and lawful basis (DC-03), data-subject rights and retention (IN-14), exit handover (RL-08), legal documents (DC-14) |

## 8. Each step's test specification

Every step has `{step}-test-spec.md` in its app-factory phase folder, in this form:

- **Proves:** one sentence.
- **Tests:** a table of catalogue test IDs, each with one line on how it applies at this step.
- **Particular to this step:** a test no other step needs, only when there is one.
- **On failure:** what happens.

Evidence is saved in the step's output folder, named `{slug}-{step}-{run}-{kind}`.

## 9. Tools

| Tool | Used for |
|---|---|
| pytest | Levels 1 and 2 |
| Anvil App Server, with Java | The local runtime |
| Anvil Uplink | Server and client connections |
| pyotp | Second-factor codes for `TEST_` users |
| aiosmtpd | The local mail catcher |
| `ts_local.sh` | Starts and stops the local runtime |
| PyYAML | The scanner |
| pip-audit | Known vulnerabilities in packages |
| gitleaks | Secrets in code and git history |
| bandit | Static security analysis of Python (SAST) |
| OWASP ZAP | One dynamic scan per release (DAST), passive on hosted App 1 |
| GStack `browse`, `/qa-only`, `/cso`, `benchmark`, `canary` | Browser tests, security review, performance, release watch |

About 0.8 GB in WSL. The Python tools live in one virtual environment, `~/mybizz-test-tools/venv`, and ZAP in `~/mybizz-test-tools/ZAP_2.17.0`; Java and gitleaks are Ubuntu packages. Each tool is installed with the developer's approval at the version below, and never upgraded without the developer's decision.

| Tool | Approved version |
|---|---|
| Java (OpenJDK runtime, `openjdk-21-jre-headless`) | 21.0.12.1; the Anvil App Server needs Java 21 or later |
| Anvil App Server (`anvil-app-server`) | 1.18.0 |
| Anvil Uplink (`anvil-uplink`) | 0.7.0 |
| pytest | 9.1.1 |
| pyotp | 2.10.0 |
| aiosmtpd | 1.4.6 |
| PyYAML | 6.0.3 |
| pip-audit | 2.10.1 |
| bandit | 1.9.4 |
| gitleaks (Ubuntu package) | 8.16.0 |
| OWASP ZAP | 2.17.0 |
| GStack | The version installed for PDLF |

## Why it works this way

- **Level 2 with selected Level 3,** because the costliest failures are a stolen owner account, a forged payment and an unrecorded change to money, and those get the extra controls; everything else gets the standard level.
- **The local runtime first,** because the Hobby plan has no test database, and attacks must never hit a hosted service.
- **A client connection for access tests,** because a server connection passes every access check and proves nothing.
- **Saved evidence,** because an agent can report a pass that never happened, and because that evidence, kept over time, is what a SOC 2 Type II audit and a customer's questionnaire ask for.
- **One catalogue,** because a test used at many steps must be the same test everywhere.
