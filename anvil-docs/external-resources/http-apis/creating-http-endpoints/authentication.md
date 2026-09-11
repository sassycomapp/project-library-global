---
document: "Authentication"
title: "Authentication"
url: "/docs/external-resources/http-apis/creating-http-endpoints/authentication"
doc-id: authentication
state: Live
date-created: 2026-09-08
---


# [Authentication in HTTP Endpoints](#authentication-in-http-endpoints)

## [Authenticating using the Users Service](#authenticating-using-the-users-service)

The `@anvil.server.route` decorator accepts the optional keyword argument `authenticate_users` (default `False`).

If this is set to `True`, it will automatically authenticate users against the Users Service in your app using HTTP Basic Authentication. The username and password are the same as the user would enter into the [Users Service login form](/docs/users/presenting-a-login-form).

If the user visits the endpoint in a web browser, it will present them with a login form.

Commandline HTTP tools often have convenient means to supply credentials for HTTP Basic Authentication, for example `curl`:

```python
curl -u user123@gmail.com:mySuperS3cretPassw0rd https://your-app.anvil.app/_/api/users/42
```

You can get the logged-in user from the `Users` table using `anvil.server.request.user`. Of course, you can also retrieve the logged-in user with the usual `anvil.users.get_user()` mechanism.

If authentication fails, a `401 Unauthorized` response will be sent back automatically.

```python
import anvil.server
from anvil.server import request

@anvil.server.route("/protected", authenticate_users=True)
def serve_protected_content():
  print(f"Authenticated {request.user['email']}, who signed up on {request.user['signed_up']}.")

  # User is now authenticated.
```

## [Checking credentials yourself](#checking-credentials-yourself)

The `@anvil.server.route` decorator accepts the optional keyword argument `require_credentials` (default `False`).

If this is set to `True`, remote users must provide a username and password through HTTP Basic Authentication ([as above](#authenticating-using-the-users-service)).

If credentials are not provided, a `401 Unauthorized` response will be sent back automatically.

Unlike with the `authenticate_users` option, **it is your responsibility to check the provided username and password** and return an appropriate response if the validation fails.

```python
from anvil.server import route, request

@route("/protected", require_credentials=True)
def serve_protected_content():
  print(f"User {request.username} connected with password {request.password}")

  # Check username and password before continuing...
```
