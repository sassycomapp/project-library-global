---
document: "Facebook"
title: "Facebook"
url: "/docs/integrations/facebook"
doc-id: facebook-_index
state: Live
date-created: 2026-09-08
---


# [Facebook Integration](#facebook-integration)

### Log users in to your app with Facebook

You can log users in with their Facebook accounts, meaning they don’t have to sign up for your app.

You can add Facebook Login to the Users Service login form - see [Users:Authentication Choices](/docs/users/authentication_choices) for more details, and check the [Quickstart](facebook/quickstart) to see how to get it set up.

You can also use `anvil.facebook.auth.login()` to present a simple login dialog for only Facebook login. If you use `anvil.facebook.auth.login()`, your users’ login details are not stored in Anvil’s Data Tables.

There are analogous login options for [Microsoft](microsoft) and [Google](google) accounts.

To find out how to configure Facebook to recognise your Anvil app, see [Linking Facebook and Anvil](facebook/linking-facebook-and-anvil).
