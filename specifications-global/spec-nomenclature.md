---
document: Mybizz CS — Nomenclature & Naming Conventions
doc-id: spec-nomenclature
state: Live
date-created: 2026-07-25T150027+0200
---
# Mybizz CS — Nomenclature & Naming Conventions

**Authority:** Mandatory — all code, files, forms, and databases must follow

---

## File & Folder Naming

| Element | Convention | Example |
|---|---|---|
| Folders | PascalCase | `ServerAuth`, `ContactListForm` |
| Files | lowercase_with_underscores.ext | `backup_strategy_analysis.md` |
| ADR files | `{adr}-{kebab-case-name}.md` | `[[adr-brevo-replaces-zoho-email]]` |
| ADR files (superseded) | `{adr}-{kebab-case-name}.md` with `[Superseded]` on line 2 | `13-system-currency-setting.md` |
| ADR files (cancelled) | `{adr}-cancelled-{kebab-case-name}.md` | `adr-onboarding-finality.md` |
| Custom component wireframes | `wireframe-custom-component-{ComponentName}.html` | `wireframe-custom-component-ClauseBuilder.html` |

### UI Form Folder Nomenclature (formalized 2026-09-10)

Every form folder under `{slug}-project-library\ui\{package}\{FormName}\` carries exactly six
files — three authored documents and three derived renderings — named by the locked UI
convention below. This convention is the single standard for the UI tree, applied
consistently; folder-prefixed variants (`checklist-{package}-{FormName}.md`,
`wireframe-{package}-{FormName}.html`) are retired.

**Authored documents (markdown, carry front matter):**

| Element | Pattern | Example |
|---|---|---|
| Wireframe definition | `{FormName}-wireframe-definition.md` | `LoginForm-wireframe-definition.md` |
| Wireframe checklist | `{FormName}-wireframe-chklist.md` | `LoginForm-wireframe-chklist.md` |
| Screen checklist | `{FormName}-screen-chklist.md` | `LoginForm-screen-chklist.md` |

**Derived renderings (no front matter — register row is their identity):**

| Element | Pattern | Example |
|---|---|---|
| Wireframe rendering | `{FormName}-wireframe.html` | `LoginForm-wireframe.html` |
| Screen rendering | `{FormName}-screen.html` | `LoginForm-screen.html` |
| Screen capture | `{FormName}-screen.png` | `LoginForm-screen.png` |

**Sub-forms / row templates** nest one folder deeper and repeat the same patterns with the
full qualified stem: `{FormName}{SubForm}-{kind}` (e.g.
`RevenueReportForm-RowTemplate-screen-chklist.md`). The stem is always the form name first;
kind prefixes (`checklist-`, `wireframe-` before the form name) are retired by this
specification. Register rows carry the same identity; html/png identity lives in the register
(a format cannot carry front matter).

---

## User Terminology

| Term | Definition |
|---|---|
| Client | Mybizz subscriber (business owner) |
| Customer | Client's end user (their customer) |
| Visitor | Public website visitor (not logged in) |
| Staff | Client's staff member — `Staff` role in RBAC |
| Owner | Client's business owner — `Owner` role in RBAC |
| Manager | Client's operational manager — `Manager` role in RBAC |
| Admin | Client's administrative staff — `Admin` role in RBAC |

Client and Owner are principally defined as;
"Client" refers to the entity, business or individual, which signs up to the Mybizz management application as a new client/ subscriber who is then onboarded and then becomes the "owner" Of that client instance 
"Owner" refers to the entity which signed up with the maybizz management application for a new client instance and is therefore the person responsible for that client instance


---

## Form Naming

**Pattern:** `{Entity}{Type}Form`

| Type | Purpose | Example |
|---|---|---|
| `ListForm` | Data listing/browsing | `ContactListForm` |
| `EditorForm` | Create or edit | `ContactEditorForm` |
| `ViewerForm` | Read-only detail | `ContactViewerForm` |
| `DashboardForm` | Summary with metrics | `DashboardForm` |
| `Page` | Public-facing read-only page | `PrivacyPolicyPage`, `TermsConditionsPage` |

---

## Component Prefixes

| Component | Prefix | Example |
|---|---|---|
| Button | `btn_` | `btn_save` |
| TextBox / TextArea | `txt_` | `txt_name` |
| Heading | `hdg_` | `hdg_title` |
| DropdownMenu | `dd_` | `dd_status` |
| DatePicker | `dp_` | `dp_date` |
| FileLoader | `fu_` | `fu_upload` |
| Link / Navigation | `nav_` | `nav_dashboard` |
| Checkbox | `cb_` | `cb_agree` |
| RadioButton | `rb_` | `rb_option` |
| ColumnPanel | `col_` | `col_main` |
| FlowPanel | `flow_` | `flow_header` |
| Card | `card_` | `card_details` |
| DataGrid | `dg_` | `dg_customers` |
| DataRowPanel | `drp_` | `drp_comment_row` |
| Icon | `ico_` | `ic_empty_vault` (maps to `IconButton` used decoratively — no click event) |
| RepeatingPanel | `rp_` | `rp_items` |
| Plot | `plot_` | `plot_revenue` |

---

## Module Naming

| Module Type | Pattern | Example |
|---|---|---|
| Server service | `{purpose}_service.py` | `booking_service.py` |
| Server integration | `{purpose}_integration.py` | `brevo_integration.py` |
| Client utility | `{purpose}_utils.py` | `validation_utils.py` |
| Client helper | `{purpose}_helpers.py` | `navigation_helpers.py` |

---

## Database Tables

- **Table names:** lowercase_snake, no prefix
- **Link columns:** `{table}_id` or singular name matching target table
- **System columns:** `created_at`, `updated_at` (mandatory on most tables)

---

## Transaction Types

| Type | Usage |
|---|---|
| `appointment` | Timed service booking |
| `consulting` | Fixed-price service |

---

## Currency Terms

| Term | Definition |
|---|---|
| System Currency | Primary currency (set at onboarding, immutable after first transaction) |
| Display Currency | Optional secondary currency for customer-facing prices |

---

## Critical Concepts

| Concept | Definition |
|---|---|
| Master Template | Published Anvil dependency containing all features |
| Client Instance | Individual Anvil app for one business, depends on master_template |
| Pull-Based Updates | Clients choose when to adopt new master_template version |
| Data Isolation | Complete — each client is separate Anvil app with separate database |
| The Vault | Encrypted secrets store for all client API keys |
| RBAC | Role-Based Access Control with 5 roles |

---

## Version & Release System

| Term | Format | Example |
|---|---|---|
| Phase | `Phase {number}: {Name}` | Phase 1: Authentication |
| Stage | `Stage {phase}.{number}: {Name}` | Stage 1.1: User Auth System |
| Task | `T{stage}-{number}: {Action}` | T1.1-001: Create users table |

---

## Common Abbreviations

| Abbrev | Full Term |
|---|---|
| MVP | Minimum Viable Product |
| CRM | Customer Relationship Management |
| RBAC | Role-Based Access Control |
| TOTP | Time-Based One-Time Password |
| GDPR | General Data Protection Regulation |
| POPIA | Protection of Personal Information Act |
| PCI DSS | Payment Card Industry Data Security Standard |
| SMTP | Simple Mail Transfer Protocol |
| SEO | Search Engine Optimization |

---

## Component Permission Model — Naming + Permission

The prefix convention (§1) carries an additional permission dimension. Every component falls into
one of two tiers, and the naming convention reflects which camp it belongs to:

| Tier | Rule |
|---|---|
| **Approved** | Component listed in [[spec-m3_component_mapping|M3 Component Mapping]] with its assigned prefix |
| **Restricted** | Legacy `Label` component — banned. Any component not in the approved list — treated as restricted by default |

Additions to the approved list require an ADR and an update to [[spec-m3_component_mapping|M3 Component Mapping]].
The `drp_` prefix (DataRowPanel) is the documented example of a component prefix that was
identified as a gap and later codified — the process for closing a prefix gap is: flag it,
ADR it, add it.

---

*End of file*
