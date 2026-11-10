---
title: "spec-regulatory-compliance-baseline"
doc-id: "mb-6f1553b6"
updated: "2026-11-10"
---
# Mybizz — Regulatory Compliance Baseline (Specification)

**Scope:** Mybizz-wide. This posture applies because Mybizz-Live Ltd is a United Kingdom company, operated from the United Kingdom, that serves businesses in the United States, Canada, the United Kingdom, the European Union, the European Economic Area and Switzerland, and runs one app and one database per client, never a multi-tenant model. It does not depend on what any individual app does.
App-specific facts (e.g., whether a given app actually processes payments, and therefore whether
PCI DSS applies to it) are recorded in [[[default:specifications-global/spec-security-architecture|Security Architecture Specification]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md), which
should reference this baseline rather than restate it.

---

## Roles

- **Each client is the controller** of the personal data of its own customers and staff. Mybizz-Live Ltd processes that data on the client's behalf, as **processor**, under the data processing agreement each client accepts.
- **Mybizz-Live Ltd is the controller** of its own records of client businesses: their contacts, registry record and billing status in App 5.
- All work with access to client personal data is carried out from the United Kingdom or from within the markets Mybizz serves, so that no other country's data protection law reaches Mybizz's processing.

## UK GDPR — Mandatory, Every App

Mybizz-Live Ltd is subject to the UK GDPR and the Data Protection Act 2018. Mybizz-Live Ltd registers with the Information Commissioner's Office (ICO) and pays its data protection fee before launch. The data subject rights — access, rectification, erasure, restriction, objection and portability — are implemented in every app.

## The Client's Own Law — Per Client

Each client's own law governs the data the client controls:

| Client's market | Law |
|---|---|
| United Kingdom | UK GDPR and the Data Protection Act 2018 |
| European Union and European Economic Area | EU GDPR |
| Switzerland | The Federal Act on Data Protection (FADP) |
| Canada | PIPEDA; in Quebec, Law 25 |
| United States | The privacy law of the client's state, such as the California Consumer Privacy Act (CCPA) |

The data-subject-rights implementation required by the UK GDPR (export and anonymisation functions) satisfies every law in the table: no separate implementation is needed per law. Each client's legal pages are written for the client's own law in the Clause Builder.

Client data is hosted in London. The United Kingdom holds an adequacy decision from the European Union and is recognised as adequate by Switzerland, so data from clients in Europe and Switzerland may be held there without further transfer safeguards.

## Personal Data Breaches

Mybizz, as processor, tells the affected client of a personal data breach without undue delay. The controller notifies its supervisory authority within 72 hours where its law requires it, and the people affected where the breach puts them at high risk. Mybizz's own procedure is in each app's incident response plan.

## PCI DSS — Conditional, Per App

Applies to any app that processes payments. The standard Mybizz approach: store only payment
tokens, never raw card numbers — this places a compliant app in SAQ A, the lowest compliance
scope. An annual Self-Assessment Questionnaire is required for any app in scope.

SAQ A also requires that the payment page cannot be tampered with by scripts: card details are taken only on the gateway's own hosted page or in the gateway's own embedded payment fields, never in the app's own inputs; every script on a page that hosts or redirects to payment is listed and approved, and the list is checked at every release (test SC-10).

## Standard Data Retention Periods (Mybizz-Wide Defaults)

| Data Type | Retention |
|---|---|
| Contacts | Indefinite, unless deletion requested |
| Transactions and invoices | 7 years (tax compliance) |
| Audit logs | 2 years |
| Cookie consent records | 2 years |
| Acceptance records of the Terms and Conditions and the Privacy Policy | 7 years |
| Email logs | 90 days |
| Completed tasks | Auto-deleted after 90 days |

A given app may need additional data categories beyond this list (recorded in that app's own
security document) but should not override these defaults without a stated reason.

## Required Legal Documents Before Any App Goes Live

Privacy Policy, Terms of Service, Cookie Policy — per app, since these are customer-facing and
must reflect that app's actual data practices, even though the underlying regulatory posture
above is shared. All three are built in the Clause Builder and published by the Owner before
the client instance goes live. Their versions, the acceptance of the Terms and Conditions and the Privacy
Policy, the cookie banner and every consent record follow [[[default:policy-global/pol-legal-documents-and-consent|Legal Documents and Consent]]](C:/dev/project-library-global/policy-global/pol-legal-documents-and-consent.md) and [[[default:specifications-global/spec-legal-documents-and-consent|Legal Documents and Consent]]](C:/dev/project-library-global/specifications-global/spec-legal-documents-and-consent.md).

## Standard Offboarding Data Handover Procedure

On client offboarding, all the client's data is written to the client's own R2 bucket, and the client leaves in possession of that bucket. After the handover is confirmed, the platform retains nothing of the client's data except the records Mybizz is legally required to keep. [[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md).

**Handover package, written to the client's R2 bucket:**
1. Full export of all Data Tables belonging to that client instance
2. The client's `encryption_key`
3. All Vault contents in decrypted form
4. Everything the bucket already holds (webhook payloads, logs, backups)

**Handover:** the bucket sits in the client's own Cloudflare account; Mybizz's Cloudflare user leaves that account.

**Post-handover:**
- All client data is removed from the platform
- No backup copies are retained beyond standard backup rotation window
- Offboarding is logged with timestamp, operator identity, and confirmation of data removal

**Legal basis:** Article 20 of the UK GDPR and of the EU GDPR (right to data portability). The procedure ensures clients can take their data to another
provider without platform lock-in.

