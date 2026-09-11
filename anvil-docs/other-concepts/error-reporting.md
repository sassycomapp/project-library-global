---
document: "Error Reporting"
title: "Error Reporting"
url: "/docs/other-concepts/error-reporting"
doc-id: error-reporting
state: Live
date-created: 2026-09-08
---


# [Error reporting](#error-reporting)

When an uncaught exception occurs in your Anvil app, it is displayed in the Output window if you are debugging in the Anvil Editor. If you are running the app outside the Anvil Editor, it will display a box at the bottom-right of the screen, as pictured here.

You can get a full stack trace of the error from the [app logs](/docs/editor/app-logs).

## [Custom error handling](#custom-error-handling)

You can install a custom handler for uncaught errors using `set_default_error_handling`. The default error handler is a function that is called for any uncaught error in your code. It is passed the uncaught exception as its only argument.

If a custom error handler is set, it is called instead of the automatic pop-up box. This enables you to handle errors more smoothly, such as by connecting the user with customer support, or suggesting that they refresh the page.

```python
# This code displays an Anvil alert, rather than
# the default red box, when an error occurs.

def error_handler(err):
  alert(str(err), title="An error has occurred")

set_default_error_handling(error_handler)
```

The exception is always logged to the app logs, whether or not you have set a custom error handler.

If a custom error handler throws an exception itself, Anvil will display the default red pop-up and log the new exception to the app logs. Anvil will then disable the custom error handler (so as to avoid an infinite loop of errors), and fall back to the default pop-up from then on.

If the custom error handler re-raises the *original* exception (ie the one it got passed as an argument), the default red pop-up will appear, but the custom error handler will not be disabled.
