---
title: "App Secrets across Repos"
url: "/docs/workflows/version-control/git/secrets-across-repos"
doc-id: secrets-across-repos
state: Live
date-created: 2026-09-08
---


# [Using App Secrets with Multiple Checkouts](#using-app-secrets-with-multiple-checkouts)

If you use Anvil’s [App Secrets](../../security/encrypting-secret-data) to store secret data, then the values are encrypted with an encryption key that is unique to your app. This means that if you sync your source code between multiple Anvil apps (for example, using a shared [GitHub repo](../git)), the secrets you configure with one app will not be available in another.

Instead, Anvil’s App Secrets can contain multiple values for each secret or key, distinguished by which app they apply to. If you are using the same source code across multiple apps, you will have to set the value for each secret in each app.

The open-source [App Server](https://anvil.works/open-source) cannot decrypt any of these secrets, as it runs outside the Anvil hosted service. If you are using the App Server, you must supply values for each secret on the command line or in a configuration file.
