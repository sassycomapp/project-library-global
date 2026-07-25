---
document: PDLF Standards Library — M3 Design & Component Standards
doc-id: global-0065
state: Live
date-created: 2026-07-25T150027+0200
---
# PDLF Standards Library — M3 Design & Component Standards

**Location:** `C:\pdlf\standards-library\m3-design-standards.md`
**Scope:** Project-agnostic component and navigation patterns. Specific token *values* (colors,
exact spacing scale) are project-specific and belong in that project's own DESIGN.md.
**Source:** Extracted from `mb-3-cs` (anvil-spec-table.md, architecture.md,
screen-production-standard.md), generalized for reuse.

---

## 1. Component Prefix Convention

| Category | Component | Prefix |
|---|---|---|
| Typography | Heading | `hdg_` |
| Buttons | Button / IconButton / ToggleIconButton | `btn_` |
| Input | TextBox / TextArea | `txt_` |
| Input | DropdownMenu | `dd_` |
| Input | Checkbox | `cb_` |
| Input | RadioButton | `rb_` |
| Input | DatePicker | `dp_` |
| Input | FileLoader | `fu_` |
| Containers | ColumnPanel | `col_` |
| Containers | FlowPanel | `flow_` |
| Containers | RepeatingPanel | `rp_` |
| Containers | Data Grid | `dg_` |
| Display | Card | `card_` |
| Display | CardContentContainer / SidesheetContent | `col_` |
| Menus | ButtonMenu / IconButtonMenu / AvatarMenu | `menu_` |
| Navigation | Link (sidebar) | `nav_` |
| Integrations | Plot | `plot_` |

A consistent prefix convention is the standard, not the specific list above — a project may add
component types, but should keep one prefix per component category.

## 2. Button Hierarchy

One filled (primary) button per screen. Outlined for secondary actions (cancel, back). Text-only
for low-emphasis tertiary actions. This 1-primary-per-screen rule is a hard constraint, not a
guideline — more than one filled button on a screen is a compliance failure, not a style choice.

## 3. Typography Standards

| Use | Standard |
|---|---|
| Page title | Headline-large |
| Section title | Headline-small |
| Card/panel title | Title (medium equivalent) |
| Body copy | Body-medium |
| Field label | Label-medium |
| Caption | Body-small equivalent |
| Never use | Legacy `Label` component — M3 apps use `Text`/`Heading` instead |

## 4. Input Standards

- TextBox/TextArea/DropdownMenu/DatePicker: outlined appearance for forms.
- DropdownMenu items set in code, not in the Designer.
- Password fields: `hide_text = True` in the Designer.
- Validation failure: use the component's error/outlined-error state with the error message in
  the supporting text or placeholder — not a separate ad-hoc error label.

## 5. Container and Layout Rules

- ColumnPanel: default structural container.
- FlowPanel: preferred for responsive wrapping and horizontal layouts; orientation set in code.
- Avoid XYPanel for primary layout work.
- Card content goes inside the auto-created CardContentContainer, not directly inside the Card.

## 6. Components vs. Widgets

- **Custom Component** (should be the default, ~90% of cases): a reusable Anvil Form written
  entirely in Python — supports data bindings, events, properties, Designer configuration.
- **Widget** (~10%, exception case): a wrapper around third-party JS/HTML/CSS via an HTML panel —
  only for third-party JS libraries, browser APIs, or custom DOM rendering needs.
- Pattern: the Custom Component handles layout/data/events/API; a Widget, if needed, sits hidden
  behind the component's interface, keeping the rest of the app pure Anvil.

## 7. Navigation Patterns

**Layout shell:** Use the native M3 Layouts — `NavigationRailLayout` or `NavigationDrawerLayout` — for the admin and customer portal shells. `HTMLTemplate` is banned per the `htmltemplate-use` ADR.

**Authenticated (internal) navigation:**
- Plain `Link` components in the sidebar, not `NavigationLink`.
- Lambda click handlers with **mandatory loop-variable capture**:
  ```python
  lambda e, fn=form_name, a=attr_name: self._nav_click(fn, a)
  ```
  Without this capture, every lambda in a loop resolves to the last loop value — a well-known,
  specific failure mode, not a hypothetical one.
- `open_form(string)` for parameterised internal navigation (row clicks, detail views).

**Public/routed navigation:**
- Use the Routing dependency (`@router.route(...)`) for public, shareable, bookmarkable pages —
  not the internal pattern above.
- Route constructor signature: `def __init__(self, routing_context, **properties)`.
- Access route parameters via `routing_context.params['id']`.

