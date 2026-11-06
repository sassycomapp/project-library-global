---
title: "adr-htmltemplate-use"
doc-id: "mb-f7c956d1"
updated: "2026-11-06"
---
# `htmltemplate-use` ADR: HTMLTemplate Use

## Status

Accepted

## Context

Anvil's `HTMLTemplate` component builds a form or layout from raw HTML. `m3-custom-theme` ships complete native layouts, `NavigationRailLayout` and `NavigationDrawerLayout`, and every positioning need a form has is met by the theme's containers and roles. An HTML form template, `form_template.html`, is a different thing: it is Anvil's file format for a form, and it names native components; it is not the `HTMLTemplate` component.

## Decision

The `HTMLTemplate` component is banned. Every form and layout is built from `m3-custom-theme` components and the theme's two native layouts.

## Consequences

- No form uses the `HTMLTemplate` component; the test suite's form scan rejects it.
- Every form template is an HTML form template that names theme components, as [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) sets out.
- A future need that no theme component or layout can meet is decided by a new ADR before any form uses `HTMLTemplate`.

## Alternatives Considered

- **Allow `HTMLTemplate` for specific edge cases.** Rejected. Every known case has a native alternative, and an exception opens an HTML route around Anvil's component model.
- **Allow `HTMLTemplate` with ADR approval per use.** Rejected. A per-use approval adds governance with no case that needs it.

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-ui-standards\|UI Standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) | Sets the components every form uses; lists `HTMLTemplate` as banned |
| `[[spec-component-properties]]` | Documents component properties; for `HTMLTemplate`, this ADR governs |
| [[[default:adr-global/adr-anvil-extras-exclusion]]](C:/dev/project-library-global/adr-global/adr-anvil-extras-exclusion.md) | Excludes third-party packages; this ADR extends the exclusion principle to `HTMLTemplate` |
| [[[default:adr-global/adr-ui-customization-approach\|UI Customization Approach]]](C:/dev/project-library-global/adr-global/adr-ui-customization-approach.md) | Broader UI customization approach; this ADR is a specific component exclusion |
| [[[default:adr-global/adr-role-property-assignment-mechanism\|Role Property Assignment Mechanism]]](C:/dev/project-library-global/adr-global/adr-role-property-assignment-mechanism.md) | Roles give the styling an HTML escape hatch would otherwise be used for |
