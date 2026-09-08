---
title: "HTMLComponent"
url: "/docs/components/standard-components/html-component"
---


# [HtmlComponent](#htmlcomponent)

You can add native HTML elements to a Form’s HTML from [HTML view](/docs/client/forms/forms-in-the-editor#html-view). Anvil represents these native HTML elements as HTMLComponents that you can then edit and interact with from the drag-and-drop designer and Python code.

The HTMLComponent has `classes` and `style` properties for styling the component with CSS. You can also [access the components underlying DOM](/docs/client/adding-ui-elements/adding-html-elements#accessing-the-dom-api) node to use its JavaScript API.

## [Referencing HTMLComponents from Python Code](#referencing-htmlcomponents-from-python-code)

You can give an HTMLComponent a Python name from the Properties Panel or the Object Palette.

You can also give it an `anvil:name` attribute in HTML view:

```html
<button anvil:name="html_button">
  Subscribe
</button>
```

You can then reference the component in Python using this name. For example:

```python
self.html_button.visible = False
```

When you add a [show or hide event](/docs/client/events#the-show-and-hide-events) to an HTML Component from the Properties Panel, Anvil automatically gives it an `anvil:name` attribute.

## [Styling HTMLComponents](#styling-htmlcomponents)

You can use CSS to style HTMLComponents via the **`classes`** and **`style`** properties.

### The `classes` property

The `classes` property accepts a list of CSS class names as defined in your app’s [`theme.css`](/docs/client/customisation/using-css#writing-css-in-themecss). You can set this property from the Properties Panel with one class per line.

You can also set the `classes` property in Python code as a list of strings:

```python
self.html_button.classes = ["subscribe-button", "disabled"]
```

You can also add or remove classes using the `add` and `remove` methods, or by setting the class name to `True` or `False` using bracket notation:

```python
# add a class
self.html_button.classes.add("rounded")
# is equivalent to
self.html_button.classes["rounded"] = True

# remove a class
self.html_button.classes.remove("rounded")
# is equivalent to
self.html_button.classes["rounded"] = False
```

If you want to check if an HTMLComponent has a particular class, you can use bracket notation or query if the string is `in` the component’s `classes`:

```python
print(self.html_button["rounded"])
# is equivalent to
print("rounded" in self.html_button)
# will return True or False
```

### The `style` property

The `style` property takes a string and sets it as the [`style` property](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/style) of the HTML element. This can be set from the Properties Panel or in Python code.

```python
self.html_button.style = "border-radius: 20px"
```

You can also set and look up styles using bracket notation:

```python
# set the border radius of the button
self.html_button.style["border-radius"] = "20px"

# check the border-radius
print(self.html_button.style["border-radius"])
# 20px
```

## [The HTMLComponent at runtime](#the-htmlcomponent-at-runtime)

At runtime, Anvil doesn’t create a separate `HtmlComponent` for every individual HTML element. Instead, it creates one `HtmlComponent` for the first HTML element it encounters, which contains that element and all the HTML inside it, until it hits:

-   an `<anvil-component>` tag, or
-   an HTML element with an `anvil:` attribute, such as `anvil:name`

When an HTML element has an `anvil:` attribute, that element becomes its own `HtmlComponent`.