**`navigate_to` is never used** — it is not compatible with the content panel navigation pattern.
**`NavigationLink` is not used for sidebar navigation** — the `nav_` prefix in component naming
refers to Link components styled for sidebar use, not NavigationLink components.

## 8. Sidesheet

- Correct term is **Sidesheet**, not "Slidesheet."
- Native M3 pattern using `NavigationRailLayout`, enabled via `show_sidesheet = True`, contained
  in `SidesheetContent`.
- Best suited to guided multi-step workflows: pass accumulated data via `self.item` between
  steps; submit to the server once, at the final step — not a server call per step.

## 9. Restricted / Avoid List

- Anvil Extras — excluded by policy in at least one real project; confirm per-project whether
  this restriction applies before assuming it's universal.
- Legacy `Label` — superseded by `Text`/`Heading` in M3.
- RichText — use sparingly; not a core M3 pattern.

## 10. Semantic Status Colors — Fixed Platform Standard, Not a Per-Project Decision

Material Design 3 does not ship success/warning/pending color roles natively — the only semantic
status role M3 provides is **Error**. This gap is closed once, permanently, at the platform
level, not decided per project:

| Role name | Meaning | Value | Notes |
|---|---|---|---|
| `status-success` | Success / completed | **#2DB52D** (RGB 45, 181, 45) | Add as a custom color in Anvil's Color Scheme editor |
| `status-pending` | Pending / unresolved | **#FF6600** (RGB 255, 102, 0) | Add as a custom color in Anvil's Color Scheme editor |
| `status-error` | Failure | **#FF0000** (RGB 255, 0, 0) | May reuse M3's native `Error` role, or be added as its own custom color — confirm which per project's Color Scheme setup |

These three values and role names are fixed for every project built under this system. A project
never redefines them — reference `status-success` / `status-pending` / `status-error` by role
name, never by a re-chosen or re-typed hex value.

## 11. Typography Scale (M3 Spec Defaults)

| Scale | Size | Line Height | Weight | Use Case |
|---|---|---|---|---|
| Display | 57px | 64px | 400 | Hero headlines (rare) |
| Headline Large | 32px | 40px | 400 | Page titles |
| Headline Small | 22px | 28px | 500 | Section headers |
| Title | 18px | 24px | 500 | Card titles |
| Body | 14px | 20px | 400 | Standard text |
| Button | 14px | 14px | 500 | Button labels |
| Label | 12px | 16px | 500 | Form labels |
| Caption | 12px | 16px | 400 | Helper text |

These are M3 spec defaults. A project overriding any of these should state the override
explicitly in its own Canonical design document, not silently diverge.

## 12. Spacing Scale (4px Base Unit — Standard Default)

| Token | Value |
|---|---|
| `--space-1` | 4px |
| `--space-2` | 8px |
| `--space-3` | 12px |
| `--space-4` | 16px |
| `--space-6` | 24px |
| `--space-8` | 32px |

## 13. Elevation (M3 Convention)

| Element | Elevation |
|---|---|
| Surface | 0dp |
| Card (Elevated) | 2dp |
| Card (Tonal) | 0dp |
| Dialog | 24dp |
| Navigation Rail / App Bar | 0dp (border only) |

## 14. Component State Pattern (Token-Based, Never Hardcoded)

Every interactive component should define behavior for: Default, Focused, Error, Disabled,
Read-only (inputs); Default, Hover, Active/Pressed, Disabled, Loading (buttons); Default, Hover,
Selected, Disabled (cards). Each state references token roles (`Primary`, `Error`, `Outline`,
`On Disabled`, etc.) — never a literal hex value. Disabled states use ~38% opacity by convention.

## 15. Responsive Mechanism — `wrap_on`, Not CSS Breakpoints

Anvil's responsive behavior is controlled per-container via `wrap_on`, not pixel-based CSS
breakpoints:
- `wrap_on = mobile` where a container should wrap/stack on small screens
- `wrap_on = never` where a fixed layout should not rearrange
- `NavigationRailLayout` / `NavigationDrawerLayout` auto-collapse on small screens automatically

## 16. Layout Patterns by Screen Type — Single Source of Truth

**This table is the one authoritative source for these values** — `screen-and-wireframe-
production-standards.md` and any project's own design document should reference this table
rather than restate it, to avoid the two independently-drifting copies found during audit.

| Screen Type | Max Width | Container Pattern |
|---|---|---|
| Auth | 400px | Centred card |
| List | 1200px | Full-width, header + filters + grid |
| Dashboard | 1200px | Full-width, metric cards |
| Editor/Viewer/Forms | 900px | Full-width, sectioned panels |
| Public pages | 900px | Full-width, content sections |
| Settings | 1000px | Full-width, tab bar + panels |
| Onboarding | 600px | Centred card, step indicator |
| Card (grid item) | 320px | Embedded |
| Modal form | 480px | Overlay |
| Modal detail | 640px | Overlay |

