---
title: "Cross-site Security"
url: "/docs/external-resources/http-apis/creating-http-endpoints/security-cross-site"
---


# [Security and cross-site sessions](#security-and-cross-site-sessions)

You should take care when writing HTTP endpoints. They are accessible to anyone on the internet, so you must be robust against malicious requests.

What’s more, it is often possible for an attacker to cause *legitimate, logged-in users of your app* to access HTTP endpoints in a way under an attacker’s control! If you’re not careful, this can cause your application to perform operations on the user’s behalf, but without their consent. This is called XSRF (Cross-Site Request Forgery).

### External requests to HTTP endpoints are in a dedicated session by default

Anvil protects your apps against XSRF by serving HTTP endpoints in a separate session from the rest of your app if they were triggered by a different website. Even if the browser that requests that endpoint has [cookies](/docs/server/sessions-and-cookies#cookies) or is logged in with the [Users service](/docs/users), they will not be available to the endpoint function if the request was triggered by a different site (ie if the `Origin` or `Referer` headers do not match your app).

### Turning that off

If you want to accept requests from other websites, you can turn off this protection, by passing `cross_site_session=True` to `@anvil.server.route()`. This will cause all requests to execute in the session of the browser they come from, whatever site initiated them.

If you do this, you need to write your endpoint to be safe in all circumstances - **even if it is called with a URL and parameters chosen by a malicious adversary**. Best practices for writing safe endpoints under these circumstances are more complex than we can go into here – search online for “XSRF” to learn more.
