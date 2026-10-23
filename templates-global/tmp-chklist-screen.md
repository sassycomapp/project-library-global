# Compliance Checklist — {FormName} Screen

**Screen:** `{path to the screen file}`
**Wireframe:** `{path to its wireframe}`
**Date:** {date}

Mark each item `[x]` when it passes, or `N/A` with the reason, and give the evidence.

---

## A. Wireframe fidelity

- [ ] Every component in the wireframe's Section 2 appears in the screen (list each one)
- [ ] Components hidden on load (dashed border) are excluded
- [ ] No extra components
- [ ] Component hierarchy matches the wireframe
- [ ] Component types match the wireframe

## B. Page chrome exclusion

- [ ] No left sidebar, app bar, footer or navigation
- [ ] The screen contains only what the wireframe declares

## C. Repeating panels and row templates

- [ ] DataGrid row content is not rendered; a placeholder annotation is shown
- [ ] No RepeatingPanel present

## D. Sample data

- [ ] Sample data fits the application's business and currency
- [ ] No Lorem ipsum, no production data

## E. MUI aesthetic overlay (all 9 variables)

- [ ] 1. Surface distinction
- [ ] 2. Card shadow
- [ ] 3. Card radius — 8px
- [ ] 4. Heading weight — 600
- [ ] 5. Dividers — outline-variant at 40% opacity
- [ ] 6. Hover opacity — 0.08
- [ ] 7. Pressed and focused — 0.12
- [ ] 8. App bar
- [ ] 9. Left nav

## F. Colour and token compliance

- [ ] No hardcoded hex, except the semantic status colours the standard allows
- [ ] No hardcoded rgba
- [ ] Every other colour comes from a CSS custom property

## G. Component compliance

- [ ] No Label, HTMLTemplate, SidesheetContent or HtmlPanel
- [ ] Every component is from the approved M3 list

## H. Naming and structure

- [ ] Prefixes are correct (hdg_, txt_, nav_, card_, flow_, col_, dg_, plot_)
- [ ] Material Icons imported

## I. Output quality

- [ ] Renders correctly
- [ ] Typography scale correct
- [ ] Spacing on the 4px grid
- [ ] Dark mode — a `@media (prefers-color-scheme: dark)` block with the token overrides
- [ ] Reduced motion present

---

## Discrepancies found

{Each discrepancy, or "None".}
