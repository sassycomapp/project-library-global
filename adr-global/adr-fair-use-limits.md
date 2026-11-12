---
title: "adr-fair-use-limits"
doc-id: "mb-f903b927"
updated: "2026-11-12"
---
# Fair-Use Limits

Status: Accepted

---

## Context

Every Mybizz client instance shares resources with every other client instance of the same business: one DigitalOcean Managed PostgreSQL cluster, one Amazon SES account, one Groq organisation and one DigitalOcean account. One client's heavy or abusive use of a shared resource can slow, stop or cost money for every other client. Each client pays one flat monthly price, so a client's use carries no extra charge that would discourage excess.

Mybizz is run by one person who does not watch supplier consoles. Every limit must therefore be measured and enforced automatically, and must stop excess before it harms other clients, while staying well above normal and heavy use.

---

## Decision

1. **Every shared resource carries a limit per client.** Each limit is set well above the budgeted use of a team of about six using every feature every working day, so normal and heavy use never reaches it.

2. **The limits are these:**

| Resource | Budgeted use | Warning to the client | Hard limit | At the hard limit |
|---|---|---|---|---|
| Database connections | Up to 3 | None | 3 | Further requests wait for a free connection. |
| Database query time | Under 1 second | None | 60 seconds per query | The query is cancelled and logged. |
| Idle open transaction | None | None | 120 seconds | The database session is ended. |
| Database size | 100 MB a year | 1 GiB | 2 GiB | Bulk imports are switched off for that client, and David is notified. |
| Container memory | 1 GiB | At 80% use | 2 GiB container | No further raise; David is notified. |
| Marketing email | About 10,000 a month | 20,000 | 25,000 a month | Marketing sends pause until the next month. Booking, invoice and sign-in emails continue. |
| All email | About 12,000 a month | 40,000 | 50,000 a month | All sending except sign-in email pauses until the next month; David is notified. |
| Email reputation | Bounces under 2%, complaints under 0.05% | SES warns at its reputation policy's warning level | SES reputation policy pause level | SES pauses that client's sending alone. App 5 notifies the client and David. |
| AI and natural voice spend | £5.60 a month | £5.60 | £16.80 a month | AI and natural voice pause until the next month. The browser's built-in voice continues. |
| AI request rate | A few a minute | None | 20 a minute | Further requests wait. |
| Data transfer | Within 150 GB | 150 GB | 500 GB a month | The client and David are notified, and the fair-use terms apply. |
| Client's own Cloudflare storage | Under 10 GB | 8 GB | None | Cloudflare bills the client directly above 10 GB. |

3. **The database limits are set on each client's database user** when the user is created: a connection limit of 3, a statement timeout of 60 seconds and an idle-in-transaction timeout of 120 seconds. PostgreSQL enforces them itself, so they hold even when App 5 is down.

4. **App 5 measures every other limit.**
   - Database size arrives with each client container's heartbeat.
   - Container memory comes from DigitalOcean's metrics through the DigitalOcean API.
   - Email volumes come from each client's SES tenant; email reputation is enforced by the SES tenant reputation policy itself.
   - AI and voice spend is metered per request in the client instance and reported with the heartbeat; the request rate is enforced in the client instance.
   - Data transfer comes from DigitalOcean's bandwidth figures for the client's container.
   - Sizes and monthly totals are checked once a day; the rest continuously.

5. **The Groq organisation carries its own spend limit of £1,700 a month,** with alerts at 50%, 75% and 90%. It covers every client at its AI and voice cap at 100 clients, so no single client can exhaust the shared limit while every client stays within its own.

6. **Notifications.** At a warning, App 5 emails the client's owner with the figure and the limit. At a hard limit, App 5 emails the client's owner and sends David an immediate message. Every warning and every hard-limit action is written to App 5's audit record and listed in David's daily summary.

7. **The limits are contractual.** The client service agreement carries every limit of point 2 as fair-use terms, together with the acceptable-use terms.

8. **Acceptable use and abuse reports.** A client's website or email used for spam, phishing or unlawful content breaches the acceptable-use terms. Every client website footer shows `abuse@mybizz.live`, which forwards to David. On a confirmed report, David uses App 5's **Suspend** action, which stops that client's container alone and records the reason.

---

## Rationale

1. A limit per client turns a shared resource into a fair share. One client can never take the capacity, the reputation or the budget that every other client depends on.
2. Limits far above budgeted use mean no ordinary client ever meets one, so the limits cost nothing in client goodwill.
3. Database limits held by PostgreSQL itself do not depend on Mybizz's code or on App 5 being up.
4. SES's per-tenant reputation policy pauses one client's sending before Amazon reviews the whole account, so one client's bad list cannot stop every client's email.
5. The Groq organisation limit is a second line behind the per-client cap: a fault in per-client metering can cost at most a known amount.
6. Fair-use terms in the agreement make every limit enforceable without dispute.
7. A published abuse address and a one-client **Suspend** action let Mybizz act before DigitalOcean or Amazon acts against the whole account.

---

## Consequences

- The highest cost of one client, with every limit reached, is £54.78 a month, which each client's £119 covers (the Mybizz budget, `Budget.md` in `data-mybizz-mgt`).
- Client provisioning creates each database user with the limits of point 3 ([[[default:specifications-global/spec-client-activation-runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)).
- App 5 carries the measurements, notifications and the **Suspend** action ([[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).
- The client instance meters AI and voice spend and enforces the request rate.
- The test suite tests every limit against simulated suppliers ([[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md)).

---

## Related Documents

- [[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md)
- [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)
- [[[default:specifications-global/spec-client-instance-hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)
- [[[default:specifications-global/spec-integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md)
- The client service agreement of each business
