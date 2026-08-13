---
document: Mybizz — ADR Index
doc-id: adr-index
state: Live
date-created: 2026-07-25T150027+0200
---
# Mybizz — ADR Index

**Last Updated:** 2026-08-05
**Total ADRs:** 41 (40 global, 1 local) — 25 Accepted, 8 Confirmed, 1 Superseded, 7 Approved

---

## Global ADRs (`adr-global/`)

Company-wide architecture, technology, and standards decisions — apply to all Mybizz applications.

| ADR File | Title | Status | Date |
|---|---|---|---|
| [[brevo-replaces-zoho-email|Brevo Replaces All Zoho Products]] | Brevo Replaces All Zoho Products | Accepted | 2026-03-21 |
| [[navigation-lambda-link-open-form|Navigation Lambda/Link/open_form]] | Navigation Standard: Lambda/Link/open_form | Accepted | 2026-03-18 |
| [[payment-security-boundary-vault|Payment Security Boundary Vault]] | Payment Security Boundary: Vault | Accepted | 2026-03-15 |
| [[lead-capture-simultaneous-creation|Lead Capture Simultaneous Creation]] | Lead Capture: Simultaneous Creation | Accepted | 2026-03-21 |
| [[timezone-utc-storage-display-conversion|Client Timezone: UTC Storage, Display Conversion]] | Client Timezone: UTC Storage, Display Conversion | Accepted | 2026-03-17 |
| [[crm-package-replaces-marketing|CRM Package Replaces Marketing]] | Package Name: crm/ Replaces marketing/ | Accepted | 2026-03-18 |
| [[single-contacts-table|Single Contacts Table]] | Single Contacts Table Replaces Dual contacts/customers | Accepted | 2026-05-03 |
| [[anvil-extras-exclusion|Anvil Extras Exclusion]] | Anvil Extras Exclusion | Accepted | 2026-05-21 |
| [[material-3-theme-component-scope|Material 3 Theme Component Scope]] | Material 3 Theme Component Scope | Accepted | 2026-05-21 |
| [[system-currency-selection-and-immutability|System Currency Selection and Immutability]] | System Currency, Display Currency, and Immutability | Accepted | 2026-05-29 |
| [[onboarding-vs-settings-boundary|Onboarding vs Settings Boundary]] | Onboarding vs Settings Boundary | Accepted | 2026-05-29 |
| [[legal-policy-responsibility-acknowledgement-and-clause-builder-architecture|Legal Policy Responsibility Acknowledgement and Clause-Builder Architecture]] | Legal Policy Responsibility Acknowledgement and Clause-Builder Architecture | Accepted | 2026-05-29 |
| [[payment-gateway-configuration-is-a-settings-function-and-is-rbac-governed|Payment Gateway Configuration Is a Settings Function and Is RBAC-Governed]] | Payment Gateway Configuration Is a Settings Function and Is RBAC-Governed | Accepted | 2026-05-29 |
| [[onboarding-data-schema-alignment|Onboarding Data Schema Alignment]] | Onboarding Data Schema Alignment | Accepted | 2026-05-29 |
| [[client-data-management-rights-and-mybizz-retention-boundary|Client Data Management Rights and Mybizz Retention Boundary]] | Client Data Management Rights and Mybizz Retention Boundary | Accepted | 2026-05-29 |
| [[tiers-model|Tiers Model]] | Tiers Model | Accepted | 2026-05-29 |
| [[onboarding-resumability|Onboarding Resumability]] | Onboarding Resumability | Accepted | 2026-05-29 |
| [[payment-gateway-mutability|Payment Gateway Mutability]] | Payment Gateway Mutability | Accepted | 2026-05-29 |
| [[onboarding-finality|Onboarding Finality]] | Onboarding Finality | Accepted | 2026-06-01 |
| [[design-rules|Design Rules]] | Design Rules | Accepted | 2026-06-10 |
| [[client-instance-architecture|Client Instance Architecture]] | Client Instance Architecture | Confirmed | 2026-06-13 |
| [[dependency-update-model|Dependency Update Model]] | Dependency Update Model | Confirmed | 2026-06-13 |
| `blank-client-template.md` | blank_client_template as Provisioning Clone Source | Confirmed | 2026-06-13 |
| [[free-trial-abandoned|30-Day Free Trial Abandoned]] | 30-Day Free Trial Abandoned | Confirmed | 2026-06-13 |
| [[observability-architecture|Observability Architecture]] | Observability Architecture | Confirmed | 2026-06-13 |
| [[mybizz-management-visibility|Mybizz Management Visibility]] | Mybizz_management Visibility and Control | Confirmed | 2026-06-13 |
| [[anvil-platform-constraints|Anvil Platform Constraints and Design Boundaries]] | Anvil Platform Constraints and Design Boundaries | Approved | 2026-06-14 |
| [[form-architecture-and-state|Form Architecture and State Management]] | Form Architecture and State Management | Approved | 2026-06-14 |
| [[real-time-and-background-tasks|Real-Time and Background Tasks]] | Real-Time Updates and Background Task Architecture | Approved | 2026-06-14 |
| [[ui-customization-approach|UI Customization Approach]] | UI Customization Approach | Approved | 2026-06-14 |
| [[webhook-architecture|Webhook Architecture]] | Webhook Architecture | Approved | 2026-06-14 |
| [[pdf-invoice-generation|PDF Invoice Generation]] | PDF Invoice Generation | Approved | 2026-06-14 |
| [[data-access-patterns|Data Access Patterns and Query Limitations]] | Data Access Patterns and Query Limitations | Approved | 2026-06-14 |
| [[dependency-based-not-multi-tenant|Dependency-Based Architecture, Not Multi-Tenant]] | Dependency-Based Architecture, Not Multi-Tenant | Confirmed | 2026-06-13 |
| [[client-instance-readme-five-app-system|Client Instance README Five-App System]] | Mandatory README in Every Client Instance Documenting the Five-App System | Accepted | 2026-06-28 |
| [[role-property-assignment-mechanism|Role Property Assignment Mechanism]] | Role Property Assignment Mechanism (Designer vs. Code) | **Superseded** | 2026-06-27 |
| [[responsive-behaviour-mechanism|Responsive Behaviour Mechanism]] | Responsive Behaviour Mechanism | Accepted | 2026-06-27 |
| [[htmltemplate-use|HTMLTemplate Use]] | HTMLTemplate Use | Accepted | 2026-06-27 |
| [[dark-mode-v1|Dark Mode V1]] | Dark Mode — V1 Inclusion | Accepted | 2026-07-03 |
| [[dev-tooling-source-repos-must-be-github-backed|All Dev-Tooling Source Repositories Must Be GitHub-Backed]] | All Dev-Tooling Source Repositories Must Be GitHub-Backed | Confirmed | 2026-08-05 |

