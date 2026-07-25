---
document: Client Timezone: IANA String, UTC Storage, Display-Time Conversion
doc-id: global-0037
state: Live
date-created: 2026-07-25T160000+0200
---
# Client Timezone: IANA String, UTC Storage, Display-Time Conversion
Date: 2026-03-17
Status: Accepted
Source: cs-architectural-specification-D.md §13

---

## Context

Mybizz serves clients globally. Datetimes (bookings, reminders, invoices, activity
logs) must be meaningful to each client in their own local time. A decision was needed
on how to store and display datetimes across client instances with different timezones.

---

## Decision

**Each client instance configures its own timezone at onboarding**, stored as an IANA
timezone string (e.g. `'Africa/Johannesburg'`, `'Europe/London'`) in the
`business_profile` table (`timezone` field).

**All datetimes are stored in the database as UTC.**

**Conversion to the client's local timezone occurs at display time** in server
functions that return datetime data for UI presentation. Client code never handles
timezone conversion.

**The Mybizz platform itself** (devlog timestamps, build artefacts, reference
documents) uses UTC+2 (Africa/Johannesburg) — the developer's timezone. This applies
to build artefacts only, not to client data handling. Do not conflate the two.

### Practical implication for server functions

Any server function returning a datetime for display must convert from UTC to the
client's configured timezone before returning. The `timezone` value is read from
`business_profile` at the start of the function. A helper function for this conversion
should be centralised — not duplicated per function.

---

## Build Artefact Timestamp Format Standard

**Added 2026-07-25T160000+0200.** This section covers a different problem from the Decision above,
using a different mechanism — the two are not in conflict and do not replace one
another. The Decision above uses an **IANA timezone string** for client data because
an IANA string represents a *geographical region*, not a fixed offset — necessary
because a region's actual UTC offset changes with daylight saving, and different
clients are in different regions. This section covers only the developer's own
build artefacts — backups, logs, front matter, registers — all created on one PC, in
one place, where a **fixed UTC+2 offset** is correct and sufficient because there is
no region-dependent daylight-saving shift to account for. IANA strings are never used
for build-artefact timestamps; a fixed offset is never used for client data.

Applies to every timestamp recorded by Mybizz's own tooling —
front matter (`date-created`), registers, alignment logs, learnings entries, backup
folder names, devlog entries, and any other build artefact. Does not apply to client
data, which follows the Decision above.

**Format: Filename-Safe ISO 8601, UTC+2, with seconds.**

```
YYYY-MM-DDTHHMMSS+0200
```

Example: `2026-07-25T143045+0200`

- Date portion keeps hyphens (`YYYY-MM-DD`).
- Time portion drops colons (`HHMMSS`, not `HH:MM:SS`) — colons are invalid in
  Windows filenames and this format must work equally as a timestamp value and as
  part of a folder/file name.
- Timezone offset is always `+0200`, stated explicitly, never omitted — this system
  does not use UTC or "local time" as an implicit default; UTC+2 is stated on every
  timestamp so there is never ambiguity about which timezone a given value is in.
- Seconds are included even where minute-level precision would usually suffice, so
  that two artefacts created close together never collide on an identical timestamp.

### Rules files affected

| File | Required content |
|---|---|
| `spec_architecture.md` | Timezone architecture, UTC storage mandate, display-time conversion pattern |
| `spec_database.md` | `business_profile.timezone` field (IANA string) |
| `ref_anvil_coding.md` | Datetime handling — UTC storage rule, display-time conversion |
| AGENTS.md (global and per-project) | Build-artefact timestamp format standard — see above |

---

## Consequences

### Rules files affected

| File | Required content |
|---|---|
| `spec_architecture.md` | Timezone architecture, UTC storage mandate, display-time conversion pattern |
| `spec_database.md` | `business_profile.timezone` field (IANA string) |
| `ref_anvil_coding.md` | Datetime handling — UTC storage rule, display-time conversion |

---

*End of `timezone-utc-storage-display-conversion` ADR*
