---
title: "spec-nomenclature"
doc-id: "mb-a3648afc"
updated: "2026-10-24"
---
# Nomenclature and Naming Conventions

## How this document works

This is the nomenclature document for everything common to Mybizz's systems. Every common name and term is defined here, once.

- **Part 1** applies to everything: PDLF and every application.
- **Part 2** holds names used only by PDLF.

The terms of one application are defined in that application's own `docs-local\GLOSSARY.md`, never here. A term is defined in exactly one place. Part 2 holds only what is unique to PDLF; anything shared moves to Part 1. When a name is agreed in discussion, it is written here before anything relies on it.

Why one document for common names: separate nomenclature documents overlap, and the same term ends up meaning different things in different places. An application's own terms are kept with that application, because nothing else uses them.

---

## Part 1 — Common to everything

### 1.1 Documents

| Element | Convention | Example |
|---|---|---|
| Document file | lowercase kebab-case `.md` | `platform-architecture.md` |
| ADR file | `adr-{kebab-case-name}.md` | `adr-brevo-email-and-crm.md` |
| Front matter | `title` (the filename without `.md`), `doc-id`, `updated` | |

`doc-id` is a permanent code (`mb-xxxxxxxx`) added by the commit hook, never written by hand. Links between documents are written by agents as `[[name]]` and converted by the commit hook into the standard form; their rules belong to mybizz-os, not to this document.

### 1.2 Repositories and paths

