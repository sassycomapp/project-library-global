---
document: "Checks and Validation"
title: "Checks and Validation"
url: "/docs/data-tables/model-classes/validation"
doc-id: validation
state: Live
date-created: 2026-09-08
---


# [Checks and Validation](#checks-and-validation)

When defining the data structure for your application, it is common to want to define rules about your data and what happens when it changes. These include:

-   **Validation,** e.g. “This column must be a number between 1 and 10”

-   **Permissions,** e.g. “Only administrators may change the value of this column”

-   **Side effects,** e.g. “Every time we update a row from this table, we set its `last_updated` column to the current time”

Model classes allow you to express these constraints in code.

## [Low-level API](#low-level-api)

Anvil curently only supports this low-level validation API. We intend to release a higher-level API to reduce code duplication, once we have gathered feedback from how people are using models in practice.

A model class may override the methods `_do_update()`, `_do_delete()` and/or `_do_create()` to intercept updates, deletion and [draft creation](../buffering#drafts). To complete the action, call the superclass method.

### `_do_update()`

The `_do_update()` method is called when column values are updated by assigning to a column, calling the `update()` method, or saving [buffered changes](../buffering) to a row.

It takes two positional arguments:

1.  `updates`: A dictionary of column names to new values, representing the requested changes

2.  `from_client`: A boolean value, true if the request was initiated by the client. (This is useful when creating [client-writable models](client-writable), in which case `_do_update()` will run on the server even if the change was initiated by client code.)

### `_do_delete()`

The `_do_delete()` method is called when row deletion is requested with the `delete()` method. It takes one positional argument:

1.  `from_client`: A boolean value, true if the request was initiated from the client.

### `_do_create()`

The `_do_create()` class method is called when [saving a draft row](../buffering#drafts). It takes two positional arguments:

1.  `values`: A dictionary of column names to values representing the requested changes

2.  `from_client`: A boolean value, true if the request was initiated from the client.

**Note:** `_do_create()` should be a `@classmethod`, as it does not refer to an existing instance.

## [Example](#example)

This code extends the [previous example](creating#example) to add validation, add permission checks and automatically update the `last_created` column with the current time whenever the row is changed:

```python
class TodoItem(app_tables.todos.Row):
  def _do_delete(self, from_client):
    me = anvil.users.get_user()
    if not me:
      raise Exception("Must be logged in to delete records")
    if self["assigned_user"] != me:
      raise Exception("Only the assigned user can delete a record")
    super()._do_delete(from_client)

  def _do_update(self, updates, from_client):
    me = anvil.users.get_user()
    if me is None:
      raise Exception("Must be logged in to edit records")
    if self["assigned_user"] != me:
      raise Exception("Must be the owner of this item to update it")
    if "title" in updates and not update["titles"]:
      raise Exception("Must specify a title")

    updates['last_updated'] = datetime.now()

    super()._do_update(updates, from_client)

  @classmethod
  def _do_create(cls, values, from_client):
    me = anvil.users.get_user()
    if me is None:
      raise Exception("Must be logged in to do this")
    if not values.get("title", ""):
      raise Exception("Must specify a title")

    values["assigned_user"] = me
    values['last_updated'] = datetime.now()

    return super()._do_create(values, from_client)
```
