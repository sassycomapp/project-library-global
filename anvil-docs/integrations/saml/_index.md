---
title: "SAML Authentication"
url: "/docs/integrations/saml"
---


# [SAML Authentication](#saml-authentication)

Configuring SAML authentication allows users to log in to your app with an identity provded by another service.

The SAML Authentication Service is available for users on Business plans and above.

### Overview

Anvil’s SAML integration allows users of your app to authenticate against your own SAML Identity Provider, which might be managed by your company.

SAML authentication requires that both parties (identity provider and service provider) have been [configured to trust each other](saml/configuration-options). Then, when a user authenticates, the service provider can trust that the identity provider has verified their identity, and the identity provider can trust that the user was sent from a legitimate source.

To set up this relationship, you need some data from your Service Provider (your Anvil app) and your Identity Provider (which might be something like Okta, ADFS, or Shibboleth). Anvil provides your app’s metadata from [within the SAML Authentication Service tab](saml/configuration-options#configuring-your-identity-provider-with-your-anvil-app-s-details), and your Identity Provider should supply you with their data.

Once both your Service Provider and your Identity Provider have been configured to trust each other, authenticating a user is easy - the Service Provider sends the user to the Identity Provider, who verifies their identity and sends them back.

Follow the [Quickstart](saml/quickstart) to enable SAML authentication in your app and display a form that users can use to log in with their existing accounts.

### Accessing user SAML attributes within Anvil

Some Identity Providers send additional user attributes in SAML responses; these can include things like full name and group membership. The SAML module within Anvil allows you to easily access a logged-in user’s SAML attributes within your app. Test it out with the following snippet.

```python
    import anvil.saml.auth

    print(anvil.saml.auth.get_user_attributes())
```

### Sharing credentials across your Anvil apps

If you want all your Anvil apps to use the same Identity Provider, it’s easy to share a SAML configuration across all apps in your Anvil account or subscription. See [Sharing Credentials Across Apps](saml/sharing-credentials-across-apps) to find out more.

### Other integrations

Anvil also has specific support for single sign-on with [Microsoft](microsoft/microsoft-single-sign-on), [Google](google/authenticating-users) and [Facebook](facebook). If you use one of those services, you might want to use the service-specific functionality - it’s easier to configure, and also supports those services’ APIs.

As well as SAML, you can add any of these authentication options to the multi-purpose login form presented by the [Users Service](/docs/users).
