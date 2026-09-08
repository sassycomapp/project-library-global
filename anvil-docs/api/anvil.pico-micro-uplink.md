---
title: "anvil.pico (micro-uplink)"
url: "/docs/api/anvil.pico-micro-uplink"
---


## `anvil.pico [micro-uplink]` Module

#### Functions

[`call`](#call) [`callable`](#callable) [`callable_async`](#callable_async) [`connect`](#connect)

## Functions

#### `call(function_name, *args, **kwargs)` [(more info)](/pico)

-   `function_name` - The name of the server function, as registered with @anvil.server.callable (or @anvil.pico.callable on another Pico device).

-   `args` - All arguments will be passed to that function

-   `kwargs` - Keyword arguments will be passed to that function

---

#### `callable([require_user=False])` [(more info)](/pico)

-   `require_user` - If require_user=True, this function can only be called from a session with an authenticated user via the Users Service. If require_user is set to a string, this function can only be called if the user with the specified email is logged in via the Users Service.

---

#### `callable_async([require_user=False])` [(more info)](/pico/advanced#async)

-   `require_user` - If require_user=True, this function can only be called from a session with an authenticated user via the Users Service. If require_user is set to a string, this function can only be called if the user with the specified email is logged in via the Users Service.

---

#### `connect(key, [on_first_connect=None], [on_every_connect=None], [no_led=False])` [(more info)](/pico)

Connect your Pico to your Anvil app. This function will block forever: register all @anvil.pico.callable functions beforehand.

The key is a unique string and should be kept private. You can generate a new key from inside your anvil app.

-   `on_first_connect` - If you pass an async task as the on_first_connect keyword parameter, it will be called after the uplink connection is first established.

-   `on_every_connect` - If you pass an async task as the on_first_connect keyword parameter, it will be called after the uplink connection is established or reconnected.

-   `no_led` - If set to True, the Uplink will not display connection status on the on-board LED.
