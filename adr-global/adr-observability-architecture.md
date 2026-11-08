---
title: "adr-observability-architecture"
doc-id: "mb-d5da852f"
updated: "2026-11-08"
---
# `observability-architecture` ADR — Observability Architecture

**Status:** Confirmed  

---

## Context

The platform requires visibility into the health, activity, and status of up to 100 client instances from a single operator view. External monitoring tools (Prometheus, Grafana) were considered.

### The Platforms' Own Monitoring

- **DigitalOcean**, for each client instance: the container's logs and its CPU and memory use, and the cluster's metrics ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)).
- **Anvil**, for Apps 1, 2, 3 and 5: App Logs, CPU and Memory Usage tabs, and Profiling and Tracing tools.

These tools are valuable for diagnosing individual app issues. They are not suitable as the primary monitoring solution for this platform because:

- They are **per-app** — viewing 100 client instances means opening 100 separate containers
- They provide **no view of the application's own health** — bookings, payments, background task results
- They have **no application-level alerting** — no notification when a client's payments fail or its heartbeat goes silent

---

## Decision

Client instance observability is achieved through **application-level metrics** written to each client's own Data Tables and pushed to Mybizz_management in its heartbeats.

Mybizz_management is the consolidated observability layer — the platform's equivalent of a monitoring dashboard.

### What Client Instances Write

Master_template includes server-side logic that writes key events and metrics to designated tables within the client instance:

| Event type | Trigger | Written to |
|---|---|---|
| Health heartbeat | Scheduled background task | `health_log` table |
| Background task completion/failure | On task end | `activity_log` table |
| Payment event | On payment success/failure | `activity_log` table |
| Vault access | On every Vault open | `activity_log` table (existing, [[[default:adr-global/adr-payment-security-boundary-vault\|Payment Security Boundary Vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) ADR) |
| Error threshold exceeded | On unhandled exception | `error_log` table |
| Session activity | On user login/logout | `activity_log` table |

### What Mybizz_management Displays

Each client instance pushes a heartbeat to Mybizz_management on a schedule, without blocking its own work; Mybizz_management never polls instances. Its HTTP endpoints on each instance (see [[[default:adr-global/adr-mybizz-management-visibility|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) ADR) remain for control and on-demand checks. From the heartbeats it presents:

- Last active timestamp per client
- Background task health (last run, success/failure)
- Error count and last error per client
- Subscription and billing status
- CPU and memory trend (from Anvil's per-app data, accessed via IDE or future API)

---

## Alternatives Rejected

| Alternative | Reason rejected |
|---|---|
| Prometheus + Grafana | External infrastructure; contradicts hosted simplicity; overkill for 100-client scale |
| Anvil App Logs (per-app) | No consolidated view; IDE-bound; no alerting |
| Manual per-app IDE monitoring | Not scalable at 100 clients; reactive not proactive |
| Third-party SaaS monitoring (Datadog, New Relic) | External dependency; cost; no native Anvil integration |

---

## Consequences

- ✅ Consolidated monitoring across all 100 client instances in one dashboard
- ✅ No external infrastructure or third-party monitoring subscriptions required
- ✅ Monitoring logic ships with master_template — all client instances monitored automatically
- ✅ DigitalOcean's per-container logs and metrics, and Anvil's tools on App 1, remain available for deep diagnostics when needed
- ⚠️ `health_log`, `error_log` and `activity_log` are part of every application's schema and of App 3's table definitions
- ⚠️ Heartbeat background task adds to per-client scheduled task load — must be accounted for in each client container's memory

---

## Relationship to Platform Tools

The platforms' own observability tools are not replaced — they are complementary:

| Tool | Use case |
|---|---|
| Mybizz_management dashboard | Day-to-day operational monitoring across all clients |
| DigitalOcean container logs | Deep diagnostic investigation of a specific client issue |
| DigitalOcean container and cluster metrics | Performance investigation of a specific client instance |
| Anvil App Logs, Profiling and Tracing on App 1 | Code-level bottleneck analysis during development |

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-payment-security-boundary-vault\|Payment Security Boundary Vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) | Audit log pattern (existing) extended by this ADR |
| [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) | HTTP endpoint mechanism by which management queries client metrics |

