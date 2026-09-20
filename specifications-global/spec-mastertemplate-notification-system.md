---
document: "`mastertemplate-notification-system` Spec — Notification Engine for Client Instances"
doc-id: spec-mastertemplate-notification-system
state: Draft
date-created: 2026-09-15
---

# `mastertemplate-notification-system` Spec — Notification Engine for Client Instances

**Status:** Draft — for review
**Lives in:** `master_template`, inherited by every `[client-name]-cs` instance via the standing dependency
**Depends on:** [[adr-client-instance-architecture|Client Instance Architecture]] ADR (Data Tables resolve per-instance; server modules and forms live only in `master_template`)
**Companion document:** [[spec-mybizz-management-app-notification-system|Platform-to-Client Notification Console]] (the platform-tier producer that calls into this engine — see §7)

---

## 1. Status

Draft. Not yet built. This spec is independently buildable now — it does not require `Mybizz_management` (App 5) to exist, since the platform-inbound endpoint (§6) can be built and left dormant until App 5 ships.

---

## 2. Context

Every client instance needs a way to send notifications to its own members/customers — order updates, account alerts, announcements, transactional messages. Because of the five-app architecture, this cannot be built per-client: client instances contain no server modules or forms of their own ([[adr-client-instance-architecture|Client Instance Architecture]] ADR). The entire notification system — schema, dispatch logic, and UI — must therefore live in `master_template` and be inherited automatically by every client instance, exactly like all other server logic and UI.

`app_tables` calls inside `master_template` server modules resolve to the calling client instance's own Data Tables (confirmed, Test A). This means one shared notification engine, written once, produces fully data-isolated results per client with no per-client code and no per-client deployment step.

This spec also reserves a second entry point (§6) so the same engine can receive notifications *from* the platform operator (via `Mybizz_management`, App 5) and render them through the identical in-app UI a client's own outbound notifications use — one rendering/delivery pipeline, two producers.

The original source design this spec is derived from (`Notification-System-Design.md`) targets a 50M-DAU, Kafka/Redis-backed system. That design is not appropriate at this platform's scale or on Anvil's infrastructure. §5.4 states explicitly what was kept and what was deliberately dropped, and why.

---

## 3. Scope

**In scope (v1):**
- In-app notification feed, per user, per client instance
- Email channel
- User-level preferences (per channel, per type, quiet hours, frequency caps)
- Idempotent sends (no duplicate delivery on retry)
- Delivery audit log
- Inbound endpoint to receive platform-origin notifications from `Mybizz_management`

**Out of scope (v1) — see §5.4 for rationale:**
- SMS, mobile push (FCM/APNs) — no mobile app exists yet; add as a channel later without schema changes
- True real-time push (WebSocket) — not natively available in Anvil; v1 uses polling (§8.5)
- Kafka, Redis, multi-region, fan-out strategy, priority-topic infrastructure — solving problems this platform does not have at its current or foreseeable scale

---

## 4. Architecture Overview

```
Client's own server logic (master_template)          Mybizz_management (App 5, future)
        │  send_notification()                                 │  HTTP POST (signed)
        ▼                                                       ▼
┌─────────────────────────────────────────────────────────────────┐
│  master_template: Notification Engine                            │
│                                                                    │
│   receive_platform_notification()  ◄──── inbound HTTP endpoint    │
│              │                                                    │
│              ▼                                                    │
│   notifications table (app_tables — resolves to calling instance) │
│              │                                                    │
│              ▼                                                    │
│   dispatch_notification()  [Background Task]                     │
│      ├─ checks user_preferences (channel/type/quiet hours/cap)    │
│      ├─ in-app: nothing further needed, row already visible       │
│      └─ email: calls anvil.email or external provider             │
│              │                                                    │
│              ▼                                                    │
│   delivery_logs table (audit trail, per instance)                │
└─────────────────────────────────────────────────────────────────┘
              │
              ▼
   In-app UI: bell + badge, feed, preferences center (§8)
```

Both producers — a client's own server code, and an inbound platform push — converge on the same `notifications` table and the same dispatch/UI code. They are distinguished only by the `source` field (§5.1). This is deliberate: one engine, one place to fix bugs, one UI to maintain.

---

## 5. Data Schema

All tables are Anvil Data Tables, created once in `blank_client_template` (App 3) so every newly provisioned client instance has them from day one. Per the [[adr-client-instance-architecture|Client Instance Architecture]] ADR, **schema changes do not propagate automatically** — any future column change must be applied manually to `blank_client_template` and to every existing client instance.

### 5.1 `notifications`

