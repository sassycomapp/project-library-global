---
title: "Sessions and Cookies"
url: "/docs/server/sessions-and-cookies"
doc-id: sessions-and-cookies
state: Live
date-created: 2026-09-08
---


# [Sessions and Cookies](#sessions-and-cookies)

When your users visit your app, their browser starts a ‘session’ and stores a token to identify what session they are in. If they run your app again in the same browser window, your app will get the same session token. Anvil uses this to allow you to store data in Server Modules for the duration of a user’s session.

To store small amounts of data in between sessions, you can use cookies. Cookies are stored in the user’s browser.

(For larger-scale data persistence, use [Data Tables](../data-tables))

## [Storing session data](#storing-session-data)

In your Server Module, you might want to save information between calls in the same session. For example, you might want to store which pages the user has visited in this session.

Server Modules have access to a dictionary called `anvil.server.session`. This data is private - it’s never sent to the user’s web browser - and it is saved between calls to Server Module functions. (All other variables will get wiped.)

The data in `anvil.server.session` is specific to the session - that is, each browser window running the app has its own `anvil.server.session`. So it will be different for each user. Each server session has a unique ID that is stored in the dictionary. You can find it by calling `anvil.server.session.session_id` or `anvil.server.get_session_id()`.

In this example, we count how many times `ring_the_bell()` has been called:

```python
import anvil.server

@anvil.server.callable
def ring_the_bell():

  n_rings = anvil.server.session.get("n_rings", 0)
  n_rings += 1

  print("DING!")
  print(f"You have rung the bell {n_rings} times")

  anvil.server.session["n_rings"] = n_rings
```

Here’s another example, where we use `anvil.server.session` to record whether a user entered the correct password (normally we’d let the [Users Service](/docs/users) do this for us, which hashes the password to make things secure). We can later check that the user has authenticated before we let them upload data to an app file in Google Drive.

```python
import anvil.server
from anvil.google.drive import app_files

@anvil.server.callable
def check_password(password):
  if password == "MY SECRET":
    anvil.server.session["authenticated"] = True

@anvil.server.callable
def overwrite_file(new_data):
  if anvil.server.session.get("authenticated", False):
    app_files.my_file.set_bytes(new_data)
```

### What can sessions store?

`anvil.server.session` can store anything that a server function can return, except for Media objects. This includes [Data Table](/docs/data-tables) Rows.

For more information, see [Valid Arguments and Return Values](/docs/server/server-modules#valid-arguments-and-return-values).

## [Session expiry](#session-expiry)

An Anvil session will stay open as long as an operation has been performed in the last 30 minutes.

If a user’s session expires, the next server operation will cause the following dialog to appear.

Note that a “server operation” isn’t always a call to `anvil.server.call()`. It could be a [data table search](/docs/data-tables/data-tables-in-code#searching-querying-a-table) or a [Google Drive](/docs/integrations/google/google-drive) query.

### Recovering from an expired session

For most apps, the default session behaviour is sufficient. However, some advanced apps might want to recover from an expired session themselves. Here’s how to do it.

When a user’s session expires, the server operation is raising an `anvil.server.SessionExpiredError`. If this exception is not caught, you will see the ‘Session Expired’ dialog.

Once the session has expired, *every* server operation will raise an `anvil.server.SessionExpiredError`. To stop this from happening, you must call `anvil.server.reset_session()`.

```python
# We think we might have timed out
try:
  anvil.server.call("foo")
except anvil.server.SessionExpiredError:
  anvil.server.reset_session()
  # This will work now, but with a blank session
  anvil.server.call("foo")
```

You now have a fresh, blank session. This may cause some unexpected behaviour. For example:

-   You will be logged out from the Users service (`anvil.users.get_user()` will return `None`)
-   `anvil.server.session` will be reset to an empty dictionary (`{}`)
-   Objects returned from the server (eg table rows and Google Drive files) will no longer be valid, and will raise exceptions if you try to use them.

We recommend that manually catching `SessionExpiredError` should only be done if necessary.

## [Cookies](#cookies)

Cookies allow you to store a small amount of information securely in the user’s browser between sessions. Cookies can only be accessed/modified in Server Modules (or via the [Uplink](/docs/uplink)).

Anvil provides two types of cookies for you to choose from:

-   `anvil.server.cookies.local` is a private cookie available only to Server Modules within your app. Information stored in this cookie is not accessible to any other app.
-   `anvil.server.cookies.shared` is a cookie shared by all your apps (or those in your team if you belong to one). Information stored in this cookie is readable and writeable by Server Modules in any of your apps.

Cookies can be accessed like simple Python dictionaries to get and set values, including the usual `get` method to return a default value if the key is not found. See below for code samples.

Values set using the standard `[ ]` indexing notation will expire after 30 days. To set a custom timeout, use the `set(timeout, **vals)` method, which accepts a custom timeout (in days), and the values as keyword arguments.

To clear all the keys/values in a cookie, call the `clear()` method.

Updates to cookies take effect immediately. This means that the user can navigate away from the page any time after a cookie has been updated and the data will persist.

```python
# In a Server Module:

# Set a value with the default expiry of 30 days:
anvil.server.cookies.local['name'] = "Bob"

# Set multiple values with an expiry of 3 days:
anvil.server.cookies.local.set(3, name="Bob", age=42)

# Remove a value:
del anvil.server.cookies.local['age']

# Get a value, or return a default if not found:
anvil.server.cookies.local.get("name", "Not Found")

# Clear the cookie:
anvil.server.cookies.local.clear()
```

### What can cookies store?

Cookies can store any type of value that you can pass to/from a server function, except for Media objects. This includes Data Table Rows.

For more information, see [Valid Arguments and Return Values](/docs/server/server-modules#valid-arguments-and-return-values).

Bear in mind that cookies are limited by most web browsers to around 4Kb. This could be used up very quickly if you store anything more than very simple objects. If the data passed to a cookie is too large to be accepted, an `anvil.server.CookieError` will be raised.

If your app is hosted at `.anvil.app`, the data limit will be shared with other `.anvil.app` apps that the user visits. Use a [Custom Domain](/docs/deployment/custom-domains) to avoid this.

### Security

Information in cookies is encrypted, so no-one can access the information, even by inspecting their own web browser.

This information is also authenticated, so if you read information from a cookie then you can be sure that you put that information there.

It is not possible for a user to fake the value of one of their cookies, or to reuse the value of one cookie as the value of another.
