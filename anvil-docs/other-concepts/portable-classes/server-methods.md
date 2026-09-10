---
title: "Server Methods"
url: "/docs/other-concepts/portable-classes/server-methods"
doc-id: server-methods
state: Live
date-created: 2026-09-08
---


# [Server-side methods](#server-side-methods)

Sometimes you might want to define a method on the client but have it run on the server. You can do this with the `@anvil.server.server_method` decorator.

For example, the following code defines a `Person` class that has a method to check whether or not the person is in a Data Table. When that method is called, the Portable Class is sent to the server and the server method is called there.

```python
import anvil.server

@anvil.server.portable_class
class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @anvil.server.server_method
    def is_in_database(self):
      return bool(app_tables.people.get(first_name=self.first_name, last_name=self.last_name))

```

Using `@anvil.server.server_method` is the equivalent of defining the method on the server and using `anvil.server.call` on the client:

```python
def is_in_database(self):
  return anvil.server.call('check_database', self.first_name, self.last_name)
```

```python
@anvil.server.callable
def check_database(first_name, last_name):
  return bool(app_tables.people.get(first_name=self.first_name, last_name=self.last_name))
```

## [Using server methods securely](#using-server-methods-securely)

You can only call a server method on an instance of your Portable Class, but the contents of your class are generally untrusted just like the arguments to an `anvil.server.call()` call. You should only rely on trusted information, for example, code from the server or [Capabilities](/docs/server/portable-classes/capabilities).
