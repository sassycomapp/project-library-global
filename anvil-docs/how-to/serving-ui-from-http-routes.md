---
title: "Serve your UI from HTTP routes"
url: "/docs/how-to/serving-ui-from-http-routes"
---


# [Serving your app’s user interface from HTTP routes](#serving-your-apps-user-interface-from-http-routes)

Anvil lets you serve your app’s user interface directly from [HTTP endpoints](/docs/external-resources/http-apis/creating-http-endpoints) using [`AppResponder`](/docs/external-resources/http-apis/creating-http-endpoints#appresponder-object). This is useful when you want a URL to load a specific Form.

`AppResponder` lets you do things that a plain HTTP response can’t, like setting the page title and metadata for a specific route, and pre-loading data into your Form before it initialises.

If you just want URL-based navigation within your app, the [Routing module](/docs/client/navigation/routing) is a better fit. This guide is for cases where you need direct control over what gets served from a route and how.

## [Setting the page title and description](#setting-the-page-title-and-description)

By default, every page in your Anvil app shares the same title. For example, if a user shares a link to `/directory`, the preview will show your app’s default title rather than anything meaningful about that page. You can use `AppResponder` to set the `title` and `description` of a specific page.

```python
@anvil.server.route("/directory")
def serve_directory(**p):
    responder = anvil.server.AppResponder(
        meta={
            "title": "All Employees",
            "description": "Meet the Team",
        }
    )
    return responder.load_form("DirectoryForm")
```

### Using theme assets in meta tags

If you want an image to appear in social sharing previews, you can reference an image from your app’s [assets](/docs/client/customisation/assets) by prefixing the value with `"asset:"`. Anvil resolves the asset path to the correct URL automatically.

```python
responder = anvil.server.AppResponder(
    meta={
        "title": "All Employees",
        "description": "Meet the Team",
        "og:image": "asset:logo.png",
    }
)
```

## [Pre-loading data with startup_data](#pre-loading-data-with-startup_data)

When a user navigates directly to a URL, any data your Form needs has to be fetched after it loads. With `AppResponder`, you can pre-load that data server-side and make it available at `anvil.server.startup_data` before the Form initialises, avoiding the extra round-trip.

In this example, we pre-load a list of employees from a Data Table and pass it to `DirectoryForm` via `startup_data`:

```python
@anvil.server.route("/directory")
def serve_directory(**p):
    employees = app_tables.employees.search()

    responder = anvil.server.AppResponder(
        data={"employees": employees}, # pre-load startup_data with employees
        meta={
            "title": "All Employees",
            "description": "Meet the Team",
            "og:image": "asset:logo.png",
        }
    )
    return responder.load_form("DirectoryForm")
```

In `DirectoryForm`, read from `startup_data` if it’s available:

```python
class DirectoryForm(DirectoryFormTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        startup = anvil.server.startup_data or {}
        self.employees = startup.get("employees")
```

You can clone the example app from this guide and run it yourself:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:QY5NIV3SARZP4FYB%3dXSQZREIO7AXQSN37JSHCP3XQ)
