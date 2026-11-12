---
title: "adr-mybizz-management-visibility"
doc-id: "mb-1962f48d"
updated: "2026-11-12"
---
# `mybizz-management-visibility` ADR — Mybizz_management Visibility and Control

**Status:** Confirmed  

---

## Context

Mybizz_management requires three capabilities with respect to client instances:

1. **Read** — health metrics, last active, error counts, billing status, background task health
2. **Write and Control** — push notifications, suspend accounts, trigger configuration changes, push update alerts
3. **Receive events** — payment failures, background task errors, Vault access alerts, error thresholds

Every client instance is a separate Anvil App Server with its own database ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)). Anvil provides no native cross-app data access outside of the dependency model. Mybizz_management cannot depend on each client instance (inverse of the intended dependency direction), and client instances cannot depend on Mybizz_management (circular, and architecturally wrong).

---

## Decision

Communication between Mybizz_management and client instances is via **bidirectional HTTP endpoints**, secured with per-client Bearer tokens. Three communication patterns are implemented.

The client instances' containers and databases are created, released to and removed by Mybizz_management through the DigitalOcean API, with two access keys of custom scope (see Operations Automation below) ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) sections 6 to 8). The application itself is reached only through the endpoints below.

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
POST /management/plan-summary     → writes the plan, the next renewal preview and the referrals to the client's plan_summary table
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
- Payment success / failure in the client's own payment gateway
- Background task failure
- Unhandled exception (error threshold)
- Vault access (every occurrence)

---

## Communication Pattern 3 — Heartbeat Push

**Used for:** Proactive health monitoring across all client instances

Each client instance runs a scheduled background task, every 15 minutes, that sends its health summary (the same content as `/management/health`) to Mybizz_management's event receiver, without blocking its own work. Mybizz_management never polls instances. It stores each heartbeat in its client registry table, and a client whose heartbeat is more than 30 minutes old triggers an operator alert. The heartbeat carries the client's database size and its AI and voice spend for the month.

---

## Subscription Billing

Mybizz_management learns of every subscription payment from Paddle, not from the client instance. Paddle's notifications reach Mybizz_management's endpoint `/_/api/paddle`; Mybizz_management stores each one in Mybizz's R2 bucket, updates the client registry, suspends a client 7 days after a failed payment, unsuspends it when it pays, and runs the client exit 37 days after the failed payment ([[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) sections 4 and 5).

---

## Operations Automation

Mybizz is run by one person who does not watch supplier consoles. Every recurring operation is carried out by Mybizz_management or by a scheduled job, and Mybizz_management tells the developer what happened.

### DigitalOcean access

