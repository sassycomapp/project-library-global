---
document: "Layouts"
title: "Layouts"
url: "/docs/components/material-3/layouts"
doc-id: layouts
state: Live
date-created: 2026-09-08
---


# [Material 3 Layouts](#material-3-layouts)

The Anvil Material 3 theme comes with two predefined [layouts](/docs/ui/layouts), based on two different styles of [Material 3 navigation regions](https://m3.material.io/foundations/layout/understanding-layout/parts-of-layout).

Layouts have properties that allow for greater interaction. These can be set from the Form that’s using the layout – either from code or from the [Properties Panel](/docs/editor/form-editor#properties-panel). For example, both layouts have an optional side sheet, which can be controlled by setting the `show_sidesheet` property to `True` or `False`.

```python
  def m3_button_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.layout.show_sidesheet = True
```

## [Navigation Rail Layout](#navigation-rail-layout)

[Properties](/docs/api/m3#NavigationRailLayout_attributes) | [Events](/docs/api/m3#NavigationRailLayout_events)

The Navigation Rail Layout uses the [Material 3 navigation rail](https://m3.material.io/components/navigation-rail/overview). Navigation rails are meant for displaying a small number of app destinations (see the [Material 3 usage guidelines](https://m3.material.io/components/navigation-rail/guidelines#d9d85ba1-db8f-491a-a555-c1f5221c69f8) for more information).

You can control the vertical alignment of the content of the navigation rail with the `navigation_rail_vertical_align` property.

```python
self.layout.navigation_rail_vertical_align = "center"
```

On smaller screens, the navigation rail can be collapsed into a modal drawer or an app bar. This can be controlled with the `navigation_rail_collapse_to` property.

Visit the [API documentation](/docs/api/m3#NavigationRailLayout) for more information about the Navigation Rail Layout.

## [Navigation Drawer Layout](#navigation-drawer-layout)

[Properties](/docs/api/m3#NavigationDrawerLayout_attributes) | [Events](/docs/api/m3#NavigationDrawerLayout_events)

The Navigation Drawer Layout uses the [Material 3 navigation drawer](https://m3.material.io/components/navigation-drawer/overview). Navigation drawers are best suited when you want to display a longer list of app destinations. They’re also useful when you want to convey navigation hierarchys and groupings (see the [Material 3 usage guidelines](https://m3.material.io/components/navigation-drawer/guidelines#761e9679-2e72-4a85-894d-55bc3666b567) for more information).

On smaller screens, the navigation drawer will always collapse into a modal drawer.

Visit the [API documentation](/docs/api/m3#NavigationDrawerLayout) for more information about the Navigation Drawer Layout.
