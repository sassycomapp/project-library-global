---
title: "User Permissions"
url: "/docs/users/permissions"
doc-id: permissions
state: Live
date-created: 2026-09-08
---


# [User Permissions](#user-permissions)

User management consists of two aspects: **authentication** (checking who people are, login) and **authorisation** (deciding what they can do based on who they are).

Authorisation is quite simple in Anvil: you check the current user and use Python logic to allow or deny them access to data and functionality.

## [Checking who’s logged in](#checking-whos-logged-in)

You can get the current logged-in user with `anvil.users.get_user()`. Do this when they are about to do something for which they need to be authorised (e.g. access private data).

The `anvil.users.get_user()` function returns the [Data Table](/docs/data-tables) row from the Users table for the currently logged-in user. If no user is logged in, it returns `None`.

In this example, we check the user’s email address. If this is an authorised user, we give them access to some secret data (by returning a [client-readable view](/docs/data-tables/data-security#views) on a data table).

```python
@anvil.server.callable
def get_secret_data():
  user = anvil.users.get_user()

  if user['email'] == 'john.smith@example.com':
    return app_tables.secret_table.client_readable()
```

You can pass an optional keyword argument `allow_remembered` to `get_user()`, which is `True` by default. Setting this to `False` will prevent `get_user` from returning a User who logged in in a previous session and selected “Remember me”.

`anvil.users.get_user()` can be used from Server Modules and from client code. To be sure that the results are correct, you should call it from a Server Module. The user has ultimate control of anything running in their browser, but [the server environment is secure](../security).

Calling `anvil.users.get_user()` accesses the database if a cache miss occurs, so making the call from client code causes a spinner to be displayed. To suppress the spinner, run it in a `with anvil.server.no_loading_indicator` block.

## [User Roles](#user-roles)

You can easily set up user roles to define groups of users that have certain permissions. Just add a `role` column to your Users table.

Imagine you wanted to designate some users as `admin` users. You can put `'admin'` in the `role` column for those users, then check the `role` column when you’re deciding what access to give them:

```python
@anvil.server.callable
def get_secret_data():
  user = anvil.users.get_user()

  if user['role'] == 'admin':
    return app_tables.secret_table.client_readable()
```

You can combine user roles with [Data Tables views](../data-tables/data-security#views) to show only certain records depending on user roles. Just store a ‘role’ column on the table you want to restrict, and store which role can view each row. If it’s multiple roles, use a [Simple Object](../data-tables/data-tables-in-code#searching-simple-objects) with a list of roles.

```python
@anvil.server.callable
def get_secret_data():
  user = anvil.users.get_user()

  return app_tables.my_table.client_readable(role=user['role'])
```
