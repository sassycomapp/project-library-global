---
title: "Forms"
url: "/docs/client/forms"
---


# [Forms](#forms)

Forms are the pages of your Anvil app. Each Form has two parts: a visual design that describes how it looks and a Python class that defines how it behaves.

When you create an Anvil app, it comes with a Form by default. You build your user interface in the [Anvil Editor](/docs/editor) by dragging and dropping [components](components) from the [Toolbox](/docs/editor/form-editor#toolbox) onto the Form, or by defining components directly in the Form’s code. You can also edit the Form’s structure as HTML.

A single Anvil app can have one or many Forms, and you can add them at any time in the Anvil Editor.

## [](#forms-in-the-anvil-editor)[Forms in the Anvil Editor](/docs/client/forms/forms-in-the-editor)

The Anvil Editor is where you build and manage your Forms. You can view and edit each Form in Design view, Code view, HTML view, or Split view, and set which Form loads first when your app opens.

## [](#forms-as-python-classes)[Forms as Python Classes](/docs/client/forms/forms-as-python-classes)

Each Form is a Python class. You can get a reference to the currently open Form, navigate between Forms, and control components through the Form object and its attributes.

## [](#forms-as-html)[Forms as HTML](/docs/client/forms/forms-as-html)

The user interface of every Form is represented under the hood as HTML.

## [](#layouts)[Layouts](/docs/client/forms/layouts)

Forms can be turned into Layouts that define the look and structure of other Forms.

## [](#forms-as-components)[Forms as Components](/docs/client/forms/forms-as-components)

Forms can be added to other Forms to build complex, nested interfaces.

## [](#form-templates)[Form Templates](/docs/client/forms/form-templates)

Every Form in Anvil inherits from a template class that defines its basic structure and layout.
