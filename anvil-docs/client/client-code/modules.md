---
title: "Modules"
url: "/docs/client/client-code/modules"
---


# [Modules](#modules)

Modules allow you to write code that exists independently of your Forms. They also allow you to write code that can be used on the server and in the browser.

You can add Modules to your app in the same way you add Forms.

These are Python modules that you can import in your Forms. You can also import them in Server Modules.

Module code is loaded in the same environment as whatever is importing it. If you import a Module from a Form, it will be loaded in [approximately Python 3.7](/docs/client#what-kind-of-python); if you import from [server code](/docs/server), it will be loaded in whichever Python version you have chosen.

The user of an app can see source code for your Modules. They can also manipulate how Module code behaves in the browser. (Of course, they can’t change how Modules behave when they’re imported by [Server Modules](/docs/server) and running on Anvil’s servers.)

## [Startup Module](#startup-module)

You can also launch your app with a Module, rather than a [Form](/docs/client/forms/forms-in-the-editor#the-startup-form). This means you can execute code before you’ve decided which page to open.

Your module code can then call [`open_form()`](/docs/client/navigation#using-open_form) to display the user interface.

```python
# In the startup module
from anvil import open_form

open_form('Form1') 
```

## [Global variables](#global-variables)

Passing values between different Forms is simple. You can create a Module that has global variables, and import it in different Forms. Changing a global variable in one Form makes it available in another.

In [this example app](https://sidebar-navigation.anvil.app) there are two different pages, each of which is a different Form. There’s a counter on each Form to display the number of times the user has clicked a link.

This is achieved in a module named `Global`, which has a variable named `number_of_clicks`. In each Link’s click handler, `number_of_clicks` is incremented. The `Global` module can be imported into each Form, which allows the `number_of_clicks` to be displayed in a Label.

Click to clone the example app in the Anvil designer:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:NCSFDLM25ZJRUGDM%3d6ZOE23O7ZRM7GQVALKGSJE2X)

### Global variables in Server Modules

Each server function call is executed in a new Python interpreter, meaning that global variables won’t persist between server function calls. Instead, you can store data between server calls using [session state](/docs/server/sessions-and-cookies).

Enabling Persistent Server Modules by checking ‘Keep server running’ allows the same interpreter to be used for multiple function calls.

Persistent Server Modules are available on the [Business Plan](/pricing) and above.

Persistent Server Modules can serve as a performance optimisation, allowing you to perform expensive variable instantiation when your server code runs for the first time.

If ‘Keep server running’ is checked, global variables **may** persist between server function calls.
