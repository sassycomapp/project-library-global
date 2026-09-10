---
title: "Quickstart"
url: "/docs/external-resources/http-apis/making-http-requests/quickstart"
doc-id: making-http-requests-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Making HTTP requests](#quickstart-making-http-requests)

Anvil lets you make HTTP requests with very little code.

Follow this quickstart to access an external HTTP API from Python and print the response.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Install `requests`](#install-requests)

Go to Settings, and click on **Python versions**. Select “Python 3.10” from the dropdown and [install](/docs/server/custom-packages#adding-packages) `requests`.

## [Add a Server Module](#add-a-server-module)

Go back to the App Browser and click “+ Add Server Module” next to Server Code to add a new Server Module.

A new tab will open with a code editor with an orange background.

## [Write a server function](#write-a-server-function)

Import `requests` and write this function into the Server Module:

```python
@anvil.server.callable
def access_xkcd_api(comic_number):
  response = requests.get(f"https://xkcd.com/{comic_number}/info.0.json")
  return response.json()
```

`requests` makes the HTTP request. We are using the API of the webcomic [XKCD](https://xkcd.com) to get the details of a given comic.

## [Call your server function from the client](#call-your-server-function-from-the-client)

Go to the code for Form1. It looks like this.

At the end of the `__init__` method, write these lines:

```python
    return_value = anvil.server.call('access_xkcd_api', 353)
    print(return_value)
```

This means your function will run when the app starts, and the result will be printed.

## [Run your app](#run-your-app)

Now click the ‘Run’ button at the top of the screen.

The Output Panel should display this.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:UAINOMJEFJGAQSKQ%3d42JOJYLA6WPC7K57ZBEX727V)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [HTTP APIs and requests in Anvil](/docs/http-apis).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
