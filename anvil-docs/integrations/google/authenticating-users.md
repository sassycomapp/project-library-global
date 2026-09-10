---
title: "Authenticating Users"
url: "/docs/integrations/google/authenticating-users"
doc-id: authenticating-users
state: Live
date-created: 2026-09-08
---


# [Authenticating Users with Google](#authenticating-users-with-google)

Your users can log in to their Google accounts in your app. It’s easy to add Google login to the Users Service - see [Users:Authentication Choices](/docs/users/authentication_choices) to see how.

If you want to use the Anvil Google API to present a login form just for Google accounts, this section tells you how. You may wish to do it this way if you don’t want to store your users email addresses in your app’s Users table.

You don’t need the user to log in to Google if you only use app files or send email. Those belong to the app, not the user.

## [Log in](#log-in)

To allow your users to log into your app with Google, call `anvil.google.auth.login()`.

```python
import anvil.google.auth

email_addr = anvil.google.auth.login()
print(f"User logged in as {email_addr}")
```

If the login succeeds, `anvil.google.auth.login()` will return the user’s email address.

If the login fails, or the user cancels, `anvil.google.auth.login()` will raise an exception.

## [Check who is logged in](#check-who-is-logged-in)

To find out who is currently logged in, call `anvil.google.auth.get_user_email()`. If nobody is logged in, this returns `None`.

```python
import anvil.google.auth

# This can run on the server:
email_addr = anvil.google.auth.get_user_email()
print(f"{email_addr} is now logged in")
```

The `get_user_email` function can be called from a [Server Module](/docs/server), or [Uplink](/docs/uplink) code, to check whether a user is authorised to perform the requested action.
