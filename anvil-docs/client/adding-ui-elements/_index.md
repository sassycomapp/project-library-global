---
document: "Adding UI Elements"
title: "Adding UI Elements"
url: "/docs/client/adding-ui-elements"
doc-id: adding-ui-elements-_index
state: Live
date-created: 2026-09-08
---


# [UI Elements](#ui-elements)

In Anvil, every part of your user interface is a component. Components are Python objects you can create, configure and control entirely in Python. Components range from simple display elements like [Labels](/docs/ui/components/basic#label) and [Images](/docs/ui/components/basic#image) to interactive ones like [Buttons](/docs/ui/components/basic#button) and [TextBoxes](/docs/ui/components/basic#textbox). Alongside components, Anvil also gives you visual and interactive elements you can control entirely in code, like alerts, notifications or loading indicators.

For the full list of available components, see [Anvil Components](/docs/ui/components).

## [Adding Components](#adding-components)

You can build your UI by adding elements to a [Form](/docs/client/forms) in [Design view, HTML view or Code view](/docs/editor/form-editor).

In Design view, you can drag and drop components onto the Form. In HTML view, these components appear as `<anvil-component>` tags.

In Code View, you can create components in code and add them to a Form:

```python
class Form1(Form1Template):
    # ... Somewhere inside Form1 ...
    self.button_1 = Button(text="Click me")
    self.add_component(self.button_1)
```

### Properties

Every component has properties that control how it looks and behaves. You can set these in the Properties Panel in the editor:

Or directly in code:

```python
self.button_1.text = "Click me"
self.button_1.visible = False
```

You can also read from properties. For example, reading the text property of a TextBox gives you whatever the user has typed:

```python
user_input = self.text_box_1.text
```

To learn more about properties, [read the full documentation](/docs/client/component-properties).

### Events

Components raise events when the user interacts with them. For example, a Button raises a `click` event when clicked. You can handle events in the Anvil Editor:

```python
@handle("button_1", "click")
def button_1_click(self, **event_args):
    print("Button clicked!")
```

Read the [Events docs](/docs/client/events) to learn more.

## [](#containers)[Containers](/docs/client/adding-ui-elements/containers)

Containers are components that hold other components and define how they are laid out on the page.

## [](#alerts-and-notifications)[Alerts and Notifications](/docs/client/adding-ui-elements/alerts-and-notifications)

You can display alerts, confirmation dialogs, and notifications to communicate with your client while your app is running.

## [](#adding-html-elements)[Adding HTML Elements](/docs/client/adding-ui-elements/adding-html-elements)

You can use native HTML elements in your apps and combine them with Anvil components.

## [](#loading-indicator)[Loading Indicator](/docs/client/adding-ui-elements/loading-indicator)

A loading indicator is displayed on your client when your app is retrieving data. You can also configure your loading indicator through code.
