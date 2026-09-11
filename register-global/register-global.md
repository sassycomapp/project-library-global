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

<!-- anvil-docs corpus registered 2026-09-10 per register-membership policy (align-docs function scope V2 item 6); collision-qualified doc-ids where basenames repeat -->
| anvil-docs-config | anvil-docs/anvil-docs-config.md | anvil-docs | anvil-docs | Live |  |
| anvil-docs-explainer | anvil-docs/anvil-docs-explainer.md | anvil-docs | anvil-docs | Live |  |
| anvil-docs-reference | anvil-docs/anvil-docs-reference.md | anvil-docs | anvil-docs | Live |  |
| anvil-docs-README | anvil-docs/README.md | anvil-docs | anvil-docs | Live |  |
| site-map | anvil-docs/site-map.md | anvil-docs | anvil-docs | Live |  |
| agent-chat-window | anvil-docs/ai/agent-chat-window.md | anvil-docs/ai | anvil-docs | Live |  |
| connecting-your-account | anvil-docs/ai/connecting-your-account.md | anvil-docs/ai | anvil-docs | Live |  |
| ai-_index | anvil-docs/ai/_index.md | anvil-docs/ai | anvil-docs | Live |  |
| anvil.email | anvil-docs/api/anvil.email.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.email.message | anvil-docs/api/anvil.email.message.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.facebook.auth | anvil-docs/api/anvil.facebook.auth.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.files | anvil-docs/api/anvil.files.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.google.auth | anvil-docs/api/anvil.google.auth.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.google.drive | anvil-docs/api/anvil.google.drive.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.google.mail | anvil-docs/api/anvil.google.mail.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.google.sheets | anvil-docs/api/anvil.google.sheets.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.googlemap.data | anvil-docs/api/anvil.googlemap.data.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.googlemap | anvil-docs/api/anvil.googlemap.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.http | anvil-docs/api/anvil.http.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.image | anvil-docs/api/anvil.image.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.js | anvil-docs/api/anvil.js.md | anvil-docs/api | anvil-docs | Live |  |
| anvil | anvil-docs/api/anvil.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.media | anvil-docs/api/anvil.media.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.microsoft.auth | anvil-docs/api/anvil.microsoft.auth.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.mpl_util | anvil-docs/api/anvil.mpl_util.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.pdf | anvil-docs/api/anvil.pdf.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.pico-micro-uplink | anvil-docs/api/anvil.pico-micro-uplink.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.plotly_templates | anvil-docs/api/anvil.plotly_templates.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.saml.auth | anvil-docs/api/anvil.saml.auth.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.script | anvil-docs/api/anvil.script.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.secrets | anvil-docs/api/anvil.secrets.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.server-uplink | anvil-docs/api/anvil.server-uplink.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.server | anvil-docs/api/anvil.server.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.stripe | anvil-docs/api/anvil.stripe.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.tables | anvil-docs/api/anvil.tables.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.tables.query | anvil-docs/api/anvil.tables.query.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.tz | anvil-docs/api/anvil.tz.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.users | anvil-docs/api/anvil.users.md | anvil-docs/api | anvil-docs | Live |  |
| anvil.users.mfa | anvil-docs/api/anvil.users.mfa.md | anvil-docs/api | anvil-docs | Live |  |
| segment.client | anvil-docs/api/segment.client.md | anvil-docs/api | anvil-docs | Live |  |
| stripe.checkout | anvil-docs/api/stripe.checkout.md | anvil-docs/api | anvil-docs | Live |  |
| api-_index | anvil-docs/api/_index.md | anvil-docs/api | anvil-docs | Live |  |
| app-structure | anvil-docs/app-structure/app-structure.md | anvil-docs/app-structure | anvil-docs | Live |  |
| client-quickstart | anvil-docs/client/quickstart.md | anvil-docs/client | anvil-docs | Live |  |
| client-_index | anvil-docs/client/_index.md | anvil-docs/client | anvil-docs | Live |  |
| adding-html-elements | anvil-docs/client/adding-ui-elements/adding-html-elements.md | anvil-docs/client/adding-ui-elements | anvil-docs | Live |  |
| alerts-and-notifications | anvil-docs/client/adding-ui-elements/alerts-and-notifications.md | anvil-docs/client/adding-ui-elements | anvil-docs | Live |  |
| adding-ui-elements-containers | anvil-docs/client/adding-ui-elements/containers.md | anvil-docs/client/adding-ui-elements | anvil-docs | Live |  |
| loading-indicator | anvil-docs/client/adding-ui-elements/loading-indicator.md | anvil-docs/client/adding-ui-elements | anvil-docs | Live |  |
| adding-ui-elements-_index | anvil-docs/client/adding-ui-elements/_index.md | anvil-docs/client/adding-ui-elements | anvil-docs | Live |  |
| modules | anvil-docs/client/client-code/modules.md | anvil-docs/client/client-code | anvil-docs | Live |  |
| the-python-environment | anvil-docs/client/client-code/the-python-environment.md | anvil-docs/client/client-code | anvil-docs | Live |  |
| client-code-_index | anvil-docs/client/client-code/_index.md | anvil-docs/client/client-code | anvil-docs | Live |  |
| data-bindings | anvil-docs/client/component-properties/data-bindings.md | anvil-docs/client/component-properties | anvil-docs | Live |  |
| component-properties-_index | anvil-docs/client/component-properties/_index.md | anvil-docs/client/component-properties | anvil-docs | Live |  |
| assets | anvil-docs/client/customisation/assets.md | anvil-docs/client/customisation | anvil-docs | Live |  |
| colour-schemes | anvil-docs/client/customisation/colour-schemes.md | anvil-docs/client/customisation | anvil-docs | Live |  |
| customisation-_index | anvil-docs/client/customisation/_index.md | anvil-docs/client/customisation | anvil-docs | Live |  |
| html-components | anvil-docs/client/customisation/custom-components/html-components.md | anvil-docs/client/customisation/custom-components | anvil-docs | Live |  |
| custom-components-_index | anvil-docs/client/customisation/custom-components/_index.md | anvil-docs/client/customisation/custom-components | anvil-docs | Live |  |
| accessing-javascript | anvil-docs/client/customisation/javascript/accessing-javascript.md | anvil-docs/client/customisation/javascript | anvil-docs | Live |  |
| html-forms | anvil-docs/client/customisation/javascript/html-forms.md | anvil-docs/client/customisation/javascript | anvil-docs | Live |  |
| javascript-quickstart | anvil-docs/client/customisation/javascript/quickstart.md | anvil-docs/client/customisation/javascript | anvil-docs | Live |  |
| javascript-_index | anvil-docs/client/customisation/javascript/_index.md | anvil-docs/client/customisation/javascript | anvil-docs | Live |  |
| loading_indicator | anvil-docs/client/customisation/using-css/loading_indicator.md | anvil-docs/client/customisation/using-css | anvil-docs | Live |  |
| roles | anvil-docs/client/customisation/using-css/roles.md | anvil-docs/client/customisation/using-css | anvil-docs | Live |  |
| using-css-_index | anvil-docs/client/customisation/using-css/_index.md | anvil-docs/client/customisation/using-css | anvil-docs | Live |  |
| service-worker-whiteboard | anvil-docs/client/doc/service-worker-whiteboard.md | anvil-docs/client/doc | anvil-docs | Live |  |
| component-lifecycle | anvil-docs/client/events/component-lifecycle.md | anvil-docs/client/events | anvil-docs | Live |  |
| events-_index | anvil-docs/client/events/_index.md | anvil-docs/client/events | anvil-docs | Live |  |
| form-templates | anvil-docs/client/forms/form-templates.md | anvil-docs/client/forms | anvil-docs | Live |  |
| forms-as-components | anvil-docs/client/forms/forms-as-components.md | anvil-docs/client/forms | anvil-docs | Live |  |
| forms-as-html | anvil-docs/client/forms/forms-as-html.md | anvil-docs/client/forms | anvil-docs | Live |  |
| forms-as-python-classes | anvil-docs/client/forms/forms-as-python-classes.md | anvil-docs/client/forms | anvil-docs | Live |  |
| forms-in-the-editor | anvil-docs/client/forms/forms-in-the-editor.md | anvil-docs/client/forms | anvil-docs | Live |  |
| forms-_index | anvil-docs/client/forms/_index.md | anvil-docs/client/forms | anvil-docs | Live |  |
| html-layouts | anvil-docs/client/forms/layouts/html-layouts.md | anvil-docs/client/forms/layouts | anvil-docs | Live |  |
| layouts-api | anvil-docs/client/forms/layouts/layouts-api.md | anvil-docs/client/forms/layouts | anvil-docs | Live |  |
| layouts-quickstart | anvil-docs/client/forms/layouts/quickstart.md | anvil-docs/client/forms/layouts | anvil-docs | Live |  |
| layouts-_index | anvil-docs/client/forms/layouts/_index.md | anvil-docs/client/forms/layouts | anvil-docs | Live |  |
| navigation-_index | anvil-docs/client/navigation/_index.md | anvil-docs/client/navigation | anvil-docs | Live |  |
| caching | anvil-docs/client/navigation/routing/caching.md | anvil-docs/client/navigation/routing | anvil-docs | Live |  |
| navigation | anvil-docs/client/navigation/routing/navigation.md | anvil-docs/client/navigation/routing | anvil-docs | Live |  |
| parameters | anvil-docs/client/navigation/routing/parameters.md | anvil-docs/client/navigation/routing | anvil-docs | Live |  |
| routing-quickstart | anvil-docs/client/navigation/routing/quickstart.md | anvil-docs/client/navigation/routing | anvil-docs | Live |  |
| router | anvil-docs/client/navigation/routing/router.md | anvil-docs/client/navigation/routing | anvil-docs | Live |  |
| routing-_index | anvil-docs/client/navigation/routing/_index.md | anvil-docs/client/navigation/routing | anvil-docs | Live |  |
| components-_index | anvil-docs/components/_index.md | anvil-docs/components | anvil-docs | Live |  |
| components | anvil-docs/components/material-3/components.md | anvil-docs/components/material-3 | anvil-docs | Live |  |
| layouts | anvil-docs/components/material-3/layouts.md | anvil-docs/components/material-3 | anvil-docs | Live |  |
| material-3-_index | anvil-docs/components/material-3/_index.md | anvil-docs/components/material-3 | anvil-docs | Live |  |
| basic | anvil-docs/components/standard-components/basic.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| canvas | anvil-docs/components/standard-components/canvas.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| standard-components-containers | anvil-docs/components/standard-components/containers.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| data-grids | anvil-docs/components/standard-components/data-grids.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| html-component | anvil-docs/components/standard-components/html-component.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| maps | anvil-docs/components/standard-components/maps.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| plots | anvil-docs/components/standard-components/plots.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| repeating-panel | anvil-docs/components/standard-components/repeating-panel.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| standard-components-_index | anvil-docs/components/standard-components/_index.md | anvil-docs/components/standard-components | anvil-docs | Live |  |
| buffering | anvil-docs/data-tables/buffering.md | anvil-docs/data-tables | anvil-docs | Live |  |
| csv-and-excel | anvil-docs/data-tables/csv-and-excel.md | anvil-docs/data-tables | anvil-docs | Live |  |
| data-security | anvil-docs/data-tables/data-security.md | anvil-docs/data-tables | anvil-docs | Live |  |
| data-tables-in-code | anvil-docs/data-tables/data-tables-in-code.md | anvil-docs/data-tables | anvil-docs | Live |  |
| faster-storage | anvil-docs/data-tables/faster-storage.md | anvil-docs/data-tables | anvil-docs | Live |  |
| indexes | anvil-docs/data-tables/indexes.md | anvil-docs/data-tables | anvil-docs | Live |  |
| legacy-tables | anvil-docs/data-tables/legacy-tables.md | anvil-docs/data-tables | anvil-docs | Live |  |
| links-between-tables | anvil-docs/data-tables/links-between-tables.md | anvil-docs/data-tables | anvil-docs | Live |  |
| multiple-databases | anvil-docs/data-tables/multiple-databases.md | anvil-docs/data-tables | anvil-docs | Live |  |
| data-tables-quickstart | anvil-docs/data-tables/quickstart.md | anvil-docs/data-tables | anvil-docs | Live |  |
| sql-access | anvil-docs/data-tables/sql-access.md | anvil-docs/data-tables | anvil-docs | Live |  |
| transactions | anvil-docs/data-tables/transactions.md | anvil-docs/data-tables | anvil-docs | Live |  |
| data-tables-_index | anvil-docs/data-tables/_index.md | anvil-docs/data-tables | anvil-docs | Live |  |
| server_funcs | anvil-docs/data-tables/anvil/tables/v2/server_funcs.md | anvil-docs/data-tables/anvil/tables/v2 | anvil-docs | Live |  |
| types | anvil-docs/data-tables/anvil/tables/v2/types.md | anvil-docs/data-tables/anvil/tables/v2 | anvil-docs | Live |  |
| data-files-quickstart | anvil-docs/data-tables/data-files/quickstart.md | anvil-docs/data-tables/data-files | anvil-docs | Live |  |
| data-files-_index | anvil-docs/data-tables/data-files/_index.md | anvil-docs/data-tables/data-files | anvil-docs | Live |  |
| client-writable | anvil-docs/data-tables/model-classes/client-writable.md | anvil-docs/data-tables/model-classes | anvil-docs | Live |  |
| creating | anvil-docs/data-tables/model-classes/creating.md | anvil-docs/data-tables/model-classes | anvil-docs | Live |  |
| patterns | anvil-docs/data-tables/model-classes/patterns.md | anvil-docs/data-tables/model-classes | anvil-docs | Live |  |
| validation | anvil-docs/data-tables/model-classes/validation.md | anvil-docs/data-tables/model-classes | anvil-docs | Live |  |
| model-classes-_index | anvil-docs/data-tables/model-classes/_index.md | anvil-docs/data-tables/model-classes | anvil-docs | Live |  |
| anvil-debugging-guide | anvil-docs/debugging-guide/anvil-debugging-guide.md | anvil-docs/debugging-guide | anvil-docs | Live |  |
| custom-domains | anvil-docs/deployment/custom-domains.md | anvil-docs/deployment | anvil-docs | Live |  |
| deployment-dependencies | anvil-docs/deployment/dependencies.md | anvil-docs/deployment | anvil-docs | Live |  |
| embedding-your-app | anvil-docs/deployment/embedding-your-app.md | anvil-docs/deployment | anvil-docs | Live |  |
| hosting-options | anvil-docs/deployment/hosting-options.md | anvil-docs/deployment | anvil-docs | Live |  |
| on-site | anvil-docs/deployment/on-site.md | anvil-docs/deployment | anvil-docs | Live |  |
| deployment-quickstart | anvil-docs/deployment/quickstart.md | anvil-docs/deployment | anvil-docs | Live |  |
| runtime-repo-dependencies | anvil-docs/deployment/runtime-repo-dependencies.md | anvil-docs/deployment | anvil-docs | Live |  |
| deployment-_index | anvil-docs/deployment/_index.md | anvil-docs/deployment | anvil-docs | Live |  |
| environments-and-code | anvil-docs/deployment/environments/environments-and-code.md | anvil-docs/deployment/environments | anvil-docs | Live |  |
| environments-_index | anvil-docs/deployment/environments/_index.md | anvil-docs/deployment/environments | anvil-docs | Live |  |
| form-editor | anvil-docs/editor/form-editor.md | anvil-docs/editor | anvil-docs | Live |  |
| keyboard-shortcuts | anvil-docs/editor/keyboard-shortcuts.md | anvil-docs/editor | anvil-docs | Live |  |
| look-and-feel | anvil-docs/editor/look-and-feel.md | anvil-docs/editor | anvil-docs | Live |  |
| editor-_index | anvil-docs/editor/_index.md | anvil-docs/editor | anvil-docs | Live |  |
| profiling-and-tracing | anvil-docs/editor/app-logs/profiling-and-tracing.md | anvil-docs/editor/app-logs | anvil-docs | Live |  |
| app-logs-_index | anvil-docs/editor/app-logs/_index.md | anvil-docs/editor/app-logs | anvil-docs | Live |  |
| cloning-and-collaboration | anvil-docs/editor/app-settings/cloning-and-collaboration.md | anvil-docs/editor/app-settings | anvil-docs | Live |  |
| app-settings-data-tables | anvil-docs/editor/app-settings/data-tables.md | anvil-docs/editor/app-settings | anvil-docs | Live |  |
| titles-and-logos | anvil-docs/editor/app-settings/titles-and-logos.md | anvil-docs/editor/app-settings | anvil-docs | Live |  |
| app-settings-_index | anvil-docs/editor/app-settings/_index.md | anvil-docs/editor/app-settings | anvil-docs | Live |  |
| managed-enterprise | anvil-docs/enterprise/managed-enterprise.md | anvil-docs/enterprise | anvil-docs | Live |  |
| trials | anvil-docs/enterprise/trials.md | anvil-docs/enterprise | anvil-docs | Live |  |
| enterprise-_index | anvil-docs/enterprise/_index.md | anvil-docs/enterprise | anvil-docs | Live |  |
| custom | anvil-docs/enterprise/deployment/custom.md | anvil-docs/enterprise/deployment | anvil-docs | Live |  |
| docker | anvil-docs/enterprise/deployment/docker.md | anvil-docs/enterprise/deployment | anvil-docs | Live |  |
| enterprise-deployment-index | anvil-docs/enterprise/deployment/_index.md | anvil-docs/enterprise/deployment | anvil-docs | Live |  |
| aks | anvil-docs/enterprise/deployment/kubernetes/aks.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| configuration | anvil-docs/enterprise/deployment/kubernetes/configuration.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| eks | anvil-docs/enterprise/deployment/kubernetes/eks.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| gke | anvil-docs/enterprise/deployment/kubernetes/gke.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| installation | anvil-docs/enterprise/deployment/kubernetes/installation.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| k3s | anvil-docs/enterprise/deployment/kubernetes/k3s.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| k8s-prerequisites | anvil-docs/enterprise/deployment/kubernetes/k8s-prerequisites.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| oke | anvil-docs/enterprise/deployment/kubernetes/oke.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| openshift | anvil-docs/enterprise/deployment/kubernetes/openshift.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| kubernetes-_index | anvil-docs/enterprise/deployment/kubernetes/_index.md | anvil-docs/enterprise/deployment/kubernetes | anvil-docs | Live |  |
| changelog | anvil-docs/enterprise/deployment/operator/changelog.md | anvil-docs/enterprise/deployment/operator | anvil-docs | Live |  |
| cluster | anvil-docs/enterprise/deployment/operator/cluster.md | anvil-docs/enterprise/deployment/operator | anvil-docs | Live |  |
| restore | anvil-docs/enterprise/deployment/operator/restore.md | anvil-docs/enterprise/deployment/operator | anvil-docs | Live |  |
| operator-_index | anvil-docs/enterprise/deployment/operator/_index.md | anvil-docs/enterprise/deployment/operator | anvil-docs | Live |  |
| github | anvil-docs/enterprise/deployment/prerequisites/github.md | anvil-docs/enterprise/deployment/prerequisites | anvil-docs | Live |  |
| google | anvil-docs/enterprise/deployment/prerequisites/google.md | anvil-docs/enterprise/deployment/prerequisites | anvil-docs | Live |  |
| microsoft | anvil-docs/enterprise/deployment/prerequisites/microsoft.md | anvil-docs/enterprise/deployment/prerequisites | anvil-docs | Live |  |
| tls-certificates | anvil-docs/enterprise/deployment/prerequisites/tls-certificates.md | anvil-docs/enterprise/deployment/prerequisites | anvil-docs | Live |  |
| prerequisites-_index | anvil-docs/enterprise/deployment/prerequisites/_index.md | anvil-docs/enterprise/deployment/prerequisites | anvil-docs | Live |  |
| external-resources-external-database | anvil-docs/external-resources/external-database.md | anvil-docs/external-resources | anvil-docs | Live |  |
| external-resources-_index | anvil-docs/external-resources/_index.md | anvil-docs/external-resources | anvil-docs | Live |  |
| http-apis-_index | anvil-docs/external-resources/http-apis/_index.md | anvil-docs/external-resources/http-apis | anvil-docs | Live |  |
| authentication | anvil-docs/external-resources/http-apis/creating-http-endpoints/authentication.md | anvil-docs/external-resources/http-apis/creating-http-endpoints | anvil-docs | Live |  |
| creating-http-endpoints-quickstart | anvil-docs/external-resources/http-apis/creating-http-endpoints/quickstart.md | anvil-docs/external-resources/http-apis/creating-http-endpoints | anvil-docs | Live |  |
| security-cross-site | anvil-docs/external-resources/http-apis/creating-http-endpoints/security-cross-site.md | anvil-docs/external-resources/http-apis/creating-http-endpoints | anvil-docs | Live |  |
| creating-http-endpoints-_index | anvil-docs/external-resources/http-apis/creating-http-endpoints/_index.md | anvil-docs/external-resources/http-apis/creating-http-endpoints | anvil-docs | Live |  |
| making-http-requests-quickstart | anvil-docs/external-resources/http-apis/making-http-requests/quickstart.md | anvil-docs/external-resources/http-apis/making-http-requests | anvil-docs | Live |  |
| making-http-requests-_index | anvil-docs/external-resources/http-apis/making-http-requests/_index.md | anvil-docs/external-resources/http-apis/making-http-requests | anvil-docs | Live |  |
| calling-functions-remotely | anvil-docs/external-resources/uplink/calling-functions-remotely.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| uplink-data-tables | anvil-docs/external-resources/uplink/data-tables.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| uplink-dependencies | anvil-docs/external-resources/uplink/dependencies.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| pico | anvil-docs/external-resources/uplink/pico.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| uplink-quickstart | anvil-docs/external-resources/uplink/quickstart.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| setting-up | anvil-docs/external-resources/uplink/setting-up.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| uplink-security | anvil-docs/external-resources/uplink/uplink-security.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| uplink-_index | anvil-docs/external-resources/uplink/_index.md | anvil-docs/external-resources/uplink | anvil-docs | Live |  |
| build-first-app | anvil-docs/get-started/build-first-app.md | anvil-docs/get-started | anvil-docs | Live |  |
| coming-from-scripting | anvil-docs/get-started/coming-from-scripting.md | anvil-docs/get-started | anvil-docs | Live |  |
| coming-from-streamlit | anvil-docs/get-started/coming-from-streamlit.md | anvil-docs/get-started | anvil-docs | Live |  |
| help | anvil-docs/get-started/help.md | anvil-docs/get-started | anvil-docs | Live |  |
| how-does-it-work | anvil-docs/get-started/how-does-it-work.md | anvil-docs/get-started | anvil-docs | Live |  |
| get-started-_index | anvil-docs/get-started/_index.md | anvil-docs/get-started | anvil-docs | Live |  |
| collaborate-in-anvil | anvil-docs/how-to/collaborate-in-anvil.md | anvil-docs/how-to | anvil-docs | Live |  |
| creating-material-3-colour-scheme | anvil-docs/how-to/creating-material-3-colour-scheme.md | anvil-docs/how-to | anvil-docs | Live |  |
| crud-best-practice-guide | anvil-docs/how-to/crud-best-practice-guide.md | anvil-docs/how-to | anvil-docs | Live |  |
| custom-user-auth | anvil-docs/how-to/custom-user-auth.md | anvil-docs/how-to | anvil-docs | Live |  |
| customising-the-font | anvil-docs/how-to/customising-the-font.md | anvil-docs/how-to | anvil-docs | Live |  |
| dropdowns-data-tables | anvil-docs/how-to/dropdowns-data-tables.md | anvil-docs/how-to | anvil-docs | Live |  |
| embedding-webpage-iframe | anvil-docs/how-to/embedding-webpage-iframe.md | anvil-docs/how-to | anvil-docs | Live |  |
| expand-collapse | anvil-docs/how-to/expand-collapse.md | anvil-docs/how-to | anvil-docs | Live |  |
| how-to-external-database | anvil-docs/how-to/external-database.md | anvil-docs/how-to | anvil-docs | Live |  |
| git-configuration | anvil-docs/how-to/git-configuration.md | anvil-docs/how-to | anvil-docs | Live |  |
| plot | anvil-docs/how-to/plot.md | anvil-docs/how-to | anvil-docs | Live |  |
| plotly-express | anvil-docs/how-to/plotly-express.md | anvil-docs/how-to | anvil-docs | Live |  |
| porting-app-to-new-layouts | anvil-docs/how-to/porting-app-to-new-layouts.md | anvil-docs/how-to | anvil-docs | Live |  |
| prompting-best-practices | anvil-docs/how-to/prompting-best-practices.md | anvil-docs/how-to | anvil-docs | Live |  |
| serving-ui-from-http-routes | anvil-docs/how-to/serving-ui-from-http-routes.md | anvil-docs/how-to | anvil-docs | Live |  |
| upload-large-files-to-s3 | anvil-docs/how-to/upload-large-files-to-s3.md | anvil-docs/how-to | anvil-docs | Live |  |
| how-to-_index | anvil-docs/how-to/_index.md | anvil-docs/how-to | anvil-docs | Live |  |
| linux-ssh-key-setup | anvil-docs/how-to/app-server/linux-ssh-key-setup.md | anvil-docs/how-to/app-server | anvil-docs | Live |  |
| app-server-_index | anvil-docs/how-to/app-server/_index.md | anvil-docs/how-to/app-server | anvil-docs | Live |  |
| aws-lightsail-app-server-deployment | anvil-docs/how-to/app-server/cloud-deployment-guides/aws-lightsail-app-server-deployment.md | anvil-docs/how-to/app-server/cloud-deployment-guides | anvil-docs | Live |  |
| azure-app-server-deployment | anvil-docs/how-to/app-server/cloud-deployment-guides/azure-app-server-deployment.md | anvil-docs/how-to/app-server/cloud-deployment-guides | anvil-docs | Live |  |
| digitalocean-app-server-deployment | anvil-docs/how-to/app-server/cloud-deployment-guides/digitalocean-app-server-deployment.md | anvil-docs/how-to/app-server/cloud-deployment-guides | anvil-docs | Live |  |
| google-cloud-app-server-deployment | anvil-docs/how-to/app-server/cloud-deployment-guides/google-cloud-app-server-deployment.md | anvil-docs/how-to/app-server/cloud-deployment-guides | anvil-docs | Live |  |
| linode-app-server-deployment | anvil-docs/how-to/app-server/cloud-deployment-guides/linode-app-server-deployment.md | anvil-docs/how-to/app-server/cloud-deployment-guides | anvil-docs | Live |  |
| cloud-deployment-guides-_index | anvil-docs/how-to/app-server/cloud-deployment-guides/_index.md | anvil-docs/how-to/app-server/cloud-deployment-guides | anvil-docs | Live |  |
| integrations-_index | anvil-docs/integrations/_index.md | anvil-docs/integrations | anvil-docs | Live |  |
| linking-facebook-and-anvil | anvil-docs/integrations/facebook/linking-facebook-and-anvil.md | anvil-docs/integrations/facebook | anvil-docs | Live |  |
| facebook-quickstart | anvil-docs/integrations/facebook/quickstart.md | anvil-docs/integrations/facebook | anvil-docs | Live |  |
| facebook-_index | anvil-docs/integrations/facebook/_index.md | anvil-docs/integrations/facebook | anvil-docs | Live |  |
| authenticating-users | anvil-docs/integrations/google/authenticating-users.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| gmail | anvil-docs/integrations/google/gmail.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| google-drive | anvil-docs/integrations/google/google-drive.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| google-rest-apis | anvil-docs/integrations/google/google-rest-apis.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| linking-google-and-anvil | anvil-docs/integrations/google/linking-google-and-anvil.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| google-quickstart | anvil-docs/integrations/google/quickstart.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| google-_index | anvil-docs/integrations/google/_index.md | anvil-docs/integrations/google | anvil-docs | Live |  |
| accessing-microsoft-apis | anvil-docs/integrations/microsoft/accessing-microsoft-apis.md | anvil-docs/integrations/microsoft | anvil-docs | Live |  |
| linking-azure-and-anvil | anvil-docs/integrations/microsoft/linking-azure-and-anvil.md | anvil-docs/integrations/microsoft | anvil-docs | Live |  |
| microsoft-single-sign-on | anvil-docs/integrations/microsoft/microsoft-single-sign-on.md | anvil-docs/integrations/microsoft | anvil-docs | Live |  |
| microsoft-quickstart | anvil-docs/integrations/microsoft/quickstart.md | anvil-docs/integrations/microsoft | anvil-docs | Live |  |
| microsoft-_index | anvil-docs/integrations/microsoft/_index.md | anvil-docs/integrations/microsoft | anvil-docs | Live |  |
| configuration-options | anvil-docs/integrations/saml/configuration-options.md | anvil-docs/integrations/saml | anvil-docs | Live |  |
| saml-quickstart | anvil-docs/integrations/saml/quickstart.md | anvil-docs/integrations/saml | anvil-docs | Live |  |
| sharing-credentials-across-apps | anvil-docs/integrations/saml/sharing-credentials-across-apps.md | anvil-docs/integrations/saml | anvil-docs | Live |  |
| saml-_index | anvil-docs/integrations/saml/_index.md | anvil-docs/integrations/saml | anvil-docs | Live |  |
| payments-and-subscriptions | anvil-docs/integrations/stripe/payments-and-subscriptions.md | anvil-docs/integrations/stripe | anvil-docs | Live |  |
| stripe-quickstart | anvil-docs/integrations/stripe/quickstart.md | anvil-docs/integrations/stripe | anvil-docs | Live |  |
| raw-api-tokens | anvil-docs/integrations/stripe/raw-api-tokens.md | anvil-docs/integrations/stripe | anvil-docs | Live |  |
| stripe-_index | anvil-docs/integrations/stripe/_index.md | anvil-docs/integrations/stripe | anvil-docs | Live |  |
| buying | anvil-docs/integrations/x/buying.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| data-tables-in-tableau | anvil-docs/integrations/x/data-tables-in-tableau.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| publishing | anvil-docs/integrations/x/publishing.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| x-quickstart | anvil-docs/integrations/x/quickstart.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| tableau-extensions-api | anvil-docs/integrations/x/tableau-extensions-api.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| testing-in-tableau | anvil-docs/integrations/x/testing-in-tableau.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| trexjacket | anvil-docs/integrations/x/trexjacket.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| x-_index | anvil-docs/integrations/x/_index.md | anvil-docs/integrations/x | anvil-docs | Live |  |
| error-reporting | anvil-docs/other-concepts/error-reporting.md | anvil-docs/other-concepts | anvil-docs | Live |  |
| other-concepts-_index | anvil-docs/other-concepts/_index.md | anvil-docs/other-concepts | anvil-docs | Live |  |
| creating-pdf-files-quickstart | anvil-docs/other-concepts/creating-pdf-files/quickstart.md | anvil-docs/other-concepts/creating-pdf-files | anvil-docs | Live |  |
| creating-pdf-files-_index | anvil-docs/other-concepts/creating-pdf-files/_index.md | anvil-docs/other-concepts/creating-pdf-files | anvil-docs | Live |  |
| capabilities | anvil-docs/other-concepts/portable-classes/capabilities.md | anvil-docs/other-concepts/portable-classes | anvil-docs | Live |  |
| capability-scoped-cache-updates | anvil-docs/other-concepts/portable-classes/capability-scoped-cache-updates.md | anvil-docs/other-concepts/portable-classes | anvil-docs | Live |  |
| custom-serialisation | anvil-docs/other-concepts/portable-classes/custom-serialisation.md | anvil-docs/other-concepts/portable-classes | anvil-docs | Live |  |
| server-methods | anvil-docs/other-concepts/portable-classes/server-methods.md | anvil-docs/other-concepts/portable-classes | anvil-docs | Live |  |
| portable-classes-_index | anvil-docs/other-concepts/portable-classes/_index.md | anvil-docs/other-concepts/portable-classes | anvil-docs | Live |  |
| working-with-files-_index | anvil-docs/other-concepts/working-with-files/_index.md | anvil-docs/other-concepts/working-with-files | anvil-docs | Live |  |
| files-on-disk | anvil-docs/other-concepts/working-with-files/media/files-on-disk.md | anvil-docs/other-concepts/working-with-files/media | anvil-docs | Live |  |
| image-manipulation | anvil-docs/other-concepts/working-with-files/media/image-manipulation.md | anvil-docs/other-concepts/working-with-files/media | anvil-docs | Live |  |
| media-quickstart | anvil-docs/other-concepts/working-with-files/media/quickstart.md | anvil-docs/other-concepts/working-with-files/media | anvil-docs | Live |  |
| media-_index | anvil-docs/other-concepts/working-with-files/media/_index.md | anvil-docs/other-concepts/working-with-files/media | anvil-docs | Live |  |
| faq | anvil-docs/overview/faq.md | anvil-docs/overview | anvil-docs | Live |  |
| quickstarts | anvil-docs/overview/quickstarts.md | anvil-docs/overview | anvil-docs | Live |  |
| overview-_index | anvil-docs/overview/_index.md | anvil-docs/overview | anvil-docs | Live |  |
| account-management | anvil-docs/plans-and-accounts/account-management.md | anvil-docs/plans-and-accounts | anvil-docs | Live |  |
| choosing-the-right-plan | anvil-docs/plans-and-accounts/choosing-the-right-plan.md | anvil-docs/plans-and-accounts | anvil-docs | Live |  |
| enterprise | anvil-docs/plans-and-accounts/enterprise.md | anvil-docs/plans-and-accounts | anvil-docs | Live |  |
| free-vs-paid | anvil-docs/plans-and-accounts/free-vs-paid.md | anvil-docs/plans-and-accounts | anvil-docs | Live |  |
| plans-and-accounts-_index | anvil-docs/plans-and-accounts/_index.md | anvil-docs/plans-and-accounts | anvil-docs | Live |  |
| call-context | anvil-docs/server/call-context.md | anvil-docs/server | anvil-docs | Live |  |
| offline-apps | anvil-docs/server/offline-apps.md | anvil-docs/server | anvil-docs | Live |  |
| scheduled-tasks | anvil-docs/server/scheduled-tasks.md | anvil-docs/server | anvil-docs | Live |  |
| scripts | anvil-docs/server/scripts.md | anvil-docs/server | anvil-docs | Live |  |
| sessions-and-cookies | anvil-docs/server/sessions-and-cookies.md | anvil-docs/server | anvil-docs | Live |  |
| server-_index | anvil-docs/server/_index.md | anvil-docs/server | anvil-docs | Live |  |
| communicating-back | anvil-docs/server/background-tasks/communicating-back.md | anvil-docs/server/background-tasks | anvil-docs | Live |  |
| defining-and-running | anvil-docs/server/background-tasks/defining-and-running.md | anvil-docs/server/background-tasks | anvil-docs | Live |  |
| background-tasks-quickstart | anvil-docs/server/background-tasks/quickstart.md | anvil-docs/server/background-tasks | anvil-docs | Live |  |
| background-tasks-_index | anvil-docs/server/background-tasks/_index.md | anvil-docs/server/background-tasks | anvil-docs | Live |  |
| packages | anvil-docs/server/custom-packages/packages.md | anvil-docs/server/custom-packages | anvil-docs | Live |  |
| custom-packages-_index | anvil-docs/server/custom-packages/_index.md | anvil-docs/server/custom-packages | anvil-docs | Live |  |
| attachments | anvil-docs/server/email/attachments.md | anvil-docs/server/email | anvil-docs | Live |  |
| email-quickstart | anvil-docs/server/email/quickstart.md | anvil-docs/server/email | anvil-docs | Live |  |
| security-and-dkim | anvil-docs/server/email/security-and-dkim.md | anvil-docs/server/email | anvil-docs | Live |  |
| sending-and-receiving | anvil-docs/server/email/sending-and-receiving.md | anvil-docs/server/email | anvil-docs | Live |  |
| email-_index | anvil-docs/server/email/_index.md | anvil-docs/server/email | anvil-docs | Live |  |
| server-modules-quickstart | anvil-docs/server/server-modules/quickstart.md | anvil-docs/server/server-modules | anvil-docs | Live |  |
| server-modules-_index | anvil-docs/server/server-modules/_index.md | anvil-docs/server/server-modules | anvil-docs | Live |  |
| tests-README | anvil-docs/tests/README.md | anvil-docs/tests | anvil-docs | Live |  |
| SmokeTest-README | anvil-docs/tests/apps/SmokeTest/README.md | anvil-docs/tests/apps/SmokeTest | anvil-docs | Live |  |
| authentication-choices | anvil-docs/users/authentication-choices.md | anvil-docs/users | anvil-docs | Live |  |
| configuring-emails | anvil-docs/users/configuring-emails.md | anvil-docs/users | anvil-docs | Live |  |
| logging-in-using-code | anvil-docs/users/logging-in-using-code.md | anvil-docs/users | anvil-docs | Live |  |
| permissions | anvil-docs/users/permissions.md | anvil-docs/users | anvil-docs | Live |  |
| presenting-a-login-form | anvil-docs/users/presenting-a-login-form.md | anvil-docs/users | anvil-docs | Live |  |
| quickstart-login | anvil-docs/users/quickstart-login.md | anvil-docs/users | anvil-docs | Live |  |
| quickstart-permissions | anvil-docs/users/quickstart-permissions.md | anvil-docs/users | anvil-docs | Live |  |
| the-users-table | anvil-docs/users/the-users-table.md | anvil-docs/users | anvil-docs | Live |  |
| two-factor-authentication | anvil-docs/users/two-factor-authentication.md | anvil-docs/users | anvil-docs | Live |  |
| users-_index | anvil-docs/users/_index.md | anvil-docs/users | anvil-docs | Live |  |
| commands | anvil-docs/using-another-ide/commands.md | anvil-docs/using-another-ide | anvil-docs | Live |  |
| creating-and-editing-apps | anvil-docs/using-another-ide/creating-and-editing-apps.md | anvil-docs/using-another-ide | anvil-docs | Live |  |
| using-another-ide-quickstart | anvil-docs/using-another-ide/quickstart.md | anvil-docs/using-another-ide | anvil-docs | Live |  |
| using-another-ide-_index | anvil-docs/using-another-ide/_index.md | anvil-docs/using-another-ide | anvil-docs | Live |  |
| dealing-with-timezones | anvil-docs/workflows/dealing-with-timezones.md | anvil-docs/workflows | anvil-docs | Live |  |
| workflows-_index | anvil-docs/workflows/_index.md | anvil-docs/workflows | anvil-docs | Live |  |
| how-to-import-things | anvil-docs/workflows/app-architecture/how-to-import-things.md | anvil-docs/workflows/app-architecture | anvil-docs | Live |  |
| python-directory-structure | anvil-docs/workflows/app-architecture/python-directory-structure.md | anvil-docs/workflows/app-architecture | anvil-docs | Live |  |
| structuring-your-app | anvil-docs/workflows/app-architecture/structuring-your-app.md | anvil-docs/workflows/app-architecture | anvil-docs | Live |  |
| app-architecture-_index | anvil-docs/workflows/app-architecture/_index.md | anvil-docs/workflows/app-architecture | anvil-docs | Live |  |
| additional-debugging-tools | anvil-docs/workflows/debugger/additional-debugging-tools.md | anvil-docs/workflows/debugger | anvil-docs | Live |  |
| interactive-debugger | anvil-docs/workflows/debugger/interactive-debugger.md | anvil-docs/workflows/debugger | anvil-docs | Live |  |
| debugger-_index | anvil-docs/workflows/debugger/_index.md | anvil-docs/workflows/debugger | anvil-docs | Live |  |
| encrypting-secret-data | anvil-docs/workflows/security/encrypting-secret-data.md | anvil-docs/workflows/security | anvil-docs | Live |  |
| security-_index | anvil-docs/workflows/security/_index.md | anvil-docs/workflows/security | anvil-docs | Live |  |
| collaborators | anvil-docs/workflows/version-control/collaborators.md | anvil-docs/workflows/version-control | anvil-docs | Live |  |
| version-control-quickstart | anvil-docs/workflows/version-control/quickstart.md | anvil-docs/workflows/version-control | anvil-docs | Live |  |
| version-control-anvil | anvil-docs/workflows/version-control/version-control-anvil.md | anvil-docs/workflows/version-control | anvil-docs | Live |  |
| what-is-version-control | anvil-docs/workflows/version-control/what-is-version-control.md | anvil-docs/workflows/version-control | anvil-docs | Live |  |
| workflows | anvil-docs/workflows/version-control/workflows.md | anvil-docs/workflows/version-control | anvil-docs | Live |  |
| version-control-_index | anvil-docs/workflows/version-control/_index.md | anvil-docs/workflows/version-control | anvil-docs | Live |  |
| direct-checkout | anvil-docs/workflows/version-control/git/direct-checkout.md | anvil-docs/workflows/version-control/git | anvil-docs | Live |  |
| git-quickstart | anvil-docs/workflows/version-control/git/quickstart.md | anvil-docs/workflows/version-control/git | anvil-docs | Live |  |
| secrets-across-repos | anvil-docs/workflows/version-control/git/secrets-across-repos.md | anvil-docs/workflows/version-control/git | anvil-docs | Live |  |
| git-_index | anvil-docs/workflows/version-control/git/_index.md | anvil-docs/workflows/version-control/git | anvil-docs | Live |  |
| plg-readme | README.md | . | readme | Live | 2026-09-11 | 2026-09-11 | | registered by align-docs re-validation run |

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
