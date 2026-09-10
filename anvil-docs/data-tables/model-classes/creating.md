---
title: "Creating Model Classes"
url: "/docs/data-tables/model-classes/creating"
doc-id: creating
state: Live
date-created: 2026-09-08
---


# [Creating Model Classes](#creating-model-classes)

[Model classes](/docs/data-tables/model-classes) allow you to extend the [Data Table Row class](/docs/data-tables/data-tables-in-code#row-objects) for a particular table.

To specify the model class to use for a particular Data Table:

1.  Create a [Module](/docs/client/modules) in your app to hold code that can be imported on both client and server

2.  In that Module, define a class that inherits from `app_tables.[tablename].Row` (substituting `[tablename]` with the table for which you are defining a model).

3.  Import that Module when your app starts up (eg from a startup Form) and from one of your Server Modules if you have them

Now every time your code interacts with that Data Table, you will receive instances of your model class instead of ordinary [Row objects](/docs/data-tables/data-tables-in-code#row-objects). Because the model class inherits from the Row class, it still supports the normal [Data Tables Row API](/docs/data-tables/data-tables-in-code), so existing code that worked with rows from this table will continue to work.

For example, here is a model class for a To Do List app that has a property to check whether or not the task is overdue:

```python
class TodoItem(app_tables.todo_items.Row):
  @property
  def is_overdue(self):
    return datetime.now() > self["due_date"]
```

## [Options](#options)

You can specify additional options when inheriting from a row class:

-   `buffered=True`: Automatically [buffer changes](../buffering) to rows in this table, without having to call the `buffer_changes()` method on each object.

-   `attrs=True`: Allow access to column values as attributes on the object as well as by dictionary lookup (eg `row.due_date` as well as `row["due_date"]`).

-   `client_updatable=True`, `client_creatable=True`, `client_deletable=True`, `client_writable=True`: See [Client-Writable Models](client-writable).

## [Model classes and the server](#model-classes-and-the-server)

Defining a model class in a Module means that your class can be imported both on the client and the server. However, sometimes you’ll want to define methods that can only run on the server or write code that is not visible to the client.

### Server methods

If you want to write methods for your model class that will run on the server, you can use the [`@anvil.server.server_method` decorator](/docs/server/portable-classes/server-methods). Methods with this decorator are callable on the client but are passed to the server to run. When server methods are defined in a Client Module, the method is still visible to the client even though it will never run there.

```python
import anvil.server

class TodoItem(app_tables.todo_items.Row, buffered=True):

  @anvil.server.server_method
  def assign_to_on_call_user(self):
    on_call_user = app_table.users.get(on_call=True)[0]
    self["assigned_user"] = on_call_user
```

### `self` is trustworthy

You cannot set instance variables on a model. The only state allowed in a model is the values of the Data Table columns. Because of this, if you define server methods to perform privileged actions, `self` is always trustworthy despite being passed from the client: it is guaranteed to be a row from the table corresponding to this model with every property derived directly from the database. (However, the other arguments to a server method come from [untrusted client code](https://anvil.works/articles/client-vs-server), so should be treated with care.)

## [Server versions of models](#server-versions-of-models)

Module code is visible on the client, so even though server methods run on the server, their code is visible to the client. If you want to create server methods with private implementations, you can define a server version of your model.

In a Server Module, create a class that inherits from your model class. Rows accessed on the server will now be instantiated as the server-side class, and rows accessed on the client will be the client-side class. Objects will be automatically converted between client-side and server-side versions when they are passed into or out of server code.

Now, in the client-side model, you can define a “stub” `@server_method` that does nothing, and override it in the server-side model. The client will see only the stub method, but when it is called the server-side version will be executed.

### Override behavior

When you have both client and server versions of a model class, Anvil provides some helpful automatic behavior:

1.  **Instance Creation**: When you instantiate the client model class (e.g., `TodoItem()`) on the server, you actually get a draft instance of the server class. This means any server-specific behavior is automatically available.

2.  **Server Method Overrides**: When you call a [`@server_method`](/docs/server/portable-classes/server-methods) decorated `@classmethod` on the client model class (e.g., `TodoItem.get_my_todos()`), if the server model has defined its own version of that method, the server model’s version will be executed. This makes it easy to write code that runs correctly on both client and server without needing to know which version of the model you’re working with.

These override behaviors mean you can write your client-side code to work with the client model class, and if a server version exists with additional functionality or different implementations, that will be used automatically.

```python
class TodoItem(app_tables.todo_items.Row, buffered=True):

  @anvil.server.server_method
  @classmethod
  def get_my_todos(cls):
    # The actual implementation is hidden from the client
    raise NotImplementedError
```

```python
from . import Module1

class TodoItem(Module1.TodoItem):
  @anvil.server.server_method(require_user=True)
  @classmethod
  def get_my_todos(cls):
    me = anvil.users.get_user()
    return app_tables.todos.search(assigned_user=me)
```

This functionality does not affect permissions: Just because server method code is visible to the client doesn’t mean that a malicious client can change the code that runs on the server. This feature is only useful for hiding implementation details from the client.

## [Example](#example)

Let’s put it all together in an example. We’re creating a To Do List application, which has a table called `app_tables.todo_items` with a column called `due_date`. We want to define a model class for it, so we create a Module and define the following class:

```python
from anvil.tables import app_tables
from datetime import datetime
from anvil.server import server_method



class TodoItem(app_tables.todo_items.Row, buffered=True):
  @property
  def is_overdue(self):
    return datetime.now() > self["due_date"]

  @server_method(require_user=True)
  def assign_to_on_call_user(self):
    on_call_user = app_tables.users.get(on_call=True)
    self["assigned_user"] = on_call_user
    self.save()

  @server_method
  @classmethod
  def get_my_todos(cls):
    # The actual implementation is hidden from the client
    raise NotImplementedError
```

We also create a Server Module, and define the following class:

```python
from . import Module1

class TodoItem(Module1.TodoItem):
  @server_method(require_user=True)
  @classmethod
  def get_my_todos(cls):
    me = anvil.users.get_user()
    return app_tables.todo_items.search(assigned_user=me)
```

Now, whenever we call `app_tables.todo_items.search()` we get a sequence of `TodoItem` instances (we’ll get the client-side version of `TodoItem` on the client, and the server-side version if we’re running on the server). We can access the `.is_overdue` property of these objects or call a server method with `row.assign_to_on_call_user()`. Changes to these objects are buffered by default.

There is also a server-side classmethod whose implementation is hidden from the client: `TodoItem.get_my_todos()`.
