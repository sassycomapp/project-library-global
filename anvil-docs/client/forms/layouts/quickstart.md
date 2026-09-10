---
title: "Quickstart"
url: "/docs/client/forms/layouts/quickstart"
doc-id: layouts-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Layouts](#quickstart-layouts)

A Layout is a Form that provides a visual template for other Forms. It lets you create reuasble page structures shared across multiple Forms. This makes it especially useful for page navigation.

In this Quickstart, we’ll create an app with a simple Layout that has links in a sidebar. The other Forms in the app will use this Layout and users will be able to click on the links in the sidebar to navigate between Forms.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘Blank app’. Choose the Material Design 3 theme.

## [Create a Layout Form](#create-a-layout-form)

Our new app will already have a Form in it called `Form1`. We’ll turn this Form into a Layout and use it to define the structure of our other Forms.

Double click on `Form1` in the [App Browser](/docs/editor#app-browser) and rename it to `Homepage`. At the top of the Form, click the three dots menu and choose “Use as Layout”.

## [Add Links to the sidebar](#add-links-to-the-sidebar)

We can now build our Layout by dragging and dropping components from the [Toolbox](/docs/editor/form-editor#toolbox) onto the Form.

Drag a [ColumnPanel](/docs/ui/components/containers#columnpanel) from the Toolbox into the sidebar.

Next, add some [Link](/docs/ui/components/basic#link) components into the Sidebar and change their text.

## [Add a Slot to the Form](#add-a-slot-to-the-form)

Now we need to add a Slot to our Form. A Slot is not a component, but it defines where components can be added by Forms that use our Layout.

Drag and drop a Slot from the Toolbox into the middle of the page. This is where the Forms that use our Layout will be able to add content.

## [Use the Layout](#use-the-layout)

We can now use this Form as the Layout for other Forms. Create a new Form and choose `Homepage` as the Layout.

Our new Form will now have the same links we added to the Layout Form. We won’t be able to change or remove these links from the new Form, but we can always make edits to `Homepage` that will affect every Form using it as a Layout.

Because we added a Slot to `Homepage`, we can add components to our new Form.

For a more in-depth explanation on how to use Layouts to create a multi-page app, see our tutorial:

[Using Layouts to Create a Multi-page App](/learn/tutorials/using-layouts-to-create-multi-page-app)
