---
title: "Quickstart"
url: "/docs/server/server-modules/quickstart"
---


# [Quickstart: Server Code](#quickstart-server-code)

### Learn how to run code in Anvil’s hosted Python backend

Anvil provides a server-side Python environment for your apps.

Follow this quickstart to write a server function and call it from the client.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Add a Server Module](#add-a-server-module)

In the App Browser, click “+ Add Server Module” next to Server Code to add a new Server Module.

A new tab will open with a code editor. The orange line on the left margin of the code editor indicates that this code will run on the server.

## [Write a server function](#write-a-server-function)

Write this function into the Server Module:

```python
def say_hello(name):
  print(f"Hello from the server, {name}")
  return [1, 2, 3, 4]
```

## [Make your function client-callable](#make-your-function-client-callable)

Above your `say_hello` function, add `@anvil.server.callable`. The function now looks like this:

```python
@anvil.server.callable
def say_hello(name):
  print(f"Hello from the server, {name}")
  return [1, 2, 3, 4]
```

That makes the `say_hello` function callable from the client side.

## [Switch to the Code View for Form1](#switch-to-the-code-view-for-form1)

Under Forms in the App Browser, select Form1.

Click on the ‘Code’ tab to see the Python code for `Form1`.

## [Call your server function from the client](#call-your-server-function-from-the-client)

You will see a few lines of pre-written code. Your Form is represented as a class called Form1. It currently has only one method, the `__init__` method.

At the end of the `__init__` method, write these lines:

```python
    return_value = anvil.server.call('say_hello', 'Anvil Developer')
    print(f"The return value was {return_value}")
```

## [Run your app](#run-your-app)

Now click the ‘Run’ button at the top of the screen.

The Output Panel should display these lines:

The output with the orange line next to it came from a Python process running in Anvil’s cloud cluster. The output with the blue line next to it ran in your browser. You made the browser communicate with the server over the internet by writing `anvil.server.call('say_hello', 'Anvil Developer')`.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:DYC4ARVS4ZZRX4KN%3dQBJ4LUJNGX3DOURQP37SXT4M)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [server-side code in Anvil](/docs/server).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
