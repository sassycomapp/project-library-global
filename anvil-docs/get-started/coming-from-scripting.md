---
title: "Coming from Scripts"
url: "/docs/get-started/coming-from-scripting"
---


# [Introduction to GUI and Server Programming](#introduction-to-gui-and-server-programming)

#### Contents:

-   [Intro to GUI programming](#intro-to-gui-programming)
-   [Intro to server programming](#intro-to-server-programming)
-   [Intro to database programming](#intro-to-database-programming)

## [Intro to GUI programming](#intro-to-gui-programming)

If you’re used to writing Python scripts or using Jupyter notebooks, you’re used to code that runs once from beginning to end. GUIs (**G**raphical **U**ser **I**nterfaces) aren’t like that. In a GUI, code runs because some [event](../client/events) has happened – for example, when the user clicks on a button.

In Anvil, you design your pages ([Forms](../client/forms)) with the drag-and-drop designer. Then you write the [event handlers](../client/events) as Python methods, in the code attached to your Form.

For example, here is how to place a button and then set up some Python code that runs when it’s clicked.

### Try it yourself

Building your first GUI code with our tutorial:

[Build a feedback form](/learn/tutorials/feedback-form)

## [Intro to server programming](#intro-to-server-programming)

Your event handlers – in fact, all the code in your Forms – runs on the user’s computer or phone, in the web browser where thy open your app. To do the heavy lifting, to control who can do what, or to use [packages you’ve installed from PyPI](../server/custom-packages), you’ll need server code.

Code in your [Server Modules](../server/server-modules) runs on Anvil’s computers, where your users can’t see or influence it. You can define “[callable functions](../server/server-modules#calling-server-functions-from-client-code)” in your Server Modules, and call them from your client-side event handlers. For example:

```python
# This code goes inside a Server Module

@anvil.server.callable
def send_feedback(feedback_text):
    # Write to the database (privileged operation, trusted code only)
    app_tables.feedback.add_row(feedback=feedback_text)
```

```python
    # This code goes inside a Form.
    # It assumes you've placed a Button named button_1 and a TextBox named feedback_box.

    @handle('button_1', 'click')
    def button_1_click(self, **event_args):
        anvil.server.call('send_feedback', self.feedback_box.text)
```

### Try it yourself

Build a server-client app with our tutorial:

[Build a feedback form](/learn/tutorials/feedback-form)

## [Intro to database programming](#intro-to-database-programming)

Most programs need to store data – information users have submitted, uploaded files, user accounts…whatever you need.

This is done with a **database**: a set of tables with fixed columns where the code can create new rows, search for rows with particular column values, and edit existing rows.

Anvil comes with a powerful built-in database called [Data Tables](../data-tables). Rows in Data Tables are Python objects – you can return them from server to client code and pass them back again. You can even [define your own Python classes](../data-tables/model-classes) for the rows of each table, to add extra functions and attributes.

### Try it yourself

Learn to use Data Tables with our tutorial:

[Build a database-backed app](/learn/tutorials/database-backed-apps)

Or read the full documentation to learn about advanced features:

[Data Tables documentation](/learn/tutorials/database-backed-apps)

## [Learn more](#learn-more)

If you want to get to grips with Anvil, check out our full range of tutorials:

[All tutorials](/learn/tutorials)

Or dive into our reference documentation:

[Full documentation](/docs)
