---
document: "Quickstart"
title: "Quickstart"
url: "/docs/integrations/saml/quickstart"
doc-id: saml-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: SAML Authentication](#quickstart-saml-authentication)

### Authenticate with SAML in your Anvil app

Anvil provides a SAML login function to authenticate users with an existing external account, alongside or instead of other user management options.

This quickstart takes you through an example, showing how to configure an Anvil app to authenticate with identities provided by [Auth0](https://auth0.com).

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Enable SAML Authentication](#enable-saml-authentication)

In the [Sidebar Menu](/docs/editor#sidebar-menu), click the blue plus button. You’ll see a list of available services and integrations. Click on SAML Authentication.

## [Configure the Users Service to use SAML](#configure-the-users-service-to-use-saml)

[Add the Users Service](/docs/users/quickstart-login), and then click on the ‘Users’ under the Services section to get to the Users configuration page. Here, you’ll be able to enable SAML login, and, optionally, disable email login.

## [Configure your identity provider to trust your Anvil app](#configure-your-identity-provider-to-trust-your-anvil-app)

When configuring your identity provider for use with Anvil’s SAML authentication, you’ll need some metadata from your Anvil app. This can be downloaded by clicking the ‘Download Service Provider Metadata’ button in the SAML Authentication service section.

You’ll need to use this metadata to configure your identity provider. Your chosen identity provider will have their own method of using the metadata provided by the ‘Download Service Provider Metadata’ button. Many will allow direct upload of this XML file.

The following example specifically shows how Auth0 uses this data.

*These instructions are specific to Auth0; your IdP will vary. See [Auth0’s SAML documentation](https://auth0.com/docs/protocols/saml-configuration-options/configure-auth0-as-saml-identity-provider) for more details.*

From your Auth0 dashboard, go to Applications, and create an app. Click on that app and go to its ‘Addons’ tab, under which you will be able to toggle the ‘SAML2 Web App’ add-on.

Once toggled to ‘True’, clicking on that ‘Addon’ box will bring up the page where Auth0 requires the metdata from your Anvil app. Auth0 does not have a feature allowing direct upload of XML metadata.

In this example:

-   the `Application Callback URL` is how Auth0 refers to the Assertion Consumer Service URL for your Anvil app, which is available within your app’s metadata file as `Location` under the `AssertionConsumerService` tag
-   the `audience` is the Entity ID, available within your app’s metadata as `entityID` under the `EntityDescriptor` tag
-   the `signingCert` is the `X509Certificate` from your app’s metadata

## [Configure your Anvil app to trust your identity provider](#configure-your-anvil-app-to-trust-your-identity-provider)

Now you need to do the converse of the above; your identity provider will also supply some metadata to allow you to configure your Anvil app. In particular, you need the data to fill in the fields found at the top of the SAML Authentication service configuration.

These details should either be provided to you explicitly by your identity provider, or supplied in the form of an XML file.

For more details, see [Configuring Options for SAML Authentication](configuration-options).

## [Call the login function](#call-the-login-function)

When users visit your app, we want to display the login box immediately. We can do that by calling `anvil.users.login_with_form()` in the `__init__` method of `Form1` as follows:

Click on `Form1` in the App Browser.

Go to the Code view to see the code for `Form1`.

In the `__init__` method, add these lines:

```python
    anvil.users.login_with_form()

    print(f"You are logged in as: {anvil.users.get_user()['email']}")
```

## [Run your app and log in](#run-your-app-and-log-in)

Now click the ‘Run’ button at the top of the screen.

Your app will run and display a dialog allowing you to authenticate with SAML. If you have not disabled email login, the email login dialog will also display in this form.

Click ‘Log In with SAML’ to authenticate. A new window will open, allowing you to log in with your chosen identity provider.

You are now logged into your app. The email address you logged in with is printed in the [App Console](/docs/editor#app-console).

## [Next Up](#next-up)

### Want more depth on this subject?

SAML authentication has more options for configuration; see [here](configuration-options) for more details.

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
