---
document: "Threat Model — Insecure Direct Object Reference"
doc-id: sec-insecure-direct-object-reference
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Insecure Direct Object Reference

**Scope note:** related to, but distinct from, `sec-broken-access-control-within-instance.md`, which covers a query returning too much data. This document covers a single, specific object (an invoice PDF, an uploaded file) being reachable directly by guessing or incrementing its identifier.

## Applicable Threat

An invoice, generated per the `pdf-invoice-generation` ADR, or any uploaded file, is reachable via a predictable or sequential identifier, letting a user access another user's specific document by changing an ID in a URL or request, without going through any search function's own filtering.

## Security Requirement

Any server function that retrieves a specific object by ID (not a search/list) verifies the requesting user actually owns or is permitted to access that specific object — the same ownership check required generally in `sec-broken-access-control-within-instance.md`, applied specifically to single-object retrieval by ID.

## Approved Pattern

```python
@anvil.server.callable
def get_invoice_pdf(invoice_id):
    user = anvil.users.get_user()
    invoice = app_tables.invoices.get(id=invoice_id)
    if invoice['customer'] != user and user['role'] not in ('owner', 'manager'):
        raise anvil.server.PermissionDenied()
    return invoice['pdf_file']
```

## Prohibited Pattern

```python
@anvil.server.callable
def get_invoice_pdf(invoice_id):
    return app_tables.invoices.get(id=invoice_id)['pdf_file']
```

Retrieving by ID with no ownership check — any authenticated user supplying any valid ID receives that document.

## Implementation Guidance

Every "get by ID" function is a candidate for this check — not just the obviously sensitive ones. Review each one explicitly rather than assuming only "important" objects need it.

## Verification Requirements

For each get-by-ID function, log in as a user with no relationship to a specific object, attempt to retrieve it directly by ID, confirm rejection.

## Authoritative Sources

- `pdf-invoice-generation` ADR (referenced; specific document not yet reviewed directly)
- `sec-broken-access-control-within-instance.md`

## Known Exceptions

Roles explicitly permitted broader access (Owner, Manager) per the RBAC table are exempt, same as `sec-broken-access-control-within-instance.md`.

## Lessons Learned

None yet. Populated as real findings occur.
