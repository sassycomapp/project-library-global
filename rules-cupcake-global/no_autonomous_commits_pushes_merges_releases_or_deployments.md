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
Any bash tool call whose command performs a git commit, git push, git
merge, or an equivalent publish, release, or deployment action (e.g.
`git commit`, `git push`, `git merge`, `npm publish`, a deploy CLI
invocation), unless the developer has given explicit approval for that
specific action in the current session.

## Decision
Block (deny). Do not allow the action to proceed without explicit
approval.

## Message shown to the agent on block
"This action makes changes authoritative or externally consequential. Do
not commit, push, merge, publish, release, or deploy without explicit
developer approval for this specific action."

## Reason
Preparing a change and making that change authoritative are separate
actions. Consequential actions remain under explicit developer control.
