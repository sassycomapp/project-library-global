---
title: "adr-freeagent-integration"
doc-id: "mb-284cb388"
updated: "2026-11-11"
---
# FreeAgent Integration

Status: Accepted

---

## Context

Mybizz-Live Ltd keeps its accounts in FreeAgent, which files its VAT returns, annual accounts and company tax return. FreeAgent calculates every tax and accounts deadline and receives every bank transaction from the Wise account through a bank feed. App 5 sends David his reminders and his daily summary, so it needs FreeAgent's deadlines and figures without David copying them across.

FreeAgent's API signs in with OAuth and has no read-only permission: a connection can do anything the approving FreeAgent user can do.

---

## Decision

1. **App 5 connects to FreeAgent's API through its own FreeAgent user,** created by David at the lowest access level that reads the tax timeline (Tax, Accounting and Users). David approves the connection once, signed in as that user.

2. **App 5 only reads.** App 5's code calls only read requests on the FreeAgent API. No request that creates, changes or deletes anything in FreeAgent exists in App 5.

3. **What App 5 reads:**

| FreeAgent data | Use in App 5 |
|---|---|
| Tax timeline | Every tax and accounts deadline, read daily; a reminder to David 30 days before each one |
| Corporation Tax returns | The amount due and the filing and payment status |
| Bank transactions of the Wise account | The daily bank feed check: a message to David when no Wise transaction has arrived for 7 days |
| Monthly income and costs | The figures in David's daily summary |

4. **Credentials.** The OAuth tokens are stored in App 5's Vault and are never shown or logged.

5. **Failure.** When a FreeAgent request fails, or the connection's approval has lapsed, App 5 sends David an immediate message naming the failure and what to do.

6. **Bank feed consent.** FreeAgent's access to the Wise account must be renewed every 90 days. App 5 reminds David 7 days before each 90-day consent ends.

---

## Rationale

1. A separate FreeAgent user for App 5 limits what a leaked token can reach to that user's access level, and can be removed without affecting David's own access.
2. Building only read requests into App 5 makes "read only" a property of the code, since FreeAgent's API offers no read-only permission.
3. Reading deadlines from FreeAgent keeps one source of truth for every date FreeAgent calculates.
4. A missing bank transaction for 7 days is the earliest sign that the bank feed has stopped and the books are falling behind.

---

## Consequences

- App 5 carries the FreeAgent connection, the deadline reminders, the bank feed check and the daily figures ([[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).
- The test suite tests the connection against a FreeAgent sandbox company and confirms that no write is made ([[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md)).

---

## Related Documents

- [[[default:adr-global/adr-company-compliance]]](C:/dev/project-library-global/adr-global/adr-company-compliance.md)
- [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)
- [[[default:specifications-global/spec-vault-system]]](C:/dev/project-library-global/specifications-global/spec-vault-system.md)
- [[[default:specifications-global/spec-integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md)
