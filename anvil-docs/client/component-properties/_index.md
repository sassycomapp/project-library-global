---
title: "Component Properties"
url: "/docs/client/component-properties"
doc-id: component-properties-_index
state: Live
date-created: 2026-09-08
---


# [Component Properties](#component-properties)

Components have **properties** that determine how they look and how they behave. Properties can be modified in the [Anvil Editor](/docs/editor) using the Properties Panel (on the right below the Toolbox):

The Properties Panel allows you to edit a component’s content, appearance and behaviour.

You can also change some of the most common component properties from the Object Palette, which will show up above the component when you select it.

The Object Palette allows you to quickly modify  
a component’s most common properties

## [Working with properties](#working-with-properties)

You can adjust a component’s appearance by setting a property:

```python
self.button_1.text = "Click me"
```

If you’re creating components in code, you can pass in initial values for the properties when you create the component, for example:

```python
self.my_button = Button(text="Click me")
```

You can also read data from a component by reading properties (for example the `text` property of a TextBox component contains whatever text the user has entered in the box).

```python
latest_user_input = self.text_box_1.text
```

The properties of all Anvil’s built-in components can be found in the [API Reference](/docs/api/anvil).

### Container Properties

When a component is inside a [container](/docs/components/standard-components/containers), it will have container properties that control the relationship between the component and the container it is in. For example, you can set the width, `x`-position and `y`-position of a component in an [XYPanel](/docs/components/standard-components/containers#xypanel).

Container properties can also be passed as keyword arguments when adding a component to a container in code:

```python
self.xy_panel_1.add_component(my_button, x=42, y=128)
```

### Properties and Form initialisation

Each [Form](/docs/client/forms) contains this line of code:

```python
# Set Form properties and Data Bindings.
super().__init__(**properties)
```

When this line runs during Form initialisation, the properties you set in the Properties Panel are applied to your components.

Forms also have properties. When no components are selected, the Properties Panel will display the current Form’s properties.

## [The `tag` property](#the-tag-property)

Every component also has a property called `tag`, which is for you to store any extra data you like. By default, it’s an empty object that you can store attributes on:

```python
self.my_textbox.tag.foo = "bar"
```

You can also keep a component’s properties in sync with your data by using [Data Bindings](/docs/client/component-properties/data-bindings). A Data Binding associates a property of a component with a single Python expression, which saves you from writing similar assignments manually. Learn more about [Data Bindings](/docs/client/component-properties/data-bindings).
