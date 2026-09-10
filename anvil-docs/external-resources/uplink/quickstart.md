---
title: "Quickstart"
url: "/docs/external-resources/uplink/quickstart"
doc-id: uplink-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Connect to code on your local machine](#quickstart-connect-to-code-on-your-local-machine)

The Anvil Uplink lets you connect to Python code running anywhere and call Python functions directly from your app.

In this quickstart, you’ll create a simple function on your local machine and call it from your Anvil app.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘Create a new app’. Choose the Material Design theme.

## [Enable the Uplink](#enable-the-uplink)

Click the **+** button in the Sidebar Menu, and select **Uplink**.

The Uplink window looks different depending on whether your app has one or multiple [deployment environments](/docs/deployment/environments):

**For a single deployment environment:** You will be prompted to choose between a Client Uplink and a Server Uplink. Click the **Enable server Uplink** button.

**For multiple deployment environments:** Click on the environment you want to connect the Uplink to, then click **Enable** next to **Server Uplink Key**.

#### Copy your Uplink key

Once enabled, Anvil generates a secret key. You will use this key to connect your external Python code to your application. **Copy it to your clipboard**.

You can also use a ‘client’ Uplink key that only gives the permissions available to client-side code. You can use this to connect to untrusted code with a restricted set of permissions so your data remains secure. We’ll stick with the Server Uplink key for this quickstart. [Learn more about Client Uplink](/docs/uplink#client-uplink).

## [Install the Uplink library](#install-the-uplink-library)

On your own computer, install the Uplink library (ensure you have Python installed).

```python
pip install anvil-uplink
```

## [Connect a Python script to your app](#connect-a-python-script-to-your-app)

On your computer, create a file called `hello.py` with the following contents:

```python
import anvil.server

anvil.server.connect("<your Uplink key>")

@anvil.server.callable
def say_hello(name):
  print(f"Hello from your own machine, {name}!")

anvil.server.wait_forever()
```

Replace the `"<your Uplink key>"` string with the Uplink key from your app.

Run the script. You should see output like this:

```
Connecting to wss://anvil.works/uplink
Anvil websocket open
Authenticated OK
```

## [Call your local function from your app](#call-your-local-function-from-your-app)

Back in the Anvil Editor, close the Uplink dialog and click on ‘Code’ to see the Python code for `Form1`.

You will see a few lines of pre-written code. Your [Form](/docs/ui/forms) is represented as a class called Form1. It currently has only one method, the `__init__` method.

At the end of the `__init__` method, add this line to call the `say_hello` function in your `hello.py` script on your computer:

```python
    anvil.server.call('say_hello', 'Anvil Developer')
```

## [Run your app](#run-your-app)

Now click the **Run** button at the top right of the screen.

Go back to where your script is running on your computer. It should have printed this message:

```
Hello from your own machine, Anvil Developer!
```

You’ve successfully connected your own machine to your Anvil app.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:F7TDC2LWKXMR36XL%3dTDSO5DU7AKULMNW4NVF66HIO)

## [What you can do with the Uplink](#what-you-can-do-with-the-uplink)

A script that runs `anvil.server.connect()` can do anything an Anvil Server Module can. For example, it can:

-   call functions in your Anvil Server Modules or in any other Uplink-connected script, using `anvil.server.call`
-   use Data Tables directly
-   check which user is currently logged in

You can connect the Uplink to any environment that runs Python, including Jupyter Notebooks.

[Tutorial: build a UI for a Jupyter Notebook](/learn/tutorials/jupyter-notebook-to-web-app)

This means you are not limited to what Anvil provides — you can use all the capabilities of your own machine or setup, while still benefiting from Anvil’s features. Many people use Anvil as an add-on to their existing systems, to provide a UI or simple email client.

The Uplink works by running a Python process on your machine that connects securely to your Anvil app. Because Python can make system calls, that process can trigger any program or action your machine can perform. This makes it possible to integrate with existing systems, control hardware, run automated tests, or launch other processes directly from your Anvil app.

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [connecting your app to any external Python code](/docs/uplink).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
