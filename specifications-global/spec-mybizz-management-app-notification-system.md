---
title: "spec-mybizz-management-app-notification-system"
doc-id: "mb-631f063d"
updated: "2026-11-01"
---
# `mybizz-management-app-notification-system` Spec — Platform-to-Client Notification Console

**Status:** Accepted
**Lives in:** `Mybizz_management` (App 5, built before launch)
**Depends on:** [[[default:specifications-global/spec-mastertemplate-notification-system|Notification Engine for Client Instances]]](C:/dev/project-library-global/specifications-global/spec-mastertemplate-notification-system.md) (the receiving engine this console calls into)

---

## 1. Status

Built with Mybizz_management (App 5), before launch. Its provisioning step (§5) is part of the Client Instance Activation Runbook.

---

## 2. Context

You, as platform operator, need to communicate with your paying clients — billing notices, platform announcements, incident notifications, onboarding nudges. This is structurally distinct from a client's own outbound notifications to their members/customers (covered by [[[default:specifications-global/spec-mastertemplate-notification-system|Notification Engine for Client Instances]]](C:/dev/project-library-global/specifications-global/spec-mastertemplate-notification-system.md)): it must originate from a single point with visibility across all clients, which `Mybizz_management` is the only app positioned to have.

`Mybizz_management` is **not** a dependency of client instances and client instances are **not** dependencies of it — there is no `app_tables` resolution path between them, unlike the `master_template` → client-instance relationship. Reaching a specific client instance's data from `Mybizz_management` therefore requires an explicit, authenticated network call, not an in-process function call. This spec treats that as a deliberate, structural boundary to be crossed narrowly and auditable — not a gap to be papered over.

Rather than build a second, separate notification-rendering system inside each client instance for platform messages, this design reuses the client's own in-app notification feed, bell, and preferences UI (already specified in [[[default:specifications-global/spec-mastertemplate-notification-system|Notification Engine for Client Instances]]](C:/dev/project-library-global/specifications-global/spec-mastertemplate-notification-system.md)) as the display layer. `Mybizz_management`'s job is narrower than the source `Notification-System-Design.md` implies: it is a **producer and sender**, not a renderer. It composes a message, decides who receives it, and pushes it across the boundary — the client instance's own inherited engine takes it from there.

---

## 3. Scope

**In scope (v1):**
- Compose a notification (title, body, priority, optional structured data)
- Target: a single client, a selected subset, or broadcast to all active clients
- Immediate or scheduled send
- Per-client delivery audit (did the push succeed, retry status)
- A registry of client instances and their inbound endpoint credentials

**Out of scope (v1):**
- Any UI or logic for rendering the notification — that is `master_template`'s job, inherited by the client instance, not duplicated here
- Two-way messaging (clients replying to the platform through this system) — a distinct feature, not specced here
- SMS/push to the platform operator's own clients — email + in-app only, matching [[[default:specifications-global/spec-mastertemplate-notification-system|Notification Engine for Client Instances]]](C:/dev/project-library-global/specifications-global/spec-mastertemplate-notification-system.md)'s scope

---

