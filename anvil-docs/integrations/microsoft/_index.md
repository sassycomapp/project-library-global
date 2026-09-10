---
title: "Microsoft"
url: "/docs/integrations/microsoft"
doc-id: microsoft-_index
state: Live
date-created: 2026-09-08
---


# [Microsoft Integration](#microsoft-integration)

The Microsoft API Service enables users to log in to your app using their Entra ID account. This can be restricted to accounts within your Microsoft organisation.

You can also access a range of Microsoft Azure REST APIs by geting an API token.

The Microsoft API Service is available for users on Business plans and above.

### Get started

Follow the [Quickstart](microsoft/quickstart) to enable the Microsoft API Service in your app and display a login form that users can use to login with their Microsoft accounts.

### More on Microsoft Account auth

For more detail on Microsoft Account login (including how to do it using the Users Service instead), see [Microsoft Single Sign-On](microsoft/microsoft-single-sign-on).

### Restricting users to your own Azure organisation

Restrict your app to users within your own organisation by using your own Entra ID tenant. See [Connecting Entra ID to Anvil](microsoft/linking-azure-and-anvil) to find out how.

### Access Microsoft Azure APIs

Once your user has logged in to Microsoft, you can get an API token for Microsoft Azure’s many REST APIs. See [Accessing Microsoft Azure APIs](microsoft/accessing-microsoft-apis) to find out how.

### Other integrations

Similar Single Sign-On login functionality is available for Facebook and Google.

Just as users can log in with their Microsoft accounts using `anvil.microsoft.auth.login()`, they can log in with Facebook accounts using `anvil.facebook.auth.login()`, and Google accounts using `anvil.google.auth.login()`.

You can add any of these login options to the multi-purpose login form presented by the [Users Service](/docs/users) as well.