| Element | Convention | Example |
|---|---|---|
| Project slug | the business's short name, lowercase, hyphens kept, supplied once at Step 11 | `mb-3-cs` |
| Project folder | `C:\dev\dev-{slug}\` | `C:\dev\dev-mb-3-cs\` |
| Code repositories | one per app: `{slug}-app1`, `{slug}-app2`, `{slug}-app3`, `{slug}-app5`; full path `C:\dev\dev-{slug}\{slug}-app{n}\`. App 4 lives on the client's own Anvil account and has no folder | `mb-3-cs-app1` |
| Documentation repository | `dev-{slug}\{slug}-project-library\`, one per business | `dev-mb-3-cs\mb-3-cs-project-library\` |
| GitHub organisation | `sassycomapp` | |

Every repository carries the slug as a prefix so that a business's repositories sort together on GitHub.

**Rule:** plain-language text may use the short forms above. Any command the agent runs uses the full absolute path, because a short form is not something the operating system can act on. The `dev-{slug}\` segment is never dropped from the documentation repository's path.

### 1.3 Global and local folders

Every folder in `project-library-global` has a matching local folder in each project's documentation repository. The local folder holds only what is true of that one project.

| Global | Local |
|---|---|
| `adr-global` | `adr-local` |
| `checklists-global` | `checklists-local` |
| `docs-standard-global` | `docs-standard-local` |
| `policy-global` | `policy-local` |
| `specifications-global` | `specifications-local` |
| `standard-operating-procedures-global` | `standard-operating-procedures-local` |
| `templates-global` | `templates-local` |

### 1.4 The five apps

| App | Role name | Anvil app and repository | Example (`mb-3-cs`) |
|---|---|---|---|
| App 1 — development workspace | development workspace | `{slug}-app1` | `mb-3-cs-app1` |
| App 2 — published dependency | `master_template` | `{slug}-app2` | `mb-3-cs-app2` |
| App 3 — provisioning clone source | `blank_client_template` | `{slug}-app3` | `mb-3-cs-app3` |
| App 4 — client instance | `[client-name]-{vertical}` | on the client's own Anvil account; no repository | `[client-name]-cs` |
| App 5 — management tooling | `{Product}_management` | `{slug}-app5` | `mb-3-cs-app5` |

### 1.5 Mybizz business terms

| Term | Meaning |
|---|---|
| Client | The business or individual that subscribes to a Mybizz application and is given its own client instance. |
| Owner | The person responsible for a client instance: the client who signed up, once onboarded. |
| Customer | A client's own customer, who uses the client's instance. |
| Visitor | Someone viewing a client's public website without logging in. |
| Master template | `master_template`, the published dependency holding all server logic and forms for every client instance. |
| System currency | The primary currency, set at onboarding and fixed after the first transaction. |
| Display currency | An optional second currency for prices shown to customers. |
| The Vault | The encrypted store for a client's API keys and secrets. |
| Roles | Owner, Manager, Admin, Staff and Customer, the same in every application, as [[[default:specifications-global/spec-security-architecture\|Security Architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md) defines them. |
| Client instance | One client's own Anvil app, with its own database, running on `master_template`. |
| Data isolation | Every client instance is a separate app with a separate database. No database is ever shared between clients. |
| Updates | A client instance receives every release pushed into `master_template` automatically. |

### 1.6 Anvil application code

**Forms:** `{Entity}{Type}Form`.

| Type | Purpose | Example |
|---|---|---|
| `ListForm` | Listing and browsing | `ContactListForm` |
| `EditorForm` | Create or edit | `ContactEditorForm` |
| `ViewerForm` | Read-only detail | `ContactViewerForm` |
| `DashboardForm` | Summary with metrics | `DashboardForm` |
| `Page` | Public read-only page | `PrivacyPolicyPage` |

**Packages:** lowercase, by feature (`auth/`, `bookings/`); server packages carry `server_` (`server_bookings/`).

**Modules:** lowercase with underscores.

| Module | Pattern | Example |
|---|---|---|
| Server service | `{purpose}_service.py` | `booking_service.py` |
| Server integration | `{purpose}_integration.py` | `brevo_integration.py` |
| Client utility | `{purpose}_utils.py` | `validation_utils.py` |
| Client helper | `{purpose}_helpers.py` | `navigation_helpers.py` |

**Components:**

| Component | Prefix | Example |
|---|---|---|
| Button | `btn_` | `btn_save` |
| TextBox / TextArea | `txt_` | `txt_name` |
| Heading | `hdg_` | `hdg_title` |
| DropdownMenu | `dd_` | `dd_status` |
| DatePicker | `dp_` | `dp_date` |
| FileLoader | `fu_` | `fu_upload` |
| Link / navigation | `nav_` | `nav_dashboard` |
| Checkbox | `cb_` | `cb_agree` |
| RadioButton | `rb_` | `rb_option` |
| ColumnPanel | `col_` | `col_main` |
| FlowPanel | `flow_` | `flow_header` |
| Card | `card_` | `card_details` |
| DataGrid | `dg_` | `dg_customers` |
| DataRowPanel | `drp_` | `drp_comment_row` |
| Icon (decorative IconButton, no click event) | `ico_` | `ico_empty_vault` |
| RepeatingPanel | `rp_` | `rp_items` |
| Plot | `plot_` | `plot_revenue` |

Only components listed in [[[default:specifications-global/spec-m3_component_mapping|M3 Component Mapping]]](C:/dev/project-library-global/specifications-global/spec-m3_component_mapping.md) may be used. The legacy `Label` component is banned. Any component not on that list is restricted until an ADR adds it, together with its prefix.

**Data tables:** table names lowercase with underscores, no prefix; link columns `{table}_id` or the singular name of the target table; `created_at` and `updated_at` on most tables.

### 1.7 UI form folders

Each form folder, `{slug}-project-library\ui\{package}\{FormName}\`, holds exactly six files:

| File | Pattern | Front matter |
|---|---|---|
| Wireframe definition | `{FormName}-wireframe-definition.md` | Yes |
| Wireframe checklist | `{FormName}-wireframe-chklist.md` | Yes |
| Screen checklist | `{FormName}-screen-chklist.md` | Yes |
| Wireframe rendering | `{FormName}-wireframe.html` | No |
| Screen rendering | `{FormName}-screen.html` | No |
| Screen capture | `{FormName}-screen.png` | No |

A sub-form or row template sits one folder deeper and uses the full stem: `{FormName}{SubForm}-{kind}`. A custom component's wireframe is `wireframe-custom-component-{ComponentName}.html`.

### 1.8 Planning units

| Term | Format | Example |
|---|---|---|
| Phase | `Phase {n}: {Name}` | Phase 1: Authentication |
| Stage | `Stage {phase}.{n}: {Name}` | Stage 1.1: User Auth System |
| Task | `T{stage}-{nnn}: {Action}` | T1.1-001: Create users table |

### 1.9 Acronyms

| Acronym | Meaning |
|---|---|
| ADR | Architecture Decision Record |
| AC | Acceptance Criterion |
| CRM | Customer Relationship Management |
| DX | Developer Experience |
| FS | Functional Specification |
| GDPR | General Data Protection Regulation |
| M3 / MD3 | Material Design 3 |
| MCP | Model Context Protocol |
| MVP | Minimum Viable Product |
| NFR | Non-Functional Requirement |
| PCI DSS | Payment Card Industry Data Security Standard |
| POPIA | Protection of Personal Information Act |
| PRD | Product Requirements Document |
| RBAC | Role-Based Access Control |
| SEO | Search Engine Optimisation |
| SMTP | Simple Mail Transfer Protocol |
| TDD | Test-Driven Development |
| TOTP | Time-Based One-Time Password |
| TTHW | Time to Hello World (time from install to first working output) |
| UAT | User Acceptance Testing |
| US | User Story |
| WSL | Windows Subsystem for Linux |

---

## Part 2 — PDLF

### 2.1 Terms

| Term | Meaning |
|---|---|
| PDLF | Project Development Lifecycle Framework |
| BFT | BODY Frame Thinking (Edward de Bono), PDLF's thinking checkpoint |
| ISA | Ideal State Artifact, a project's definition of "done" |
| ISC | Ideal State Criterion, one criterion in the ISA |
| GBrain | The memory layer of mybizz-os (PostgreSQL in WSL) |
| GStack | A library of workflow skills used by PDLF |
| Ledger | PDLF's PostgreSQL database `pdlf` |
| Module | One finished step, compiled into its module file in its phase folder in `app-factory/` |
| Gate | A hard stop where David approves a commitment before the build continues |
| Deviation | A recorded decision taken when a step cannot be done as written |
| Step Receipt | The report of a step, produced from its ledger row |

### 2.2 Locations

| Location | Path |
|---|---|
| PDLF | `C:\pdlf\` |
| Global library | `C:\dev\project-library-global\` |
| Project template | `C:\dev\project-template\dev-(SLUG)\` |

### 2.3 Steps and modules

| Element | Convention | Example |
|---|---|---|
| Phase folder | `app-factory\phase-{letter}-{name}\`, lowercase kebab-case | `phase-b-discover-and-define\` |
| Step file | `{NN}-{skill-or-function-name}.md`, in its phase folder | `14-plan-ceo-review.md` |
| Build notes | `{NN}-build-notes.md` | `14-build-notes.md` |
| Decision tree | `{NN}-decision-tree.html` | `14-decision-tree.html` |
| Inserted step | nearest preceding number plus a lowercase letter | `35a-testing.md` |
| Module | `{NN}-module.md`, two digits, matching the step number, in the step's phase folder | `07-module.md` |

The skill or function name appears only in the step file's own name, never in its build notes or decision tree. Step numbers identify steps; they never state the order in which steps run (`orchestrator-run-plan.md` does that). Step 1 is the orchestrator; Steps 2 to 10 are entry points for work on existing applications; Steps 13 and 25 are not used.

### 2.4 Build records and outputs

| Artifact | Path |
|---|---|
| Step Receipt | `{docs-repo}\pdlf-outputs\{step}\{slug}-{step}-{run}-receipt.md` |
| First concept draft | `{docs-repo}\docs-local\design-doc-first-concept.md` (written once, never overwritten) |
| Working design doc | `{docs-repo}\docs-local\design-doc.md` |
| Output copy | `{docs-repo}\pdlf-outputs\{step}\{slug}-{step}-{run}-{name}.md` |

`{step}` is the step's folder name in the app factory (for example `b14`). `{run}` is `app{n}` for a whole application (`app1`, `app2`, `app3` or `app5`), or the feature's short name for a feature or an update, so no run overwrites another run's files. The prefix is always the project slug, never a GStack-derived name. Nothing an application produces is kept in `C:\pdlf`.

### 2.5 GStack project names

GStack does not use the project slug. Each GStack skill derives a project name from the Git repository it runs in: first from its cache (keyed by the working folder), otherwise from the Git remote (`org-repo`), otherwise from the folder name. Because PDLF fixes the repository names, the derived names are fixed too:

| Skill runs in | GStack name | Native save folder |
|---|---|---|
| The documentation repository | `sassycomapp-{slug}-project-library` | `~/.gstack/projects/sassycomapp-{slug}-project-library/` |
| A code repository | `sassycomapp-{slug}-app{n}` | `~/.gstack/projects/sassycomapp-{slug}-app{n}/` |

PDLF starts its Phase B GStack skills from the documentation repository, so their GStack name is always `sassycomapp-{slug}-project-library`. Any document that gives a GStack save path names the repository it means.

**Cache rule.** GStack's cache is never reconciled with the Git remote, so a renamed or re-cloned repository can keep an old name. The cache is never edited casually. When the cached name differs from the name the remote gives, the remote's name is written into the cache, with David's permission.
