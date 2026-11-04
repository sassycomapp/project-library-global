---
title: "spec-legal-documents-and-consent"
doc-id: "mb-cb15091a"
updated: "2026-11-04"
---
# Mybizz — Legal Documents and Consent

**Scope:** Mybizz-wide. The single authoritative document on how every Mybizz application builds, publishes and versions its three legal documents, and asks for, records and honours consent and acceptance. The rules it implements: [[[default:policy-global/pol-legal-documents-and-consent|Legal Documents and Consent]]](C:/dev/project-library-global/policy-global/pol-legal-documents-and-consent.md).

---

## 1. The Three Documents

The Privacy Policy, the Terms and Conditions and the Cookie Policy are the Clause Builder's three documents, each in its own table: `privacy_policy`, `t_and_c` and `cookie_policy`.

| Column | Type | Notes |
|---|---|---|
| `category` | string | |
| `title` | string | |
| `clause` | string | |
| `sort_order` | number | Order within the category |
| `is_seeded` | bool | Seeded clauses can be edited, not deleted |
| `is_active` | bool | Published |
| `created_at` | datetime | |
| `updated_at` | datetime | |

`cookie_policy` has one further column, `feature_key` (string): the feature whose cookies the clause describes, empty for a general clause. A clause with a `feature_key` is active exactly while its feature is in use; the application switches it on and off with the feature, and the Owner cannot switch it off while the feature is on. The Owner can edit its wording.

The application seeds each document's clauses at provisioning; the Cookie Policy's seeds are in Appendix A. Each published document shows on its own public page, linked from the footer of every public page.

## 2. Versions and Kept Copies

- Every publish of a document raises that document's version by one. The three versions are held in the application's configuration.
- At every publish, the application writes the published text, as an HTML page, to the client's R2 bucket at `legal/{document}/v{version}.html`, where `{document}` is `privacy_policy`, `t_and_c` or `cookie_policy`.
- Kept copies are never changed or deleted while the client's data exists. They are part of the client's data at exit.

## 3. Acceptance of the Terms and Conditions and the Privacy Policy

- At every point where a customer enters an agreement with the business, the customer ticks one box, never ticked in advance: "I accept the Terms and Conditions and have read the Privacy Policy." Both documents are linked beside the box. The agreement does not proceed without it.
- Each application lists its acceptance points in its own design documents. Typical points: a booking, an order, a purchase, an online payment, signing up to the customer portal, and accepting a quote.
- When either document is published in a new version, the customer accepts the new version at the next agreement or the next customer-portal sign-in.
- Every form that collects personal details links to the Privacy Policy beside its submit button. Sending the form records that the person was shown the current version.

## 4. Cookie Categories

| Category | Consent | What it holds |
|---|---|---|
| Necessary | Not needed | Sign-in session, security, payment fraud checks by the payment services, the consent cookie (section 7) |
| Embedded content | Needed | Cookies set by embedded maps and videos from outside services |

No Mybizz application uses advertising or analytics cookies. A feature that would bring a cookie of another category is a policy change, decided before the feature is built.

## 5. The Cookie Register

Each application keeps a cookie register in its own security document: one row per cookie source, giving the source, its category, the feature that brings it, what it is used for, how long it lasts and the Cookie Policy clause that describes it. A row is added when the feature is built. The register and the seeded clauses always agree.

## 6. The Cookie Banner

- Shown on the first visit to any public page, at the bottom of the screen, without blocking the page.
- Text: "This site uses cookies. Some are needed for the site to work. Others, from embedded maps and videos, are used only if you accept." Buttons: **Accept all**, **Refuse all**, **More info**.
- Accept all and Refuse all have the same size, style and position weight. More info opens the Cookie Policy page.
- Closing the banner without choosing sets nothing optional, and the banner shows again on the next page.
- A **Cookie settings** link in the footer of every public page opens the banner again, and shows the visitor's consent number.
- The banner text is a phrase key of the translation module, so it shows in the visitor's language.

## 7. The Consent Cookie

A first-party necessary cookie, `mb_consent`, holds the consent number, the choice (`accepted` or `refused`), the Cookie Policy version shown and the date of the choice. It lasts 12 months. The banner shows again when the cookie is missing, older than 12 months, or holds a version lower than the published Cookie Policy version.

## 8. Before and After the Cookie Choice

- Before a choice, and after Refuse all, no embedded content is loaded. Each embedded map or video shows a placeholder naming the service, with a **Load** button.
- **Load** loads that one item on that page view. It is recorded as a choice of `item:{service}` and does not change the visitor's banner choice.
- After Accept all, embedded content loads and plays as built, with no further click.

## 9. Help Videos

Help and explainer videos are stored once per language in a Mybizz-owned Cloudflare R2 bucket published at `media.mybizz.live`, and play in the video component as direct video addresses. They are never stored in `theme/assets/` and never embedded from an outside video service. No Cloudflare feature that sets cookies is enabled on `media.mybizz.live`, so the videos play at once with no consent needed.

## 10. The Consent Record

Every cookie choice, every change of choice, every **Load** click, every acceptance and every privacy notice shown on a form is recorded by a server function in one table, `consents`:

| Column | Type | Notes |
|---|---|---|
| `consent_id` | string | A random record number; for a cookie record, the same as in `mb_consent` |
| `document` | string | `cookie_policy` / `privacy_policy` / `t_and_c` |
| `choice` | string | `accepted` / `refused` / `item:{service}` / `shown` |
| `policy_version` | number | The version of the document shown |
| `contact_id` | link → contacts | The contact who accepted or was shown the notice; empty for a cookie record |
| `created_at` | datetime | UTC |

