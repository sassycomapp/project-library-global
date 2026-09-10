---
title: "Loading Indicator"
url: "/docs/client/adding-ui-elements/loading-indicator"
doc-id: loading-indicator
state: Live
date-created: 2026-09-08
---


# [Loading Indicator](#loading-indicator)

A loading indicator is displayed when your app is retrieving data. This stops users from being able to interact with your app while the server returns data.

## [Starting and stopping the indicator manually](#starting-and-stopping-the-indicator-manually)

To start or stop the indicator manually, start by creating an instance of the loading indicator using [`loading_indicator()`](/docs/api/anvil.server#loading_indicator), and then call `start()` or `stop()` as needed:

```python
from time import sleep

# Create an instance of the loading spinner and store it in a variable
self.loading_indicator = anvil.server.loading_indicator()

# Start and stop the indicator however you wish
self.loading_indicator.start()
sleep(5)
self.loading_indicator.stop()
```

Here’s a clone link to an example app that demonstrates the behaviour:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:KJXHMSTHPCHR63PX%3dGTC3LX6WO4DHGUWI4IHZEWO3)

## [Loading indicators for individual components](#loading-indicators-for-individual-components)

In some cases, you might want to use a loading indicator to temporarily block user interaction with a specific [component](https://anvil.works/docs/ui/components) or [container](https://anvil.works/docs/ui/components/containers).

You can do this using a [`with` statement](https://docs.python.org/3/reference/compound_stmts.html#with) which calls [`anvil.server.loading_indicator`](/docs/api/anvil.server#loading_indicator). `anvil.server.loading_indicator()` can take a component as an argument, so you can use it within a block like the one below to display an indicator over that component:

```python
"""An example function which overlays a indicator on top of the
card_1 component and stops users being able to interact with it"""
def overlay_indicator_on_card_1(self, **event_args):
    # This block takes the component we want to overlay a indicator onto
    # and keeps the indicator there until the inner code is executed
    with anvil.server.loading_indicator(self.card_1):
        anvil.server.call('my_server_function')
```

Note that while you’re in a `with anvil.loading_indicator` block, server calls will not trigger the global loading indicator.

Here’s a clone link to an example app that demonstrates using indicators for individual components:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:YLF4IUOSVHHZGYCT%3dAWRSLNDH354TWIRVU7YYDDIR)

## [Minimum height](#minimum-height)

When creating an instance of the loading indicator, you can define its minimum height with the `min_height` argument:

```python
def start_large_indicator_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    with anvil.server.loading_indicator(self.outlined_card, min_height="50vh"):
        anvil.server.call('foo')
```

Here’s a clone link to an example app that demonstrates the behaviour:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:RQDPDVRSD7HQT3XS%3d7C7VL77U4SNXO2D2T4VJYD4H)

## [Customising and styling the loading indicator](#customising-and-styling-the-loading-indicator)

For information on changing and/or styling the default loading indicator, see the UI [styling documentation](https://anvil.works/docs/client/customisation/using-css/loading_indicator).
