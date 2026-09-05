---
document: "Threat Model — Injection and Unsafe Input"
doc-id: sec-injection-unsafe-input
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Injection and Unsafe Input

## Applicable Threat

User-supplied text (a booking note, a customer name, a search field) is used unsafely — inserted into a query in a way that changes the query's meaning, or displayed on a page in a way that lets it run as code in another user's browser (cross-site scripting).

## Security Requirement

All Data Table access goes through Anvil's own Data Tables API, per `spec-security.md` §1 — never raw SQL string-building. Any user-supplied text rendered back to a page must be treated as text, never as HTML/executable content, unless explicitly and deliberately sanitized for a specific, approved rich-text use case.

## Approved Pattern

```python
app_tables.bookings.search(customer_name=q.text)  # Anvil Data Tables API — parameterized by design
```

## Prohibited Pattern

```python
# Constructing a raw query string from user input — not how Anvil Data Tables work,
# but the equivalent failure mode if any raw SQL/external DB call is ever introduced:
query = f"SELECT * FROM bookings WHERE customer_name = '{user_input}'"
```

Any code path that builds a query, command, or file path by directly concatenating user-supplied text.

## Implementation Guidance

- Anvil's Data Tables API is parameterized by default — the main real risk is a future integration (an external database, a shell command, a generated report) that doesn't use it. Any such integration needs its own explicit review against this document.
- User-supplied text displayed in a form must use Anvil's own text-display components, not `HTMLTemplate` with raw user content injected — `HTMLTemplate` is already banned platform-wide per the `adr-htmltemplate-use` ADR, for unrelated reasons, but this is a second, independent reason it stays banned.

## Verification Requirements

- For any feature accepting free-text input, confirm it's stored and retrieved via the Data Tables API, not string-built.
- Attempt to submit a booking note or similar field containing `<script>` tags or SQL-like syntax; confirm it's stored and displayed as inert text, not executed.

## Authoritative Sources

- `spec-security.md` §1 — RBAC and Data Access
- `adr-htmltemplate-use` — HTMLTemplate ban (independent reason, same practical effect)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
