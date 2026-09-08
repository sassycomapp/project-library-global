---
title: "Making HTTP requests"
url: "/docs/external-resources/http-apis/making-http-requests"
---


# [Making HTTP requests](#making-http-requests)

## [From client code](#from-client-code)

Anvil’s HTTP module allows you to make any HTTP requests that will run from client code.

### Calling anvil.http.request

Begin by importing the `anvil.http` module.

```python
import anvil.http
```

Once you have imported the `anvil.http` module, you make web requests using the `anvil.http.request` function.

```python
resp = anvil.http.request("https://api.mysite.com/foo")
print(f"Response MIME type: {resp.content_type}")
```

There are a range of arguments to allow you to specify the HTTP method, custom headers, data to send in the request body, and other things you need to include. See [this section of API docs](/docs/api/anvil.http#request) for a full list of parameters.

```python
resp = anvil.http.request(url="https://api.mysite.com/foo",
                    method="POST",
                    data="Data to post",
                    headers= {
                      "Authentication": "my-access-key",
                    })
print(f"Response MIME type: {resp.content_type}")
```

When making requests from client code, you should be aware of [Browser Restrictions](#browser-restrictions).

### Using the response

If the HTTP status code is successful (200-299), the `anvil.http.request` function returns the response body of the request. By default, this will be a [`Media` object](/docs/working-with-files/media).

```python
response = anvil.http.request("http://ip.jsontest.com")
print(f"The response body was {response.get_bytes()}")
```

If the `json` parameter is set to `True`, a JSON-decoded object will be returned.

```python
response = anvil.http.request("http://ip.jsontest.com", json=True)
print(f"My IP address is {response['ip']}")
```

### HTTP error codes

If the HTTP status code is an error code, an `anvil.http.HttpError` will be raised. `HttpError` has two attributes:

-   `status` - The HTTP status code (a number)
-   `content` - The response body (JSON-decoded as above if possible, or a `Media` object if JSON decoding has failed)

```python
# This code will print "Error 404":
try:
  anvil.http.request("https://anvil.works/404")
except anvil.http.HttpError as e:
  print(f"Error {e.status}")
```

### URL-encoding strings

The HTTP module also contains functions for URL-encoding and URL-decoding strings. This is useful when constructing links to other sites, or URL-encoding [URL hash parameters](/docs/client/navigation#using-the-url-hash) in an Anvil app.

```python
# Prints "Hello%20there"
print(anvil.http.url_encode("Hello there"))

# Prints "Hello there"
print(anvil.http.url_decode("Hello%20there"))
```

### Browser Restrictions

Web browsers restrict the HTTP requests you can make from form code. When the web browser disallows a request, an `HttpError` is raised with a `status` of `0`. The easiest solution is to make your request from a [Server Module](/docs/server) instead.

A client-side `HttpError` with status `0` is usually for one of three reasons:

1.  The URL is inaccessible (cannot connect to host).

2.  You’re requesting an unencrypted (`http://`) URL. All Anvil apps are served over encrypted links (HTTPS), so the browser does not allow unencrypted requests from client-side code.

3.  The URL doesn’t obey the cross-origin rules. (It needs to respond to an OPTIONS request, have the right CORS headers, etc.)

There are two possible ways to remedy this error:

1.  Make the URL behave correctly. (Make sure it’s accessible, serve it over HTTPS, give it the right CORS headers, and so on. This will require some expertise with web serving, and requires you to control the URL you are requesting. You may need to open up your browser’s developer tools to work out precisely what the problem is.)

2.  Make the request from a server module instead. Server modules don’t run in the web browser, so they don’t have any of the browser’s limitations.

## [From server code](#from-server-code)

You can make requests from server code by using Python’s [`requests` library](https://requests.readthedocs.io/en/latest/).

Install the library from the Python version section of your App Settings, or select one of the [base environments](/docs/server/custom-packages#available-base-environments) in which it’s already included.

Import the library and make a request using the `requests.get` function. This will return a Response object.

```python
import requests

resp = requests.get("https://api.mysite.com/foo")
```

To get a JSON object, use the built-in JSON decoder on the response:

```python
resp = requests.get("https://api.mysite.com/foo")
print(resp.json())
```

For more details on how to use the `requests` library, take a look at [their documentation](https://requests.readthedocs.io/).
