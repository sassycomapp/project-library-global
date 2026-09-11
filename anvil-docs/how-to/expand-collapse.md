---
document: "Expand and collapse sections of pages"
title: "Expand and collapse sections of pages"
url: "/docs/how-to/expand-collapse"
doc-id: expand-collapse
state: Live
date-created: 2026-09-08
---


# [Expand and collapse sections using components](#expand-and-collapse-sections-using-components)

Components can be shown and hidden by setting their `visible` property to `True` or `False`. Showing or hiding a [container](/docs/client/components/containers) such as a ColumnPanel shows or hides the components within it, allowing you to create expandable/collapsable sections of pages.

You can use this technique to make the contents of a Data Grid cell expandable/collapsable.

[Here’s an example app](https://expandable-stock-chart-grid.anvil.app) showing a Data Grid full of stock data. There’s a column containing a time-series chart for the price of each stock. The chart is hidden by default, and it can be shown by clicking a Link.

Click here to clone the example app in the Anvil designer:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:2TSJEOQK7TS6IRWP%3dYUA3R6GLI3Q3VKAKDIX7QAGR)