| Column | Type | Notes |
|---|---|---|
| `user_id` | Link to Users table | The recipient within this client instance |
| `source` | Text | `'client'` (sent by this client to their own user) or `'platform'` (received from `Mybizz_management`) |
| `type` | Text | e.g. `order.shipped`, `account.alert`, `platform.announcement` |
| `priority` | Text | `transactional` \| `social` \| `marketing` — same three tiers as the original design, minus the Kafka topic mapping |
| `title` | Text | |
| `body` | Text | |
| `data` | Simple Object (dict) | Arbitrary structured payload, e.g. `{"orderId": "...", "url": "..."}` |
| `is_read` | Boolean | Default `False` |
| `created_at` | Date/Time | Default now |
| `expires_at` | Date/Time | Nullable |
| `idempotency_key` | Text, indexed | See §5.5 |

### 5.2 `user_preferences`

| Column | Type | Notes |
|---|---|---|
| `user_id` | Link to Users table | |
| `channel` | Text | `inapp` \| `email` |
| `type` | Text | `transactional` \| `social` \| `marketing` |
| `enabled` | Boolean | Default `True` |
| `quiet_from` | Text (HH:MM) | Nullable |
| `quiet_to` | Text (HH:MM) | Nullable |
| `freq_cap` | Number | Max sends/day for this channel+type; `None` = unlimited |

Composite uniqueness on (`user_id`, `channel`, `type`) enforced in application code — Anvil Data Tables do not enforce composite unique constraints natively.

### 5.3 `delivery_logs`

| Column | Type | Notes |
|---|---|---|
| `notification` | Link to `notifications` row | |
| `channel` | Text | `inapp` \| `email` |
| `status` | Text | `pending` \| `sent` \| `delivered` \| `failed` |
| `attempts` | Number | Default 0 |
| `error` | Text | Nullable |
| `created_at` | Date/Time | Default now |

### 5.4 What was dropped from the source design, and why

