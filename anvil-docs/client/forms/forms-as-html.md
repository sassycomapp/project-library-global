---
title: "Forms as HTML"
url: "/docs/client/forms/forms-as-html"
---


# [Forms as HTML](#forms-as-html)

You do not need to know HTML to use Anvil. You can build your UIs entirely with the drag-and-drop designer without having to edit your Form’s UI as text in the [HTML view](/docs/editor/form-editor#html-view).

Under the hood, the user interface of every Form in Anvil is represented by [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML), including any [Anvil Components](/docs/components) on the Form. [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) is the markup language used to write ordinary web pages.

You can inspect and edit a Form’s HTML from the Anvil Editor in [HTML view](/docs/client/forms/forms-in-the-editor#html-view). Changes made to a Form through the [drag-and-drop designer](/docs/editor/form-editor#design-view) are reflected in the Form’s HTML and vice versa.

## [The structure of a Form’s HTML](#the-structure-of-a-forms-html)

In most cases, the root of a Form’s HTML is the `<anvil-form>` element. This element defines whether the Form is structured with a [container](/docs/components/standard-components/containers) component or a [Layout](/docs/client/forms/layouts) Form. The root of a Form’s HTML can also be native HTML or an Anvil component. See [Form Templates](/docs/client/forms/form-templates) for more details on the different Form types.

Each [Anvil component](/docs/components) in a Form is represented by an `<anvil-component>` tag, specifying the type of component, its properties and data:

-   The `type` attribute specifies the type of Anvil component, e.g. `"Button"`, `"TextBox"`
-   The `name` attribute is its Python name, used to reference it in your [Form’s code](/docs/client/forms/forms-as-python-classes)
-   The component properties are set using the `prop:` prefix, e.g. `prop:text="Maya Chen"`.
-   [Data Bindings](/docs/client/component-properties/data-bindings) are set using `bind:` along with the property and data, e.g. `bind:text="self.item['name']"`. If [writeback](/docs/client/component-properties/data-bindings#two-way-data-bindings) is enabled, the `writeback` attribute is used, e.g. `writeback:text="self.item['name']"`.

[Container components](/docs/components/standard-components/containers) can contain other components between their opening and closing `<anvil-component>` tags. For example, in the image below, the [FlowPanel](/docs/components/standard-components/containers#flowpanel) contains two [Labels](/docs/components/standard-components/containers#flowpanel) for projects and location:

When components are placed in a [slot](/docs/client/forms/layouts#adding-slots) they are wrapped in an `<anvil-block>` element. The `slot` attribute specifies the name of the slot it fills:

## [Combining HTML and Anvil components](#combining-html-and-anvil-components)

A Form can consist of native HTML elements as well as Anvil components.

For example, this profile card uses a native HTML image element alongside Anvil components:

The `<img>` element is ordinary HTML that uses the `profile-avatar` CSS class. The `LinearPanel` and `Label` elements are Anvil components. They are all in an `<anvil-form>` whose container is a [Column Panel](/docs/components/standard-components/containers#columnpanel).

For more details on using native HTML elements in your Anvil Forms, see [Adding HTML Elements](/docs/client/adding-ui-elements/adding-html-elements).
