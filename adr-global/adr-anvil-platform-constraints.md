---
title: "adr-anvil-platform-constraints"
doc-id: "mb-d1719e5a"
updated: "2026-10-23"
---
# `anvil-platform-constraints` ADR — Anvil Platform Constraints and Design Boundaries

**Status:** Accepted

---

## Context

Every Mybizz application is built on Anvil.works, a hosted full-stack Python platform. Anvil gives significant velocity — built-in hosting, HTTPS, Data Tables, user authentication and a visual designer — but imposes constraints that differ from a self-hosted Python deployment.

---

## Decision

**Every Mybizz application is designed within Anvil's parameters, never around them.** No feature assumes a capability Anvil does not provide. Velocity is chosen over a migration path: no abstraction layer is built for a hypothetical move off Anvil.

The constraints, and the rule each one imposes, are catalogued once, in [[[default:specifications-global/spec-anvil-platform-standards|Anvil Platform Mechanics]]](C:/dev/project-library-global/specifications-global/spec-anvil-platform-standards.md): section 17 (the checklist every design decision runs against) and sections 22 to 26 (the Skulpt runtime, Git integration, media and files, no persistent server, and `app_tables` resolution failure). The Owner's second-factor recovery for the Vault is set in [[[default:specifications-global/spec-vault-system|Spec: Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md) section 4.

---

## Consequences

- ✅ Faster development: no abstraction layers for a hypothetical migration
- ✅ A simpler codebase that uses Anvil's native capabilities directly
- ✅ Anvil-specific strengths used fully: lazy loading, background tasks, the dependency model
- ⚠️ Moving off Anvil would need a full rewrite; this is an accepted trade-off
- ⚠️ Anvil platform changes (deprecations, limit changes) affect every application directly
- ⚠️ Every developer and agent learns Anvil's patterns before building features

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-navigation-lambda-link-open-form\|Navigation Lambda/Link/open_form]]](C:/dev/project-library-global/adr-global/adr-navigation-lambda-link-open-form.md) | Navigation pattern that works within Anvil's constraints |
| [[[default:adr-global/adr-payment-security-boundary-vault\|Payment Security Boundary Vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) | The Vault holds every secret except `encryption_key` |
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | Dependency model — the core architectural pattern |
| [[[default:adr-global/adr-form-architecture-and-state\|Form Architecture and State Management]]](C:/dev/project-library-global/adr-global/adr-form-architecture-and-state.md) | How forms work within Anvil's form model |
| [[[default:adr-global/adr-real-time-and-background-tasks]]](C:/dev/project-library-global/adr-global/adr-real-time-and-background-tasks.md) | Background task patterns within Anvil's limits |
| [[[default:adr-global/adr-data-access-patterns\|Data Access Patterns and Query Limitations]]](C:/dev/project-library-global/adr-global/adr-data-access-patterns.md) | Data Table query patterns within Anvil's model |

