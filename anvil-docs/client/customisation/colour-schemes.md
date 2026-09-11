---
document: "Colour Schemes"
title: "Colour Schemes"
url: "/docs/client/customisation/colour-schemes"
doc-id: colour-schemes
state: Live
date-created: 2026-09-08
---


# [Colour Schemes](#colour-schemes)

Some Anvil app themes have built-in colour schemes. You can find the colour scheme of your app by navigating to the ‘Theme’ tab in the [Sidebar menu](/docs/editor#sidebar-menu), then choosing ‘Colour Scheme’.

## [Using the colour scheme](#using-the-colour-scheme)

### In the Anvil Editor

Colour scheme colours can be used in the [Properties Panel](/docs/editor/form-editor#properties-panel) to change the appearance of a component. Choose the paintbrush icon next to a property to choose a colour from the app’s colour scheme.

### In Python code

From Python code, you can access your app’s colour scheme using `app.theme_colors`, which returns a dictionary of the form `{'Colour Name': '<value>'}`. Colours can then by accessed by indexing the dictionary:

```python
#set the background colour of the Button to Secondary
self.button_1.background = app.theme_colors['Secondary']
```

This is an advanced feature. You don’t need to write HTML and CSS to use Anvil!

### In CSS code

Your app’s colours are accessible in CSS code by using `%color:Colour Name%`.

```css
/* Set the background and foreground colours of the filled-button role*/
.anvil-role-filled-button {
    background-color: %color:Primary%;
    color: %color:On Primary%; 
}
```

## [Changing the colour scheme](#changing-the-colour-scheme)

You can also change individual colours by modifying the colour’s code. (Any [type of color value valid in CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/color) will work.)

### Single colour scheme

Newer themes (currently the [Material Design 3](/learn/tutorials/using-material-3) and Rally themes) have a dropdown menu that lets you choose from a number of pre-defined colour schemes.

These newer themes follow the colour system defined by [Google’s Material Design 3](https://m3.material.io/) design system. Learn how to create a custom Material Design 3 colour scheme for your apps by following the how-to guide: [Creating a custom Material Design 3 colour scheme](/docs/how-to/creating-material-3-colour-scheme)

### Multiple colour palettes

Older versions of the Material Design system, as used by Anvil’s Material Design and Classic themes, have simpler colour schemes built around primary and secondary hues. There are separate dropdown menus for changing the theme’s primary and secondary colours:
