---
document: "Creating HTTP APIs"
title: "Creating HTTP APIs"
url: "/docs/external-resources/http-apis/creating-http-endpoints"
doc-id: creating-http-endpoints-_index
state: Live
date-created: 2026-09-08
---


# [Creating HTTP APIs](#creating-http-apis)

You can build an HTTP API for your app by decorating server functions with the `@anvil.server.route` decorator.

You can use this to give your app a REST API that non-Anvil apps can use to interface with it, in situations where you can’t use the Uplink.

Before you build an HTTP interface for your app, consider using the [Uplink](/docs/uplink) instead. It lets you make any Python code behave like an Anvil Server Module.

If you want other people/organisations to interface with your app, they can still use the Uplink safely with the [Uplink client key](/docs/uplink/uplink_security).

## [The `route` decorator](#the-route-decorator)

The `@anvil.server.route` decorator makes your function callable over HTTP. It has one required argument - the path, e.g. `/users/list`.

```python
import anvil.server

@anvil.server.route("/users/list")
def get_user_list():
  return [u['email'] for u in app_tables.users.search()]
```

### Path parameters

You can think of URLs as having two parts: *origin* and *path*. Assume you have this URL:

```
https://<your-app-id>.anvil.app/users/1234
```

The *origin* is `https://<your-app-id>.anvil.app/`, this tells Anvil how to route requests to your app.

The *path* is `/users/1234`. This is what is passed into your `@anvil.server.route` functions.

The path may contain one or more **path parameters**, denoted by the **`:`** character, e.g. `/users/:id`.

```python
import anvil.server

@anvil.server.route("/users/:id")
def get_user(id):
  return f"You requested user {id}"
```

In the example above, if you navigate to `https://<your-app-id>.anvil.app/users/42`, you will receive a response of `You requested user 42`:

You can also use path parameters in the middle of a path (`/users/:id/history`) or use multiple path parameters in the same path (`/users/:user_id/history/:item_id`).

### Query strings

The query string is the part of the URL after the question mark (`?`), such as in this URL:

```
https://<your-app-id>.anvil.app/users/42?x=foo
```

It consists of key/value pairs `key=value`. If there are multiple key/value pairs, they are separated by `&`, for example `key1=value1&key2=value2`.

Query-string parameters will be passed to your function as keyword arguments. In this example, we use Python’s `**` notation to capture all query string parameters in the `params` variable:

```python
import anvil.server

@anvil.server.route("/users/:id")
def get_user(id, **params):
  return f"You requested user {id} with params {params}"
```

In the example above, if you navigate to `https://<my-app-id>.anvil.app/users/42?x=foo`, you will receive a response of `You requested user 42 with params {'x': 'foo'}`.

### Optional keyword arguments

To configure your HTTP endpoints more, `@anvil.server.route` takes some optional keyword arguments:

-   `methods` specifies which HTTP methods this endpoint supports (the default is `['GET','POST']`)
-   `enable_cors` adds CORS HTTP headers (`Access-Control-Allow-Origin: *`) to your response when set to `True`. By default, we set CORS headers to permit requests from any web address where your app can be reached (eg `xyz.anvil.app`, `my-custom-domain.com`, etc).
-   `cross_site_session` is described in [Cross-site Security](creating-http-endpoints/security-cross-site).
-   `require_credentials` and `authenticate_users` are described in [Authentication](creating-http-endpoints/authentication).

### Path restrictions

Your `route`s cannot respond to paths that begin with `/_/`. This prefix is reserved for internal Anvil use.

