---
title: "anvil.js"
url: "/docs/api/anvil.js"
doc-id: anvil.js
state: Live
date-created: 2026-09-08
---


## `anvil.js` Module

#### Classes

[`ProxyType`](#ProxyType)

#### Functions

[`await_promise`](#await_promise) [`call`](#call) [`get_dom_node`](#get_dom_node) [`import_from`](#import_from) [`new`](#new) [`report_all_exceptions`](#report_all_exceptions) [`report_exceptions`](#report_exceptions) [`to_media`](#to_media)

#### Globals

[`window`](#window)

#### Exceptions

[`ExternalError`](#ExternalError)

## Classes

### `ProxyType`

The type of a JavaScript object in when accessed in Python code

#### Constructor

`ProxyType()`

---

## Functions

#### `await_promise(js_promise)` [(more info)](/docs/client/javascript/accessing-javascript#calling-asynchronous-javascript-apis)

Await the result of a Javascript Promise in Python. This function will block until the promise resolves or rejects. If the promise resolves, it will return the resolved value. If the promise rejects, it will raise the rejected value as an exception

---

#### `call(js_function_or_name, *args)` [(more info)](/docs/client/javascript/accessing-javascript#calling-proxyobjects)

Call a global Javascript function by name, translating arguments and return values from Python to Javascript.

---

#### `get_dom_node(component) → DOM node` [(more info)](/docs/client/javascript/accessing-javascript#accessing-a-dom-node)

Returns the Javascript DOM node for an Anvil component. If a DOM node is passed to the function it will be returned. Anything else throws a TypeError

---

#### `import_from(url) → Javascript Module` [(more info)](/docs/client/javascript/accessing-javascript#javascript-modules)

use anvil.js.import_from(url) to dynamically import a Javascript Module. Accessing the attributes of a Javascript Module vary depending on the Module. See the documentation for examples

---

#### `new(js_class, *args)` [(more info)](/docs/client/javascript/accessing-javascript#calling-with-new)

Given a Javascript class (aka function object) that's been passed into Python, construct a new instance of it.

---

#### `report_all_exceptions(bool, [reraise=True])` [(more info)](/docs/client/javascript/accessing-javascript#capturing-exceptions-in-callbacks)

Set the default exception reporting behaviour for Python callbacks in Javascript.When set to True all exception will be reported by anvil and then re-raised within Javascript. This may mean some exceptions are reported twice, but it ensures Exceptions in your Python code are reported correctly. If reraise is to False, Exceptions raised in python code will be reported by Anvil, but not re-raised in Javascript. Instead the Python callback will return undefined to Javascript.

---

#### `report_exceptions(wrapped_function) → function` [(more info)](/docs/client/javascript/accessing-javascript#capturing-exceptions-in-callbacks)

Use @anvil.js.report_exceptions as a decorator for any function used as a javascript callback. Error handling may be suppressed by an external javascript libary. This decorator makes sure that errors in your python code are reported.

---

#### `to_media(blob, [content_type=""], [name=None]) → anvil.BlobMedia instance`

Convert a javascript Blob, ArrayBuffer, Uint8Array or an Array of these types to an anvil BlobMedia object. If a Blob, or Array of Blobs, is passed the content_type will be inferred.

---

## Globals

#### `window`

The Javascript global 'window' object, wrapped and accessible from Python.

---

## Exceptions

#### `ExternalError` [(more info)](/docs/client/javascript/accessing-javascript#catching-exceptions)

An Error that occurs in Javascript will be raised in Python as an anvil.js.ExternalError. Typically used in a try/except block to catch a Javascript Error

#### Attributes

**original_error** - *Javascript object*

The original Javascript error that was raised.
