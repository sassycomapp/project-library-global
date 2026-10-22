---
title: "spec-deployment"
doc-id: "mb-4a8a251d"
updated: "2026-10-22"
---
# Mybizz — Deployment Specification

**Scope:** Mybizz-wide. Covers the five apps' roles in deployment, the release workflow, rollback procedures, and schema migration.
**Authority:** [[[default:adr-global/adr-dependency-update-model|Dependency Update Model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md) ADR, the `blank-client-template` ADR (mb-3-cs project library), [[[default:adr-global/adr-anvil-platform-constraints|Anvil Platform Constraints and Design Boundaries]]](C:/dev/project-library-global/adr-global/adr-anvil-platform-constraints.md) ADR §7

---

## 1. Deployment Model

Every Mybizz business has five apps (see [[[default:specifications-global/spec-five-app-architecture-model]]](C:/dev/project-library-global/specifications-global/spec-five-app-architecture-model.md)). Each app has one environment and one database; the Hobby plan, on which every client starts, has no staging environment.

| App | Role in deployment |
|---|---|
| App 1 — `{slug}-app1` | Development. Features are built and tested here, and each release is tagged here (`vMAJOR.MINOR.PATCH`). |
| App 2 — `master_template` | The release. It holds exactly App 1's latest released tag. Every client instance depends on it. |
| App 3 — `blank_client_template` | The released schema, with no data. New client instances are cloned from it. |
| App 4 — each client instance | On the client's own Anvil account; its code comes from App 2 through the dependency. |
| App 5 — Mybizz management | Receives heartbeats and events; sends control calls. |

Testing before release happens on the Anvil App Server on the developer's computer and on a test client instance, not in a staging environment.

---

## 2. Release Workflow

### The Five-App Update Flow

```
App 1 (tagged release, e.g. v1.4.0)
    ↓ the developer pushes the tag into App 2's repository (Step 42)
App 2 — master_template
    ↓ automatically, through the dependency
Every client instance
```

### Release Steps

1. **Feature complete** in App 1, and signed off (`build-verified`)
2. **Release ready** — every test passes and no High or Critical finding is open (Step 41)
3. **Tag** the release in App 1
4. **Back up** every client instance to its own R2 bucket
5. **Push** the tag into App 2's repository (Step 42) — this is the production action, and only the developer performs it
6. **Every client instance** receives the update through its dependency on App 2
7. **Send release notification** to clients via Anvil built-in email

### Pre-Release Checklist

Before pushing a release into App 2:

- [ ] Every feature of the release has passed `build-verified`
- [ ] No breaking Data Table schema change without a migration plan in the schema migration log
- [ ] Release notes written
- [ ] Vault and integration dependencies documented if changed
- [ ] The whole test suite passes for the release, as [[[default:security-global/requirements/sec-requirements-pre-merge-master-template]]](C:/dev/project-library-global/security-global/requirements/sec-requirements-pre-merge-master-template.md) requires

---

## 3. Staged Rollout

For high-risk releases:

1. Set a subset of client instances to depend on the previous version tag of App 2, and the rest on the new release, or the reverse for a canary
2. Monitor heartbeats and error logs
3. Once the release is confirmed, set the remaining client instances to the new release

Each client instance is changed in its own client's Anvil account.

---

## 4. Rollback

### Code Rollback

Rollback is re-pointing App 2 to the last good release tag and republishing — not a code revert, which does not un-publish an app.

**Steps:**
1. Identify the last good release tag
2. Push that tag into App 2's repository again
3. Republish App 2
4. Verify the rollback succeeded on the test client instance and in the heartbeats

### Schema Rollback

Schema changes (adding/modifying Data Tables) cannot be automatically rolled back in Anvil. Schema rollback requires:

1. Manual removal of added columns/tables in the Anvil IDE
2. Data migration if columns were modified
3. Application to every affected client instance individually

**Rule:** Never release a schema change without a documented migration plan for existing client instances.

---

## 5. Schema Migration

### Responsibility

| Target | Purpose | Frequency |
|---|---|---|
| App 3 — `blank_client_template` | Ensures future client instances get the correct schema | On every schema change |
| Every existing client instance | Ensures running clients are not broken | On every schema change |

### Migration Process

1. Apply the schema change in App 1, and record it in the project library's schema migration log (Step 17)
2. Test it on the local runtime and on the test client instance
3. Apply the same schema change to App 3
4. Document migration steps for existing client instances
5. Release the code to App 2 (Step 42)
6. Apply the schema migration to each existing client instance

**Constraint:** There is no automated migration tool in Anvil. Schema migrations to existing client instances are manual operations in each client's account.

---

## 6. Backup

### Backup Points

| Event | Action |
|---|---|
| Before a test run on hosted App 1 | Back up App 1 |
| After a passing test run on hosted App 1 | Back up App 1 (known good state) |
| Before a release (Step 42) | Back up every client instance to its own R2 bucket |
| Before a schema migration | Back up the client instance |
| Never | Back up a failing state |

Test runs on the local Anvil App Server need no backup: they start from an empty database each time.

### Backup Method

- Git commit and release tag (code)
- Data export of each client instance to its own R2 bucket (data)

---

## 7. Client Instances

Each client instance is a separate Anvil app on the client's own account. Deployment to client instances is automatic through the dependency model:

- **Code updates:** Automatic — once a release is in App 2, every client instance receives it
- **Schema updates:** Manual — applied per client instance
- **Configuration updates:** Manual — per client instance settings

### Post-Release Verification

After every release to App 2:

1. Verify App 2 loads without errors
2. Verify the test client instance reflects the update and passes its smoke test
3. Check each instance's heartbeat for its release version and schema fingerprint
4. Check `error_log` for new errors
5. Verify background tasks are running (heartbeat)

### Schema Migration Strategy Classifications

Schema migrations are classified into three types, each with its own ordered procedure:

| Type | Definition | Procedure |
|---|---|---|
| **Additive** | New columns added, no existing data affected | Add column via Data Tables UI, update App 3, document |
| **Breaking** | Columns removed or renamed | 1. Mark column deprecated, 2. Migrate data to replacement, 3. Remove column only after all instances confirmed migrated |
| **Modified** | Column type or constraint changed | 1. Add new column with correct type, 2. Migrate data, 3. Remove old column |

**Migration checklist (every migration, regardless of type):**
1. Update release notes with migration description
2. Record it in the schema migration log
3. Document procedure for existing clients
4. Add backward-compatibility code where applicable
5. Define rollback procedure
6. Test on the test client instance before broad rollout

## 8. Account-Level Failure Scenarios

Any Anvil project operating multiple client instances under a single Anvil account has a
single point of failure at the account level. Documented responses for each scenario:

| Scenario | Detection | Recovery | Prevention |
|---|---|---|---|
| Account suspension | Email from Anvil + app unavailable | Contact Anvil support immediately; no self-service recovery | Monitor billing status |
| Account compromise | Unauthorized changes, unknown collaborators | Contact Anvil support; rotate all credentials; audit all instances | Strong passwords, 2FA, restrict collaborators |
| Platform outage | App unreachable, `anvil.works` status page | No recovery action possible — wait for Anvil resolution | Document recovery expectations in client SLA |

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

Rollback mechanism: re-point App 2 to the last good release tag (section 4) — not `git revert` (which does not un-publish an app).

