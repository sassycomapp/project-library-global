---
document: Global ADR Index
doc-id: INDEX
state: Live
date-created: 2026-07-25T150027+0200
---
# Global ADR Index

Architecture Decision Records that apply to all Anvil.works projects. Check this index before making architecture or technology decisions. Read only the specific ADR relevant to the current decision.

Full index with statuses and dates: `adr-index.md`.

## Quick reference — Key ADRs by category

### Architecture
- [[client-instance-architecture|Client Instance Architecture]] — Dependency-based architecture, not multi-tenant
- [[dependency-based-not-multi-tenant|Dependency-Based Architecture, Not Multi-Tenant]] — Prohibits tenant discriminator columns
- [[dependency-update-model|Dependency Update Model]] — Four-app update flow
- [[data-access-patterns|Data Access Patterns and Query Limitations]] — Data access patterns and query limitations

### Security & Payments
- [[payment-security-boundary-vault|Payment Security Boundary Vault]] — Payment security via Vault
- [[payment-gateway-configuration-is-a-settings-function-and-is-rbac-governed|Payment Gateway Configuration Is a Settings Function and Is RBAC-Governed]] — RBAC-governed settings
- [[client-data-management-rights-and-mybizz-retention-boundary|Client Data Management Rights and Mybizz Retention Boundary]] — Data rights boundary

### UI & Design
- [[design-rules|Design Rules]] — Design rules
- [[material-3-theme-component-scope|Material 3 Theme Component Scope]] — M3 component scope
- [[responsive-behaviour-mechanism|Responsive Behaviour Mechanism]] — Responsive via `wrap_on`, not CSS breakpoints
- [[htmltemplate-use|HTMLTemplate Use]] — HTMLTemplate is banned
- [[dark-mode-v1|Dark Mode V1]] — Dark mode in V1
- [[ui-customization-approach|UI Customization Approach]] — M3+CSS customization

### Data & Currency
- [[system-currency-selection-and-immutability|System Currency Selection and Immutability]] — Currency rules
- [[timezone-utc-storage-display-conversion|Client Timezone: UTC Storage, Display Conversion]] — UTC storage, display conversion
- [[single-contacts-table|Single Contacts Table]] — Single contacts table
- [[tiers-model|Tiers Model]] — Tiers model

### Integration & Platform
- [[anvil-platform-constraints|Anvil Platform Constraints and Design Boundaries]] — Platform constraints
- [[anvil-extras-exclusion|Anvil Extras Exclusion]] — No Anvil Extras
- [[webhook-architecture|Webhook Architecture]] — Webhook patterns
- [[observability-architecture|Observability Architecture]] — Observability design

### Onboarding
- [[onboarding-finality|Onboarding Finality]] — Onboarding is resumable
- [[onboarding-resumability|Onboarding Resumability]] — Resumability mechanism
- [[onboarding-vs-settings-boundary|Onboarding vs Settings Boundary]] — Onboarding vs settings boundary
- [[onboarding-data-schema-alignment|Onboarding Data Schema Alignment]] — Data schema alignment

### Dev Tooling & Source Control
- [[dev-tooling-source-repos-must-be-github-backed|All Dev-Tooling Source Repositories Must Be GitHub-Backed]] — Every PDLF/dev-makepdlf source repo must have a GitHub remote; template repos for scaffolds, normal repos for live tools
