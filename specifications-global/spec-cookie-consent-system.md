---
title: "spec-cookie-consent-system"
doc-id: "mb-37dc0470"
updated: "2026-11-04"
---
# Mybizz — Cookie Consent System

**Scope:** Mybizz-wide. The single authoritative document on how every Mybizz application asks for, records and honours a visitor's cookie choice, and on its Cookie Policy. The rules it implements: [[[default:policy-global/pol-cookies-and-consent|Cookies and Consent]]](C:/dev/project-library-global/policy-global/pol-cookies-and-consent.md).

---

## 1. Cookie Categories

| Category | Consent | What it holds |
|---|---|---|
| Necessary | Not needed | Sign-in session, security, payment fraud checks by the payment services, the consent cookie (section 4) |
| Embedded content | Needed | Cookies set by embedded maps and videos from outside services |

No Mybizz application uses advertising or analytics cookies. A feature that would bring a cookie of another category is a policy change, decided before the feature is built.

## 2. The Cookie Register

Each application keeps a cookie register in its own security document: one row per cookie source, giving the source, its category, the feature that brings it, what it is used for, how long it lasts and the Cookie Policy clause that describes it. A row is added when the feature is built. The register and the seeded clauses (Appendix A) always agree.

## 3. The Banner

- Shown on the first visit to any public page, at the bottom of the screen, without blocking the page.
- Text: "This site uses cookies. Some are needed for the site to work. Others, from embedded maps and videos, are used only if you accept." Buttons: **Accept all**, **Refuse all**, **More info**.
- Accept all and Refuse all have the same size, style and position weight. More info opens the Cookie Policy page.
- Closing the banner without choosing sets nothing optional, and the banner shows again on the next page.
- A **Cookie settings** link in the footer of every public page opens the banner again.
- The banner text is a phrase key of the translation module, so it shows in the visitor's language.

## 4. The Consent Cookie

A first-party necessary cookie, `mb_consent`, holds the consent number, the choice (`accepted` or `refused`), the Cookie Policy version shown and the date of the choice. It lasts 12 months. The banner shows again when the cookie is missing, older than 12 months, or holds a version lower than the published Cookie Policy version.

## 5. Before and After the Choice

- Before a choice, and after Refuse all, no embedded content is loaded. Each embedded map or video shows a placeholder naming the service, with a **Load** button.
- **Load** loads that one item on that page view. It is recorded as a choice of `item:{service}` (section 6) and does not change the visitor's banner choice.
- After Accept all, embedded content loads and plays as built, with no further click.
- Help and explainer videos are stored with the application's own files and are never embedded from an outside service.

## 6. The Consent Record

Every choice, every change of choice and every **Load** click is recorded by a server function in the table `cookie_consents`:

| Column | Type | Notes |
|---|---|---|
| `consent_id` | string | The random consent number, the same as in `mb_consent` |
| `choice` | string | `accepted` / `refused` / `item:{service}` |
| `policy_version` | number | The Cookie Policy version shown |
| `created_at` | datetime | UTC |

The record holds no name, email address or IP address. Access: `client: none`, `server: full`.

**Retention.** The last 30 days stay in the table. A nightly background task moves older rows to the client's R2 bucket, in `cookie_consents/{year}/{month}/`, and deletes R2 files older than 2 years. The moved files are part of the client's data at exit, like every other file in the bucket.

**Proof.** A visitor who asks what they chose gives their consent number, shown in Cookie settings; the record is found by that number.

## 7. The Cookie Policy

The Cookie Policy is the Clause Builder's third document, beside the Privacy Policy and the Terms and Conditions, in the table `cookie_policy`:

| Column | Type | Notes |
|---|---|---|
| `category` | string | |
| `title` | string | |
| `clause` | string | |
| `sort_order` | number | Order within the category |
| `is_seeded` | bool | Seeded clauses can be edited, not deleted |
| `is_active` | bool | Published |
| `feature_key` | string | The feature whose cookies the clause describes; empty for a general clause |
| `created_at` | datetime | |
| `updated_at` | datetime | |

- The application seeds the clauses of Appendix A at provisioning.
- A clause with a `feature_key` is active exactly while its feature is in use: the application switches it on and off with the feature, and the Owner cannot switch it off while the feature is on. The Owner can edit its wording.
- Every publish raises the Cookie Policy version by one. The version is held in the application's configuration and read by the banner (section 4).
- The published policy shows on a public Cookie Policy page, linked from the footer beside the Privacy Policy and the Terms and Conditions.

## 8. Before Go-Live

The Owner reviews the seeded clauses, accepts or changes them, and publishes the Cookie Policy with the Privacy Policy and the Terms and Conditions, under the recorded acknowledgement of responsibility. The client instance does not go live until all three are published. [[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md).

## 9. What Is Tested

- On a first visit, the banner shows and no embedded-content cookie is set.
- Refuse all sets no embedded-content cookie; each map and video shows its placeholder.
- Accept all loads embedded content with no further click.
- Each choice, change and **Load** writes one `cookie_consents` row with the published version.
- A new Cookie Policy version shows the banner again.
- The nightly task moves rows older than 30 days to `cookie_consents/{year}/{month}/` and deletes files older than 2 years.
- A clause with a `feature_key` is active exactly while its feature is in use.

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

**5. Embedded videos.** Some pages show videos from YouTube, Vimeo or Dailymotion. These services set cookies when a video loads, to play the video and to measure its use. A video loads only if you accept cookies, or if you click Load on the video. Our help videos are stored on this site and set no outside cookies.

**6. Payment services.** When you pay online, the payment is handled by {payment_services}. These services set cookies on the payment pages to process the payment securely and to prevent fraud. These cookies are needed to make a payment and are set without asking you.

**7. Similar technologies.** This site may also store small amounts of information in your browser's own storage, in the same way as cookies, for example to remember your cookie choice. This policy covers that storage in the same way as cookies.

**8. No advertising or tracking.** This site does not use advertising cookies, does not use cookies to track you across other websites, and does not sell any information about your visit.

**9. Your choices.** When you first visit, you can accept or refuse the cookies that are not needed for the site to work. You can change your choice at any time through the Cookie settings link at the bottom of every page. You can also block or delete cookies in your browser's settings; your browser's help pages explain how.

**10. Records of your choice.** To show that we respect your choice, we record it with a random consent number, the date and time, and the version of this policy you were shown. The record does not include your name, email address or IP address. We keep it for 2 years. Your consent number is shown in Cookie settings.

**11. Outside services' own policies.** The outside services named in this policy are responsible for the cookies they set: {provider_policy_links}.

**12. Changes and contact.** We may update this policy when the site changes. When we do, the date below changes and you are asked for your choice again. If you have a question about cookies on this site, contact us at {contact_email}. Last updated: {policy_date}.
