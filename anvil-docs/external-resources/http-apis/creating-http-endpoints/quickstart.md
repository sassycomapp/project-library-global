---
title: "Quickstart"
url: "/docs/external-resources/http-apis/creating-http-endpoints/quickstart"
doc-id: creating-http-endpoints-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Creating HTTP endpoints](#quickstart-creating-http-endpoints)

### Put an HTTP API on your app

Anvil lets you set up HTTP endpoints with very little code.

Follow this quickstart to create an HTTP endpoint that extracts two variables from the path and creates a response dynamically based on their values.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Add a Server Module](#add-a-server-module)

In the App Browser, click “+ Add Server Module” next to Server Code to add a new Server Module.

A new tab will open with a code editor with an orange border.

## [Create an HTTP endpoint](#create-an-http-endpoint)

Write this function:

```python
def add_numbers(a, b):
  a = int(a)
  b = int(b)
  return {
    'originals': [a, b],
    'sum': a + b,
  }
```

It takes two numbers and returns a data structure containing their sum.

Above this function, write `@anvil.server.route('/add/:a/:b')`:

```python
@anvil.server.route('/add/:a/:b')
def add_numbers(a, b):
  a = int(a)
  b = int(b)
  return {
    'originals': [a, b],
    'sum': a + b,
  }
```

## [Access your HTTP endpoint](#access-your-http-endpoint)

If you haven’t [published your app](/docs/deployment) yet, at the bottom of your Server Module you will see a message prompting you to publish your app.

Once you’ve published your app, you will see a message explaining URL stem of HTTP API.

Copy the URL (without the `{path}` part), and put `add/32/10` at the end. For my app that would be:

`https://tepid-optimal-brain.anvil.app/api/add/32/10`

Open a new browser tab and access that URL. You should see this response:

```
{"sum":42,"originals":[32,10]}
```

Pass in different numbers to get a different answer:

`https://tepid-optimal-brain.anvil.app/add/1/3`

This time the response is:

```
{"sum":4,"originals":[1,3]}
```

(To set up a nicer URL for your API, see [deployment](/docs/deployment/quickstart).)

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:BWRDAQNJ2QGBCDYQ%3dUPLKHPZR5YRPG76PVPS3JQFX)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [HTTP APIs and requests in Anvil](/docs/http-apis).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
