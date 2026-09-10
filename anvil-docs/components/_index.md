---
title: "Components"
url: "/docs/components"
doc-id: components-_index
state: Live
date-created: 2026-09-08
---


# [Component Libraries](#component-libraries)

In Anvil, you build your UI by [adding components](/docs/client/adding-ui-elements) to [Forms](/docs/client/forms), either via code or dragging and dropping. These components are just Python objects.

You control the content, appearance and behaviour of your components by setting their [Properties](/docs/client/component-properties). You can set these properties from the Anvil Editor or through Python code.

Components raise [events](/docs/client/events) in response to user interaction. For example, when a user clicks a button, the component will raise a `click` event. To make your app interactive, you can write Python functions that will run when events are raised.

Anvil currently offers two different component libraries to choose from: Standard Anvil Components and Material 3.

## [Standard Anvil Components](#standard-anvil-components)

The Standard Anvil component library is the original set of Anvil components and is used in much of the Anvil documentation and tutorials.

## [Material 3](#material-3)

Anvil’s Material 3 library is a set of custom components and layouts that implement Google’s [Material 3](https://m3.material.io/) design system.

The Material 3 theme is currently in beta.
