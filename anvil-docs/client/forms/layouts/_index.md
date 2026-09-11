---
document: "Layouts"
title: "Layouts"
url: "/docs/client/forms/layouts"
doc-id: layouts-_index
state: Live
date-created: 2026-09-08
---


# [Layouts](#layouts)

The structure of an Anvil [Form](/docs/client/forms) is defined by its Layout. A Layout is a Form that provides the visual template for other Forms.

Layouts have slots that define where components can be added. They can also have properties and interactivity of their own, just like components. You can use a Layout provided by an Anvil theme, or you can construct your own by creating a Form and turning it into a Layout. A Form can both use a Layout and be a Layout for other Forms.

## [Choosing a Layout](#choosing-a-layout)

To create a Form that uses a Layout, click the “+ Add Form” button then choose a Layout from the options in the dialog.

Here you will see any Layouts you have created in your app as well as Layouts defined by your app’s theme or any dependencies.

If a Form already uses a Layout, you can switch its Layout by clicking the three dots button at the top of the Form and selecting “Choose layout”. You can then pick a Layout from the options in the dialog. If the Form does not already use a Layout, then you cannot switch it to using a Layout. Create a new Form instead.

If you choose a new Layout that doesn’t have the same slots as your old Layout, components in those slots will disappear. If this happens, you can retrieve them by dragging and dropping them out of the [**Orphaned Components** panel](#orphaned-components).

## [Creating a Layout from an Anvil Form](#creating-a-layout-from-an-anvil-form)

Any Form can become a Layout. To enable a Form to be used as a Layout, choose “Use as Layout” from the three dots menu at the top of the Form

### Adding Slots

Once your Form is a Layout, you’ll be able to drag and drop Slots from the Toolbox onto the Form. **Slots are not components**, instead they describe where components can be added to Forms that use that Layout.

### Orphaned components

Each Slot has a name, which can be changed. However, if the Form is already being used as a Layout and you change the name of a Slot, then any components that were in that Slot will become orphaned. You can retrieve them by dragging and dropping them out of the **Orphaned Components** panel.

### Adding a thumbnail and description

You can set a thumbnail image and a description for your Layout Form that will be displayed when adding a new Form or switching to a new Layout.

Click on the three dots menu at the top of the Form Editor and select “Edit Properties and Events”. In the dialog that opens, you will find a section called “Layout Metadata” where you can change the title and description of your Layout and upload a thumbnail image. The thumbnail should be 246px x 128px or a 123:64 aspect ratio.

### Layout properties and events

Layouts can have their own properties and events, just like components. For example, if a Layout Form has a top app bar, it could have a property that sets the color of the app bar.

To edit the properties and events of your Layout, click on the three dots menu at the top of the Form Editor and select “Edit Properties and Events”. This will open a dialog that allows you to set custom properties and events for your Layout Form.

Setting custom properties and events for Layouts is the same as setting them for custom components. See the [custom component documentation](/docs/client/customisation/custom-components) for more information about how to set up properties and events.

You can access a Layout’s properties and events from the Form that is using the Layout by using `self.layout`. For example, if a Layout Form has a property called `app_bar_background_color`, then you can set its value from a Form that is using the Layout with `self.layout.app_bar_background_color = "#1bb0ee"`.
