---
title: "anvil.saml.auth"
url: "/docs/api/anvil.saml.auth"
doc-id: anvil.saml.auth
state: Live
date-created: 2026-09-08
---


## `anvil.saml.auth` Module

#### Functions

[`get_user_attributes`](#get_user_attributes) [`get_user_email`](#get_user_email) [`login`](#login)

## Functions

#### `get_user_attributes()`

Get the user attributes of the currently-logged-in SAML user.

The exact attributes available will depend on your SAML Identity Provider.

---

#### `get_user_email()`

Get the email address of the currently-logged-in SAML user.

To log in with SAML, call anvil.saml.auth.login() from form code.

---

#### `login()`

Prompt the user to log in via SAML
