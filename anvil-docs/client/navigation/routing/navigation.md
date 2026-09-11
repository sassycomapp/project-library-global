---
document: "Navigation"
title: "Navigation"
url: "/docs/client/navigation/routing/navigation"
doc-id: navigation
state: Live
date-created: 2026-09-08
---


# [Navigation](#navigation)

To provide navigation, the Routing dependency needs to be given instructions on which Form should be opened based on which URL has been navigated to. This is done by definining routes which are then used by the router to interpret given URLs.

## [Routes](#routes)

Routes are subclasses of the Routing dependency’s `Route` class. They link URL addresses and Anvil Forms, allowing the [router module](/docs/client/navigation/routing/router) to serve the appropriate Form based on a given URL. They are mostly centered around two attributes:

-   `path` – The URL path for the Route (excluding [your app’s base URL](/docs/deployment/choosing-urls#choosing-your-apps-url)). When navigating to a new path, the router module attempts to find a Route whose path matches the path in the browser’s URL.
-   `form` – The name of the Form this Route opens when matched.
    
    ```python
    from routing.router import Route
    
    class MyRoute(Route):
      path = "/"
      form = "MyForm"
    ```

There are other attributes that you can define, all of which can be found in the [full route documentation](https://routing-docs.anvil.works/routes/#route-attributes).

## [Routes module](#routes-module)

Routes should be defined in a dedicated [Module](/docs/client/modules). This Module then needs to be imported by both the Module responsible for launching the router and by [server code](/docs/server), for them to be aware of our Route definitions. This process is demonstrated [here](/docs/client/navigation/routing/quickstart#importing-our-route-definitions).

One thing to note is that the router will try to match routes in the order they are defined; when receiving a path, the router goes through the route definitions in order, meaning that if two routes match the same path, the one that was defined earlier will be matched.

```python
from routing.router import Route

class NewerRoute(Route):
    path="/my-route"
    form = "NewerForm"

class DeprecatedRoute(Route):
    path = "/my-route"
    form = "DeprecatedForm"
```

In the above example, `NewerRoute` is defined before `DeprecatedRoute`. Navigation to the `"/my-route"` path will thus match with `NewerRoute` instead of `DeprecatedRoute` and open an instance of `NewerForm` rather than `DeprecatedForm`.

This is particularly important to keep in mind when defining routes with [parameters](/docs/client/navigation/routing/parameters).

```python
from routing.router import Route

class AuthorsRoute(Route):
    path = "/authors"
    form = "Pages.Authors"

class NewAuthorRoute(Route):
    path = "/authors/new"
    form = "Pages.NewAuthor"

class AuthorRoute(Route):
    path = "/authors/:id"
    form = "Pages.Author"
```

With the above Route definitions, if we were to navigate to “authors/new”, the router’s first match would be `NewAuthorRoute`, which is what we intended.

Let’s look at what would happen if we were to swap the order of the `NewAuthorRoute` and `AuthorRoute` definitions.

```python
from routing.router import Route

class AuthorsRoute(Route):
    path = "/authors"
    form = "Pages.Authors"

class AuthorRoute(Route):
    path = "/authors/:id"
    form = "Pages.Author"

class NewAuthorRoute(Route):
    path = "/authors/new"
    form = "Pages.NewAuthor"
```

With this order, if we were to navigate to “authors/new”, the router’s first match would not be `NewAuthorRoute`, but `AuthorRoute`; because `AuthorRoute` is defined first, the “new” part of our path is seen as a value for the `id` parameter. This means that we never end up reaching our `NewAuthorRoute`.

## [NavLinks](#navlinks)

The Routing dependency comes with its own NavLink component to enable navigation through your various routes.

NavLinks must be given a `path` attribute. When a NavLink is clicked, the Routing library sets the browser URL to the NavLink’s `path`. The router module will then attempt to find a route to match this path. If a match is found, the router module will open the Form associated with this route.

## [The navigate method](#the-navigate-method)

Alternatively, the [navigate method](https://routing-docs.anvil.works/navigating/#navigating-with-navigate) can be used to access a route through code. It functions the same way NavLinks do, allowing you to supply a path and other parameters as keyword arguments.

```python
import anvil.users
from routing.router import navigate

class MyForm(MyFormTemplate)
  def __init__(self, **properties):
    super().__init__(**properties)

  def on_user_log_out(self, **event_args):
    # This form has a log out button, to which we have added this method as a handler of its Click event.
    # When the log out button is clicked, we log the user out and navigate them to the login page.
    anvil.users.logout()
    navigate(path="/login-page")
```

You can find more details on the `navigate` method in its [documentation page](https://routing-docs.anvil.works/navigating/#navigating-with-navigate).

## [Redirects](#redirects)

You can redirect to a different route by raising a `Redirect` exception in a route’s `before_load` method.

```python
from routing.router import Route, Redirect

class IndexRoute(Route):
    path = "/"

    def before_load(self, **loader_args):
        raise Redirect(path="/dashboard")
```

In the above example, the user will be redirected to the `/dashboard` route when they navigate to your app.

A common use case for redirecting is to ensure that a user is logged in before navigating to a route.

```python
from routing.router import Route, Redirect
import anvil.users

class IndexRoute(Route):
    path = "/"

    def before_load(self, **loader_args):
        if anvil.users.get_user():
            raise Redirect(path="/dashboard")
        else:
            raise Redirect(path="/login")
```

A determined user will be able to bypass the redirect by opening the form directly. Always ensure you check the user is logged in on the server before sending sensitive data to the client.
