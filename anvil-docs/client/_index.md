---
document: "Building the Front-End"
title: "Building the Front-End"
url: "/docs/client"
doc-id: client-_index
state: Live
date-created: 2026-09-08
---


# [Building the Front-End](#building-the-front-end)

You can build your [front-end](/docs/app-architecture) in the [Anvil Editor](/docs/editor). You create your user interface by dragging and dropping [built-in](/docs/ui/components) or [custom](/docs/client/customisation/custom-components) components onto [Forms](client/forms) in [Design view](/docs/editor/form-editor#design-view), editing your UI as text in [HTML view](/docs/editor/form-editor#html-view), or defining components directly in [Code view](/docs/editor/form-editor#code-view). You then write [client-side code](client/client-code) to control how your interface behaves and responds to user interaction.

[Quickstart: User Interfaces](/docs/client/quickstart)

## [](#forms)[Forms](client/forms)

Forms are the pages of your Anvil app. Each Form has a visual layout that defines how it looks, and a Python class that defines how it behaves. You build your user interface by [placing components](/docs/client/adding-ui-elements) onto Forms in the [Form Editor](/docs/editor/form-editor), editing the Form’s structure as text in HTML view, and writing Python code to control them.

Forms are themselves components, which means they can be [nested](/docs/client/forms/forms-as-components) inside other Forms to build more complex interfaces.

## [](#adding-ui-elements)[Adding UI Elements](client/adding-ui-elements)

Components are the visual elements you add to a Form, such as buttons and text boxes. You can add components visually in the Form Editor, define them in HTML, or create them in code.

## [](#component-properties)[Component Properties](client/component-properties)

Every component has properties that control how it looks and behaves. You can set properties in the [Properties Panel](/docs/editor/form-editor#properties-panel) or change them dynamically in your [Form’s code](/docs/client/forms/forms-as-python-classes#the-form-class). Component properties can also be bound to Python expressions using [Data Bindings](/docs/client/component-properties/data-bindings), keeping them in sync with the underlying data.

## [](#events)[Events](client/events)

Components raise events when users interact with them, such as clicking a button or changing the value of an input. You can write Python functions called **event handlers** to respond to these events.

## [](#client-side-code)[Client-Side Code](client/client-code)

Client-side code is Python code that runs in the user’s browser. It controls how your interface behaves, updates components dynamically, responds to user interactions, and can call [server-side functions](/docs/server) or [code outside of Anvil](uplink). Client code is mainly written in your [Form](client/forms) code and [Modules](client/client-code/modules).

## [](#navigation)[Navigation](client/navigation)

Navigation in an Anvil app is handled by switching between Forms. You can switch between Forms programmatically using `open_form()`, or implement URL-based navigation with [routing](/docs/client/navigation/routing) so that different pages of your app correspond to different URLs.

## [](#customisation)[Customisation](client/customisation)

Anvil components can be customised in several ways. You can change colour schemes, create custom components from Forms, build components from scratch with HTML, apply CSS styling, or extend functionality with JavaScript.
