---
title: "Sharing SAML Credentials across Anvil apps"
url: "/docs/integrations/saml/sharing-credentials-across-apps"
---


# [Sharing SAML credentials across Anvil apps](#sharing-saml-credentials-across-anvil-apps)

For the purposes of this documentation, ‘all your Anvil apps’ means all apps owned by you, or users within your Anvil subscription.

In many use cases, you’ll want the same accounts within your organisation to able to use all your Anvil apps - for example, if you have developed multiple internal tools with Anvil, you’ll want your users to be able to access all of them with the same credentials. With the ability to share your SAML configuration across your apps, it means you only have to configure your Identity Provider once, but you are then able to use that Identity Provider for authentication across all your Anvil apps.

To enable sharing of your SAML configuration, tick the box in the SAML Authentication Service. This causes all of your Anvil apps to behave as a single service provider. Then, once you’ve configured your Identity provider to trust one of your apps, you can simply copy that app’s configuration to the rest of your apps in order to allow your IdP to trust all of them - without having to reconfigure your IdP.

Then, in order to use the same SAML configuration in another of your apps, configure its SAML Authentication service in exactly the same way as the app that’s already set up. The Service Provider Metadata (XML) for each app configured in this way will then be the same, so your Identity Provider will trust all of them.

## [Sharing credentials and the EntityID](#sharing-credentials-and-the-entityid)

The `entityID` for your Anvil app will change depending on whether its SAML configuration is shared across all your apps.

If the SAML configuration is not shared, then the service provider is the app itself, and has its own `entityID`.

If the SAML configuration is shared, then the service provider is your organisation’s Anvil account, and all your apps share the `entityID.`

Therefore, if you will want to share your SAML configuration across apps, it’s best to enable this option before setting up your first app, to ensure that you use the shared `entityID` from the start.
