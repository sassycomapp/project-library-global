---
document: "Rule: No Rewriting or Destroying Development History"
doc-id: no_rewriting_or_destroying_development_history
state: Live
date-created: 2026-09-05
---

# Rule: No Rewriting or Destroying Development History

## Harness
opencode

## What to block
Any bash tool call whose command force-pushes (`git push --force`,
`git push -f`), rewrites history (`git rebase`, `git filter-branch`,
`git filter-repo`), amends an existing commit (`git commit --amend`), or
deletes a branch or tag (`git branch -d`/`-D`, `git push --delete`,
`git tag -d`), unless the developer has given explicit approval for that
specific operation in the current session.

## Decision
Block (deny). Do not allow the operation to proceed without explicit
approval.

## Message shown to the agent on block
"Development history and audit evidence are protected. Do not
force-push, rewrite history, amend commits, delete branches or tags, or
destroy evidence without explicit developer approval for the specific
operation."

## Reason
Version-control history provides recovery capability and preserves
evidence of what changed and when. Destructive or history-rewriting
operations can remove that capability and must remain under explicit
developer control.
