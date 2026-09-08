---
title: "Using Stripe's Python API"
url: "/docs/integrations/stripe/raw-api-tokens"
---


# [Using Stripe’s Python API](#using-stripes-python-api)

If you’re using a [Python 3.10](https://anvil.works/docs/server/custom-packages#available-python-versions) server environment, you can opt out of using Anvil’s simplified APIs. Instead, you can install the Stripe package with [self-service package installation](https://anvil.works/docs/server/custom-packages) and use the official [Stripe Python API](https://stripe.com/docs/api?lang=python) from your Server Modules.

To use Stripe’s Python API, you’ll need to do two things:

1.  Configure your Stripe **Secret Key** in your Anvil app. Use the [App Secrets](/docs/security/encrypting-secret-data) service to store it, rather than leaving it in your source code!

2.  Enter your **Publishable Keys** into Anvil’s Stripe configuration page.

The [steps below](#configuring-your-stripe-api-keys) show you how to do this in Anvil

## [Configuring your Stripe API keys](#configuring-your-stripe-api-keys)

To use the official API, you will need to provide Anvil with your Secret Key and your Publishable Keys.

The steps below will walk you through how to access your keys and how to configure them inside Anvil.

To learn more about Stripe’s API Keys, how to manage your keys and when you should use Test and Live modes, see the Stripe docs [here](https://stripe.com/docs/keys)

### Accessing your Stripe API Keys

First, navigate to your Stripe [Dashboard](https://dashboard.stripe.com/test/dashboard)

In the navigation pane on the left, click on ‘Developers’, then click on ‘API keys’.

You’ll see a list of ‘Standard Keys’ which includes both your Publishable Key and your Secret key.

You also have the option to view either your live keys or your test keys using the toggle.

### Adding your publishable keys to Anvil

After adding the ‘Stripe’ service by clicking the blue plus button, select ‘Stripe’ from the Sidebar Menu. Add your Test and Live publishable keys in the boxes provided.

### Adding your secret key to Anvil

Use the [App Secrets](/docs/security/encrypting-secret-data) service to store your Secret key, and then add the key to your app.

For example, if you store your secret key using Anvil’s App Secrets service as ‘stripe\_key’, add these lines to provide Stripe with your secret key:

```python
import stripe

stripe.api_key = anvil.secrets.get_secret('stripe_key')
```

## [Taking a payment](#taking-a-payment)

Once you have configured both your publishable and secret keys, you can use Stripe’s Python API.

To use the official API, you will still need to collect users’ card details and generate Stripe tokens. In your Form code, you can call `stripe.checkout.get_token()` with the `raw=True` parameter. This will generate a token that you can use with the Stripe Python API.

For example, to take a payment:

```python
# Use Stripe Checkout to generate a raw token
token, user_info = stripe.checkout.get_token(
    currency='GBP',
    amount=999,
    title='Payment for your Anvil',
    raw=True
)
anvil.server.call('charge', token)
```

```python
import stripe

stripe.api_key = anvil.secrets.get_secret('stripe_key')

@anvil.server.callable
def charge(token):
  charge = stripe.Charge.create(
    currency='GBP',
    amount=999,
    description='Payment for your Anvil',
    source=token
  )
```
