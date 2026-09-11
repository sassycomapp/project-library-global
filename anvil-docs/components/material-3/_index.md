---
document: "Material 3"
title: "Material 3"
url: "/docs/components/material-3"
doc-id: material-3-_index
state: Live
date-created: 2026-09-08
---


# [New Material 3 Theme](#new-material-3-theme)

Anvil’s Material 3 theme is a set of custom components and layouts that implement Google’s [Material 3](https://m3.material.io/) design system.

Not every Material 3 component is supported (yet!), and any Anvil components that don’t have a Material 3 counterpart have been styled to match the Material 3 specs as best as possible. The Material 3 theme components can be used with other Anvil components and containers.

The New Material 3 Theme is currently in beta. If you encounter something strange, please ask about it on the [Anvil forum](https://anvil.works/forum).

The Anvil Material 3 theme is an [open-source project](https://github.com/anvil-works/material-3-theme) that is currently a work-in-progress. We’d love your help implementing new components and fixing bugs.

## [How to use the Material 3 theme](#how-to-use-the-material-3-theme)

When creating an app, choose **New M3 (Beta)**.

### Adding the Material 3 theme to an existing app

If you already have an app and want to use components or layouts from the Material Design 3 theme, you can add the dependency manually. Just go to **Settings -> Dependencies**, choose **Third Party** and enter the dependency ID `4UK6WHQ6UX7AKELK`.

If your app already contains an existing theme, it is possible that the theme CSS will disrupt the M3 theme. If you’re seeing strange results, try creating a new blank M3 app.

## [Component index](#component-index)

Material 3 includes a large number of components. See the documentation for [all components](material-3/components), or browse through them by type:

### [Typography](material-3/components#typography)

There are three typography components for displaying text in Material 3:

-   [Text](material-3/components#text)
-   [Heading](material-3/components#heading)
-   [Link](material-3/components#link)

### [Buttons](material-3/components#button)

Buttons are for performing actions. The ButtonMenu component displays a floating menu when clicked.

-   [Button](material-3/components#button)
-   [Icon Button](material-3/components#iconbutton)
-   [Toggle Icon Button](material-3/components#toggleiconbutton)
-   [Button Menu](material-3/components#buttonmenu)

### [Display](material-3/components#display)

Display components are designed to help display content on the page.

-   [Card](material-3/components#card)
-   [InteractiveCard](material-3/components#interactivecard)
-   [Divider](material-3/components#divider)

### [Navigation](material-3/components#navigation)

The NavigationLink is designed to work with the Material 3 Layouts to make it easy to navigate between Forms.

-   [NavigationLink](material-3/components#navigationlink)

### [Menus](material-3/components#menus)

Menus hold other components as a list of options. MenuItems are designed to populate Menus.

-   [ButtonMenu](material-3/components#buttonmenu)
-   [MenuItem](material-3/components#menuitem)

### [Form Input](material-3/components#form-input)

Form Input components are interactive components used to get data from the user.

-   [Checkbox](material-3/components#checkbox)
-   [RadioButton](material-3/components#radiobutton)
-   [TextBox](material-3/components#textbox)
-   [TextArea](material-3/components#textarea)
-   [DropdownMenu](material-3/components#dropdownmenu)
-   [Switch](material-3/components#switch)
-   [FileLoader](material-3/components#fileloader)
-   [Slider](material-3/components#slider)

### [Feedback](material-3/components#feedback)

Use feedback components to show the status of a process.

-   [LinearProgressIndicator](material-3/components#linearprogressindicator)
-   [CircularProgressIndicator](material-3/components#circularprogressindicator)

## [Layout index](#layout-index)

The Material 3 theme has [two layouts](material-3/layouts) designed for page navigation:

-   [Navigation Rail Layout](material-3/layouts#navigation-rail-layout)
-   [Navigation Drawer Layout](material-3/layouts#navigation-drawer-layout)
