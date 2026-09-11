---
document: "anvil.google.auth"
title: "anvil.google.auth"
url: "/docs/api/anvil.google.auth"
doc-id: anvil.google.auth
state: Live
date-created: 2026-09-08
---


## `anvil.google.auth` Module

#### Functions

[`get_user_access_token`](#get_user_access_token) [`get_user_email`](#get_user_email) [`get_user_refresh_token`](#get_user_refresh_token) [`login`](#login) [`refresh_access_token`](#refresh_access_token)

## Functions

#### `get_user_access_token()`

Get the secret access token of the currently-logged-in Google user, for use with the Google REST API. Requires this app to have its own Google client ID and secret.

---

#### `get_user_email()`

Get the email address of the currently-logged-in Google user.

To log in with Google, call anvil.google.auth.login() from form code.

---

#### `get_user_refresh_token()`

Get the secret refresh token of the currently-logged-in Google user, for use with the Google REST API. Requires this app to have its own Google client ID and secret.

---

#### `login([additional_scopes])`

Prompt the user to log in with their Google account.

If you have specified your own client ID in the Google Service configuration, you can specify additional OAuth scopes for use with the Google REST API.

---

#### `refresh_access_token(refresh_token)`

Get a new access token from a refresh token you have saved, for use with the Google REST API. Requires this app to have its own Google client ID and secret.
