---
title: "Connecting Facebook to Anvil"
url: "/docs/integrations/facebook/linking-facebook-and-anvil"
---


# [Connecting Facebook to Anvil](#connecting-facebook-to-anvil)

You can allow your users to sign in with Facebook using the Facebook Service.

Follow these steps to configure Facebook to allow Anvil to communicate with it.

## [Create an app in Facebook for Developers](#create-an-app-in-facebook-for-developers)

To connect Anvil with Facebook, you need to create an ‘app’ in [Facebook for Developers](https://developers.facebook.com/). For our purposes, this is just a record held by Facebook to inform it of your Anvil app.

If you already have an app in Facebook for Developers that you want to link to Anvil, you can skip this step.

To create a new one, go to [https://developers.facebook.com/](https://developers.facebook.com/) and click on ‘get started’. You’re presented with some simple setup steps, fill them in as appropriate.

## [Add Facebook Login to your Facebook app](#add-facebook-login-to-your-facebook-app)

After some basic setup steps, you’ll be presented with ‘Add A Product’. Add Facebook Login.

## [Configure the OAuth redirect URI](#configure-the-oauth-redirect-uri)

In the Facebook Login Product’s Settings, there is a box marked ‘Valid OAuth Redirect URIs’. Add `https://anvil.works/apps/_/facebook_auth_callback` to it.

## [Copy the App ID and App Secret into Anvil](#copy-the-app-id-and-app-secret-into-anvil)

Now go to Settings->Basic. Copy the App ID and App Secret for your app.

Add the Facebook Service to your Anvil app from the Anvil Editor, and paste your App ID and App Secret into the appropriate boxes.

## [Authenticate with Facebook and get an Access Token](#authenticate-with-facebook-and-get-an-access-token)

To show a Facebook login prompt, in client code, call:

```python
    anvil.facebook.auth.login()
```

You can also request particular OAuth scopes, to use with the Facebook Graph API. For example, to access your user’s Instagram profile and post content on their behalf:

```python
    anvil.facebook.auth.login(['instagram_basic', 'instagram_content_publish'])
```

Once your user has logged in with Facebook, you can get basic information about the logged-in user by calling [`anvil.facebook.auth.get_user_id()`](/docs/api/anvil.facebook.auth#get_user_id) or [`anvil.facebook.auth.get_user_email()`](/docs/api/anvil.facebook.auth#get_user_email).

For other interactions, you’ll need to use the [Facebook Graph API](https://developers.facebook.com/docs/graph-api/). To get an Access Token to access the Graph API, call [`anvil.facebook.auth.get_user_access_token()`](/docs/api/anvil.facebook.auth#get_user_access_token). Here’s an example:

```python
    if anvil.facebook.auth.login() is not None:
        user_id = anvil.facebook.auth.get_user_id()
        token = anvil.facebook.auth.get_user_access_token()
        r = anvil.http.request(f"https://graph.facebook.com/{user_id}?fields=id,name&access_token={token}", json=True)
        alert(f"Hello, {r['name']}!")
```

## [Authenticate with the Users Service](#authenticate-with-the-users-service)

You can also use Facebook login with Anvil’s [built-in user authentication](/docs/users). To do this, add the Users Service and check the Sign In With Facebook box.

Your login form will now show a ‘Log In With Facebook’ link, which opens the Facebook login dialog when clicked.

Click this link to login with your Facebook account.

You can also use `anvil.facebook.auth.login()` to present a simple login dialog for only Facebook login. If you use `anvil.facebook.auth.login()`, your users’ login details are not stored in Anvil’s Data Tables.

## [Next up](#next-up)

The Microsoft and Google services allow user management with Microsoft and Google Single-Sign-On services in a very similar way.

They also provide integration with Google and Microsoft Azure REST APIs, plus Python bindings for Google Drive and Gmail.
