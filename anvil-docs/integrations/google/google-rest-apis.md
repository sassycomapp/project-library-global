---
title: "Google REST APIs"
url: "/docs/integrations/google/google-rest-apis"
---


# [Google REST APIs](#google-rest-apis)

You might want to use one of Google’s REST APIs directly. To do this, you will need a Google API Client ID from the Google Developer Console - see [Linking Anvil and Google](linking-google-and-anvil) for full instructions.

To request additional OAuth scopes, call `anvil.google.auth.login()` with a list of scope names. In this case we are requesting the ability to read the user’s Gmail inbox with the [Gmail API](https://developers.google.com/gmail/api/).

```python
# Log in and request access to a user's mailbox
anvil.google.auth.login(["https://www.googleapis.com/auth/gmail.readonly"])
```

Once logged in, you can get an access token for the current user’s session by calling [`anvil.google.auth.get_user_access_token()`](/docs/api/anvil.google.auth#get_user_access_token). This token is a string, and you can use it to make requests to the Google REST API. In this example, we are getting a list of threads in the user’s inbox using the [Gmail API](https://developers.google.com/gmail/api/).

```python
access_token = anvil.google.auth.get_user_access_token()

email_threads = anvil.http.request(
    "https://www.googleapis.com/gmail/v1/users/me/threads",
    json=True, headers={
      'Authorization':
        'Bearer ' + access_token
    })
```

Access tokens expire within a short period of time (typically less than an hour). If you want to retain access after this time, you need to store a refresh token. This refresh token can be converted into an access token later by calling `anvil.google.auth.refresh_access_token()`.

```python
refresh_token = anvil.google.auth.get_user_refresh_token()

# ... some time later ...

access_token = anvil.google.auth.refresh_access_token(refresh_token)
```
