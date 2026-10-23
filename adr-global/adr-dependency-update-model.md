---
title: "adr-dependency-update-model"
doc-id: "mb-bf8aa7d8"
updated: "2026-10-23"
---
# `dependency-update-model` ADR — Dependency Update Model

**Status:** Accepted

---

## Context

Every Mybizz application needs to release updates from its development workspace (App 1) to all client instances without manual per-client intervention.

Anvil's dependency system lets a client instance depend on master_template's published version or on a specific version tag. Pushing App 1's tagged release into master_template's repository updates every client instance at once; no re-cloning is required.

---

## Decision

### The App Structure

| App | Purpose | How it is updated |
|---|---|---|
| App 1 — `{slug}-app1` | Development workspace | Daily development; each release is tagged `vMAJOR.MINOR.PATCH` |
| App 2 — `master_template` | Published dependency | The developer pushes App 1's tagged release into App 2's repository (Step 42) |
| App 3 — `blank_client_template` | Provisioning clone source | Carries the released schema |
| App 5 — `{Product}_management` | Platform operator tooling | Its own repository |

### Update Flow

```
App 1 (tagged release)
    ↓ pushed into App 2's repository when tested and approved (Step 42)
master_template
    ↓ automatically, through the dependency
Every client instance
```

1. All feature development happens in App 1
2. When a release is tested and approved, the developer pushes its tag into App 2's repository
3. master_template reflects the release when it is published
4. Every client instance depending on master_template receives the update automatically — no client action required
5. A release notification email is sent to clients via Anvil built-in email

### Client Notification

Clients receive a release notification via Anvil built-in email containing:
- What changed (release notes)
- Any action required on their part (rarely, if ever)

The email does not trigger a technical update action. The update has already happened at the point of sending. The email is informational only.

### Staged Rollout Option

Anvil supports version tags using the format `vMAJOR.MINOR.PATCH` (e.g. `v1.1.0`). For high-risk releases:

1. The release is tagged in App 1 and pushed into App 2 with its tag
2. A subset of client instances is set to depend on the new tag, the rest stay on the previous tag
3. Monitor heartbeats and error logs
4. Once the release is confirmed, the remaining client instances are set to the new tag

Each client instance is changed in its own client's Anvil account.

---

## Alternatives Rejected

| Alternative | Reason rejected |
|---|---|
| Re-clone master_template per release | Changes app ID — breaks all existing client dependencies |
| Manual per-client update trigger | Unworkable at 100 clients; no Anvil provisioning API |
| Client-initiated pull via in-app button | No Anvil API to change dependency version from within the app |

---

## Release Discipline

Because every client instance updates as soon as a release reaches App 2, the quality gate is the release decision itself. The following must be true before a release is pushed into App 2:

- Every feature of the release has passed `build-verified` and the whole test suite passes
- No breaking changes to existing Data Table schemas without a migration plan
- Release notes are written and ready to send
- Vault and integration dependencies are documented if changed

---

## Proof

Update propagation to a client instance on a separate Anvil account, and rollback to the previous release, are proven before the first client is onboarded (tests RL-05 and RL-07).

---

## Consequences

- ✅ Updates require no manual per-client action once the release is in App 2
- ✅ All client instances always run the same version (unless deliberately pinned)
- ✅ Staged rollout available via version tags without infrastructure changes
- ✅ Each client owns its own Anvil account and leaves with it
- ⚠️ Pushing a release into App 2 is a production action — release discipline is mandatory
- ✅ UI and form updates propagate automatically via master_template dependency (see [[[default:adr-global/adr-client-instance-architecture|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) ADR)
- ⚠️ Schema changes require separate migration process for existing client instances

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | Defines what lives in client instance vs master_template |
| [[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Includes dependency configuration step at provisioning |

