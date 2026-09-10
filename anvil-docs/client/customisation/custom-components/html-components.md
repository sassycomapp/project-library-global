---
title: "Components from HTML"
url: "/docs/client/customisation/custom-components/html-components"
doc-id: html-components
state: Live
date-created: 2026-09-08
---


# [Building Custom Components from Scratch](#building-custom-components-from-scratch)

You can create your own custom components in Anvil entirely in Python. However, if you want more control over the look and function of your custom components, you can build them from scratch using HTML with a Custom HTML Form. You can also style your components using CSS and add functionality using Python or JavaScript.

This page covers building custom components from scratch using a Custom HTML Form. To learn about turning the Form into a custom component, setting its properties and events, and configuring its appearance in the Toolbox, see our general [documentation on custom components](/docs/client/customisation/custom-components).

## [Creating a component from a Custom HTML Form](#creating-a-component-from-a-custom-html-form)

To create a custom component from scratch, you’ll first want to add a **Custom HTML** Form from the New Form modal.

From the three dots menu at the top of the Form Editor, tick **Use as custom component**.

Switch to the [HTML view](/docs/client/forms/forms-in-the-editor#html-view) to edit the Form’s HTML.

Here you can write HTML to build your custom component. Any valid HTML code you write will show up live in Design view. You can use a combination of native HTML elements and Anvil components.

For more information on using HTML elements in Anvil and styling them with CSS, see [Adding HTML Elements](/docs/client/adding-ui-elements/adding-html-elements).

### Accessing elements

You can access your HTML elements from Python code using the `dom_nodes` API. To do this, you’ll first need to give an element the `anvil:dom-node` attribute.

```html
<div anvil:dom-node="my-component"></div>
```

Then, in Python, you can look up the element in the Form’s `dom_nodes` dictionary.

```python
my_element = self.dom_nodes['my-component']
```

These objects are real [JavaScript `HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) objects, and you can access their properties and methods over Anvil’s [Javascript-to-Python bridge](/docs/client/customisation/javascript/accessing-javascript). This is especially useful for setting up custom properties and events.

### Custom properties using the `dom_nodes` API

Anvil components have [properties](/docs/client/component-properties) that determine how they look and behave. You can create custom properties that control the appearance and content of your HTML elements by:

1.  Adding the property in the [Custom Component Configuration dialog](/docs/client/customisation/custom-components#configuring-custom-properties)
2.  Giving the HTML element you want to control an `anvil:dom-node` attribute
3.  Writing getter and setter methods in Python using the `dom_nodes` API

For example, the below code creates a custom HTML button. The `<span>` element inside the button has `anvil:dom-node="custom-button-text"` as an attribute so that it can be accessed from Python code.

```html
<button class="custom-button" anvil:dom-node="custom-button">
  <i class="material-symbols-outlined">check</i>
  <span anvil:dom-node="custom-button-text">Click me</span>
</button>
```

We can then [add a property](/docs/client/customisation/custom-components#creating-properties) called `text` to change the text of the Button:

Then, we can use Python’s standard [Property Descriptors](https://developer.ibm.com/tutorials/os-pythondescriptors/) to write getter and setter methods to set the `innerText` of the `custom-button-text` element:

```python
  @property
  def text(self):
    return self._text

  @text.setter
  def text(self, value):
    self._text = value
    self.dom_nodes['custom-button-text'].innerText = value
```

### Adding properties to the Object Palette

When you add a property to a custom component, it will show up in the Properties Panel. You can also add some types of properties to the Object Palette.

#### Boolean type properties

For Boolean type properties, you can choose to have an icon appear in the Object Palette that will toggle that property on and off.

In the Custom Components Configuration dialog, choose the property you want to add to the Object Palette, click “Show advanced settings” and expand the “Designer” section. In the “Designer Hint” dropdown menu, you’ll see several options.

Choosing the Designer Hint will add the associated icon to the Object Palette but you’ll still need to write the setter and getter methods. The available icons are:

-   enabled:
-   font-bold:
-   font-italic:
-   font-underline:
-   toggle:
-   visible:

For example, we can add a `bold` property to our custom button component that controls whether the text on the button is bold or not:

```python
  @property
  def bold(self):
    return self._bold

  @bold.setter
  def bold(self, value):
    self._bold = value
    if value:
        self.dom_nodes['custom-button-text'].style.fontWeight = "bold"
    else:
        self.dom_nodes['custom-button-text'].style.fontWeight = "normal" 
```

We then can add `font-bold` as the Designer Hint from the Custom Component Configuration dialog.

We can now toggle the `bold` property from the Object Palette.

#### Enum type properties

For `enum` type properties, there is one Designer Hint option: `align-horizontal`. If you set a property to have this Designer Hint, up to four icons will be added to the Object Palette depending on what options you add. Below are the icons that will be added if the associated word is one of the `enum` options:

-   ‘left'
-   ‘center’
-   ‘right’
-   ‘justify’ or ‘full’

Just as with the Boolean Designer Hints, you’ll still need to set up the setter and getter methods for the property.

#### URI type properties

For `uri` type properties, there is one Designer Hint option, `asset-upload`, which adds a icon to the Object Palette. Clicking the icon will bring up a window that allows you to choose an asset from your app or to upload a new file.

### Custom events

You can also add custom events to your custom components. This section is specifically about using the `dom_nodes` API to set up custom JavaScript events for HTML components. For more general information about adding custom events to a custom component, see [Anvil Docs | Custom Components](../custom-components#configuring-custom-components)

Accessing your HTML elements through the `dom_nodes` dictionary means you can set up event listeners with JavaScript.

For example, we can add a `click` event to the custom button component. After adding the event in the Custom Component Configuration dialog, we can then add an event listener using Anvil’s [Javascript-to-Python bridge](/docs/client/customisation/javascript/accessing-javascript) to the `custom-button` element:

```python
class CustomButton(CustomButtonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)
    self.dom_nodes['custom-button'].addEventListener('click', self._handle_click)

  def _handle_click(self, event):
    self.raise_event('click')
```

You can also use `anvil:on-dom:` to handle native DOM events in HTML. See [Handling native DOM events on HTML elements](/docs/client/forms/forms-as-html#handling-native-dom-events-on-html-elements).

When the component is added to another Form, we can now add a `click` function for it that will run when the button is clicked, just as if it were a normal Anvil Button.

## [Making a custom component a container](#making-a-custom-component-a-container)

Custom HTML components can be made into containers so that other components can be dragged inside.

To make your custom HTML component a container, you need to tick ‘Make this Form available as a container’ in the Custom Component Configuration dialog.

You’ll also need to add [a slot](/docs/ui/layouts/html-layouts#adding-slots) element to your HTML where you want components to be dropped. You’ll be able to drag components into this slot while building the component, but it will also be available to users of the component when it’s added to another Form.

For example, the following code has one slot. Components can be dragged into the slot while editing the custom component and when the custom component is added to another Form.

```html
<div class="custom-container" style="border: 2px solid; padding: 10px;">
  <anvil-slot name="default"></anvil-slot>
</div>
```
