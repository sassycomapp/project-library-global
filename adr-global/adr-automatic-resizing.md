---
title: "adr-automatic-resizing"
doc-id: "mb-9773fcc7"
updated: "2026-11-11"
---
# Automatic Resizing

Status: Accepted

---

## Context

Each client instance runs in its own 1 GiB container on DigitalOcean App Platform, and every client's database sits in one DigitalOcean Managed PostgreSQL cluster with a standby. A busy client can outgrow its container, and the business can outgrow the cluster's connection capacity. Mybizz is run by one person who does not watch the DigitalOcean console, so both resizes must happen without David acting, and David must always know when one has happened.

---

## Decision

1. **Container resize.** When a client's container passes 80% memory use, App 5 raises that container from 1 GiB to 2 GiB through the DigitalOcean API. 2 GiB is the largest container size App 5 may choose. A 2 GiB container that passes 80% memory use is not raised further: App 5 sends David an immediate message.

2. **Cluster resize.** When the number of active clients reaches 60, App 5 raises the database cluster, with its standby, from the 8 GiB plan to the 16 GiB plan through the DigitalOcean API. 16 GiB is the largest plan App 5 may choose.

| Plan | Connections | Clients at 3 connections each |
|---|---|---|
| 8 GiB | 197 | 65 |
| 16 GiB | 397 | 132 |

3. **Timing.** A container resize runs as soon as the memory alert arrives; the container restarts on the new size. A cluster resize runs in the cluster's weekly maintenance window, Sunday 06:00 UK time, after the client count reaches 60. The raise at 60 leaves headroom of five clients on the 8 GiB plan until it runs.

4. **Storage.** The cluster's storage autoscaling, a DigitalOcean setting, adds storage before the disk fills. App 5 takes no action on storage.

5. **Notification.** Every resize is written to App 5's audit record with the client or cluster, the old size, the new size, the trigger and the time. App 5 sends David a message at each resize, and lists it in his daily summary.

6. **No automatic reduction.** App 5 never reduces a size. A reduction is David's decision.

---

## Rationale

1. A resize triggered by a measured threshold happens before clients notice slowness, and without David watching any console.
2. A largest size for each resize caps the cost App 5 can commit without David: a 2 GiB container costs £18.75 a month, and the 16 GiB cluster about £390.
3. Raising the cluster at 60 clients, five below the 8 GiB plan's limit of 65, leaves time for the maintenance window and for new clients signing up meanwhile.
4. Running the cluster resize in the maintenance window keeps any brief interruption at the quietest time of the week for every market Mybizz serves.
5. Never reducing automatically avoids a resize loop when use rises and falls around a threshold.

---

## Consequences

- App 5 holds a DigitalOcean access key whose scope allows updating apps and databases ([[[default:security-global/cloud/sec-client-provisioning-security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md)).
- Container memory reaches App 5 from DigitalOcean's metrics ([[[default:adr-global/adr-observability-architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).
- The test suite tests each resize decision against a simulated DigitalOcean API ([[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md)).
- The budget's escalation points follow this record (the Mybizz budget, `Budget.md` in `data-mybizz-mgt`).

---

## Related Documents

- [[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)
- [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)
- [[[default:specifications-global/spec-client-instance-hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)
