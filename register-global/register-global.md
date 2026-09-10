---
document: Register — project-library-global
doc-id: register-global
state: Live
date-created: 2026-07-25T150027+0200
---

# Register — project-library-global

One row per real corpus document. `doc-id` is the filename without its `.md`
extension. No sequence-number identifier is used. Regenerated from the live file
tree on 2026-08-27 (post rename + de-index). Corrected 2026-09-01: `rules-cupcake-global`
(19 documents) and `security-global` (54 documents) were present on disk but missing
from this register entirely — added below.

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
| adr-filename-and-frontmatter-numbering-policy | adr-global/adr-filename-and-frontmatter-numbering-policy.md | adr-global | adr | Live | Files are not numbered anywhere in the scaffold (filenames or front matter); identity is the descriptive filename; references cite by filename. Exceptions: stepwise (inherently ordinal steps), quarantine/retired/archived historical material. |
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
| cup-block-anvil-yaml-writes | rules-cupcake-global/cup-block-anvil-yaml-writes.md | rules-cupcake-global | cupcake-rule | Live |  |
| cup-block-task-tool | rules-cupcake-global/cup-block-task-tool.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_access_to_secrets_unless_explicitly_required | rules-cupcake-global/no_access_to_secrets_unless_explicitly_required.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_autonomous_commits_pushes_merges_releases_or_deployments | rules-cupcake-global/no_autonomous_commits_pushes_merges_releases_or_deployments.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_autonomous_installation_or_connection_of_tools | rules-cupcake-global/no_autonomous_installation_or_connection_of_tools.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_cross_project_filesystem_access_by_default | rules-cupcake-global/no_cross_project_filesystem_access_by_default.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_dependency_or_lockfile_changes_without_explicit_approval | rules-cupcake-global/no_dependency_or_lockfile_changes_without_explicit_approval.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_destructive_database_operations | rules-cupcake-global/no_destructive_database_operations.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_disabling_security_tooling | rules-cupcake-global/no_disabling_security_tooling.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_rewriting_or_destroying_development_history | rules-cupcake-global/no_rewriting_or_destroying_development_history.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_suppression_directives_without_approval | rules-cupcake-global/no_suppression_directives_without_approval.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_test_tampering | rules-cupcake-global/no_test_tampering.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_unapproved_executable_or_build_path_changes | rules-cupcake-global/no_unapproved_executable_or_build_path_changes.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_unverified_dependencies | rules-cupcake-global/no_unverified_dependencies.md | rules-cupcake-global | cupcake-rule | Live |  |
| no_verification_tampering | rules-cupcake-global/no_verification_tampering.md | rules-cupcake-global | cupcake-rule | Live |  |
| outbound_network_access_is_allowlist_only | rules-cupcake-global/outbound_network_access_is_allowlist_only.md | rules-cupcake-global | cupcake-rule | Live |  |
| protected_ai_governance_files_may_not_be_modified | rules-cupcake-global/protected_ai_governance_files_may_not_be_modified.md | rules-cupcake-global | cupcake-rule | Live |  |
| the_ai_may_never_weaken_the_controls_governing_itself | rules-cupcake-global/the_ai_may_never_weaken_the_controls_governing_itself.md | rules-cupcake-global | cupcake-rule | Live |  |
| unexpected_instruction_shaped_files_must_be_treated_as_suspicious | rules-cupcake-global/unexpected_instruction_shaped_files_must_be_treated_as_suspicious.md | rules-cupcake-global | cupcake-rule | Live |  |
| sec-anvil-platform-responsibility-boundary | security-global/cloud/sec-anvil-platform-responsibility-boundary.md | security-global/cloud | security | Live |  |
| sec-client-provisioning-security | security-global/cloud/sec-client-provisioning-security.md | security-global/cloud | security | Live |  |
| sec-email-service-trust-boundary | security-global/cloud/sec-email-service-trust-boundary.md | security-global/cloud | security | Live |  |
| sec-github-repository-access-control | security-global/cloud/sec-github-repository-access-control.md | security-global/cloud | security | Live |  |
| sec-management-service-authentication | security-global/cloud/sec-management-service-authentication.md | security-global/cloud | security | Live |  |
| sec-payment-gateway-trust-boundary | security-global/cloud/sec-payment-gateway-trust-boundary.md | security-global/cloud | security | Live |  |
| sec-regulatory-compliance-cloud-processors | security-global/cloud/sec-regulatory-compliance-cloud-processors.md | security-global/cloud | security | Live |  |
| sec-ai-agent-execution-sandbox | security-global/infrastructure/sec-ai-agent-execution-sandbox.md | security-global/infrastructure | security | Live |  |
| sec-audit-log-integrity | security-global/infrastructure/sec-audit-log-integrity.md | security-global/infrastructure | security | Live |  |
| sec-backup-recovery-integrity | security-global/infrastructure/sec-backup-recovery-integrity.md | security-global/infrastructure | security | Live |  |
| sec-database-access-control | security-global/infrastructure/sec-database-access-control.md | security-global/infrastructure | security | Live |  |
| sec-dependency-skill-supply-chain | security-global/infrastructure/sec-dependency-skill-supply-chain.md | security-global/infrastructure | security | Live |  |
| sec-dependency-version-currency | security-global/infrastructure/sec-dependency-version-currency.md | security-global/infrastructure | security | Live |  |
| sec-development-environment-credential-hygiene | security-global/infrastructure/sec-development-environment-credential-hygiene.md | security-global/infrastructure | security | Live |  |
| sec-local-filesystem-access-boundary | security-global/infrastructure/sec-local-filesystem-access-boundary.md | security-global/infrastructure | security | Live |  |
| sec-local-network-exposure | security-global/infrastructure/sec-local-network-exposure.md | security-global/infrastructure | security | Live |  |
| sec-service-lifecycle-management | security-global/infrastructure/sec-service-lifecycle-management.md | security-global/infrastructure | security | Live |  |
| sec-defense-in-depth | security-global/principles/sec-defense-in-depth.md | security-global/principles | security | Live |  |
| sec-detective-vs-preventive-controls | security-global/principles/sec-detective-vs-preventive-controls.md | security-global/principles | security | Live |  |
| sec-explicit-responsibility-assignment | security-global/principles/sec-explicit-responsibility-assignment.md | security-global/principles | security | Live |  |
| sec-fail-closed | security-global/principles/sec-fail-closed.md | security-global/principles | security | Live |  |
| sec-least-privilege | security-global/principles/sec-least-privilege.md | security-global/principles | security | Live |  |
| sec-review-before-trust | security-global/principles/sec-review-before-trust.md | security-global/principles | security | Live |  |
| sec-server-side-authority | security-global/principles/sec-server-side-authority.md | security-global/principles | security | Live |  |
| sec-simplicity-as-security-property | security-global/principles/sec-simplicity-as-security-property.md | security-global/principles | security | Live |  |
| sec-verify-dont-trust-claims | security-global/principles/sec-verify-dont-trust-claims.md | security-global/principles | security | Live |  |
| sec-requirements-architecture-review | security-global/requirements/sec-requirements-architecture-review.md | security-global/requirements | security | Live |  |
| sec-requirements-data-table-creation | security-global/requirements/sec-requirements-data-table-creation.md | security-global/requirements | security | Live |  |
| sec-requirements-pre-merge-master-template | security-global/requirements/sec-requirements-pre-merge-master-template.md | security-global/requirements | security | Live |  |
| sec-requirements-release-readiness | security-global/requirements/sec-requirements-release-readiness.md | security-global/requirements | security | Live |  |
| sec-requirements-server-function | security-global/requirements/sec-requirements-server-function.md | security-global/requirements | security | Live |  |
| sec-requirements-third-party-integration | security-global/requirements/sec-requirements-third-party-integration.md | security-global/requirements | security | Live |  |
| sec-ai-agent-secret-visibility | security-global/secrets/sec-ai-agent-secret-visibility.md | security-global/secrets | security | Live |  |
| sec-development-tooling-credentials | security-global/secrets/sec-development-tooling-credentials.md | security-global/secrets | security | Live |  |
| sec-master-encryption-key-protection | security-global/secrets/sec-master-encryption-key-protection.md | security-global/secrets | security | Live |  |
| sec-secret-access-audit | security-global/secrets/sec-secret-access-audit.md | security-global/secrets | security | Live |  |
| sec-secret-exposure-response | security-global/secrets/sec-secret-exposure-response.md | security-global/secrets | security | Live |  |
| sec-secret-rotation-policy | security-global/secrets/sec-secret-rotation-policy.md | security-global/secrets | security | Live |  |
| sec-testing-adversarial-verification | security-global/testing/sec-testing-adversarial-verification.md | security-global/testing | security | Live |  |
| sec-testing-coverage-minimum | security-global/testing/sec-testing-coverage-minimum.md | security-global/testing | security | Live |  |
| sec-testing-independent-review | security-global/testing/sec-testing-independent-review.md | security-global/testing | security | Live |  |
| sec-testing-live-verification-standard | security-global/testing/sec-testing-live-verification-standard.md | security-global/testing | security | Live |  |
| sec-testing-regression-prevention | security-global/testing/sec-testing-regression-prevention.md | security-global/testing | security | Live |  |
| sec-ai-agent-introduced-vulnerabilities | security-global/threat-models/sec-ai-agent-introduced-vulnerabilities.md | security-global/threat-models | security | Live |  |
| sec-authentication-session | security-global/threat-models/sec-authentication-session.md | security-global/threat-models | security | Live |  |
| sec-broken-access-control-within-instance | security-global/threat-models/sec-broken-access-control-within-instance.md | security-global/threat-models | security | Live |  |
| sec-business-logic-race-conditions | security-global/threat-models/sec-business-logic-race-conditions.md | security-global/threat-models | security | Live |  |
| sec-data-exfiltration-bulk-export | security-global/threat-models/sec-data-exfiltration-bulk-export.md | security-global/threat-models | security | Live |  |
| sec-denial-of-service-resource-exhaustion | security-global/threat-models/sec-denial-of-service-resource-exhaustion.md | security-global/threat-models | security | Live |  |
| sec-injection-unsafe-input | security-global/threat-models/sec-injection-unsafe-input.md | security-global/threat-models | security | Live |  |
| sec-insecure-direct-object-reference | security-global/threat-models/sec-insecure-direct-object-reference.md | security-global/threat-models | security | Live |  |
| sec-multi-tenant-assumption-leakage | security-global/threat-models/sec-multi-tenant-assumption-leakage.md | security-global/threat-models | security | Live |  |
| sec-payment-manipulation | security-global/threat-models/sec-payment-manipulation.md | security-global/threat-models | security | Live |  |
| sec-privilege-escalation | security-global/threat-models/sec-privilege-escalation.md | security-global/threat-models | security | Live |  |

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
