---
title: "spec-five-app-architecture-model"
doc-id: "mb-1b7a1fda"
updated: "2026-11-08"
---
# Mybizz — Five-App Architecture Model (Specification)

**Scope:** Mybizz-wide. Applies to every Mybizz application. The app names below are patterns; an application's actual instance names are recorded in its own project library.

---

## The Five Apps

| App | Role | Contains | Updated via |
|---|---|---|---|
| App 1 — `{slug}-app1` | Development workspace. All feature work happens here. Never a dependency for any client instance. | All Data Tables (dev/testing), all UI forms, all server modules, all application code | Daily development; each release is tagged here |
| App 2 — `master_template` | Published dependency. Sole source of all server-side logic and UI forms for every client instance. | All server modules + all forms + all UI | The developer pushes App 1's tagged release into App 2's repository (Step 42) |
| App 3 — `blank_client_template` | The client app. The app every client instance runs. | The full table definitions, one startup module, the scheduled tasks, the Users service settings, `master_template` as dependency. Zero server modules, zero forms. | Each release that changes the table definitions |
| App 4 — `[client-name]-{vertical}` | One per paying client — a dedicated, isolated client instance. | One container running the release image, and one database of its own. | Through the release image: App 5's Release action moves every client instance to each new release |
| App 5 — `{Product}_management` | Platform operator's internal tooling — provisioning, health monitoring, billing automation, release distribution. | Client registry, monitoring dashboard, billing status, the New client, Release and Remove actions | Built before the first paying client, with `master_template`; updated by its own releases |

Apps 1, 2, 3 and 5 run on Mybizz's Anvil Business account. Each client instance runs on the Anvil App Server, as one container on DigitalOcean App Platform with its own database in DigitalOcean Managed PostgreSQL ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)).

## Why This Shape

- **Data isolation is structural.** Each client instance is a separate App Server with a separate database. `app_tables` always resolves to the current client's data. Cross-client access is architecturally impossible.
- **`master_template` is stateless.** It contains zero client data. All state lives in each client's own database and the client's own R2 bucket.
- **Clients never see source code.** Clients use the application through its web address; they have no access to the release image, the container or the repositories.
- **App 3 carries the schema.** The App Server builds a new client's tables from App 3's table definitions, and adds each release's new tables and columns when the container starts on that release.

## ⚠️ The Critical Constraint — Client-Specific Changes Are Made in App 1 Only

Every client instance runs the same release image. A change needed for one client belongs in the development workspace (App 1), tested against the test client instance, then released into `master_template` — after which every client instance, including the one that prompted the change, receives it through the next release.

Every client instance carries a README stating this explicitly, from App 3 ([[[default:adr-global/adr-client-instance-readme-five-app-system|Client Instance README]]](C:/dev/project-library-global/adr-global/adr-client-instance-readme-five-app-system.md)), since this is not a mistake that reliably gets caught by intuition alone — it does not transfer to an AI coding agent scoped to "fix something for client X," a new team member, or anyone working under time pressure.

## Update Deployment Model

```
{slug}-app1 (tagged release)
    ↓ pushed into App 2's repository when tested and approved (Step 42)
master_template + blank_client_template
    ↓ built into the release image
Test client instance
    ↓ App 5's Release action
Every client instance
```

No manual per-client update action exists. Releasing to client instances is a production action — release discipline (the whole test suite passing on the release image before release) is the quality gate. For high-risk releases, a staged rollout moves a subset of clients first, with the remainder following once stability is confirmed ([[[default:specifications-global/spec-deployment|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md)).
