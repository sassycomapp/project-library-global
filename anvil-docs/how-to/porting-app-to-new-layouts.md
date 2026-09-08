---
title: "Port an app to new Layouts"
url: "/docs/how-to/porting-app-to-new-layouts"
---


# [Using Layouts in your app](#using-layouts-in-your-app)

Anvil has introduced [Layouts](../../blog/announcing-layouts), a major update to the Anvil UI system. In the old UI system, you would have a pseudo “layout” Form which would add and delete Forms from its [containers](https://anvil.works/docs/client/adding-ui-elements/containers). In the new UI system, you can create a Layout Form that other Forms can inherit from - which is much simpler. This guide will show you how to take an old style Anvil app and convert it to use Layouts.

## [Contents](#contents)

1.  [Step 1](#step-1---introduction-to-the-old-style-app) - Introduction To Old Style App
2.  [Step 2](#step-2---making-the-homepage-a-layout) - Making The Homepage A Layout
3.  [Step 3](#step-3---recreating-the-child-forms) - Recreating The Child Forms
4.  [Step 4](#step-4---setting-the-new-startup-form) - Setting The New Startup Form

## [Step 1 - Introduction To The Old Style App](#step-1---introduction-to-the-old-style-app)

Below is a clone link to an example of the old style UI system in Anvil. To follow along with this guide, click the link below and clone the app:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:ENGS32YC5GG3OKG2%3d443PC4A5TYSLM2AI446QPP37)

The app consists of a `Homepage` Form and two pages. The `Homepage` Form has a navbar with two links. If you check the client-code, you’ll see when either link is clicked, it “opens” the corresponding Form by deleting whatever is in its `content_panel` component and adding the corresponding Form - previously, this was the best way to navigate between Forms.

## [Step 2 - Making The Homepage A Layout](#step-2---making-the-homepage-a-layout)

Let’s start by clicking the three dot icon above the `Homepage` Form and selecting “Use as layout”.

The first time you use Layouts in your app, you’ll need to migrate the app to use the new UI features. If the app hasn’t yet been migrated, you’ll see a popup message when you change your Form to a Layout. This is an irreversible change to your app, so please be aware if you’re migrating an app you’ve built with the old Anvil Designer.

Let’s add a description of our Layout in the Form’s configuration menu. This information shows up when deciding which Layout a new Form should use. Click the three dot icon above the Form again and select “Edit properties and events”. Then add a description.

Next up, we want to define where Forms using our Layout can add components. We do this by adding a Slot. We’ll add a Slot to the `content_panel` of our homepage by dragging in a “Slot” from [Toolbox](https://anvil.works/docs/editor/form-editor#toolbox) on to the right of the designer.

Each Slot has a name. We can rename our slot using the object palette. Let’s call it `main_slot`.

Be aware that if you delete or rename a Slot from a Layout that is being used by another Form, any components that were inside that Slot will not know where to go. You can find them in the Orphaned Components Panel and add them back to your page. For more information, see our [documentation on Layouts](/docs/ui/layouts#orphaned-components)

Finally, let’s remove the redundant code from our Homepage Form. Open the `Homepage` Layout’s client code and delete the import statements at the top of the Form that import `Page1` and `Page2`. In the `init` of our `Homepage`, remove `self.content_panel.add_component(Page1())` and `self.page_1_link.role = 'selected'`.

Then replace all the code in the `page_1_link_click()` function with `open_form('Page1')`:

```python
def page_1_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Page1')
```

Now do the same with `page_2_link_click` function.

Great, our Layout is complete. Now it’s time to update the `Page1` and `Page2` Forms to use the Layout.

## [Step 3 - Recreating The Child Forms](#step-3---recreating-the-child-forms)

If a Form doesn’t already use a Layout, we cannot change it to have a Layout. Instead we need to create a new Form.

We don’t want to lose the content of our old Forms yet, so for now let’s rename each page by adding “_old” to their names.

Then, we’ll add a new Form to our app, selecting the `Homepage` Layout.

Rename the Form to “Page1” and drag in a `ColumnPanel` into the main slot. Rename the `ColumnPanel` to `content_panel`.

Then, we can select the components we want to copy (CTRL+C) in “Page1_old” and paste (CTRL+V) them into the `ColumnPanel` in our new Page1 Form.

Finally, let’s write some code to control what happens when `Page1` is [opened/shown](https://anvil.works/docs/client/components#the-show-and-hide-events). Select the Form in the designer and in the [Events section](https://anvil.works/docs/editor#events) of the properties panel, click the blue button next to the “Show” event.

This will open up the code view and add a function that will run every time `Page1` is shown. Inside the function, we can interact with the Layout our Form is using with `self.layout`. This gives us the ability to call functions defined in our Layout and change the properties of the Layout’s components. Let’s call the `Homepage`’s `reset_links()` function and change the `page_1_link`’s role to “selected”.

```python
def form_show(self, **event_args):
    """This method is called when the form is shown on the screen"""
    self.layout.reset_links()
    self.layout.page_1_link.role = 'selected'
```

Repeat this process for `Page2` and delete both the old `Page1_old` and `Page2_old`.

## [Step 4 - Setting The New Startup Form](#step-4---setting-the-new-startup-form)

One quick final step, we no longer need the `Homepage` Form to be our [startup Form](/docs/client/components/forms#the-startup-form-or-module). Whenever a Form that uses our Layout is opened, it instantiates the Layout for us, so let’s set `Page1` to be our startup Form instead.

And that’s it! Our app is now using Layouts.

Here’s a link if you would like to clone a finished example:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:53LI5KDBQJPHVATK%3dF4PKH7RRYXYEHUZYQUWS5AFE)

To learn more about Layouts, check out our [documentation here](/docs/ui/layouts#layouts).
