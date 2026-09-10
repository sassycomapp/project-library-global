---
title: "HTML Forms"
url: "/docs/client/customisation/javascript/html-forms"
doc-id: html-forms
state: Live
date-created: 2026-09-08
---


# [HTML Forms](#html-forms)

All [HTML Forms](/docs/ui/layouts/html-layouts) have an underlying HTML Template. HTML Forms are able to call JavaScript functions defined within the HTML Template.

This reference describes how to interact with those JavaScript functions defined in the HTML Template.

## [Calling JavaScript](#calling-javascript)

Every HTML Form (that is, any Form **except a Blank Panel Form**) has a `call_js` method that will invoke a JavaScript function.

Blank Panel Forms do not have a `call_js` method - make sure you’re using a **Custom HTML** Form.

Here is a simple JavaScript function that can be placed in an HTML template of a Custom HTML form.

```html
<script>
function showJsAlert(message) {
    alert(message);
    return 42;
}
</script>
```

Here is the code to call that function from Python.

```python
def button_1_click(self, **event_args):
    # This method is called when the button gets clicked
    self.call_js('showJsAlert', 'Hello, world!')
```

You can pass any argument to this function. JSON-compatible values (strings, numbers, lists, bools, dicts and `None`) are mapped to JavaScript equivalent JSON-compatible values. Non-JSON-compatible values are wrapped. The reverse is also true when calling a Python function from JavaScript. *(Note JavaScript dictionary-like objects are returned as dictionaries, unlike return values from the [`anvil.js` module](accessing-javascript#return-values-from-anviljs))*

This is just an example. If you want to show a pop-up alert in your app, you should use Anvil’s [`alert() function`](/docs/client/adding-ui-elements/alerts-and-notifications) instead!

You may also use the [`anvil.js.call()`](/docs/api/anvil.js#call) function to call global JavaScript functions. This does not need to be called from an HTML form, it will work anywhere in client code. The main difference between the `self.call_js` method described above, and `anvil.js.call()` is the JavaScript `this`. See the next section for details.

### Referring to the form from JavaScript

When you call a JavaScript function from an HTML Form using `self.call_js`, `this` is bound to the (jQuery-wrapped) DOM node that represents the form itself (`self`). Whereas `this` will not be bound when using the `anvil.js.call()` function.

Using `self.call_js` means you have all the usual [jQuery methods](https://api.jquery.com/) available to you, starting from the current component:

```javascript
// (in JavaScript:)

function setColor(color) {
    // Find all the 'div' elements inside this component

    var divs = this.find("div");
    divs.css("background-color", color)
}
```

```python
# (in Python)
def button_1_click(self, **event_args):
    # This method is called when the button gets clicked
    self.call_js('setColor', 'red')
```

This is just an example. If you want to change the background colour of something on your page, change the `background` [property](/docs/client/component-properties) of a component instead!

### Running JavaScript on Form startup

If you want to run JavaScript on Form startup, run it from the `show` event handler.

```python
def form_show(self, **event_args):
    """This method is called when the HTML panel is shown on the screen"""
    self.call_js('initMyJavaScriptLibrary')
```

This executes after the Form has been added to the page. Do not `self.call_js()` from your form’s `__init__` method. A Form’s `__init__` method runs before the Form is added to the page, and JavaScript in the Form’s HTML template is not executed until it is added to the page.

### Implementation detail

If you have multiple functions in the JavaScript global namespace with the same name you cannot guarantee which function will be called when using `self.call_js`. This might happen if you have various HTML Forms with the same underlying HTML Template.

## [Calling Python from JavaScript](#calling-python-from-javascript)

Any method on your Custom HTML Form can be called from JavaScript. Imagine you have this method:

```python
def my_method(self, name):
    alert(f"Hello, {name}")
    return 42
```

To call into Python from JavaScript, use `anvil.call()` within a JavaScript function.

```javascript
// (in JavaScript:)

function myFunc() {
    anvil.call($('.content'), 'my_method', 'world')
}
```

The first argument is a DOM element (optionally jQuery-wrapped) that indicates which Form instance you would like to call the function on. It is not necessary to specify the exact DOM element of the Form; any child element will work. It is an error to pass a first argument that is *not* an Anvil HTML Form or a child of an HTML Form.

The second argument is a method name, and all other arguments are passed to the Python method.

The second argument of `anvil.call` is the name of a Python method on a Custom HTML Form. Make sure you’re using a **Custom HTML** Form, not a Blank Panel Form.

## [Asynchronous JavaScript](#asynchronous-javascript)

`anvil.call()` returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), which resolves to the method’s return value (if it returns), or rejects with an exception object (if it throws an exception). *If the method throws an exception, the exception stack trace will be captured in the Anvil logs, regardless of the JavaScript’s behaviour.*

An Example of Asynchronous JavaScript:

```python
# (in Python)
def my_method(self, name):
    alert(f"Hello, {name}")
    return 42
```

```javascript
// (in JavaScript:)

// Pop up a "Hello, World" Anvil alert when my-link

// is clicked.

$('.my-link').on('click', function(e) {
    var linkElement = this;
    anvil.call(linkElement, "my_method", "World")
    .then(function (r) {
        // resolves after the python function has exectuted

        // in this case r will be 42

        console.log("The function returned:", r);
    });
    e.preventDefault();
});
```

If you call a JavaScript function from an Anvil form, and it returns a Promise, Python execution will block until that promise resolves (in which case, the resolved value is returned) or rejects (in which case, the rejected value is thrown with an `ExternalError` exception).

```javascript
// (in JavaScript:)

function sleepForSomeTime(duration) {
    return new Promise(function(resolve, reject) {
        setTimeout(function() { resolve(42); }, duration)
    })
}
```

Here’s the Python code that runs that JavaScript:

```python
# When the button is clicked, it will wait 5 seconds
# before printing '42' to the Output Panel:
def button_1_click(self, **event_args):
    r = self.call_js('sleepForSomeTime', 5000)
    print(r)
```
