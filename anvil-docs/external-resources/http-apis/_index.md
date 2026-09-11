---
document: "HTTP APIs"
title: "HTTP APIs"
url: "/docs/external-resources/http-apis"
doc-id: http-apis-_index
state: Live
date-created: 2026-09-08
---


# [HTTP APIs](#http-apis)

You don’t need to make HTTP requests to build an Anvil app thanks to Anvil’s ability to call Python functions between client and server code (including [code outside of Anvil](/docs/uplink)). Even if you’re collaborating with a third-party, they can use the [Client Uplink](/docs/uplink/uplink_security) to safely make function calls to and from your app.

That said, HTTP is still a powerful tool to have available. Anvil has an [HTTP requests library](http-apis/making-http-requests), plus a simple way to [create HTTP endpoints](http-apis/creating-http-endpoints) that expose your app’s functionality over HTTP. Check the [Making HTTP requests](http-apis/making-http-requests/quickstart) and [Creating HTTP endpoints](http-apis/creating-http-endpoints/quickstart) quickstarts to get up and running.

## [Making HTTP Requests](#making-http-requests)

You can make HTTP requests from server code by using the `requests` library.

You can [install the `requests` library](/docs/server/custom-packages#adding-packages) from the **Python version** section of the App Settings. Alternatively, it’s already included on the Standard, Data Science and Machine Learning [base environments](/docs/server/custom-packages#available-base-environments).

```python
import requests
resp = requests.get("https://api.mysite.com/foo")
print(resp.json())
```

For any requests that will run from client-side code, Anvil has a human-friendly Python library for making HTTP requests.

```python
import anvil.http
resp = anvil.http.request("https://api.mysite.com/foo")
print(f"Response MIME type: {resp.content_type}")
```

See [Making HTTP Requests](http-apis/making-http-requests) for details.

## [Creating HTTP APIs](#creating-http-apis)

You can make your server functions into HTTP endpoints using a decorator:

```python
import anvil.server

@anvil.server.route("/users/:id")
def get_user(id):
  ip = anvil.server.request.remote_address
  return f"You requested user {id} from IP {ip}"
```

See [Creating HTTP Endpoints](http-apis/creating-http-endpoints) for details.
