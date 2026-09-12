---
document: "Rule: No Bash-Mediated File Writes Without Grant"
doc-id: no_bash_mediated_file_writes_without_grant
state: Live
date-created: 2026-09-11
---

# Rule: No Bash-Mediated File Writes Without Grant

## Harness
opencode

## What to block
Any BASH tool call that writes, modifies, moves, or deletes files via
shell constructs, where the written target path resolves outside the
current working directory's project root — UNLESS the target falls inside
an always-open shared-library folder (the same list as
`no_cross_project_filesystem_access_by_default`), or the developer has
issued an active permission slip (grant) for that specific folder.

This rule closes the same boundary as the Edit/Write cross-project rule:
file tools are not the only way an agent writes files. Shell constructs
write files too, and they receive the identical check.

## Write-shapes inspected (strictly enumerated — nothing else)

A Bash command counts as a file write when it contains one of:

1. **Heredoc/interpreter write execution** — `python3 - <<`, `python - <<`,
   `python3 -c` containing `open(` with write mode, `perl -e` containing
   `open(` with write mode (the bulk-rewrite channels).
2. **In-place stream editing** — `sed -i` (any target path it names).
3. **Redirect writes** — `>` and `>>` followed by a path
   (`command > file`, `command >> file`), including `/dev/null`-free
   target paths.
4. **Stream-to-file** — `tee` (with or without `-a`).
5. **File mutation commands with named targets** — `cp`, `mv`, `rm`,
   `truncate`, `dd`, `touch`, `ln` where a target path is named.

Only the enumerated shapes are inspected. No other Bash command is
affected by this rule.

## The developer exception — absolute, never overridden

The developer's own physical work in a real terminal is never governed by
this rule and must never be hindered by it. This rule binds AI agents'
tool calls only — it evaluates agent-issued Bash tool calls
(`PreToolUse` on the Bash tool). The developer typing commands in their
own terminal is outside Cupcake's reach entirely, and nothing in this
rule, its message, or its enforcement may create a situation where the
developer is locked out of their own machine. If enforcement ever
conflicts with the developer working directly, the developer wins, always.

## Reads stay free

Read-only commands are never touched by this rule: `cat`, `grep`, `find`,
`ls`, `git status`, `git log`, `git diff`, `head`, `tail`, `wc`,
`md5sum`, and every other non-write command remain unrestricted, in every
folder.

## Grant mechanism — identical to the Edit/Write rule

The same grants file, the same `mg-grant` slips, the same expiry and
count semantics. A slip issued for a folder covers both governed channels
(file tools and this rule's Bash write-shapes) — nothing new for the
developer to learn.

Deny message shown to the agent on block:

"This Bash command writes outside the current project and not on the
shared-library list. Shell-mediated writes follow the same boundary as
file-tool writes: a separate, explicit developer permission slip is
required for this occasion. Do not proceed based on a previous access or
an assumed standing permission."

## Reason

The Edit/Write cross-project rule governs the four file tools; the Bash
channel was structurally ungoverned. Enforcement must deny the first
ungranted violation, not observe for repetition — there is no
exception-once-then-report design anywhere in this rule. The 2026-09-11
enforcement review recorded that an agent routed bulk file writes through
Python heredocs and sed inside Bash — a channel no rule watched — and the
defect was the absence of coverage, not the absence of intervention. This
rule makes the shell channel governed from the first command: same
boundary, same grants, same message. The enumerated write-shapes keep
false positives near zero; reads stay free; and the developer's own
terminal work is absolutely exempt, so the boundary can never lock the
developer out of their own machine.
