---
title: "anvil.http"
url: "/docs/api/anvil.http"
doc-id: anvil.http
state: Live
date-created: 2026-09-08
---


## `anvil.http` Module

#### Classes

[`HttpError`](#HttpError) [`UrlEncodingError`](#UrlEncodingError)

#### Functions

[`request`](#request) [`url_decode`](#url_decode) [`url_encode`](#url_encode)

## Classes

### `HttpError`

-   [Attributes](#HttpError_attributes)

---

Create a new 'HttpError' object

#### Constructor

`HttpError()`

---

#### HttpError Attributes

**content** - *anvil.Media instance*

The content returned by the request (eg the body of a 404 response)

**status** - *number*

The numeric HTTP status error (eg 404 for "not found").

Status will be 0 for errors that prevent the request completing at all (eg cross-origin policy in the browser).

---

### `UrlEncodingError`

---

Create a new 'UrlEncodingError' object

#### Constructor

`UrlEncodingError()`

---

## Functions

#### `request(url, [method="GET"], [data=None], [json=False], [headers=None], [username=None], [password=None], [timeout=None])` [(more info)](/docs/http-apis/making-http-requests)

Make an HTTP request to the specified URL.

-   `url` - The request will be made to this URL.

-   `method` - The HTTP method. Defaults to 'GET'.

-   `data` - The data to send in the request body

-   `json` - If set to True, the response is parsed into Python objects (dicts/lists/etc), and 'data' is JSON-encoded before sending. If False, the response will be a Media object.

-   `headers` - A dict of strings to set HTTP headers

-   `username` - If specified, used to perform HTTP Basic authentication

-   `password` - If specified, used to perform HTTP Basic authentication

-   `timeout` - An int or float representing the amount of time, in seconds, to wait for a response. Default is 60 seconds.

---

#### `url_decode(string_to_encode)`

URL-decode a string. Raises UrlEncodingError on failure.

---

#### `url_encode(string_to_encode)`

URL-encode a string
