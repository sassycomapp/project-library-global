---
title: "adr-timezone-utc-storage-display-conversion"
doc-id: "mb-5ba3ccea"
updated: "2026-10-23"
---
# Client Timezone: IANA String, UTC Storage, Display-Time Conversion
Status: Accepted

---

## Context

Mybizz serves clients globally. Datetimes (bookings, reminders, invoices, activity
logs) must be meaningful to each client in their own local time. This decision sets
how datetimes are stored and displayed across client instances in different timezones.

---

## Decision

**Each client instance configures its own timezone at onboarding**, stored as an IANA
timezone string (e.g. `'Africa/Johannesburg'`, `'Europe/London'`) in the
`business_profile` table (`timezone` field).

**All datetimes are stored in the database as UTC.**

**Conversion to the client's local timezone occurs at display time** in server
functions that return datetime data for UI presentation. Client code never handles
timezone conversion.

### Practical implication for server functions

Any server function returning a datetime for display must convert from UTC to the
client's configured timezone before returning. The `timezone` value is read from
`business_profile` at the start of the function. A helper function for this conversion
should be centralised — not duplicated per function.

---

## Consequences

- Every datetime column holds UTC.
- `business_profile.timezone` holds the client's IANA timezone string, set at onboarding.
- One central server helper converts UTC to the client's timezone for display; client code never converts.
