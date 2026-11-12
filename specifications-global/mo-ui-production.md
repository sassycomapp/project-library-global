---
title: "mo-ui-production"
doc-id: "mb-a19c4d89"
updated: "2026-11-12"
---
# Mybizz — Method of Operation: UI Production

## 1. What This Method Is

- This method is how the forms of a Mybizz Anvil application are designed, built, wired and checked, one feature at a time.
- Every form it produces meets [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md).
- The approved screen requirement is the design of a form. `mb-form-builder` writes each form from it as a real Anvil HTML form, and David checks the form in the Anvil editor.
- In PDLF, the whole application's tables are built at Step 17, and every screen requirement is written and approved at Steps 22 to 26. This method's per-feature work runs in the build loop of Phase E.
- Why: the form written from an approved requirement is the only design copy, so nothing is copied into Anvil by hand and nothing drifts.

## 2. Roles

| Who | Does | Never does |
|---|---|---|
| David | Approves screen requirements and forms; makes Data Tables changes in the Data Tables view; commits; relays prompts | — |
| Claude | Writes and checks screen requirements; reviews server code, forms, spec sheets and the Anvil agent's changes against [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md), `project-library-global` and the project library; writes prompts | Writes to GitHub |
| OpenCode | Builds the scaffold, the data table schema, the server code and all application code; runs `mb-form-builder` | Wires forms |
| Anvil agent | Fills the empty event handlers so they call the server functions the spec sheets name; checks its wiring against Anvil's standards with `/review-commit` | Builds, changes or judges the UI; renames, adds or removes forms, components or server functions |

Why the Anvil agent does not judge the UI: Anvil's own agent references cover only Anvil's base M3 theme, not `m3-custom-theme`.

## 3. Once per Application

1. The application's only theme dependency is `m3-custom-theme`, with the package name `m3`.
2. David's Claude account is connected to the Anvil agent in the Anvil editor.
3. The Anvil CLI is installed on David's computer.
4. The application's `ts-config.yaml` lists the allowed Anvil standard components in `approved_components`, and its `tests/` folder holds a current copy of the theme's `docs/component-inventory.yaml`.
5. Features are built in this order: `layouts` and `shared` first, `auth` second, then every other feature. Why: every page form sits on a layout, and the application starts on its sign-in form.

## 4. Per Feature

Each feature is built, checked and signed off by David before the next feature starts. Before the first feature, the application's tables exist and every screen requirement of the run is approved.

1. **Claude:** Check that the feature's ticket, its approved screen requirements, the authoritative schema and the SRS still agree, and correct them where they disagree. A change to an approved screen requirement needs David's approval.
2. **OpenCode, build mode:** Write the feature's server module and server functions, named exactly as the screen requirements name them, and add each server function to `access-matrix.yaml`.
3. **Claude:** Review the server code against the screen requirements and the SRS.
4. **David, WSL terminal:** Commit the documentation repositories with `commit-all`, then the app with `git pull` followed by `gcp`.
5. **OpenCode, build mode:** Run `mb-form-builder` for the feature (section 5).
6. **Claude:** Review every form and spec sheet against its screen requirement and [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md).
7. **David, WSL terminal:** Commit the documentation repositories with `commit-all`, then the app with `git pull` followed by `gcp`. The forms reach GitHub, and the Anvil editor shows them.
8. **David, Anvil editor:** Open each form. Success means every component shows, nothing is reported missing, and the form looks as its screen requirement describes.
9. **David, Anvil agent chat:** Give the Anvil agent the wiring task: "Wire the forms listed below to their server functions, as their spec sheets in `theme/assets/docs/app{n}/` state. Fill the empty event handlers only." Then list the forms by module path.
10. **David, Anvil agent chat:** Run `/review-commit` on the Anvil agent's commit.
11. **David, WSL terminal:** Pull the Anvil agent's commit, then run `anvil --json validate client_code` and `ts_scan.py`.
12. **Claude:** Review the Anvil agent's commit. Success means only event handler bodies changed, each as its spec sheet states. Any deviation goes back to the Anvil agent as a correction prompt, and steps 10 to 12 repeat.
13. **David, Anvil:** Run the application and carry out every action in every spec sheet of the feature. Success means each action gives the result its spec sheet states.
14. **Claude:** Close the feature in the PDLF record.

A feature added to an application that already exists first passes through PDLF Steps 17 to 26 for its own tables and screen requirements, then follows these steps.

## 5. mb-form-builder

`mb-form-builder` is the OpenCode skill that writes a feature's forms.

### 5.1 Inputs

- the feature's approved screen requirements;
- the scaffold specification, the user flows, the authoritative schema and the SRS, from the project library;
- the theme's component documentation and `docs/component-inventory.yaml`;
- `approved_components` in `ts-config.yaml`;
- the feature's server module in `server_code/`;
- [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md), [[[default:specifications-global/spec-nomenclature]]](C:/dev/project-library-global/specifications-global/spec-nomenclature.md) and [[[default:specifications-global/spec-translation]]](C:/dev/project-library-global/specifications-global/spec-translation.md).

### 5.2 Gate

The skill stops and reports, writing nothing, when any of these is missing:

- an approved screen requirement for a form of the feature;
- the feature's server module;
- a server function a screen requirement names.

### 5.3 Outputs per Form

- `client_code/<package path>/<FormName>/form_template.html`;
- `client_code/<package path>/<FormName>/__init__.py`, holding the class, the `translate_form(self)` call, and every event handler named and empty;
- `theme/assets/docs/app{n}/<package path>/<FormName>.md`, the spec sheet;
- the form's entry in `access-matrix.yaml`;
- the form's phrase keys in `en.py`.

### 5.4 Old Forms

In the same run, for each old form of the feature:

1. A new form at the same module path replaces the old form's two files in place.
2. An old form with no new form at its module path is removed: its own folder, its spec sheet and its `access-matrix.yaml` entry.
3. Every reference to a removed form is updated, including `startup` in `anvil.yaml`, routes and navigation code.
4. Package folders and their `__init__.py` files are never removed.

### 5.5 Checks

1. The skill runs `anvil --json validate client_code` and `ts_scan.py`.
2. The skill fixes every failure and reruns both checks until both pass.
3. The skill touches only the feature's files, and stops and reports when the same failure happens twice.

## 6. Check Points

| # | When | Who | What it proves |
|---|---|---|---|
| 1 | Section 4, step 5 | `mb-form-builder` | `validate` and `ts_scan.py` pass before any commit |
| 2 | Section 4, step 6 | Claude | Each form and spec sheet matches its screen requirement and [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) |
| 3 | Section 4, step 8 | David | Each form displays as designed in Anvil |
| 4 | Section 4, step 10 | Anvil agent | The wiring meets Anvil's standards |
| 5 | Section 4, step 11 | David | `validate` and `ts_scan.py` still pass after the wiring |
| 6 | Section 4, step 12 | Claude | The Anvil agent changed only event handler bodies |
| 7 | Section 4, step 13 | David | Every action gives the result its spec sheet states |

## 7. Rules

1. Only David commits. Documentation repositories are committed with `commit-all`, which also updates GBrain. App repositories are committed with `git pull` followed by `gcp`.
2. OpenCode runs in plan mode before build mode, and touches only the files its task names.
3. The Anvil agent works on the `master` branch and commits automatically. Its work is reviewed after David pulls it, before the next feature starts.
4. A feature's old forms leave the application in the same run that adds its new forms, so the application never holds two versions of a feature.
