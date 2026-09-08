---
title: "Quickstart"
url: "/docs/integrations/microsoft/quickstart"
---


# [Quickstart: Microsoft SSO](#quickstart-microsoft-sso)

Users can log into your Anvil app [using their Microsoft account](microsoft-single-sign-on). You can also restrict access to only users in your own Entra organisation by [linking your Entra ID application to Anvil](linking-azure-and-anvil).

Follow this quickstart to enable the Microsoft Service and set up a login that uses Microsoft’s Single Sign-On system.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘Blank App’. Choose the Material Design theme.

## [Enable the Users service](#enable-the-users-service)

Click the blue plus button in the [Sidebar Menu](/docs/editor#sidebar-menu) and add the Users Service.

## [Add Microsoft sign-in](#add-microsoft-sign-in)

This will open up the Users tab where you’ll see a list of options for configuring user management in your app.

Tick “Microsoft (Entra ID/Office 365)” to enable users to sign in with their Microsoft account.

This will automatically add the Microsoft API service to your app. From the Microsoft API tab, you can connect to your own Entra ID application or use other Microsoft APIs.

## [Presenting a login form](#presenting-a-login-form)

You can now [present a login form](/docs/users/presenting-a-login-form) from the Users Service.

Click on `Form1` in the App Browser.

Go to the Code view to see the code for `Form1`.

In the `__init__` method, add these lines:

```python
    anvil.users.login_with_form()

    print(f"You are logged in as: {anvil.users.get_user()['email']}")
```

## [Run your app and log in](#run-your-app-and-log-in)

Now click the ‘Run’ button at the top of the screen.

Your app will display a login form with a “Sign in with Microsoft” button.

Click the button, and the Microsoft Single Sign-On page will open in a new browser window. Log in with a Microsoft account.

You are now logged into your app. The App Console has printed the email address you logged in with.

## [Optional: Bypassing the Users Service](#optional-bypassing-the-users-service)

If you don’t want to use the Anvil Users service, you can bypass this and, instead, call Microsoft authentication directly.

Click the blue plus button in the [Sidebar Menu](/docs/editor#sidebar-menu) and add “Microsoft API”. You can then log users in using `anvil.microsoft.auth.login()` instead of `anvil.users.login_with_form()`. This will display a dialog informing the user that they are about to log in with Microsoft.

Clicking ‘Log In’ with open the Microsoft Single Sign-On page in a new browser window.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:QBAEFK7YK3ZH6TIU%3d2Y7QJ5KAAZHGJZOAMN6W36QB)

## [Next Up](#next-up)

### Want more depth on this subject?

You can restrict access to only users in your own Entra organization. Read [Connecting Entra ID to Anvil](linking-azure-and-anvil) for more details.

It’s easy to access Microsoft Azure APIs via your Entra ID. Anvil fetches an API token for you, so you just have to make the relevant HTTP requests. Read [Accessing Microsoft APIs](accessing-microsoft-apis) for more details.

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
