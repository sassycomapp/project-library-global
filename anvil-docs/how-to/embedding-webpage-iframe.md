---
title: "Embed a Webpage in an Anvil App"
url: "/docs/how-to/embedding-webpage-iframe"
---


# [Embed a Webpage in an Anvil App](#embed-a-webpage-in-an-anvilapp)

In this guide, I’ll show you how to embed a webpage in your Anvil app with just 3 simple steps. You can use this to embed blogs, charts or embedded analytics like PowerBI.

We’ll do this using an [iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe), which is a way of embedding one webpage inside another. Anvil lets us call JavaScript functions in Python code using [anvil.js](https://anvil.works/docs/client/customisation/javascript/accessing-javascript). We’re going to use `anvil.js` to create an iframe tag and add it to our page, using jQuery.

Here’s a link if you would like to clone a finished example:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:BSCEDQFEQTOLPZXA%3dMOEWITBLNADXXOHYXNU434KT)

Let’s get started.

## [1. Importing jQuery and get_dom_node](#1-importing-jquery-and-get_dom_node)

Let’s start by importing jQuery and get_dom_node at the top of our Anvil app’s [form](https://medium.com/r/?url=https%3A%2F%2Fanvil.works%2Fdocs%2Fclient%2Fui).

```python
# Add these imports to your form
from anvil.js.window import jQuery
from anvil.js import get_dom_node
```

## [2. Creating the iframe element](#2-creating-the-iframeelement)

Next, let’s create an iframe element. We can use [jQuery’s `attr()`](https://api.jquery.com/attr/#attr-attributeName-value) function to set the `src` attribute to the website we would like to embed in our iframe.

```python
# Create an iframe element and set the src
iframe = jQuery("<iframe width='100%' height='800px'>").attr("src","https://www.wired.co.uk/")
```

## [3. Adding the iframe to a container](#3-adding-the-iframe-to-a-container)

Lastly, we need to add the iframe to a [container component](https://anvil.works/docs/client/components/containers).

We can use [jQuery’s `appendTo()`](https://api.jquery.com/appendto/) function to add the `iframe` object to a container in our form. We’ll need to pass the [DOM node](https://developer.mozilla.org/en-US/docs/Glossary/DOM) of the container into this function. In this example, I’m appending the `iframe` to `self.content_panel`. We will use [`anvil.js.get_dom_node()`](https://anvil.works/docs/client/customisation/javascript/accessing-javascript#accessing-a-dom-node) to access the DOM node for the content panel.

```python
# Append the iframe to a container in our form
iframe.appendTo(get_dom_node(self.content_panel))
```

That’s it! We now have a webpage embedded in our Anvil app.

## [Conclusion](#conclusion)

We’ve learnt how to:

-   Import jQuery and get_dom_node
-   Create the iframe element
-   Add the iframe to a container

Here’s a link if you would like to clone a finished example:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:BSCEDQFEQTOLPZXA%3dMOEWITBLNADXXOHYXNU434KT)
