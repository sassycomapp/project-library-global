---
title: "spec-translation"
doc-id: "mb-9bdef25d"
updated: "2026-11-10"
---
# Translation

**Scope:** Every Mybizz application. How an application shows every fixed text, email, document, date, number and amount in the client's chosen language.

---

## 1. Languages

| Code | Language | Variant | Gateway locale |
|---|---|---|---|
| `en` | English | United Kingdom | `en-GB` / `en_GB` |
| `fr` | French | France | `fr` / `fr_FR` |
| `es` | Spanish | Spain | `es` / `es_ES` |
| `de` | German | Germany | `de` / `de_DE` |
| `it` | Italian | Italy | `it` / `it_IT` |

- The client chooses one language for the whole instance: screens, public website, emails, documents and help videos. The choice is stored in `business_profile.app_language`, set at onboarding and changeable in Settings; a change reloads the application in the new language.
- English is the source language. A language is offered only when every phrase key exists in it.
- No right-to-left language is offered.
- Gateway locale: Stripe takes the first form, PayPal the second.

## 2. What is translated

| Translated | Not translated |
|---|---|
| Every fixed screen text: headings, labels, buttons, menus, placeholders, tooltips, empty states, messages, errors, alerts | The client's own content: services, products, blog posts, pages, email templates the client writes |
| The public website's fixed text | Names and data entered by people |
| System emails, invoice and quote PDFs, customer statements | |
| Sample data | |
| Help videos (one version per language) | |

## 3. Phrase keys

- Every fixed text has a phrase key: lowercase words joined by dots, from general to particular, for example `booking.confirm.button`, `invoice.status.overdue`.
- A key names its place and purpose, never its English wording, so the English can change without breaking any other language.
- One key per meaning. The same English word with two meanings has two keys.

## 4. The translation module

`client_code/shared/translations/` in App 2 (shared code runs in the browser and on the server, so screens and emails use one source):

| File | Holds |
|---|---|
| `__init__.py` | `t(key, **values)`, `t_plural(key, count, **values)`, `translate_form(form)`, the current language |
| `en.py`, `fr.py`, `pt.py`, `es.py`, `de.py`, `it.py` | `PHRASES = {key: text}` for that language |
| `formats.py` | Per language: month and day names, date and time patterns, decimal and thousands separators, currency pattern; taken from CLDR, the Unicode standard locale data |
| `glossary.py` | Per language: the fixed translation of each product term (booking, invoice, package, Vault and so on) |

- `t(key, **values)` returns the text in the current language, with each `{name}` replaced by its value. Each language places the values in its own word order.
- `t_plural(key, count)` chooses the form by the CLDR plural rule of the language:

| Language | `one` | `other` |
|---|---|---|
| `en`, `de`, `it`, `es` | count is 1 | every other count |
| `pt` (Portugal) | count is 1 | every other count |
| `fr` | count is 0 or 1 | every other count |

  A plural key holds both forms: `{"one": "...", "other": "..."}`.
- Missing text: a key missing in the current language shows the English text, and the gap is written to `error_log`. A key missing in English shows the key itself and is a test failure.
- Dates, numbers and amounts are formatted only through `formats.py`, on the browser and on the server alike, so both show the same result.
- Every update to the module reaches every client instance through App 2.

## 5. Screens

- The Designer holds the phrase key as each component's visible text (text, placeholder, tooltip, title, items). It never holds words.
- Each form's `__init__` calls `translate_form(self)` after `self.init_components(**properties)`. `translate_form` walks every component of the form and replaces each phrase key with its text. Text set later in code uses `t()`.
- Server functions never return finished text for display. They return a phrase key and its values (`{"message": "booking.slot_taken", "values": {...}}`), and the browser calls `t()`.
- Layouts allow for text up to 40% longer than English: buttons and labels wrap or grow, never cut text off. Layouts are checked in German, the longest of the six.

## 6. Emails and documents

- System emails and invoice, quote and statement PDFs are built on the server with `t()` and `formats.py` in the instance's language.
- Email templates the client edits are stored per language (`email_templates.language`); the defaults are created in the client's language from the phrase files.

## 7. Anvil's own screens and emails

- Anvil's built-in sign-in, sign-up and two-factor forms are English only. Every application builds its own sign-in, sign-up, two-factor enrolment and two-factor login screens with Anvil's code functions (`anvil.users.login_with_email`, `anvil.users.signup_with_email`, `anvil.users.mfa`), translated like every other screen.
- Anvil's two-factor reset page and the browser's security-key prompt are shown by Anvil and the browser in their own language.
- Anvil's Users service emails (password reset, email confirmation, two-factor reset) have one template per app, set in the editor. Each template holds all six languages, English first, in App 3, so every clone carries them and a language change needs no edit.

## 8. Payment screens

Stripe Elements and PayPal's buttons are given the app language as `locale` (section 1).

## 9. Help videos

Each help video is held per language. The help pop-up plays the version in the app language, and the English version with subtitles when that language's version does not yet exist.

## 10. Producing translations

1. The build agents write the English text of every key.
2. AI translates every key into each other language, applying `glossary.py`, keeping every `{name}` placeholder, and keeping plural forms.
3. The tests in section 11 must pass before a language is offered.
4. A wrong translation reported by a client through Help is corrected in the phrase file and reaches every client with the next release.

## 11. Tests

| Check | How |
|---|---|
| Every visible Designer text is a phrase key | Scanner over every form's YAML |
| Every key used in code and forms exists in `en.py` | Scanner |
| Every key in `en.py` exists in each offered language | Scanner |
| Every language keeps the same `{name}` placeholders and plural forms | Scanner |
| No English text and no raw key shows with another language set | Browser test of every admin screen in French and German |
| Emails and PDFs come out in the instance's language | Test with the mail catcher |

## 12. Adding a language

Add its phrase file, its `formats.py` and `glossary.py` entries and its plural rule; pass section 11; release through App 2. Every client can then choose it.

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-integration\|Integration Specification]]](C:/dev/project-library-global/specifications-global/spec-integration.md) | Gateway locale |
| [[[default:specifications-global/spec-security-architecture\|Security & Secrets Architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md) | Sign-in and two-factor rules the custom sign-in screens follow |
