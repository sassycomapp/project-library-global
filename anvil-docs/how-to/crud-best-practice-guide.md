---
title: "Building clean database apps"
url: "/docs/how-to/crud-best-practice-guide"
doc-id: crud-best-practice-guide
state: Live
date-created: 2026-09-08
---


# [Building clean database-backed apps](#building-clean-database-backed-apps)

There are many ways to build database-backed, or CRUD (**C**reate/**R**ead/**U**pdate/**D**elete) apps with Anvil. This guide describes our **recommended** approach for building CRUD functionality in Anvil. It’s not mandatory – Anvil provides tons of flexibility, so you can do whatever you need to – but we’ve found that these principles make your apps faster to build and easier to maintain.

## [Don’t repeat yourself](#dont-repeat-yourself)

**Recommendation #1**: Reuse code and UI components wherever possible

Reusing code and UI components can save you a lot of time and dramatically simplify your CRUD apps.

### One Form for Creating and Updating

Often, it’s possible to use one Form to both **C**reate and **U**pdate records.

We recommend using a Form’s [`self.item` property](../client/components/forms#the-item-property), a Python dictionary and [Data Bindings](/docs/client/component-properties/data-bindings) to do this.

For example, say you have a Form with a set of prompts and user input fields to be used to **C**reate a record.

You’ll want to keep track of the user’s inputs as they fill in the Form. You’ll also want a simple way to discard user inputs if they decide not to save the record. You can do this by setting that Form’s `self.item` attribute to a dictionary.

If you’re **C**reating a new record, that can be an empty dictionary:

```python
from UserEdit import UserEdit
# Add the UserEdit Form to the page and set `self.item` to an empty dictionary
self.content_panel.add_component(UserEdit(item={}))
```

As the user fills in the form, add their inputs to the dictionary using [Data Bindings](/docs/client/component-properties/data-bindings). For example, using the UserEdit Form from above:

-   `name_box`: Bind the `text` property to `self.item['name']`
-   `email_box`: Bind the `text` property to `self.item['email']`

If the user decides to create the new record, write the data in the dictionary into the Data Table. If they cancel, you can just discard the dictionary.

In our example, you can also use the `UserEdit` Form for **U**pdating records. Instead of setting the `self.item` property of UserEdit to an empty dictionary, this time we pass a **copy** of the record from the Data Table that we want to edit:

```python
from UserEdit import UserEdit
user_row = """This is the user row from the Data Table"""
# Call dict() on this row to create a copy of it
self.user_copy = dict(user_row)
# Add the UserEdit Form to the page and set `self.item` to the copy of the user_row
self.content_panel.add_component(UserEdit(item=self.user_copy))
```

We already have [Data Bindings](/docs/client/component-properties/data-bindings) to `self.item` in our UserEdit Form, so any updates the user makes will also be written back to the `user_copy` dictionary. If the user saves their changes, we use that dictionary to update the row in the Data Table, and if they cancel – we can just discard the dictionary, and leave the row as it is.

You can see a full worked example of using Python dictionaries, and Data Bindings to reuse **C**reate and **U**pdate Forms in our [Building Database-Backed Apps](/learn/tutorials/database-backed-apps) tutorial.

## [Global vs record-specific logic](#global-vs-record-specific-logic)

**Recommendation #2**: Keep the business logic of your app together on your main Form. Reuse UI components and Forms - they **don’t need to know** which CRUD operation they’re performing. Let your main Form take care of that.

For example, if your app has a ‘Homepage’, or ‘Main’ Form, keeping your CRUD operations inside this ‘Main’ Form simplifies your app:

1.  All actions in your app that perform the same operation (e.g. deleting a record) can just call the same ‘Main’ delete function, rather than having several functions performing the same operation. This also makes things simpler if you decide to change your delete function – you’ll only have to change it in one place.
2.  If you’re reusing similar components (e.g. using the same form for Creating and Updating a record), the components don’t need to know which CRUD operation they’re performing. They can just accept user inputs, and leave the ‘Main’ Form to perform the correct CRUD operation.

For example, take the ‘UserEdit’ Form [above](#dont-repeat-yourself). All this Form does is record user inputs using [Data Bindings](/docs/client/component-properties/data-bindings) – no CRUD operations or logic are stored in the Code of the ‘UserEdit’ Form. Since the Form is **only** responsible for taking user inputs, we can use it to both **C**reate and **U**pdate user records.

### Event handlers on the ‘Main’ Form

Keeping the logic of your CRUD operations inside the ‘Main’ Form means you’ll sometimes need to call a function on the ‘Main’ Form from inside a nested or ‘child’ Form. We recommend setting a custom [event handler](../client/components#events) on the child’s container (often a RepeatingPanel), and triggering this from the ‘child’ Form. You can look up a component’s ‘parent’ container with the `.parent` attribute.

## [Cancelling operations](#cancelling-operations)

**Recommendation #3**: Use a Python dictionary to record user inputs, and save those inputs to the database when the user confirms the operation. If they cancel, just discard the dictionary.

It’s important to consider what your app will do if a user cancels the operation they’re performing.

We recommend using a Python dictionary to record user inputs. If the user cancels the operation, the dictionary containing the user inputs can just be discarded.

When performing the **U**pdate operation, make a **copy** of the record that’s being updated, and use that dictionary to record user inputs. If the user clicks “Save”, you can then write that data from the dictionary back to the database record. If the user clicks “Cancel”, you can discard the dictionary and you haven’t overwritten any data.

The [reusing components section above](#reusing-components) has more information and examples about using dictionaries to simplify data management and cancelling operations.

## [Data Bindings](#data-bindings)

**Recommendation #4**: Data Bind to things that can be refreshed quickly.

It’s likely you’ll want to use [Data Bindings](/docs/client/component-properties/data-bindings) to keep a component’s properties in sync with the underlying data. You’ll need to decide **where** you’ll use Data Bindings in your app.

We recommend you data bind to things that can be refreshed quickly (e.g. without a round-trip to the server).

### Data Binding to data from a server function

If you’re data binding to data returned from a server function, we recommend you set your component properties *in code*. This way, you can be explicit about when you’re performing round trips to the server.

## [Validation](#validation)

**Recommendation #5**: Place your validation logic inside a ‘Validation’ [Module](../client/python/modules), and carry out validation from both client and server.

You’ll often want to validate your users’ inputs. For example, you might want to ensure that the “name” field is not empty, or that “date_of_birth” is in the past.

Validation has two purposes:

1.  To provide good feedback to the user, to prompt them to correct their input.
2.  To ensure that your app does not write malformed data into the database.

It’s easiest to provide feedback (#1) in client code, but client code cannot be trusted (see our [security recommendations](#security)), so the final check (#2) must happen in server code.

We therefore recommend validating inputs on *both* client *and* server. The easiest way to do this is to place your validation logic inside a ‘Validation’ [Module](../client/python/modules), so you can import it from both client and server code. Validation functions should return error messages that can be handled by both client and server.

For example, let’s say our ‘Validation’ module contains the the following `get_user_errors()` function. It checks whether the dictionary provided contains a name, and returns an error message if not:

```python
def get_user_errors(user):
  error_messages = []
  if not user.get('name'):
    error_messages.append("You must provide a name")
  return error_messages
```

We can handle the error message on the client using an alert:

```python
import Validation

# ...
# When we want to create a new user:
error_messages = Validation.get_user_errors(new_user_dict)
if error_messages:
  alert("The following errors occurred: \n{}".format(' \n'.join(msg for msg in error_messages)))
else:
  anvil.server.call('add_user', new_user_dict)
# ...
```

On the server, if we get passed invalid data, we can raise an Exception.

If we receive invalid data in a server function, **something has gone badly wrong**. If nobody has tampered with our client code, we should never have got this far – the client-side validation logic would have caught the error! So there’s a good chance something fishy is going on.

Therefore, at this point, we don’t need to display a clean error. We just need to make sure we **don’t add the incorrect data to our database**. Raising an Exception (that probably won’t be caught) is a good way to do this.

```python
import Validation

# ...
@anvil.server.callable
def add_user(new_user_dict):
  exceptions = Validation.get_user_errors(new_user_dict)
  if exceptions:
    raise Exception("The following errors occurred: \n{}".format(' \n'.join(word for word in exceptions)))
  else:
    app_tables.users.add_row(**new_user_dict)
# ...
```

## [Security](#security)

**Recommendation #6**: Restrict database access to [server modules](../server) – don’t allow client-side code to access [Data Tables](../data-tables).

Anvil is designed with [security in mind](../security).

If your CRUD app uses Data Tables or an external database to store data, we recommend restricting database access to [Server Modules](../server).

This is because [client-side code](../client/python) can’t be trusted. As is the case with **any** web app, client-side code is executed in the user’s web browser - this means that any user can edit the client code to do whatever they like. We can’t trust that Forms (and Modules they import) will do what we tell them, and we must write our app bearing this in mind.

[Server modules](../server), by contrast, cannot be edited by the user, so we can trust them to do what we tell them. This is why it is best practice to carry out all database transactions from a server module.

By default, Anvil Forms (which contain your client-side code) [are not given any access](../data-tables/data-security#permissions) to your [Data Tables](../data-tables). This is to encourage users to always access Data Tables from within a server module.

### Make sure database rows are real before using them

You will sometimes write server code that accepts a database row from the client, and performs some action on it. For example, here is a naive **U**pdate server function that does not perform any checks. (We’re using the datamodel from our [CRUD tutorial](/learn/tutorials/database-backed-apps):)

```python
# THIS FUNCTION IS DANGEROUSLY INSECURE. Do not do this!
@anvil.server.callable
def update_article(article_row, article_dict):
  article_row.update(**article_dict)
```

Because this code **doesn’t check that `article_row` belongs to the `articles` table**, malicious client code could pass *any* database row to this function, and it will be updated! Not a good idea.

Here’s what you should do instead:

```python
# This function is safe: It will only update rows from the
# `articles` table.
@anvil.server.callable
def update_article(article_row, article_dict):
  if app_tables.articles.has_row(article_row):
    article_row.update(**article_dict)
  else:
    raise Exception('No such article')
```

## [Naming conventions](#naming-conventions)

**Recommendation #7**: give your UI components and functions sensible names to make the logic of your app easy to follow

We use certain naming conventions in our example code, which we’ll outline below. You don’t have to stick to them, but we’ve found they make our code a lot clearer.

For example, this code is far easier to follow:

```python
def refresh_articles(self):
  # Load existing articles from the Data Table, and display them in the RepeatingPanel
  self.articles_panel.items = anvil.server.call('get_articles')
```

than this:

```python
# What 'data' are we refreshing? What is 'repeating_panel_1' for?
# Who knows!
def refresh_data(self):
  self.repeating_panel_1.items = anvil.server.call('get_data')
```

All the examples below are for an app designed to manage user records. Our CRUD operations will all be for a ‘User’ record.

#### Naming Forms

##### Create & Update

If can use our **C**reate Form to also **U**pate records, we call our **C**reate / **U**pdate Form ‘UserEdit’

If we have a separate **C**reate and **U**pdate Forms, we call these ‘CreateUser’, and ‘UserEdit’

##### Read

If we have a number of columns in our Data Table, it’s likely that we will have two views for **R**eading a record: one displaying summary information, the other displaying more detailed information about a record.

Forms presenting summary information are called ‘UserSummary’. Forms presenting detailed information are called ‘UserView’.

Information for **R**eading a record is often presented in a list, using a Data Grid or RepeatingPanel. The ItemTemplate of the RepeatingPanel should be named ‘UserSummary’ or ‘UserView’, depending on the level of information it is displaying

For example, in our [basic CRUD example](/learn/tutorials/database-backed-apps), the `ItemTemplate` of our RepeatingPanel is displaying detailed information for a list of news articles, so the ItemTemplate is called ‘ArticleView’

#### Naming Buttons

We give our buttons useful names so that it’s easy to recognise them from code. We use names like `add_user_button`, `edit_user_button`, `delete_user_button`.

#### Naming Functions

When displaying a list of users (for example, on the Homepage), we load all user data in a function called `refresh_users`, and call it from the Form’s `__init__` method. We use the term `refresh` because the function can also be called anywhere else the data needs reloading, for example after a **C**reate, **D**elete or **U**pdate operation.

To [make operations easy to cancel](#cancelling-operations), we recommend using a Python dictionary to store user inputs. We define a function called `reset_new_user` to initialise the dictionary which will record user inputs.

```python
def reset_new_user(self):
  # Initialise a dict for creating a new user
  # & write back to it using data bindings
  self.new_user = {}
```

`reset_new_user()` can be called whenever the dictionary needs to be reset. For example, we would call `reset_new_user` in the `__init__` method of our Form to create the dictionary when our app is run for the first time. We would also call this function if the user cancels the current CRUD operation. This would reset the dictionary, discarding any user inputs made before the operation was cancelled.

#### Naming Events and Handlers

We recommend [using events](#global-vs-record-specific-logic) to communicate between forms in your app. If you are setting a custom event handler on your [‘Main’ Form](#global-vs-record-specific-controls) to handle **D**elete operations, call the custom event `x-delete-user`, and use this to trigger a `self.delete_user(user)` function.

For example:

```python
# In your Main Form
def __init__(self, **properties):
  # Set Form properties and Data Bindings.
  super().__init__(**properties)
  self.refresh_users()
  self.set_event_handler('x-delete-user', self.delete_user)

# ...

def delete_user(self, user):
  anvil.server.call('delete_user', user)
  self.refresh_users()
```
