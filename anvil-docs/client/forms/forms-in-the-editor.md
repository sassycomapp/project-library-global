---
title: "Forms in the Editor"
url: "/docs/client/forms/forms-in-the-editor"
doc-id: forms-in-the-editor
state: Live
date-created: 2026-09-08
---


# [Forms in the Anvil Editor](#forms-in-the-anvil-editor)

The Anvil Editor lists all the Forms in your app in the [App Browser](/docs/editor#the-app-browser). Clicking on a Form in the App Browser opens it in the [Form Editor](/docs/editor/form-editor), where you can view and edit it in four modes:

-   [Design view](#design-view)
-   [HTML view](#html-view)
-   [Code view](#code-view)
-   [Split view](#split-view)

### Design view

In Design view, you build your Form’s interface visually, by dragging and dropping [components](/docs/ui/components) from the [Toolbox](/docs/editor/form-editor#toolbox) onto the Form.

### HTML view

In HTML view, you can see the code that defines your Form’s interface. You can inspect and edit the structure of your Form as text, using HTML tags alongside Anvil components.

Changes you make in HTML view are reflected in Design view, and changes you make in Design view are reflected in HTML view.

To learn more about your Form’s HTML, see [Forms as HTML](/docs/client/forms/forms-as-html).

### Code view

In Code view, you can see and edit the Python class that represents your Form. This is where you write Python to control how your Form behaves and responds to user interactions. You can also create and manipulate components directly in code. See [Adding UI Elements](/docs/client/adding-ui-elements) and [Component Properties](/docs/client/component-properties) for more details.

### Split view

In Split view, you can show Design, HTML and Code views together, in any combination

## [The startup Form](#the-startup-form)

The Form with the lightning bolt symbol next to it in the App Browser is the startup Form. This is the first page displayed when your Anvil app is opened. You can only have one startup Form at a time.

To change the startup Form, click the three dots menu next to the Form you want to make the startup Form and choose “Set as Startup Form”.

When the app loads, the “startup Form” is loaded and becomes the [top-level Form](/docs/client/forms/forms-as-python-classes#the-top-level-form). Since each Form is a Python class, the startup Form’s `__init__` method runs automatically when the app loads, with no arguments passed in.

You can also launch your app with a [Module](/docs/client/client-code/modules#startup-module) instead of a Form, which lets you run code first, before deciding which page to open.
