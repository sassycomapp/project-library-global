---
title: "anvil.script"
url: "/docs/api/anvil.script"
---


## `anvil.script` Module

#### Globals

[`args`](#args) [`return_value`](#return_value)

## Globals

#### `args`

The positional arguments this script was launched with (also available as sys.argv[1:], except that Media arguments appear in sys.argv as the names of temporary files containing their content).

---

#### `return_value`

Set this from your script to return a value to anvil.server.run_script(). Defaults to None.
