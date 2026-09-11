---
document: "Navigation"
title: "Navigation"
url: "/docs/client/navigation"
doc-id: navigation-_index
state: Live
date-created: 2026-09-08
---


# [Navigation](#navigation)

Anvil apps are [Single-Page Applications](https://developer.mozilla.org/en-US/docs/Glossary/SPA). When you open an Anvil app, only a single web page is loaded, but the content on that page can change.

You can navigate between content in an Anvil app by opening and closing [Forms](/docs/client/forms). This can be done in two different ways:

-   You can directly use [the `open_form` method](#using-open-form).
-   You can [implement URL routing](#using-routing-for-url-functionality) in your app to open and close Forms based on the current URL.

## [Using `open_form`](#using-open_form)

The simplest way to display a Form is to call the `open_form` method. This method, which can be imported from [the `anvil` module](/docs/api/anvil), will display an instance of whatever Form name you pass to it as an argument.

When you do this, the new Form takes over entirely and becomes the top-level Form. The old Form is no longer visible.

If you pass any extra parameters into `open_form()`, they are passed to the new Form’s constructor:

```python
class Form1(Form1Template):
  # ...

  def btn1_click(self, **event_args):
    open_form('Form2', my_parameter="an_argument")
```

As well as specifying a Form by name, you can also create an instance of the Form yourself and pass it in. This code snippet is equivalent to the previous one:

```python
from ..Form2 import Form2

class Form1(Form1Template):
  # ...

  def btn1_click(self, **event_args):
    frm = Form2(my_parameter="an_argument")
    open_form(frm)
```

Note that Forms are not available to other Forms unless you explicitly import them. Each Form has its own module, which has the same name as the Form, so to import Form2 from inside Form1, you use `from ..Form2 import Form2`.

[Learn about importing Forms, Modules and Packages in Anvil](/docs/app-architecture/how-to-import-things)

### Resetting the current Form

To reset the Form that’s currently open, just run `open_form(form_name)`. For example, if Form1 is open, run `open_form("Form1")`.

### Maintaining a consistent structure

Oftentimes, you’ll want to build an app that has a navigation bar so that users can switch to different pages in your app. The best way to build this is by creating a [Layout Form](/docs/ui/layouts) that has a Slot for the main content and a navigation bar with Links inside. You can then add Forms to your app that use the Layout Form as their Layout. The Links in the Layout Form should each have an event handler that calls `open_form` to switch to the desired Form.

```python
def about_us_link_click(self, **event_args):
  """This method is called when the link is clicked"""
  open_form('AboutUs')
```

Because the Forms are all using the same layout, the pages in your app will have the same navigation bar.

Check out our tutorial on creating a multi-page app to see a worked example of using a Layout Form to navigate between pages:

Tutorial: Using Layouts to Create a Multi-Page App

## [Using routing for URL functionality](#using-routing-for-url-functionality)

Because Anvil apps are Single-Page Apps, updates to the webpage are not reflected in the URL. If we want the URL to reflect the state of the page, we can use **URL routing**. The best way to implement URL routing in an Anvil app is to use Anvil’s Routing dependency.

Routing is an advanced feature and isn’t needed for most apps. However, if you want the URL to change with your app’s page contents, [this section](/docs/client/navigation/routing) of the documentation will walk you through most of the dependency’s features.
