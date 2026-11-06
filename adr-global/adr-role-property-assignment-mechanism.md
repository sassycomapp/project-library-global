---
title: "adr-role-property-assignment-mechanism"
doc-id: "mb-0475ad64"
updated: "2026-11-06"
---
# `role-property-assignment-mechanism` ADR: Role Property Assignment

## Status

**Accepted**

## Context

Anvil lets a component's `role` be set in the form template or in code (`self.button_1.role = "submit"`). A component can carry several roles, as a space-separated string or a list of strings. Every Mybizz form is an HTML form template held in version control and reviewed before it is committed.

## Decision

Set `role` in the **form template**, as `prop:role="role-name"`. Code sets a role only where the role changes while the form is open.

## Why

A role in the form template is visible in review and in version control, sits beside the component it styles, and is checked by the test suite's form scan. A role that changes with the form's state belongs in the code that changes the state.

## Consequences

- Every screen requirement and spec sheet states each component's role.
- `mb-form-builder` writes every fixed role into the form template.
- A role set in code is a defect unless the role changes while the form is open.

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-ui-standards\|UI Standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) | States the rule for every form |
| Anvil Roles documentation | `https://anvil.works/docs/client/customisation/using-css/roles` |
