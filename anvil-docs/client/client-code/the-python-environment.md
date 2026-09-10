---
title: "The Python Environment"
url: "/docs/client/client-code/the-python-environment"
doc-id: the-python-environment
state: Live
date-created: 2026-09-08
---


# [The Client-side Python Environment](#the-client-side-python-environment)

Your Form code, which runs in the browser, runs in approximately Python 3.7. We say “approximately”, because in fact your Python code is being compiled to Javascript so it can run right in the user’s browser.

Anvil compiles client-side Python into Javascript using the [Skulpt](http://skulpt.org) compiler. This compiler supports a subset of Python 3.7. Some standard libraries are missing or incomplete – particularly libraries such as file manipulation that do not make much sense in a web browser. Skulpt also cannot compile third-party Python libraries.

If you need to use a library or language feature that is not available in the browser, don’t worry – you can make a function call to a [Server Module](../../server/server-modules) which runs in a full Python environment. You can also make function calls to and from your own Python environments using the [Uplink](../../external-resources/uplink).

Our client-side Python support uses the open source [Skulpt](http://skulpt.org) Python-to-Javascript compiler. We believe strongly in giving back to open source - if you want to join the project, visit Skulpt [on GitHub](https://github.com/skulpt/skulpt).

## [The `anvil` module](#the-anvil-module)

[API Docs](../../api/anvil)

The `anvil` module is Anvil’s Python API.

Most of the Anvil-specific Python code in this documentation uses classes and functions from `anvil`. In particular, all the [component](../../ui/components) classes are in the `anvil` module. Anvil’s core server-side functionality is in `anvil.server` (along with client-side functionality that relates to the server, such as `anvil.server.call`). Other features of Anvil have their own namespaces within `anvil`, such as `anvil.email`, `anvil.users` and `anvil.http`.

The `anvil` module is imported by default in Forms, and must be referred to explicitly in [Server Modules](../../server/server-modules) (when you add a Service, the relevant imports are automatically written for you).

A complete listing of classes and functions in the `anvil` module is available in the [API Reference](../../api).

## [When your app starts](#when-your-app-starts)

When a user opens your app in their browser, what happens first depends on which Form or Module is set to run at startup – that’s the one marked with the lightning bolt icon. You can change your startup code in the [App Browser](../../editor#the-app-browser).

**If your app runs a [Form](../../client/forms) on startup:** Anvil will instantiate and then display that Form class, as if you had called the [`open_form()`](../../client/navigation#using-open_form) function with the name of that Form.

**If your app runs a [Module](modules) on startup:** Anvil will load and run the specified Module as a Python script. Your code can then call [`open_form()`](../../client/navigation#using-open_form) to display its user interface.

## [Storing data in memory](#storing-data-in-memory)

Since the client-side Python runs in the user’s web browser, you can store data in the browser’s memory by creating variables in Python.

In the following example, we store a list of active filters as an attribute of the `Form1` class. When the Form loads, the list of filters is empty. The Form contains a series of CheckBoxes, and when one is checked, we add its `text` to the list of active filters.

```python
class Form1():
  def __init__(self, **properties):
    # No filters are active on startup.
    self.active_filters = []

  def check_box_change(self, **event_args):
    # When a CheckBox is changed, set the active filter accordingly
    check_box = event_args['sender']
    if check_box.checked:
      self.active_filters.append(check_box.text)
    else:
      self.active_filters.remove(check_box.text)
```

You can also create [global variables](../../client/client-code/modules#global-variables) that can be used by all your Forms.

This data persists as long as the app is open in the user’s browser tab. If you want to store data to be retrieved when the user re-vists your app, you can use Anvil’s built-in [database](../../data-tables), or use [Sessions and Cookies](../../server/sessions-and-cookies).

## [Unit tests for client-side code](#unit-tests-for-client-side-code)

A partial implementation of the Python ‘unittest’ library is available in the client side Python that runs in the browser.

On the [server side](../../server), both ‘unittest’ and ‘pytest’ are available.

## [Blocking Code](#blocking-code)

Python code is blocking if the execution must wait for a process to complete before continuing. If you use `time.sleep()` or `anvil.server.call()` then you have written blocking code

If you receive a `SuspensionError`, it means the Python-to-Javascript compiler does not support blocking code at that location.

The following are considered blocking in Python:

-   `sleep()`
-   [`anvil.server.call()`](../../server/server-modules#calling-server-functions-from-client-code)
-   [`anvil.users.get_user()`](../../users#checking-user-permissions)
-   Interacting with [Data Tables](../../data-tables)
-   Importing less common modules from the Python standard library may block
-   Interacting with `anvil.js` when the Javascript returns a `Promise` e.g. [`anvil.js.import_from(url)`](../../client/customisation/javascript)

You’ll find that blocking code is supported almost everywhere in client-side Python. You should rarely need to think about it. However, there are certain places where blocking code is not supported:

### Python Dunders

Overriding certain Python dunders (or magic methods) may result in a `SuspensionError`. For example, you may want to use blocking code in a custom `__iter__` that invokes lazy loading of data using `anvil.server.call()`. Unfortunately, client-side Python does not support blocking code when creating an iterator object. `__next__`, however, does support blocking code. Lazy loading can therefore happen in the first call to `__next__`.

Common dunders that do **not** support blocking code:

-   `__iter__`
-   `__repr__`
-   `__str__`
-   `__bool__`
-   Number dunders like `__add__`, `__mul__`
-   Comparison dunders like `__eq__`, `__gt__`

Common dunders that **do** support blocking code:

-   `__getattr__`, `__setattr__`
-   `__getitem__`, `__setitem__`
-   `__next__`
-   `__dir__`
-   `__init__`, `__new__`
-   `__len__`
-   `__contains__`
