---
title: "Quickstart"
url: "/docs/integrations/facebook/quickstart"
---


# [Quickstart: Facebook Integration](#quickstart-facebook-integration)

### Log users in using Facebook accounts

Anvil provides a one-line login function to log users in to their Facebook account. You can also add a Facebook login option to the [Users Service](/docs/users) login form.

Follow this quickstart to enable the Facebook Service and log users in with Facebook.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘Blank App’. Choose the Material Design theme.

## [Enable the Facebook Service](#enable-the-facebook-service)

To add the Facebook service to your app, click the blue plus button in the [Sidebar Menu](/docs/editor#sidebar-menu).

You’ll see a list of available services and integrations. Click on the Facebook API.

## [Make Facebook aware of your Anvil app](#make-facebook-aware-of-your-anvil-app)

Facebook needs to know about your Anvil app in order for the OAuth login flow to work. You’ll use the [Facebook for Developers](https://developers.facebook.com/) console for this - it only takes a few minutes.

Run through the [Linking Facebook and Anvil](linking-facebook-and-anvil) guide and continue from here when you’re done.

## [Add a Facebook Login dialog](#add-a-facebook-login-dialog)

Go to the Code View for Form1.

Add this line to the `__init__` method:

```python
    anvil.facebook.auth.login()
```

Now add this line below it to print the logged-in user’s email:

```python
    print(f'Logged in with Facebook as: {anvil.facebook.auth.get_user_email()}')
```

## [Run your app](#run-your-app)

Run your app.

You will see a Facebook login alert.

If you click the ‘Log In’ button, the Facebook login screen will open in a new window.

You can now login with Facebook. When you’re logged in, you’ll see your email address in the App Console.

And that’s all there is to it!

## [Next up](#next-up)

### Other SSO integrations

Similar Single Sign On login functionality is available for [Microsoft](../microsoft) and [Google](../google) (and there are some other integrations for Microsoft and Google too).

Just as users can log in with their Facebook accounts using `anvil.facebook.auth.login()`, they can log in with Microsoft accounts using `anvil.microsoft.auth.login()`, and Google accounts using `anvil.google.auth.login()`.

You can add any of these login options to the multi-purpose login form presented by the [Users Service](/docs/users) as well.

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
