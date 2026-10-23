---
title: "adr-role-property-assignment-mechanism"
doc-id: "mb-0475ad64"
updated: "2026-10-23"
---
# `role-property-assignment-mechanism` ADR: Role Property Assignment in Code

## Status

**Accepted**

## Context

Anvil lets a component's `role` be set either in the Designer's Properties Panel or in code (`self.button_1.role = "submit"`). A component can carry several roles, as a space-separated string or a list of strings. Mybizz's property-setting rule is: if a property can be set programmatically, it is set programmatically.

## Decision

Set `role` in **code** (`self.component.role = "role-name"`), never in the Designer Properties Panel.

## Why

The property-setting rule applies to `role` because Anvil supports setting it in code. Roles set in code are visible in review and in version control, and cannot be lost in a Designer edit.

## Consequences

- Role assignment is done in Python code.
- Every design document and standard shows roles as code, not as Designer instructions.
- A wireframe never lists `role` in its Designer properties table.

## Related Documents

| Document | Relationship |
|---|---|
| `[[spec-material-3-theme]]` | Code examples of role assignment |
| Anvil Roles documentation | `https://anvil.works/docs/client/customisation/using-css/roles` |
