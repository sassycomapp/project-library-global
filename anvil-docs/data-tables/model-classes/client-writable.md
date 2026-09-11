---
document: "Client-Writable Models"
title: "Client-Writable Models"
url: "/docs/data-tables/model-classes/client-writable"
doc-id: client-writable
state: Live
date-created: 2026-09-08
---


# [Client-Writable Models](#client-writable-models)

It’s convenient to express all your UI logic in Forms, without having to create a server function corresponding to every action. However, this needs to be done securely: Forms are [untrusted client-side code](https://anvil.works/articles/client-vs-server), so we must perform server-side validation.

With client-writable models, client-code can update rows directly, create new rows, and delete existing rows. All of these operations go via the server, where [validation and permission checks](validation) can run in a trusted environment before the changes are applied to the database.

## [Making a model client-writable](#making-a-model-client-writable)

When creating a model class, you can add options to the superclass that allow instances of your model to be created, updated and/or deleted directly from Form code.

There are four different options:

-   `client_updatable=True`: client code can update rows directly
-   `client_creatable=True`: client code can create new rows
-   `client_deletable=True`: client code can delete existing rows
-   `client_writable=True`: equivalent to setting the three above options to `True`

If any of the above options are set to `True`, you’ll need to implement [permission checks](validation) to ensure that only permitted operations can occur. For example, if `client_updatable` is set to `True`, you’ll want to override `_do_update()` to check that the logged-in user has permission to edit this row before doing the update.

For example:

```python
class TodoItem(app_tables.todo_items.Row, client_updatable=True):

  def _do_update(self, updates, from_client):
    if from_client:
        me = anvil.users.get_user()
    if me is None:
        raise Exception("Must be logged in to edit records")
    if self["assigned_user"] != me:
        raise Exception("Must be the owner of this item to update it")

    updates['last_updated'] = datetime.now()

    super()._do_update(updates, from_client)
```

If you create a client-writable model, it is **very important** that you implement checks on every operation you permit. Otherwise, any untrusted visitor will be able to make arbitrary changes to your data.

**Do not** configure the table as client-writable in the Data Tables config page, and avoid using [`client_writable()` views](/docs/data-tables/data-security#views) when you have defined a client-writable model. This setting will allow untrusted client code to save changes directly to the database and will override any permission checks and may cause errors in the future.

## [How it works](#how-it-works)

When the `client_[X]able` option is set for a particular operation, it will cause that operation to be redirected to your server-side Python code. This will execute the corresponding `_do_[X]()` method on the server. If the default `_do_[X]()` function is called (eg via calling `super()._do_update()`), then the operation will be sent to the Anvil database and executed.

For example, if we have a row with a client-updatable model, and we update the `'name'` column to the value `'foo'`, the following operations might execute:

1.  Client-side code runs `row['name'] = 'foo'` to update the value of the `'name'` column.

2.  The update is sent to the app’s server code.

3.  In the app’s server side environment, the model’s `_do_update()` function on the model is called.

    -   The `updates` argument is the dictionary `{'name': 'foo'}`.
    -   The `from_client` argument is `True`.

4.  The model’s `_do_update()` function decides that this update is permitted, and calls `super()._do_update({'name': 'foo'}, True)`.

5.  The superclass `_do_update()` sends the update to the Anvil database.
