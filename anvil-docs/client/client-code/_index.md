---
title: "Client Code"
url: "/docs/client/client-code"
doc-id: client-code-_index
state: Live
date-created: 2026-09-08
---


# [Client-side code](#client-side-code)

The user interface of an Anvil app is programmed in Python. This code that makes up the [front-end of your app](/docs/app-architecture) is called client-side code. When someone visits your app, Anvil compiles the client-side Python code into Javascript which runs in the user’s web browser.

Client-side code is mainly written in your [Form](forms) code (but can also be written in [Modules](client-code/modules)). Here you can write Python that interacts with your user interface by manipulating the Python objects that represent components.

For example, when components raise events, they call functions in your client-side code:

```python
@handle("button_1", "click")
def button_1_click(self, **event_args):
  """This method is called when the button is clicked"""
  alert(f"Logged in as: {anvil.users.get_user()['email']}")
```

## [Everything is an object](#everything-is-an-object)

Forms and components are represented in code as Python objects. You can instantiate Forms and components like any Python class:

```python
from .Form1 import Form1
form1_instance = Form1(param='an_argument')

label_instance = Label(text='Hello, World!')
```

These Python objects have attributes and methods that you use to control the UI:

```python
# Change the text on the Label
label_instance.text = "Hello again, World!"

# Get a list of all the components in form1_instance
components_on_form1 = [x for x in form1_instance.get_components()]
```

## [Communicating with the server](#communicating-with-the-server)

Because client-side code runs in the web browser, users have access to it. This means that the client is not a secure environment. Sometimes you’ll want to write secure code (e.g. to access user data from a database or to verify a password before showing a file), or code that cannot run in a web browser. This code should run in a server environment instead.

Anvil provides a secure server to run code, but you can also use your own Python environment. To write code using Anvil’s server environment, you’ll need to add a [Server Module](/docs/server) to your app. Here, you can write secure code including functions that can be called from client-side code. To make a server function callable by the client, you need to decorate it with `@anvil.server.callable`.

```python
@anvil.server.callable
def get_secret_data():
  user = anvil.users.get_user()
  if user['role'] == "secret_agent":
    return app_tables.secret_table.get(message="mission_info")
  else:
    return "You are not authorized to view this message"
```

To then call the function from the client, you just need to use `anvil.server.call()` and pass in the name of the function as a string and any arguments:

```python
self.label_1.text = anvil.server.call("get_secret_data")
```

You can also write client-callable functions in your own Python environment using [the Uplink](/docs/uplink). Once you connect your enviroment to your Anvil app via the uplink, you can decorate your server functions with `@anvil.server.callable` just as if they were in an Anvil Server Module. You can then call these functions from your Anvil app’s client code with `anvil.server.call()`.
