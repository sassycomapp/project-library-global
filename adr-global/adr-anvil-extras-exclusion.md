---
title: "adr-anvil-extras-exclusion"
doc-id: "mb-d08beff2"
updated: "2026-11-11"
---
# Anvil Extras Exclusion
Status: Accepted

---

## Context

Anvil Extras is a third-party package that provides additional components and utilities for Anvil applications. Every Mybizz application uses `m3-custom-theme` (`UGGJBAZUZ74XZ7VU`), the full Material 3 theme built on Anvil's Material 3 Theme, as the sole UI framework.

---

## Decision

**Anvil Extras is out of scope and excluded from every Mybizz application.**

This exclusion applies to:
- All Anvil Extras components (Tabs, MultiSelectDropDown, Autocomplete, Quill, Switch, Slider, RadioGroup, CheckBoxGroup, Popover, etc.). The ban covers Anvil Extras' versions only: the Material 3 Theme's own `Switch`, `Slider` and `RadioButton` are permitted.
- Any third-party packages not included in `m3-custom-theme`
- Any custom JavaScript frameworks or non-standard widget dependencies

**Native M3 components** provided by `m3-custom-theme` are the only permitted UI components. If a required component is not available in the theme, it must be:
1. Composed from available M3 primitives (for example, a footer from Cards and Links)
2. Built as a Custom Component using native M3 components
3. Rejected as out of scope if composition is not feasible

---

## Rationale

1. **CSS conflicts**: Mixing Anvil Extras with M3 produces hard-to-diagnose CSS conflicts
2. **Maintenance burden**: Third-party packages introduce external dependencies and update risks
3. **Consistency**: Using only M3 components ensures consistent styling and behavior
4. **Support**: Official Anvil components have direct support from Anvil.works

---

## Consequences

### Blocked components (always excluded)
- Anvil Extras' Tabs, MultiSelectDropDown, Autocomplete, Quill, Switch, Slider, RadioGroup, CheckBoxGroup, Popover
- Any component not in `m3-custom-theme`

### Allowed patterns
- Native M3 components from the theme dependency
- Custom Components built from native M3 primitives
- Material Web Components only if explicitly required and approved via ADR