---

## Local ADRs (`adr-local/`)

App-specific decisions — apply to mb-3-cs (Consulting & Services) only.

| ADR File | Title | Status | Date |
|---|---|---|---|
| `schema-scope-reduction.md` | Schema Scope Reduction | Accepted | 2026-05-03 |

---

## Notes

### Reorganization (2026-07-06)

- **Numeric prefixes dropped.** ADRs are now referenced by descriptive slug, not number. All files renamed from `NN-slug.md` to `slug.md`.
- **Global/local split.** 39 ADRs apply company-wide; 1 ADR is CS-specific. Contents validated per-ADR before classification.
- **4 ADRs deleted** as superseded/historical: `multi-vertical-to-single-vertical-conversion` (historical, no longer relevant), `consolidated-build-sequence` (superseded), `system-currency-setting` (superseded by [[system-currency-selection-and-immutability|System Currency Selection and Immutability]]), `onboarding-finality` (cancelled — fully reversed by replacement [[onboarding-finality|Onboarding Finality]]).

### Legacy numeric references

- **ADR-07 and ADR-08:** Permanently skipped — numbers assigned to obsolete decisions, files never created. These numbers are now retired; no ADRs occupy these slots.

### Notable ADRs

- **[[system-currency-selection-and-immutability|System Currency Selection and Immutability]]:** Consolidated from original ADR-13 and ADR-16. Covers system currency, display currency, immutability enforcement, and currency conversion strategy.
- **[[onboarding-finality|Onboarding Finality]]:** Created 2026-05-31, updated 2026-06-01. Onboarding is resumable and revisitable. Owners may change any credential at any time. Mybizz_management maintains an append-only amendment log with three data tables. Reversed and fully replaced the original `onboarding-finality` (deleted).
- **[[client-instance-architecture|Client Instance Architecture]]:** Defines the dependency-based architecture. Confirmed by live testing (Test A: app_tables resolution, Test B: forms from dependency). Foundation for all data access patterns.
- **[[dependency-update-model|Dependency Update Model]]:** Four-app update flow (mb-3-cs → master_template → client instances). Branch propagation confirmed.
- **[[anvil-platform-constraints|Anvil Platform Constraints and Design Boundaries]] through [[data-access-patterns|Data Access Patterns and Query Limitations]]:** Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md.
- **[[dependency-based-not-multi-tenant|Dependency-Based Architecture, Not Multi-Tenant]]:** Definitive statement that Mybizz CS is a dependency-based SaaS platform, not a multi-tenant application. Prohibits tenant discriminator columns and tenant-filtered queries.
- **[[client-instance-readme-five-app-system|Client Instance README Five-App System]]:** Every client instance must contain a standardized README documenting the five-app architecture and the constraint against adding forms or modules directly to client instances.
- **[[role-property-assignment-mechanism|Role Property Assignment Mechanism]]:** Superseded. Original decision: set `role` via Designer Properties Panel. Reversed by project-wide property-setting rule: if a property can be set programmatically, it must be set programmatically. Current decision: set `role` in code (`self.component.role = "role-name"`).
- **[[responsive-behaviour-mechanism|Responsive Behaviour Mechanism]]:** Resolves contradicting breakpoint models in design-direction.md. Responsive behaviour uses `wrap_on` per-container, not CSS breakpoint tables. Nav collapse is automatic and separate.
- **[[htmltemplate-use|HTMLTemplate Use]]:** `HTMLTemplate` is banned. All current use cases have native M3 alternatives. Wireframes using it require reworking.
- **[[dark-mode-v1|Dark Mode V1]]:** Dark mode incorporated into V1. No longer deferred to V2. All screens require `@media (prefers-color-scheme: dark)` blocks.
- **[[ui-customization-approach|UI Customization Approach]]:** Partially superseded by [[htmltemplate-use|HTMLTemplate Use]] on layout components (native M3 Layouts are standard). M3+CSS customization approach for styling remains valid.
- **[[dev-tooling-source-repos-must-be-github-backed|All Dev-Tooling Source Repositories Must Be GitHub-Backed]]:** Grew out of a 2026-08-05 `gbrain doctor` root-cause investigation that found two PDLF-ecosystem sources (`pdlf`, `template-project-library`) as local-only working trees with no GitHub remote — the actual cause of a persistent `sync_freshness` failure and an unmanaged data-loss risk. Requires every dev-tooling source to be GitHub-backed: normal private repos for live tools, GitHub template repos for copy-to-start scaffolds.

---

*End of file — adr-index.md*
