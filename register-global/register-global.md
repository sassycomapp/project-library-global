---
title: "register-global"
doc-id: "register-global"
---
# Register — project-library-global

One row per real corpus document. `doc-id` is the filename without its `.md`
extension. No sequence-number identifier is used. Regenerated from the live file
tree on 2026-08-27 (post rename + de-index). Corrected 2026-09-01: `rules-cupcake-global`
(19 documents) and `security-global` (54 documents) were present on disk but missing
from this register entirely — added below.

| doc-id | title | state | superseded-by | notes |
| --- | --- | --- | --- | --- |
| adr-anvil-extras-exclusion | adr-anvil-extras-exclusion.md | Live |  |  |
| adr-brevo-replaces-zoho-email | adr-brevo-replaces-zoho-email.md | Live |  |  |
| adr-client-data-management-rights-and-mybizz-retention-boundary | adr-client-data-management-rights-and-mybizz-retention-boundary.md | Live |  |  |
| adr-client-instance-architecture | adr-client-instance-architecture.md | Live |  | Defines the dependency-based architecture. Confirmed by live testing (Test A: app_tables resolution, Test B: forms from dependency). Foundation for all data access patterns. |
| adr-client-instance-readme-five-app-system | adr-client-instance-readme-five-app-system.md | Live |  | Every client instance must contain a standardized README documenting the five-app architecture and the constraint against adding forms or modules directly to client instances. |
| adr-dark-mode-v1 | adr-dark-mode-v1.md | Live |  | Dark mode incorporated into V1. No longer deferred to V2. All screens require `@media (prefers-color-scheme: dark)` blocks. |
| adr-dependency-based-not-multi-tenant | adr-dependency-based-not-multi-tenant.md | Live |  | Definitive statement that Mybizz CS is a dependency-based SaaS platform, not a multi-tenant application. Prohibits tenant discriminator columns and tenant-filtered queries. |
| adr-dependency-update-model | adr-dependency-update-model.md | Live |  | Four-app update flow (mb-3-cs → master_template → client instances). Branch propagation confirmed. |
| adr-filename-and-frontmatter-numbering-policy | adr-filename-and-frontmatter-numbering-policy.md | Live |  | Files are not numbered anywhere in the scaffold (filenames or front matter); identity is the descriptive filename; references cite by filename. Exceptions: stepwise (inherently ordinal steps), quarantine/retired/archived historical material. |
| adr-design-rules | adr-design-rules.md | Live |  |  |
| adr-dev-tooling-source-repos-must-be-github-backed | adr-dev-tooling-source-repos-must-be-github-backed.md | Live |  | Grew out of a 2026-08-05 `gbrain doctor` root-cause investigation that found two PDLF-ecosystem sources (`pdlf`, `template-project-library`) as local-only working trees with no GitHub remote — the actual cause of a persistent `sync_freshness` failure and an unmanaged data-loss risk. Requires every dev-tooling source to be GitHub-backed: normal private repos for live tools, GitHub template repos for copy-to-start scaffolds. |
| adr-free-trial-abandoned | adr-free-trial-abandoned.md | Live |  |  |
| adr-frontmatter-exemption-transient-files | adr-frontmatter-exemption-transient-files.md | Live |  |  |
| adr-htmltemplate-use | adr-htmltemplate-use.md | Live |  | `HTMLTemplate` is banned. All current use cases have native M3 alternatives. Wireframes using it require reworking. |
| adr-instructions-md-per-folder | adr-instructions-md-per-folder.md | Live |  |  |
| adr-lead-capture-simultaneous-creation | adr-lead-capture-simultaneous-creation.md | Live |  |  |
| adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture | adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md | Live |  |  |
| adr-material-3-theme-component-scope | adr-material-3-theme-component-scope.md | Live |  |  |
| adr-mybizz-management-visibility | adr-mybizz-management-visibility.md | Live |  |  |
| adr-navigation-lambda-link-open-form | adr-navigation-lambda-link-open-form.md | Live |  |  |
| adr-observability-architecture | adr-observability-architecture.md | Live |  |  |
| adr-onboarding-data-schema-alignment | adr-onboarding-data-schema-alignment.md | Live |  |  |
| adr-onboarding-finality | adr-onboarding-finality.md | Live |  | Created 2026-05-31, updated 2026-06-01. Onboarding is resumable and revisitable. Owners may change any credential at any time. Mybizz_management maintains an append-only amendment log with three data tables. Reversed and fully replaced the original `onboarding-finality` (deleted). |
| adr-onboarding-resumability | adr-onboarding-resumability.md | Live |  |  |
| adr-onboarding-vs-settings-boundary | adr-onboarding-vs-settings-boundary.md | Live |  |  |
| adr-openai-embedding-provider | adr-openai-embedding-provider.md | Live |  |  |
| adr-payment-gateway-configuration-is-a-settings-function-and-is-rbac-governed | adr-payment-gateway-configuration-is-a-settings-function-and-is-rbac-governed.md | Live |  |  |
| adr-payment-gateway-mutability | adr-payment-gateway-mutability.md | Live |  |  |
| adr-payment-security-boundary-vault | adr-payment-security-boundary-vault.md | Live |  |  |
| adr-responsive-behaviour-mechanism | adr-responsive-behaviour-mechanism.md | Live |  | Resolves contradicting breakpoint models in design-direction.md. Responsive behaviour uses `wrap_on` per-container, not CSS breakpoint tables. Nav collapse is automatic and separate. |
| adr-role-property-assignment-mechanism | adr-role-property-assignment-mechanism.md | Live |  | Superseded. Original decision: set `role` via Designer Properties Panel. Reversed by project-wide property-setting rule: if a property can be set programmatically, it must be set programmatically. Current decision: set `role` in code (`self.component.role = "role-name"`). |
| adr-single-contacts-table | adr-single-contacts-table.md | Live |  |  |
| adr-system-currency-selection-and-immutability | adr-system-currency-selection-and-immutability.md | Live |  | Consolidated from original ADR-13 and ADR-16. Covers system currency, display currency, immutability enforcement, and currency conversion strategy. |
| adr-tiers-model | adr-tiers-model.md | Live |  |  |
| adr-timezone-utc-storage-display-conversion | adr-timezone-utc-storage-display-conversion.md | Live |  |  |
| docstd-business-requirements-document | docstd-business-requirements-document.md | Live |  |  |
| docstd-globals-contract | docstd-globals-contract.md | Live |  |  |
| docstd-product-requirements-document | docstd-product-requirements-document.md | Live |  |  |
| docstd-software-requirements-specification | docstd-software-requirements-specification.md | Live |  |  |
| gui-anvil-deprecated-guide | gui-anvil-deprecated-guide.md | Live |  |  |
| gui-Anvil-Debugging-Guide | gui-Anvil-Debugging-Guide.md | Live |  |  |
| pol-anvil-first-development | pol-anvil-first-development.md | Live |  |  |
| pol-documentation-and-decisions | pol-documentation-and-decisions.md | Live |  |  |
| pol-security-and-data-governance | pol-security-and-data-governance.md | Live |  |  |
| pol-testing-and-quality | pol-testing-and-quality.md | Live |  |  |
| spec-anvil-platform-standards | spec-anvil-platform-standards.md | Live |  |  |
| spec-anvil-spec-table | spec-anvil-spec-table.md | Live |  |  |
| spec-api-specification | spec-api-specification.md | Live |  |  |
| spec-client-activation-runbook | spec-client-activation-runbook.md | Live |  |  |
| spec-component-properties | spec-component-properties.md | Live |  |  |
| spec-deployment | spec-deployment.md | Live |  |  |
| spec-five-app-architecture-model | spec-five-app-architecture-model.md | Live |  |  |
| spec-integration | spec-integration.md | Live |  |  |
| spec-m3-design-standards | spec-m3-design-standards.md | Live |  |  |
| spec-m3_component_mapping | spec-m3_component_mapping.md | Live |  |  |
| spec-material-3-theme | spec-material-3-theme.md | Live |  |  |
| spec-nomenclature | spec-nomenclature.md | Live |  |  |
| spec-observability | spec-observability.md | Live |  |  |
| spec-onboarding-implementation-plan | spec-onboarding-implementation-plan.md | Live |  |  |
| spec-regulatory-compliance-baseline | spec-regulatory-compliance-baseline.md | Live |  |  |
| spec-screen-and-wireframe-production-standards | spec-screen-and-wireframe-production-standards.md | Live |  |  |
| spec-screen-production-standard | spec-screen-production-standard.md | Live |  |  |
| spec-security-architecture | spec-security-architecture.md | Live |  |  |
| spec-security | spec-security.md | Live |  |  |
| spec-testing-methodology-standards | spec-testing-methodology-standards.md | Live |  |  |
| spec-testing | spec-testing.md | Live |  |  |
| spec-ui-standards | spec-ui-standards.md | Live |  |  |
| spec-vault-system | spec-vault-system.md | Live |  |  |
| sop-deployment-procedures | sop-deployment-procedures.md | Live |  |  |
| sop-offboarding | sop-offboarding.md | Live |  |  |
| sop-vault-totp-recovery | sop-vault-totp-recovery.md | Live |  |  |
| sop-agent-readiness-framework | sop-agent-readiness-framework.md | Live |  |  |
| sop-set3-anvil_cop_agent_readiness | sop-set3-anvil_cop_agent_readiness.md | Live |  |  |
| tmp-authoritative-schema | tmp-authoritative-schema.md | — |  |  |
| tmp-chklist-anvil-app-testing | tmp-chklist-anvil-app-testing.md | — |  |  |
| tmp-chklist-screen | tmp-chklist-screen.md | — |  |  |
| tmp-chklist-wireframe | tmp-chklist-wireframe.md | — |  |  |
| tmp-custom-component-requirements-matrix | tmp-custom-component-requirements-matrix.md | — |  |  |
| cup-block-anvil-yaml-writes | cup-block-anvil-yaml-writes.md | Live |  |  |
| cup-block-task-tool | cup-block-task-tool.md | Live |  |  |
| no_access_to_secrets_unless_explicitly_required | no_access_to_secrets_unless_explicitly_required.md | Live |  |  |
| no_autonomous_commits_pushes_merges_releases_or_deployments | no_autonomous_commits_pushes_merges_releases_or_deployments.md | Live |  |  |
| no_autonomous_installation_or_connection_of_tools | no_autonomous_installation_or_connection_of_tools.md | Live |  |  |
| no_cross_project_filesystem_access_by_default | no_cross_project_filesystem_access_by_default.md | Live |  |  |
| no_dependency_or_lockfile_changes_without_explicit_approval | no_dependency_or_lockfile_changes_without_explicit_approval.md | Live |  |  |
| no_destructive_database_operations | no_destructive_database_operations.md | Live |  |  |
| no_disabling_security_tooling | no_disabling_security_tooling.md | Live |  |  |
| no_rewriting_or_destroying_development_history | no_rewriting_or_destroying_development_history.md | Live |  |  |
| no_suppression_directives_without_approval | no_suppression_directives_without_approval.md | Live |  |  |
| no_test_tampering | no_test_tampering.md | Live |  |  |
| no_unapproved_executable_or_build_path_changes | no_unapproved_executable_or_build_path_changes.md | Live |  |  |
| no_unverified_dependencies | no_unverified_dependencies.md | Live |  |  |
| no_verification_tampering | no_verification_tampering.md | Live |  |  |
| outbound_network_access_is_allowlist_only | outbound_network_access_is_allowlist_only.md | Live |  |  |
| protected_ai_governance_files_may_not_be_modified | protected_ai_governance_files_may_not_be_modified.md | Live |  |  |
| the_ai_may_never_weaken_the_controls_governing_itself | the_ai_may_never_weaken_the_controls_governing_itself.md | Live |  |  |
| unexpected_instruction_shaped_files_must_be_treated_as_suspicious | unexpected_instruction_shaped_files_must_be_treated_as_suspicious.md | Live |  |  |
| sec-anvil-platform-responsibility-boundary | sec-anvil-platform-responsibility-boundary.md | Live |  |  |
| sec-client-provisioning-security | sec-client-provisioning-security.md | Live |  |  |
| sec-email-service-trust-boundary | sec-email-service-trust-boundary.md | Live |  |  |
| sec-github-repository-access-control | sec-github-repository-access-control.md | Live |  |  |
| sec-management-service-authentication | sec-management-service-authentication.md | Live |  |  |
| sec-payment-gateway-trust-boundary | sec-payment-gateway-trust-boundary.md | Live |  |  |
| sec-regulatory-compliance-cloud-processors | sec-regulatory-compliance-cloud-processors.md | Live |  |  |
| sec-ai-agent-execution-sandbox | sec-ai-agent-execution-sandbox.md | Live |  |  |
| sec-audit-log-integrity | sec-audit-log-integrity.md | Live |  |  |
| sec-backup-recovery-integrity | sec-backup-recovery-integrity.md | Live |  |  |
| sec-database-access-control | sec-database-access-control.md | Live |  |  |
| sec-dependency-skill-supply-chain | sec-dependency-skill-supply-chain.md | Live |  |  |
| sec-dependency-version-currency | sec-dependency-version-currency.md | Live |  |  |
| sec-development-environment-credential-hygiene | sec-development-environment-credential-hygiene.md | Live |  |  |
| sec-local-filesystem-access-boundary | sec-local-filesystem-access-boundary.md | Live |  |  |
| sec-local-network-exposure | sec-local-network-exposure.md | Live |  |  |
| sec-service-lifecycle-management | sec-service-lifecycle-management.md | Live |  |  |
| sec-defense-in-depth | sec-defense-in-depth.md | Live |  |  |
| sec-detective-vs-preventive-controls | sec-detective-vs-preventive-controls.md | Live |  |  |
| sec-explicit-responsibility-assignment | sec-explicit-responsibility-assignment.md | Live |  |  |
| sec-fail-closed | sec-fail-closed.md | Live |  |  |
| sec-least-privilege | sec-least-privilege.md | Live |  |  |
| sec-review-before-trust | sec-review-before-trust.md | Live |  |  |
| sec-server-side-authority | sec-server-side-authority.md | Live |  |  |
| sec-simplicity-as-security-property | sec-simplicity-as-security-property.md | Live |  |  |
| sec-verify-dont-trust-claims | sec-verify-dont-trust-claims.md | Live |  |  |
| sec-requirements-architecture-review | sec-requirements-architecture-review.md | Live |  |  |
| sec-requirements-data-table-creation | sec-requirements-data-table-creation.md | Live |  |  |
| sec-requirements-pre-merge-master-template | sec-requirements-pre-merge-master-template.md | Live |  |  |
| sec-requirements-release-readiness | sec-requirements-release-readiness.md | Live |  |  |
| sec-requirements-server-function | sec-requirements-server-function.md | Live |  |  |
| sec-requirements-third-party-integration | sec-requirements-third-party-integration.md | Live |  |  |
| sec-ai-agent-secret-visibility | sec-ai-agent-secret-visibility.md | Live |  |  |
| sec-development-tooling-credentials | sec-development-tooling-credentials.md | Live |  |  |
| sec-master-encryption-key-protection | sec-master-encryption-key-protection.md | Live |  |  |
| sec-secret-access-audit | sec-secret-access-audit.md | Live |  |  |
| sec-secret-exposure-response | sec-secret-exposure-response.md | Live |  |  |
| sec-secret-rotation-policy | sec-secret-rotation-policy.md | Live |  |  |
| sec-testing-adversarial-verification | sec-testing-adversarial-verification.md | Live |  |  |
| sec-testing-coverage-minimum | sec-testing-coverage-minimum.md | Live |  |  |
| sec-testing-independent-review | sec-testing-independent-review.md | Live |  |  |
| sec-testing-live-verification-standard | sec-testing-live-verification-standard.md | Live |  |  |
| sec-testing-regression-prevention | sec-testing-regression-prevention.md | Live |  |  |
| sec-ai-agent-introduced-vulnerabilities | sec-ai-agent-introduced-vulnerabilities.md | Live |  |  |
| sec-authentication-session | sec-authentication-session.md | Live |  |  |
| sec-broken-access-control-within-instance | sec-broken-access-control-within-instance.md | Live |  |  |
| sec-business-logic-race-conditions | sec-business-logic-race-conditions.md | Live |  |  |
| sec-data-exfiltration-bulk-export | sec-data-exfiltration-bulk-export.md | Live |  |  |
| sec-denial-of-service-resource-exhaustion | sec-denial-of-service-resource-exhaustion.md | Live |  |  |
| sec-injection-unsafe-input | sec-injection-unsafe-input.md | Live |  |  |
| sec-insecure-direct-object-reference | sec-insecure-direct-object-reference.md | Live |  |  |
| sec-multi-tenant-assumption-leakage | sec-multi-tenant-assumption-leakage.md | Live |  |  |
| sec-payment-manipulation | sec-payment-manipulation.md | Live |  |  |
| sec-privilege-escalation | sec-privilege-escalation.md | Live |  |  |
| anvil-docs-config | anvil-docs-config.md | Live |  |  |
| anvil-docs-explainer | anvil-docs-explainer.md | Live |  |  |
| anvil-docs-reference | anvil-docs-reference.md | Live |  |  |
| anvil-docs-README | README.md | Live |  |  |
| site-map | site-map.md | Live |  |  |
| agent-chat-window | agent-chat-window.md | Live |  |  |
| connecting-your-account | connecting-your-account.md | Live |  |  |
| ai-_index | _index.md | Live |  |  |
| anvil.email | anvil.email.md | Live |  |  |
| anvil.email.message | anvil.email.message.md | Live |  |  |
| anvil.facebook.auth | anvil.facebook.auth.md | Live |  |  |
| anvil.files | anvil.files.md | Live |  |  |
| anvil.google.auth | anvil.google.auth.md | Live |  |  |
| anvil.google.drive | anvil.google.drive.md | Live |  |  |
| anvil.google.mail | anvil.google.mail.md | Live |  |  |
| anvil.google.sheets | anvil.google.sheets.md | Live |  |  |
| anvil.googlemap.data | anvil.googlemap.data.md | Live |  |  |
| anvil.googlemap | anvil.googlemap.md | Live |  |  |
| anvil.http | anvil.http.md | Live |  |  |
| anvil.image | anvil.image.md | Live |  |  |
| anvil.js | anvil.js.md | Live |  |  |
| anvil | anvil.md | Live |  |  |
| anvil.media | anvil.media.md | Live |  |  |
| anvil.microsoft.auth | anvil.microsoft.auth.md | Live |  |  |
| anvil.mpl_util | anvil.mpl_util.md | Live |  |  |
| anvil.pdf | anvil.pdf.md | Live |  |  |
| anvil.pico-micro-uplink | anvil.pico-micro-uplink.md | Live |  |  |
| anvil.plotly_templates | anvil.plotly_templates.md | Live |  |  |
| anvil.saml.auth | anvil.saml.auth.md | Live |  |  |
| anvil.script | anvil.script.md | Live |  |  |
| anvil.secrets | anvil.secrets.md | Live |  |  |
| anvil.server-uplink | anvil.server-uplink.md | Live |  |  |
| anvil.server | anvil.server.md | Live |  |  |
| anvil.stripe | anvil.stripe.md | Live |  |  |
| anvil.tables | anvil.tables.md | Live |  |  |
| anvil.tables.query | anvil.tables.query.md | Live |  |  |
| anvil.tz | anvil.tz.md | Live |  |  |
| anvil.users | anvil.users.md | Live |  |  |
| anvil.users.mfa | anvil.users.mfa.md | Live |  |  |
| segment.client | segment.client.md | Live |  |  |
| stripe.checkout | stripe.checkout.md | Live |  |  |
| api-_index | _index.md | Live |  |  |
| app-structure | app-structure.md | Live |  |  |
| client-quickstart | quickstart.md | Live |  |  |
| client-_index | _index.md | Live |  |  |
| adding-html-elements | adding-html-elements.md | Live |  |  |
| alerts-and-notifications | alerts-and-notifications.md | Live |  |  |
| adding-ui-elements-containers | containers.md | Live |  |  |
| loading-indicator | loading-indicator.md | Live |  |  |
| adding-ui-elements-_index | _index.md | Live |  |  |
| modules | modules.md | Live |  |  |
| the-python-environment | the-python-environment.md | Live |  |  |
| client-code-_index | _index.md | Live |  |  |
| data-bindings | data-bindings.md | Live |  |  |
| component-properties-_index | _index.md | Live |  |  |
| assets | assets.md | Live |  |  |
| colour-schemes | colour-schemes.md | Live |  |  |
| customisation-_index | _index.md | Live |  |  |
| html-components | html-components.md | Live |  |  |
| custom-components-_index | _index.md | Live |  |  |
| accessing-javascript | accessing-javascript.md | Live |  |  |
| html-forms | html-forms.md | Live |  |  |
| javascript-quickstart | quickstart.md | Live |  |  |
| javascript-_index | _index.md | Live |  |  |
| loading_indicator | loading_indicator.md | Live |  |  |
| roles | roles.md | Live |  |  |
| using-css-_index | _index.md | Live |  |  |
| service-worker-whiteboard | service-worker-whiteboard.md | Live |  |  |
| component-lifecycle | component-lifecycle.md | Live |  |  |
| events-_index | _index.md | Live |  |  |
| form-templates | form-templates.md | Live |  |  |
| forms-as-components | forms-as-components.md | Live |  |  |
| forms-as-html | forms-as-html.md | Live |  |  |
| forms-as-python-classes | forms-as-python-classes.md | Live |  |  |
| forms-in-the-editor | forms-in-the-editor.md | Live |  |  |
| forms-_index | _index.md | Live |  |  |
| html-layouts | html-layouts.md | Live |  |  |
| layouts-api | layouts-api.md | Live |  |  |
| layouts-quickstart | quickstart.md | Live |  |  |
| layouts-_index | _index.md | Live |  |  |
| navigation-_index | _index.md | Live |  |  |
| caching | caching.md | Live |  |  |
| navigation | navigation.md | Live |  |  |
| parameters | parameters.md | Live |  |  |
| routing-quickstart | quickstart.md | Live |  |  |
| router | router.md | Live |  |  |
| routing-_index | _index.md | Live |  |  |
| components-_index | _index.md | Live |  |  |
| components | components.md | Live |  |  |
| layouts | layouts.md | Live |  |  |
| material-3-_index | _index.md | Live |  |  |
| basic | basic.md | Live |  |  |
| canvas | canvas.md | Live |  |  |
| standard-components-containers | containers.md | Live |  |  |
| data-grids | data-grids.md | Live |  |  |
| html-component | html-component.md | Live |  |  |
| maps | maps.md | Live |  |  |
| plots | plots.md | Live |  |  |
| repeating-panel | repeating-panel.md | Live |  |  |
| standard-components-_index | _index.md | Live |  |  |
| buffering | buffering.md | Live |  |  |
| csv-and-excel | csv-and-excel.md | Live |  |  |
| data-security | data-security.md | Live |  |  |
| data-tables-in-code | data-tables-in-code.md | Live |  |  |
| faster-storage | faster-storage.md | Live |  |  |
| indexes | indexes.md | Live |  |  |
| legacy-tables | legacy-tables.md | Live |  |  |
| links-between-tables | links-between-tables.md | Live |  |  |
| multiple-databases | multiple-databases.md | Live |  |  |
| data-tables-quickstart | quickstart.md | Live |  |  |
| sql-access | sql-access.md | Live |  |  |
| transactions | transactions.md | Live |  |  |
| data-tables-_index | _index.md | Live |  |  |
| server_funcs | server_funcs.md | Live |  |  |
| types | types.md | Live |  |  |
| data-files-quickstart | quickstart.md | Live |  |  |
| data-files-_index | _index.md | Live |  |  |
| client-writable | client-writable.md | Live |  |  |
| creating | creating.md | Live |  |  |
| patterns | patterns.md | Live |  |  |
| validation | validation.md | Live |  |  |
| model-classes-_index | _index.md | Live |  |  |
| anvil-debugging-guide | anvil-debugging-guide.md | Live |  |  |
| custom-domains | custom-domains.md | Live |  |  |
| deployment-dependencies | dependencies.md | Live |  |  |
| embedding-your-app | embedding-your-app.md | Live |  |  |
| hosting-options | hosting-options.md | Live |  |  |
| on-site | on-site.md | Live |  |  |
| deployment-quickstart | quickstart.md | Live |  |  |
| runtime-repo-dependencies | runtime-repo-dependencies.md | Live |  |  |
| deployment-_index | _index.md | Live |  |  |
| environments-and-code | environments-and-code.md | Live |  |  |
| environments-_index | _index.md | Live |  |  |
| form-editor | form-editor.md | Live |  |  |
| keyboard-shortcuts | keyboard-shortcuts.md | Live |  |  |
| look-and-feel | look-and-feel.md | Live |  |  |
| editor-_index | _index.md | Live |  |  |
| profiling-and-tracing | profiling-and-tracing.md | Live |  |  |
| app-logs-_index | _index.md | Live |  |  |
| cloning-and-collaboration | cloning-and-collaboration.md | Live |  |  |
| app-settings-data-tables | data-tables.md | Live |  |  |
| titles-and-logos | titles-and-logos.md | Live |  |  |
| app-settings-_index | _index.md | Live |  |  |
| managed-enterprise | managed-enterprise.md | Live |  |  |
| trials | trials.md | Live |  |  |
| enterprise-_index | _index.md | Live |  |  |
| custom | custom.md | Live |  |  |
| docker | docker.md | Live |  |  |
| enterprise-deployment-index | _index.md | Retired |  |  |
| aks | aks.md | Live |  |  |
| configuration | configuration.md | Live |  |  |
| eks | eks.md | Live |  |  |
| gke | gke.md | Live |  |  |
| installation | installation.md | Live |  |  |
| k3s | k3s.md | Live |  |  |
| k8s-prerequisites | k8s-prerequisites.md | Live |  |  |
| oke | oke.md | Live |  |  |
| openshift | openshift.md | Live |  |  |
| kubernetes-_index | _index.md | Live |  |  |
| changelog | changelog.md | Live |  |  |
| cluster | cluster.md | Live |  |  |
| restore | restore.md | Live |  |  |
| operator-_index | _index.md | Live |  |  |
| github | github.md | Live |  |  |
| google | google.md | Live |  |  |
| microsoft | microsoft.md | Live |  |  |
| tls-certificates | tls-certificates.md | Live |  |  |
| prerequisites-_index | _index.md | Live |  |  |
| external-resources-external-database | external-database.md | Live |  |  |
| external-resources-_index | _index.md | Live |  |  |
| http-apis-_index | _index.md | Live |  |  |
| authentication | authentication.md | Live |  |  |
| creating-http-endpoints-quickstart | quickstart.md | Live |  |  |
| security-cross-site | security-cross-site.md | Live |  |  |
| creating-http-endpoints-_index | _index.md | Live |  |  |
| making-http-requests-quickstart | quickstart.md | Live |  |  |
| making-http-requests-_index | _index.md | Live |  |  |
| calling-functions-remotely | calling-functions-remotely.md | Live |  |  |
| uplink-data-tables | data-tables.md | Live |  |  |
| uplink-dependencies | dependencies.md | Live |  |  |
| pico | pico.md | Live |  |  |
| uplink-quickstart | quickstart.md | Live |  |  |
| setting-up | setting-up.md | Live |  |  |
| uplink-security | uplink-security.md | Live |  |  |
| uplink-_index | _index.md | Live |  |  |
| build-first-app | build-first-app.md | Live |  |  |
| coming-from-scripting | coming-from-scripting.md | Live |  |  |
| coming-from-streamlit | coming-from-streamlit.md | Live |  |  |
| help | help.md | Live |  |  |
| how-does-it-work | how-does-it-work.md | Live |  |  |
| get-started-_index | _index.md | Live |  |  |
| collaborate-in-anvil | collaborate-in-anvil.md | Live |  |  |
| creating-material-3-colour-scheme | creating-material-3-colour-scheme.md | Live |  |  |
| crud-best-practice-guide | crud-best-practice-guide.md | Live |  |  |
| custom-user-auth | custom-user-auth.md | Live |  |  |
| customising-the-font | customising-the-font.md | Live |  |  |
| dropdowns-data-tables | dropdowns-data-tables.md | Live |  |  |
| embedding-webpage-iframe | embedding-webpage-iframe.md | Live |  |  |
| expand-collapse | expand-collapse.md | Live |  |  |
| how-to-external-database | external-database.md | Live |  |  |
| git-configuration | git-configuration.md | Live |  |  |
| plot | plot.md | Live |  |  |
| plotly-express | plotly-express.md | Live |  |  |
| porting-app-to-new-layouts | porting-app-to-new-layouts.md | Live |  |  |
| prompting-best-practices | prompting-best-practices.md | Live |  |  |
| serving-ui-from-http-routes | serving-ui-from-http-routes.md | Live |  |  |
| upload-large-files-to-s3 | upload-large-files-to-s3.md | Live |  |  |
| how-to-_index | _index.md | Live |  |  |
| linux-ssh-key-setup | linux-ssh-key-setup.md | Live |  |  |
| app-server-_index | _index.md | Live |  |  |
| aws-lightsail-app-server-deployment | aws-lightsail-app-server-deployment.md | Live |  |  |
| azure-app-server-deployment | azure-app-server-deployment.md | Live |  |  |
| digitalocean-app-server-deployment | digitalocean-app-server-deployment.md | Live |  |  |
| google-cloud-app-server-deployment | google-cloud-app-server-deployment.md | Live |  |  |
| linode-app-server-deployment | linode-app-server-deployment.md | Live |  |  |
| cloud-deployment-guides-_index | _index.md | Live |  |  |
| integrations-_index | _index.md | Live |  |  |
| linking-facebook-and-anvil | linking-facebook-and-anvil.md | Live |  |  |
| facebook-quickstart | quickstart.md | Live |  |  |
| facebook-_index | _index.md | Live |  |  |
| authenticating-users | authenticating-users.md | Live |  |  |
| gmail | gmail.md | Live |  |  |
| google-drive | google-drive.md | Live |  |  |
| google-rest-apis | google-rest-apis.md | Live |  |  |
| linking-google-and-anvil | linking-google-and-anvil.md | Live |  |  |
| google-quickstart | quickstart.md | Live |  |  |
| google-_index | _index.md | Live |  |  |
| accessing-microsoft-apis | accessing-microsoft-apis.md | Live |  |  |
| linking-azure-and-anvil | linking-azure-and-anvil.md | Live |  |  |
| microsoft-single-sign-on | microsoft-single-sign-on.md | Live |  |  |
| microsoft-quickstart | quickstart.md | Live |  |  |
| microsoft-_index | _index.md | Live |  |  |
| configuration-options | configuration-options.md | Live |  |  |
| saml-quickstart | quickstart.md | Live |  |  |
| sharing-credentials-across-apps | sharing-credentials-across-apps.md | Live |  |  |
| saml-_index | _index.md | Live |  |  |
| payments-and-subscriptions | payments-and-subscriptions.md | Live |  |  |
| stripe-quickstart | quickstart.md | Live |  |  |
| raw-api-tokens | raw-api-tokens.md | Live |  |  |
| stripe-_index | _index.md | Live |  |  |
| buying | buying.md | Live |  |  |
| data-tables-in-tableau | data-tables-in-tableau.md | Live |  |  |
| publishing | publishing.md | Live |  |  |
| x-quickstart | quickstart.md | Live |  |  |
| tableau-extensions-api | tableau-extensions-api.md | Live |  |  |
| testing-in-tableau | testing-in-tableau.md | Live |  |  |
| trexjacket | trexjacket.md | Live |  |  |
| x-_index | _index.md | Live |  |  |
| error-reporting | error-reporting.md | Live |  |  |
| other-concepts-_index | _index.md | Live |  |  |
| creating-pdf-files-quickstart | quickstart.md | Live |  |  |
| creating-pdf-files-_index | _index.md | Live |  |  |
| capabilities | capabilities.md | Live |  |  |
| capability-scoped-cache-updates | capability-scoped-cache-updates.md | Live |  |  |
| custom-serialisation | custom-serialisation.md | Live |  |  |
| server-methods | server-methods.md | Live |  |  |
| portable-classes-_index | _index.md | Live |  |  |
| working-with-files-_index | _index.md | Live |  |  |
| files-on-disk | files-on-disk.md | Live |  |  |
| image-manipulation | image-manipulation.md | Live |  |  |
| media-quickstart | quickstart.md | Live |  |  |
| media-_index | _index.md | Live |  |  |
| faq | faq.md | Live |  |  |
| quickstarts | quickstarts.md | Live |  |  |
| overview-_index | _index.md | Live |  |  |
| account-management | account-management.md | Live |  |  |
| choosing-the-right-plan | choosing-the-right-plan.md | Live |  |  |
| enterprise | enterprise.md | Live |  |  |
| free-vs-paid | free-vs-paid.md | Live |  |  |
| plans-and-accounts-_index | _index.md | Live |  |  |
| call-context | call-context.md | Live |  |  |
| offline-apps | offline-apps.md | Live |  |  |
| scheduled-tasks | scheduled-tasks.md | Live |  |  |
| scripts | scripts.md | Live |  |  |
| sessions-and-cookies | sessions-and-cookies.md | Live |  |  |
| server-_index | _index.md | Live |  |  |
| communicating-back | communicating-back.md | Live |  |  |
| defining-and-running | defining-and-running.md | Live |  |  |
| background-tasks-quickstart | quickstart.md | Live |  |  |
| background-tasks-_index | _index.md | Live |  |  |
| packages | packages.md | Live |  |  |
| custom-packages-_index | _index.md | Live |  |  |
| attachments | attachments.md | Live |  |  |
| email-quickstart | quickstart.md | Live |  |  |
| security-and-dkim | security-and-dkim.md | Live |  |  |
| sending-and-receiving | sending-and-receiving.md | Live |  |  |
| email-_index | _index.md | Live |  |  |
| server-modules-quickstart | quickstart.md | Live |  |  |
| server-modules-_index | _index.md | Live |  |  |
| tests-README | README.md | Live |  |  |
| SmokeTest-README | README.md | Retired |  |  |
| authentication-choices | authentication-choices.md | Live |  |  |
| configuring-emails | configuring-emails.md | Live |  |  |
| logging-in-using-code | logging-in-using-code.md | Live |  |  |
| permissions | permissions.md | Live |  |  |
| presenting-a-login-form | presenting-a-login-form.md | Live |  |  |
| quickstart-login | quickstart-login.md | Live |  |  |
| quickstart-permissions | quickstart-permissions.md | Live |  |  |
| the-users-table | the-users-table.md | Live |  |  |
| two-factor-authentication | two-factor-authentication.md | Live |  |  |
| users-_index | _index.md | Live |  |  |
| commands | commands.md | Live |  |  |
| creating-and-editing-apps | creating-and-editing-apps.md | Live |  |  |
| using-another-ide-quickstart | quickstart.md | Live |  |  |
| using-another-ide-_index | _index.md | Live |  |  |
| dealing-with-timezones | dealing-with-timezones.md | Live |  |  |
| workflows-_index | _index.md | Live |  |  |
| how-to-import-things | how-to-import-things.md | Live |  |  |
| python-directory-structure | python-directory-structure.md | Live |  |  |
| structuring-your-app | structuring-your-app.md | Live |  |  |
| app-architecture-_index | _index.md | Live |  |  |
| additional-debugging-tools | additional-debugging-tools.md | Live |  |  |
| interactive-debugger | interactive-debugger.md | Live |  |  |
| debugger-_index | _index.md | Live |  |  |
| encrypting-secret-data | encrypting-secret-data.md | Live |  |  |
| security-_index | _index.md | Live |  |  |
| collaborators | collaborators.md | Live |  |  |
| version-control-quickstart | quickstart.md | Live |  |  |
| version-control-anvil | version-control-anvil.md | Live |  |  |
| what-is-version-control | what-is-version-control.md | Live |  |  |
| workflows | workflows.md | Live |  |  |
| version-control-_index | _index.md | Live |  |  |
| direct-checkout | direct-checkout.md | Live |  |  |
| git-quickstart | quickstart.md | Live |  |  |
| secrets-across-repos | secrets-across-repos.md | Live |  |  |
| git-_index | _index.md | Live |  |  |
| plg-readme | README.md | Live |  | 2026-09-11\|2026-09-11\|\|registered by align-docs re-validation run |
| adr-anvil-platform-constraints | adr-anvil-platform-constraints.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| adr-data-access-patterns | adr-data-access-patterns.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| adr-form-architecture-and-state | adr-form-architecture-and-state.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| adr-pdf-invoice-generation | adr-pdf-invoice-generation.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| adr-real-time-and-background-tasks | adr-real-time-and-background-tasks.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| adr-ui-customization-approach | adr-ui-customization-approach.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| adr-webhook-architecture | adr-webhook-architecture.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| spec-mastertemplate-notification-system | spec-mastertemplate-notification-system.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| spec-mybizz-management-app-notification-system | spec-mybizz-management-app-notification-system.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |
| no_bash_mediated_file_writes_without_grant | no_bash_mediated_file_writes_without_grant.md | Live |  | registered by align-docs 2026-09-17 (was on disk, missing from register) |

