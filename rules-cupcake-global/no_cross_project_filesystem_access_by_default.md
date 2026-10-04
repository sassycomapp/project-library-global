---
title: "no_cross_project_filesystem_access_by_default"
doc-id: "mb-9a9b54d6"
updated: "2026-10-04"
---
# Rule: No Cross-Project Filesystem Access by Default

## Harness
opencode

## What to block
Any WRITE-type tool call (Edit, Write, MultiEdit, NotebookEdit) whose
target file path resolves outside the current working directory's project
root, UNLESS the target is `/tmp` (the only always-open exemption, listed
below), or the developer has issued an active permission slip (grant) for
that specific folder.

Reads are never blocked by this rule: Read and Grep remain free
everywhere, in every folder.

Always-open exemption (reads and writes, no permission needed, regardless
of the current working directory) — exactly one entry:
- /tmp (scratch space)

Restricted project folders — writes blocked unless the agent's current
working directory IS that folder, or a permission slip is active for it:
- /mnt/c/data-mybizz-mgt (restricted-with-slip, amendment 2026-09-22,
  decision G2 of the Docs-Skills Architecture Proposal; the compiled
  treatment is unchanged — this folder was already denied without a slip
  as an outside-cwd path, and the list entry documents that routing)
- /mnt/c/dev/dev-makepdlf/makepdlf-project-library
- /mnt/c/dev/dev-mb-3-cs/mb-3-cs
- /mnt/c/dev/dev-mb-3-cs/mb-3-cs-project-library
- /mnt/c/dev/dev-mb4ecom/mb4ecom
- /mnt/c/dev/dev-mb4ecom/mb4ecom-project-library
- /mnt/c/dev/dev-mb5pdlf/mb5pdlf
- /mnt/c/dev/dev-mb5pdlf/mb5pdlf-project-library
- /home/dev-p/memory-governor

A prior approval, for a prior occasion, does not authorise a further
access to the same or a different external project.

## Decision
Block (deny) writes only, per the above. Never block a read.

## Message shown to the agent on block
"This path is outside the current project and not exempt. Writing to
another project folder requires a separate, explicit developer permission
slip for this occasion. Do not proceed based on a previous access or an
assumed standing permission."

## Reason
Project boundaries limit accidental damage, information exposure, and
scope expansion — but the boundary must not stall legitimate work.
Cross-project work is legitimate but deliberate: each occasion is granted
through a slip. `/tmp` stays open as scratch space because nothing there
is authoritative. Restricted project folders protect each project's own
files: working in another project is a deliberate, developer-approved
occasion, granted through the slip mechanism. Reads never damaged a
project; they stay free.
