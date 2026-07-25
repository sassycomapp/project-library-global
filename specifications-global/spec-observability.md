---
document: PDLF Standards Library — Observability Requirements
doc-id: global-0069
state: Live
date-created: 2026-07-25T150027+0200
---
# PDLF Standards Library — Observability Requirements

**Location:** `C:\dev\project-library-global\specifications-global\spec-observability.md`
**Scope:** Project-agnostic. Applies to any Anvil.works project requiring structured observability
using strictly Anvil-native facilities — no external monitoring infrastructure (Prometheus,
Grafana, Datadog).
**Source:** Extracted from mb-3-cs `observability-requirements.md`. Patterns validated against
Anvil.works platform constraints.

---

## 1. Application-Level Observability via Data Tables

Anvil-hosted deployments without access to external monitoring infrastructure use Anvil Data
Tables as the observability store. A management application queries these tables via HTTP
endpoints to produce consolidated dashboards — there is no separate metrics pipeline.

**Three canonical log tables:**

| Table | Purpose | Retention |
|---|---|---|
| `health_log` | Heartbeat pings, uptime indicators | Rolling window |
| `audit_log` | Business-level operation events (who did what, when) | Permanent |
| `error_log` | Uncaught exceptions, stack traces, error context | Rolling window |

All three are written by server functions only. No client-side code writes to log tables.

---

## 2. Structured Logging Standard for Anvil Server Functions

Every server function logs using Python's `logging.getLogger(__name__)`. Messages use
JSON-structured format with these required fields:

| Field | Type | Description |
|---|---|---|
| `timestamp` | ISO 8601 | When the event occurred |
| `level` | string | DEBUG / INFO / WARNING / ERROR / CRITICAL |
| `function` | string | `__name__` of the calling server function |
| `error_type` | string | Exception class name (empty for non-error) |
| `error_message` | string | Exception message (empty for non-error) |
| `user_id` | string | `anvil.users.get_user()` identifier |
| `request_id` | string | UUID generated per request for correlation |

**Additional rules:**
- Log function entry and exit at DEBUG level (including arguments for entry)
- Log any external API call at INFO level (including duration)
- Log any caught-then-re-raised exception at ERROR level
- Do NOT log user credentials, API keys, or PII in any log message

---

## 3. Pre-Computed Business Metrics in Summary Tables

Anvil Data Tables do not support complex aggregation queries (GROUP BY, SUM across large
row sets with acceptable performance). Complex business metrics are computed by scheduled
background tasks and stored in summary Data Tables.

**Pattern:**

1. A Scheduled Task runs at the required interval (hourly, daily)
2. The task queries source tables, performs aggregation server-side
3. Results are written to a summary table (`daily_metrics`, `service_performance`, etc.)
4. Dashboards and reports read from the summary table — never compute on-demand

**Example:** Daily revenue is not queried from `appointments` joined with `payments` on
every dashboard load. A daily task computes `daily_revenue` and writes one row to
`daily_metrics`. The dashboard reads a single pre-computed row.

---

*Observability specification version 1.0. Extracted from mb-3-cs observability-requirements.md.
Anvil-native only — no external monitoring tools required.*
