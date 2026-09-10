---
title: "stripe.checkout"
url: "/docs/api/stripe.checkout"
doc-id: stripe.checkout
state: Live
date-created: 2026-09-08
---


## `stripe.checkout` Module

#### Functions

[`charge`](#charge) [`get_token`](#get_token)

## Functions

#### `charge(amount=, currency=, [title=], [description=], [icon_url=], [billing_address=], [shipping_address=], [zipcode=])` [(more info)](/docs/integrations/stripe)

Charge the user for a one-off payment, by showing a Stripe checkout form. Returns a dictionary of information about the transaction on success.

-   `amount` - a number, in least units of currency (eg cents or pennies)

-   `currency` - a three-letter currency code (eg 'USD')

-   `title` - configures the checkout dialog

-   `description` - configures the checkout dialog

-   `icon_url` - path to an image to be used on the checkout form (eg anvil.server.get_app_origin() + '/_/theme/icon.png')

-   `billing_address` - (boolean) setting to True requires the user to enter a billing address

-   `shipping_address` - (boolean) setting to True requires the user to enter a shipping and billing address

-   `zipcode` - (boolean) setting to True requires the user to enter their zipcode/postal code

---

#### `get_token(amount=, currency=, [title=], [description=], [icon_url=], [billing_address=], [zipcode=], [raw=])`

Show the Stripe checkout form, and return a raw (token, user_details) tuple.

The token can be used to place charges from server modules. The user_details are a dictionary of user-supplied data (eg 'email').

'amount' is a number, in least units of currency (eg cents or pennies). 'currency' is a three-letter currency code (eg 'USD'). 'title' and 'description' configure the checkout dialog. Setting 'zipcode' to True requires the user to enter their postal code. Setting 'billing_address' to True requires the user to entier a billing address.

Setting 'raw' to True returns a token for your own API key, which is only useful if you are using the Stripe API directly. If you do this, you cannot use this token with the Anvil Stripe APIs.
