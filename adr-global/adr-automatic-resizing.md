---
title: "adr-automatic-resizing"
doc-id: "mb-9773fcc7"
updated: "2026-11-17"
---
# Automatic Resizing

Status: Accepted

---

## Context

Each client instance runs in its own 1 GiB container on a Mybizz Hetzner application server, and every client's database sits in one Ubicloud managed PostgreSQL service shared by every Mybizz business. A busy client can outgrow its container, and Mybizz can outgrow the database service. The service runs with a standby from the first client and grows in size with the client count. Mybizz is run by one person who does not watch any supplier console, so the resizes must happen without David watching, and David must always know when one has happened.

---

## Decision

1. **Container resize.** When a client's container passes 80% memory use, App 5 raises that container from 1 GiB to 2 GiB through the server's provisioning runner; the container then takes two places on its server. 2 GiB is the largest container size App 5 may choose. A 2 GiB container that passes 80% memory use is not raised further: App 5 sends David an immediate message.

2. **Database stages.** The Ubicloud service has a standby throughout, and grows in three stages with the number of active clients of every Mybizz business together:

| Stage | From client | Service | Monthly cost | Action by App 5 |
|---|---|---|---|---|
| 1 | 1 | `standard-2` (8 GB), with a standby | £116.22 | Created at Mybizz's platform set-up |
| 2 | 60 | `standard-4` (16 GB), with a standby | £232.44 | Raises the size of the same service through Ubicloud's API |
| 3 | 130 | `standard-8` (32 GB), with a standby | £466.37 | Raises the size of the same service through Ubicloud's API |

   `standard-8` is the largest size App 5 may choose. Beyond 260 clients, David decides the next step.

3. **Timing.** A container resize runs as soon as the memory alert arrives; the container restarts on the new size. Each database stage runs in the service's weekly maintenance window, Sunday 06:00 UK time, after the client count reaches the stage. Each stage starts at least three clients before the current size is full, which leaves time for the maintenance window and for new clients signing up meanwhile.

4. **Storage.** App 5 messages David when the service's storage passes 80%, and David adds storage in Ubicloud.

5. **Notification.** Every resize is written to App 5's audit record with the client or the database service, the old size, the new size, the trigger and the time. App 5 sends David a message at each resize, and lists it in his daily summary.

6. **No automatic reduction.** App 5 never reduces a size. A reduction is David's decision.

---

## Rationale

1. A resize triggered by a measured threshold happens before clients notice slowness, and without David watching any console.
2. A largest size for each resize caps the cost App 5 can commit without David: a 2 GiB container takes one more place on a server, and the largest database stage costs £466.37 a month.
3. A standby from the first client means a database failure stops clients for minutes, not the hours a restore from backup takes.
4. Every stage raises the size of the same service, so no client moves as Mybizz grows.
5. Running every database stage in the maintenance window keeps any brief interruption at the quietest time of the week for every market Mybizz serves.
6. Never reducing automatically avoids a resize loop when use rises and falls around a threshold.

---

## Consequences

- App 5 holds a Ubicloud API key, used only to change the service's size, and reaches each server's containers through its provisioning runner ([[[default:security-global/cloud/sec-client-provisioning-security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md)).
- Container memory reaches App 5 from the provisioning runner's server report ([[[default:adr-global/adr-observability-architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).
- The test suite tests each resize decision against a simulated runner and a simulated Ubicloud API ([[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md)).
- The budget's escalation points follow this record (the Mybizz budget, `mybizz-live-budget.xlsx` in `data-mybizz-mgt\business\mybizz-live`).

---

## Related Documents

- [[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)
- [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)
- [[[default:specifications-global/spec-client-instance-hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)
