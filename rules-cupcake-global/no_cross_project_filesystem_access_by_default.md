# Rule: No Cross-Project Filesystem Access by Default

## Harness
opencode

## What to block
Any WRITE-type tool call (Edit, Write, MultiEdit, NotebookEdit) whose
target file path resolves outside the current working directory's project
root, UNLESS the target falls inside one of the always-open shared-library
folders listed below, or the developer has issued an active permission
slip (grant) for that specific folder.

Reads are never blocked by this rule: Read and Grep remain free
everywhere, in every folder.

Always-open shared-library folders (reads and writes, no permission
needed, regardless of the current working directory):
- /mnt/c/dev/project-library-global
- /mnt/c/dev/dev-root
- /mnt/c/mybizz/mybizz-config-docs
- /mnt/c/mybizz/mybizz-os-docs
- /mnt/c/mybizz/logs
- /mnt/c/mybizz/memory-audit-reports (memory audit reports, written by the
  memory-functionality audit from any project)
- /tmp (scratch space; existing exemption)
- /home/dev-p/.config/cupcake and /home/dev-p/.config/opencode (the
  system's own control plane; existing exemptions)
- /mnt/c/mybizz/skills-collective (existing exemption)

Restricted project folders — writes blocked unless the agent's current
working directory IS that folder, or a permission slip is active for it:
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
"This path is outside the current project and not on the shared-library
list. Writing to another project folder requires a separate, explicit
developer permission slip for this occasion. Do not proceed based on a
previous access or an assumed standing permission."

## Reason
Project boundaries limit accidental damage, information exposure, and
scope expansion — but the boundary must not stall legitimate work. The
shared-library folders are where cross-project work legitimately lives
(divisions docs, standards, run logs), so they are always open. Restricted
project folders protect each project's own files: working in another
project is a deliberate, developer-approved occasion, granted through the
slip mechanism. Reads never damaged a project; they stay free.
