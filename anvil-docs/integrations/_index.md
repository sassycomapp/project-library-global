---
title: "Built-in Integrations"
url: "/docs/integrations"
---


# [Built-in Integrations](#built-in-integrations)

You can connect your app with services from Google, Microsoft, Facebook, Stripe and Tableau as easily as doing anything else in Anvil.

Here’s an overview of what’s available.

## [Google](#google)

-   [Authentication](integrations/google/authenticating-users) - Log users in with their Google accounts
-   [Drive](integrations/google/google-drive) - Read and write files from your own Google Drive, and the Google Drives of your users (with permission)
-   [Google Sheets](integrations/google/google-drive#google-sheets) - Anvil has a Python API for accessing worksheets, fields, rows and cells in Google Sheets
-   [Gmail](integrations/google/gmail) - You can send email with your Gmail account (although consider the Anvil [Email Service](email))
-   [Google REST APIs](integrations/google/google-rest-apis) - You can easily get and refresh an access token to use with Google’s many REST APIs. Then you can use `anvil.http.request` to make requests against the APIs.

## [Microsoft](#microsoft)

-   [Authentication using Microsoft accounts](integrations/microsoft/microsoft-single-sign-on) - allow users to sign-in using their Office 365, Skype and other Microsoft accounts.
-   [Authentication using your own Entra ID tenant](integrations/microsoft/linking-azure-and-anvil) - allow users to sign-in using accounts in your own Entra ID tenant. You can restrict access to *only* users in your Azure organization.
-   [Microsoft Azure REST APIs](integrations/microsoft/accessing-microsoft-apis) - You can easily get and refresh an access token to use with Microsoft Azure’s many REST APIs. Then you can use `anvil.http.request` to make requests against the APIs.

## [Facebook](#facebook)

-   [Authentication using Facebook accounts](integrations/facebook/quickstart) - allow users to sign-in using their Facebook accounts.

## [SAML Authentication](#saml-authentication)

-   [Authentication using SAML](integrations/saml) - allow users to sign-in using accounts provided by a SAML identity provider.

## [Stripe](#stripe)

-   [Take payments using a built-in payment form](integrations/stripe/payments-and-subscriptions#taking-one-off-payments) - this can be customised with your own title, description and icon.
-   [Take payments using Python code](integrations/stripe/payments-and-subscriptions) - allowing you to build your own payment form and/or workflow. You can also associate multiple payments with one customer.
-   [Manage recurring subscriptions](integrations/stripe/payments-and-subscriptions#recurring-subscriptions).

## [Tableau with Anvil X](#tableau-with-anvil-x)

You can use [Anvil X](x) to create Tableau Extensions for your Tableau dashboards.

-   Quickstart: [Create a simple Tableau extension with Anvil X](x/quickstart)
-   [Access the Tableau Extensions API from within Anvil](x/tableau-extensions-api) to allow your Anvil app extension to access and manipulate data in your Tableau dashboard
-   Once you’ve got your extension published [publish a production version of your extension](integrations/x/publishing)
