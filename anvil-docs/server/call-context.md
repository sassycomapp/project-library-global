---
title: "Call Context"
url: "/docs/server/call-context"
doc-id: call-context
state: Live
date-created: 2026-09-08
---


# [Call Context](#call-context)

Call context provides information about where your code is running and where it was called from.

The [`anvil.server.context` object](/docs/api/anvil.server#context) provides this information.

## [Where your code is running](#where-your-code-is-running)

To check where your code is running, call `anvil.server.context.type`. For example:

```python
if anvil.server.context.type == 'uplink':
  # We're on the Uplink, so connect to Anvil.
  anvil.server.connect("<my-app-key>")
```

## [Client information](#client-information)

Client information tells you about how the user is accessing your app – whether from a [web browser](../client), an [HTTP endpoint](../http-apis), an [incoming email](../email), or an [Uplink script](../uplink).

The `anvil.server.context.client` object tells you about that client, including its `type` (one of `"browser"`, `"http"`, `"email"`, `"uplink"`, `"client_uplink"` or `"background_task"`).

For browsers and HTTP addresses, you can also find the IP address (`client.ip`), and a geographical location estimated from that IP (`client.location`).

`client` is `None` when executing in the browser, or when executing on an Uplink but *not* as part of a server function. (In this situation, this code *is* the client!)

## [Remote caller](#remote-caller)

It’s also sometimes important to know how the current server function was called. For example, code in the web browser is [not trustworthy](../security#client-vs-server-code), so it could pass us malicious arguments. `anvil.server.context.remote_caller` tells us about how this server function was called.

`remote_caller.is_trusted` is a boolean value that tells us whether we were called from trusted code – that is, a server module, background task or uplink.

`remote_caller.type` tells us exactly what type of code or event triggered this call (can be `"browser"`, `"server_module"`, `"http"`, `"email"`, `"uplink"`, `"client_uplink"` or `"background_task"`).

`remote_caller` is `None` when executing in the browser, or when executing on an Uplink but *not* as part of a server function. (This code was not called from anywhere!)
