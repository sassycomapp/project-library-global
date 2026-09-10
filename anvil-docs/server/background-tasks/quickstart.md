---
title: "Quickstart"
url: "/docs/server/background-tasks/quickstart"
doc-id: background-tasks-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Background Tasks](#quickstart-background-tasks)

If you need to run a process that takes a long time, you want your app to carry on running while it executes.

Follow this quickstart to trigger an artificially slow-running HTTP request in the background, and return control to your main app while it executes.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘Blank App’. Choose the Material Design theme.

## [Add a Server Module](#add-a-server-module)

In the App Browser, click “+ Add Server Module” next to Server Code to add a new Server Module.

A new tab will open with a code editor with an orange background.

## [Write a Background Task](#write-a-background-task)

Start by importing the `anvil.http` library.

```python
import anvil.http
```

Write this function into the Server Module

```python
@anvil.server.background_task
def make_slow_request():
  response = anvil.http.request("https://httpstat.us/200?sleep=5000")  # An API that provides slow responses
  print(response)
```

The `@anvil.server.background_task` decorator means that this function can be run in the background.

## [Launch the Background Task](#launch-the-background-task)

Still in the server module, write a function that launches the Background Task

```python
@anvil.server.callable
def launch_slow_request_task():
  task = anvil.server.launch_background_task('make_slow_request')
  return task
```

The `@anvil.server.callable` decorator means this function can be called from the client code.

Go to the code for Form1. It looks like this:

At the end of the `__init__` method, write these lines:

```python
    self.task = anvil.server.call('launch_slow_request_task')
```

This means your function will run when the app starts, and the `task` object will be stored. The `task` object holds all available information about the task.

## [Run your app](#run-your-app)

Now click the ‘Run’ button at the top of the screen.

The App Console at the bottom will show your Background Task running.

## [Check the output](#check-the-output)

To check the output, open the app’s Logs in the [Sidebar Menu](/docs/editor#sidebar-menu). Then select `Background Tasks`. You’ll see a table showing all the Background Tasks that this app has ever run.

Click on View Logs. You’ll be taken to the App Logs entry for that Task.

You can see the output from the Background Task. As expected, the Task printed the response from the test HTTP endpoint.

(It’s a [Media object](/docs/working-with-files/media) with a length of 0 bytes and no content - that’s because the test server (`https://httpstat.us`) returns empty responses.)

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:AWHJVR77QWY2V3R6%3d5WDDBEFKBYGUWLKT2P47BJXK)

## [Next up](#next-up)

### Want more depth on this subject?

You can pass data from a Background Task into the main app, access a task’s state, and terminate it programmatically.

You can also get a list of all the Background Tasks your app has.

Read more about [Background Tasks](/docs/background-tasks) to find out how.

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
