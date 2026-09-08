---
title: "Managing Users"
url: "/docs/users"
---


# [Managing Users](#managing-users)

The Users Service handles signup, login and user permissions, and provides a range of functionality to make user management easy and flexible. See the [Quickstart for logins](users/quickstart-login) and the [Quickstart for permissions](users/quickstart-permissions) to get up and running quickly.

To add the Users Service to your app, click the blue plus button in the [Sidebar Menu](/docs/editor#sidebar-menu). Then select the Users service.

## [Get a login form in one line](#get-a-login-form-in-one-line)

You can present a signup/login form with a single line of code. This handles signup, login, email verification, password reset and ‘remember me’. See [Presenting a Login Form](users/presenting-a-login-form) for details.

## [Building the process yourself](#building-the-process-yourself)

If you want to build your own login form or customise your signup/login workflow, see our [how-to guide](/blog/custom-user-auth).

There are also a number of functions such as `anvil.users.logout()` that let you run the steps of the user management process manually. See [Logging in Using Code](users/logging_in_using_code) or the [API Reference](/docs/api/anvil.users) to learn what functions are available.

## [Authentication Options](#authentication-options)

In addition to username and password, you can allow your users to log in with their existing Google, Facebook or Microsoft accounts. Anvil also has built-in local Active Directory (AD) and PKI Certificate systems for Enterprise users, and supports SAML Authentication. See [Authentication Choices](users/authentication_choices) for more information.

Anvil’s Users Service also comes with Two-Factor Authentication. See [Two-Factor Authentication](users/two_factor_authentication) for more detail.

## [How user information is stored](#how-user-information-is-stored)

If you’re using the Users Service, user accounts are stored in a [Data Table](/docs/data-tables) called ‘Users’. The password is `bcrypt` hashed for you and the rest of the relevant user details are processed and added to the ‘Users’ Data Table. See [the Users Table](users/the_users_table) for more information.

You can add your own columns to this Data Table - it’s common to add a `role` column to store user roles for permissions management.

## [Checking user permissions](#checking-user-permissions)

You can get the currently logged-in user using `anvil.users.get_user()`. This returns a row from the Users table.

This allows you to set up Python code in your Server Modules that checks usernames or roles before running particular code or returning particular data. This is Anvil’s authorisation model. See [User Permissions](users/permissions) for more detail.
