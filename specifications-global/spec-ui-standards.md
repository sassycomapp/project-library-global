---
title: "spec-ui-standards"
doc-id: "mb-8d841a9d"
updated: "2026-11-06"
---
# Mybizz — UI Standards

## 1. What This Specification Is

- This specification sets the rules every form of every Mybizz Anvil application meets.
- [[[default:specifications-global/mo-ui-production]]](C:/dev/project-library-global/specifications-global/mo-ui-production.md) sets out how forms are produced to these rules.
- Why: one set of rules, applied identically to every form, lets an agent build and check a form without choosing between methods.

## 2. Theme

1. Every Mybizz application uses `m3-custom-theme` as its only theme dependency.
2. The theme's package name is `m3`. In code and in form templates, `m3.` always means `m3-custom-theme`.
3. The theme's documentation, in the `m3-custom-theme-project-library` repository, is the single source for every component's type, properties, events and writeback property:
   - `docs/base-inventory.md` for the components the theme inherits;
   - `docs/components/<Component>.md` for each component the theme adds.
4. A component property that is not in that documentation does not exist. No agent guesses a component, a property or a value.

Why: one theme and one source of component facts stop two component sets, or two descriptions of one component, from entering an application.

## 3. Components

1. **Design from the full theme.** Each element of a screen uses the `m3-custom-theme` component that serves it best, chosen from the whole component set (for example Chip, Tabs, Dialog, Snackbar, FloatingActionButton, ListItem, TopAppBar, NavigationBar, ButtonGroup, Badge, LoadingIndicator). A plainer component is never used where a better-fitting theme component exists.
2. **Theme first.** A form uses an Anvil standard component only where the theme has no component for that purpose.
3. **Allowed standard components.** The Anvil standard components a form may use are exactly those listed in `approved_components` in the application's `ts-config.yaml`.
4. **Banned components:** `Label` (use the theme's `Text`), `HtmlTemplate`, `HtmlPanel`, and every Anvil Extras component.
5. **Custom components** exist only where the application's custom component register names them. A custom component is built from theme components.
6. **Repeated data** is shown with a `RepeatingPanel` and an item template form, never with HTML loops or strings built in code.

## 4. Form Files

1. Every form is a package form: a folder `client_code/<package path>/<FormName>/` holding exactly two files:
   - `form_template.html`, the form's layout;
   - `__init__.py`, the form's Python class.
2. Every form template is HTML. No form template is written in YAML.
3. A form template names each theme component by the type path its documentation gives, for example `m3._Components.Card`, and sets each property as `prop:<name>="<value>"`.
4. Theme layouts, slots and blocks follow Anvil's HTML template syntax: `<anvil-form layout="...">`, `<anvil-block slot="...">`, `<anvil-slot name="...">`.
5. A form's identity is its module path: the folders below `client_code`, then the form name, joined by dots (for example `auth.LoginForm`). The module path is unique, even where two forms share a name.
6. Every reference to a form uses its module path: the access matrix, the screen requirement, the spec sheet, routes and `anvil.yaml`.
7. Code opens a form through its imported class or its route, never through a bare name string.
8. Package folders are permanent. Removing a form removes only that form's own folder.

Why: HTML templates are the format Anvil's own agent rules prefer, they are readable in review and in version control, and a module path is the only form name Anvil guarantees to be unique.

## 5. Naming

1. Component names follow the prefixes in [[[default:specifications-global/spec-nomenclature]]](C:/dev/project-library-global/specifications-global/spec-nomenclature.md).
2. No form, component, file or folder name contains a hyphen. Anvil names are Python names.
3. An event handler is named `<component_name>_<event>`, for example `btn_save_click`. This is the name Anvil itself generates.

## 6. Text

1. Every visible text in a form template is a phrase key, never words, as [[[default:specifications-global/spec-translation]]](C:/dev/project-library-global/specifications-global/spec-translation.md) sets out.
2. Every form's `__init__` calls `translate_form(self)` once the form's components exist.
3. Every phrase key a form uses exists in `en.py` with its English text.

## 7. Colour, Roles and Layout

1. Every colour comes from the theme's colour roles. A form template holds no hex, `rgb()`, `rgba()` or `hsl()` value.
2. Light and dark mode come from the theme's palettes. A form holds no colour scheme of its own.
3. A component's role is set in the form template as `prop:role="<role>"`, using a role the theme defines.
4. Every page form sits on a layout form from the application's `layouts` package. Every layout form is built on a theme layout.
5. Responsive behaviour is set per container with `wrap_on`, as [[[default:adr-global/adr-responsive-behaviour-mechanism]]](C:/dev/project-library-global/adr-global/adr-responsive-behaviour-mechanism.md) sets out. No form uses pixel breakpoints.

## 8. Data and Behaviour

1. A form is presentation only. Each event handler calls a server function or a client module function; logic lives in modules, as [[[default:specifications-global/spec-anvil-platform-standards]]](C:/dev/project-library-global/specifications-global/spec-anvil-platform-standards.md) sets out.
2. Every server function a form calls exists before the form is built.
3. An input that edits data is bound with a writeback binding (`writeback:<property>="..."`) on the property its theme documentation marks as writeback.
4. Every form that shows data has an empty state of exactly four components: an icon, a heading, a body text and a primary action button.
5. A form template holds no sample data.

## 9. Access

1. Every form is listed in the application's `access-matrix.yaml`, under `forms`, keyed by its module path, with a scope for every role.
2. A form a role may not use is hidden from that role's navigation and refused when opened directly.

## 10. Always-Available Controls

1. Every page shows three controls at all times:
   - **Tooltips on/off:** switches tooltips on or off for the signed-in user. The choice is saved in the user's preferences and applies on every page.
   - **Help videos:** opens a menu listing a help video link for every process on the current page. The menu has a switch to show all help videos or only those of the current page. Each video plays in the application's language, as [[[default:specifications-global/spec-translation]]](C:/dev/project-library-global/specifications-global/spec-translation.md) sets out.
   - **Dashboard:** opens the dashboard.
2. The three controls live in the layout forms, so every page that sits on a layout has them.
3. Every actionable component has a tooltip. The tooltip is a phrase key, and it shows only while the user has tooltips switched on.
4. The dashboard shows each user only what that user's role may see, as the application's access matrix sets out.
5. The dashboard has a clear **Return** button that takes the user back to the page the dashboard was opened from.

Why: help, tooltips and the dashboard must always be one click away, so that no user is ever stuck on a page without guidance or a way back.

## 11. Accessibility

1. Every form meets WCAG 2.2 AA.
2. Every flow can be completed by keyboard, and keyboard focus is always visible.
3. Every icon-only button has a name.
4. Every error message says what to fix.
5. Every text and control colour pair reaches 4.5:1 contrast for text and 3:1 for controls, in light and dark mode.

## 12. Documents per Form

Each form has two documents, both named after the form.

### 12.1 Screen Requirement

- **Location:** `{slug}-project-library/ui/<package path>/<FormName>/<FormName>-requirement.md`.
- **Read by:** OpenCode and Claude.
- **Front matter:** `status: draft` until David approves it, then `status: approved`. Only an approved screen requirement is built.
- **Contents:**
  1. the form's module path, purpose, layout and route;
  2. every element of the screen, with the theme component chosen for it and the reason;
  3. the data each element shows, by table and column in the authoritative schema;
  4. every user action, with the server function it calls and the result it gives;
  5. the empty state;
  6. the scope of every role, for the access matrix;
  7. the phrase key of every visible text and every tooltip, with its English text;
  8. every process on the page, with the help video that explains it;
  9. the user flows the form takes part in.

### 12.2 Spec Sheet

- **Location:** `{slug}-app1/theme/assets/docs/app1/<package path>/<FormName>.md`.
- **Read by:** the Anvil agent.
- **Written by:** `mb-form-builder`, from the approved screen requirement.
- **Contents:**
  1. every component in the form and its purpose;
  2. every property set on each component, including its tooltip, with its allowed values from the theme's documentation;
  3. the writeback property of every input;
  4. the data each component shows;
  5. every event handler, with the server function it calls and the result it gives;
  6. the checks that must pass.
- **Public:** Anvil serves everything in `theme/assets/` at a public web address. A spec sheet therefore holds no secret, key, password or user data.

Why: the screen requirement is the design David approves; the spec sheet is the same design restated for the Anvil agent, in the only place in the app the agent reads documents from.

## 13. Checks

Every new or changed form passes both checks before it is committed:

1. `anvil --json validate client_code` passes. This checks the Python files and `anvil.yaml`.
2. The test suite scanner, `ts_scan.py`, passes for forms: every component type and property exists in the theme's documentation or in `approved_components`, every tag is closed, no banned component is used, and no colour value is written in the template.
