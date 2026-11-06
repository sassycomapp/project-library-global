---
title: "adr-ui-customization-approach"
doc-id: "mb-426881de"
updated: "2026-11-06"
---
# `ui-customization-approach` ADR — UI Customization Approach

**Status:** Accepted

---

## Context

Every client instance needs a consistent, professional interface. `m3-custom-theme` is the Material 3 theme dependency every Mybizz application uses: it holds the components, the layouts, the type scale and the palettes. This decision sets how far an application customises its interface beyond the theme.

---

## Decision

### The theme with controlled customization

`m3-custom-theme` is the foundation. An application customises its interface only by these means:

1. **Palette choice** — an application chooses one of the theme's palettes; the palette sets every colour, in light and dark mode.
2. **Theme roles** — components are styled with the roles the theme defines, set in the form template.
3. **Native layouts** — every layout shell is `NavigationRailLayout` or `NavigationDrawerLayout` ([[[default:adr-global/adr-htmltemplate-use|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md)).
4. **Component composition** — complex interfaces are built by composing theme components, never by replacing them.

A styling need the theme cannot meet is met by changing `m3-custom-theme` itself, so every application receives it. An application's own `theme.css` holds no brand styling.

---

## Consequences

- One design language across every client instance, set by one theme.
- A brand is expressed by its palette, never by application-specific CSS.
- No external UI framework: everything stays within Anvil's native capabilities.
- A change of the theme reaches every application that depends on it.

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:specifications-global/spec-ui-standards\|UI Standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) | The rules every form meets |
| [[[default:adr-global/adr-htmltemplate-use\|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md) | Native layouts for every layout shell |
| [[[default:adr-global/adr-navigation-lambda-link-open-form\|Navigation Lambda/Link/open_form]]](C:/dev/project-library-global/adr-global/adr-navigation-lambda-link-open-form.md) | How navigation works inside the layouts |
| [[[default:adr-global/adr-role-property-assignment-mechanism\|Role Property Assignment]]](C:/dev/project-library-global/adr-global/adr-role-property-assignment-mechanism.md) | Where roles are set |
| [[[default:adr-global/adr-dark-mode\|Dark Mode]]](C:/dev/project-library-global/adr-global/adr-dark-mode.md) | Light and dark mode from the theme's palettes |