## 4. Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│  Mybizz_management                                            │
│                                                                 │
│   Compose UI (§7) ──► send_platform_notification()             │
│                              │                                 │
│                              ▼                                 │
│                     client_registry table (§5.1)               │
│                     resolves target(s) → endpoint URL + secret │
│                              │                                 │
│                              ▼                                 │
│              [Background Task] push_to_client(client_id, ...)  │
│                              │                                 │
│                              │  signed HTTPS POST               │
│                              ▼                                 │
│      master_template's receive_platform_notification()         │
│         (running inside the target client instance)             │
│                              │                                 │
│                              ▼                                 │
│                platform_delivery_logs table (§5.2)             │
│                  (Mybizz_management's own audit copy —          │
│                   it cannot see the client's delivery_logs)     │
└─────────────────────────────────────────────────────────────┘
```

The push is one-directional and stateless from the client instance's point of view — it is just another caller of `receive_platform_notification`, authenticated the same way any inbound HTTP call would be. `Mybizz_management` does not read anything back from the client instance; success/failure is determined entirely from the HTTP response to its own POST.

---

## 5. Data Schema

All tables below are Anvil Data Tables local to `Mybizz_management` — they are never shared with, or visible to, any client instance.

### 5.1 `client_registry`

| Column | Type | Notes |
|---|---|---|
| `client_id` | Text, unique | Matches the client instance's slug/identifier |
| `client_name` | Text | Display name for the compose UI |
| `endpoint_url` | Text | The client instance's `receive_platform_notification` HTTP endpoint URL |
| `auth_token` | Text, encrypted | The client instance's management Bearer token, validated by the client instance on receipt |
| `status` | Text | `active` \| `inactive` \| `provisioning` |
| `created_at` | Date/Time | |

**Provisioning dependency:** every row here must be created at the same time a client instance is provisioned via `blank_client_template`, and the same `auth_token` value must be written into that client instance's own stored secret so the two sides agree. This is the management token step of the [[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) (Step 6).

### 5.2 `platform_delivery_logs`

| Column | Type | Notes |
|---|---|---|
| `client_id` | Text | |
| `notification_batch_id` | Text | Groups one compose-and-send action across multiple target clients |
| `http_status` | Number | Nullable until attempted |
| `attempts` | Number | Default 0 |
| `error` | Text | Nullable |
| `sent_at` | Date/Time | |

This is `Mybizz_management`'s own send-side audit trail — deliberately separate from, and not reconciled against, each client instance's `delivery_logs` table, since the two apps cannot see each other's Data Tables. If end-to-end confirmation (platform sent → client instance actually stored it) is ever required, that needs a follow-up acknowledgment call from the client instance back to `Mybizz_management`, which is not in v1 scope.

### 5.3 `sent_notifications`

| Column | Type | Notes |
|---|---|---|
| `batch_id` | Text | |
| `title` | Text | |
| `body` | Text | |
| `priority` | Text | |
| `target_type` | Text | `single` \| `subset` \| `broadcast` |
| `scheduled_for` | Date/Time | Nullable — immediate if empty |
| `created_by` | Text | Which operator/admin sent it |
| `created_at` | Date/Time | |

The composed message itself, independent of per-client delivery status — lets you see what was sent without cross-referencing every `platform_delivery_logs` row.

---

## 6. Server API (`Mybizz_management` server modules)

```python
@anvil.server.callable
def send_platform_notification(target_type, target_ids, title, body, priority, scheduled_for=None):
    """target_type: 'single' | 'subset' | 'broadcast'. Writes one sent_notifications
    row, resolves target client_ids against client_registry (status='active' only),
    then launches push_to_client as a Background Task per target — matching the
    source design's principle of never letting a slow/failed send block the caller."""

@anvil.server.background_task
def push_to_client(client_id, notification_payload):
    """Looks up endpoint_url + auth_token from client_registry, POSTs the signed
    payload to receive_platform_notification, writes one platform_delivery_logs
    row with the result. Retries on 5xx/timeout with backoff (1s → 2s → 4s),
    same pattern as the source design's dispatcher retry logic. Background
    tasks have no runtime cap on the Business plan."""

@anvil.server.background_task  # run by a Scheduled Task
def process_scheduled_platform_notifications():
    """Polls sent_notifications for rows whose scheduled_for has arrived and have
    not yet been pushed, and launches push_to_client for each resolved target."""

@anvil.server.callable
def get_delivery_status(batch_id):
    """Returns per-client delivery status for a given sent batch — backs the
    compose UI's confirmation/audit view (§7.3)."""
```

---

## 7. UI Design — Essential Elements

### 7.1 Compose Form
- Title/body text fields, a priority dropdown (`transactional` / `social` / `marketing` — same three tiers as the client-facing system, for consistency of meaning across both tiers)
- Target selector: radio choice of Single client (searchable dropdown from `client_registry`) / Subset (multi-select) / Broadcast (all `active`)
- Optional schedule picker (date/time) — leaves `scheduled_for` empty for immediate send
- Send button calls `send_platform_notification`; shows a confirmation `Notification` (Anvil's built-in toast) on successful queueing — not on successful delivery, since delivery is async

### 7.2 Client Registry Management
- A simple table view (`DataGrid` bound to `client_registry`) for adding/editing/deactivating client endpoint entries
- This is an internal admin tool, not client-facing — no design polish required beyond functional clarity

### 7.3 Delivery Status View
- Given a `batch_id` (from `sent_notifications`), a `RepeatingPanel` bound to `get_delivery_status` showing each targeted client, its `http_status`, and `attempts` — lets you see at a glance which clients did not receive a broadcast and why
- Not real-time (same polling caveat as the companion spec, §8.5 there) — a manual "Refresh" button is sufficient here, since this is an admin-facing status check, not a user-facing feed

---

## 8. What Was Deliberately Not Built

Consistent with [[[default:specifications-global/spec-mastertemplate-notification-system|Notification Engine for Client Instances]]](C:/dev/project-library-global/specifications-global/spec-mastertemplate-notification-system.md) §5.4: no Kafka, no Redis, no multi-region, no fan-out strategy. The additional simplification specific to this tier: **no shared rendering system between the two apps.** `Mybizz_management` only sends; it never renders a notification for an end user to see. This avoids duplicating the bell/feed/preferences UI work done in `master_template`, and keeps the isolation boundary narrow — one authenticated HTTP call per client, nothing else crosses it.

---

## 9. Dependencies

1. **Build order.** This console is built with Mybizz_management, before launch.
2. **Provisioning.** The `client_registry` row and the instance's matching token are created together at provisioning (Activation Runbook, Step 6).
3. **Auth token storage.** The token is the client instance's management Bearer token, generated at provisioning ([[[default:specifications-global/spec-client-activation-runbook|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md), Step 6), held encrypted in the Mybizz_management client registry and in the instance's Vault.
4. **Broadcast volume.** A broadcast launches one background task per client; Business plan background tasks have no runtime cap, so volume grows with client count without a per-task limit.

---

## 10. Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-mastertemplate-notification-system\|Notification Engine for Client Instances]]](C:/dev/project-library-global/specifications-global/spec-mastertemplate-notification-system.md) | The receiving engine and shared UI this console pushes into |
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | Basis for why this app cannot use `app_tables` to reach client data directly |
| [[[default:adr-global/adr-client-instance-readme-five-app-system\|Client Instance Readme Five App System]]](C:/dev/project-library-global/adr-global/adr-client-instance-readme-five-app-system.md) | The five-app boundary this spec respects |
| `Notification-System-Design.md` | Source design; §8 of this document records what was deliberately not carried over |