Mybizz_management holds two DigitalOcean access keys with custom scopes, in its Vault ([[[default:security-global/cloud/sec-client-provisioning-security|Client Provisioning Security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md)):

| Key | Scope | Used by |
|---|---|---|
| Automatic-tasks key | Read and update apps and databases | Scheduled checks, both resize actions, **Release**, **Suspend** |
| Provisioning key | Create and delete apps and databases | **New client**, **Remove** and **Rebuild** only |

### Scheduled checks

| Check | Frequency | Action |
|---|---|---|
| Heartbeat age | Continuous | An active client whose heartbeat is more than 30 minutes old makes the status endpoint report a fault. Suspended and exited clients are excluded |
| Container memory | On each DigitalOcean memory alert | The container resize of [[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md) |
| Client count | Daily | The cluster stages of [[[default:adr-global/adr-automatic-resizing]]](C:/dev/project-library-global/adr-global/adr-automatic-resizing.md): 16 GiB at client 60 and 32 GiB at client 130. At client 20 Mybizz_management messages the developer to engage part-time support, after buying employers' liability insurance. At client 25 Mybizz_management reminds the developer to raise the insurance covers ([[[default:adr-global/adr-business-insurance]]](C:/dev/project-library-global/adr-global/adr-business-insurance.md)) |
| Fair-use limits | Continuous, and daily for sizes and monthly totals | Each limit of [[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md) measured and enforced |
| Backup check | Daily | Each client's nightly copy checked for arrival, date and size |
| Restore drill | Monthly | Scheduled on the test client instance; the result is reported back |
| Domain and certificate check | Daily | Each client domain checked for resolution, certificate validity and registration expiry; the client is warned 30 days before expiry |
| Image findings | On each scan report | The 14-day countdown on each high or critical finding, with messages on days 7 and 10 ([[[default:adr-global/adr-dependency-update-model\|Dependency Update Model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md)) |
| Access key expiry | Daily | Rotation instructions sent 14 days before each DigitalOcean key expires |
| Company deadlines | Daily | Every tax and accounts deadline read from FreeAgent's tax timeline ([[[default:adr-global/adr-freeagent-integration]]](C:/dev/project-library-global/adr-global/adr-freeagent-integration.md)), plus the confirmation statement date held in Mybizz_management; a reminder 30 days before each one ([[[default:adr-global/adr-company-compliance]]](C:/dev/project-library-global/adr-global/adr-company-compliance.md)) |
| Wise bank feed | Daily | A message when no Wise transaction has reached FreeAgent for 7 days; a reminder 7 days before each 90-day consent ends |
| Cyber Essentials certificate | Daily | A reminder 60 days before expiry ([[[default:security-global/compliance/sec-cyber-essentials-compliance]]](C:/dev/project-library-global/security-global/compliance/sec-cyber-essentials-compliance.md)) |
| Business insurance | Daily | A reminder 30 days before the policy expires ([[[default:adr-global/adr-business-insurance]]](C:/dev/project-library-global/adr-global/adr-business-insurance.md)) |

### Actions

- **New client**, **Release** and **Remove**, as [[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) sections 6 to 8 set out. **Release** stages every release: test client instance, 10% of clients, all clients, with a health check and automatic rollback at each stage, and releases only an image whose signature verifies.
- **Suspend**: stops one client's container and records the reason, for an abuse report or a breach of the acceptable-use terms ([[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)). Distinct from the payment suspension through `/management/suspend`, which keeps the container running.
- **Rebuild**: restores every client of the business into a new cluster and new containers in another DigitalOcean region ([[[default:specifications-global/spec-deployment|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md)).

### Status endpoint

Mybizz_management publishes a status endpoint that reports a fault when Mybizz_management itself fails or when any heartbeat check fails. DigitalOcean Uptime checks it every minute and emails the developer, so a stopped Mybizz_management is noticed even though it is the system that does the noticing ([[[default:adr-global/adr-observability-architecture|Observability Architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md)).

### Incident record

Each security incident is recorded in Mybizz_management with its timeline: detected, contained, insurer called, Information Commissioner's Office reported (within 72 hours of a personal data breach), clients notified. The incident response plan of each business sets the order of these steps.

### Audit record and messages

- Every automatic action, every warning and every limit reached is written to Mybizz_management's audit record, with the client, the trigger, the action and the time.
- The developer receives one daily summary of routine actions, including Mybizz-Live Ltd's monthly income and costs read from FreeAgent, and an immediate message for anything that needs his decision.

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
| `plan` | Monthly (£119 a month) or annual (£1,190 a year), or the fixed price in the client's currency ([[[default:adr-global/adr-tiers-model\|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md)) |
| `assisted_setup` | Whether the client bought assisted setup |
| `referral_code` | The client's own referral code, issued when the client starts the annual plan; its link is `https://mybizz.live/r/{code}` |
| `referred_by` | The `client_id` of the annual client whose code the client entered at registration |
| `paddle_customer_id`, `paddle_subscription_id` | The client's customer and subscription in Paddle |
| `paid_until` | The end of the period the client has paid for |
| `payment_failed_at` | The date of the first failed renewal payment; empty when the client is paid up |
| `onboarded_date` | Activation date |
| `last_health_check` | Timestamp of the last heartbeat received |
| `last_active` | Last user session timestamp (from health endpoint) |
| `container_size` | 1 GiB or 2 GiB |
| `database_size` | The client database's size, from the last heartbeat |
| `ai_spend_month` | The client's AI and voice spend this month, from the last heartbeat |

Mybizz_management also keeps a `referrals` table, one row per referral: `referrer_id` and `referred_id` (each a `client_id`), `state` (`pending`, `confirmed`, `used` or `void`), `registered_at`, `confirmed_at` and `used_at`. The states and the rules for credits are in [[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) section 4.1.

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

Mybizz_management (App 5) is built before launch, with master_template: it provisions every client instance, so no client is onboarded without it. The management endpoint module ships in master_template from the first release, so every client instance has the endpoints from day one.

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
| [[[default:specifications-global/spec-client-billing\|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) | Paddle's notifications, suspension and exit for non-payment |

