---
title: "pol-cookies-and-consent"
doc-id: "mb-19834f9b"
updated: "2026-11-04"
---
# Policy — Cookies and Consent

**Binding.** Every Mybizz application conforms. No exceptions without documented justification.

**How it is built:** [[[default:specifications-global/spec-cookie-consent-system|Cookie Consent System]]](C:/dev/project-library-global/specifications-global/spec-cookie-consent-system.md).

---

## What

### Consent Before Any Optional Cookie

A client's site sets only the cookies and browser storage it needs to work until the visitor chooses: sign-in, security, payment fraud checks and the record of the visitor's choice. Every other cookie, including those of embedded maps and videos, is set only after the visitor accepts.

### Refusing Is as Easy as Accepting

The first visit shows a banner with **Accept all**, **Refuse all** and **More info**. Accept all and Refuse all are equally visible and each takes one click. Closing the banner, scrolling or carrying on browsing is never taken as consent. Nothing is ticked in advance.

### The Choice Can Be Changed at Any Time

A **Cookie settings** link in the footer of every public page opens the banner again. Changing the choice is as easy as making it.

### The Choice Is Remembered and Renewed

The choice is remembered for 12 months. The banner shows again after 12 months, and whenever the Cookie Policy is published in a new version.

### Every Choice Is Recorded

Each choice is recorded with a random consent number, the choice, the Cookie Policy version shown and the date and time. The record holds no name, email address or IP address. Records are kept for 2 years.

### Every Cookie Is Known at Build Time

Clients never add code, so clients never add cookies. Every cookie a site can set comes from a feature MyBizz built, and is listed in the application's cookie register when that feature is built. A feature that brings a new cookie is not released until its register entry and its Cookie Policy clause exist.

### Help Videos Set No Outside Cookies

Help and explainer videos are stored with the application's own files, never on an outside video service, so they play at once with no consent needed.

### The Owner Is Responsible for the Cookie Policy

The Cookie Policy is built in the Clause Builder from seeded clauses. The Owner accepts or changes them and publishes the policy before the client instance goes live, under the same acknowledgement of responsibility as the Privacy Policy and Terms and Conditions. [[[default:adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture|Legal Policy Responsibility]]](C:/dev/project-library-global/adr-global/adr-legal-policy-responsibility-acknowledgement-and-clause-builder-architecture.md).

---

## Why

- The EU ePrivacy rules, as applied by the UK and French regulators, require consent before any non-essential cookie is set, a refusal as easy as acceptance, and proof of each consent (GDPR Article 7(1)). POPIA has no cookie rule of its own, and consent first is the accepted practice in South Africa.
- One rule for every client site means one mechanism to build, test and maintain, whichever regime a client's visitors fall under.
- Recording no personal data in the consent record keeps the record itself outside the data it would otherwise have to protect.
- Self-hosted help videos remove the one case where the consent rule would add friction for the client's own staff.
