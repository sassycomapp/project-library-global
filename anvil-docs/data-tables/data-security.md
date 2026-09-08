---
title: "Data Security"
url: "/docs/data-tables/data-security"
---


# [Data Security with Data Tables](#data-security-with-data-tables)

**Data in Data Tables is encrypted at rest.** This page is a guide to prevent you from accidentally disclosing data to app users.

Code for Forms executes in the user’s browser, also called the client, which means the code is under the user’s control. A determined attacker can access anything that your Forms are allowed to access. So you can restrict access to each Data Table.

By default, client-side code is not given any access to your Data Tables. You can instead access the data by writing [Server Modules](/docs/server) that pass the data back to your Forms. You can also expose [views](#views) to give your client-side Forms permissions on limited sets of data from your Data Tables.

## [Permissions](#permissions)

Server Modules are *not* under the user’s control. So you can trust them, eg, not to return table data to unauthorised users.

You can return table rows (or `search()` results) from Server Module functions. The (client-side) Form code will be able to read them, but not update them. If you pass a row object into a server function, the Server Module can update it.

### Relaxing permissions

You may want to relax these restrictions. For example, if your app is a blog, it’s OK for every visitor to be able to view your blog posts (but not edit them). Or if you will only send the Share link to a small group of co-workers, it’s OK that they can all edit your data.

You can choose from three levels of permission, for either Forms or Server Modules:

**No access**  
Your code will not be able to search, update, or edit the table. If it gets a row from this table (eg returned from a server function), it can read that row and any linked rows. But it cannot update or delete that row.

**Can search table**  
Your code can call `search()` and `get()` on this table, and read all the data in its rows (and linked rows). However, it cannot add new rows, or update or delete existing rows.

**Can search, edit and delete**  
Your code can perform any operation on this table.

### More notes on permissions

-   You can also restrict what Server Modules can do. For example, you can make the table read-only for your app by making sure even Server Modules can’t write to the table.
-   [Server Uplink](/docs/uplink) code can do everything that Server Modules can. This includes accessing and updating tables.

## [Views](#views)

[Tutorial: Multi-User Apps with Data Tables](/blog/advanced-data-storage)

If you don’t want to give every visitor access to a Data Table, you’ll want to use [Server Modules](/docs/server) to control access to them. Server Modules can return **views** on a Data Table to client code, with extra permissions or restrictions.

Data Tables have three view methods, which offer the client code different levels of access:

-   `client_readable()` allows the client to read this table, and any rows linked to from this table.
-   `client_writable()` allows the client to update rows in this table, and add new rows. Client code can also read any linked rows.
-   `client_writable_cascade()` allows the client to write to this table, and update any rows linked to in this table.

It is almost always more convenient and secure to use [client-writable model classes](model-classes) rather than client-writable views.

A table view is just like a table - you can call `search()`, `add_row()`, and so on on it.

This server function returns a `client_writable` view on this table, but only for authorised users.

```python
@anvil.server.callable
def get_data():
  if user_is_authorised():
    return app_tables.my_table.client_writable()
```

This pattern can be used to implement simple applications where all users must log in, but any logged-in user may access all the data in a table.

View methods can also take keyword parameters, just like the `search()` function. This returns a **restricted view**, that only contains matching rows. In this case, we use [Google authentication](/docs/integrations/google/authenticating-users) to return a view that can only access rows whose `owner` column matches the email address of the current logged-in user. (If no user is logged in, it returns `None`.)

```python
@anvil.server.callable
def get_data_for_logged_in_user():
  email = anvil.google.auth.get_user_email()
  if email is not None:
    return app_tables.my_table.client_writable(owner=email)
```

If you call `add_row` on a restricted view, the fixed columns (`owner` in this example) are filled in automatically. If you attempt to specify a fixed column in `add_row()`, the request will fail.

In this example, this means that any row a user adds to this table will always have their email address attached to it.

```python
my_data = anvil.server.call('get_data_for_logged_in_user')

# This adds a row with columns X and Y 
# and adds my email address to the 'owner' column
my_data.add_row(X=4, Y="F")

# This raises an error, because the 'owner'
# column is fixed by the view, and we cannot
# override it.
my_data.add_row(owner="bob@example.com",
                X=5, Y="Hello!")
```

Fixed columns are not accessible in code. This means that the client does not gain read or write access to rows referenced in a fixed column.

```python
# This also raises an error, because fixed
# columns are not accessible from code:
for row in my_data.search():
  # Raises an error:
  print(row['owner'])
```

Columns cannot be automatically added to a restricted view.

## [Client-Hidden Columns](#client-hidden-columns)

When you return a row from a Server Module to the client, all columns in that row are included by default. Client-hidden columns allow you to specify which columns are visible to the client and which should not be, providing column-level access control. This ensures sensitive fields never reach the client, whether rows are returned from a Server Module or fetched directly by the client.

Client-hidden columns are not simply hidden from display; the data is removed before it ever reaches the client. A client requesting a view or row from a Data Table will never receive data from client-hidden columns. This enables you to enforce clear security boundaries.

If you are using [Model Classes](/docs/data-tables/model-classes), this can cause issues if you are attempting to access a client-hidden column or attribute while running on the client. You should make sure model classes only attempt to access client-hidden columns while on the server.

Click the icon next to a column name to toggle its client visibility.

All columns are client-visible by default, except in the [Users table](/docs/users/the-users-table), where only the email column is client-visible.

When a column is client-hidden:

-   Rows returned from Server Modules to the client will not include that column’s data, while the same row accessed in the Server Module code will include it.
-   Client code cannot access this column, regardless of the [table’s permissions](/docs/data-tables/data-security#relaxing-permissions).
-   [Views](#views) returned to the client exclude client-hidden columns.
