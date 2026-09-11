---
document: "Logging in Using Code"
title: "Logging in Using Code"
url: "/docs/users/logging-in-using-code"
doc-id: logging-in-using-code
state: Live
date-created: 2026-09-08
---


# [Logging in Using Code](#logging-in-using-code)

As well as using the built-in login and sign-up forms, you can create your own forms and call the following functions yourself.

All of the manual login and signup functions take an optional keyword argument `remember`, which is `False` by default (for `login_with_form` and `signup_with_form`, the argument is called `remember_by_default`). If set to true, and the “Remember login between sessions” configuration option is enabled, the user’s login status will be remembered between sessions for the configured amount of time.

See the [API Docs](/docs/api/anvil.users) for full argument lists.

## [Email + password](#email--password)

### Login

To log in manually with an email and password, call `anvil.users.login_with_email()`, passing the email address and password as arguments. This function returns the newly-logged-in user, or raises an `AuthenticationFailed` exception if the login failed.

```python
user = anvil.users.login_with_email("abc@example.com",
                                    "<password>")
```

This function can be called from client or server code.

If `Require 2-factor authentication` is enabled in the Users Service, calling `anvil.users.login_with_email()` will require an additional argument for the Two-Factor Authentication details.

An `MFARequired` exception will be raised if Two-Factor Authentication is not passed or is invalid. See the [Two-Factor Authentication section](/docs/users/logging_in_using_code#log-in-with-two-factor-authentication) for more information.

### Password reset

To reset a user’s password, call `anvil.users.send_password_reset_email()`. If the specified email address is in the Users table, Anvil will send them an email with a link where they can set a new password for their account.

```python
anvil.users.send_password_reset_email("abc@example.com")
```

This function can be called from client or server code.

### Sign up

To register a new account with an email and password, call `anvil.users.signup_with_email()`. If signup succeeds, this function returns the newly-created user object. The new user will also be logged in if email confirmation is *not* required, and new-user registrations are automatically enabled.

```python
anvil.users.signup_with_email("abc@example.com",
                              "<password>")
```

This function can be called from client or server code, if the “allow signups” option is enabled in the Users Service configuration. Otherwise, it can only be called from server code.

## [Log in with Google (etc.)](#log-in-with-google-etc)

You can run separate login functions for [Google](../integrations/google), [Facebook](../integrations/facebook) and [Microsoft](../integrations/microsoft) accounts. Let’s discuss Google login, you just need to replace the word `google` with `facebook` or `microsoft` for the other two services.

To log in with Google, call `anvil.users.login_with_google()`. This function will prompt the user to log into Google, then attempt to authenticate that user with the Users Service. It will return a user object, or `None` if the Google login is cancelled, or raise an `AuthenticationFailed` exception.

```python
user = anvil.users.login_with_google()
```

This function must be called from client code (e.g. an event handler on a Form).

To sign up a new user with Google, call `anvil.users.signup_with_google()`. This will prompt the user to log into Google, then attempt to register this user with the Users Service. It will return a user object, or `None` if the Google login is cancelled, or raise a `UserExists` exception. If signup succeeds, the user is automatically logged in.

```python
anvil.users.signup_with_google()
```

This function must be called from client code (e.g. an event handler on a Form).

The [Google Service](/docs/integrations/google) must be enabled for Google authentication to work. It will be added to your app automatically when you tick Google as an authentication option in the Users Service.

For Facebook and Microsoft login, you need to register your Anvil App with their online developer console - see [Connecting Facebook to Anvil](../integrations/facebook/linking-facebook-and-anvil) and [Connecting Microsoft Azure to Anvil](../integrations/microsoft/linking-azure-and-anvil) for step-by-step instructions.

## [Log in with Two-Factor Authentication](#log-in-with-two-factor-authentication)

If `Require 2-factor authentication` is enabled in the Users Service, logging in with code will require a second factor of authentication.

There are two paths you can take to collect and verify a user’s second factor of authentication. The first, is by using the standard Two-Factor Authentication login form by calling `mfa_login_with_form()`. The second, is to implement 2nd factor authentication yourself by calling the underlying API functions, detailed below.

### Two-Factor Authentication login form

To log in manually while using Two-Factor Authentication, you need to call `anvil.users.mfa.mfa_login_with_form()` passing it the user’s `email` and `password`.

```python
# create the mfa dict
mfa_return = anvil.users.mfa.mfa_login_with_form("abc@example.com", "<password>")
```

This will present the standard Two-Factor Authentication login alert. The alert gives the user three options: submit their second factor credentials, request to reset their credentials via email (if enabled in the Users Service) and cancel.

Depending on the user’s selection, the function `mfa_login_with_form()` returns:

-   A multi-factor authentication (mfa) `dictionary object`, if the user successfully enters their second factor credentials.
-   `None`, if the user cancels.
-   `"reset_mfa"`, if the user requests to reset their credentials.

For more details on Two-Factor Authentication options, please visit the [Two-Factor Authentication documentation](/docs/users/two_factor_authentication).

Here is an example of how you could handle the return of `mfa_login_with_form()` as part of a manual login process:

```python
if mfa_return == 'reset_mfa':
  # If the user selects the reset option, email them with a 2 factor authentication reset link
  anvil.users.mfa.send_mfa_reset_email("abc@example.com")
elif mfa_return == None:
  # If the user selects cancel on the second authentication login screen
  pass
else:
  # If the user provides their two factor auth details, pass the mfa object to the login function
  user = anvil.users.login_with_email("abc@example.com", "<password>", mfa=mfa_return)
```

Once Two-Factor Authentication is completed, the object returned by `mfa_login_with_form()` can then be passed as the `mfa` argument to `anvil.users.login_with_email()`. If the details for both factors of authentication are correct, the function will return the newly-logged-in user, or raise an `AuthenticationFailed` exception if the login failed.

### Implement Two-Factor Authentication yourself

If you want to create your own second factor authentication form or process, there are a number of functions you can use. Each function available is documented below.

#### Get available Two-Factor Authentication type for user

Each user has details of what Two-Factor Authentication types are available to them. To find out, we can call `anvil.users.mfa.get_available_mfa_types()` passing the user’s `email` and `password` as arguments.

```python
# Passing email and password of a user will return their available mfa types
anvil.users.mfa.get_available_mfa_types("abc@example.com", "<password>")
```

This will return a list of strings representing this user’s registered Two-Factor Authentication types, for example: `['totp', 'fido']`.

#### Get TOTP login

If you want to use TOTP login, collect the 6-digit code from the user’s authentication app and pass it to `anvil.users.mfa.get_totp_mfa_login()`. This will return an MFA Login object you can pass to `login_with_email()`.

```python
# Get the TOTP mfa
mfa_return = anvil.users.mfa.get_totp_mfa_login(012345)
# Log in the user with the MFA login object
user = anvil.users.login_with_email("abc@example.com", "<password>", mfa=mfa_return)
```

If the details for both factors of authentication are correct, `login_with_email()` will return the newly-logged-in user, or raise an `AuthenticationFailed` exception if the login failed.

#### Get FIDO login

Before collecting the details for the FIDO login, you should check whether FIDO is available in the current environment. This can be done by calling `anvil.users.mfa.webauthn.is_webauthn_available()` which returns `false` if FIDO is unavailable, for example the application is in an `iframe` or unsupported browser.

```python
# Checking FIDO is available in the apps environment
anvil.users.mfa.webauthn.is_webauthn_available()
```

Once you have checked the environment, you can authorise the user with FIDO login. Collect the user’s email and password and pass them to `anvil.users.mfa.get_fido_mfa_login()`. If successful, `get_fido_mfa_login()` returns an MFA Login object you can pass to `login_with_email()`.

```python
# Get the TOTP mfa
mfa_return = anvil.users.mfa.get_fido_mfa_login("abc@example.com", "<password>")
# Log in the user with the MFA login object
user = anvil.users.login_with_email("abc@example.com", "<password>", mfa=mfa_return)
```

If the details for both factors of authentication are correct, `login_with_email()` will return the newly-logged-in user, or raise an `AuthenticationFailed` exception if the login failed.

## [Sign up for Two-Factor Authentication](#sign-up-for-two-factor-authentication)

There are two paths you can take to collect and verify a user signing up for second factor authentication. The first is by using the standard Two-Factor Authentication sign-up form by calling `configure_mfa_with_form()`. The second is to implement a 2nd factor sign up method by calling the underlying API functions.

### Two-Factor Authentication sign-up form

To use the standard Two-Factor Authentication sign-up form you can simply call `configure_mfa_with_form()`. The function takes one optional argument of `allow_cancel` which displays a `cancel` button if set to `True`, by default `allow_cancel` is set to False.

The standard Two-Factor Authentication sign-up form gives the user everything they need to set up their second factor of authentication and record it against their account.

### Implement Two-Factor sign up yourself

To implement your own custom Two-Factor sign up or recovery process, you can use a number of underlying API functions.

When registering a new second factor of authentication for a user, you can either generate a TOTP or FIDO method record. Both of these create a second factor authentication method that can then be added to a user’s account.

#### Create a TOTP login method

Calling `anvil.users.mfa.generate_totp_secret()` and passing the user’s email as an argument creates a dictionary object that can be used to create your second factor authentication form.

```python
# Generate TOTP secret
totp_secret = anvil.users.mfa.generate_totp_secret("abc@example.com")
```

An example of the `TOTP secret dictionary` object is:

```python
{
  'secret': "<secret>",
  'qr_code': <anvil.Media object>,
  'mfa_method': {'type': 'totp', 'id': "<id>", 'serial': "<serial>", 'secret': "<encrypted secret>"}
}
```

The `mfa_method` can then be added to the user’s record using `add_mfa_method()`, using the arguments `password`, `method` and `clear_existing` which defaults to `False`.

```python
anvil.users.mfa.add_mfa_method("<password>", totp_secret['mfa_method'], True)
```

For more information on `add_mfa_method()`, please see the [add Two-Factor Authentication method](#add-two-factor-authentication-method) section below.

The `qr_code` can be displayed using an [image component](/docs/client/components/basic#image) and scanned by the user’s authenticator application. Once scanned, the user’s authenticator app will start displaying the 6-digit code required to verify their second factor authentication.

See the [**Log in with Two-factor Authentication - Get TOTP login**](#get-totp-login) section of this document for how to validate the code while logging the user in. To validate the code without logging the user in, see the [**Validate TOTP login method**](#validate-totp-login-method) section below.

#### Validate TOTP login method

To validate the TOTP code provided by the user without logging them in, you can use `anvil.users.mfa.validate_totp_code()`. This takes the arguments `mfa_method`, which is provided in the dict returned from `generate_totp_secret`, and `code` which the user will provide by using their authenticator app, for example [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en&ref_topic=2954345). You should use this method to verify that the user has configured their authenticator app correctly during signup.

```python
# Validate the TOTP code against the user's MFA method
is_valid = anvil.users.mfa.validate_totp_code(totp_secret['mfa_method'], "<code>")
```

#### Create a FIDO login method

Calling `anvil.users.mfa.create_fido_mfa_method()` and passing the user’s email as an argument creates an MFA method object. The function should be called as part of the signup process.

```python
# Checking FIDO is available in the apps environment
if anvil.users.mfa.webauthn.is_webauthn_available():
  # Create FIDO method
  fido_method = anvil.users.mfa.create_fido_mfa_method("abc@example.com")
```

The `mfa_method` can then be added to the user’s account using `add_mfa_method()`, using the arguments `password`, `method` and `clear_existing` which defaults to `False`.

```python
anvil.users.mfa.add_mfa_method("<password>", fido_method, True)
```

For more information on `add_mfa_method()`, please see the [add Two-Factor Authentication method section](#add-two-factor-authentication-method) below.

#### Add Two-Factor Authentication method

To register a Two-Factor Authentication method to a user’s account, call `anvil.users.mfa.add_mfa_method()` with the arguments `password`, `mfa_method` and optionally `clear_existing` which defaults to `False`. If `clear_existing` is `True`, all existing Two-Factor Authentication methods will be removed from the User record and replaced with the provided one.

```python
anvil.users.mfa.add_mfa_method("<password>", mfa_method, True)
```

## [Handling exceptions](#handling-exceptions)

If any of these functions fails, it will raise an `anvil.users.AuthenticationFailed` exception. There are a few subclasses if you wish to handle them separately:

-   `anvil.users.UserExists` - You have attempted to sign up with an email address which is already in the Users table.
-   `anvil.users.EmailNotConfirmed` - You have attempted to log in with an email address that has not yet been confirmed. (Only occurs with Email + password login, when email confirmation is enabled)
-   `anvil.users.AccountIsNotEnabled` - This account is disabled (the `enabled` box is not ticked in the Users table). This happens if an administrator has manually disabled an account, or if the Users Service is configured not to enable newly-registered accounts.
-   `anvil.users.MFARequired` - You have attempted to log in by calling `anvil.users.login_with_email()` without providing the `mfa` argument for the second factor of authentication.
-   `anvil.users.TooManyPasswordFailures` - You have attempted to log in for the 10th consecutive time with an incorrect password. The user must reset their password via email.
-   `anvil.users.AuthenticationFailed` - This is the parent class of all these exceptions. It indicates that authentication has failed for some reason.

Here’s an example of how you can handle one of these exceptions in client code:

```python
import anvil.users

def login(self, **event_args):
try:
    anvil.users.login_with_email("example@email.com", "<incorrect_password>")
except anvil.users.TooManyPasswordFailures as e:
    # Do something in response to the exception
    print(e.message)
```

## [Build your own authentication flow](#build-your-own-authentication-flow)

You can implement your own login mechanism. To log a user in, pass a row from the Users table into `anvil.users.force_login()` in server code. `anvil.users.force_login()` returns the now-logged-in user. Passing `None` is the equivalent of `anvil.users.logout()`, and will return `None`.

This example shows a simple implementation of username/password login. (This is approximately the logic used by `anvil.users.login_with_email()`.)

```python
import bcrypt

@anvil.server.callable
def login_with_password(username, password):
  user = app_tables.users.get(email=username)
  if (user is not None) and \
       bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
    anvil.users.force_login(user)
    return user
  else:
    return None
```
