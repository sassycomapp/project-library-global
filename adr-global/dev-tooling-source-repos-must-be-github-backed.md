---
document: "`dev-tooling-source-repos-must-be-github-backed` ADR — All Dev-Tooling Source Repositories Must Be GitHub-Backed"
doc-id: dev-tooling-source-repos-must-be-github-backed
state: Live
date-created: 2026-08-05T120000+0200
---
# `dev-tooling-source-repos-must-be-github-backed` ADR — All Dev-Tooling Source Repositories Must Be GitHub-Backed

**Status:** Confirmed — Sealed
**Date:** 2026-08-05
**Authority:** Derived from live diagnostic investigation 2026-08-05 (gbrain `sync_freshness` root-cause analysis), David's "simple, secure, robust, fit for purpose" credo
**Audience:** All developers and AI coding assistants working across dev-makepdlf, PDLF, and any future dev-tooling repositories

---

## Context

On 2026-08-05, a `gbrain doctor` health check surfaced a persistent `sync_freshness` FAIL against two sources — `pdlf` and `template-project-library` — that could not be cleared by running `gbrain sync --all`. Root-cause investigation (full trace preserved in conversation history) established:

- Both repositories were **local working trees with no `origin` remote configured**. `gbrain sync --all` reported them `up_to_date` but had nothing to push to and no upstream to reconcile against.
- gbrain's `sync_freshness` check only clears via a git-based short-circuit that requires (a) local `HEAD` matching the DB's stored `last_commit`, and (b) a clean working tree with no uncommitted tracked changes.
- Both repositories had uncommitted tracked changes sitting for multiple days, which is what actually caused the FAIL — not a defect in gbrain, but gbrain correctly reporting genuinely unsynced, unbacked-up work.
- Neither repository had any off-machine backup. All content existed in exactly one place: this WSL machine's local disk.

This is a structural gap, not a one-off mistake: any dev-tooling source with `local_path` set in gbrain but no GitHub remote will eventually reproduce this same failure, and carries permanent single-point-of-failure data-loss risk in the meantime.

---

## Decision

**Every dev-tooling source repository tracked by gbrain (i.e., every source with a `local_path` feeding the PDLF / dev-makepdlf ecosystem) must have a GitHub remote.** A local-only working tree is not an acceptable end state for any repository in this category.

### Two repository types, chosen by function

| Repo function | GitHub repo type | Rationale |
|---|---|---|
| A live, evolving tool or product — actively developed, never copied wholesale to start something else | Normal private repository | Standard version-controlled development with full history |
| A scaffold whose entire purpose is to be copied as the starting point for new, independent projects | GitHub **template repository** (`is_template: true`) | "Use this template" creates a clean, independent history for each spin-off — the scaffold's own edit history never leaks into projects built from it, and each new project doesn't risk being mistaken for a fork that pushes back into the scaffold |

### Established under this decision (2026-08-05)

| Source | GitHub repo | Type | Visibility | Default branch |
|---|---|---|---|---|
| `pdlf` | `github.com/sassycomapp/pdlf` | Normal repository | Private | `master` |
| `template-project-library` | `github.com/sassycomapp/template-project-library` | Template repository | Private | `master` |

**Visibility:** Private by default for all dev-tooling repositories. The only repositories in this account that are intentionally public are Anvil-generated application code repositories — that exception does not extend to PDLF/dev-tooling sources.

**Account:** All dev-tooling repositories are created under the `sassycomapp` GitHub account, matching the existing convention already in use for `project-library-global`.

---

## Why This Was Chosen Over the Local-Only Workaround

An earlier draft of this fix proposed documenting a permanent two-branch workflow in `daily-ops.md` — "repos with a remote push normally; repos without a remote skip the push step and just commit locally." That workaround was evaluated and rejected in favour of this ADR, on the following reasoning:

| Consideration | Local-only workaround | GitHub-backed (this decision) |
|---|---|---|
| Simplicity | Two permanent categories of workflow to remember, forever | One universal workflow — commit, push, sync |
| Security | Single point of failure — machine loss or disk failure is unrecoverable | Off-machine backup on every push |
| Robustness | `sync_freshness` will recur on any repo left uncommitted for 72h, indefinitely, by design | Same underlying gbrain behaviour, but the fix (commit + push) is now the same motion everywhere, and repos are never structurally isolated from backup |
| Fit for purpose | Treats a data-loss risk as a documentation footnote | Treats source-of-truth preservation as a first-class requirement for tooling this system depends on |

This directly follows the "simple, secure, robust, fit for purpose" credo: a workaround that has to be remembered forever is not simple, a repo that exists in one place is not secure, and a fix that leaves the underlying risk in place while suppressing the symptom is not robust.

---

## Required Pattern Going Forward

Any new dev-tooling repository created for the PDLF/dev-makepdlf ecosystem must be given a GitHub remote **at creation**, not retrofitted later:

```bash
cd <new-repo-local-path>
git init   # if not already a repo
git add -A
git commit -m "Initial commit"
gh repo create sassycomapp/<repo-name> --private --source=. --remote=origin --push
```

If the repository is a scaffold meant to be copied to start new projects (matching `template-project-library`'s function), mark it as a template repository immediately after creation:

```bash
gh api repos/sassycomapp/<repo-name> -X PATCH -f is_template=true
```

After any work session in any dev-tooling repo, commit and push before ending the session — see `daily-ops.md` for the exact per-repo command sequence.

---

## What to Do If You Find a Local-Only Dev-Tooling Repo

If you are unsure whether a gbrain-tracked source has a GitHub remote, check:

```bash
cd <local_path>
git remote -v
```

Empty output means no remote — treat this as a gap requiring the same remediation performed here: commit any pending work, create the GitHub repo with `gh repo create --source=. --remote=origin --push`, and re-run `gbrain sync --source <id>` to confirm `sync_freshness` clears.

---

## Consequences

- ✅ Every dev-tooling repository has off-machine backup — machine loss no longer means data loss for these sources
- ✅ One universal commit/push/sync workflow, not a permanently-remembered exception list
- ✅ `template-project-library`'s "copy the whole thing to start a new project" function is now structurally supported by GitHub's template-repo mechanism, rather than relying on manual copy discipline
- ✅ `sync_freshness` FAILs on these sources now correctly indicate real uncommitted work needing attention — not an unresolvable structural condition
- ⚠️ Any future dev-tooling source added without a remote reproduces this exact gap — this ADR's "Required Pattern Going Forward" must be followed at creation time, not treated as optional
- ⚠️ `daily-ops.md` must stay in sync with this decision — see companion update

---

## Related Documents

| Document | Relationship |
|---|---|
| `C:\projects-reference\workspace-reference\workflow reference\daily-ops.md` | Operational per-repo commit/push/sync commands implementing this decision |
| Handover — The 5 Step Plan (gbrain doctor improvement), 2026-08-04 | Prior work this investigation grew out of; points 2–4 of that plan may need re-sequencing now that source-of-truth locations have changed |

---

*End of `dev-tooling-source-repos-must-be-github-backed` ADR*
