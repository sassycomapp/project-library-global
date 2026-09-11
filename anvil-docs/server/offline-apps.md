---
document: "Offline Apps"
title: "Offline Apps"
url: "/docs/server/offline-apps"
doc-id: offline-apps
state: Live
date-created: 2026-09-08
---


# [Running an app offline](#running-an-app-offline)

Anvil apps can function offline. In other words, an app’s client-side code will continue to work if the device loses its internet connection.

When an app is offline, client-side code (Forms and Modules) will continue to work. However, any code that tries to communicate with the server will fail with an `anvil.server.AppOfflineError`. This includes accessing the [Users Service](../users), working with [Data Tables](../data-tables) or any use of `anvil.server.call`.

This section explores some offline strategies to handle code that communicates with the server.

## [Installing Anvil Apps](#installing-anvil-apps)

Anvil apps are progressive web apps (PWAs) and can be installed almost like native apps.

Specific instructions for installing an Anvil app depends on the platform. On Chrome desktop, the option is available next to the address bar. In Chrome for Android or Safari for iPhone, there is an option to ‘Add to home screen’.

Installing an Anvil app isn’t necessary for an app to work offline. If you visit an Anvil app in a browser and lose connection, the app will continue to run as described above.

## [Is the app online?](#is-the-app-online)

There are two ways to check if an app is online. The first is using `anvil.server.is_app_online()`. If this returns `False`, subsequent communications to the server will fail.

```python
if anvil.server.is_app_online():
    user = anvil.users.login_with_form()
else:
    # we can't use the Users Service since we're offline
    alert("It looks like you're offline")
```

It is worth noting that `anvil.server.is_app_online()` is a heuristic for checking the app’s online status based on the browser’s implementation. `anvil.server.is_app_online()` is reliable at determining when an app is offline. However, it is a known issue that some browsers may give a false positive, i.e. the browser determines the app is online when it is offline. Be prepared to act offline in this situation. Consider providing users with an offline mode. An offline mode will provide users with a stable network option. Useful when the network jumps from offline to online in areas of unstable connection.

Alternatively, wrapping code that communicates with the server in a `try/except` block will allow you to catch and handle an `anvil.server.AppOfflineError` gracefully.

```python
try:
    anvil.server.call('save_data', data)
except anvil.server.AppOfflineError:
    ...
    # save the data in the browser
```

`anvil.server.AppOfflineError` is raised anytime an offline app attempts to communicate with the server. In the above example, we use the `try/except` strategy. First, we `try` and save data using `anvil.server.call`. If we find the app is offline, the code inside the `except` block runs. We would then need to consider strategies for storing (caching) data in the browser inside the `except` block. Later, when the app comes back online, we can make the server call using the cached data.

## [Working with data offline](#working-with-data-offline)

If your app needs data and you want it to run offline, you’ll have to store (cache) that data in the browser to interact with it. Likewise, if a user makes changes while offline, you’ll need to store those changes until you can save them on the server.

A simple storage mechanism for browsers is the `localStorage` object. `localStorage` is a dictionary-like javascript object that persists between browser sessions and works offline. It can be used to store JSON data and can be accessed using `anvil.js`.

```python
from anvil.js.window import localStorage
import json


if anvil.server.is_app_online():
    anvil.server.call('save_data', data)
else:
    localStorage.setItem('unsaved_data', json.dumps(data))
```

A wrapper for `localStorage` can be found in [`anvil_extras`](https://github.com/anvilistas/anvil-extras) (available as a [third-party dependency](https://anvil.works/forum/t/third-party-dependencies/8712)), which provides a cleaner python API for the same object.

```python
from anvil_extras.storage import local_storage

if anvil.server.is_app_online():
    anvil.server.call('save_data', data)
else:
    local_storage['unsaved_data'] = data
```

Note that the persistence of `localStorage` depends on the browser. After several days of inactivity, a browser may clear the `localStorage` object.

`localStorage` is best suited for JSONable data. For more advanced offline data storage consider the browser’s [`IndexedDB API`](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/). `IndexedDB` is a low level client-side database that is suitable for storing simple data types such as strings and floats, as well as more complex data types such as bytes and lists. Working with `IndexedDB` can be tricky and it may be useful to find a Javascript library that wraps `IndexedDB` in a more user friendly API.

## [Example app](#example-app)

In the following Todo app, we explore some strategies for working with data offline. Launching the app offline is possible since it caches user data from the previous sessions. If the app goes offline during a session, attempts to save data on the server are also cached.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:H4CJHWDLCP2EIJRJ%3d77RD4EZMG2RAMWKJZ76M2OZ2)