<!-- anvil-docs corpus registered 2026-09-10 per register-membership policy (align-docs function scope V2 item 6); collision-qualified doc-ids where basenames repeat -->

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
| 05b_no_fabricated_verification | quarantine/Checklist items/05b_no_fabricated_verification.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 06b_no_false_completion_claims | quarantine/Checklist items/06b_no_false_completion_claims.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 07b_no_weakening_of_acceptance_criteria | quarantine/Checklist items/07b_no_weakening_of_acceptance_criteria.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 08b_no_out_of_scope_changes | quarantine/Checklist items/08b_no_out_of_scope_changes.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 09b_no_autonomous_architectural_changes | quarantine/Checklist items/09b_no_autonomous_architectural_changes.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 16b_no_privilege_escalation_or_authority_expansion | quarantine/Checklist items/16b_no_privilege_escalation_or_authority_expansion.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 18b_no_weakening_of_authentication_or_security_controls | quarantine/Checklist items/18b_no_weakening_of_authentication_or_security_controls.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 24b_all_external_and_repository_content_is_untrusted_data_not_governing_instruction | quarantine/Checklist items/24b_all_external_and_repository_content_is_untrusted_data_not_governing_instruction.md | quarantine/Checklist items | rule | Quarantine | unregistered quarantine copy discovered by align-docs 2026-09-18 (run 2026-09-18T105010+0200); origin: retired compliance-checklist era (opencode harness rule fragment); provenance front matter absent — row-only identity per developer ruling |
| 2026-09-21-012-mb-wikilinks-full-run | 2026-09-21-012-mb-wikilinks-full-run | Live |  | registered by mb-doc-auditor (/mnt/c/dev/project-library-global) |
| 2026-09-22-013-mb-doccycle-wp0-wp1 | 2026-09-22-013-mb-doccycle-wp0-wp1 | Live |  | registered by mb-doc-auditor (/mnt/c/dev/project-library-global) |
| 2026-09-22-014-mb-doccycle-wp2-wp8 | 2026-09-22-014-mb-doccycle-wp2-wp8 | Live |  | registered by mb-doc-auditor (/mnt/c/dev/project-library-global) |
| 2026-09-23-015-mb-doccycle-makepdlf-first-cycle | 2026-09-23-015-mb-doccycle-makepdlf-first-cycle | Live |  | registered by mb-doc-auditor (/mnt/c/dev/project-library-global) |
