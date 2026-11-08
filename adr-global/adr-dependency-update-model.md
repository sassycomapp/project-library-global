---
title: "adr-dependency-update-model"
doc-id: "mb-bf8aa7d8"
updated: "2026-11-08"
---
# `dependency-update-model` ADR — Dependency Update Model

**Status:** Accepted

---

## Context

Every Mybizz application needs to release updates from its development workspace (App 1) to all client instances without manual per-client intervention.

Every client instance runs the release image: the Anvil App Server with App 3, App 2 (`master_template`) and the `m3` theme ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)). A release reaches clients when their containers are moved to the new release image.

---

## Decision

### The App Structure

| App | Purpose | How it is updated |
|---|---|---|
| App 1 — `{slug}-app1` | Development workspace | Daily development; each release is tagged `vMAJOR.MINOR.PATCH` |
| App 2 — `master_template` | Published dependency | The developer pushes App 1's tagged release into App 2's repository (Step 42) |
| App 3 — `blank_client_template` | The client app | Its table definitions carry the released schema |
| App 4 — each client instance | Runs the release image | App 5's Release action |
| App 5 — `{Product}_management` | Platform operator tooling | Its own repository |

### Update Flow

```
App 1 (tagged release)
    ↓ pushed into App 2's repository when tested and approved (Step 42)
master_template + blank_client_template
    ↓ built into the release image, stored under the release tag
Test client instance
    ↓ App 5's Release action
Every client instance
```

1. All feature development happens in App 1
2. When a release is tested and approved, the developer pushes its tag into App 2's repository, and the release's table changes into App 3's table definitions
3. The release image is built and stored under the release tag
4. The table-change check passes, and the full test suite passes on the release image
5. The test client instance moves to the release image and passes its smoke test
6. App 5's Release action moves every client instance to the release image; each client's App Server adds the release's new tables and columns as it starts
7. App 5 sends each client a release notification email

### Client Notification

Clients receive a release notification email from App 5 containing:
- What changed (release notes)
- Any action required on their part (rarely, if ever)

The email does not trigger a technical update action. The update has already happened at the point of sending. The email is informational only.

### Staged Rollout

For high-risk releases:

1. App 5's Release action moves a chosen group of client instances to the new release image; the rest stay on the previous image
2. Monitor heartbeats and error logs
3. Once the release is confirmed, App 5 moves the remaining client instances to the new release image

### Rollback

App 5 moves the client instances back to the previous release image, with the App Server's `auto-migrate` off and `ignore-invalid-schema` on. Because a release only adds tables and nullable columns, the previous release runs on the newer schema, and no table or column is removed. The next release switches `auto-migrate` back on.

---

## Alternatives Rejected

| Alternative | Reason rejected |
|---|---|
| Manual per-client update | Unworkable at 100 clients |
| Client-initiated pull via in-app button | Releases are a production action taken only by Mybizz |
| Building a separate image per client | Clients would no longer run identical, tested code |

---

## Release Discipline

Because a release reaches every client instance in one action, the quality gate is the release decision itself. The following must be true before App 5's Release action runs:

- Every feature of the release has passed `build-verified` and the whole test suite passes on the release image
- The table-change check passes: no table or column is removed, renamed or retyped
- The test client instance runs the release and passes its smoke test
- Release notes are written and ready to send
- Vault and integration dependencies are documented if changed

---

## Proof

Releasing to the test client instance, a staged rollout, and rollback to the previous release image are proven before the first client is onboarded (tests RL-05 and RL-07).

---

## Consequences

- ✅ Updates require no manual per-client action
- ✅ All client instances always run the same release image (unless deliberately held back in a staged rollout)
- ✅ Staged rollout and rollback by release image
- ✅ New tables and nullable columns reach every client's database with the release
- ⚠️ Running App 5's Release action is a production action — release discipline is mandatory
- ⚠️ After a business's first release, a release never removes, renames or retypes a table or column

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-client-instance-architecture\|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md) | Defines what lives in client instance vs master_template |
| [[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) | The release image and App 5's actions |
| [[[default:specifications-global/spec-deployment\|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) | Release, rollback and backup procedures |
