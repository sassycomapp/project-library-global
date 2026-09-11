---
document: "Layouts from HTML"
title: "Layouts from HTML"
url: "/docs/client/forms/layouts/html-layouts"
doc-id: html-layouts
state: Live
date-created: 2026-09-08
---


# [Building Layouts from HTML](#building-layouts-from-html)

In addition to building [Layouts from Anvil Forms](docs/client/forms/layouts#creating-a-layout-from-an-anvil-form), you can create Layouts from HTML using HTML Forms. This allows you to build fully custom layouts with HTML elements and Anvil components.

## [Creating an HTML Form Layout](#creating-an-html-form-layout)

Add a new **HTML Form** to your app from the New Form modal.

Click the three dots menu at the top of the Form Editor and select **Use as Layout**. Then switch to the [HTML view](/docs/client/forms/forms-in-the-editor#html-view) to write your Layout’s HTML.

## [Adding slots](#adding-slots)

**Slots** define where components can be added to the Layout when it is used by other Forms. You can add a slot in two ways:

-   **In Design view**, drag and drop a Slot from the Toolbox to where you want it to appear. This will add an `<anvil-slot>` element at that point in your HTML.

-   **[In HTML view](/docs/editor/form-editor#html-view)**, add an `<anvil-slot>` element directly where you want components to appear:

```html
<anvil-slot name="slot-name"></anvil-slot>
```

When another Form uses this Layout, components can be dropped into the named slot.

## [Designer prompts](#designer-prompts)

You might want to add prompts to your Layout that are not visible when the app is run. You can do this by adding the `anvil-designer-only` class to any element, which will make it so the element is only visible in the Anvil Designer.

```html
<!-- The div will only be visible while editing the Form in the designer -->
<div class="anvil-designer-only" style="color: gray; font-style: italic;">
     Drop components below
</div>
<anvil-slot name="slot_1"></anvil-slot>
```
