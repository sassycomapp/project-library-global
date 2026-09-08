---
title: "Connecting Entra ID to Anvil"
url: "/docs/integrations/microsoft/linking-azure-and-anvil"
---


# [Connecting Entra ID to Anvil](#connecting-entra-id-to-anvil)

For advanced use of Anvil’s Microsoft integration, you need to let Microsoft Entra ID know about your app. This is true if you want to do either of these things:

-   [Restrict your Microsoft login to users in your organization](#create-an-app-registration)
-   [Access Microsoft Azure APIs from Anvil](accessing-microsoft-apis)

Follow this guide to create an Entra ID App Registration. An App Registration represents Azure’s knowledge of your Anvil App.

## [Create an App Registration](#create-an-app-registration)

Sign in to the [Entra Portal](https://entra.microsoft.com/) and choose ‘App registrations’ from the menu on the left. Then click ‘+ New registration’ at the top of that page.

You’ll then be able to register an application by filling out the form.

You’ll need to fill out the form with:

##### Name

Name it whatever you like - it does not *need* to be the same as the name of your Anvil App.

##### Supported account types

You have four options for who can access your app. You can restrict access to users in:

1.  Accounts in this organizational directory only (Single tenant)
2.  Accounts in any organizational directory (Any Microsoft Entra ID tenant - Multitenant)
3.  Accounts in any organizational directory (Any Microsoft Entra ID tenant - Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)
4.  Personal Microsoft accounts only

You can use any of these options with Anvil.

If you want to restrict access to **only users within your organization**, choose ‘Accounts in this organizational directory only (Single tenant)’

##### Redirect URI

Choose ‘Web’ as the platform and enter `https://anvil.works/apps/_/microsoft_auth_callback` as the redirect URI. You can add this later if you forget at this stage.

## [Copy the relevant IDs into Anvil](#copy-the-relevant-ids-into-anvil)

After you’ve created the app registration, you will see an overview screen, which has an ‘Application (client) ID’ and a ‘Directory (tenant) ID’. You will need to copy these values into Anvil.

If your Anvil app doesn’t already have the Microsoft API service added, click the blue plus button in the Sidebar Menu. You’ll see a list of available services and integrations. Click on Microsoft API.

In the Microsoft API tab that opens, tick ‘Link to your own Entra ID app’

You’ll now be able to add the Application ID and Tenant ID from earlier. If you chose options 2, 3 or 4 in the list above (allowing access to accounts in any Entra ID tenent or all Microsoft accounts), select ‘Multi-tenant’. In this case you do not need to enter a Tenant ID.

## [Create a Client Secret](#create-a-client-secret)

Back in your app registration overview, choose ‘Certificates & secrets’ and then click ‘+ New client secret’

Add a description for your secret and choose when you would like it to expire. A client secret will be generated for you. Copy its value now. You won’t be able to view the secret again if you close this page.

Back in your Anvil app, from the Microsoft API tab, click ‘Set Client Secret’ and paste in the value you copied from Entra.

## [Test that it works](#test-that-it-works)

To check it works, go to the Code view for Form1. Add these lines to the `__init__` method:

```python
    anvil.microsoft.auth.login()
    print(anvil.microsoft.auth.get_user_access_token())
```

If everything is working, you should successfully get an access token.

This checks that your Anvil app is successfully linked to your Entra ID app - if it were not linked, Entra would not provide an access token.

## [Next up](#next-up)

### Access Microsoft APIs

Now you have your Anvil app set up to connect your Entra ID tenant, you can access a whole universe of Microsoft APIs. Read [Accessing Microsoft APIs](accessing-microsoft-apis) to see how (you’re most of the way there already).
