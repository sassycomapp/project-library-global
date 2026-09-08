---
title: "Portable Classes"
url: "/docs/other-concepts/portable-classes"
---


# [Writing Portable Classes](#writing-portable-classes)

By default, Anvil already knows how to pass [many basic Python objects](/docs/server#valid-arguments-and-return-values) between client and server code. But if you want to pass more complicated objects, you can define your own classes that can be passed from server to client code. We call these **portable classes**.

To make a class portable, you can decorate it with `anvil.server.portable_class`. You can then use instances of this class as arguments to (or return values from) Server Functions.

If you want a class to be portable, it needs to follow two main rules:

First, the class definition needs to be accessible to both client and server code, so it should go in an Anvil [Module](/docs/client/python/modules) (**not** a Server Module). Here’s an example:

```python
# In a module called, say, 'my_classes'...
import anvil.server

@anvil.server.portable_class
class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name
```

Now we can return an instance of the `Person` class from a server function, and it will arrive fully-formed on the client:

```python
# In a Server Module...
from my_classes import Person

@anvil.server.callable
def get_person():
    # Look up the person - in a database, perhaps.
    return Person("John", "Smith")
```

```python
# Then, on the client...

p = anvil.server.call("get_person")
print(p.get_full_name()) # --> John Smith
```

Notice that the object returned from the server was a full instance of the Person class. Anvil took care of serialising all the object’s attributes, transmitting it, and deserialising it when it arrived. Of course, this works the other way too - you can pass instances of portable classes as arguments to Server Functions too.

Secondly, for a class to serialise correctly, all its attributes need to be values that Anvil can serialise - including instances of other portable classes! You must also avoid *circular references* - ie if object A refers to object B, then object B can’t contain a reference to object A.

When you pass a portable object between client and server, it is *copied*. So, for example, if you pass a Person instance to a server function that returns its argument, the return value from the `anvil.server.call()` is a new instance.

(The same goes for your class’s attributes: For example, if you have two attributes referring to the same `dict` object, they will deserialise to two separate objects at the other end. If you need more precise control over serialisation, you can [customise how your class is serialised](portable-classes/custom-serialisation).)

## [Using portable classes via Uplink](#using-portable-classes-via-uplink)

In order for uplink code to serialise and deserialise a portable class, the class should be registered with the same unique name in both your app code and in your uplink code. By default the `anvil.server.portable_class` decorator registers a portable class based on its module and name. To register a portable class with a unique name, pass the name to the decorator.

```python
# use a unique name to register this class

@anvil.server.portable_class('_Person')
class Person():
    def __init__(self, first_name, last_name):
        ...
```

## [More powerful control](#more-powerful-control)

You can customise your portable classes for efficiency, or to enforce permissions:

### [Custom Serialisation](portable-classes/custom-serialisation)

By default, Anvil transmits all of a portable object’s attributes. By implementing the `__serialize__` and `__deserialize__` methods, you can control precisely how your data is transmitted.

### [Capabilities](portable-classes/capabilities)

Client code is untrusted - a malicious user can make their browser do anything! Sometimes, you want your objects to have unforgeable identities, so that clients can only perform operations if the server code has given them permission. Anvil’s Capability objects make this easy.

### [Capability-scoped cache updates](portable-classes/capability-scoped-cache-updates)

The portable objects you pass to the client might represent some long-lived underlying object in your app’s data model. To avoid round-trips, you might want to pass some information around with that object so it can be accessed quickly from client code – in other words, cached data. But when you call a server function to update that object, you want to update the client side cache too. And to avoid data leaks, you need to send updates only if this is an object the client already knows about. Anvil includes a mechanism for secure capability-scoped cache updates to make this easy.
