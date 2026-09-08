---
title: "Forms as Python Classes"
url: "/docs/client/forms/forms-as-python-classes"
---


# [Forms as Python Classes](#forms-as-python-classes)

Each Form is represented by a Python package that defines a class with the same name as the Form. This class inherits from a class called `<FormName>Template`, which defines the basic structure of the Form.

When a Form is displayed on the screen, Anvil creates an instance of that class — a Python object. The components you add to the Form in the designer are attributes of that object, and they are themselves [Python objects](/docs/client/client-code#everything-is-an-object).

## [The Form Class](#the-form-class)

When you add a new Form to your app, the Anvil Editor auto-generates the following code:

```python
from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
```

In this example, the `Form1` Class that inherits from `Form1Template`. When `Form1` is displayed on the screen, Anvil instantiates the class to create a Python object of type `Form1`. The `__init__` method runs during this process, initialising the Form’s components and properties. See [How Forms are Initialised](#how-forms-are-initialised) for more details.

The components you drop into the Form in Design view become attributes of the `Form1` object. For example, if you added a button called `submit_button` to `Form1` in the Design View, you can access and modify it directly in code:

```python
from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("submit_button", "click")
  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.submit_button.text = "Submitted"
    self.submit_button.enabled = False
```

## [The Top-Level Form](#the-top-level-form)

Anvil components exist in a hierarchy, and at the top is a single Form - the **top-level Form**. The Top-level Form is the currently visible Form that sits at the top of the component hierarchy and contains all other components. You can get a reference to it by calling `get_open_form()`, which gives you access to all of its components.

This is especially useful when you need to access a component in a parent Form from within a RepeatingPanel’s ItemTemplate:

```python
# Get the open Form
form = get_open_form()

form.label_loading.text = "Loading test runs..."

# repeating_panel_1 displays some test runs,
# get the latest data for each one.
for test_run in form.repeating_panel_1.get_components():
  test_run.refresh()

form.label_loading.text = "Loaded!"
form.label_loading.icon = "fa:check"
```

To replace the top-level Form with a new Form, call `open_form()`, and pass in the Form you want to display. See [Navigation](/docs/client/navigation) for more details.

## [The `item` property](#the-item-property)

All Forms have a property called `item`. Its default value is an empty dictionary, and it triggers a [Data Binding](/docs/client/component-properties/data-bindings) refresh whenever it is set.

By default, `item` is the only property that Forms have. If you configure your Form as a [Custom Component](/docs/client/customisation/custom-components#configuring-custom-components), you can add more properties.

[RepeatingPanels](/docs/ui/components/repeating-panel) repeat the same Form once for each element in their `items` list. In that case, the `item` property of each Form instance corresponds to one element of `items`.

`self.item` works slightly differently for Repeating Panels. It is explained fully in the section on [RepeatingPanels](/docs/ui/components/repeating-panel).

## [How Forms are initialised](#how-forms-are-initialised)

When a Form is initialised, the following sequence of events occurs.

First, the template’s `__new__` method creates all the components specified in the visual designer, adds them to the Form, and makes them available as attributes on the Form object (e.g. `self.button_1`).

Then, the Form’s `__init__` method is called. It takes properties as keyword arguments, which is why the auto-generated `__init__` method has a `**properties` parameter. Inside `__init__`, the call to `super().__init__(**properties)` sets those property values as attributes of the Form and refreshes any [Data Bindings](/docs/client/component-properties/data-bindings). This is required for the Form’s setup.

If you want to set up any values that your Data Bindings rely on, do so before the call to `super().__init__(**properties)` in the `__init__` method:

```python
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.
```
