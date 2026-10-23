---
title: "pol-common-aspects-for-mybizz-anvil-applications"
updated: "2026-10-23"
doc-id: "mb-ab18d72d"
---
# Policy — Common Aspects for Mybizz Anvil Applications

**Binding.** Every Mybizz application built on Anvil.works conforms to every aspect below, in the same way. An application deviates only where its business domain requires it, and records the deviation and its reason as an ADR in its own project library. See [[[default:adr-global/adr-common-architecture-across-mybizz-applications|Common Architecture Across Mybizz Applications]]](C:/dev/project-library-global/adr-global/adr-common-architecture-across-mybizz-applications.md) ADR.

---

## What

### 1. The five-app structure, never multi-tenant

Every application has App 1 (development workspace), App 2 (`master_template`, the published dependency), App 3 (`blank_client_template`), App 4 (one client instance per client) and App 5 (Mybizz management). Every client has its own app and its own database. No application ever shares a database between clients or separates clients by filtering. [[[default:specifications-global/spec-five-app-architecture-model|Five-App Architecture Model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md), [[[default:adr-global/adr-dependency-based-not-multi-tenant|Dependency-Based, Not Multi-Tenant]]](C:/dev/project-library-global/adr-global/adr-dependency-based-not-multi-tenant.md).

### 2. Client Anvil accounts and plan tiers

Each client instance runs on an Anvil account of its own, held by Mybizz and named after the client's business. Every client starts on Anvil's Hobby tier. A client's tier is raised, or server resources are added, on that client's account alone, with no change to App 2 and no effect on any other client. A client's transactions run in its own instance; App 2 carries no client load.

### 3. Configuration, never code, in a client instance

App 4 holds the schema, one startup module and its dependency on App 2, nothing else. Anything that differs between clients is data in the client's own tables, set through the application's settings, never code in the client instance. [[[default:adr-global/adr-client-instance-architecture|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md).

### 4. Schema designed up front, extended without breaking

- The schema is designed in App 1, published through App 2 and carried by App 3. No code creates or alters tables.
- Every core table carries a metadata column (a Simple Object column) for client-level attributes, and client-defined attributes use attribute tables, so that most new needs are met without a schema change.
- A later schema change adds only new tables or nullable columns. It is applied by hand to App 3 and to every client instance, from a migration plan written before release. [[[default:specifications-global/spec-deployment|Deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md).

### 5. Secrets in the Vault

Every credential lives in the client's Vault. The one Anvil Secret is `encryption_key`. [[[default:specifications-global/spec-vault-system|Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md).

### 6. Payments, webhooks and outbound calls

- One active payment gateway per client instance (Stripe or Paystack). [[[default:specifications-global/spec-integration|Integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md).
- Every webhook handler returns 200 at once, processes in a background task, and is idempotent by the event's transaction id, so a repeated delivery never charges or fulfils twice. [[[default:adr-global/adr-webhook-architecture|Webhook Architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md).
- Every outbound call to a third party retries with backoff when rate-limited. Rate limits apply per client instance, so one client's volume never affects another's.

### 7. Email

Anvil's built-in email for system email, Brevo SMTP for transactional email, Brevo Campaigns for marketing. [[[default:adr-global/adr-brevo-email-and-crm|Brevo for Email and CRM]]](C:/dev/project-library-global/adr-global/adr-brevo-email-and-crm.md).

### 8. Client storage and exit

Each client has one or two Cloudflare R2 buckets of its own, set up at onboarding. Raw webhook payloads, logs and backups go to the buckets; Data Tables keep an index row. When the client exits, all its data is written to its bucket and the client leaves in possession of it. [[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md).

### 9. Management and health

- Every client instance exposes the management endpoints from its first release, secured with a per-client token. [[[default:adr-global/adr-mybizz-management-visibility|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md).
- Every client instance pushes a heartbeat of its health and resource use to App 5 on a schedule. App 5 never polls client instances. App 5 flags any client that needs a higher plan tier. [[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md).

### 10. Background work and real-time updates

Background tasks stay within the background-task limits of the client's plan tier. Near-real-time updates use client-side polling. [[[default:adr-global/adr-real-time-and-background-tasks|Real-Time and Background Tasks]]](C:/dev/project-library-global/adr-global/adr-real-time-and-background-tasks.md).

### 11. Access, currency and time

Role-based access with the same roles in every application. [[[default:specifications-global/spec-security-architecture|Security Architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md). System currency is set at onboarding and fixed after the first transaction. [[[default:adr-global/adr-system-currency-selection-and-immutability|System Currency]]](C:/dev/project-library-global/adr-global/adr-system-currency-selection-and-immutability.md). Times are stored in UTC and shown in the client's timezone. [[[default:adr-global/adr-timezone-utc-storage-display-conversion|Timezone]]](C:/dev/project-library-global/adr-global/adr-timezone-utc-storage-display-conversion.md).

### 12. Compliance

POPIA in every application; GDPR and PCI DSS where they apply; the required legal documents before go-live; the standard offboarding. [[[default:specifications-global/spec-regulatory-compliance-baseline|Regulatory Compliance Baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md).

### 13. User interface

Anvil's Material 3 theme only; components outside the M3 dependency, Anvil Extras and `HTMLTemplate` are not used; dark mode from the first release. [[[default:specifications-global/spec-m3-design-standards|M3 Design Standards]]](C:/dev/project-library-global/specifications-global/spec-m3-design-standards.md), [[[default:adr-global/adr-material-3-theme-component-scope|Material 3 Component Scope]]](C:/dev/project-library-global/adr-global/adr-material-3-theme-component-scope.md).

### 14. Reference platforms

An application may take a reference platform (for example Medusa, for e-commerce) as the model for its business domain and workflows. Only the domain and the workflows are taken. The reference's technology (its language, runtime, cache and queue services, connection poolers, or any shared-database tenancy) is never carried over: everything is rebuilt in Python for Anvil, to this policy.

### Both directions

An improvement to any aspect above, made while building one application, is written back to `project-library-global` and applied to every other application in its next release.

---

## Why

Mybizz applications differ in their business domain, not in how they are built, hosted, secured or managed. Building the shared aspects once keeps every application on one method, lets one fix serve all, and lets what one application teaches improve the others. Every difference that remains is deliberate and recorded.

---

## Where

Every Mybizz application built on Anvil.works, from its first build through PDLF, and every release after it.
