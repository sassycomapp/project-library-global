---
title: "adr-client-instance-architecture"
doc-id: "mb-c7c61252"
updated: "2026-10-23"
---
# `client-instance-architecture` ADR — Client Instance Architecture

**Status:** Accepted

---

## Context

Every client needs complete data isolation from every other client, automatic propagation of server and UI updates, and a clear separation between application code and client data. This decision sets the relationship between `master_template` (App 2, the published dependency) and each client instance.

---

## Anvil Behaviour This Rests On

Both facts below were proven by test on Anvil before any server module was written.

1. **`app_tables` resolves to the calling app.** When a server module in a dependency calls `app_tables`, the rows are read from and written to the Data Tables of the client instance that depends on it, never to the dependency's own tables. This is structural and automatic; no application-level enforcement is needed.
2. **Forms are served from the dependency.** A client instance with no forms of its own can import a form from its dependency and open it; the form loads and renders from the dependency at runtime.

---

## Decision

Client instances are structured as follows:

| Component | Lives in | Notes |
|---|---|---|
| Server modules | master_template only | All business logic, integrations, background tasks |
| UI forms and form code | master_template only | Served to client instances via dependency at runtime |
| Startup module | Client instance | One minimal module; imports and opens first form from master_template |
| Data Tables (every table of the released schema) | Client instance | All client data; never leaves the instance |
| master_template dependency | Client instance | Set to the current release at provisioning; active |

**Client instances contain no server modules and no forms of their own.** The startup module is the only code a client instance contains. It imports the first form from master_template and opens it. All subsequent navigation, UI, form code, and server logic is served from master_template via the dependency.

```python
# The complete client-side code of every client instance
from master_template.MainForm import MainForm
from anvil import open_form
open_form(MainForm())
```

---

## Rationale

- `app_tables` resolves to the client instance (Anvil behaviour 1)
- Forms defined in a dependency are served to and rendered in the client instance at runtime (Anvil behaviour 2)
- Keeping all code (server modules and forms) exclusively in master_template ensures all updates propagate automatically to every client instance simultaneously
- Data isolation between clients is architecturally guaranteed — one client instance cannot access another's tables
- Security boundary is structural, not enforced in application code
- The startup module is the minimum viable client-side code — one import, one open_form call

---

## Consequences

- ✅ Server logic updates propagate to all client instances automatically on master_template release
- ✅ UI and form code updates propagate to all client instances automatically on master_template release
- ✅ Data is fully isolated per client — structural guarantee
- ✅ No cross-client data access is architecturally possible
- ✅ Client instances require no maintenance — only Data Tables and one startup module
- ⚠️ Client instances must never have server modules or forms added — provisioning documentation must make this explicit
- ⚠️ Schema changes (adding/modifying Data Tables) are the only update that does not propagate automatically — applied by the developer, in Anvil's Data Tables view, to `blank_client_template` and every existing client instance

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-dependency-update-model\|Dependency Update Model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md) | How updates flow from App 1 to client instances |
| [[[default:specifications-global/spec-five-app-architecture-model\|Five-App Architecture Model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md) | App 3, `blank_client_template`, the provisioning source for new client instances |
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Step-by-step provisioning process |

