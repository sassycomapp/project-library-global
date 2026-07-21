# {Project Name} — globals.py Contract

**Authority:** **[PROJECT]** cite this project's form-architecture/state-management ADR.
**Status:** Living document — update as new shared state is added during implementation.

---

## Purpose

This document defines every shared state variable in `globals.py`. Each entry specifies
the variable name, type, which form sets it, which forms read it, and what happens when
it's `None`.

**Rule:** Every form that reads from `globals.py` must use `getattr(globals, 'var_name', None)`
and handle the `None` case defensively. Never assume a globals variable is set.

---

## State Variables

**[PROJECT]** — replace the entries below with this project's actual shared state. The
example (project `mb0test`) shows the expected shape: a simple selected-record variable,
and a multi-step flow-state variable with per-key tracking. Neither is this project's
real state — do not carry `mb0test`'s variable names forward.

### Example — `current_contact` (mb0test)

| Field | Value |
|-------|-------|
| **Type** | `app_tables.contacts` row or `None` |
| **Set by** | `ContactListForm` (on contact selection), `BookingEditorForm` (on contact auto-create) |
| **Read by** | `ContactViewerForm`, `ContactEditorForm`, `BookingEditorForm` |
| **When None** | Redirect to `ContactListForm` |

### Example — `booking_flow_state` (mb0test)

| Field | Value |
|-------|-------|
| **Type** | `dict` with keys below |
| **Set by** | `BookingEditorForm` (during multi-step booking flow) |
| **Read by** | `BookingEditorForm` (each step reads prior selections) |
| **When None** | Initialize empty dict at flow start |

**Keys:**

| Key | Type | Set at step | Read at step |
|-----|------|-------------|--------------|
| `service` | `app_tables.services` row | Step 1 (service selection) | Steps 2-7 |
| `provider` | `app_tables.users` row | Step 2 (provider selection) | Steps 3-7 |
| `date` | `str` (ISO date) | Step 3 (date selection) | Steps 4-7 |
| `time_slot` | `str` (HH:MM) | Step 3 (time selection) | Steps 4-7 |
| `cached_context` | `dict` or `None` | Step 1 response cache | Steps 2-5 (avoid re-fetch) |

**Reset:** Clear a multi-step flow-state dict to `{}` on completion or cancellation —
document this explicitly for every flow-state variable this project actually has.

---

## Defensive Loading Pattern

Every form that reads from `globals.py` must follow this pattern:

```python
def __init__(self, **event_args):
    import globals
    self.contact = getattr(globals, 'current_contact', None)
    if self.contact is None:
        from anvil import open_form
        open_form('content_panel', 'contact_list')
        return
    # Continue with form initialization
```

**Do not** use `globals.current_contact` directly — it raises `AttributeError` if the
variable was never set.

---

*This is the global starter model. Copy into a new project's `docs-local/`, replace the
`mb0test` example entries with this project's real shared state, and remove this closing
note. An unfilled `[PROJECT]` marker in a live project's contract is a failure condition.*
