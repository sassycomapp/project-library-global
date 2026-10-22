---
title: "adr-mybizz-management-visibility"
doc-id: "mb-1962f48d"
updated: "2026-10-22"
---
# `mybizz-management-visibility` ADR — Mybizz_management Visibility and Control

**Status:** Confirmed  
**Date:** 2026-06-13  
**Authority:** Derived from the retired platform-overview.md, [[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md) ADR

---

## Context

Mybizz_management requires three capabilities with respect to client instances:

1. **Read** — health metrics, last active, error counts, billing status, background task health
2. **Write and Control** — push notifications, suspend accounts, trigger configuration changes, push update alerts
3. **Receive events** — payment failures, background task errors, Vault access alerts, error thresholds

All client instances are separate Anvil apps on the same mybizz account. Anvil provides no native cross-app data access outside of the dependency model. Mybizz_management cannot depend on each client instance (inverse of the intended dependency direction), and client instances cannot depend on Mybizz_management (circular, and architecturally wrong).

---

## Decision

Communication between Mybizz_management and client instances is via **bidirectional HTTP endpoints**, secured with per-client Bearer tokens. Three communication patterns are implemented.

---

## Communication Pattern 1 — Mybizz_management → Client Instance

**Used for:** On-demand data reads, control actions, push notifications

Master_template includes a `server_modules/management_endpoints.py` module that exposes secured HTTP endpoints. These ship with every client instance automatically.

```
GET  /management/health           → returns health metrics, last active, error summary
GET  /management/status           → returns subscription status, feature flags
POST /management/suspend          → writes suspended flag to client tables
POST /management/unsuspend        → clears suspended flag
POST /management/push-notification → writes notification row to client notifications table
POST /management/push-update-alert → writes update available notice to client tables
```

**Authentication:** Each request must include a Bearer token in the `Authorization` header. The token is validated against a value stored in the client instance's management configuration. Requests without a valid token are rejected with HTTP 403.

**Triggered by:** Mybizz_management UI (operator actions) and on-demand checks.

---

## Communication Pattern 2 — Client Instance → Mybizz_management

**Used for:** Event push — payment failures, background task errors, error threshold exceeded, Vault access

Mybizz_management exposes an event receiver HTTP endpoint:

```
POST /events/receive  → logs incoming client event to Mybizz_management event table
```

Master_template's server modules call this endpoint when key events occur. The call is non-blocking — it fires and does not wait for a response so that the client instance's own processing is not delayed.

**Authentication:** Each client instance includes a shared event push token (stored in its Vault or management configuration). Mybizz_management validates this token on receipt.

**Events pushed:**
- Payment success / failure
- Background task failure
- Unhandled exception (error threshold)
- Vault access (every occurrence)
- Client suspension trigger (e.g. subscription lapsed)

---

## Communication Pattern 3 — Heartbeat Push

**Used for:** Proactive health monitoring across all client instances

Each client instance runs a scheduled background task, every 15 minutes, that sends its health summary (the same content as `/management/health`) to Mybizz_management's event receiver, without blocking its own work. Mybizz_management never polls instances. It stores each heartbeat in its client registry table, and a client whose heartbeat is more than 45 minutes old triggers an operator alert.

---

## Security Model

| Direction | Token type | Stored in |
|---|---|---|
| Mybizz → Client | Per-client Bearer token (unique per instance) | Mybizz_management client registry (encrypted) |
| Client → Mybizz | Shared event push token | Each client instance Vault |

Per-client tokens ensure that compromise of one client instance does not affect any other. Token generation is part of the client activation process (see [[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)).

---

## Client Registry

Mybizz_management maintains a client registry table containing:

| Field | Purpose |
|---|---|
| `client_id` | Unique identifier |
| `app_name` | Anvil app name |
| `base_url` | Client instance HTTP endpoint base URL |
| `management_token` | Encrypted Bearer token for management calls |
| `subscription_status` | Active / suspended / churned |
| `plan` | Pricing tier |
| `onboarded_date` | Activation date |
| `last_health_check` | Timestamp of the last heartbeat received |
| `last_active` | Last user session timestamp (from health endpoint) |

---

## Alternatives Rejected

| Alternative | Reason rejected |
|---|---|
| Shared hub app | Single point of failure across all clients; all clients depend on hub availability |
| Anvil Uplink | Designed for external Python processes connecting to Anvil; not Anvil-to-Anvil |
| Dependency model (reverse) | Mybizz_management depending on client instances is architecturally inverted |
| IDE log monitoring | Per-app only; not scalable; no alerting; operator must log in per app |

---

## Implementation Timing

Mybizz_management is deferred — it will be built after master_template reaches launch readiness and the first client has been manually onboarded. However, **the management endpoint module in master_template must be built as part of the initial template**, so that all client instances provisioned from day one already have the endpoints in place.

Until Mybizz_management is built, the operator uses Anvil's IDE-level tools for per-app monitoring and management.

---

## Consequences

- ✅ Full read, write, and control capability across all client instances from Mybizz_management
- ✅ Event-driven visibility without polling latency for critical events
- ✅ Per-client token isolation — security boundary between client instances
- ✅ Management endpoints ship automatically with every client instance via master_template
- ⚠️ Mybizz_management must store and manage per-client auth tokens securely
- ⚠️ HTTP endpoint base URLs must be captured at provisioning and stored in client registry
- ⚠️ Management endpoint module adds surface area to master_template — must be secured rigorously
- ⚠️ Event push calls from client instances to Mybizz_management assume Mybizz_management is running — failure handling must be non-blocking

---

## Additions to Client Activation Runbook

The following steps are added to the provisioning process:

- Generate unique management Bearer token for the new client instance
- Store token in Mybizz_management client registry (encrypted)
- Store token in client instance management configuration
- Record client instance base URL in Mybizz_management client registry
- Verify management endpoint responds correctly before completing activation

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-observability-architecture\|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md) | Defines what metrics are written and queried |
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | Confirms server modules (including management endpoints) live in master_template |
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Token generation and registry steps |

---

*End of `mybizz-management-visibility` ADR*