| Dropped | Reason |
|---|---|
| `device_tokens` table, FCM/APNs dispatcher | No mobile app exists. Re-add this table and dispatcher unchanged if/when one ships — nothing else in this schema needs to change. |
| Kafka priority topics | Solves a queue-contention problem at 1M+ msg/sec. This platform's Background Tasks, called per-notification, do not have that contention problem at realistic client volumes. |
| Redis (caching, idempotency, rate limiting) | No Redis is available in Anvil without standing up an external service. The idempotency and preference-caching problems Redis solves are handled here with Data Table lookups instead — slower per-call, but adequate at this scale, and avoids taking on an external infrastructure dependency for v1. |
| WebSocket real-time server, fan-out strategy (push vs. pull for celebrity accounts) | Anvil has no general-purpose server-push mechanism to browser clients (confirmed against Anvil's own docs and community forum). There is no "celebrity account" fan-out problem on this platform. Real-time is handled by short-interval polling (§8.5) — sufficient for account/order-style notifications, not intended for chat-speed messaging. |
| Multi-region deployment | Single-region is sufficient at current and foreseeable scale. |

### 5.5 Idempotency

Before writing a notification, compute `idempotency_key = sha256(user_id + type + data.get('event_id', ''))`. Check for an existing `notifications` row with that key before inserting. This replaces the source design's Redis-backed 24h-TTL key store with a direct Data Table check — correct behavior, no external dependency, acceptable at this platform's write volume.

---

## 6. Server API (`master_template` server modules)

```python
@anvil.server.callable
def send_notification(user_id, type, priority, title, body, data=None, channels=('inapp',)):
    """Called by a client's own server-side logic (source='client').
    Writes the notification, checks idempotency, launches dispatch_notification
    as a Background Task."""

@anvil.server.http_endpoint("/platform-notification", methods=["POST"])
def receive_platform_notification():
    """Inbound endpoint for Mybizz_management. Validates the shared auth token
    (see spec-mybizz-management-app-notification-system.md §5) against this
    instance's stored secret before writing a notification with source='platform'.
    Rejects with 401 on auth failure. Idempotency check applies identically to
    client-origin sends."""

@anvil.server.callable
def get_notifications(cursor=None, limit=20):
    """Cursor-based pagination — WHERE created_at < cursor ORDER BY created_at
    DESC LIMIT :limit. Matches the source design's pagination fix (no offset
    pagination) exactly; the bug it prevents is not scale-dependent."""

@anvil.server.callable
def get_unread_count(user_id):
    """Backs the bell badge. A direct count query — at this platform's per-user
    notification volume, this does not need the source design's Redis
    INCR/DEL pattern."""

@anvil.server.callable
def mark_read(notification_id): ...

@anvil.server.callable
def mark_all_read(user_id): ...

@anvil.server.callable
def update_preferences(user_id, channel, type, enabled, quiet_from=None, quiet_to=None, freq_cap=None):
    """Upserts a user_preferences row."""
```

### Background / Scheduled Tasks

```python
@anvil.server.background_task
def dispatch_notification(notification_id):
    """Reads the notification, checks user_preferences (enabled, quiet hours,
    frequency cap) before each channel send — server-side enforcement only,
    matching the source design's failure-pattern lesson on quiet hours never
    being trusted client-side. Writes one delivery_logs row per channel
    attempted. On the Free Plan this task has a 30-second runtime cap — see
    §9.1."""

@anvil.server.background_task  # Scheduled Tasks require a paid plan
def process_scheduled_notifications():
    """For future-dated sends: polls for notifications whose send_at has
    arrived and dispatches them. Requires the Scheduled Tasks feature —
    flagged as a paid-plan dependency, see §9.1."""
```

---

## 7. Relationship to `Mybizz_management`

This engine does not call out to `Mybizz_management` — it only exposes `receive_platform_notification` as a passive inbound endpoint. All outbound logic (who to send to, retry-on-failure, send audit) lives in `Mybizz_management` and is specified in the companion document. This keeps the isolation boundary intact: `master_template` never needs visibility into other clients, and the only thing crossing the boundary is an authenticated HTTP call in one direction.

---

## 8. UI Design — Essential Elements

Anvil components map onto the source design's five frontend components closely enough to reuse the same names.

### 8.1 Bell Icon + Badge
- A `Link` or `Button` component styled as an icon, with a `Label` overlay bound to `get_unread_count()`.
- Refreshed on a `Timer` component (see §8.5), and on `form_show` of any form containing the bell.
- Click opens the notification feed panel/form.

### 8.2 Notification Feed
- A `RepeatingPanel` bound to `get_notifications(cursor)`, rendering a `NotificationCard` template component per row (title, body preview, relative timestamp, read/unread state).
- "Load more" button at the bottom calls `get_notifications` again with the last-seen `created_at` as cursor — no infinite-scroll library needed at this data volume; a manual "Load more" is sufficient and simpler to build correctly.

### 8.3 Toast / Alert
- Anvil already provides a native equivalent: `anvil.Notification(title, message, style=...).show()`. No custom component needed — this is a direct, better-than-source-design fit, since Anvil's built-in `Notification` already handles stacking and auto-dismiss.
- Suppress toasts for `priority == 'marketing'`, matching the source design's rule — only `transactional` and `social` priority notifications toast; everything else appears in the feed only.

### 8.4 Preferences Center
- A settings `Form` listing each (`channel`, `type`) pair as a `CheckBox`, plus `TextBox` fields for quiet hours.
- Optimistic update: flip the UI state immediately on toggle, call `update_preferences` in the background, revert the toggle and show an error `Notification` on failure — same pattern as the source design's rollback logic.

### 8.5 "Real-time" via Polling
- A `Timer` component (interval: 30–60s, tunable) on any form with a bell icon calls `get_unread_count()` and refreshes the badge.
- This is a deliberate, explicit substitution for the source design's WebSocket layer — see §5.4. It is not real-time in the sub-second sense; it is adequate for the notification types in scope (§3). If a future requirement needs true real-time (e.g. live chat), that is a distinct system and should not be retrofitted onto this one — flag as a new spec if it arises.

---

## 9. Open Questions / Dependencies

1. **Free Plan runtime caps.** `dispatch_notification` and `process_scheduled_notifications` both depend on Background/Scheduled Tasks running longer than the Free Plan's 30-second cap for anything beyond trivial volume. This spec assumes at least the Hobby Plan for Background Tasks and a Business-tier-or-above plan for Scheduled Tasks. Needs confirmation against current plan before build.
2. **Provisioning of the platform auth token.** `receive_platform_notification` requires a per-client shared secret to validate inbound calls. This must be generated and stored at provisioning time — an addition to `blank_client_template`'s provisioning process, and to the existing README ADR's scope. Not yet specced — should be a short addendum to [[spec-client-activation-runbook|Client Instance Activation Runbook]], not a new document.
3. **Email provider.** Not yet decided — Anvil's built-in Email Service is the default assumption; confirm whether a third-party provider (SendGrid etc.) is required for deliverability/volume reasons before build.

---

## 10. Related Documents

| Document | Relationship |
|---|---|
| [[spec-mybizz-management-app-notification-system|Platform-to-Client Notification Console]] | The platform-tier producer that calls `receive_platform_notification` |
| [[adr-client-instance-architecture|Client Instance Architecture]] | Basis for the app_tables-resolves-per-instance guarantee this design depends on |
| [[adr-client-instance-readme-five-app-system|Client Instance Readme Five App System]] | Governs where this code may and may not live |
| `Notification-System-Design.md` | Source design this spec derives from; §5.4 documents deviations |

---

*End of `mastertemplate-notification-system` spec*
