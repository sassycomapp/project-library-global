---
title: "Uplink Security"
url: "/docs/external-resources/uplink/uplink-security"
---


# [Uplink Security](#uplink-security)

## [Sharing](#sharing)

Whoever you share the text of your server Uplink key with will have the same access to your app. So be careful if you are releasing your code online or sharing it outside your organisation. You may want to modify your scripts to remove lines with the plain text of the Uplink key:

```python
anvil.server.connect("<your Uplink key>")
```

You can instead read the key in from a file or an environment variable, and `.gitignore` any file you use to set the key locally. That way it is not shared with people you don’t trust fully. For instance:

```python
with open("<file with secret uplink key in first line>", 'r') as fin:
  uplink_key = fin.read().strip()

anvil.server.connect(uplink_key)
```

## [Client Uplink](#client-uplink)

If you are concerned about the security of a system you want to connect with Uplink, consider using [Client Uplink](/docs/uplink#client-uplink). It has the same privileges as client-side code. It cannot access [Data Tables](/docs/data-tables) unless they have been [set to client-accessible](/docs/data-tables/data-security), and it cannot register server functions. It can still *call* server functions, which allows you to selectively expose functionality by writing server functions that perform only the operations you’re willing to expose.

You can use both Server and Client keys at the same time, from different Uplink scripts.

## [Multiple Deployment Environments](#multiple-deployment-environments)

If you’re using more than one [deployment environment](/docs/deployment/environments) (for example separate “testing” and “release” versions), your app has different uplink keys for each environment.

This means that, for example, you can connect untested Uplink code to a “testing” environment without affecting the behaviour of the “release” app.

### Making Uplink functions available to all environments

Sometimes, though, you want to define `@anvil.server.callable` functions and make them available to *any* environment. For example, you might have an Uplink function that queries a local database, and you don’t want to run a new instance of that Uplink script for every environment.

For these cases, you can select **Send server calls from other environments to this Uplink** in the Uplink or Publish dialog.

This option only affects Server Uplinks, because Client Uplinks cannot define server functions.

## [Uplinks and Dependencies](#uplinks-and-dependencies)

If you select **Send server calls from other environments to this Uplink**, then Uplink functions can be called from your app’s dependencies.

That is to say, if you define server functions for your app with `@anvil.server.callable`, and another application uses your app as a [dependency](/docs/deployment/dependencies), and you have enabled uplink sharing, then that app can also call these server functions.

When your app makes an `anvil.server.call()`, it will look for server functions in these locations, in the following order:

1.  Uplink connected to this environment.
2.  Shared Uplinks in other environments of this app.
3.  Shared Uplinks in dependency apps.
4.  Server Modules.
