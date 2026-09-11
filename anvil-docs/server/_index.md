---
document: "Building the Backend"
title: "Building the Backend"
url: "/docs/server"
doc-id: server-_index
state: Live
date-created: 2026-09-08
---


# [Building the Backend](#building-the-backend)

While the [front-end](/docs/client) of your Anvil app controls how the UI looks and behaves, the back-end takes care of your app’s functionality and infrastructure.

Front-end code runs in the user’s browser, or client, which means the [user has complete access to this code](/docs/workflows/security#client-vs-server-code) and can do whatever they want with it. In the back-end, we can write code that can’t run in a browser and code that we don’t want our end users to see or touch.

Anvil provides a **server-side Python environment for your apps** which takes care of running your app’s infrastructure in a secure environment, not in a browser controlled by your end users. In this server environment, you can [run long processes](/docs/server/background-tasks) that persist beyond a user’s session, [send emails](/docs/server/email), and much more. Back-end code in Anvil is not accessible by the client, so it can house sensitive code and connect securely to your [Data Tables](/docs/data-tables). It’s also a Python 3.10 environment, which means you can [install your favourite Python packages](/docs/server/custom-packages) to run complex processes.

## [](#server-modules)[Server Modules](/docs/server/server-modules)

Anvil’s Server Modules are a full server-side Python environment, with the ability to import any packages you like.

## [](#installing-python-packages)[Installing Python Packages](/docs/server/python-versions)

Your Server Module code runs in a Python 3.10 environment on the Anvil server. Here, you can install any third-party Python packages you need into your app’s environment.

## [](#scripts)[Scripts](/docs/server/scripts)

Scripts in Anvil are single-file Python scripts that run from beginning to end. You can run Scripts directly in the Anvil Editor or launch them from your Client Code or Server Code.

## [](#background-tasks)[Background Tasks](/docs/server/background-tasks)

Background Tasks allow you to fire off a function to run in the background, leaving your main program to continue executing while the function is running.

## [](#scheduled-tasks)[Scheduled Tasks](/docs/server/scheduled-tasks)

Sometimes you want to run server functions at particular times, regardless of user activity on your app. For users on paid plans, Scheduled Tasks let you do just that.

## [](#sending-and-receiving-email)[Sending and Receiving Email](/docs/server/email)

Your apps can send and receive email using the built-in Email Service.

## [](#sessions-and-cookies)[Sessions and Cookies](/docs/server/sessions-and-cookies)

Anvil uses session tokens to allow you to store data in Server Modules for the duration of a user’s session.

Anvil also lets you store small amounts of data in between sessions through cookies, which are stored in the user’s browser.

## [](#call-context)[Call Context](/docs/server/call-context)

Call context, available through the [`anvil.server.context` object](/docs/api/anvil.server#context), provides information about where your code is running and where it was called from.

## [](#offline-apps)[Offline Apps](/docs/server/offline-apps)

Anvil apps can function offline. An app’s client-side code will continue to work if the device loses its internet connection, though some offline strategies are required to handle code that communicates with the server.
