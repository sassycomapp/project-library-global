---
document: "Using the Extensions API"
title: "Using the Extensions API"
url: "/docs/integrations/x/tableau-extensions-api"
doc-id: tableau-extensions-api
state: Live
date-created: 2026-09-08
---


# [The Tableau Extensions API](#the-tableau-extensions-api)

Tableau Extensions can access data and components within a Tableau dashboard, using the [Extensions API](https://tableau.github.io/extensions-api/) provided by Tableau. Anvil X gives you access to the Extensions API from Python, as the `anvil.tableau` module.

This gives you access to all the objects in the Extensions API from Python, as described in Tableau’s [API documentation](https://tableau.github.io/extensions-api/docs/index.html).

## [Using `trexjacket`](#using-trexjacket)

While it is entirely possible to create extensions with only the Tableau Extensions API, it is a fairly low-level API. Instead, you might want to consider the higher-level [Trexjacket](trexjacket) library, which is designed to make extension development easier.

You can use Trexjacket alongside the Extensions API, so you can mix and match – for example, you might use Trexjacket for common tasks, and the Extensions API for advanced operations not included in Trexjacket.

[Learn more about Trexjacket](https://trexjacket.readthedocs.io)

## [Using the Tableau Extension API directly](#using-the-tableau-extension-api-directly)

The `anvil.tableau` module is imported automatically in every Anvil X project:

```python
from anvil import tableau
```

This gives you access to the full `tableau.extensions` API from Python. For example, in order to get the name of every worksheet in the current dashboard, you can write the following Python code:

```python
worksheet_names = [
    worksheet.name for worksheet in
    tableau.extensions.dashboardContent.dashboard.worksheets
    ]
```

Similarly, you can register [event listeners](https://tableau.github.io/extensions-api/docs/interfaces/worksheet.html#addeventlistener) using Python functions, or methods of your [Form](https://anvil.works/docs/client/ui#forms) class:

```python
class Form1(Form1Template):
    def __init__(self, **properties);
        super().__init__(**properties)

        first_worksheet = tableau.extensions.dashboardContent.dashboard.worksheets
        first_worksheet.addEventListener("mark-selection-changed", self.print_mark)

    def print_mark(self, event):
        marks = event.getMarksAsync()
        print(f"{len(marks)} marks selected")
```

## [Learning more](#learning-more)

To learn more about the Tableau Extensions API, please see the [Tableau Extensions API Basics page](https://tableau.github.io/extensions-api/docs/trex_api_about.html) and consult the [API reference documentation.](https://tableau.github.io/extensions-api/docs/index.html)
