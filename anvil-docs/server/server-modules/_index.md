---
document: "Server Modules"
title: "Server Modules"
url: "/docs/server/server-modules"
doc-id: server-modules-_index
state: Live
date-created: 2026-09-08
---


# [Server Modules](#server-modules)

Anvil’s Server Modules are a full server-side Python environment, with the ability to [import any packages you like](/docs/server/custom-packages).

The user has ultimate control over their own browser: If they open up their browser’s developer tools or Javascript console, they can see and modify all the client-side code in your Anvil app (that’s your Forms and Modules).

Sometimes, you want to write code that always executes exactly as it is written (for example, checking a password before changing a file), or code that contains some secret information (for example, your secret authentication keys for a third-party API).

You can write this code in a server module, and it will never be seen by your app’s users (even if they’re experts and poking around inside their own browser). You can call functions in your server modules from your client side code.

You can pass useful things like [data table rows](/docs/data-tables) and [Media objects](/docs/working-with-files/media) to and from server functions, as well as simple Python data structures (more information [below](#valid-arguments-and-return-values)).

Check the [Quickstart](/docs/server/server-modules/quickstart) to see some examples and get up and running. To learn more about the difference between client and server code, see [this explanation](/articles/client-vs-server).

## [Calling server functions from client code](#calling-server-functions-from-client-code)

To make a server function available from your client code, decorate it as `@anvil.server.callable`.

For example, in the [Feedback Form](/learn/tutorials/feedback-form) tutorial, `add_feedback` is decorated as `@anvil.server.callable`:

```python
import anvil.server

@anvil.server.callable
def add_feedback(name, email, feedback):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now()
  )
  
  anvil.email.send(to="noreply@anvil.works", # Messages go to the app owner
                   subject="Feedback from {}".format(name),
                   text=f"""A new person has filled out the feedback form!
                   Name: {name}
                   Email address: {email}
                   Feedback:{feedback}
                   """)
```

From ordinary client-side code, you can call your server-side function using `anvil.server.call(<function_name>)`, where `function_name` is the function name as a string.

For example, the event handler in the Feedback Form app uses `anvil.server.call`:

```python
  def submit_button_click(self, **event_args):
    name = self.name_box.text
    email = self.email_box.text
    feedback = self.feedback_box.text
    
    anvil.server.call('add_feedback', name, email, feedback)
    Notification("We have recorded your feedback, and sent an email to the owner of this app.", title="Thanks!").show()

    self.clear_inputs()
```

Just call `anvil.server.call(name, more_arguments...)`. Any extra arguments are passed through to the server function. This includes keyword arguments.

You can call server functions from client-side code and [Uplink](/docs/uplink) functions (`anvil.server.call()` is available everywhere). You can even use it to call server functions from other server functions, though in that case it is more efficient to call the function directly rather than wrapping it in an `anvil.server.call()`.

[Tutorial: Feedback Form](/learn/tutorials/feedback-form)

## [Valid arguments and return values](#valid-arguments-and-return-values)

Anvil can only transfer certain data types as the arguments or return values of `@anvil.server.callable` functions. We call these *portable* types, and these are:

-   Strings
-   Numbers
-   Lists
-   Booleans (`True` and `False`)
-   Dicts (with strings as keys)
-   `datetime.date` and `datetime.datetime` objects
-   `None`
-   [Media objects](/docs/working-with-files/media)
-   [Data Table](/docs/data-tables) rows, tables, views or search iterators
-   [Portable Classes](/docs/server/portable-classes) defined by your app

Arguments and return values may not be *circular* (for example, a dict may not contain itself - directly or indirectly).

Data returned from Server Modules or the Uplink has a size limit of 4MB, **excluding Media Objects**. If you want to send more than 4MB of data, send it as a Media Object.

## [Suppressing the spinner](#suppressing-the-spinner)

Using `anvil.server.call` in client code displays a spinner. To call server functions without displaying a spinner, enclose your code in a `with anvil.server.no_loading_indicator:` block:

```python
def do_guess_silently(n):
  with anvil.server.no_loading_indicator:
    anvil.server.call("guess", n)
```

You can also call a server function without displaying a spinner by using `anvil.server.call_s` instead of `anvil.server.call`:

```python
def do_guess_silently(n):
  anvil.server.call_s("guess", n)
```

## [Customising the name of a server function](#customising-the-name-of-a-server-function)

You can customise the name of your callable function by passing a parameter to `@anvil.server.callable`. In this example, the function `foo` must be called with `anvil.server.call('my_func')`.

```python
import anvil.server

@anvil.server.callable("my_func")
def foo():
  return 42
```

## [Require user authentication](#require-user-authentication)

You can also customise the `@anvil.server.callable` decorator to verify that a user is logged in using Anvil’s [Users Service](/docs/users) before executing the function. You do this by passing a `require_user` parameter to `@anvil.server.callable`:

```python
# verify that a user is logged in using the Users Service
@anvil.server.callable(require_user=True)
```

`require_user` can take a boolean value (as above), or a function. If given a function, that function will receive the currently logged-in user (the return value of [`anvil.users.get_user()`](/docs/users/permissions#checking-whos-logged-in)).

For example, if your [Users table](/docs/users/the_users_table) has a boolean column called ‘admin’, you could restrict your server functions to admin users using a regular function:

```python
def validate_user(u):
  return u['admin']

@anvil.server.callable(require_user = validate_user)
def test():
  print("passed the test!")
```

or a lambda function:

```python
@anvil.server.callable(require_user = lambda u: u['admin'])
```

If the logged in user isn’t an admin, the server will raise a `anvil.server.PermissionDenied Exception`.

## [Persistent Server Modules](#persistent-server-modules)

Each server function call is executed in a new Python interpreter. This means each server call has to wait to execute while the interpreter spins up, and global variables don’t persist between server function calls.

Enabling Persistent Server Modules by checking ‘Keep server running’ allows the same interpreter to be used for multiple server function calls. This speeds up your app when making server calls and improves performance.

Persistent Server Modules are available on the [Business Plan](https://anvil.works/pricing) and above.

Persistent Server Modules can serve as a performance optimisation, allowing you to perform expensive setup when your server code loads for the first time.

If ‘Keep server running’ is checked, global variables **may** persist between server function calls, but this is not guaranteed.

## [Server function timeout](#server-function-timeout)

Server functions run synchronously and should return fairly quickly. The timeout is set to 30 seconds, after which a running function will be stopped. For longer-running jobs, you should use [Background Tasks](/docs/background-tasks).
