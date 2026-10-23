---
title: "adr-ui-customization-approach"
doc-id: "mb-426881de"
updated: "2026-10-23"
---
# `ui-customization-approach` ADR — UI Customization Approach

**Status:** Accepted

---

## Context

Every client instance needs a consistent, professional interface. Anvil provides Material Design 3 (M3) as a theme dependency, a drag-and-drop Designer, and the theme stylesheet `theme.css`. This decision sets how far the interface is customised beyond M3.

---

## Decision

### M3 Theme with Controlled Customization

The M3 theme dependency is the foundation. Customization uses only these means:

1. **M3 tokens** — colour palette, typography, spacing and elevation are set through M3 design tokens.
2. **CSS overrides** — `theme.css` holds brand styling that the tokens cannot express.
3. **Native M3 layouts** — every layout shell is `NavigationRailLayout` or `NavigationDrawerLayout` ([[[default:adr-global/adr-htmltemplate-use|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md)).
4. **Component composition** — complex interfaces are built by composing M3 components, never by replacing them.

### What M3 Provides

| Capability | M3 Support | Customization |
|---|---|---|
| Colour system | Dynamic colour, light and dark theme | Palette tokens |
| Typography | Material type scale | Font selection through tokens |
| Components | Buttons, cards, dialogs, data grids and others | Styling through roles and CSS classes |
| Elevation | Shadow system | Tokens |
| Layout | Navigation rail and drawer layouts | Used for every layout shell |

### The Designer and Code

The Designer places components and builds structure. Every property that can be set in code is set in code ([[[default:adr-global/adr-role-property-assignment-mechanism|Role Property Assignment]]](C:/dev/project-library-global/adr-global/adr-role-property-assignment-mechanism.md)). When the Designer resists precise positioning for more than ten minutes, the work moves to code.

### MUI Design Patterns

MUI (Material-UI) patterns are a source of inspiration only, never implemented directly. Anvil's component model differs from React's, and MUI's prop-based styling does not map onto it. The same visual outcomes (spacing, hierarchy, colour use) are reached through M3 tokens and CSS overrides.

---

## Consequences

- ✅ One design language across every client instance through M3 tokens
- ✅ Brand customization through palette tokens and CSS overrides
- ✅ No external UI framework: everything stays within Anvil's native capabilities
- ⚠️ Complex layouts need code: the Designer is a starting point, not the final word
- ⚠️ CSS overrides are checked after every M3 theme update

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-material-3-theme-component-scope]]](C:/dev/project-library-global/adr-global/adr-material-3-theme-component-scope.md) | Which M3 components are in scope |
| [[[default:adr-global/adr-design-rules\|Design Rules]]](C:/dev/project-library-global/adr-global/adr-design-rules.md) | Wireframe design rules |
| [[[default:adr-global/adr-htmltemplate-use\|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md) | Native M3 layouts for every layout shell |
| [[[default:adr-global/adr-navigation-lambda-link-open-form\|Navigation Lambda/Link/open_form]]](C:/dev/project-library-global/adr-global/adr-navigation-lambda-link-open-form.md) | How navigation works inside the M3 layouts |
| [[[default:specifications-global/spec-ui-standards\|UI Standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) | UI standards and component usage |
| `[[spec-material-3-theme]]` | M3 theme specification |

