---
title: "spec-deployment"
doc-id: "mb-4a8a251d"
updated: "2026-11-11"
---
# Mybizz — Deployment Specification

**Scope:** Mybizz-wide. Covers the five apps' roles in deployment, the release workflow, rollback procedures, schema changes, backup and failure scenarios.

---

## 1. Deployment Model

Every Mybizz business has five apps (see [[[default:specifications-global/spec-five-app-architecture-model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md)). Each app has one environment and one database; Mybizz uses no staging environment. Apps 1, 2, 3 and 5 run on Mybizz's Anvil Business account. Each client instance runs on the Anvil App Server on DigitalOcean ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md)).

| App | Role in deployment |
|---|---|
| App 1 — `{slug}-app1` | Development. Features are built and tested here, and each release is tagged here (`vMAJOR.MINOR.PATCH`). |
| App 2 — `master_template` | The release. It holds exactly App 1's latest released tag. |
| App 3 — `blank_client_template` | The client app: the released table definitions, the startup module and the scheduled tasks. |
| Release image | App 3, App 2 and `m3` on the pinned App Server, built once per release in the business's `{slug}-app4` repository and stored under the release tag. |
| App 4 — each client instance | One container running the release image, with its own database. |
| App 5 — Mybizz management | Receives heartbeats and events; sends control calls; runs the New client, Release and Remove actions through the DigitalOcean API. |

Testing before release happens on the Anvil App Server on the developer's computer, on the release image, and on the test client instance, not in a staging environment. The test client instance is a client instance of its own, on DigitalOcean, holding test data only.

---

## 2. Release Workflow

### The Update Flow

```
App 1 (tagged release, e.g. v1.4.0)
    ↓ the developer pushes the tag into App 2's repository (Step 42)
App 2 — master_template + App 3 — blank_client_template
    ↓ built into the release image
Test client instance
    ↓ App 5's Release action
Every client instance
```

### Release Steps

1. **Feature complete** in App 1, and signed off (`build-verified`)
2. **Release ready** — every test passes and no High or Critical finding is open (Step 41)
3. **Tag** the release in App 1
4. **Back up** every client instance to its own R2 bucket
5. **Push** the tag into App 2's repository, and the release's table changes into App 3's table definitions (Step 42) — only the developer performs this
6. **Build** the release image and store it under the release tag
7. **Check** the table definitions: the table-change check passes
8. **Test** the release image: the whole test suite passes on it
9. **Release to the test client instance** and pass its smoke test (Step 43)
10. **Release to every client instance** with App 5's Release action (Step 44)
11. **Send release notification** to clients from App 5

### Pre-Release Checklist

Before App 5's Release action runs:

- [ ] Every feature of the release has passed `build-verified`
- [ ] The table-change check passes: no table or column is removed, renamed or retyped
- [ ] Every table change is recorded in the schema migration log
- [ ] Release notes written
- [ ] Vault and integration dependencies documented if changed
- [ ] The whole test suite passes on the release image, as [[[default:security-global/requirements/sec-requirements-pre-merge-master-template]]](C:/dev/project-library-global/security-global/requirements/sec-requirements-pre-merge-master-template.md) requires
- [ ] The test client instance runs the release and passes its smoke test
- [ ] The release image's signature verifies
- [ ] The image scan shows no high or critical finding older than 14 days, and no end-of-life software

---

## 3. Staged Rollout

Every release is staged ([[[default:adr-global/adr-dependency-update-model|Dependency Update Model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md)):

1. App 5's Release action moves the test client instance to the new release image, by its digest
2. Then 10% of client instances
3. Then every client instance

Each stage passes its health check before the next starts: every container in the stage runs the new image by its digest, sends a heartbeat within 30 minutes and shows no rise in errors. A failed health check rolls that stage back automatically (section 4), stops the release and messages the developer. At every release, the image build workflow deletes images older than the last three releases and cleans the registry's storage.

---

## 4. Rollback

Rollback moves client instances back to the previous release image. It is not a code revert.

**Steps:**
1. Identify the last good release tag
2. App 5 moves the affected client instances to that release image, with `auto-migrate` off and `ignore-invalid-schema` on
3. Verify the rollback on the test client instance and in the heartbeats
4. The next release switches `auto-migrate` back on

A release only adds tables and nullable columns, so the previous release runs on the newer schema and no data is lost.

---

## 5. Schema Changes

### The Rule

- A business's first release sets its full schema.
- Every later release only adds tables and nullable columns. It never removes, renames or retypes a table or column.
- The table-change check in the business's `{slug}-app4` repository compares App 3's table definitions with the previous release and stops any release that breaks the rule.

### Process

1. Apply the schema change in App 1, and record it in the project library's schema migration log (Step 17)
2. Test it on the local App Server and on the test client instance
3. Write the same change into App 3's table definitions (Step 42)
4. The table-change check passes
5. The release image carries the change to every client instance; each client's App Server adds the new tables and columns when its container starts on the release

A column that is no longer used stays in place, unused. It is never removed from a client's database.

---

## 6. Backup

### Backup Points

| Event | Action |
|---|---|
| Every day | DigitalOcean backs up the cluster, kept for 7 days, with point-in-time recovery |
| Every night | Every client instance copies its data to its own R2 bucket |
| Before a test run on hosted App 1 | Back up App 1 |
| After a passing test run on hosted App 1 | Back up App 1 (known good state) |
| Before a release (Step 42) | Every client instance copies its data to its own R2 bucket |
| Never | Back up a failing state |

Test runs on the local Anvil App Server need no backup: they start from an empty database each time.

### Backup Checks

- **Daily:** App 5 checks that each client's nightly copy arrived, with the right date and a plausible size.
- **Monthly:** the restore drill. The test client instance restores one client's nightly copy into a scratch database in the cluster, compares its row counts with the source, deletes the scratch database and reports the result to App 5. The drill runs inside DigitalOcean because the cluster accepts connections from DigitalOcean only.
- Each client's nightly copies sit under the `backups/` prefix of its R2 bucket, with a 30-day lock: no key, Mybizz's included, can delete or overwrite a copy during those 30 days.

### Backup Method

- Git commit and release tag (code)
- The release image in the Container Registry, under its release tag (running code)
- DigitalOcean's cluster backups (data, inside DigitalOcean)
- Each client instance's copy in its own R2 bucket (data, outside DigitalOcean)

---

## 7. Client Instances

Each client instance is one container running the release image, with its own database. Deployment to client instances is through the release image:

- **Code updates:** App 5's Release action
- **Schema updates:** carried by the release image; applied by each client's App Server as its container starts
- **Configuration updates:** per client instance, in its encrypted App Platform environment values, through App 5

### Post-Release Verification

After every release:

1. Verify the test client instance runs the release and passes its smoke test
2. Check each instance's heartbeat for its release version and schema fingerprint
3. Check `error_log` for new errors
4. Verify background tasks are running (heartbeat)

---

## 8. Failure Scenarios

Mybizz's Anvil account holds Apps 1, 2, 3 and 5. Each business's DigitalOcean project holds its cluster, its test client instance and its client instances. Documented responses for each scenario:

| Scenario | Detection | Recovery | Prevention |
|---|---|---|---|
| Anvil account suspension | Email from Anvil; App 1, App 2 and App 5 unavailable | Client instances keep running; contact Anvil support; releases and provisioning wait until App 5 is back | Monitor billing status |
| One client container fails | That client's heartbeats stop | App Platform restarts the container; if it does not recover, App 5 recreates the container from the current release image | Container size checked against the client's use in App 5 |
| Cluster main node fails | Database errors in heartbeats | The standby node takes over automatically | Standby node from the first paying client |
| DigitalOcean region outage or account suspension | Every client's heartbeats stop; DigitalOcean Uptime reports App 5's status endpoint fault | App 5's **Rebuild** action (section 10) | Nightly R2 copies with a 30-day lock; the rebuild tested before the first paying client |
| Account compromise | Unauthorized changes, unknown collaborators | Contact the provider's support; rotate all credentials; audit all instances; follow the business's incident response plan | Hardware security keys on every supplier account; two scoped DigitalOcean keys; the cluster's trusted sources; locked nightly copies |

## 9. Rollback Trigger Thresholds

Quantitative triggers for immediate vs. considered rollback, measured against production
instances:

**Immediate rollback** (do not wait for investigation):
- Error rate > 10% across instances
- Critical functionality broken (booking, payments, login)
- Data corruption detected
- Security vulnerability introduced

**Considered rollback** (investigate, then decide):
- Error rate > 5% across instances
- Performance degradation > 50% (response time, throughput)
- Increasing pattern of customer complaints

Rollback mechanism: App 5 moves the client instances back to the previous release image (section 4).

---

## 10. Rebuild

App 5's **Rebuild** action restores every client of a business in another DigitalOcean region when `LON1` or the business's cluster is lost. It uses the provisioning key ([[[default:security-global/cloud/sec-client-provisioning-security|Client Provisioning Security]]](C:/dev/project-library-global/security-global/cloud/sec-client-provisioning-security.md)).

1. The developer chooses the region and starts **Rebuild** in App 5.
2. App 5 creates a new Managed PostgreSQL cluster in that region: Advanced Edition, PostgreSQL 18, at the current plan size, with its standby, storage autoscaling and trusted sources.
3. App 5 creates the provisioning job in the new region; the job creates each client's database and database user with its three limits.
4. Each client's data is restored from DigitalOcean's backups when they are reachable, otherwise from the client's latest nightly copy in its R2 bucket. At most 24 hours of data is lost when the nightly copy is used.
5. App 5 creates each client's container from the current release image, by its digest, with the client's settings, keys and domain, and points the client's DNS record at the new container through the Cloudflare API.
6. Each client is checked by its heartbeat; App 5 reports every client restored and any that failed.
7. App 5 messages every client about the interruption.

The rebuild restores the test client instance into another region before the first paying client ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 10).
