---
document: "Connecting to External Resources"
title: "Connecting to External Resources"
url: "/docs/external-resources"
doc-id: external-resources-_index
state: Live
date-created: 2026-09-08
---


# [Connecting to External Resources](#connecting-to-external-resources)

You can connect your Anvil app to code, web services, and databases that live outside of Anvil.

## [Uplink: code outside Anvil](#uplink-code-outside-anvil)

The Anvil Uplink lets you connect Python code running anywhere — your laptop, a private server, an IoT device, or a Colab notebook — to your Anvil app. The Uplink can expose callable functions to your app, and your app can call them just like any other [server function](/docs/server).

## [HTTP APIs](#http-apis)

Anvil makes it easy to [make HTTP requests](http-apis/making-http-requests) from client or server code. You can also expose your app’s own functionality as [HTTP endpoints](http-apis/creating-http-endpoints) using the `@anvil.server.route()` decorator.

## [Connecting to an external database](#connecting-to-an-external-database)

Because Anvil’s back end is a full Python environment, you can use standard database drivers such as Pymysql or Psycopg2 in your Server Modules to query a MySQL or PostgreSQL database.
