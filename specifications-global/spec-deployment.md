---
document: Mybizz — Deployment Specification
doc-id: global-0062
state: Live
date-created: 2026-07-25T150027+0200
---
# Mybizz — Deployment Specification

**Scope:** Mybizz-wide. Covers Anvil deployment environments, release workflow, rollback procedures, and schema migration.
**Authority:** `dependency-update-model` ADR, `blank-client-template` ADR, `anvil-platform-constraints` ADR §7

---

## 1. Deployment Model

Anvil deploys via **named Deployment Environments**, each with its own URL, code version (branch/commit), and database. This is not a generic CI/CD pipeline.

### Environment Structure

| Environment | Purpose | GitHub Branch | URL Pattern |
|---|---|---|---|
| Development | Feature work, testing | `develop` | `mb-3-cs.anvil.app` |
| Staging | Pre-release verification | `stable` (tagged) | `[client-name]-staging.anvil.app` |
| Production | Client-facing | `stable` | `[client-name].anvil.app` or custom domain |

### Environment Branching in Code

```python
if anvil.app.environment.name == "Production":
    # Production-specific behavior
elif anvil.app.environment.name == "Staging":
    # Staging-specific behavior
```

---

## 2. Release Workflow

### The Five-App Update Flow

```
mb-3-cs (develop branch)
    ↓ merge when tested and ready
master_template (stable branch)
    ↓ automatically, immediately
All client instances tracking stable branch
```

### Release Steps

1. **Feature complete** in mb-3-cs on `develop` branch
2. **Test** in mb-3-cs Development environment
3. **Merge** `develop` → `stable` in GitHub (this is the production action)
4. **master_template** reflects the update immediately (tracks `stable`)
5. **All client instances** receive the update automatically via dependency
6. **Send release notification** to clients via Anvil built-in email

### Pre-Merge Checklist

Before merging `develop` → `stable`:

- [ ] Feature fully tested in mb-3-cs
- [ ] No breaking Data Table schema changes without migration plan
- [ ] Release notes written
- [ ] Vault and integration dependencies documented if changed
- [ ] All pure logic tests passing
- [ ] Integration tests passing via Uplink

---

## 3. Staged Rollout

For high-risk releases, Anvil supports version tags using format `vMAJOR.MINOR.PATCH`:

1. Tag the release commit in master_template's GitHub repo
2. Update a subset of client instances to the version tag instead of tracking `stable`
3. Monitor for issues
4. Once confirmed stable, roll remaining client instances to `stable`

All managed from the single mybizz Anvil account IDE.

---

## 4. Rollback

### Code Rollback

Rollback is re-pointing an environment to a different commit and republishing — not a code revert, which does not un-publish an app.

**Steps:**
1. Identify the last known good commit in GitHub
2. In Anvil IDE, re-point the environment to that commit
3. Republish the environment
4. Verify the rollback succeeded

### Schema Rollback

Schema changes (adding/modifying Data Tables) cannot be automatically rolled back in Anvil. Schema rollback requires:

1. Manual removal of added columns/tables in the Anvil IDE
2. Data migration if columns were modified
3. Application to every affected client instance individually

**Rule:** Never merge a schema change to `stable` without a documented migration plan for existing client instances.

---

## 5. Schema Migration

### Responsibility

| Target | Purpose | Frequency |
|---|---|---|
| `blank_client_template` | Ensures future client instances get correct schema | On every schema change |
| Every existing client instance | Ensures running clients are not broken | On every schema change |

### Migration Process

1. Apply schema change in mb-3-cs (Development environment)
2. Test thoroughly
3. Apply same schema change to `blank_client_template`
4. Document migration steps for existing client instances
5. Merge code to `stable` (master_template)
6. Apply schema migration to each existing client instance manually

**Constraint:** There is no automated migration tool in Anvil. Schema migrations to existing client instances are manual IDE operations.

---

## 6. Backup

### Backup Points

| Event | Action |
|---|---|
| Before integration tests | Create backup (safety checkpoint) |
| After integration tests pass | Create backup (known good state) |
| Before schema migration | Create backup |
| Never backup failed tests | Only backup "known good" states |

### Backup Method

Anvil does not provide automated backup. Backup is achieved via:
- Git commit (code)
- Anvil IDE clone (app state)
- Manual Data Table export (data)

---

## 7. Deployment Environments — Client Instances

Each client instance is a separate Anvil app. Deployment to client instances is automatic via the dependency model:

- **Code updates:** Automatic — merge to `stable` and all client instances update
- **Schema updates:** Manual — must be applied per client instance in the Anvil IDE
- **Configuration updates:** Manual — per client instance settings

---

## 8. Post-Deploy Verification

After any release to `stable`:

1. Verify master_template loads without errors
2. Verify at least one client instance reflects the update
3. Check `health_log` table for degradation
4. Check `error_log` table for new errors
5. Verify background tasks are running (check `health_log` heartbeat)

---

## 7. Schema Migration Strategy Classifications

Schema migrations are classified into three types, each with its own ordered procedure:

| Type | Definition | Procedure |
|---|---|---|
| **Additive** | New columns added, no existing data affected | Add column via Data Tables UI, update blank_client_template, document |
| **Breaking** | Columns removed or renamed | 1. Mark column deprecated, 2. Migrate data to replacement, 3. Remove column only after all instances confirmed migrated |
| **Modified** | Column type or constraint changed | 1. Add new column with correct type, 2. Migrate data, 3. Remove old column |

**Migration checklist (every migration, regardless of type):**
1. Update release notes with migration description
2. Update `blank_client_template.md` with new schema
3. Document procedure for existing clients
4. Add backward-compatibility code where applicable
5. Define rollback procedure
6. Test on at least one existing client instance before broad rollout

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

Rollback mechanism: re-point the Production environment to the last known-good commit in
the Anvil Publish dialog — not `git revert` (which does not un-publish an app).

---

*spec-deployment.md v1.1 — Added §7 Schema Migration Classifications, §8 Account-Level Failure Scenarios, §9 Rollback Trigger Thresholds. Extracted from mb-3-cs deployment-procedures.md.*
