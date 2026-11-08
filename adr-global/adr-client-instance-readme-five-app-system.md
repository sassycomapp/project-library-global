---
title: "adr-client-instance-readme-five-app-system"
doc-id: "mb-ed135450"
updated: "2026-11-08"
---
# Mandatory README in Every Client Instance Documenting the Five-App System

## Status

Accepted

## Context

Mybizz runs on a five-app architecture. Apps 1, 2, 3 and 5 are on Mybizz's Anvil Business account; each client instance runs the release image on DigitalOcean ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)):

1. **`{slug}-app1`** — the development workspace. All feature work happens here. Never a dependency for any client instance.
2. **`master_template`** — the sole source of all server-side logic and UI forms for every client instance. Receives App 1's tagged releases, pushed in by the developer.
3. **`blank_client_template`** — the client app. Contains the table definitions (see the project's authoritative-schema document), one startup module, the scheduled tasks, and `master_template` as a dependency. Zero server modules, zero forms.
4. **`[client-name]-{vertical}`** — one per paying client: one container running the release image, with its own database. Nothing else.
5. **`{Product}_management`** — internal platform-operator tooling: provisioning, health monitoring, billing automation and release distribution.

App 3 therefore appears, on inspection, almost entirely empty: no forms, no server modules — only a startup module, table definitions, scheduled tasks and a dependency reference. All server-side logic and UI a client instance displays comes from `master_template`.

This emptiness is intentional, but Anvil's dependency-precedence behavior means that if a server module or form is ever added to App 3, Anvil executes or renders that local copy instead of the one in `master_template`. Because every client instance runs App 3, that copy silently overrides `master_template` for every client, and later fixes to the same form or module in `master_template` stop reaching clients, with no error, warning, or other obvious signal that anything has gone wrong.

A human developer with architectural context, on opening App 3 and finding it conspicuously empty, will typically pause and investigate before adding code — the absence of any forms or modules functions as an implicit stop sign. However, this is a learned instinct, not a guarantee. It does not reliably transfer to:

- An AI coding agent given a task scoped to "fix something for client X," which may treat an empty directory as an invitation to create the missing file rather than as a structural signal to investigate further.
- A new team member, contractor, or maintainer who has not yet internalized the five-app model.
- Anyone working under time pressure who skips the investigation step.

## Decision

App 3's repository and the business's `{slug}-app4` repository each contain a standardized README that:

1. **Leads with the constraint, not the explanation.** The first visible line states plainly that App 3 is intentionally empty except for the startup module, the table definitions and the scheduled tasks, and that no forms or server modules are to be added to it.
2. **Explains the mechanism.** A brief explanation that App 3 depends on `master_template` for all server logic and UI, and that a form or module added to App 3 overrides `master_template` for every client instance.
3. **Redirects to the correct location.** A pointer to where the requested change actually belongs: the `{slug}-app1` development workspace, tested against the test client instance, then released into `master_template` (Step 42), after which every client instance receives the change through the next release.

The image build in `{slug}-app4` stops if App 3 holds any form or server module, so no release image can carry one.

## Consequences

**Positive**

- Removes reliance on tacit human intuition as the sole safeguard against an action that is easy to take and hard to notice.
- Gives AI coding agents and unfamiliar maintainers the necessary context inline, at the exact point where the risk exists, rather than in a separate architecture document they may never consult before acting.
- The image build's check makes the mistake impossible to release, and the README explains why the build stopped.
- The README travels with every release, so it is always current.

**Negative / Trade-offs**

- The README depends on being read before action is taken; the image build's check is the safeguard when it is not.

## Alternatives Considered

- **Rely on developer training and tacit convention alone.** Rejected — does not transfer to AI agents, new hires, or anyone acting under time pressure.
- **Document the rule only in a central/external architecture document.** Rejected — context not present at the point of action is context that can be skipped; the constraint needs to live where the risk is, not only where the explanation is.
