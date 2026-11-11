---
title: "adr-dependency-update-model"
doc-id: "mb-bf8aa7d8"
updated: "2026-11-11"
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

Every release is staged:

1. App 5's Release action moves the test client instance to the new release image
2. Then 10% of client instances; the rest stay on the previous image
3. Then every client instance

Each stage passes its health check before the next starts: every container in the stage runs the new image by its digest, sends a heartbeat within 30 minutes and shows no rise in errors. A failed health check rolls that stage back to the previous release image automatically, stops the release, and sends the developer an immediate message.

### Signed Images

- Each release image is signed when it is built, by the image build workflow in `{slug}-app4`.
- Each client container runs the image by its digest, never by a tag, so the image a container runs cannot be swapped under the same name.
- App 5's Release action verifies the image's signature before it moves any container, and refuses an image whose signature does not verify.

### Image Security

- The image build workflow scans the release image for known vulnerabilities at every build, and again every week. Each finding is reported to App 5.
- A high or critical finding (vendor-rated high or critical, CVSS 7 or above, or with no rating given) is fixed and released to every client within 14 days of the vendor's fix. App 5 counts the days and messages the developer on days 7 and 10. The patched image is released once the developer approves it.
- The base image and the Java runtime are kept on versions their vendors support. A build containing end-of-life software fails.
- These rules meet the Cyber Essentials security update control ([[[default:security-global/compliance/sec-cyber-essentials-compliance]]](C:/dev/project-library-global/security-global/compliance/sec-cyber-essentials-compliance.md)).

### Registry Clean-Up

At every release, the image build workflow deletes images older than the last three releases and runs the registry's storage clean-up, so the registry stays inside its plan.

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
- The image's signature verifies
- The image scan shows no high or critical finding older than 14 days, and no end-of-life software
- Release notes are written and ready to send
- Vault and integration dependencies are documented if changed

---

## Proof

Releasing to the test client instance, a staged rollout, and rollback to the previous release image are proven before the first client is onboarded (tests RL-05 and RL-07).

---

## Consequences

- ✅ Updates require no manual per-client action
- ✅ All client instances always run the same release image (except during the stages of a release)
- ✅ Every release staged, with automatic rollback on a failed health check
- ✅ Only signed images run, each by its digest
- ✅ Known vulnerabilities closed within 14 days
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
