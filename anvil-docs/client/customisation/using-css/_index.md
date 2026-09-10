---
title: "Using CSS"
url: "/docs/client/customisation/using-css"
doc-id: using-css-_index
state: Live
date-created: 2026-09-08
---


# [Using CSS in Anvil Apps](#using-css-in-anvil-apps)

You can build the front-end of your app entirely in Python using [Anvil’s components](/docs/ui/components). However, your app still uses [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) and [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) under the hood.

Anvil components generate HTML. When you change their [properties](/docs/client/component-properties) in the [Properties Panel](/docs/editor/form-editor#properties-panel) or in the [Form’s code](/docs/client/forms), the CSS applied to them is updated automatically.

If you are new to CSS, our [introductory guide](/articles/using-css) explains how to customise the appearance of web apps.

## [Writing CSS in theme.css](#writing-css-in-themecss)

Every Anvil app includes a stylesheet called [`theme.css`](/articles/using-css#writing-css-in-the-stylesheet). Depending on the theme you choose when creating your app, it may already contain default CSS rules targeting Anvil components. You can write CSS rules here in the traditional way to [change a component’s appearance](using-css/roles#changing-the-components-style-in-css). For example, see [Customising the Loading Indicator](using-css/loading_indicator).

## [](#reusing-styles-with-roles)[Reusing Styles with Roles](using-css/roles)

To apply consistent styling across multiple components, you can create reusable style classes called **Roles**. They can be applied to components through the Properties Panel or in the Form code. See [Roles](using-css/roles) to learn how to create and use them.
