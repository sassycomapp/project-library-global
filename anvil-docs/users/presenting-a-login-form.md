---
title: "Presenting a Login Form"
url: "/docs/users/presenting-a-login-form"
doc-id: presenting-a-login-form
state: Live
date-created: 2026-09-08
---


# [Presenting a Login Form](#presenting-a-login-form)

The simplest way to use the Users service is to call `anvil.users.login_with_form()` on the client. This function shows a graphical login form, including all the options configured in the Users service (eg password, Google, two factor authenticatication, and new-account registration). If login succeeds, `anvil.users.login_with_form()` returns the user object; if it is cancelled, it returns `None`.

Call this in the `__init__` method of your startup Form to show a login form when your app loads. Otherwise, call it wherever you like in client code to show a login form at an appropriate time, for example when a user attempts to enter a restricted area or wants to pay for the items in their basket.

```python
user = anvil.users.login_with_form()
```

See the [API Docs](/docs/api/anvil.users#login_with_form) for full argument list.

By default, users can sign in with their email address and password, or sign up for a new account. By default, they will need to confirm their email address by clicking on a link. All of this is configurable in the Users service.

You can also explicitly bring up the new-user registration form by calling `anvil.users.signup_with_form()`. If signup succeeds, this function returns the new user object; if cancelled, it returns `None`. There is a ‘signup’ button on the Login form as well, so you only need this function if you want the signup button elsewhere.

```python
anvil.users.signup_with_form()
```

See the [API Docs](/docs/api/anvil.users#signup_with_form) for full argument list.

Note that, even if a new user has been created, they will not be logged in if their account is not yet enabled. For example, if the user needs to confirm their email address, `anvil.users.signup_with_form()` can return a user object, but `anvil.users.get_user()` will still return `None` because they are not yet logged in. If no confirmation is required, the new user will be logged in immediately.

To get the currently logged-in user, call `anvil.users.get_user()`. This returns the currently logged-in user, or `None` if no user is logged in.

```python
user = anvil.users.get_user()
```

Call this function in a server module before doing anything you need to protect: Remember, form code cannot be trusted, because a malicious user can change it to do whatever they want!

To log a user out, call `anvil.users.logout()`. After this function returns, `anvil.users.get_user()` will return `None`.

```python
anvil.users.logout()
```

You can see all registered users when you open the Users service.

## [Configuration Options](#configuration-options)

As well as choosing the [available authentication methods](authentication_choices), there are various other options that can be customised.

### Require Secure Passwords

When this option is selected, users signing up with an email address and password will be required to choose a password that is at least 8 characters long and that has not been previously leaked online. This check is performed [without sharing the password with any third-party services](https://blog.cloudflare.com/validating-leaked-passwords-with-k-anonymity/).

### Remember login between sessions

When this option is selected, users will see a “Remember me” checkbox on the login form. If they leave this checked (the default), the fact that they are logged in will be stored in an [Anvil cookie](/docs/server/sessions-and-cookies#cookies) for a configurable time (30 days is the default).

Which cookie is used depends on the “share login status” option, below. If a user visits an app where they are already logged in, `anvil.users.get_user()` will return that user without the need for them to log in again. You can still allow them to log in as a different user by calling `anvil.users.login_with_form()` as usual. Calling `anvil.users.logout()` will remove their login status from the cookie as well as logging them out in the current session.

This logic also applies to manual calls to `login_with_email()`, `force_login()`, and similar functions. They each accept `remember=` keyword argument to control whether to remember this user’s login.

The remembered login sessions will be stored in the `remembered_logins` column for that user. To un-remember a user’s login session, delete the contents of the `remembered_logins` column for that user.

### Share login status with other apps

Selects which [Anvil cookie](/docs/server/sessions-and-cookies#cookies) is used to store the user’s login status. If not selected (the default), user login status will only be remembered for this app and will not affect (or be affected by) user behaviour on any other apps. When selected, users’ login status is stored in the shared Anvil cookie, meaning that they will be automatically logged into any other apps sharing the same Users table and on the same top-level domain (anvil.app by default).

### Require 2-factor authentication

When this option is selected, a second login screen is added to the login process to collect a second factor of authentication. The second factor of authentication can be either a hardware token, such as a [YubiKey](https://www.yubico.com/) or other FIDO/FIDO2 device, or a code from an authenticator app. For more detail, please see our [two factor authentication documentation](/docs/users/two_factor_authentication).

`Require 2-factor authentication` comes with two additional options. `Allow 2-factor reset by email` displays a link on the second factor login screen that allows the user to reset their second factor of authentication by sending a reset link to their email. `Remember 2-factor authentication state for` allows you to select how frequently a user has to provide their second factor of authentication; if it is `disabled`, the user will have to provide their second factor every time they log in.
