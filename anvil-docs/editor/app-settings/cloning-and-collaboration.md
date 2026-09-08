---
title: "Cloning and Collaboration"
url: "/docs/editor/app-settings/cloning-and-collaboration"
---


# [Collaboration with other Anvil developers](#collaboration-with-other-anvil-developers)

There are two options for collaborating on an Anvil app with other Anvil developers: adding collaborators and app cloning. Both options are available in [App Settings](/docs/editor/app-settings), under **Collaboration**.

Alternatively, you can also click the more options button next to Publish in the Editor’s header.

## [Adding other Anvil developers as collaborators](#adding-other-anvil-developers-as-collaborators)

Collaborating with other developers requires the [**Business Plan**](/pricing) or higher.

You can work on the same Anvil app with developers who are part of your subscription. You can add a developer as a collaborator to a given app, granting them access to it as if it were their own.

For more detailed instructions, please visit [this page](/docs/version-control/collaborators).

## [Cloning apps](#cloning-apps)

You can create a copy of your apps’ design, code and Data Tables. You can also allow other people to copy your apps. Each app has a secret URL for this purpose.

You will see a clone link for your app. Anyone with this link can copy your app with all its source code into their own Anvil account.

If you visit this URL in your web browser, you will be taken to the Anvil Editor, and there will be a confirmation dialog containing the name of the app and its author.

If you click `Make Copy`, you will get an app named ‘Clone of X’ (where X is the name of the original app).

The original app is not affected in any way by this operation.

## [Security Notes](#security-notes)

Clone links have the form:

```
https://anvil.works/build#clone:<app_id>=<secret_token>
```

You can regenerate the `<secret_token>` in case you want to revoke access to your app from people who currently have the clone link. The `<app_id>` is a unique ID for your app that never changes (you can access it from code using `anvil.app.id`.)

Note that using a clone link will always share the latest version of the app, including the content of all Data Tables. Make sure you regenerate the secret token if you have previously shared a Clone Link and subsequently add sensitive data to your app.
