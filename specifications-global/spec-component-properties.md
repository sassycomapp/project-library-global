---
title: "spec-component-properties"
doc-id: "mb-5162b6c9"
updated: "2026-11-12"
---
# Component Properties Specification

## 1. Purpose and Source

- This specification states how a form sets component properties, bindings and events, and which theme components support writeback.
- The facts for each component come from the theme's documentation in `m3-custom-theme-project-library`, as [[[default:specifications-global/spec-ui-standards|UI Standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) section 2 sets out. `docs/base-inventory.md` lists every property of every component, with its type, options, default and description; `docs/component-inventory.yaml` holds the same facts for tools.
- This specification does not repeat each component's properties. Where it and the theme's documentation differ, the theme's documentation is right and this specification is corrected.

Why: one source of component facts. The previous version of this file listed properties by hand and had drifted from the theme.

## 2. Setting Properties in a Form Template

A form is an HTML template, `form_template.html`. Each component is an `<anvil-component>` element.

| Attribute | Sets | Example |
|---|---|---|
| `type` | The component type: a theme component's inventory key, a form of the application by its package-qualified name, or an approved Anvil component. The legacy `form:dep_<id>:...` spec is never written | `type="m3._Components.Button"` |
| `name` | The Python name, with the prefix [[[default:specifications-global/spec-nomenclature\|Nomenclature]]](C:/dev/project-library-global/specifications-global/spec-nomenclature.md) section 1.6 gives | `name="btn_save"` |
| `prop:<property>` | A fixed property value, read as JSON: `true`, `false`, `null`, numbers, arrays and objects; anything else is a string | `prop:text="booking.save"`, `prop:enabled="false"` |
| `bind:<property>` | A one-way data binding | `bind:text="self.item['name']"` |
| `writeback:<property>` | A two-way data binding; only on a property in section 4 | `writeback:text="self.item['name']"` |

Event handlers are wired in the form's Python class, not in the template: `@handle("btn_save", "click")` above `def btn_save_click(self, **event_args):`, with `from anvil import *` at the top of the module.

Rules:

1. Every property, binding and handled event names something the component has in the theme's inventory. `ts_scan.py` (ST-11) fails a form that names anything else.
2. A visible text property (`text`, `placeholder`, `tooltip`, `title`, `label`, `content`) holds a phrase key, never words ([[[default:specifications-global/spec-translation|Translation]]](C:/dev/project-library-global/specifications-global/spec-translation.md)).
3. Colours, fonts and spacing come from the theme's roles and tokens, never from a value written in the template.
4. A layout form's components sit in `<anvil-block slot="...">` elements, and each slot is one the layout offers in the inventory.
5. Every Anvil element is closed with its own closing tag, even when empty; none is self-closed with `/>`.
6. Every property can also be set in code. There are no designer-only properties.

## 3. Theme Components

Every component the theme offers, with the events it raises. Layouts (`m3.Layouts.NavigationDrawerLayout` and `m3.Layouts.NavigationRailLayout`) are listed in the inventory with their slots.

