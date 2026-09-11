---
document: "Uplink for Pico W"
title: "Uplink for Pico W"
url: "/docs/external-resources/uplink/pico"
doc-id: pico
state: Live
date-created: 2026-09-08
---


# [Create Internet-Connected Gadgets with Anvil and the Pico W](#create-internet-connected-gadgets-with-anvil-and-the-pico-w)

The [Raspberry Pi Pico W](https://www.raspberrypi.com/news/raspberry-pi-pico-w-your-6-iot-platform) is a $6 microcontroller board with on-board WiFi. Anvil supports connecting the Pico to your Anvil apps via a cut-down version of the Uplink, that runs in [MicroPython](https://micropython.org/).

Find more tutorials and resources for building IoT devices with the Pico and Anvil [here](/pico).

## [Quickstart](#quickstart)

Get started with the Pico W by following the [Getting Started](/pico/get-started) tutorial.

## [The Anvil Pico W Firmware](#the-anvil-pico-w-firmware)

There is an [official Anvil build of MicroPython](https://github.com/anvil-works/anvil-pico/releases), which includes everything you need to get started with Anvil on the Pico W - including many of the [Pimoroni libraries](https://github.com/pimoroni/pimoroni-pico).

The Getting Started tutorial contains all the steps you need to get going, and this page describes how to use Anvil from your Pico W with the official Anvil Pico W firmware installed.

## [Connecting to your Pico W](#connecting-to-your-pico-w)

The Anvil Pico W firmware configures your Pico W to appear as a Mass Storage device when connected to your computer via USB. There are two files on this volume by default:

-   `boot.py` runs when the Pico W is powered up. In our firmware, this takes care of connecting to Wifi, so you will need to enter your Wifi credentials in this file.
-   `main.py` runs after `boot.py`, and is the main entrypoint for your app. In our firmware, this file contains a sample Anvil Uplink script by default. You should replace this will the code for your app.

## [Differences from the Anvil Uplink](#differences-from-the-anvil-uplink)

The standard [Anvil Uplink](/docs/uplink) library is designed to run in full Python on a computer running Windows, OS X, or Linux, such as your laptop or a Raspberry Pi. The Pico W is a microcontroller without any operating system, so only a subset of the full Uplink functionality is available. To make the distinction clear, you import `anvil.pico` instead of `anvil.server`. The behaviour of most `anvil.pico` functions does not exactly match those in `anvil.server`. As MicroPython does not support threading (yet!), we make use of [`asyncio`](https://docs.python.org/3/library/asyncio.html) to run multiple tasks at once. Note that in MicroPython, this is imported with `import uasyncio`.

As with `anvil.server`, you call `anvil.pico.connect` to make an initial connection to the Anvil server, and then `anvil.pico.call` to call server functions in your app. You can also decorate your functions on the Pico W with `anvil.pico.callable` if you want to call them from your Anvil app on the web (although you should probably use `anvil.pico.callable_async` - see below).

Only certain Python values can be passed to and from functions in MicroPython. See [below](#passing-values-to-and-from-micropython) for details.

## [Connecting to Anvil from MicroPython](#connecting-to-anvil-from-micropython)

Call `anvil.pico.connect` in `main.py` to connect to your Anvil app, providing your Uplink key as an argument:

```python
import anvil.pico

anvil.pico.connect("<UPLINK-KEY>")
```

In order to connect to Anvil, the Real Time Clock (RTC) on your Pico W must be set correctly. This is done for you in `boot.py` of the official Anvil Pico W firmware, using `ntptime.settime()`. If necessary, you can set the RTC manually yourself using [the `machine.RTC().datetime(...)` function](https://docs.micropython.org/en/latest/library/machine.RTC.html?highlight=rtc#machine.RTC.datetime).

Unlike in the full Uplink library, the `anvil.pico.connect` function blocks forever, running `asyncio` tasks in the background to execute your Pico W program while also listening for function calls from your Anvil app.

To run your own program as well as connecting to Anvil, you can pass coroutines to `anvil.pico.connect` via the `on_first_connect` and/or `on_every_connect` keyword arguments:

```python
import anvil.pico
import uasyncio
from machine import Pin

led = Pin("LED", Pin.OUT, value=0)

# Blink the LED forever
async def my_program():
    while True:
        led.toggle()
        uasyncio.sleep(0.5)

anvil.pico.connect("<UPLINK-KEY>", on_first_connect=my_program())
```

Alternatively, if you want full control over the `asyncio` event loop, you can call `anvil.pico.connect_async` instead. This will do nothing on its own, but returns an `asyncio` coroutine for you to run manually:

```python
import anvil.pico
import uasyncio

async def my_program():
    anvil = anvil.pico.connect("<UPLINK-KEY>")

    uasyncio.create_task(anvil)

    # ... your code here ...

uasyncio.run(my_program())
```

## [Defining callable functions in MicroPython](#defining-callable-functions-in-micropython)

Use the `anvil.pico.callable_async` decorator to make your local async functions on the Pico W callable from your Anvil app:

```python
import anvil.pico

@anvil.pico.callable_async
async def pico_fn():
    return 42

anvil.pico.connect("<UPLINK-KEY>")
```

Providing an async function definition allows the Anvil connection to be maintained in the background, meaning you can make further calls to `anvil.pico.call` from inside the function if necessary. It is possible to mark plain functions as `anvil.pico.callable`, but be aware that these functions will have exclusive access to the microcontroller until they return, so further messages from the Anvil server will not be received in the meantime. We strongly recommend you use `callable_async` instead.

The `anvil.pico.callable_async` decorator supports the same arguments and keyword arguments as [`anvil.server.callable`](/docs/server#calling-server-functions-from-client-code). You can customise the name of the callable function, and require the user to be [logged in](/docs/users) in order to call the function. The [`anvil.users` package](/docs/users) is not available in MicroPython, so `await anvil.pico.get_user_email()` to get the email address of the currently-logged-in user (or `None` if the caller is not logged in).

```python
import anvil.pico

@anvil.pico.callable_async("my_pico_fn", require_user=True)
async def pico_fn():
    print(f"pico_fn called by {await anvil.pico.get_user_email()}")
    return 42

anvil.pico.connect("<UPLINK-KEY>")
```

## [Calling server functions from MicroPython](#calling-server-functions-from-micropython)

Functions defined in an Anvil server module can be made callable from the Pico W in the standard way: by adding the `@anvil.server.callable` decorator:

```python
@anvil.server.callable
def my_server_function(arg):
    return arg
```

Use `anvil.pico.call` to call server functions in your Anvil app from the Pico W. This is an async function, so must be awaited:

```python
import anvil.pico

async def my_program():
    x = await anvil.pico.call("my_server_function", 42)

anvil.pico.connect("<UPLINK-KEY>", on_first_connect=my_program())
```

## [Passing values to and from MicroPython](#passing-values-to-and-from-micropython)

You can only pass simple, literal values to and from server functions defined in MicroPython. Anything that can be trivially encoded as JSON will work; rich objects will not. In particular, you cannot pass or return database rows, [Portable Classes](/docs/server/portable-classes), or [Media objects](/docs/working-with-files/media).

## [Troubleshooting](#troubleshooting)

Sometimes after loading the Anvil firmware onto your Pico W and reconnecting it to your computer, the USB mass storage device fails to show up. When that happens we have found that fully wiping the Pico W flash memory and then reloading the Anvil firmware can fix the problem. See the [section on resetting your flash memory in the Raspberry Pi Pico docs](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#resetting-flash-memory) for instructions.
