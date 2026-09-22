---
document: "Rule: No Autonomous Commits, Pushes, Merges, Releases, or Deployments"
doc-id: no_autonomous_commits_pushes_merges_releases_or_deployments
state: Live
date-created: 2026-09-05
---

# Rule: No Autonomous Commits, Pushes, Merges, Releases, or Deployments

## Harness
opencode

## What to block
Any bash tool call whose command performs a git commit, git push, or git
merge (`git commit`, `git push`, `git merge`), unless a live
commit-allowance slip exists for the target repository in the git grants
data file (amendment 2026-09-22, decision G1 of the Docs-Skills
Architecture Proposal).

**The verifiable allowance.** The developer issues the slip themselves
with `git-grant --repo <folder> --count N --minutes M` (the script lives
beside `mg-grant` in `~/.config/cupcake/bin/`). The slip writes an entry
into the git grants data file
(`~/.config/cupcake/policies/opencode/cup-git-grants-data.rego`, package
`cupcake.global.policies.git_grants_data`) keyed by the repository path in
canonical WSL form, carrying `count` and `expires_at_ns`. The compiled
policy resolves the target repository from the command (`git -C <path>`
when the command names one, otherwise the session working directory) and
allows the git commit, push, or merge only when a matching entry exists
with `count > 0` whose expiry has not passed — expired entries are pruned
by the plugin before evaluation, exactly as for path slips. Each allowed
git commit, push, or merge consumes one unit of the repository's
allowance, decremented by the plugin after the call. The agent never
issues the slip itself and never works around a denial.

**No allowance channel for publish and deploy.** Package publish
(`npm`/`yarn`/`pnpm publish`) and the named deploy CLI invocations are
outside the allowance: they always require the developer's explicit
approval in the current session, exactly as before this amendment.

## Decision
Block (deny) git commit, push, and merge unless the verifiable allowance
above is live for the target repository. Block publish and deploy actions
absolutely, per explicit developer approval in the current session only.

## Message shown to the agent on block
"This action makes changes authoritative or externally consequential. Do
not commit, push, merge, publish, release, or deploy without explicit
developer approval for this specific action."

## Reason
Preparing a change and making that change authoritative are separate
actions. Consequential actions remain under explicit developer control.
The commit-allowance channel (2026-09-22, G1) keeps that control while
removing the per-commit terminal round-trip: the developer pre-approves a
bounded, expiring, per-repository allowance in one action, and the
compiled policy verifies the token mechanically instead of trusting
session memory that no enforcement could check. Publish and deploy stay
outside the channel — those actions are externally consequential in ways
a count cannot bound.
