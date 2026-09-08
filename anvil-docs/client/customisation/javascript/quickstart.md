---
title: "Quickstart"
url: "/docs/client/customisation/javascript/quickstart"
---


# [Quickstart: JavaScript](#quickstart-javascript)

Learn how to drive JavaScript functions and external libraries from Anvil.  
Follow this Quickstart guide to create an app that drives a [Quill](https://quilljs.com/) text editor (all from Python!).

## [Include the External Library](#include-the-external-library)

Check the library for the [installation options](https://quilljs.com/docs/installation). There will often be a CDN option with some HTML. When you include the HTML in your project, the library will be pulled in from an external host.  
Find this code and paste it into your [native-libraries](/docs/client/customisation/javascript#using-native-javascript-libraries).

```html
<!-- Main Quill library -->
<script src="//cdn.quilljs.com/1.3.6/quill.js"></script>
<!-- Theme included stylesheets -->
<link href="//cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
```

*Many libraries offer a choice between a .min.js file (faster to load, but harder to debug if you need it) and a .js version (for easier debugging). In this case, we suggest using the .js version while you’re developing your integration, then switching to the .min.js version when you’re ready to publish, to speed up your users’ loading time.*

**Security Note**: When using rich text editors like Quill with user-generated content, always sanitize HTML output on the server side before storing or displaying it to prevent cross-site scripting (XSS) attacks. Never trust HTML content from client-side editors without proper sanitization.

## [Import JavaScript into Anvil](#import-javascript-into-anvil)

The [`anvil.js`](/docs/api/anvil.js) module gives you access to the [window object](https://developer.mozilla.org/en-US/docs/Web/API/Window). Any JavaScript object from the window can be imported into Anvil. We need the `Quill` constructor from JavaScript so import it.

```python
from anvil.js.window import Quill 
# import the Quill constructor from JavaScript
```

## [Convert JavaScript to Python](#convert-javascript-to-python)

Start using the library. This involves reading the documentation and adapting examples to work in Anvil. Below is some JavaScript from the [Quill documentation](https://quilljs.com/guides/why-quill/#easy-to-use).

```javascript
// JavaScript code from Quill documentation


var quill = new Quill('#editor', {
    modules: { toolbar: true },
    theme: 'snow'
});

quill.on('text-change', function(delta, oldDelta, source) {
    console.log(source, quill.getText());
});
```

**Make it Python!**

-   dictionary string keys must use quotes in Python
-   `true` and `false` become `True` and `False`
-   `null` becomes `None`
-   Inline functions with multiple lines of code should be extracted into separate functions

Add a ColumnPanel in the design view. We’ll tell Quill to use the ColumnPanel as the editor with `anvil.js.get_dom_node()`.

Call the `Quill` constructor inside your Form’s `__init__` method with the DOM node and some options. We’ll also add a method `text_change()` to handle the Quill ’text-change’ event.

A Form’s `__init__` method runs before the Form, and its components, are added to the page. Some JavaScript functions will require DOM nodes to be on the page in order to execute correctly. If this is the case, or if you notice some strange behaviour, try moving the JavaScript to the Form’s `show` event. A Form’s `show` event executes after components are added to the page.

Here’s what your final code should look like.

```python
from ._anvil_designer import Form1Template
from anvil import *
from anvil.js.window import Quill
import anvil.js

class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

    editor = anvil.js.get_dom_node(self.column_panel_1)
    # add a ColumnPanel in the design view
    # get the dom node for the ColumnPanel
    
    self.quill = Quill( editor, {
        'modules': { 'toolbar': True },
        'theme': 'snow'
    })
    
    self.quill.on('text-change', self.text_change)
    
  def text_change(self, delta, old_delta, source):
    print(source, self.quill.getText())
```

The above code is enough to get started with a Quill editor in Anvil. Run the code!

## [Copy The Example App](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:DF45P3PVBZBSXNLP%3dREHNQQ6MX673CU3AG4ZJWJ7Z)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [Accessing JavaScript](accessing-javascript).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
