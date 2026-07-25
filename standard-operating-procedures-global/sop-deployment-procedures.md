---
document: "{Project Name} — SOP: Deployment Procedures"
doc-id: global-0083
state: Live
date-created: 2026-07-25T150027+0200
---
# {Project Name} — SOP: Deployment Procedures

**Authority:** **[PROJECT]** — this project's ADRs governing deployment model,
template/clone source, and platform constraints.

**How to use this SOP document:** each procedure below is trigger-based — it fires on a
specific event, not "as needed." Follow the numbered steps in order. Do not skip the
Verification step; a procedure isn't complete until verification passes. If a step fails,
go to that procedure's Escalation, don't 	improvise.

---

## Procedure 1 — Release Deployment

**Trigger:** A feature is fully tested and ready to ship.

**Preconditions:**
- All tests passing
- Release notes prepared
- Schema changes (if any) documented per Procedure 2 below

**Steps:**
1. Develop — feature work happens on the development branch
2. Test — feature fully tested
3. Prepare release notes — what changed, any action required
4. Merge — development branch → tracked release branch
5. Verify — confirm dependent instances reflect the update
6. Notify — send release notification to affected users, per project's channel

**[PROJECT]** — state this project's actual propagation model: branch-based (merge to
tracked branch releases automatically to all dependent instances — server logic, UI, and
forms propagate; schema does not, see Procedure 2) or single-instance manual publish.

**High-risk releases — staged rollout variant:**
1. Tag the release commit
2. Update a subset of instances to the version tag instead of the tracked branch
3. Monitor for issues
4. Once confirmed stable, roll remaining instances to the tracked branch

**Verification:**
- Health endpoint responds on a sample of instances
- Background tasks confirmed running
- Error rate checked, no new errors
- For significant releases: manual login + key-functionality check on a sample instance

**Escalation:** if verification fails, go to Procedure 3 (Rollback) immediately — do not
attempt a forward-fix under a failed verification.

---

## Procedure 2 — Schema Migration

**Trigger:** A Data Table schema change is needed.

**Preconditions:**
- Migration plan documented before any merge — a schema change must never reach the
  release branch without one
- **[PROJECT]** confirm the platform has no programmatic schema API (true for Anvil Data
  Tables) — if so, every step below is manual, per instance, and effort scales with
  instance count

**Steps — additive (new column):**
1. Add the column to the provisioning template
2. Add the column to each existing instance
3. Deploy code that reads both old and new fields
4. Merge to the release branch — code propagates automatically
5. Existing rows will have NULL for the new column — confirm code handles this

**Steps — breaking (removed column):**
1. Deploy code that no longer references the old column
2. Merge to the release branch
3. Remove the column from each existing instance
4. Remove the column from the provisioning template

**Steps — modified column:**
1. Add a new column with the desired schema
2. Deploy code that reads the new column, with fallback to the old
3. Merge to the release branch
4. Migrate data from old column to new column (manual or script)
5. Remove the old column

**Verification:**
- [ ] Schema change documented in release notes
- [ ] Provisioning template updated (if applicable)
- [ ] Migration tested on at least one existing instance before wider rollout
- [ ] Code confirmed backward-compatible during the transition window

**Escalation:** if migration fails on the test instance, stop — do not proceed to
remaining instances. Go to Procedure 3, Schema Rollback.

---

## Procedure 3 — Rollback

**Trigger:** A release or migration causes an incident (see Rollback Triggers below).

**Rollback Triggers — immediate, no discretion:**
- Error rate exceeds **[PROJECT]** threshold across instances
- Critical functionality broken
- Data corruption detected
- Security vulnerability introduced

**Rollback Triggers — considered, use judgment:**
- Error rate elevated but below immediate threshold
- Performance degradation beyond **[PROJECT]** threshold
- Support complaints increasing

**Steps — code rollback:**
1. Revert the merge commit on the development branch
2. Merge the revert to the release branch
3. Confirm all dependent instances update automatically to the reverted code
4. Notify affected users of the rollback

**Steps — schema rollback:**
1. Revert the code change that depends on the new schema
2. Merge the revert to the release branch
3. Manually remove the new column from affected instances, if it was added
4. Update the provisioning template if the schema change was applied there

**Verification:** confirm the specific trigger condition (error rate, broken function,
etc.) no longer holds, on the same sample used to detect it originally.

**Note:** rollback via merge preserves git history and is reversible — prefer it over any
destructive alternative (direct database edits, force-push).

---

## Procedure 4 — Platform Account Incident Response

**Trigger:** one of the three scenarios below. **[PROJECT]** — applicable only if all
instances are hosted on a single platform account (a structural single point of failure at
the account level).

### Scenario 4a — Platform Account Suspension
**Cause:** **[PROJECT]**
**Detection:** **[PROJECT]**
**Steps:** **[PROJECT]**
**Prevention:** **[PROJECT]** — see this project's platform-constraints ADR for the
accepted-risk statement, if this scenario applies.

### Scenario 4b — Platform Account Compromise
**Cause:** **[PROJECT]**
**Detection:** **[PROJECT]**
**Steps:** **[PROJECT]** — include credential rotation and audit steps explicitly; do not
leave this implicit.

### Scenario 4c — Platform Infrastructure Outage
**Cause:** **[PROJECT]**
**Detection:** **[PROJECT]**
**Steps:** **[PROJECT]** — state explicitly whether a self-hosted fallback exists, or
whether this is an accepted risk of the platform decision.

---

*This is the global starter model. Copy into a new project's `standard-operating-procedures-local/`,
fill every **[PROJECT]** marker, remove this closing note. An unfilled marker in a live
project's SOP is a failure condition — an incomplete procedure is worse than none, since
it invites someone to follow it partway with false confidence.*
