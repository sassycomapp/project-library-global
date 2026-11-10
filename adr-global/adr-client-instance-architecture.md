---
title: "adr-client-instance-architecture"
doc-id: "mb-c7c61252"
updated: "2026-11-10"
---
# `client-instance-architecture` ADR — Client Instance Architecture

**Status:** Accepted

---

## Context

Every client needs complete data isolation from every other client, every release delivered to every client with no per-client work, a clear separation between application code and client data, and a hosting cost that fits a price of £79 a month per client ([[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md)). This decision sets what a client instance contains and where it runs.

---

## Anvil Behaviour This Rests On

1. **`app_tables` resolves to the calling app.** When a server module in a dependency calls `app_tables`, the rows are read from and written to the tables of the client instance that depends on it, never to the dependency's own tables. This is structural and automatic; no application-level enforcement is needed.
2. **Forms are served from the dependency.** A client instance with no forms of its own imports a form from its dependency and opens it; the form loads and renders from the dependency at runtime.
3. **The Anvil App Server runs an app and its dependencies.** It loads each dependency checked out beside the app, matched by its dependency ID, and it builds and extends the app's tables from the app's table definitions (`auto-migrate`).

---

## Decision

**Every client instance runs on the Anvil App Server, as one container on DigitalOcean App Platform, with one database of its own in the business's DigitalOcean Managed PostgreSQL cluster.** The specification is [[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md).

| Component | Lives in | Notes |
|---|---|---|
| Server modules | master_template only | All business logic, integrations, background tasks |
| UI forms and form code | master_template only | Served to client instances via dependency at runtime |
| Startup module | App 3 | One minimal module; imports and opens the first form from master_template |
| Table definitions | App 3 | The released schema; the App Server builds the client's tables from them |
| Scheduled tasks | App 3 | Calling the background tasks in master_template |
| Release image | The business's `{slug}-app4` repository and the Container Registry | The App Server, App 3, master_template and `m3`, built once per release |
| Data | The client's own database and the client's own R2 bucket | All client data; never leaves the instance |

**Every client instance runs the same release image. A client instance holds no code of its own.** The startup module imports the first form from master_template and opens it. All subsequent navigation, UI, form code, and server logic is served from master_template.

```python
# The complete client-side code of every client instance (App 3's startup module)
from master_template.MainForm import MainForm
from anvil import open_form
open_form(MainForm())
```

---

## Rationale

- `app_tables` resolves to the client instance (Anvil behaviour 1)
- Forms defined in a dependency are served to and rendered in the client instance at runtime (Anvil behaviour 2)
- One release image for every client means every client runs exactly the same tested code
- The App Server builds and extends each client's tables (Anvil behaviour 3), so a release that adds tables or columns needs no per-client work
- Data isolation between clients is architecturally guaranteed — each client has its own App Server and its own database
- Security boundary is structural, not enforced in application code
- DigitalOcean runs the servers, updates, failover and database backups, so Mybizz runs no server

---

## Consequences

- ✅ Server logic, UI and form updates reach every client instance through the release image and App 5's Release action
- ✅ New tables and nullable columns reach every client's database when its container starts on the release
- ✅ Data is fully isolated per client — structural guarantee
- ✅ No cross-client data access is architecturally possible
- ✅ Client instances need no per-client maintenance
- ⚠️ After a business's first release, a release never removes, renames or retypes a table or column; the table-change check stops any release that would
- ⚠️ The App Server is released by Anvil separately from Anvil's hosted service; Mybizz pins one App Server version, and every release passes the full test suite on the release image
- ⚠️ One cluster in one region serves every client of a business; the rebuild procedure restores every client in another region from the release image and the clients' R2 copies

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) | How client instances are hosted, released and provisioned |
| [[[default:adr-global/adr-dependency-update-model\|Dependency Update Model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md) | How updates flow from App 1 to client instances |
| [[[default:specifications-global/spec-five-app-architecture-model\|Five-App Architecture Model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md) | The five apps and their roles |
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Step-by-step provisioning process |