| Component | Inventory key | Events |
|---|---|---|
| Avatar | `m3._Components.Avatar` | none |
| AvatarMenu | `m3._Components.AvatarMenu` | `click` |
| Badge | `m3._Components.Badge` | `show`, `hide` |
| BottomSheet | `m3._Components.BottomSheet` | `opened`, `closed`, `show`, `hide` |
| Button | `m3._Components.Button` | `click`, `show`, `hide` |
| ButtonGroup | `m3._Components.ButtonGroup` | `change`, `click`, `show`, `hide` |
| ButtonMenu | `m3._Components.ButtonMenu` | `click`, `show`, `hide` |
| Card | `m3._Components.Card` | `show`, `hide` |
| CardContentContainer | `m3._Components.Card.CardContentContainer` | `show`, `hide` |
| Carousel | `m3._Components.Carousel` | `item_click`, `change`, `show`, `hide` |
| Checkbox | `m3._Components.Checkbox` | `change`, `show`, `hide` |
| Chip | `m3._Components.Chip` | `click`, `change`, `remove`, `show`, `hide` |
| CircularProgressIndicator | `m3._Components.CircularProgressIndicator` | `show`, `hide` |
| DatePicker | `m3._Components.DatePicker` | `change`, `show`, `hide` |
| Dialog | `m3._Components.Dialog` | `show`, `hide` |
| Divider | `m3._Components.Divider` | `show`, `hide` |
| DropdownMenu | `m3._Components.DropdownMenu` | `change`, `show`, `hide` |
| FabMenu | `m3._Components.FabMenu` | `item_click`, `opened`, `closed`, `show`, `hide` |
| FileLoader | `m3._Components.FileLoader` | `change`, `focus`, `lost_focus`, `show`, `hide` |
| FloatingActionButton | `m3._Components.FloatingActionButton` | `click`, `show`, `hide` |
| Heading | `m3._Components.Heading` | `show`, `hide` |
| IconButton | `m3._Components.IconButton` | `click`, `show`, `hide` |
| IconButtonMenu | `m3._Components.IconButtonMenu` | `click` |
| InteractiveCard | `m3._Components.InteractiveCard` | `click`, `show`, `hide` |
| LinearProgressIndicator | `m3._Components.LinearProgressIndicator` | `show`, `hide` |
| Link | `m3._Components.Link` | `click`, `show`, `hide` |
| ListItem | `m3._Components.ListItem` | `click`, `show`, `hide` |
| LoadingIndicator | `m3._Components.LoadingIndicator` | `show`, `hide` |
| MenuItem | `m3._Components.MenuItem` | `click` |
| NavigationBar | `m3._Components.NavigationBar` | `change`, `show`, `hide` |
| NavigationLink | `m3._Components.NavigationLink` | `click`, `show`, `hide` |
| PaneLayout | `m3._Components.PaneLayout` | `width_class_change`, `show`, `hide` |
| RadioButton | `m3._Components.RadioButton` | `select`, `show`, `hide` |
| RadioGroupPanel | `m3._Components.RadioGroupPanel` | `change`, `hide`, `show` |
| SearchBar | `m3._Components.SearchBar` | `search`, `change`, `show`, `hide` |
| SidesheetContent | `m3._Components.SidesheetContent` | none |
| Slider | `m3._Components.Slider` | `change`, `change_end`, `show`, `hide` |
| SplitButton | `m3._Components.SplitButton` | `click`, `item_click`, `show`, `hide` |
| Switch | `m3._Components.Switch` | `change`, `show`, `hide` |
| Tabs | `m3._Components.Tabs` | `change`, `show`, `hide` |
| Text | `m3._Components.Text` | `show`, `hide` |
| TextArea | `m3._Components.TextInput.TextArea` | `change`, `show`, `hide`, `focus`, `lost_focus` |
| TextBox | `m3._Components.TextInput.TextBox` | `trailing_icon_click`, `pressed_enter`, `change`, `show`, `hide`, `focus`, `lost_focus` |
| TimePicker | `m3._Components.TimePicker` | `change`, `show`, `hide` |
| ToggleIconButton | `m3._Components.ToggleIconButton` | `click`, `show`, `hide` |
| Toolbar | `m3._Components.Toolbar` | `show`, `hide` |
| TopAppBar | `m3._Components.TopAppBar` | `navigation_click`, `show`, `hide` |

## 4. Writeback Properties

Only these properties take `writeback:`. The writeback happens on the events shown.

| Component | Property | Written back on |
|---|---|---|
| ButtonGroup | `selected_index` | `change` |
| Checkbox | `checked` | `change` |
| Chip | `selected` | `change` |
| DatePicker | `date` | `change` |
| DropdownMenu | `selected_value` | `change` |
| RadioGroupPanel | `selected_value` | raised by the component itself |
| SearchBar | `text` | `change` |
| Slider | `value` | `change_end` |
| Switch | `selected` | `change` |
| Tabs | `selected_index` | `change` |
| TextArea | `text` | raised by the component itself |
| TextBox | `text` | raised by the component itself |
| TimePicker | `time` | `change` |

Not writeback-capable: every other property, including RadioButton, FileLoader and every display component.

## 5. Anvil Standard Components

A form uses an Anvil standard component only where the theme has none for the purpose, and only if it is in `approved_components` in the application's `ts-config.yaml` (UI Standards section 3). Their properties are in Anvil's own documentation, in `project-library-global/anvil-docs/components/`. `HTMLTemplate`, `HtmlPanel` and `Label` are banned; [[[default:adr-global/adr-htmltemplate-use|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md) governs `HTMLTemplate`.
