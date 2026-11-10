---
title: "pol-common-aspects-for-mybizz-anvil-applications"
updated: "2026-11-10"
doc-id: "mb-ab18d72d"
---
# Policy — Common Aspects for Mybizz Anvil Applications

**Binding.** Every Mybizz application built on Anvil.works conforms to every aspect below, in the same way. An application deviates only where its business domain requires it, and records the deviation and its reason as an ADR in its own project library. See [[[default:adr-global/adr-common-architecture-across-mybizz-applications|Common Architecture Across Mybizz Applications]]](C:/dev/project-library-global/adr-global/adr-common-architecture-across-mybizz-applications.md) ADR.

---

## What

### 1. The five-app structure, never multi-tenant

Every application has App 1 (development workspace), App 2 (`master_template`, the published dependency), App 3 (`blank_client_template`, the client app), App 4 (one client instance per client) and App 5 (Mybizz management). Every client has its own App Server and its own database. No application ever shares a database between clients or separates clients by filtering. [[[default:specifications-global/spec-five-app-architecture-model|Five-App Architecture Model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md), [[[default:adr-global/adr-dependency-based-not-multi-tenant|Dependency-Based, Not Multi-Tenant]]](C:/dev/project-library-global/adr-global/adr-dependency-based-not-multi-tenant.md).

### 2. Client instance hosting

Each client instance runs on the Anvil App Server, in its own container on DigitalOcean named after the client's business, with its own database ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)). Server resources are raised for that client's container alone, with no change to App 2 and no effect on any other client. A client's transactions run in its own instance; App 2 carries no client load. Every client pays the same price, £79 a month or the fixed price in its currency. [[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md).

### 3. Configuration, never code, in a client instance

App 4 runs the release image: App 3's table definitions and startup module, and App 2, nothing else. Anything that differs between clients is data in the client's own tables, set through the application's settings, never code in the client instance. [[[default:adr-global/adr-client-instance-architecture|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md).

### 4. Schema designed up front, extended without breaking

- The schema is designed in App 1, published through App 2 and carried by App 3's table definitions, from which each client's App Server builds its tables. No application code creates or alters tables.
- Every core table carries a metadata column (a Simple Object column) for client-level attributes, and client-defined attributes use attribute tables, so that most new needs are met without a schema change. A core table is one that holds a business record a client works with, such as a contact, a booking, an invoice or a service. Log, control, link, lookup and attribute tables are not core tables.
- Every table carries `created_at`. Every table whose rows are edited after creation also carries `updated_at`.
- A later schema change adds only new tables or nullable columns. It is written into App 3's table definitions and recorded in the schema migration log; the release image carries it to every client instance, and the table-change check stops any release that removes, renames or retypes a table or column. [[[default:specifications-global/spec-deployment|Deployment]]](C:/dev/project-library-global/specifications-global/spec-deployment.md).

### 5. Secrets in the Vault

Every credential lives in the client's Vault. The one Anvil Secret is `encryption_key`. [[[default:specifications-global/spec-vault-system|Vault System]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md).

### 6. Payments, webhooks and outbound calls

- Stripe as the card gateway of every client instance, with PayPal as an optional second method. [[[default:specifications-global/spec-integration|Integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md).
- Every webhook handler returns 200 at once, processes in a background task, and is idempotent by the event's transaction id, so a repeated delivery never charges or fulfils twice. [[[default:adr-global/adr-webhook-architecture|Webhook Architecture]]](C:/dev/project-library-global/adr-global/adr-webhook-architecture.md).
- Every outbound call to a third party retries with backoff when rate-limited. Rate limits apply per client instance, so one client's volume never affects another's.

### 7. Email

Amazon SES for every email received and sent, one SES tenant per client; Anvil's system email goes through SES as its custom mail server. The CRM is built into the application. [[[default:adr-global/adr-brevo-email-and-crm|Amazon SES for Email; CRM Built In]]](C:/dev/project-library-global/adr-global/adr-brevo-email-and-crm.md).

### 8. Client storage and exit

Each client has one Cloudflare R2 bucket, in a free Cloudflare account in the client's own name; Mybizz is an invited member. Raw webhook payloads, archived logs, email bodies and backups go to the bucket; Data Tables keep an index row. When the client leaves, all its data is written to its bucket and Mybizz leaves the account. [[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md).

### 9. Management and health

- Every client instance exposes the management endpoints from its first release, secured with a per-client token. [[[default:adr-global/adr-mybizz-management-visibility|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md).
- Every client instance pushes a heartbeat of its health and resource use to App 5 on a schedule. App 5 never polls client instances. App 5 flags any client nearing its container's memory and the business nearing its cluster's client limit. [[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md).

### 10. Background work and real-time updates

Background tasks stay within each client container's memory. Near-real-time updates use client-side polling. [[[default:adr-global/adr-real-time-and-background-tasks|Real-Time and Background Tasks]]](C:/dev/project-library-global/adr-global/adr-real-time-and-background-tasks.md).

### 11. Access, currency and time

Role-based access with the same roles in every application. [[[default:specifications-global/spec-security-architecture|Security Architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md). System currency is set at onboarding and fixed after the first transaction. [[[default:adr-global/adr-system-currency-selection-and-immutability|System Currency]]](C:/dev/project-library-global/adr-global/adr-system-currency-selection-and-immutability.md). Times are stored in UTC and shown in the client's timezone. [[[default:adr-global/adr-timezone-utc-storage-display-conversion|Timezone]]](C:/dev/project-library-global/adr-global/adr-timezone-utc-storage-display-conversion.md).

### 12. Compliance

UK GDPR in every application, with each client's own privacy law for the data it controls; PCI DSS where it applies; the required legal documents before go-live, with acceptance and cookie consent recorded; the standard offboarding. [[[default:specifications-global/spec-regulatory-compliance-baseline|Regulatory Compliance Baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md), [[[default:policy-global/pol-legal-documents-and-consent|Legal Documents and Consent]]](C:/dev/project-library-global/policy-global/pol-legal-documents-and-consent.md).

### 13. User interface

`m3-custom-theme` only; Anvil standard components only where the theme has none; Anvil Extras and `HTMLTemplate` are not used; dark mode from the first release. [[[default:specifications-global/spec-ui-standards|UI Standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md).

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
