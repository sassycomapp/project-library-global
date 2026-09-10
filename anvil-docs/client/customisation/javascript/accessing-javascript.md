---
title: "Accessing JavaScript"
url: "/docs/client/customisation/javascript/accessing-javascript"
doc-id: accessing-javascript
state: Live
date-created: 2026-09-08
---


# [Accessing JavaScript](#accessing-javascript)

Interaction with JavaScript objects in Anvil is primarily done through the [`anvil.js`](/docs/api/anvil.js) module. This reference provides some details about working with JavaScript objects from Python code.

Check out the [Quickstart](quickstart) guide for an introduction applied to an external library.

HTML Forms also have a unique way to interact with their JavaScript functions [described here](html-forms).

## [Accessing the window](#accessing-the-window)

You can access any JavaScript function or variable by importing it from the [`window` object](https://developer.mozilla.org/en-US/docs/Web/API/Window). The `window` object can be thought of as the JavaScript global namespace in the browser where your app runs.

```python
from anvil.js.window import Foo
# Foo is a JavaScript object defined in the JavaScript namespace
```

## [Accessing a DOM Node](#accessing-a-dom-node)

You can access the [DOM node](https://developer.mozilla.org/en-US/docs/Glossary/DOM) for any Anvil Component in Python:

```python
anvil.js.get_dom_node(component)
# access any anvil component's DOM node
```

You can also [access HTML elements from Python code](/docs/client/forms/html-in-forms#accessing-the-dom-api-of-html-components) using the `dom_nodes` API. Give the element an `anvil:dom-node` attribute:

```html
<div anvil:dom-node="my-component"></div>
```

```python
my_element = self.dom_nodes['my-component']
```

These objects are real [JavaScript HTMLElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) objects.

## [Accessing an External Library](#accessing-an-external-library)

If you’ve found a JavaScript library that you want to use within Anvil, always check the documentation and look for a browser option. Not all JavaScript runs in the browser, and often library authors will provide a JavaScript option specifically for the browser.

When a JavaScript library has a browser version the code will look something like this:

```html
<script src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
```

In the above example, a CDN provider hosts the JavaScript library’s source code. By adding the script tags to our Native Libraries the JavaScript source code will add objects as attributes to the `window`. We can then import the objects into Python using `anvil.js.window`. For an example of this approach, see how we load the Quill library in the [Quickstart](quickstart) guide.

Almost all JavaScript libraries are available at [npmjs](http://npmjs.com/). Often you’ll find browser versions of those libraries hosted by CDN providers such as [jsdelivr](https://www.jsdelivr.com/), [unpkg](https://unpkg.com/) or [cdnjs](https://cdnjs.com/). Be aware that finding a JavaScript library on jsdelivr, unpkg or cdnjs does not guarantee its suitability for the browser.

You can avoid using a CDN provider by pasting the JavaScript source code into a JavaScript file in your assets. Then replacing the CDN provided URL with a relative URL.

```html
<script src="_/theme/quill.js"></script>
```

A script tag with a `src` attribute is the traditional way to access JavaScript files in the browser.

### JavaScript Modules

A more modern approach for working with JavaScript in the browser is to use a [JavaScript module](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules). The main difference is that a JavaScript module does not add objects to the `window`. Instead, you explicitly import objects from the module. The library’s sample code will look something like this:

```html
<script type="module">
  import { v4 as uuid4 } from 'https://jspm.dev/uuid';
  console.log(uuid4());
  //1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed

</script>
```

With JavaScript modules we **don’t** need to paste the sample code into our Native Libraries. Instead, we can use `anvil.js.import_from(URL)` to access the JavaScript objects directly in Python.

```python
import anvil.js
uuid_module = anvil.js.import_from('https://jspm.dev/uuid')
uuid4 = uuid_module.v4
print(uuid4()) # 1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed
```

In the JavaScript code above, `v4` is a named import (aliased as `uuid4`). We access a named import in Python using `.` notation.

JavaScript modules may also have a `default` import and you may see sample code like this:

```html
<script type="module">
  import confetti from 'https://cdn.skypack.dev/canvas-confetti';
  confetti(); // 🎉

</script>
```

Since `confetti` is not inside curly braces it is the `default` import (rather than a named import). In Python, the above sample code would become the following:

```python
import anvil.js
confetti_module = anvil.js.import_from('https://cdn.skypack.dev/canvas-confetti')
confetti = confetti_module.default
confetti() # 🎉
```

`anvil.js.import_from()` always returns a JavaScript Module object. You can then access the JavaScript objects, as we’ve done above, with `.` notation.

You can also import an ES module stored in your app’s Assets. For example, a module stored at `theme/assets/library.mjs` is available at `./_/theme/library.mjs`:

```python
import anvil.js
library_module = anvil.js.import_from('./_/theme/library.mjs')
```

The `./` prefix makes this a relative JavaScript module specifier.

*Tip: [skypack.dev](https://www.skypack.dev/) is a CDN provider that only provides JavaScript modules for the browser. If you can’t find a browser supported version of your preferred JavaScript library you may find it at skypack.dev.*

## [Return values from `anvil.js`](#return-values-from-anviljs)

When using `anvil.js`, JavaScript primitives are mapped to their Python equivalents. JavaScript collections use Python-compatible proxy objects backed by the original JavaScript collection, so changes remain visible from both languages.

`string`, `number`, `boolean` map to `str`, `int`/`float`, `bool`. `null` and `undefined` map to `None`. Mutable `Array` becomes a list-compatible proxy, frozen `Array` a Python `list`, `Map` a dict-compatible proxy, `Set` a set-compatible proxy, and `Uint8Array` Python `bytes`.

In the other direction, Python lists and tuples become JavaScript Arrays, dictionaries become object literals, sets become Sets, and `bytes` become a `Uint8Array`.

Other JavaScript objects, including dictionary-like object literals and class instances, are returned as proxyobjects. Proxyobjects are Python objects that wrap a JavaScript object and allow you to interact with the underlying JavaScript object from Python code.

An `ArrayBuffer` and typed arrays other than `Uint8Array` remain proxyobjects. Wrap an `ArrayBuffer` in `Uint8Array` when you need Python bytes:

```python
from anvil.js.window import Uint8Array
data = Uint8Array(array_buffer)
```

```python
from anvil.js.window import Foo
print(type(Foo)) # <class 'Proxy'>
```

Return values from `anvil.js.get_dom_node` are also proxyobjects.

```python
dom_node = anvil.js.get_dom_node(self.content_panel)
print(dom_node) # <HTMLDivElement proxyobject>
```

As is the `window` object!

```python
print(anvil.js.window) # <Window proxyobject>
```

## [Catching Exceptions](#catching-exceptions)

When a JavaScript Error is thrown within JavaScript code, it is re-raised in Python as an ExternalError. You can catch JavaScript errors in Python with [`anvil.js.ExternalError`](/docs/api/anvil.js#ExternalError) using a try/except block. If you need to access the original JavaScript error, use the property [`.original_error`](/docs/api/anvil.js#ExternalError_attributes).

```python
import anvil.js
from anvil.js.window import Foo

try:
    Foo()
except anvil.js.ExternalError as err:
    print(err) # this includes the string output of the original error
    js_error = err.original_error
    print(js_error.message) # most JavaScript Errors have a message property
    print(js_error.name) # most Javsacript Errors have a name property
```

## [Working with proxyobjects](#working-with-proxyobjects)

### Attributes

You can access the attributes on the underlying JavaScript object in Python as you would in JavaScript.

```python
Foo.bar     # use . notation
Foo['bar']  # use [] subscript notation
```

JavaScript attributes will be returned to Python in the same way as described above. Calling `dir()` on a proxyobject, e.g. `dir(Foo)`, will give an indication of the available attributes accessible in Python.

All proxyobjects have a `keys()` method e.g. `Foo.keys()`. Calling `keys()` returns a list of strings, which represents the underlying JavaScript object’s own property names. All proxyobjects have a `get()` method e.g. `Foo.get('bar', None)`. The default value will be returned if the attribute is not found.

### Iteration

If an object is iterable in JavaScript then it will be iterable in Python. Typically proxyobjects are not iterable - but you can iterate over the keys.

### `__class__`

Accessing `.__class__` of a proxyobject will return the constructor of the underlying JavaScript object.

```python
x = Foo()
print(x)           # <Foo proxyobject>
print(x.__class__) # <proxyclass 'Foo'> (the JavaScript constructor)
print(type(x))     # <class 'Proxy'>
```

### `True` or `False`

All proxyobjects are considered ‘Truthy’ (i.e. `bool(proxy_obj)` will be `True`) unless the underlying JavaScript object is empty `{}` or the proxyobject can be called with `len` and `len(proxy_obj) == 0`.

### `len()`

You can call `len()` on a proxyobject if the underlying JavaScript object is not a function and has a `.length` property.

## [Converting to Python](#converting-to-python)

A proxyobject, which is a dictionary-like, is easily converted into a Python dictionary.

```python
print(proxy_obj) # proxyobject({'a': 1, 'b': 2})
dict(proxy_obj)  # {'a': 1, 'b': 2}
{**proxy_obj}    # {'a': 1, 'b': 2} 
```

The above code works for all proxyobjects regardless of the underlying JavaScript object. However, only the keys returned from the `.keys()` method will be included in the dictionary object. Thus it is unlikely to be suitable for most proxyobjects.

A proxyobject is considered dictionary-like when the underlying JavaScript object is an [object literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer). Proxyobjects that are dictionary-like can be sent to the server.

## [Calling proxyobjects](#calling-proxyobjects)

If the underlying JavaScript object is callable, then the proxyobject is callable in Python.  
Kwargs will not work when calling proxyobjects since kwargs are not supported in JavaScript.

When calling a proxyobject: the arguments will be converted to JavaScript, the underlying JavaScript function will be called, and the return value will be converted to Python.

If you need to control when the `new` operator is used, you can use `anvil.js.new` or `anvil.js.call`.

```python
from anvil.js.window import Foo
import anvil.js

anvil.js.new(Foo, 1, 'a')  # Foo will be called with the new keyword
anvil.js.call(Foo, 1, 'a') # Foo will be called without the new keyword
```

`anvil.js.call('Foo')`  
`anvil.js.call(anvil.js.window['Foo'])`  
`anvil.js.window.Foo()`  
Are three ways of calling a JavaScript function from Python

### Calling asynchronous JavaScript APIs

Some JavaScript libraries will use asyncronous Promises. If your JavaScript library includes an api that returns a Promise then you can write this code as syncronouse Python.

When an asynchronous JavaScript function returns a Promise, Python blocks the execution until the Promise resolves before continuing. If the Promise rejects an exception is raised. The same mechanism described here is also used for `anvil.server.call()`.

If you obtain a Promise object by some other route, you can block until it resolves by calling [`anvil.js.await_promise(js_promise)`](/docs/api/anvil.js#await_promise). This will return the resolved value of the Promise, or raise an exception if it rejects.

## [Using Python functions as callbacks](#using-python-functions-as-callbacks)

You can use Python functions as callbacks, or event handlers, for JavaScript libraries. If you pass a callable Python object, Anvil wraps it as a JavaScript function.

### Blocking functions

When a Python function is called from JavaScript, the function returns (or throws an exception) synchronously, like any JavaScript function – **unless** it blocks. If the function blocks, it will return a Promise that resolves (or rejects) when the Python function returns (or raises an exception).

### Capturing exceptions in callbacks

Sometimes, the JavaScript library you are using will handle exceptions itself. This can make it frustrating to debug your code, as it prevents Anvil from displaying information about the exception in the [Output panel](/docs/editor#output-panel) or the [App Logs](/docs/editor/app-logs).

You can avoid this problem by adding the [`@anvil.js.report_exceptions`](/docs/api/anvil.js#report_exceptions) decorator to your Python callback. Alternatively, set Anvil’s exception reporting as the default behaviour by calling [`anvil.js.report_all_exceptions(True)`](/docs/api/anvil.js#report_all_exceptions).
