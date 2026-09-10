---
title: "Caching"
url: "/docs/client/navigation/routing/caching"
doc-id: caching
state: Live
date-created: 2026-09-08
---


# [Caching](#caching)

Routing allows two different types of caching: [Form](/docs/ui/forms) caching, and data caching. Both types involve storing Python object instances in a dictionary contained within the [router](/docs/client/navigation/routing/router) for later access.

## [Form caching](#form-caching)

When a [Route](/docs/client/navigation/routing/navigation#routes) with Form caching enabled is navigated to for the first time, it instantiates its Form and caches that instance for later navigations to this Route. Were Form caching not enabled, a new instance of the Form would be re-created every time the Route is navigated to.

By default, Form caching is disabled. To enable it, you must set the `cache_form` flag to `True` in an individual Route’s definition.

```python
class MyRouteWithFormCaching(Route):

    path = '/with-form-caching'
    form = 'FormToBeCached'

    cache_form = True
```

## [Invalidation](#invalidation)

The cache is automatically emptied after 30 minutes. This time can be changed by adjusting the `gc_time` attribute when defining your Route.

```python
class MyRouteWithFastGarbageCollection(Route):

    path = '/with-fast-garbage-collection'
    form = 'FormWithFastGarbageCollection'

    gc_time = 1 * 60 # gc_time is measured in seconds
```

You can also flush the cache manually in code by calling either the [`clear_cache` function](https://routing-docs.anvil.works/caching/#clearing-cache), which will flush the entire cache of your app, or the [`invalidate` function](https://routing-docs.anvil.works/caching/#invalidating-cache), if you only wish to clear the cache related to a specific path.

## [Data loading](#data-loading)

Under the hood, the Form opening process starts on the server. If we need to make a [server call](/docs/server#calling-server-functions-from-client-code) to fetch data for our Form upon initialization, we are basically doing a round trip between server and client, which is slower than ideal.

Routes have a `load_data` method, which is part of the navigation process. It is called before the Form is opened on the client browser.

By overriding a Route’s `load_data` method, you can execute code (including server calls) before the Form even reaches the client’s browser, preventing the round trip and speeding up the process.

```python
class MyRouteWithDataLoading(Route):

    path = '/with-data-loading'
    form = 'FormThatNeedsToLoadData'

    def load_data(self, **loader_args):
        # Perform all your data loading operations here
```

When opening a Form via router navigation, Forms are given a [`RoutingContext` object](https://routing-docs.anvil.works/routing-context/) as a keyword argument to their `__init__` function. You can retrieve the `load_data` method’s result from the `RoutingContext` object’s `data` attribute.

```python
class FormThatNeedsToLoadData(FormThatNeedsToLoadDataTemplate):

    def __init__(self, routing_context=None, **properties):

        self.routing_context = routing_context
        properties["item"] = routing_context.data

        super().__init__(**properties)
```

Unless Form caching is enabled and an instance of the Form is available in the cache, the entire data loading process happens every time the Route is navigated to. If we wish to cache the result of the data loading process but not the Form instance itself, we can enable data caching.

## [Data caching](#data-caching)

Data caching functions just as Form caching does. It lets you keep the data loaded on first opening, that is to say the result of the `load_data` method, in a cache for later use.

This can be done by setting a Route’s `cache_data` attribute to `True`.

```python
class MyRouteWithDataCaching(Route):

    path = '/with-data-caching'
    form = 'FormWithDataToBeCached'

    cache_data = True
```

Just like Form caches, data caches will be flushed once the duration set in the Route’s `gc_time` has passed or when invalidated is called on this Route’s path.

Keep in mind that, if you have Form caching enabled, data caching is redundant, as the data loading process is skipped in case a Form instance is available in cache.

## [How it works](#how-it-works)

The Routing dependency’s cache is composed of two Python dictionaries, one for Forms and one for data.

When a Route is navigated to for the first time and caching is enabled for this Route, the router module stores the created object in the appropriate dictionary under a **caching key**.

This caching key is a `string` object, built from two parts joined by a `:` character:

-   The path that is being navigated to
-   The matched Route’s [cache dependencies](/docs/client/navigation/routing/parameters#cache-dependencies)

By default, cache dependencies are only relevant in the context of [query parameters](/docs/client/navigation/routing/parameters#query). You can continue reading this section without having gone through the parameters section first. For more information, see [cache dependencies](/docs/client/navigation/routing/parameters#cache-dependencies).

For example, if we were to open the following path:  
`/my-page?show-side-panel=true`  
The caching key generated by the router module would be:  
`/my-page:{"show-side-panel": true}`

It helps to think of caching keys as unique identifiers for your app’s pages.

Let’s look at a more extensive example.

Say we have the following route for a profile page that displays the profile of different users.

```python
from routing.router import Route
import anvil.server

class Profile(Route):
    cache_form = True
    cache_data = True
    path = "/my-app/profiles/:user-id
    form = "Profile"

    def load_data(self, **loader_args):
        return anvil.server.call(
            'get_user_data',
            loader_args['routing_context'].params['user-id']
        )
```

We add a `user-id` [parameter](/docs/client/navigation/routing/parameters) to our path, so that this Route can be matched for multiple user profiles. This parameter is used to populate the `Profile` form with the data associated to the requested user ID.

If we have two users registered, User 1 and User 2, we basically have two pages associated with this route, each with their own URL:

-   `/my-app/profiles/user-1`
-   `/my-app/profiles/user-2`

When navigating to `/my-app/profiles/user-1`, the Form instance and its loaded data will be cached under the following caching key:

`/my-app/profiles/user-1:{}`

These cached objects are only relevant for User 1, and we don’t want the router module to fetch these cached objects when requesting to view User 2’s profile page.

When navigating to `/my-app/profiles/user-2`, the router module generates the following caching key:

`/my-app/profiles/user-2:{}`

Since this key is different from the one generated when navigating to `/my-app/profiles/user-1`, opening User 2’s page will not retrieve User 1’s content. It will instead either fetch whatever is stored under this different key or create new instances and store them under it for later use.
