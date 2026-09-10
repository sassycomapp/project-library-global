---
title: "Quickstart"
url: "/docs/integrations/stripe/quickstart"
doc-id: stripe-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Stripe integration](#quickstart-stripe-integration)

### Take payments using Stripe

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Enable the Stripe Service](#enable-the-stripe-service)

In the [Sidebar Menu](/docs/editor#sidebar-menu), click the blue plus button. You’ll see a list of available services and integrations. Click on Stripe

## [Log in to a Stripe account](#log-in-to-a-stripe-account)

You must now connect Anvil to a Stripe account. You have two options.

**If you already have a Stripe account**, you can log in to it from Anvil to connect your app to Stripe.

Click ‘Yes - connect my existing account’. You’ll get a Stripe log in window - log in to your account.

**If you do not already have a Stripe account**, you’ll need one in order to take payments. Click ‘No - I need to create an account’. You’ll get a Stripe sign-up window, where you can enter a few details. Once you’ve signed up, you’ll be back in the Anvil Editor.

## [Add a payment form to your app](#add-a-payment-form-to-your-app)

Click on `Form1` in the App Browser.

Go to the Code view to see the code for `Form1`.

In the `__init__` method, add these lines:

```python
    c = stripe.checkout.charge(currency="GBP", amount=100)
    print(c)
```

## [Run your app and get paid](#run-your-app-and-get-paid)

Now click the ‘Run’ button at the top of the screen.

Your app will run and display a payment form. The Stripe Service is running in test mode, so no money will actually change hands.

For the card number, enter `4242424242424242` (This is a Visa test card number). Put anything in the other fields (the expiry date must be in the future).

Hit the ‘Pay’ button. The Stripe payment form will disappear and your main app will finish loading. Your transaction details have been printed on the App Console.

The transaction details contain `'result': 'succeeded'` - so Stripe has registered the transaction!

## [Running in Live mode](#running-in-live-mode)

To take payments for real, hit the ‘Switch to **Live** mode’ button in the Stripe Service.

The warning goes away and your transactions will now be enacted for real.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:OLRW4672HFS2QQ7U%3dLGK2GLCFMSXJO7DK6HVJ4SU4)

Of course, you’ll need to log in to your own Stripe account - the cloned app does not retain the connection to Stripe, for obvious security reasons.

## [Next Up](#next-up)

### Want more depth on this subject?

As well as presenting a pre-made payment form, Anvil has Python methods for making Stripe payments programmatically. This uses Stripe’s token system that allows transmitting card details while complying with financial regulations.

The Python API allows you to:

-   Make a payment programmatically using a card details token,
-   associate transactions with a customer record,
-   store the card details token against a customer record,
-   and set up recurring subscriptions.

You can also use the raw Stripe Python API if you prefer.

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
