---
title: "Sharing Uplinks"
url: "/docs/external-resources/uplink/dependencies"
doc-id: uplink-dependencies
state: Live
date-created: 2026-09-08
---


# [Sharing Uplinks](#sharing-uplinks)

If you connect an Uplink to your app, you can choose to *share* it, by allowing it to be called from apps that [depend on](../../deployment/dependencies) this app or from other [deployment environments](../../deployment/environments).

## [Multiple Deployment Environments](#multiple-deployment-environments)

If you’re using more than one [deployment environment](../../deployment/environments) (for example separate “testing” and “release” versions), your app has different uplink keys for each environment.

This means that, for example, you can connect untested Uplink code to a “testing” environment without affecting the behaviour of the “release” app.

### Making Uplink functions available to all environments

Sometimes, though, you want to define `@anvil.server.callable` functions and make them available to *any* environment. For example, you might have an Uplink function that queries a local database, and you don’t want to run a new instance of that Uplink script for every environment.

For these cases, you can select **Send server calls from other environments to this Uplink** in the Uplink or Publish dialog.

This option only affects Server Uplinks, because Client Uplinks cannot define server functions.

## [Uplinks and Dependencies](#uplinks-and-dependencies)

If you select **Send server calls from other environments to this Uplink**, then Uplink functions can be called by any app that uses your app as a [dependency](../../deployment/dependencies).

That is to say, if you define server functions for your app with `@anvil.server.callable`, and another application uses your app as a dependency, and you have enabled uplink sharing, then that other app can also call these server functions.

When your app makes an `anvil.server.call()`, it will look for server functions in these locations, in the following order:

1.  Uplink connected to this environment.
2.  Shared Uplinks in other environments of this app.
3.  Shared Uplinks in dependency apps.
4.  Server Modules.
