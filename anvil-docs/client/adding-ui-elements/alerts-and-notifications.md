---
title: "Alerts and Notifications"
url: "/docs/client/adding-ui-elements/alerts-and-notifications"
---


# [Alerts and Notifications](#alerts-and-notifications)

You can display popup messages using the `alert` and `confirm` functions. They are in the [`anvil`](/docs/api/anvil) module, so will be imported by default.

## [Messages](#messages)

The simplest way to display a popup message is to call the `alert` function. You must supply at least one argument: The message to be displayed. The `alert` function will return `True` if the user clicks OK, or `None` if they dismiss the popup by clicking elsewhere. The example on the right produces the following popup:

```python
alert("Welcome to Anvil")
```

## [Confirmations](#confirmations)

If you want to ask your user a yes/no question, just call the `confirm` function in the same way. The `confirm` function returns `True` if the user clicks Yes, `False` if the user clicks No, and `None` if they dismiss the popup by clicking elsewhere (See `dismissible` keyword argument, below).

```python
c = confirm("Do you wish to continue?")
# c will be True if the user clicked 'Yes'
```

## [Custom popup styles](#custom-popup-styles)

You can customise alerts by passing extra named arguments to the `alert` (or `confirm`) function:

-   `content` - The message to display. This can be a string or a component (see below)
-   `title` - The title of the popup box
-   `large` - Whether to display a wide popup (default: `False`)
-   `buttons` - A list of buttons to display. Each item in the list should be a tuple `(*text*,*value*[,*role*])`, where `*text*` is the text to display on the button, `*value*` is the value to return if the user clicks the button, and the optional `*role*` sets that button’s [role](/docs/client/customisation/using-css/roles).
-   `dismissible` - Whether this modal can be dismissed by clicking on the backdrop of the page. An alert dismissed in this way will return `None`. If there is a title, the title bar will contain an ‘X’ that dismisses the modal. (default: `True`)
-   `role` - Apply a role to the alert container itself for custom styling (see [Roles](/docs/client/customisation/using-css/roles)).

```python
# Display a large popup with a title and three buttons.
result = alert(content="Choose Yes or No",
               title="An important choice",
               large=True,
               buttons=[
                 ("Yes", "YES"),
                 ("No", "NO"),
                 ("Neither", None)
               ])

print(f"The user chose {result}")
```

## [Custom popup content](#custom-popup-content)

You can display custom components in alerts by setting the content argument to an instance of a component instead of a string.

```python
t = TextBox(placeholder="Email address")
alert(content=t,
      title="Enter an email address")
print(f"You entered: {t.text}")
```

For complex layouts or interaction, you can set the content to an instance of one of your own forms. To close the alert from code inside your form, raise the `x-close-alert` event with a `value` argument:

```python
self.raise_event("x-close-alert", value=42)
```

The alert will close and return the value `42`.

## [Alert buttons](#alert-buttons)

The `buttons` argument takes a list of tuples in this format: `(button_text, return_value[, role])`.

-   `button_text`: The label shown on the button.
-   `return_value`: What `alert()` or `confirm()` returns when that button is clicked.
-   `role` (optional): A styling role such as `"success"`, `"danger"`, `"primary"`, or `"default"`.

For example, `("Yes", True, "success")` creates a **Yes** button that returns `True`.

If you do not set the `buttons` argument:

-   `alert()` defaults to `[("OK", True, "success")]`
-   `confirm()` defaults to `[("Yes", True, "success"), ("No", False, "danger")]`

The Users service login/signup dialogs use buttons like `[("Log in", True, "primary"), ("Cancel", None, "default")]`.

A role of `"default"` is equivalent to omitting the role. To style buttons by role, define CSS for those roles — see [Roles](/docs/client/customisation/using-css/roles).

Example: to style Users service login/signup buttons, add this to your app’s `theme.css`:

```css
.anvil-role-primary button {
  background: #1565c0;
  border-color: #1565c0;
  color: #fff;
}
```

With legacy Bootstrap 3, button roles automatically apply Bootstrap classes (e.g. `btn-success`).

### Custom buttons

If you need layouts or interactions beyond what the `buttons` tuples allow (icons, multi-row layouts, custom click logic), pass `buttons=[]` to hide the defaults and build your own buttons inside a custom content form. Close the alert by raising the `x-close-alert` event from your button’s click handler:

```python
# In your custom form's button click handler:
def my_custom_button_click(self, **event_args):
    self.raise_event("x-close-alert", value=42)
```

## [Notifications](#notifications)

You can display temporary notifications by creating `Notification` objects.

To show a simple notification with some content, call the `show()` method. By default, it will disappear after 2 seconds.

```python
n = Notification("This is an important message!")
n.show()
```

If you use a notification in a `with` block, it will be displayed as long as the body of the block is still running. It will then disappear.

```python
with Notification("Please wait..."):
  # ... do something slow ...
```

You can specify the timeout manually (in seconds), or set it to `None` or `0` to have the notification stay visible until you explicitly call its `hide()` method.

```python
n = Notification("This is an important message!",
                 timeout=None)
n.show()

# Later...
n.hide()
```

As well as a message, notifications can also have a title. Use the `style` keyword argument to set the colour of the notification. Use `"success"` for green, `"danger"` for red, `"warning"` for yellow, or `"info"` for blue (default).

```python
Notification("A message",
             title="A message title",
             style="success").show()
```
