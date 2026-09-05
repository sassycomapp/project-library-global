---
document: "Threat Model — Business Logic and Race Condition Abuse"
doc-id: sec-business-logic-race-conditions
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Business Logic and Race Condition Abuse

## Applicable Threat

A legitimate feature is abused through timing or sequence rather than a technical exploit — two simultaneous requests both booking the same slot before either commits, a discount applied twice through concurrent submission, a refund processed twice due to overlapping requests.

## Security Requirement

Any operation where two concurrent requests could both succeed and produce an inconsistent or duplicated result must use a real, atomic check — a database-level constraint or transaction, never a "check then act" pattern with a gap between the check and the action.

## Approved Pattern

```python
# Atomic: the uniqueness constraint itself prevents the double-booking,
# not a prior "is this slot free?" check with a gap before the write.
with app_tables.bookings.transaction():
    if app_tables.bookings.get(slot=slot_id, status='confirmed'):
        raise BookingConflict()
    app_tables.bookings.add_row(slot=slot_id, status='confirmed', ...)
```

## Prohibited Pattern

```python
existing = app_tables.bookings.search(slot=slot_id, status='confirmed')
if not existing:
    # a second, concurrent request can pass this same check
    # before either one has written its row
    app_tables.bookings.add_row(slot=slot_id, status='confirmed', ...)
```

A check-then-act sequence with no atomicity, leaving a real window for two concurrent requests to both pass the check.

## Implementation Guidance

For any feature involving a limited resource (a booking slot, a one-time discount code, a refund), identify the real race window and close it with a transaction or a database-level uniqueness constraint, not a prior read-check alone.

## Verification Requirements

For each such feature, attempt two genuinely concurrent requests for the same resource; confirm only one succeeds.

## Authoritative Sources

- None yet formally documented elsewhere in this project — this is a newly identified gap, not yet cross-referenced against an existing spec.

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
