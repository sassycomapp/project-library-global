---
document: "Events"
title: "Events"
url: "/docs/client/events"
doc-id: events-_index
state: Live
date-created: 2026-09-08
---


# [Events](#events)

[Components](/docs/ui/components) in Anvil can raise events. Events occur when users interact with your app. For example, when a Button is clicked, a `click` event is raised by a component. In Anvil, you can write Python code that runs whenever a specific event is rasied.

## [Setting event handlers](#setting-event-handlers)

You can see which events a component raises at the bottom of the [Properties Panel](/docs/editor/form-editor#properties-panel). You can also find a list of these events per component in the [API reference](/docs/api/anvil) The example below is for a Button component:

This Button calls `self.submit_button_click`  
when it is clicked.

You can have your component call a function when one of these events is raised. To do this, click the blue arrow next to the event. This will automatically create an event handler and switch your Form to code view.

The created method will be decorated with `@handle("<component-name>", "<event-name>")`. This decorator tells Anvil to run this method when the named component raises the named event. For example, in the code below, the `submit_button_click` method will run whenever the `submit_button` raises the `click` event:

```python
@handle("submit_button", "click")
def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.submit_button.text = "Submitted!"
```

The Object Palette also provides a shortcut for creating an event handler for a component’s most common event:

The Object Palette shortcut for the  
Button component sets the `click` event

Any function with the `@handle` decorator will be registered as an event handler. You do not need to create the function through the Properties Panel or Object Palette. See [Setting event handlers in code](#setting-event-handlers-in-code) for more details.

Changing the name of a component from the Designer will automatically update the first argument in the `@handle` decorator for any connected event handlers.

Any event handlers created before the [release of the `@handle` decorator](/blog/pythonic-event-handling) will not have this decorator. You will be able to change the event handler that is bound to the event by editing it from the Properties Panel. You can also modify existing event handlers to use the `@handle` decorator. In that case, the name of the event handler will no longer be editable from the Properties Panel.

### Event arguments

Events have arguments that are passed as keyword arguments to the event handler function. Every event handler has the following arguments:

-   `event_name`, for example ‘click’
-   `sender`, the Python object that triggered the event. For example, a `click` event triggered by a Link will have the Link object as the `sender`. You could use this to style the Link differently to show that it has been followed.

Other arguments may be present depending on the event, for example the precise mouse position. To discover what other arguments are present for a particular event, look at the [API Reference](/docs/api/anvil).

When you set up an event handler in Anvil, it should have the `**event_args` as a parameter. The `**` soaks up any extra keyword arguments that come with the event and puts them all in a dict called `event_args`. You can also run `print(event_args)` at the top of the event handler to see what arguments are present for that particular event.

Always use an `**event_args` if you’re defining your own event in case any new arguments get added that you need to soak up.

### Setting event handlers in code

You can also bind a method to an event entirely in code. To turn a Form method into an event handler, add the `@handle` decorator, passing in the name of the component that will raise the event and the name of the event that will be raised. The method will also need to have [`**event_args` as an argument](#event-arguments). For example, the `reload_map` method below will run when the `location_dropdown` fires the `change` event (i.e. when the user selects an item in the Dropdown menu):

```python
@handle("location_dropdown", "change")
def reload_map(self, **event_args):
    new_map = anvil.server.call("get_new_map", self.location_dropdown.selected_value) 
    self.map.data = new_map
```

You can even stack multiple `@handle` decorators, to call the same function from multiple events:

```python
@handle("location_dropdown", "change")
@handle("reload_button", "click")
def reload_map(self, **event_args):
    new_map = anvil.server.call("get_new_map", self.location_dropdown.selected_value) 
    self.map.data = new_map
```

When you create an event handler from Design view, the event handler, by default, will be named based on the name of the component and the event it is raising. However, event handlers do not need to follow this naming convention. They just need to have the `@handle` decorator with the correct component name and event name, and they need to have `**event_args` as an argument.

The event handlers you write must belong to the same Form as the component that will be calling them. In other words, a component that lives on `Form1` cannot call a method written in `Form2` using the `@handle` decorator. However, child and parent components can raise events on each other (see [raising events on parents and children](#raising-events-on-parents-and-children)), and any function can be registered as an event handler for any component using the dynamic API (see the next section).

#### Dynamically setting event handlers

You may want to add or remove event handlers dynamically in code.

In this case, you can use `add_event_handler` to add an event handler to a component. `add_event_handler` expects two arguments, the name of the event and the name of the method that will be called when the event fires.

```python
self.button_1.add_event_handler("click", self.handle_click)
```

To remove an event handler from a component, use `remove_event_handler`. `remove_event_handler` expects an `event_name` argument and optionally, a function name. If you just pass in the event name, then all handlers for that named event will be removed from the component. Alternatively, if you pass in a specific function, only that handler will be removed.

```python
self.button_1.remove_event_handler("click", self.handle_click)
```

## [Custom events](#custom-events)

You’re not limited to the events in the Properties Panel. You can add and raise custom events on any component using `@handle` and `raise_event`, respectively. The name of the custom event must begin with the prefix `x-` to avoid conflicting with any built-in event names.

When using `raise_event`, any extra keyword parameters will get passed to the event handler function. The sender argument will be the component on which `raise_event()` was called.

For example, the below code shows a Form class where a custom event called `x-refresh` has been added to the `self.sales_plot` component. When the `refresh_button` component is clicked, it raises this custom event:

```python
class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        super().__init__(**properties)
        #add event handler to the sales_plot component

    #when the refresh button is clicked, raise the x-refresh event and pass in the new_location keyword arg
    @handle("refresh_button", "click")
    def refresh_button_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.sales_plot.raise_event("x-refresh", new_location="Cambridge")

    #when the x-refresh event is raised on self.sales_plot, this method will run
    @handle("sales_plot", "x-refresh")
    def refresh_plot(self, new_location, **event_args):
        anvil.server.call("refesh_plot", new_location)
```

### Raising events on parents and children

The most common use case for custom events is raising events on parent and child components. [Container components](/docs/ui/components/containers) can contain other components and you can communicate between those components through custom events. You can raise an event on a parent component using `self.parent.raise_event("<event-name>")`.

Ensure the name of your custom event begins with `x-` to avoid conflicting with any built-in event names.

For example, in a Form with a [RepeatingPanel](/docs/ui/components/repeating-panel) component, the RepeatingPanel’s ItemTemplate might have a delete button on it. When the delete button is clicked, it calls a server function to delete the underlying data and then refreshes the entire RepeatingPanel.

To do this, you can add a custom event handler to the RepeatingPanel in the main Form code:

```python
#In the main form code

class MainForm(MainFormTemplate):
    def __init__(self, **properties):
        super().__init__(**properties)
    
    #when the x-refresh event fires, this method will be called
    @handle("repeating_panel_1", "x-refresh")
    def refresh_list(self, **event_args):
        self.repeating_panel_1.items = anvil.server.call("get_list_items")
```

And raise the event from the ItemTemplate:

```python
# in the ItemTemplate form code

    @handle("delete_button","click")
    def delete_button_click(self, **event_args):
        #when the delete button is clicked, raise the x-refresh event on the RepeatingPanel
        self.parent.raise_event("x-refresh")
```

Similarly, a parent container can raise an event on all of its children using `raise_event_on_children()`.

## [The `show` and `hide` events](#the-show-and-hide-events)

Some actions can only be performed after a component is added to the web page in the browser. For example, a `Canvas` component cannot discover the size of its drawing area until it is added to the page. This means a Form cannot usefully draw on a `Canvas` during its `__init__` function. Instead, the drawing code must run when the Form is added to the page.

To help handle these situations, all components have a `show` and `hide` event, which trigger when the component is added to, or removed from, the page.

The `show` event does not necessarily mean the component is visible to the eye - a component may be invisible, but its `show` event still fires when it is added to the page. To be precise, these events trigger after the component is added to the browser’s HTML DOM. To learn more about component lifecycle events, check out [Component Lifecycle](/docs/client/events/component-lifecycle).

`show` and `hide` propagate across containers: If a component’s container is added to the page, it too is added to the page. A container’s `show` or `hide` event is raised *after* all its children.
