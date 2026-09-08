---
title: "Custom Serialisation"
url: "/docs/other-concepts/portable-classes/custom-serialisation"
---


# [Custom serialisation](#custom-serialisation)

The `@anvil.server.portable_class` decorator marks a class as portable. By default, Anvil transmits portable objects by extracting and transmitting the class’s `__dict__` – which is usually where the object’s data attributes live. This is fine so long as every attribute of your class is already [something Anvil knows how to transmit](/docs/server#valid-arguments-and-return-values), but if you want to do something more complex, you can decide how your class gets transmitted and reconstituted by implementing the `__serialize__` and `__deserialize__` methods:

```python
@anvil.server.portable_class
class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    # Customise how Person objects are transmitted - in this
    # case, to be more compact and save network bandwidth:
    def __serialize__(self, global_data):
        return [self.first_name, self.last_name]

    def __deserialize__(self, data, global_data):
        self.__init__(data[0], data[1])
```

### The `__serialize__` method

The `__serialize__` method is responsible for returning a representation of the contents of an object that Anvil can send. This value can contain [anything Anvil knows how to transmit](/docs/server#valid-arguments-and-return-values) – even other Portable Classes (as long as they don’t contain circular references)! The default `__serialize__` implementation just returns `self.__dict__`.

Besides `self`, the `__serialize__` method takes one argument - `global_data`. (See [Global Data](#global-data), below.)

### The `__deserialize__` method

The `__deserialize__` method receives a newly created, blank object (`self`) along with whatever was returned from `__serialize__`. Given this information, it is the responsiblity of `__deserialize__` to initialise `self` with all the necessary attributes. You might do this by calling `self.__init__` (as we do here), or by directly setting attributes on `self`.

By the time `__deserialize__` is called, `data` has been fully reconstructed (for example any Portable Classes have already been deserialised), so you can use this value directly. The default `__deserialize__` implementation just calls `self.__dict__.update(data)`.

Like `__serialize__`, the `__deserialize__` method also takes a `global_data` argument. (See [Global Data](#global-data), below.)

#### `__deserialize__` and `__init__`

The `__deserialize__` method receives a *blank* `self` object, without calling `__init__` first. You can think of `__deserialize__` as happening *instead of* `__init__`.

This means that, for example, client code can receive (from the server) objects that it cannot construct (because, for example `__init__` contains code that can only run on the server). For simple classes like this one, you can choose to call `__init__` from `__deserialize__`, but you don’t need to!

If you’re interested in what’s going on under the hood, the blank object is created by calling `YourClass.__new__()` with no arguments. For more control over object creation, you can instead implement the [`__new_deserialized__` method](#controlling-object-construction).

## [Global Data](#global-data)

The `__serialize__` and `__deserialize__` methods both take a `global_data` object as an argument. This is a `dict`-like object that will be transmitted along with this server call or return, and it is shared between *all* portable objects (of this type or any other type). If you expect to send many instances of your portable object at once, and these objects contain duplicate data, you can use `global_data` to significantly reduce the amount of data that needs to be transmitted.

Let’s extend our example: let’s imagine each `Person` has a unique `id`, and we expect our app to send around long lists (or other data structures) that might include the same person many times. In that case, we could avoid sending the `first_name` and `last_name` multiple times, by making use of the `global_data` object:

```python
@anvil.server.portable_class
class Person():

    def __init__(self, id, first_name, last_name):
        self.id = id # We have added the 'id' attribute
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __serialize__(self, global_data):
        # Store the name globally, keyed by 'id'.
        global_data[f"Person.{id}"] = [self.first_name, self.last_name]

        # Each individual instance now only needs to transmit 'id'
        return self.id

    def __deserialize__(self, id, global_data):
        # Retrieve the name from global data, based on our id
        [first_name, last_name] = global_data[f"Person.{id}"]
        self.__init__(id, first_name, last_name)
```

You can transmit almost any portable value in `global_data` – including other portable classes! **However**, when portable classes in `global_data` are transmitted, their `__serialize__` and `__deserialize__` methods will *not* have access to `global_data` (accessing the `global_data` object will raise a `RuntimeError`). This will likely only happen if you are writing a dependency and do not have control over the objects that get added to `global_data` i.e. it’s an advanced consideration. To ensure you have access to `global_data` you can check whether the object is truthy or falsey. A truthy `global_data` object is safe to use, a falsey `global_data` object will raise a `RuntimeError` when accessed.

If your `__serialize__` implementation stores portable objects in `global_data`, make sure only to store objects that do not themselves require `global_data`. (This can be because they don’t define a custom `__serialize__` method, or because their `__serialize__` method works OK when its `global_data` parameter is `None`.)

## [Controlling Object Construction](#controlling-object-construction)

If you want more control over the object instance created by deserialisation, you can implement a static method called `__new_deserialized__` (instead of `__deserialized__`).

This method is a *static constructor* - it does not receive a pre-created instance of the portable class. Instead, it receives only the per-instance and global data, and returns the instantiated object. This allows you to control object creation more precisely (for example, to re-use the same object for multiple deserialisation calls).

Here is an example:

```python
@anvil.server.portable_class
class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __serialize__(self, global_data):
        return [self.first_name, self.last_name]

    # Implement __new_deserialized__ and construct the
    # object ourselves:
    @staticmethod
    def __new_deserialized__(data, global_data):
        first_name, last_name = data
        return Person(first_name, last_name)
```
