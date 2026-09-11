---
document: "Threat Model — Payment Manipulation"
doc-id: sec-payment-manipulation
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Payment Manipulation

## Applicable Threat

A user or an external actor alters a price, quantity, currency, or payment amount client-side before it reaches the payment gateway, or replays/forges a webhook event to falsely mark a payment as successful. Real attack surface: `[[spec-api-specification]]` confirms webhook handlers (Stripe, Paystack) update booking status and generate invoices directly from incoming webhook data.

## Security Requirement

The server, never the client, is the sole source of truth for any amount charged. Every webhook must have its signature validated before its payload is trusted. Every webhook event must be checked for idempotency before processing, to prevent a captured or replayed event being processed twice.

## Approved Pattern

```python
@anvil.server.callable
def create_checkout_session(booking_id):
    booking = app_tables.bookings.get(id=booking_id)
    amount = booking['service']['price']  # server-side lookup, not client-supplied
    return gateway.create_session(amount=amount, booking_id=booking_id)
```

Webhook handling per `[[spec-api-specification]]` §2.4: validate signature → check `webhook_log` for idempotency → log → dispatch to background task → return HTTP 200. Signature validation happens before any data from the payload is used.

## Prohibited Pattern

```python
@anvil.server.callable
def create_checkout_session(booking_id, amount):  # amount from client
    return gateway.create_session(amount=amount, booking_id=booking_id)
```

Accepting `amount` as a client-supplied argument. A user can call this function directly with any value.

## Implementation Guidance

- Any server function that creates a charge, session, or invoice must compute the amount itself, from the relevant Data Table, never accept it as a parameter.
- Webhook handlers must reject a request with an invalid or missing signature before touching the payload, per `[[spec-api-specification]]` §2.4.
- `webhook_log` must be checked before processing every webhook event, per the same section.

## Verification Requirements

- Attempt to call a payment-creating server function directly with a manipulated amount; confirm the server ignores it and computes its own.
- Send a webhook request with an invalid signature; confirm HTTP 400 and no state change.
- Send the same valid webhook event twice; confirm it is processed once, not twice.

## Authoritative Sources

- `[[spec-api-specification]]` §2, §2.4 — webhook endpoints, handler requirements
- `[[spec-vault-system]]` — gateway secret key handling

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
