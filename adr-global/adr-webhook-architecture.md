---
title: "adr-webhook-architecture"
doc-id: "mb-d4254987"
updated: "2026-10-23"
---
# `webhook-architecture` ADR — Webhook Architecture

**Status:** Accepted

---

## Context

Three external services POST webhooks to client instances:

| Service | Events | Criticality |
|---------|--------|-------------|
| Stripe | `payment_intent.succeeded`, `payment_intent.payment_failed`, subscription updates | High — payment status must be accurate |
| Paystack | `charge.success`, `subscription.disable`, `invoice.payment_failed` | High — payment status must be accurate |
| Brevo | Open tracking, click tracking, unsubscribe events | Medium — campaign analytics |

Each client instance is a separate Anvil app with a separate URL. Webhook URLs are:
- Stripe: `[base_url]/_/api/webhooks/stripe`
- Paystack: `[base_url]/_/api/webhooks/paystack`
- Brevo: `[base_url]/_/api/webhooks/brevo`

**Critical constraint:** Gateway webhook handlers must return HTTP 200 within a few seconds or the gateway times out and retries. Processing must be deferred.

---

## Decision

### One pattern for every webhook

Every webhook handler does exactly this, in this order:

1. **Validate** the signature against the raw request body. An invalid signature returns HTTP 400 and nothing else happens.
2. **Check idempotency:** if `webhook_log` already holds a row for this gateway and this gateway event ID, return HTTP 200 and stop. Gateways deliver at least once and retry on timeout.
3. **Log** the event to `webhook_log`, with its raw payload.
4. **Dispatch** a background task to process it. If dispatch fails, the row stays unprocessed and the reconciliation task (below) dispatches it later.
5. **Return HTTP 200** immediately, whatever happened in step 4.

```python
import json
from datetime import datetime, timedelta, timezone
import anvil.server
import anvil.tables.query as q
from anvil.tables import app_tables

@anvil.server.http_endpoint("/webhooks/stripe")
def handle_stripe_webhook():
    raw = anvil.server.request.body.get_bytes()
    sig_header = anvil.server.request.headers.get('stripe-signature', '')

    if not verify_stripe_signature(raw, sig_header):
        return anvil.server.HttpResponse(400, "Invalid signature")

    event = json.loads(raw)
    if app_tables.webhook_log.get(gateway='stripe', event_id=event['id']):
        return anvil.server.HttpResponse(200, "Already received")

    row = app_tables.webhook_log.add_row(
        gateway='stripe',
        event_id=event['id'],
        event_type=event.get('type', ''),
        payload=raw.decode('utf-8'),
        verified=True,
        processed=False,
        received_at=datetime.now(timezone.utc),
    )
    try:
        anvil.server.launch_background_task('process_webhook', row)
    except Exception:
        pass  # the reconciliation task dispatches it

    return anvil.server.HttpResponse(200, "Received")
```

The endpoint is served at `[base_url]/_/api/webhooks/stripe`; Paystack and Brevo follow the same pattern at `/_/api/webhooks/paystack` and `/_/api/webhooks/brevo`.

The gateway event ID used for idempotency:
- **Stripe:** `event['id']`
- **Paystack:** `event['data']['id']`, or `event['data']['reference']` where the event has no ID
- **Brevo:** the webhook event's ID

### Processing

```python
@anvil.server.background_task
def process_webhook(row):
    try:
        event = json.loads(row['payload'])
        route_event(row['gateway'], row['event_type'], event)   # business logic per gateway and event type
        write_payload_to_r2(row)        # raw payload to the client's R2 bucket; sets row['r2_key']
        row.update(payload=None, processed=True, processed_at=datetime.now(timezone.utc))
    except Exception as e:
        row['error_message'] = str(e)
        push_management_event('webhook_processing_error', {
            'gateway': row['gateway'], 'event_id': row['event_id'], 'error': str(e)})
```

Business logic is itself idempotent where a duplicate would do harm (for example, a payment is recorded once per payment intent), as a second line of defence.

### Reconciliation

A low-priority background task runs hourly and dispatches every row that is unprocessed five minutes after it was received, so no webhook is lost to a failed dispatch.

```python
@anvil.server.background_task
def reconcile_webhooks():
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=5)
    for row in app_tables.webhook_log.search(processed=False, error_message=None,
                                             received_at=q.less_than(cutoff)):
        anvil.server.launch_background_task('process_webhook', row)
```

### The `webhook_log` table

| Column | Type | Purpose |
|---|---|---|
| `gateway` | string | `stripe`, `paystack` or `brevo` |
| `event_id` | string | The gateway's own event ID; with `gateway`, the idempotency key |
| `event_type` | string | For example `payment_intent.succeeded` |
| `payload` | string | The raw body, kept only until processed |
| `r2_key` | string | Where the raw payload is kept in the client's R2 bucket once processed |
| `verified` | bool | The signature was verified |
| `processed` | bool | Processing completed |
| `error_message` | string | The error, if processing failed |
| `received_at` | datetime | UTC, when the webhook arrived |
| `processed_at` | datetime | UTC, when processing completed |

Anvil generates row IDs; no ID column is added. The raw payload moves to the client's R2 bucket once processed, and `webhook_log` keeps the index row ([[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).

---

## Consequences

- ✅ Handlers return 200 within the gateway's timeout
- ✅ A retried delivery never creates a second row or a second dispatch
- ✅ A failed dispatch is recovered by reconciliation; a failed processing run is kept with its error and reported to Mybizz_management
- ✅ Processing runs in the background; the client's interface is not affected
- ⚠️ Payment status updates within seconds, not instantly
- ⚠️ Failed rows (`error_message` set) are investigated and retried by hand

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-real-time-and-background-tasks]]](C:/dev/project-library-global/adr-global/adr-real-time-and-background-tasks.md) | Background task architecture and limits |
| [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) | Error events pushed to Mybizz_management |
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | §4.9: Webhook URL registration during provisioning |

