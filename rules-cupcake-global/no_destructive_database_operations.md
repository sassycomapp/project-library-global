---
document: "Rule: No Destructive Database Operations"
doc-id: no_destructive_database_operations
state: Live
date-created: 2026-09-05
---

# Rule: No Destructive Database Operations

## Harness
opencode

## What to block
Any bash tool call whose command contains a destructive or irreversible
database operation, including:
- `DROP` (table, database, schema, or index)
- `DELETE` with no `WHERE` clause present
- `TRUNCATE`
- a migration command whose content matches any of the above

This applies regardless of session state, task context, or any perceived
urgency.

## Decision
Block (deny). Do not allow the operation to proceed without explicit
developer approval for that exact operation.

## Message shown to the agent on block
"Destructive database operations are prohibited. Do not drop, truncate,
unrestrictedly delete, or irreversibly alter database data. Stop and
obtain explicit developer approval for the exact operation before
proceeding."

## Reason
Database operations can cause irreversible data loss and may affect
large amounts of information immediately. Such operations must never be
treated as ordinary autonomous development actions, and this rule
applies with no session-context exception of any kind.