A cookie record holds no name, email address or IP address. Access: `client: none`, `server: full`.

**Retention.** The last 30 days stay in the table. A nightly background task moves older rows to the client's R2 bucket, in `consents/{document}/{year}/{month}/`, and deletes R2 files older than their retention: 2 years under `consents/cookie_policy/`, 7 years under `consents/privacy_policy/` and `consents/t_and_c/`. The moved files are part of the client's data at exit.

**Proof.** A cookie record is found by the consent number shown in Cookie settings. An acceptance record is found by the contact, and is matched to the kept copy of the version accepted (section 2).

## 11. Before Go-Live

The Owner reviews the seeded clauses of all three documents, accepts or changes them, and publishes all three under the recorded acknowledgement of responsibility. The client instance does not go live until all three are published. [[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md).

## 12. What Is Tested

- A publish raises the document's version and writes `legal/{document}/v{version}.html`.
- An agreement does not proceed without the acceptance box ticked, and writes one `consents` row for each of `t_and_c` and `privacy_policy` with the published versions and the contact.
- A new version of either document is asked for at the customer's next agreement or portal sign-in.
- A form that collects personal details writes one `shown` row for the Privacy Policy.
- On a first visit, the cookie banner shows and no embedded-content cookie is set.
- Refuse all sets no embedded-content cookie; each map and video shows its placeholder.
- Accept all loads embedded content with no further click.
- Each cookie choice, change and **Load** writes one `consents` row with the published version and no contact.
- A new Cookie Policy version shows the banner again.
- The nightly task moves rows older than 30 days to `consents/{document}/{year}/{month}/`, and deletes cookie files older than 2 years and acceptance files older than 7 years.
- A Cookie Policy clause with a `feature_key` is active exactly while its feature is in use.
- `media.mybizz.live` sets no cookie.

---

## Appendix A — Seeded Cookie Policy Clauses

These clauses show how cookie policies are typically written. They are seeded as examples. The Owner accepts or changes them, and is responsible for their content, before the client instance goes live. `{business_name}` and `{contact_email}` are filled from the business profile, `{policy_date}` from the date of publication, `{payment_services}` from the payment services the client has switched on, and `{provider_policy_links}` from the outside services in use. Each outside service's cookie-policy link is checked when the feature that brings it is built.

| # | Category | Title | `feature_key` |
|---|---|---|---|
| 1 | About cookies | What cookies are | — |
| 2 | About cookies | Who sets cookies on this site | — |
| 3 | Cookies we use | Cookies the site needs | — |
| 4 | Cookies we use | Embedded maps | `maps` |
| 5 | Cookies we use | Embedded videos | `video` |
| 6 | Cookies we use | Payment services | `payments` |
| 7 | Cookies we use | Similar technologies | — |
| 8 | Cookies we use | No advertising or tracking | — |
| 9 | Your choices | Your choices | — |
| 10 | Your choices | Records of your choice | — |
| 11 | Your choices | Outside services' own policies | — |
| 12 | About this policy | Changes and contact | — |

**1. What cookies are.** Cookies are small text files that a website stores in your browser when you visit it. They let the site remember things, such as that you are signed in, and let embedded services, such as a map or a video, work. Some cookies last only until you close your browser; others stay for a set time.

**2. Who sets cookies on this site.** This site is run by {business_name}. Some cookies are set by this site itself. Others are set by outside services that this site embeds or uses, such as a map, a video or a payment service. Those services are named below, and their own policies apply to the cookies they set.

**3. Cookies the site needs.** Some cookies are needed for the site to work, and are set without asking you. They keep you signed in while you use the site, protect the site and its forms against misuse, and remember your cookie choice. You can block them in your browser, but parts of the site, such as signing in, will then not work.

**4. Embedded maps.** Our Contact page and footer show a map from Google Maps. Google sets cookies when the map loads, to provide the map and to protect the service. The map loads only if you accept cookies, or if you click Load on the map.

**5. Embedded videos.** Some pages show videos from YouTube, Vimeo or Dailymotion. These services set cookies when a video loads, to play the video and to measure its use. A video loads only if you accept cookies, or if you click Load on the video. The help videos inside the site set no cookies.

**6. Payment services.** When you pay online, the payment is handled by {payment_services}. These services set cookies on the payment pages to process the payment securely and to prevent fraud. These cookies are needed to make a payment and are set without asking you.

**7. Similar technologies.** This site may also store small amounts of information in your browser's own storage, in the same way as cookies, for example to remember your cookie choice. This policy covers that storage in the same way as cookies.

**8. No advertising or tracking.** This site does not use advertising cookies, does not use cookies to track you across other websites, and does not sell any information about your visit.

**9. Your choices.** When you first visit, you can accept or refuse the cookies that are not needed for the site to work. You can change your choice at any time through the Cookie settings link at the bottom of every page. You can also block or delete cookies in your browser's settings; your browser's help pages explain how.

**10. Records of your choice.** To show that we respect your choice, we record it with a random consent number, the date and time, and the version of this policy you were shown. The record does not include your name, email address or IP address. We keep it for 2 years. Your consent number is shown in Cookie settings.

**11. Outside services' own policies.** The outside services named in this policy are responsible for the cookies they set: {provider_policy_links}.

**12. Changes and contact.** We may update this policy when the site changes. When we do, the date below changes and you are asked for your choice again. If you have a question about cookies on this site, contact us at {contact_email}. Last updated: {policy_date}.
