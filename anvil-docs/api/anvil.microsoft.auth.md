---
title: "anvil.microsoft.auth"
url: "/docs/api/anvil.microsoft.auth"
---


## `anvil.microsoft.auth` Module

#### Functions

[`get_user_access_token`](#get_user_access_token) [`get_user_email`](#get_user_email) [`get_user_refresh_token`](#get_user_refresh_token) [`login`](#login) [`refresh_access_token`](#refresh_access_token)

## Functions

#### `get_user_access_token()`

Get the secret access token of the currently-logged-in Microsoft user, for use with the Microsoft REST API. Requires this app to have its own Microsoft client ID and secret.

---

#### `get_user_email()`

Get the email address of the currently-logged-in Microsoft user.

To log in with Microsoft, call anvil_microsoft.auth.login() from form code.

---

#### `get_user_refresh_token()`

Get the secret refresh token of the currently-logged-in Microsoft user, for use with the Microsoft REST API. Requires this app to have its own Microsoft client ID and secret.

---

#### `login()`

Prompt the user to log in with their Microsoft account

---

#### `refresh_access_token(refresh_token)`

Get a new access token from a refresh token you have saved, for use with the Microsoft REST API. Requires this app to have its own Microsoft client ID and secret.
