---
title: "Google SSO"
url: "/docs/enterprise/deployment/prerequisites/google"
---


# [Google SSO](#google-sso)

Anvil Enterprise supports using Google to log in to your Anvil apps, log in to the Anvil Editor, and [access various other Google services](/docs/integrations/google).

To prepare for this, create a new application via the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager), and set the following redirect URIs:

-   `https://PRIMARY-DOMAIN/google-oauth2-callback` for SSO in the Anvil Editor
-   `https://PRIMARY-DOMAIN/apps/_/client_auth_callback` for SSO in your Anvil apps

It’s possible to create separate Google applications for SSO in the Anvil Editor vs logging into your apps, or you can use the same credentials for both. It is usually better to create separate applications for each purpose, as this improves security isolation.

Note down your Google Client IDs and Client Secrets, you’ll need these later.
