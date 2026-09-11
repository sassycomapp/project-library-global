---
document: "How does it work?"
title: "How does it work?"
url: "/docs/get-started/how-does-it-work"
doc-id: how-does-it-work
state: Live
date-created: 2026-09-08
---


# [How does Anvil work?](#how-does-anvil-work)

Anvil is an online IDE for building web apps entirely in Python and deploying them on the web. You [build your front-end](#building-your-ui) and [back-end in Python](#creating-your-backend-server-code), and there’s even a [Python database](#storing-data-in-databases). Anvil hosts your apps for you, so there’s nothing to install and no servers to set up (unless you’re self-hosting).

Anvil apps can do anything that Python can do. Anvil apps can also do anything that traditional JS front-ends can do: you can import JS libraries and access low-level APIs if you need them. For simplicity, Anvil also has built-in support for user authentication, building APIs, sending and receiving email, and more.

So how does it work? This article will walk you through the basic concepts behind Anvil.

## [Building your UI](#building-your-ui)

Below is a quick demo of building a [user interface in Anvil](/docs/ui). In the demo, a [Button](/docs/ui/components/basic#button) is added to the page. When the Button is clicked, its text is updated to show that the Button has been clicked.

In Anvil, you build the visual design of your user interface by dragging and dropping components onto a “Form”. Forms and components, like the Button in the demo, are just Python classes. You can change the look and feel of a component by modifying its [properties](/docs/client/component-properties).

To make a component interactive, you write a method in your Form class that runs when a user interacts with the component. Anvil components raise events when a user interacts with them, and you can [set methods that run when those events happen](/docs/client/events). For example, the Button in the demo above runs the following method when clicked:

```python
@handle("button_1", "click")
def button_1_click(self, **event_args):
  """This method is called when the component is clicked."""
  self.button_1.text = "Clicked!"
```

Anything you can do from the drag-and-drop designer you can also do in code.

## [Creating your backend server code](#creating-your-backend-server-code)

Python code in your Forms and components runs in the user’s browser. To run trusted code on the server side, you can create a [Server Module](/docs/server) and write functions there.

In a Server Module, you can write Python functions and decorate them with @anvil.server.callable. Then from your Form code, you can [call these functions using `anvil.server.call()`](/docs/server#calling-server-functions-from-client-code), passing in the name of your server function and any arguments.

`anvil.server.call()` works like a regular Python function call: it supports positional arguments, keyword arguments, and returns a value. (If you’re used to AJAX and HTTP requests, this is much simpler.)

You can [install Python packages in your server environment](/docs/server/custom-packages) and import them from your Server Modules.

Server Modules aren’t scripts; they are Python modules with functions that can be called from the front-end Form code.

## [Storing data in databases](#storing-data-in-databases)

Anvil has a built-in database, called [Data Tables](/docs/data-tables), where you can store data for your app. There is a [Python API](/docs/data-tables/data-tables-in-code) for retrieving, updating and deleting this data.

You can display or modify data in Data Tables from your client-side Form code, which means you don’t have to write a server function for every action.

For example, here is a Data Table in Anvil that has been populated from calls to a server function.

You don’t need to use Anvil’s built-in database. Because a Server Module is just a normal Python environment, you can [access external databases](/docs/data-tables/external-database) from there as you normally would.

## [Publishing your app](#publishing-your-app)

Anvil takes care of [hosting your app](/docs/deployment) as well. You can publish your app to the web in just two clicks. You can choose a public URL, a private link or add a custom domain, and each app can even have [multiple enviroments](/docs/deployment/environments) - for example, a production environment and a development one.

If you don’t want to host your app on Anvil’s cloud servers, you can use the [open-source Anvil App Server](https://github.com/anvil-works/anvil-runtime) to host your app on a different machine.
