---
document: "Microsoft SSO"
title: "Microsoft SSO"
url: "/docs/enterprise/deployment/prerequisites/microsoft"
doc-id: microsoft
state: Live
date-created: 2026-09-08
---


# [Microsoft SSO](#microsoft-sso)

Anvil Enterprise [supports using Microsoft](/docs/integrations/microsoft) to log in to your Anvil apps or the Anvil Editor.

To prepare for this, create a new application via the [App Registrations section of the Azure Portal](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade), and set the following redirect URIs:

-   `https://PRIMARY-DOMAIN/sso/azure/callback` for SSO in the Anvil Editor
-   `https://PRIMARY-DOMAIN/apps/_/microsoft_auth_callback` for SSO in your Anvil apps

If you want to use a Microsoft login for the Anvil Editor, you will need to enable the option to issue ID tokens in the “Implicit grant and hybrid flows” section of the application’s authentication settings. This isn’t necessary if you are only using SSO for logging into your Anvil apps.

It’s possible to create separate Azure applications for SSO in the Anvil Editor vs logging into your apps, or you can use the same credentials for both. It is usually better to create separate applications for each purpose, as this improves security isolation.

Note down the Application IDs, Application Secrets and Tenant IDs (if needed), you’ll need these later.
