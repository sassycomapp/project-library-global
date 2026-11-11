---
title: "adr-company-compliance"
doc-id: "mb-9475f979"
updated: "2026-11-11"
---
# Company Compliance

Status: Accepted

---

## Context

Mybizz-Live Ltd is a private company limited by shares, registered in England and Wales, with one director who lives outside the UK. UK law sets the company yearly and quarterly obligations. A missed filing brings penalties, and a company that stops filing is struck off the register, which would stop every client's service. Mybizz is run by one person, so every deadline must reach David without him tracking it.

---

## Decision

1. **The obligations and how each is met:**

| Obligation | Deadline | How it is met |
|---|---|---|
| VAT registration | From incorporation, voluntarily | Registered online with HMRC on incorporation |
| VAT return | Quarterly, 1 month and 7 days after the quarter ends | Prepared and filed from FreeAgent under Making Tax Digital; David approves |
| Confirmation statement | Yearly, within 14 days of the review date | Filed online at Companies House by David |
| Annual accounts | 9 months after the year end; the first accounts 21 months after incorporation | Prepared and filed from FreeAgent as micro-entity accounts; David approves |
| Company tax return (CT600) | 12 months after the year end | Prepared and filed from FreeAgent; David approves |
| Corporation Tax payment | 9 months and 1 day after the year end | Paid from the Wise account |
| ICO data protection fee | Yearly | Tier 1, by direct debit |
| Registered office | Continuous | A UK address package: registered office and director's service address from one provider |

2. **Reminders.** App 5 reads every tax and accounts deadline from FreeAgent's tax timeline each day ([[[default:adr-global/adr-freeagent-integration]]](C:/dev/project-library-global/adr-global/adr-freeagent-integration.md)) and holds the confirmation statement date itself, because that filing is made at Companies House. App 5 sends David a reminder 30 days before each deadline.

3. **The year end** is the last day of the month in which the company was registered.

4. **The setup steps** and their order are in the business setup document, `mybizz-live-business-setup.md` in `data-mybizz-mgt`.

---

## Rationale

1. FreeAgent prepares and files the VAT returns, the accounts and the company tax return, so the filings that need accounting knowledge are produced by software, not by David.
2. Reading deadlines from FreeAgent's tax timeline means App 5 never holds a second, drifting copy of dates FreeAgent already calculates.
3. The ICO fee by direct debit renews itself.
4. Voluntary VAT registration removes VAT from almost every supplier cost and adds none to Mybizz's sales, because Paddle accounts for the VAT on payouts.

---

## Consequences

- App 5 carries the statutory deadline calendar ([[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).
- The budget carries each fee: ICO £47 a year, confirmation statement £50 a year, FreeAgent £33 a month, address package about £60 a year.

---

## Related Documents

- [[[default:adr-global/adr-freeagent-integration]]](C:/dev/project-library-global/adr-global/adr-freeagent-integration.md)
- [[[default:adr-global/adr-business-insurance]]](C:/dev/project-library-global/adr-global/adr-business-insurance.md)
- [[[default:specifications-global/spec-client-billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md)
