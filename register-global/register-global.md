---
document: Register — project-library-global
doc-id: register-global
state: Live
date-created: 2026-07-25T150027+0200
---

# Register — project-library-global

One row per real corpus document. `doc-id` is the filename without its `.md`
extension. No sequence-number identifier is used. Regenerated from the live file
tree on 2026-08-27 (post rename + de-index).

| doc-id | filename | folder | type | state | notes |
|---|---|---|---|---|---|
| adr-anvil-extras-exclusion | adr-global/adr-anvil-extras-exclusion.md | adr-global | adr | Live |  |
| adr-anvil-platform-constraints | adr-global/adr-anvil-platform-constraints.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. |
| adr-brevo-replaces-zoho-email | adr-global/adr-brevo-replaces-zoho-email.md | adr-global | adr | Live |  |
| adr-client-data-management-rights-and-mybizz-retention-boundary | adr-global/adr-client-data-management-rights-and-mybizz-retention-boundary.md | adr-global | adr | Live |  |
| adr-client-instance-architecture | adr-global/adr-client-instance-architecture.md | adr-global | adr | Live | Defines the dependency-based architecture. Confirmed by live testing (Test A: app_tables resolution, Test B: forms from dependency). Foundation for all data access patterns. |
| adr-client-instance-readme-five-app-system | adr-global/adr-client-instance-readme-five-app-system.md | adr-global | adr | Live | Every client instance must contain a standardized README documenting the five-app architecture and the constraint against adding forms or modules directly to client instances. |
| adr-dark-mode-v1 | adr-global/adr-dark-mode-v1.md | adr-global | adr | Live | Dark mode incorporated into V1. No longer deferred to V2. All screens require `@media (prefers-color-scheme: dark)` blocks. |
| adr-data-access-patterns | adr-global/adr-data-access-patterns.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. |
| adr-dependency-based-not-multi-tenant | adr-global/adr-dependency-based-not-multi-tenant.md | adr-global | adr | Live | Definitive statement that Mybizz CS is a dependency-based SaaS platform, not a multi-tenant application. Prohibits tenant discriminator columns and tenant-filtered queries. |
| adr-dependency-update-model | adr-global/adr-dependency-update-model.md | adr-global | adr | Live | Four-app update flow (mb-3-cs → master_template → client instances). Branch propagation confirmed. |
| adr-design-rules | adr-global/adr-design-rules.md | adr-global | adr | Live |  |
| adr-dev-tooling-source-repos-must-be-github-backed | adr-global/adr-dev-tooling-source-repos-must-be-github-backed.md | adr-global | adr | Live | Grew out of a 2026-08-05 `gbrain doctor` root-cause investigation that found two PDLF-ecosystem sources (`pdlf`, `template-project-library`) as local-only working trees with no GitHub remote — the actual cause of a persistent `sync_freshness` failure and an unmanaged data-loss risk. Requires every dev-tooling source to be GitHub-backed: normal private repos for live tools, GitHub template repos for copy-to-start scaffolds. |
| adr-form-architecture-and-state | adr-global/adr-form-architecture-and-state.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. |
| adr-free-trial-abandoned | adr-global/adr-free-trial-abandoned.md | adr-global | adr | Live |  |
| adr-frontmatter-exemption-transient-files | adr-global/adr-frontmatter-exemption-transient-files.md | adr-global | adr | Live |  |
| adr-htmltemplate-use | adr-global/adr-htmltemplate-use.md | adr-global | adr | Live | `HTMLTemplate` is banned. All current use cases have native M3 alternatives. Wireframes using it require reworking. |
| adr-instructions-md-per-folder | adr-global/adr-instructions-md-per-folder.md | adr-global | adr | Live |  |
| adr-lead-capture-simultaneous-creation | adr-global/adr-lead-capture-simultaneous-creation.md | adr-global | adr | Live |  |
| adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture | adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md | adr-global | adr | Live |  |
| adr-material-3-theme-component-scope | adr-global/adr-material-3-theme-component-scope.md | adr-global | adr | Live |  |
| adr-mybizz-management-visibility | adr-global/adr-mybizz-management-visibility.md | adr-global | adr | Live |  |
| adr-navigation-lambda-link-open-form | adr-global/adr-navigation-lambda-link-open-form.md | adr-global | adr | Live |  |
| adr-observability-architecture | adr-global/adr-observability-architecture.md | adr-global | adr | Live |  |
| adr-onboarding-data-schema-alignment | adr-global/adr-onboarding-data-schema-alignment.md | adr-global | adr | Live |  |
| adr-onboarding-finality | adr-global/adr-onboarding-finality.md | adr-global | adr | Live | Created 2026-05-31, updated 2026-06-01. Onboarding is resumable and revisitable. Owners may change any credential at any time. Mybizz_management maintains an append-only amendment log with three data tables. Reversed and fully replaced the original `onboarding-finality` (deleted). |
| adr-onboarding-resumability | adr-global/adr-onboarding-resumability.md | adr-global | adr | Live |  |
| adr-onboarding-vs-settings-boundary | adr-global/adr-onboarding-vs-settings-boundary.md | adr-global | adr | Live |  |
| adr-openai-embedding-provider | adr-global/adr-openai-embedding-provider.md | adr-global | adr | Live |  |
| adr-payment-gateway-configuration-is-a-settings-function-and-is-rbac-governed | adr-global/adr-payment-gateway-configuration-is-a-settings-function-and-is-rbac-governed.md | adr-global | adr | Live |  |
| adr-payment-gateway-mutability | adr-global/adr-payment-gateway-mutability.md | adr-global | adr | Live |  |
| adr-payment-security-boundary-vault | adr-global/adr-payment-security-boundary-vault.md | adr-global | adr | Live |  |
| adr-pdf-invoice-generation | adr-global/adr-pdf-invoice-generation.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. |
| adr-real-time-and-background-tasks | adr-global/adr-real-time-and-background-tasks.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. |
| adr-responsive-behaviour-mechanism | adr-global/adr-responsive-behaviour-mechanism.md | adr-global | adr | Live | Resolves contradicting breakpoint models in design-direction.md. Responsive behaviour uses `wrap_on` per-container, not CSS breakpoint tables. Nav collapse is automatic and separate. |
| adr-role-property-assignment-mechanism | adr-global/adr-role-property-assignment-mechanism.md | adr-global | adr | Live | Superseded. Original decision: set `role` via Designer Properties Panel. Reversed by project-wide property-setting rule: if a property can be set programmatically, it must be set programmatically. Current decision: set `role` in code (`self.component.role = "role-name"`). |
| adr-single-contacts-table | adr-global/adr-single-contacts-table.md | adr-global | adr | Live |  |
| adr-system-currency-selection-and-immutability | adr-global/adr-system-currency-selection-and-immutability.md | adr-global | adr | Live | Consolidated from original ADR-13 and ADR-16. Covers system currency, display currency, immutability enforcement, and currency conversion strategy. |
| adr-tiers-model | adr-global/adr-tiers-model.md | adr-global | adr | Live |  |
| adr-timezone-utc-storage-display-conversion | adr-global/adr-timezone-utc-storage-display-conversion.md | adr-global | adr | Live |  |
| adr-ui-customization-approach | adr-global/adr-ui-customization-approach.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. Partially superseded by [[adr-htmltemplate-use]] on layout components (native M3 Layouts are standard). M3+CSS customization approach for styling remains valid. |
| adr-webhook-architecture | adr-global/adr-webhook-architecture.md | adr-global | adr | Live | Created 2026-06-14. Consolidated decisions from the "Issues to be resolved" section of platform-overview.md. |
| docstd-business-requirements-document | docs-standard-global/docstd-business-requirements-document.md | docs-standard-global | guide | Live |  |
| docstd-globals-contract | docs-standard-global/docstd-globals-contract.md | docs-standard-global | guide | Live |  |
| docstd-product-requirements-document | docs-standard-global/docstd-product-requirements-document.md | docs-standard-global | guide | Live |  |
| docstd-software-requirements-specification | docs-standard-global/docstd-software-requirements-specification.md | docs-standard-global | guide | Live |  |
| gui-anvil-deprecated-guide | guides-global/gui-anvil-deprecated-guide.md | guides-global | guide | Live |  |
| gui-Anvil-Debugging-Guide | guides-global/gui-Anvil-Debugging-Guide.md | guides-global | guide | Live |  |
| pol-anvil-first-development | policy-global/pol-anvil-first-development.md | policy-global | policy | Live |  |
| pol-documentation-and-decisions | policy-global/pol-documentation-and-decisions.md | policy-global | policy | Live |  |
| pol-security-and-data-governance | policy-global/pol-security-and-data-governance.md | policy-global | policy | Live |  |
| pol-testing-and-quality | policy-global/pol-testing-and-quality.md | policy-global | policy | Live |  |
| spec-anvil-platform-standards | specifications-global/spec-anvil-platform-standards.md | specifications-global | spec | Live |  |
| spec-anvil-spec-table | specifications-global/spec-anvil-spec-table.md | specifications-global | spec | Live |  |
| spec-api-specification | specifications-global/spec-api-specification.md | specifications-global | spec | Live |  |
| spec-client-activation-runbook | specifications-global/spec-client-activation-runbook.md | specifications-global | spec | Live |  |
| spec-component-properties | specifications-global/spec-component-properties.md | specifications-global | spec | Live |  |
| spec-deployment | specifications-global/spec-deployment.md | specifications-global | spec | Live |  |
| spec-five-app-architecture-model | specifications-global/spec-five-app-architecture-model.md | specifications-global | spec | Live |  |
| spec-integration | specifications-global/spec-integration.md | specifications-global | spec | Live |  |
| spec-m3-design-standards | specifications-global/spec-m3-design-standards.md | specifications-global | spec | Live |  |
| spec-m3_component_mapping | specifications-global/spec-m3_component_mapping.md | specifications-global | spec | Live |  |
| spec-material-3-theme | specifications-global/spec-material-3-theme.md | specifications-global | spec | Live |  |
| spec-nomenclature | specifications-global/spec-nomenclature.md | specifications-global | spec | Live |  |
| spec-observability | specifications-global/spec-observability.md | specifications-global | spec | Live |  |
| spec-onboarding-implementation-plan | specifications-global/spec-onboarding-implementation-plan.md | specifications-global | spec | Live |  |
| spec-regulatory-compliance-baseline | specifications-global/spec-regulatory-compliance-baseline.md | specifications-global | spec | Live |  |
| spec-screen-and-wireframe-production-standards | specifications-global/spec-screen-and-wireframe-production-standards.md | specifications-global | spec | Live |  |
| spec-screen-production-standard | specifications-global/spec-screen-production-standard.md | specifications-global | spec | Live |  |
| spec-security-architecture | specifications-global/spec-security-architecture.md | specifications-global | spec | Live |  |
| spec-security | specifications-global/spec-security.md | specifications-global | spec | Live |  |
| spec-testing-methodology-standards | specifications-global/spec-testing-methodology-standards.md | specifications-global | spec | Live |  |
| spec-testing | specifications-global/spec-testing.md | specifications-global | spec | Live |  |
| spec-ui-standards | specifications-global/spec-ui-standards.md | specifications-global | spec | Live |  |
| spec-vault-system | specifications-global/spec-vault-system.md | specifications-global | spec | Live |  |
| sop-deployment-procedures | standard-operating-procedures-global/sop-deployment-procedures.md | standard-operating-procedures-global | sop | Live |  |
| sop-offboarding | standard-operating-procedures-global/sop-offboarding.md | standard-operating-procedures-global | sop | Live |  |
| sop-vault-totp-recovery | standard-operating-procedures-global/sop-vault-totp-recovery.md | standard-operating-procedures-global | sop | Live |  |
| sop-agent-readiness-framework | standard-operating-procedures-global/Agent readiness/sop-agent-readiness-framework.md | standard-operating-procedures-global/Agent readiness | sop | Live |  |
| sop-set3-anvil_cop_agent_readiness | standard-operating-procedures-global/Agent readiness/sop-set3-anvil_cop_agent_readiness.md | standard-operating-procedures-global/Agent readiness | sop | Live |  |
| tmp-authoritative-schema | templates-global/tmp-authoritative-schema.md | templates-global | template | — |  |
| tmp-chklist-anvil-app-testing | templates-global/tmp-chklist-anvil-app-testing.md | templates-global | template | — |  |
| tmp-chklist-screen | templates-global/tmp-chklist-screen.md | templates-global | template | — |  |
| tmp-chklist-wireframe | templates-global/tmp-chklist-wireframe.md | templates-global | template | — |  |
| tmp-custom-component-requirements-matrix | templates-global/tmp-custom-component-requirements-matrix.md | templates-global | template | — |  |

