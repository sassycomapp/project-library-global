---
document: "RepeatingPanels"
title: "RepeatingPanels"
url: "/docs/components/standard-components/repeating-panel"
doc-id: repeating-panel
state: Live
date-created: 2026-09-08
---


# [RepeatingPanels](#repeatingpanels)

[Properties](/docs/api/anvil#RepeatingPanel_attributes) | [Events](/docs/api/anvil#RepeatingPanel_events)

[Tutorial: Create a TODO list using a RepeatingPanel](/learn/tutorials/storing-and-displaying-data)

### Display the same UI elements repeatedly on the page

RepeatingPanels are a mechanism for displaying the same UI elements repeatedly on the page. Typical uses for RepeatingPanels might be:

-   a TODO list
-   a list of tickets in a ticketing system
-   a series of profiles in a dating website

A RepeatingPanel creates a form for each of a list of items. It uses a template to generate a form for each item in the list.

In the example below, the template displays the details of one email in an inbox (the subject and the ‘from’ address). The design view of the [Form Editor](/docs/editor#form-editor) shows that this template will be repeated for each email in the inbox.

## [Specifying the template](#specifying-the-template)

There are two ways to specify what to use as the template. When you create a new RepeatingPanel in the Editor, Anvil will automatically create a new Form called something like `ItemTemplate1`. You can either click on `ItemTemplate1` in the App Browser to modify `ItemTemplate1` directly, or double-click on the RepeatingPanel and drop components directly into it.

Alternatively, you can attach any Form you like to a RepeatingPanel. For example, let’s say we already have a Form called `EmailSummary`. We can create a new RepeatingPanel and attach `EmailSummary` as the template using the `item_template` dropdown in the Properties Panel.

Or in code like this:

```python
# Import the EmailSummary class from the EmailSummary Form
from EmailSummary import EmailSummary

self.repeating_panel_1.item_template = EmailSummary
```

## [Getting the Data in](#getting-the-data-in)

Set the RepeatingPanel’s `items` property to any iterable. The template will be displayed for each item in the iterable:

```python
   self.repeating_panel = RepeatingPanel()

   # You can use a search iterator from data tables
   self.repeating_panel.items = app_tables.my_emails.search()

   # You can use a flat list
   self.repeating_panel.items = ['a', 'b', 'c']

   # You can use a more complex data structure... anything that can be iterated over
   self.repeating_panel.items = (
     {'from': 'Joe', 'subject': 'Latest tech report'},
     {'from': 'Sally', 'subject': 'Movie night on Friday?'},
     {'from': 'Ada', 'subject': 'My top 10 cat videos'},
   )
```

Once you have set the RepeatingPanel’s `items` property to an iterable, you can access each item in the iterable by calling `self.item` from within the template of your RepeatingPanel.

For example, if your `items` property is set like this:

```python
   self.repeating_panel.items = (
     {'from': 'Joe', 'subject': 'Latest tech report'},
     {'from': 'Sally', 'subject': 'Movie night on Friday?'},
     {'from': 'Ada', 'subject': 'My top 10 cat videos'},
   )
```

then inside the `EmailSummary` Form, if you run the following code in the `__init__` method:

```python
   print(f"self.item = {self.item}")
```

you’ll see that `self.item` is, in turn, set to one element from `self.repeating_panel.items` from the parent Form.

This means that you can use `self.item` in Data Bindings or in the code for `EmailSummary`.

Here’s an example where we write some code in the `__init__` method of the template to set up the UI for each item:

```python
class EmailSummary(EmailSummaryTemplate):

  def __init__(self, **properties):
    super().__init__(**properties)

    # Set the Labels to have fields from the `item` dictionary,
    # which is one entry in the RepeatingPanel's `items` list:
    self.label_from.text = self.item['from']
    self.label_subject.text = self.item['subject']
```

When the app runs, we get a template instantiated for each entry in the `items` list.

### Displaying data in reverse order

The RepeatingPanel displays everything from its items property, in order. If you want to reverse the order, you can just sort the items list. There are two ways of doing this:

1.  Sort it in Python. You can call `sort()` on a Python list, or use the `sorted()` function on any iterable object. Then just set the items property of the RepeatingPanel to the sorted collection:

    ```python
      items = [
         {'from': 'Joe', 'subject': 'Latest tech report'},
         {'from': 'Sally', 'subject': 'Movie night on Friday?'},
         {'from': 'Ada', 'subject': 'My top 10 cat videos'}
        ]
        sorted_items = sorted(items, key=lambda k: k['from'], reverse=True)
        self.repeating_panel_1.items = sorted_items
    ```

2.  If your RepeatingPanel is displaying data from a [Data Table](/docs/data-tables), fetch the items in order from the Data Table using the [`search`](/docs/data-tables/data-tables-in-code#searching-querying-a-table) and [`tables.order_by()`](/docs/data-tables/data-tables-in-code#searching-querying-a-table) functions:

    ```python
      sorted_by_name = app_tables.people.search(
        tables.order_by("name", ascending=False)
      )
      self.repeating_panel_1.items = sorted_by_name
    ```

## [Accessing the RepeatingPanel from the template](#accessing-the-repeatingpanel-from-the-template)

The template has access to its parent RepeatingPanel in the code via `self.parent`.

Let’s say you want to refresh the entire RepeatingPanel when a button is clicked in the template Form. You could use `set_event_handler` to bind an event called `x-refresh` to the RepeatingPanel, then call `self.parent.raise_event('x-refresh')`.

```python
class ItemTemplate1(ItemTemplate1Template):
  # ...
  def button_refresh_click(self, **event_args):
    # Trigger the x-refresh event on the parent RepeatingPanel
    self.parent.raise_event('x-refresh')
```

## [Creating tables](#creating-tables)

[Data Grids](data-grids) are Anvil’s way of creating tables with rows and columns. By default, any Data Grid you drop into your app from the Toolbox will automatically contain a RepeatingPanel. To put data in the table, you set the `items` of that RepeatingPanel.

The auto-generated template for a RepeatingPanel inside a Data Grid is a Form called something like `RowTemplate1` instead of the usual `ItemTemplate1`. It is special because it inherits from [DataRowPanel](data-grids#the-datarowpanel-component), so it is aware of the columns of the Data Grid.

If you want to specify different UI for each row, you can delete the RepeatingPanel and drop individual [DataRowPanels](data-grids#the-datarowpanel-component) into your Data Grid instead - or you can use a RepeatingPanel *and* individual DataRowPanels.

The [Data Grids tutorials](/learn/tutorials/data-grids) are a good way to find out more about creating paginated tables in Anvil. They start with a getting started guide and go on to cover advanced usage.
