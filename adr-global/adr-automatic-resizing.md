---
title: "adr-automatic-resizing"
doc-id: "mb-9773fcc7"
updated: "2026-11-11"
---
# Automatic Resizing

Status: Accepted

---

## Context

Each client instance runs in its own 1 GiB container on DigitalOcean App Platform, and every client's database sits in one DigitalOcean Managed PostgreSQL cluster. A busy client can outgrow its container, and the business can outgrow the cluster's connection capacity. The cluster starts small, so that Mybizz breaks even at 7 clients, and grows with the client count. Mybizz is run by one person who does not watch the DigitalOcean console, so the resizes must happen without David watching, and David must always know when one has happened.

---

## Decision

1. **Container resize.** When a client's container passes 80% memory use, App 5 raises that container from 1 GiB to 2 GiB through the DigitalOcean API. 2 GiB is the largest container size App 5 may choose. A 2 GiB container that passes 80% memory use is not raised further: App 5 sends David an immediate message.

2. **Cluster stages.** The cluster grows in four stages with the number of active clients:

| Stage | From client | Cluster | Connections | Clients at 3 connections each | Action by App 5 |
|---|---|---|---|---|---|
| 1 | 1 | Standard Edition, 2 GiB, one node | 47 | 15 | Created at the business's platform set-up |
| 2 | 12 | Standard Edition, 4 GiB, one node | 97 | 32 | Raises the size of the same cluster |
| 3 | 25 | Advanced Edition, 8 GiB, with a standby | 197 | 65 | Messages David; once he approves, **Rebuild** creates the Advanced cluster and moves every client into it |
| 4 | 60 | Advanced Edition, 16 GiB, with a standby | 397 | 132 | Raises the size of the same cluster |

   16 GiB is the largest plan App 5 may choose.

3. **Timing.** A container resize runs as soon as the memory alert arrives; the container restarts on the new size. Each cluster stage runs in the cluster's weekly maintenance window, Sunday 06:00 UK time, after the client count reaches the stage. Each stage starts at least three clients before the current cluster is full, which leaves time for the maintenance window and for new clients signing up meanwhile.

4. **Storage.** The cluster's storage autoscaling, a DigitalOcean setting, adds storage before the disk fills. App 5 takes no action on storage.

5. **Notification.** Every resize is written to App 5's audit record with the client or cluster, the old size, the new size, the trigger and the time. App 5 sends David a message at each resize, and lists it in his daily summary.

6. **No automatic reduction.** App 5 never reduces a size. A reduction is David's decision.

---

## Rationale

1. A resize triggered by a measured threshold happens before clients notice slowness, and without David watching any console.
2. A largest size for each resize caps the cost App 5 can commit without David: a 2 GiB container costs £18.75 a month, and the 16 GiB cluster about £390.
3. Starting on a 2 GiB Standard cluster at £22.50 a month, rather than an Advanced cluster at £195, brings break-even down to 7 clients. The cost of the cluster then grows only as revenue grows.
4. A Standard cluster cannot have a standby, and its edition cannot be changed in place. The move to the Advanced cluster at client 25 therefore uses the **Rebuild** action, which is already built and tested for a region failure, and David approves it because it briefly interrupts every client. Until client 25 a node failure means an outage while DigitalOcean restores the cluster; few clients are exposed during that time.
5. Running every cluster stage in the maintenance window keeps any brief interruption at the quietest time of the week for every market Mybizz serves.
6. Never reducing automatically avoids a resize loop when use rises and falls around a threshold.

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