## Field definitions

- **doc-id** — filename without the `.md` extension.
- **filename** — repository-relative path to the file.
- **folder** — directory containing the file, relative to the repository root.
- **type** — document type, derived from the containing folder (adr / spec / policy / sop / template / guide / other).
- **state** — the document's own front-matter `state` value (`—` when the file carries no front-matter `state`, e.g. transient templates).
- **notes** — free text; for ADRs, the narrative carried forward from the deleted `adr-index.md`.

## Index history (carried from deleted adr-index.md)

These narratives from the former ADR index describe the corpus or entries that no
longer have a live register row, so they are preserved here rather than lost with the
deleted index files.

- **Numeric prefixes dropped (reorganization 2026-07-06):** ADRs are referenced by descriptive slug, not number. All files renamed from `NN-slug.md` to `slug.md`.
- **Global/local split (2026-07-06):** 39 ADRs apply company-wide; 1 ADR is CS-specific. Contents validated per-ADR before classification.
- **4 ADRs deleted as superseded/historical (2026-07-06):** `multi-vertical-to-single-vertical-conversion` (historical, no longer relevant), `consolidated-build-sequence` (superseded), `system-currency-setting` (superseded by `adr-system-currency-selection-and-immutability`), `onboarding-finality` (cancelled — fully reversed by replacement `adr-onboarding-finality`).
- **Legacy numeric references:** ADR-07 and ADR-08 are permanently skipped — numbers assigned to obsolete decisions, files never created. These numbers are retired; no ADRs occupy these slots.
