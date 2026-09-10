---
title: "anvil.server (uplink)"
url: "/docs/api/anvil.server-uplink"
doc-id: anvil.server-uplink
state: Live
date-created: 2026-09-08
---


## `anvil.server [uplink]` Module

#### Functions

[`connect`](#connect) [`disconnect`](#disconnect) [`wait_forever`](#wait_forever)

## Functions

#### `connect(key, [url="wss://anvil.works/uplink"], [quiet=False], [init_session=None], [extra_headers=], [default_log_level="INFO"])` [(more info)](/docs/uplink)

Connect your uplink script to your anvil app.

-   `key` - The key is a unique string that should be kept private. You can generate a new key from within your Anvil app.

-   `url` - The URL of the Anvil uplink server endpoint. Override this if you are connecting to an Anvil Enterprise server or Anvil App Server.

-   `quiet` - Equivalent to default_log_level='WARNING'.

-   `init_session` - If you pass a function to the init_session keyword parameter, it will be called after the uplink connection is established but before any other interaction.

-   `extra_headers` - A dictionary of headers to send with each request. If you pass a function, it will be called before each request, and its dict return value used as the headers.

-   `default_log_level` - The log level to use for logging, unless overridden by the `quiet` parameter or the `ANVIL_LOG_LEVEL` environment variable. Can be one of `DEBUG`, `INFO`, `WARNING`, `ERROR` or `CRITICAL`.

---

#### `disconnect()`

Disconnect your uplink script from your anvil app. Your script is then free to call `anvil.server.connect()` with the same uplink key or a new uplink key.

---

#### `wait_forever()` [(more info)](/docs/uplink/setting_up#connecting)

A useful shortcut to keep your Python script running. This allows your app to `anvil.server.call` functions inside your Python script. You can use any other way to keep the process alive in place of this function.
