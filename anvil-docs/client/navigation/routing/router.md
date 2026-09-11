---
document: "Router"
title: "Router"
url: "/docs/client/navigation/routing/router"
doc-id: router
state: Live
date-created: 2026-09-08
---


# [The Router Module](#the-router-module)

Most of the Routing dependency is contained in its **router module**.

In addition to holding the definitions of all Python objects required for the dependency to work, the router module is responsible for navigating to Forms, storing content in its cache dictionaries as requested by [Route objects](/docs/client/navigation/routing/navigation#routes), and, in general, serving all of the Routing dependency’s features.

## [Launching the router](#launching-the-router)

Because the router module takes care of opening Forms, it should be initialized as soon as the app is opened. The router is initialized by calling the router’s `launch` method.

```python
from routing.router import launch

launch()
```

This should be done in your app’s [startup Form or Module](/docs/ui/forms#the-startup-form). Because the router handles opening Forms, we recommend using a [Module](/docs/client/modules) rather than a Form.

Once launched, the router will keep track of URL changes and navigation requests.

## [Routing process](#routing-process)

Navigation in an Anvil app with Routing enabled follows the same routing process each time, handled by the router module.

The routing process is always kickstarted by a **navigation request**. Depending on the request’s origin, the process occurs either client-side or server-side.

-   If the navigation request originates from a running instance of the app, the routing process occurs **client-side**.
-   If the app is opened directly through a URL as the initial page request, the routing process occurs **server-side**.

The primary component of navigation requests is the **path**, where within the app we should navigate to. The path is a `string` object that is meant to be added at the end of an [app’s URL](/docs/deployment/choosing-urls#choosing-your-apps-url). The resulting URL then points to a specific page or state of your app.

For example, a Route with the path `"/my-page"` in an app whose URL is `https://my-app.anvil.app` will be matched with when opening `https://my-app.anvil.app/my-page`.

Once the router module has received the navigation request with a new path, it opens the Form that is associated to this path based on the **Route object** it was able to match to the path.

Route objects are data structures which hold links between paths and Forms. More information about Route objects can be found [here](/docs/client/navigation/routing/navigation#routes).

## [Default app URL](#default-app-url)

Opening your app’s URL without any added path is the same as navigating to the `"/"` path. It therefore makes sense to link your homepage Form to the `"/"` path. More information on how to do that can be found in the [Route documentation](/docs/client/navigation/routing/navigation#routes), as well as in the [quickstart guide](/docs/client/navigation/routing/quickstart#setting-up-routes).

By default, clicking the IDE’s Run button will open your app’s URL without any path added. For testing purposes, you can configure the IDE’s Run button to navigate to a specific path on startup. You can do so by clicking on the three dots next to the “Run” button and selecting “Set startup URL…”.

Do note that this is only relevant when starting the app from the IDE.

## [Debugging the routing process](#debugging-the-routing-process)

If you need more insight into what is going on during the routing process in your app, you can set the router’s debug flag to `True`. You can do so by calling the router module’s `debug_logging` method.

```python
from routing.router import launch, debug_logging

debug_logging()
launch()
```

Doing so will enable debug logging, and the router module will print messages in the app console, detailing every step of the routing process.
