---
title: "Workflows and Best Practices"
url: "/docs/workflows"
doc-id: workflows-_index
state: Live
date-created: 2026-09-08
---


# [Workflows and Best Practices](#workflows-and-best-practices)

This section covers tools and patterns to help you build better Anvil apps. Here, you’ll find information on how to structure and debug your apps as well as how to build secure apps and work collaboratively with other devlopers

## [Anvil app architecture](#anvil-app-architecture)

Learn more about how Anvil apps are structured, including where code runs and how the file system is structured.

## [Debugging your apps](#debugging-your-apps)

The Anvil Editor includes a suite of built-in debugging tools. Use the interactive debugger to pause and inspect running code, the Server Console to run server-side Python interactively, and the App Console to interact with your UI components in real time.

## [Building secure apps](#building-secure-apps)

Anvil uses a capability-based security model: untrusted client-side code runs in the browser, while trusted server-side code runs in a protected environment users can never access. Learn how this model works and how to structure your app to keep sensitive logic and data secure.

## [Version control and collaboration](#version-control-and-collaboration)

Anvil’s built-in version control is based on Git. Learn how to use commits, branches, and merges to track changes to your app, collaborate with other developers, and publish specific versions to your users.

## [Dealing with timezones](#dealing-with-timezones)

`datetime` objects can pick up different timezones as they move between the browser, server, and Data Tables. Learn how Anvil automatically stamps datetimes with timezone information and how to use the `anvil.tz` module to create timezone-aware objects explicitly.
