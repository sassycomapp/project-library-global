---
title: "Calling functions remotely"
url: "/docs/external-resources/uplink/calling-functions-remotely"
---


# [Calling functions remotely](#calling-functions-remotely)

You can use the Uplink to call functions on your own machine—or anywhere else, like a cloud server or IoT device. You can also call functions in your Anvil Server Modules from these external scripts.

## [Anvil -> your machine](#anvil---your-machine)

To use the Anvil Uplink library in your Python project, first run `pip install anvil-uplink` on your machine.

Your local Python code can now do anything a [Server Module](/docs/server) can do.

Mark functions with `@anvil.server.callable` if you want to call them from your app.

```python
# In a script on your own machine (or anywhere)

import anvil.server
anvil.server.connect("<your Server Uplink key>")

@anvil.server.callable
def get_file():
  # Return a file from this local machine
  return anvil.media.from_file("./image.jpg", "image/jpeg")

anvil.server.wait_forever()
```

If you connect multiple uplink programs that contain the same function name to the same app, then calls can be received by either uplink program.

## [Your machine -> Anvil](#your-machine---anvil)

You can also call functions in your Anvil Server Modules from your uplinked code. This makes the Uplink a two-way connection: your app can run code on your machine, and your machine can call back into your app.

```python
# This is a simple program that makes a call to a server module.
import anvil.server

anvil.server.connect("<your Uplink key>")

anvil.server.call("store_number", 42)
```

This example does not register any `@anvil.server.callable` functions, and exits as soon as the call to `store_number` returns.
