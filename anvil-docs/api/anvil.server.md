---
document: "anvil.server"
title: "anvil.server"
url: "/docs/api/anvil.server"
doc-id: anvil.server
state: Live
date-created: 2026-09-08
---


## `anvil.server` Module

#### Classes

[`AppResponder`](#AppResponder) [`CallContext`](#CallContext) [`ClientInfo`](#ClientInfo) [`Location`](#Location) [`StackFrame`](#StackFrame) [`Capability`](#Capability) [`HttpRequest`](#HttpRequest) [`HttpResponse`](#HttpResponse)

#### Functions

[`background_task`](#background_task) [`call`](#call) [`callable`](#callable) [`FormResponse`](#FormResponse) [`get_api_origin`](#get_api_origin) [`get_app_origin`](#get_app_origin) [`get_background_task`](#get_background_task) [`get_session_id`](#get_session_id) [`is_app_online`](#is_app_online) [`launch_background_task`](#launch_background_task) [`list_background_tasks`](#list_background_tasks) [`loading_indicator`](#loading_indicator) [`portable_class`](#portable_class) [`reset_session`](#reset_session) [`run_script`](#run_script) [`unwrap_capability`](#unwrap_capability)

#### Globals

[`context`](#context) [`no_loading_indicator`](#no_loading_indicator) [`request`](#request) [`session`](#session)

#### Exceptions

[`AppOfflineError`](#AppOfflineError) [`BackgroundTaskError`](#BackgroundTaskError) [`BackgroundTaskKilled`](#BackgroundTaskKilled) [`BackgroundTaskNotFound`](#BackgroundTaskNotFound) [`ExecutionTerminatedError`](#ExecutionTerminatedError) [`InternalError`](#InternalError) [`InvalidResponseError`](#InvalidResponseError) [`NoServerFunctionError`](#NoServerFunctionError) [`PermissionDenied`](#PermissionDenied) [`QuotaExceededError`](#QuotaExceededError) [`RuntimeUnavailableError`](#RuntimeUnavailableError) [`ScriptExitError`](#ScriptExitError) [`SerializationError`](#SerializationError) [`ServiceNotAdded`](#ServiceNotAdded) [`SessionExpiredError`](#SessionExpiredError) [`TimeoutError`](#TimeoutError) [`UplinkDisconnectedError`](#UplinkDisconnectedError)

## Classes

### `AppResponder`

Create an AppResponder object. `data` should be a serializable object. `meta` should be a dict of meta tag names and values to inject into the head of the HTML document.

#### Constructor

`AppResponder([data=None], [meta=None])`

#### Instance Methods

**load_app()** — Loads an app at it's startup form/module

**load_form([form], *args, **kwargs)** — Open the specified form as a new page from a route

**load_module(module_name)** — Opens the specified module as a new page from a route

---

### `CallContext`

#### CallContext Attributes

**background_task_id** - *string* — The ID of the currently running background task, if there is one.

**client** - *anvil.server.CallContext.ClientInfo instance* — An object that describes the client that initiated the current session. This can be a browser, an HTTP endpoint request, an uplink script, a background task, or an incoming email.

**remote_caller** - *anvil.server.CallContext.StackFrame instance* — An object describing the code that called this @anvil.server.callable function, where it was running, and whether it is trusted (server-side) or un-trusted (input from a browser, HTTP or other remote code)

**type** - *string* — The execution environment this code is running in. May be 'browser', 'server_module' or 'uplink'

---

### `ClientInfo`

#### ClientInfo Attributes

**ip** - *string* — The IP address of the client that initiated this session.

**location** - *anvil.server.CallContext.Location instance* — The location of this client, as determined by its IP address, or None if it cannot be determined.

**type** - *string* — How this session was initiated. Valid values are: 'browser', 'uplink', 'http', 'background_task' and 'email'.

---

### `Location`

#### Location Attributes

**city** - *string* / **country** - *string* / **latitude** - *float* / **longitude** - *float* / **subdivision** - *string*

---

### `StackFrame`

#### StackFrame Attributes

**is_trusted** - *boolean* — Was this code running in a trusted location (ie on the server side)?

**type** - *string* — The location of the calling code. Valid values are: 'browser', 'server_module', 'uplink' and 'client_uplink' for your app's code, or 'http', 'background_task' or 'email' if this code was extrernally triggered.

---

### `Capability`

Create a new 'Capability' object

#### Constructor

`Capability()`

#### Instance Methods

**narrow(additional_scope) → anvil.server.Capability instance** — Return a new capability that is narrower than this one, by appending additional scope element(s) to it.

**send_update(update)** — Send an update to the update handler for this capability, in this interpreter and also in any calling environment (eg browser code) that passed this capability into the current server function.

**set_update_handler(apply_update, [get_update])** — Set a handler for what happens when an update is sent to this capability. Optionally provide a function for aggregating updates (default behaviour is to merge them, if they are all dictionaries, or to return only the most recent update otherwise.)

#### Capability Attributes

**is_valid** - *boolean* — True if this Capability is still valid; False if it has been invalidated (for example, by session expiry)

**scope** - *list* — A list representing what this capability represents. It can be extended by calling narrow(), but not shortened. Eg: ['my_resource', 42, 'foo']

---

### `HttpRequest`

Create a new 'HttpRequest' object

#### Constructor

`HttpRequest()`

#### HttpRequest Attributes

**body** - *anvil.Media instance* — The body of the HTTP request

**body_json** - *dict* — The decoded JSON body of the HTTP request, if applicable. Only available when Content-Type header is 'application/json'.

**form_params** - *dict* — A dict of form parameters passed with this request.

**headers** - *dict* — HTTP headers sent with the current request

**method** - *string* — The HTTP method of the current request, e.g. GET, POST, etc.

**origin** - *string* — The origin of the current API request, e.g. https://my-app.anvil.app/_/api

**password** - *string* — The password received through HTTP Basic Authentication

**path** - *string* — The path of the current request, e.g. /foo/bar

**query_params** - *dict* — A dict of query-string parameters passed with this request.

**remote_address** - *string* — The IP address the current request is coming from.

**user** - *User* — When require_auth is True, returns the row from the Users table corresponding to the authenticated user.

**username** - *string* — The username received through HTTP Basic Authentication

---

### `HttpResponse`

Create an HttpResponse object

#### Constructor

`HttpResponse(status=200, body="", headers=None)`

#### HttpResponse Attributes

**body** - *any* — The body of this HTTP response. Can be a string, a Media object, or any JSON-able value.

**headers** - *dict* — The headers to return with this HTTP response. Content-Type will be set automatically if not specified.

**status** - *number* — The status code for this HTTP response. Default is 200.

---

## Functions

#### `background_task([fn_or_name])`

When applied to a function as a decorator, the function becomes available to run in the background.

-   `fn_or_name` - The name by which you want to call your function.

#### `call(function_name, **kwargs)`

Allows you to call server-side functions from the client. It requires the name of the function that you want to call, passed as a string. Any extra arguments are passed through to the server function.

#### `callable([fn_or_name], [require_user])`

When applied to a function as a decorator, the function becomes available from the client side.

-   `fn_or_name` - The name by which you want to call your function from the client.
-   `require_user` - Allows you to verify whether a user is logged in. Can be a boolean or a function.

#### `FormResponse([form], *args, **kws)`

Open the specified form as a new page from a route. 'form' is a string, and when received by the client the new form will be created (extra arguments will be passed to its constructor).

#### `get_api_origin([environment_type]) → string`

Returns the root URL of the API for the current app. By default, this function returns the URL for the current environment, which might be private or temporary. If you want the URL for the published branch, pass 'published' as an argument.

#### `get_app_origin([environment_type]) → string`

Returns the root URL for the current app. By default, this function returns the URL for the current environment. If you want the URL for the published branch, pass 'published' as an argument.

#### `get_background_task(id) → Task object`

Returns the Task object of a background task from its id. You can get the task id from task.get_id().

#### `get_session_id()`

Returns the current session's ID.

#### `is_app_online()`

Returns `True` if this app is online and `False` otherwise. If `anvil.server.is_app_online()` returns `False` we expect `anvil.server.call()` to throw an `anvil.server.AppOfflineError`

#### `launch_background_task(fn_name, [args]) → Task object`

Launches a function to run in the background. The function must be decorated with @anvil.server.background_task. Returns a Task object.

#### `list_background_tasks([all_environments]) → list of Task objects`

Returns a list of all Tasks running in the current environment. If all_environments is True, this function will return all of the app's running Tasks regardless of environemnt.

#### `loading_indicator(component_name=None, min_height=None) → context`

By default, a loading indicator is displayed when your app is retrieving data. This stops users from being able to interact with your app while the server returns data. `loading_indicator` is a context manager which allows you to create loading indicators manually.

#### `portable_class([name])`

When applied to a class as a decorator, the class becomese available to be passed from server to client code.

-   `name` - A unique name under which the class will be registered.

#### `reset_session()`

Reset the current session to prevent further SessionExpiredErrors.

#### `run_script(script_name, [args]) → any`

Run one of this app's scripts as a Background Task, wait for it to finish, and return its return value (whatever the script set anvil.script.return_value to). If the script raises an exception, exits with a non-zero status, or is killed, that error is raised here.

#### `unwrap_capability(capability, scope_pattern) → list`

Checks that its first argument is a valid Capability, and that its scope matches the supplied pattern. To match, the scope must: Be at least as broad as the pattern (ie the same length or shorter); Contain the same values in the same position as the pattern - unless that position in the pattern is Capability.ANY, which matches any value. Returns a list of matched scope elements, of the same length as the pattern. (If the scope was broader than required, missing elements are set to None.)

---

## Globals

#### `context`

Contains information about what triggered the currently running code. It's an instance of `anvil.server.CallContext`.

#### `no_loading_indicator`

Use `with anvil.server.no_loading_indicator:` to suppress the loading indicator when making server calls

#### `request`

Contains information about the current HTTP API request. It's an instance of `anvil.server.HttpRequest`.

#### `session`

A dictionary that contains information about a specific session. It can store anything that a server function can return, except for Media objects.

---

## Exceptions

`AppOfflineError`, `BackgroundTaskError`, `BackgroundTaskKilled`, `BackgroundTaskNotFound`, `ExecutionTerminatedError`, `InternalError`, `InvalidResponseError`, `NoServerFunctionError`, `PermissionDenied`, `QuotaExceededError`, `RuntimeUnavailableError`, `ScriptExitError`, `SerializationError`, `ServiceNotAdded`, `SessionExpiredError`, `TimeoutError`, `UplinkDisconnectedError`
