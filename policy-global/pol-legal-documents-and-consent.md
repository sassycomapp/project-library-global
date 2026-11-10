---
title: "pol-legal-documents-and-consent"
doc-id: "mb-48f56d2b"
updated: "2026-11-10"
---
# Policy — Legal Documents and Consent

**Binding.** Every Mybizz application conforms. No exceptions without documented justification.

**How it is built:** [[[default:specifications-global/spec-legal-documents-and-consent|Legal Documents and Consent]]](C:/dev/project-library-global/specifications-global/spec-legal-documents-and-consent.md).

---

## What

### Three Legal Documents, One System

Every client site publishes a Privacy Policy, Terms and Conditions and a Cookie Policy. All three are built in the Clause Builder from seeded clauses, published by the Owner, and handled by the same versioning and consent rules.

### The Owner Is Responsible for the Content

The Owner accepts or changes the seeded clauses and publishes all three documents before the client instance goes live, under a recorded acknowledgement of responsibility. [[[default:adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture|Legal Policy Responsibility]]](C:/dev/project-library-global/adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md).

### Every Published Version Is Kept

Each publish creates a new version of the document, and a copy of that exact version is kept in the client's R2 bucket for the life of the client's data.

### Customers Accept the Terms Where They Enter an Agreement

At every point where a customer enters an agreement with the business, the customer ticks a box, never ticked in advance: "I accept the Terms and Conditions and have read the Privacy Policy." The agreement does not proceed without it. Every form that collects personal details links to the Privacy Policy. A new version of either document is accepted at the customer's next agreement or next customer-portal sign-in.

### Consent Before Any Optional Cookie

A client's site sets only the cookies and browser storage it needs to work until the visitor chooses: sign-in, security, payment fraud checks and the record of the visitor's choice. Every other cookie, including those of embedded maps and videos, is set only after the visitor accepts.

### Refusing Is as Easy as Accepting

The first visit shows a banner with **Accept all**, **Refuse all** and **More info**. Accept all and Refuse all are equally visible and each takes one click. Closing the banner, scrolling or carrying on browsing is never taken as consent. Nothing is ticked in advance.

### The Choice Can Be Changed at Any Time

A **Cookie settings** link in the footer of every public page opens the banner again. Changing the choice is as easy as making it. The choice is remembered for 12 months, and asked again after 12 months or when the Cookie Policy is published in a new version.

### Every Choice and Every Acceptance Is Recorded

Every cookie choice and every acceptance of the Terms and Conditions or the Privacy Policy is recorded with the document, the choice, the version shown and the date and time. Cookie records hold no name, email address or IP address. Acceptance records hold the contact who accepted. Cookie records are kept for 2 years; acceptance records for 7 years.

### Every Cookie Is Known at Build Time

Clients never add code, so clients never add cookies. Every cookie a site can set comes from a feature MyBizz built, and is listed in the application's cookie register when that feature is built. A feature that brings a new cookie is not released until its register entry and its Cookie Policy clause exist.

### Help Videos Set No Outside Cookies

Help and explainer videos are stored once per language in a Mybizz-owned Cloudflare R2 bucket published at `media.mybizz.live`, and play as direct video addresses. No Cloudflare feature that sets cookies is enabled on that address, so the videos play at once with no consent needed.

---

## Why

- The EU ePrivacy rules, as applied by the UK and French regulators, require consent before any non-essential cookie is set, a refusal as easy as acceptance, and proof of each consent (GDPR Article 7(1)).
- A record of acceptance proves an agreement only when the exact text accepted can be shown, so each published version is kept beside the records that point to it.
- Acceptance records prove the terms behind bookings, orders and invoices, so they are kept as long as those transactions: 7 years.
- One system for all three documents means one mechanism to build, test and maintain.
- Recording no personal data in a cookie record keeps that record outside the data it would otherwise have to protect.
- Self-hosted help videos remove the one case where the consent rule would add friction for the client's own staff.
