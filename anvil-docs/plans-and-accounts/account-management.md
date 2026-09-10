---
title: "Managing your Anvil account"
url: "/docs/plans-and-accounts/account-management"
doc-id: account-management
state: Live
date-created: 2026-09-08
---


# [Account Management](#account-management)

This documentation will tell you all about how to manage your account and billing with Anvil.

If you’re the administrator of a subscription and you **are not an Anvil developer**, see here to learn how to [manage your organisation’s subscription](#managing-a-subscription-without-an-anvil-developer-account) without an Anvil developer account.

## [Signing Up](#signing-up)

To create an Anvil account, visit the [sign up page](https://anvil.works/sign-up). Then, click on “Sign Up For Free” and follow the on-screen instructions to create your account.

When you create an Anvil account, you can choose to sign up with an email address or with Google.

See here for details on [setting up two-factor authentication](#two-factor-authentication).

## [The Account Management Screen](#the-account-management-screen)

Once you have signed up, you can manage your account by opening the account management screen in the top right:

## [Managing Your Login](#managing-your-login)

### Changing Your Password

To change your password, open the [account management screen](#the-account-management-screen) and navigate to ‘Authentication’. Enter your current password and enter a new password. Then click “Update Password”.

If you don’t remember your current password, sign out of Anvil and go to the [login screen](https://anvil.works/login). Then, select “Forgot Password?”.

### Changing Your Email Address

Please contact [support@anvil.works](mailto:support@anvil.works) to change the email address registered to your account.

## [Two Factor Authentication (2FA)](#two-factor-authentication-2fa)

This only applies to accounts created using an email and password, and does not apply to Google SSO.

To set up two-factor authentication (2FA), open the [account management screen](#the-account-management-screen) and navigate to ‘Authentication’. Enter your account password and select ‘Enable’.

This will then give you a QR code to scan in order to set up 2FA in an authentication app (such as [Google Authenticator](https://en.wikipedia.org/wiki/Google_Authenticator)).

From now on, every time you login to your Anvil account you will be asked to provide the code from your authenticator app.

To disable two-factor authentication, go back to the “Authentication” section of the account management screen and select the “Disable” button.

## [Managing A Subscription](#managing-a-subscription)

**It is free to use Anvil, even for commercial purposes.** However, certain features are available to users on a [paid plans](https://anvil.works/pricing). For more details on free vs paid plans, [see this documentation](https://anvil.works/docs/overview/free-vs-paid).

### Upgrading An Account

To upgrade your account, open the [account management screen](#the-account-management-screen) and navigate to the Subscription tab.

Then click the “Upgrade” button and choose the [plan](https://anvil.works/pricing) that’s right for you.

Once you’ve selected the plan for you, enter your billing details and click “Upgrade”.

Once you’ve upgraded, Anvil’s paid features will be available immediately.

### Cancelling A Subscription

To cancel your subscription, open the [account management screen](#the-account-management-screen) and navigate to the Subscription tab. Then click “Cancel your subscription”.

You have to be the organisation’s account owner to cancel a **multi-user subscription**, i.e. a [Business Plan](https://anvil.works/pricing) or higher.

This will open a screen which asks you to confirm you’d like to cancel. It also shows you the date at which your account will revert to the Free Plan.

Any feedback you leave in the “Please tell us why you’re leaving” box is greatly appreciated as we continue to improve Anvil for everyone.

### Leaving A Subscription

If you’re a developer on someone else’s licence, you can leave their subscription by selecting “Leave subscription” in the subscription menu.

## [Account Management For Business Plans And Above](#account-management-for-business-plans-and-above)

### Managing Developers On A Subscription

If you are the administrator for a [Business Plan](https://anvil.works/pricing) or above, then you can have multiple developers use your licence to develop apps with paid features.

You can use the developers menu to invite new users to join your organisation via an email. To do this click “Invite a user to join this account”. To revoke an invitation, select the red minus button next to the pending invitation.

To remove developers from your subscription click the red trash button next to the developers email.

You can also add or remove developer seats from your subscription. To do this, click the “Add or Remove Seats” button. This will open the **Update Plan** window, where you can update the number of developer seats.

The minimum number of seats you can have is equal to the number of developers currently using seats on your account. To reduce the seat count, you must first remove those developers from your subscription.

### Managing A Subscription **Without** An Anvil Developer Account

You can be the administrator for a [Business Plan](https://anvil.works/pricing) or above and not have an Anvil account. To manage your account and subscription in this scenario, you can go to [https://anvil.works/manage](https://anvil.works/manage) and log in.

The [Manage page](https://anvil.works/manage) page has the same tabs, options and controls as the [Account Management screen](#account-management) for controlling your subscription. There is an additional tab called Managers which allows you to invite other people to become account managers without the need for them to sign up to an Anvil developer account.

## [Account Quotas](#account-quotas)

Some Anvil features have usage quotas, which vary depending on which [plan](https://anvil.works/pricing#compare) you are on. The Account Quotas and Usage tab shows how much of each quota you have used across these features:

1.  Email Quota: How many [emails](/docs/email) you have left from your monthly allowance, with the date it resets.
2.  Custom Package Limits: The maximum size and install time allowed for [custom packages](/docs/server/custom-packages#custom-python-packages).
3.  [Compute Usage](#compute-usage): How much compute all apps on your plan are using.
4.  [Database](#database): How much Data Table storage and rows the apps in your plan are using.

### Compute Usage

The Compute Usage chart shows the total compute used by all apps in your account over a two-month period. You can switch between views for the past 24 hours, 1 week, or 2 months.

On multi-user plans, subscription administrators see compute usage for all apps in their organisation, while non-admin users see apps they don’t have access to grouped as ‘Other Apps’.

#### What different plans see:

-   **Free, Hobby, and Business plan users:** A compute usage chart showing server usage across all apps, measured in Compute Units (CU) per second.
-   **Production plans:** Two charts showing usage of shared Anvil resources and their dedicated server resources, both measured in Compute Units (CU) per second.

The legend to the right of the chart shows all apps contributing to compute usage over the selected time period. Click an app name to view its individual usage. For app-level CPU and memory metrics, see [App CPU and Memory Usage](/docs/editor/app-logs#cpu-usage-history).

### Database

This section includes charts and tables showing how many Data Table rows you have used and how much storage your apps are consuming. It also breaks down usage by app so you can see where your quota is being used. On Business plans and above, only plan administrators can view database usage.

## [Billing And Invoices](#billing-and-invoices)

If you’re the administrator of a subscription and you **do not have an Anvil account**, see here to learn how to [manage your organisation’s subscription](#managing-a-subscription-without-an-anvil-developer-account).

The Billing tab shows your subscriptions payment details, invoices and billing history.

Your invoices are generated at the end of each day and show up under “Billing History”.

Business plans can receive invoices via email, to do this select “Receive invoices by email” and enter the address you’d like your invoices to be sent to. Once set up, you can update the email address or stop receiving invoices in the Billing tab.

## [Deleting Your Account](#deleting-your-account)

To permanently delete your Anvil account, your apps and all of your data from our systems, please contact [privacy@anvil.works](mailto:privacy@anvil.works) from the email address registered to your account.

Once your account is deleted, your account will no longer be available in our systems. **You won’t be able to reactivate your previous account and you won’t be able to recover any apps or data.**
