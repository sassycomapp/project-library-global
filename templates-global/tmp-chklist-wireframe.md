# Checklist — {FormName} Wireframe

**Wireframe:** `{path to the wireframe file}`
**Date:** {date}
**Auditor:** {who checked it}

Mark each item `[x]` when it passes, or `N/A` with the reason. Give the line number of the evidence.

---

## A. Role assignment ([[[default:adr-global/adr-role-property-assignment-mechanism|Role Property Assignment]]](C:/dev/project-library-global/adr-global/adr-role-property-assignment-mechanism.md))

- [ ] The properties table does not list `role` as a Designer property
- [ ] No annotation says "set role in Designer"
- [ ] Any role mentioned is noted as set in code

## B. Responsive behaviour ([[[default:adr-global/adr-responsive-behaviour-mechanism|Responsive Behaviour Mechanism]]](C:/dev/project-library-global/adr-global/adr-responsive-behaviour-mechanism.md))

- [ ] No breakpoint tables or pixel-based responsive rules
- [ ] Containers that wrap or stack carry `wrap_on` annotations

## C. HTMLTemplate ([[[default:adr-global/adr-htmltemplate-use|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md))

- [ ] No `HtmlTemplate` component anywhere in the wireframe
- [ ] No reference to the `anvil_slot_repeat` property

## D. Layout shells

- [ ] A layout wireframe uses `NavigationRailLayout` or `NavigationDrawerLayout`
- [ ] No custom layout shell

## E. DataRowPanel

- [ ] DataRowPanel uses the `drp_` prefix
- [ ] DataRowPanel is used for DataGrid row templates
- [ ] DataRowPanel is listed in the component annotations

## F. M3 component standard

- [ ] Every component is in the approved M3 list or the approved custom list
- [ ] InteractiveCard uses only `elevated`, `filled` or `outlined`
- [ ] No `SidesheetContent`, `Label` or `HtmlPanel` component
- [ ] Cards use the `Card` component, not a `ColumnPanel` with a role class

## G. Icon component

- [ ] Icon components use the `ico_` prefix
- [ ] A decorative icon is an `IconButton`
- [ ] An icon-only button with a click handler is an `IconButton` with the `btn_` prefix

## H. Icon names

- [ ] Every icon annotation uses the `mi:` prefix

## I. Writeback properties

- [ ] The properties table marks writeback (W) for every writeback component
- [ ] No writeback is listed for a non-writeback component

## J. Max-width values

- [ ] Max-width annotations match the form type's value in the standard

## K. Card radius

- [ ] Card annotations reference the 8px radius

## L. Tags and badges

- [ ] Tags and badges are composed from `m3.Button` or `m3.Card`
- [ ] No `Label` component is used for a tag or badge

## M. Colour

- [ ] The wireframe holds no colour, theme or dark mode content

## N. Carousel viewport

- [ ] A carousel viewport is a ColumnPanel with role-driven CSS

## O. Section structure ([[[default:adr-global/adr-design-rules|Design Rules]]](C:/dev/project-library-global/adr-global/adr-design-rules.md))

- [ ] Section 1 — Introduction present
- [ ] Section 2 — Wireframe Diagram present
- [ ] Section 3 — Properties Table present
- [ ] No sample data in the wireframe
- [ ] No behaviour text in the wireframe diagram
- [ ] Containers are drawn as containers, with their names inset in the border

---

## Result

**Status:** {PASS, or FAIL with the items to fix}
