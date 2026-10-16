---
title: "cup-protect-cupcake-control-plane"
doc-id: "mb-4c83ef87"
updated: "2026-10-16"
---
# Rule: Protect the Cupcake Control Plane

## Harness
opencode

## What to block
1. Any file-writing tool call (edit, write, multiedit, notebookedit,
   patch, matched in any letter case) whose target is part of Cupcake's
   control plane. The same targets are blocked when a Bash command writes
   to them (redirect, copy, move, `sed -i` and the other write shapes
   detected by the cross-project rule). The control plane is:
   - the live Cupcake configuration folder, `~/.config/cupcake/`
     (`/home/dev-p/.config/cupcake/`): rule files, both grants data files,
     the fallback home and the rulebook;
   - the OpenCode plugin, `~/.config/opencode/plugin/cupcake*`
     (`/home/dev-p/.config/opencode/plugin/cupcake*`);
   - the rule-authoring source folder,
     `C:\dev\project-library-global\rules-cupcake-global\`
     (`/mnt/c/dev/project-library-global/rules-cupcake-global/`);
   - any `.cupcake/opencode.json`, in any folder.
2. Any Bash command that invokes a grant-issuing tool by name: `mg-grant`,
   `git-grant` or `net-grant`, whatever its flags or target.

This block is absolute. No grant is checked and none can unlock it.

## Decision
Block (deny). Severity CRITICAL.

## Message shown to the agent on block
For a write to the control plane:
"This path is part of the Cupcake enforcement system itself (policy
folder, grants files, plugin, or rule-authoring source). It may never be
created, edited, or deleted by an agent, through any tool or mechanism,
granted or not. Only the developer, acting directly and outside this
session, may change it."

For a grant-issuing command:
"Grant-issuing commands (mg-grant, git-grant, and equivalents) may not be
run by the agent under any circumstances. Only the developer may issue a
grant, directly in their own terminal. If a grant is needed, stop and ask
the developer to issue it and supply the resulting slip."

## Reason
An agent that can change the rules that govern it is not governed. The
grants data files live in the configuration folder, so write access there
would let an agent issue its own grants. The plugin is the enforcement and
grant-counting engine. A rule source written by an agent would be compiled
and deployed as trusted on the next legitimate rule rebuild. A
`.cupcake/opencode.json` can switch the plugin off, redirect the grants
file or swap the programs it runs. The grant tools write grants as their
whole job, which no write-shape check can see, so they are blocked by
name. The developer keeps every one of these actions in the terminal,
which Cupcake does not govern.