If your app contains a [Startup Form](../../client/forms/forms-in-the-editor#the-startup-form) or [Startup Module](../../client/client-code/modules#startup-module), then your `route`s cannot respond to the plain path `/`.

## [The `http_endpoint` decorator](#the-http_endpoint-decorator)

Anvil also supports decorating your functions with `@anvil.server.http_endpoint`. The `http_endpoint` decorator works the same as the `route` decorator, except that the path of the endpoints it defines are prefixed with `/_/api`. This can be useful for separating your machine-facing URLs from your human-facing URLs.

So, for example, if you define a function:

```python
@anvil.server.http_endpoint("/users/:id")
def get_user(id, **params):
  ...
```

…then that endpoint will be available at `https://<my-app>.anvil.app/_/api/users/42`.

`http_endpoint` endpoints cannot return [`FormResponse`](#formresponse-object)s.

## [Getting the URL for your API](#getting-the-url-for-your-api)

### Getting it manually

If your app is published, your API is at

```
https://<your-app>.anvil.app/...
```

or at

```
https://your-custom-domain.com/...
```

if you have a custom domain.

If your app is private, the endpoints will be at

```
https://<your-app-id>.anvil.app/<your private access key>/...
```

### Getting it automatically

Sometimes you will want to generate URLs that point to your HTTP endpoints without having to hard-code the origin of your app. Instead of writing:

`endpoint_url = "https://my-app.anvil.app/users"`

You can call [`anvil.server.get_app_origin()`](/docs/api/anvil.server#get_app_origin):

`endpoint_url = anvil.server.get_app_origin() + "/users"`

This has the advantage of returning whichever origin the user is currently connected on, i.e. if you have [published a version](/docs/version-control#published-vs-dev-versions) but you are running your development version in the Anvil editor, `get_api_origin()` will return a temporary private link to your development version, so you can test your APIs before publishing them!

If you’re running in the editor, `get_app_origin()` might return a URL that’s private or not permanent. To get the origin for the published version of your app, call `get_app_origin('published')`.

If you’re using a custom domain, `get_app_origin` will sometimes still return the `.anvil.app` domain, if it cannot verify the DNS settings for your custom domain.

If you wish to programmatically construct URLs containing your custom domain, hard-code a constant containing your custom domain and construct URLs from that.

## [The `request` object](#the-request-object)

HTTP requests have far more information associated with them than just path and query-string parameters. This information can be accessed through the `anvil.server.request` object, which is a global variable containing information about the request currently being processed.

```python
import anvil.server

@anvil.server.route("/users/:id")
def get_user(id):
  ip = anvil.server.request.remote_address
  return f"You requested user {id} from IP {ip}"
```

The request object has the following attributes:

-   **`path`** - The path of this HTTP request.
-   **`method`** - The method of this HTTP request, e.g. `GET`, `POST`, etc.
-   **`query_params`** - The query-string parameters passed with this request, as a dictionary.
-   **`form_params`** - The form parameters passed with this request, as a dictionary.
-   **`origin`** - The URL origin of this HTTP request.
-   **`headers`** - Headers passed with this request, as a dictionary.
-   **`remote_address`** - The IP address of the source of this request.
-   **`body`** - The body of this HTTP request, as an `anvil.Media` object.
-   **`body_json`** - For requests with `Content-Type: application/json`, this is the decoded body as a dictionary. Otherwise `None`.
-   **`username`** - For authenticated requests (see [Authentication](creating-http-endpoints/authentication)), returns the provided username. Otherwise `None`.
-   **`password`** - For authenticated requests (see [Authentication](creating-http-endpoints/authentication)), returns the provided password. Otherwise `None`.
-   **`user`** - For authenticated requests, returns the row from the `Users` table representing the authenticated user.

Technically, `anvil.server.request` is [thread-local](https://en.wikipedia.org/wiki/Thread-local_storage).

## [Returning a response](#returning-a-response)

Functions decorated with `@anvil.server.route` can return:

-   **Strings**: returned with a Content-Type of `text/plain`
-   **[Media Objects](/docs/working-with-files/media#media-objects)**: returned with their attached Content-Type
-   **JSON data**: any JSON-serializable object like a dict or list will be returned with Content-Type: `application/json`
-   **[HttpResponse object](#httpresponse-object)**: returns an HTTP Response object with status codes, custom headers, etc.
-   **[FormResponse object](#formresponse-object)**: will serve the client side of your app, loading the specified Form.

```python
import anvil.server

@anvil.server.http_endpoint("/foo")
def serve_content():
  # This response will have Content-Type application/json
  return {"key": "value"}
```

### HttpResponse object

If you need more control over the response, you can return an `anvil.server.HttpResponse` object ([API Docs](/docs/api/anvil.server#HttpResponse)), providing a custom status code and response body:

```python
import anvil.server

@anvil.server.route("/foo")
def serve_content(**p):
  return anvil.server.HttpResponse(200, "Body goes here")
```

These can be used for [all the standard HTTP response codes](https://www.tutorialspoint.com/http/http_responses.htm) that the browser expects.

For instance, here is a redirection response which causes the user’s browser to take them to a different webpage:

```python
import anvil.server

@anvil.server.route("/wikipedia")
def serve_content(**p):
  response = anvil.server.HttpResponse(302, "Redirecting to Wikipedia...")
  response.headers['Location'] = "https://www.wikipedia.org"
  return response
```

You can use this method to redirect users to another part of your app, after they have triggered some action by hitting a particular HTTP endpoint.

To add custom headers to your response, just add them to the `headers` dictionary, an attribute of the `HttpResponse` object.

### FormResponse object

If, instead of serving a raw HTTP response, you want to serve your app’s [user interface](../../client), you can return a `FormResponse` object. To create a `FormResponse`, pass the name of the target form, and any arguments.

For example:

```python
import anvil.server

@anvil.server.route("/my-page")
def serve_my_page(**p):
  # This assumes there is a form called MyPageForm in your app:
  return anvil.server.FormResponse('MyPageForm')
```

You can also pass additional arguments to the form’s constructor, by passing them to the `FormResponse` constructor. This works with both positional and keyword arguments.

For example, if you want `https://my-app.anvil.app/users/<email>` to serve the page for a user with that email address, you could do something like this:

```python
import anvil.server
from anvil.server import app_tables

# This code assumes there is "users" table in your app, and a
# form called UserPage that can display a row from that table

@anvil.server.route("/users/:email")
def serve_user_page(email, **p):
  user = app_tables.users.get(email=email)
  if user is not None:
    return anvil.server.FormResponse('UserPage', user=user)
  else:
    return anvil.server.HttpResponse(404, "No such user")
```

If you want to specify additional metadata or startup data with your app’s UI response, use an [`AppResponder`](#appresponder-object) object instead.

#### AppResponder object

The `AppResponder` class allows you to specify additional data and meta information to be sent along with your app’s UI response.

Most users will not need to use `AppResponder` directly. If you want dedicated UI routes in your app, use the [Routing module](/docs/client/navigation/routing).

Use `AppResponder` when you need to serve your app’s UI from a server-side HTTP endpoint with custom metadata or startup data.

An `AppResponder` object accepts two optional keyword arguments:

1.  `data`: Any serializable object (dict, list, string, etc.). This will be available to your client code at `anvil.server.startup_data`.
2.  `meta`: A dictionary of meta tag names and values. Common tags include: `"title"`, `"description"`, `"og:title"`, `"og:image"`.

If a `meta` value starts with `"asset:"`, it will be treated as a theme asset. For example, `"og:image": "asset:logo.png"` will use the logo.png asset from your app’s theme.

Any meta tags you specify will be injected into the `<head>` of the served page, allowing you to control elements such as the page title, description, and social-sharing previews.

##### AppResponder methods

Once you’ve created an `AppResponder`, you can load your app’s UI using one of these methods:

-   `load_form(form_name, *args, **kws)`: Serves the specified Form as your app’s UI. This is equivalent to returning a [`FormResponse`](#formresponse-object), but includes the additional `data` and `meta` you defined in the `AppResponder`.
-   `load_module(module_name)`: Serves the specified module as your app’s entry point instead of a Form. Useful if your app has a startup Module rather than a startup Form.
-   `load_app()`: Serves your app’s default startup Form or module.

Example:

```python
import anvil.server

@anvil.server.route("/custom")
def serve_custom(**p):
    responder = anvil.server.AppResponder(
        data={"user": "alice"},
        meta={
            "title": "Welcome Alice!",
            "description": "A custom page for Alice.",
            "og:image": "asset:logo.png",
        }
    )
    return responder.load_form("WelcomeForm")
```

This will serve the `WelcomeForm` UI and make `{ "user": "alice" }` available at `anvil.server.startup_data`. When sharing `https://<anvil-app-origin>/custom`, the preview will use logo.png from your app’s assets.

## [Testing HTTP endpoints](#testing-http-endpoints)

If you haven’t yet [published](../../deployment) your app (or if you’ve published a version that people are using), it’s useful to be able to test the HTTP endpoints of the version you’re developing.

To do this, use a [Development Environment](../../deployment/environments#development-environments) to get a private URL that refers to the version of your app you have open in the editor – a bit like the **Run** button, but accessible from outside the Anvil Editor. This allows you to flip between writing code and testing it with a program like [curl](https://curl.se) or [Postman](https://postman.com).
