---
title: "anvil.tz"
url: "/docs/api/anvil.tz"
doc-id: anvil.tz
state: Live
date-created: 2026-09-08
---


## `anvil.tz` Module

#### Classes

[`tzlocal`](#tzlocal) [`tzoffset`](#tzoffset) [`tzutc`](#tzutc)

#### Globals

[`UTC`](#UTC)

## Classes

### `tzlocal`

Use the local timezone of the browser

##### Base class: anvil.tz.tzoffset

#### Constructor

`tzlocal()`

---

### `tzoffset`

Create a timezone with a specific offset. Use an offset in seconds, minutes or hours

#### Constructor

`tzoffset([seconds], [minutes], [hours])`

---

### `tzutc`

Create a timezone set to utc

##### Base class: anvil.tz.tzoffset

#### Constructor

`tzutc()`

---

## Globals

#### `UTC`

An object representing the UTC timezone
