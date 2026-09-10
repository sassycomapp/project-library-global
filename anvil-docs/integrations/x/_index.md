---
title: "Tableau Extensions with Anvil X"
url: "/docs/integrations/x"
doc-id: x-_index
state: Live
date-created: 2026-09-08
---


# [Anvil X](#anvil-x)

### Create Tableau extensions with Anvil

Anvil X allows you to create extensions for your Tableau dashboards, entirely in Python. Now, your Tableau dashboards aren’t read-only – you can build data apps to take action. Tableau Extension with Anvil X can access and control the data in your dashboard, using the [Tableau Extensions API](x/tableau-extensions-api), or more user-friendly tools such as [Trexjacket](x/trexjacket).

To learn more, check out our blog post:

[Build Tableau Extensions with Anvil X](/blog/announcing-anvil-x-tableau)

### Quickstart

To get started, follow the [Quickstart Guide](x/quickstart) to build a simple Tableau Extension with the Tableau Extensions API alone.

## [Tutorials](#tutorials)

The `trexjacket` project also provides step-by-step tutorials for building real-world Tableau extensions with Anvil X and the high-level `trexjacket` API:

### Annotate your data

You’ve got a dataset, and you’d like to make comments. For example: Why *are* sales so slow in Nevada this quarter, and who has been assigned to investigate?

With this step-by-step tutorial, you’ll build an extension for posting messages about specific data points within the Tableau dashboard, using Tableau’s Superstore data set as an example:

[Tutorial: Build a Chat Extension](https://trexjacket.readthedocs.io/en/latest/tutorials/chat-extension/0-main-page.html)

### Override Sales Data

In this tutorial, you’ll expand the previous tutorial to allow users to not only leave a comment on data, but to override values in the data.

You’ll connect your Tableau dashboard to Anvil’s built-in [Data Tables](/docs/data-tables) and write back to them. Learn how:

[Tutorial: Override Sales Data](https://trexjacket.readthedocs.io/en/latest/tutorials/value-override/index.html)

### Salesforce Writeback

You’ve got a sales dashboard displaying data from Salesforce, but you want to take action - for example, by updating or reassigning opportunities - right in the dashboard. With this step-by-step tutorial, you’ll build an extension to do just that:

[Tutorial: Salesforce Writeback](https://trexjacket.readthedocs.io/en/latest/tutorials/salesforce/index.html)
