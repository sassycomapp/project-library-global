---
title: "Layouts API"
url: "/docs/client/forms/layouts/layouts-api"
doc-id: layouts-api
state: Live
date-created: 2026-09-08
---


# [The Layouts API](#the-layouts-api)

**This is an advanced topic.** You can create and use Layouts entirely from the Anvil Designer. The rest of this page describes the underlying Python API, which you can use to Layouts entirely in code if you need to.

In general, you will create and use Layouts and Slots from the Designer. Learn more about Layouts in Anvil [here](/docs/client/forms/layouts). However, you can create and use Layouts without the Anvil Designer by using the Python API.

## [The Slot object](#the-slot-object)

An Anvil component can be used as a Layout if it has a `slots` attribute. The `slots` attribute must be a dictionary whose keys are the Slot names as strings and whose values are the corresponding Slot objects.

A Slot object describes how to add components to an underlying [container](/docs/ui/components/containers) and is created with the constructor:

```python
s = Slot(target, insertion_index, container_props)
```

The constructor has the following arguments:

-   **`target`**: A [container](/docs/ui/components/containers) component or another Slot.

-   **`insertion_index`** is the position within the `target` container where components added to the slot will be inserted, which typically affects the position in which they are displayed on the page. For example, an insertion index of 0 will insert all the Slot’s components before any existing components, and an insertion index of `len(target.get_components())` will insert all of the Slot’s components after any existing components.

-   **`container_props`** are any properties of the `target` [container](/docs/ui/components/containers#container-properties) that will be used to add components to the `target`.

To create the Layout, you then need to add the Slots to the `slots` attribute. For example, the following code creates a Layout out of a Linear Panel. The Layout has one Slot called `my_slot`, which is then added to the `slots` attribute.

```python
class MyLayout(LinearPanel):
    def __init__(self, **properties):
        my_slot = Slot(self, 0, {})
        self.slots = {"my_slot": my_slot}
```

A Slot object, like a container component, has the `add_component()` and `get_components()` methods. When you call `add_component()`, the component you are adding will actually be added to the underlying container. If you use the `index=` argument when calling `add_component()`, this argument refers only to a position within the list of components added via this Slot. Likewise, `get_components()` will only return this Slot’s components.

Once you have started using a Slot, you should avoid adding or removing components directly on its `target`, as this will disrupt the Slot’s ability to insert at the correct index within the target.

### Multiple Slots with one target

It is sometimes useful to have multiple Slots with a single target, for example, in different locations on a [Custom HTML Form](/docs/client/customisation/custom-components/html-components), or at two different positions within a list.

If you do this, you must call `offset_by_slot` on the Slot with the larger `insertion_index`, so that the “later” slot can account for components inserted via the “earlier” Slot.

You must call `offset_by_slot()` once for every Slot that precedes this one on the same target.

For example, if you have three Slots, `slot_a`, `slot_b`, and `slot_c`, on the same target, you must offset `slot_b` using `slot_a`, and offset `slot_c` by *both* `slot_a` and `slot_b`:

```python
target = self.linear_panel_1
slot_a = Slot(target, 0, {})
slot_b = Slot(target, 2, {})
slot_c = Slot(target, 3, {})

slot_b.offset_by_slot(slot_a)
slot_c.offset_by_slot(slot_a)
slot_c.offset_by_slot(slot_b)
```

If you have two slots with the same `target` and `insertion_index`, you must choose which Slot’s components go first, and offset the later slot using the earlier one.

## [Using Layouts from code](#using-layouts-from-code)

If you want to define a component class that uses a Layout, it should inherit from `WithLayout`. It also must specify the Layout class with the `layout=` key in the class definition. When you create a Form using a Layout from the Anvil Editor, this is done for you. Its `FormTemplate` class will automatically inherits from `WithLayout`.

The `WithLayout` class exposes the its Layout as its `layout` attribute. This means that you can access the class instance itself as `self.layout` and add components to it via its Slots. (The `layout` object is instantiated the first time the `layout` property is accessed or when the component is added to the page, whichever happens first.)

For example, the following code creates a `MyPage` class that uses a Layout called MyLayout. First, `WithLayout` is imported from `anvil` and the Layout class is imported. Then, in `MyPage`’s constructor, a Button component is created and added to one of the Layout’s Slots.

```python
from anvil import WithLayout
from MyTheme.MyLayout import MyLayout

class MyPage(WithLayout, layout=MyLayout):
    def __init__(self, **properties):
        my_button = Button(text="Click me")
        self.layout.slots["slot_a"].add_component(my_button)
```

If you need to provide keyword arguments to the Layout’s constructor, call `super().__init__(prop="value")` in your `__init__()` function. Keyword arguments to this function will be provided as properties for the Layout.