## 17. Accessibility Requirements (Universal, Not Project-Specific)

- **Target:** WCAG 2.1 Level AA.
- **Contrast:** ≥4.5:1 normal text, ≥3:1 large text (≥18px, or ≥14px bold), ≥3:1 UI components.
- **Keyboard:** all functionality reachable via keyboard; logical tab order; visible focus ring
  on every interactive element; modals/sidesheets trap focus until closed, Escape closes them.
- **Screen readers:** `aria-label` on icon-only buttons; `<label for>` on every input;
  `aria-expanded`/`aria-selected`/`aria-disabled` as appropriate; `aria-live="polite"` for dynamic
  updates; semantic HTML (`<button>`, `<nav>`, `<main>`) over generic `<div>`.
- **Never rely on color alone:** pair error/success/required states with an icon and text label,
  not color alone.
- **Touch targets:** minimum 44×44px, recommended 48×48px, minimum 8px between adjacent targets.
- **Motion:** respect `prefers-reduced-motion`; respect `prefers-color-scheme` for dark mode.

## 18. M3 Component Support Levels

The M3 theme dependency fully supports these components natively — use them directly, no custom
composition needed: `Switch`, `Slider`, `RadioButton`, `Checkbox`, `Button`, `IconButton`,
`NavigationLink`, all input components (`TextBox`, `TextArea`, `DropdownMenu`), all layout
components (`ColumnPanel`, `FlowPanel`, `DataGrid`, `Card`).

These components are only **partially** supported and require custom composition via Panels,
Cards, and Buttons: Chips, Snackbar, Bottom Sheet, Tabs, Date Picker. Do not expect a drop-in
native version of these — build them from the fully-supported primitives above.

## 19. Custom Component Reuse Threshold

A reusable interactive UI element is only justified as a shared custom component when it is
used in two or more locations. A component used in only one place must remain local/form-specific
and is explicitly downgraded from custom-component status. This prevents premature abstraction
and the maintenance cost of unused shared components.

Before extracting a component: verify it has two or more confirmed use sites. If it does not,
keep it local and document the decision.

## 20. Empty State Mandatory Pattern

Every data-driven form must include an empty state — the experience shown when no data
exists. An empty state is composed of exactly four elements:

1. **Icon** — decorative, non-interactive, M3-conformant
2. **Heading** — describes the empty condition
3. **Body text** — explains what will appear here and how to create it
4. **Primary action button** — resolves the empty state (e.g. "Create first X")

No data-driven form ships without an empty state. This ensures consistent first-run and
zero-data experiences across all instances.

## 21. MUI Aesthetic Overlay — Fixed Variable Set

The MUI aesthetic overlay is a bounded, deliberate set of exactly 9 CSS custom properties
applied as a visual layer on top of M3. It bridges M3 and MUI visual language without
breaking M3's token system.

**Overlay variables (all CSS custom properties):**

1. Surface distinction (card vs. background elevation)
2. Card shadow (box-shadow)
3. Card border radius
4. Typography heading weight
5. Divider opacity
6. State hover opacity
7. State pressed opacity
8. App bar styling
9. Left navigation styling

**Explicitly NOT affected by the overlay:** button radius, dialog radius, input radius,
nav item radius, data grid radius, font family, spacing scale, color role structure.
These remain as M3 defines them.

**Rule:** The overlay is a named, versioned design decision — never an ad-hoc override.
Any variable added to the overlay requires an ADR.

## 22. Approved/Restricted Component Model

Every component in the project falls into one of two tiers:

| Tier | Definition | Rule |
|---|---|---|
| **Approved** | Components permitted for use in any form | Listed in `spec-m3_component_mapping.md` |
| **Restricted** | Components that must not be used | Explicitly banned with documented reason |

**Restricted components (banned):**
- Legacy `Label` component — replaced by Material Design text components
- HTMLTemplate — unless justified by a specific platform gap (not general layout)
- Any component not in the approved list — treated as restricted by default

Before adding a new component type: verify it is in the approved list. If it is not and
is genuinely needed, propose addition via ADR.

---

---

*M3 Design Standards v1.3 — Added Two-Use Minimum Threshold (§19), Empty State Mandatory Pattern (§20), MUI Aesthetic Overlay Fixed Variable Set (§21), Approved/Restricted Component Model (§22). Extracted from mb-3-cs custom-component-requirements-matrix.md and internal-standards-anvil-wireframe-conversion.md.*
