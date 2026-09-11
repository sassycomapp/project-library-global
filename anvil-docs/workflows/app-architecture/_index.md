---
document: "Anvil App Architecture"
title: "Anvil App Architecture"
url: "/docs/workflows/app-architecture"
doc-id: app-architecture-_index
state: Live
date-created: 2026-09-08
---


# [App architecture](#app-architecture)

Anvil is a platform for building full-stack web applications with nothing but Python. But what exactly is a web application? And how does the structure of an Anvil app compare to that of a traditional web app?

## [Web app architecture](#web-app-architecture)

A traditional full-stack web app is made up of three main parts: the front end (also called the client), the back end (sometimes called the server) and the database. This is the “stack” in “full-stack”. The front end is all the visual elements of your app as well as the code that runs on your browser to display those elements and make them interactive. The back end is a server that communicates with the front end and runs all the code that needs to be secure, such as retrieving password information or making a payment. The database is used for data storage and is usually only accessible from the back-end.

To learn more about the difference between the client and the server and the code that runs in each location, read [our guide](/articles/client-vs-server).

Anvil apps follow this basic web architecture. What makes Anvil different is that you can build all parts of the app in Python and easily communicate between your client code, server code and database.

## [Anvil app architecture](#anvil-app-architecture)

An Anvil app’s front end is made of two main parts:

-   The [User Interface](/docs/ui), which you design by dragging and dropping components onto the page
-   [Client-side Python code](/docs/client), which defines how the components behave and runs in the web browser

Anvil’s back end runs on a secure server, but can [easily communicate with the client code](/docs/server#calling-server-functions-from-client-code) running in the browser. Anvil apps also have a built-in database. Data can be added, deleted or modified from server code (and even client-code, when appropriate).

With Anvil, you can see and modify your front end, back-end code and database all from the Anvil Editor.

Front-end code generally runs in [Forms](/docs/ui/forms). Forms are the pages of your Anvil app. They have a visual design that describes how they look and a Python class that describes how they behave.

Back-end code generally runs in [Server Modules](/docs/server). Functions written in a server module can be called from client-side code by giving the function the `@anvil.server.callable` decorator and then calling `anvil.server.call("<function-name-here>", <arg-here>)` from the Form code.

Your app’s database is made up of [Data Tables](/docs/data-tables), of which you can have many. From the Anvil Editor, you can see a visual representation of your app’s Data Tables. Here, you can add, delete and modify rows (which you can also do from code).
