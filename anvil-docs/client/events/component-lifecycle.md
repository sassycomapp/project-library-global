---
title: "Component Lifecycle"
url: "/docs/client/events/component-lifecycle"
doc-id: component-lifecycle
state: Live
date-created: 2026-09-08
---


# [Component Lifecycle](#component-lifecycle)

When building custom components in Anvil, you may need to perform basic setup and cleanup tasks such as adding event handlers when the component is connected to the [browser’s DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) and removing them when the component is disconnected from the DOM. To handle this properly, you need a way to track the component through these lifecycle changes.

An Anvil component’s lifecycle begins when it or any of its parent components are attached to the browser’s HTML DOM, whether or not the component is visible. At this point, the component is considered **on the page** (or **mounted**). The lifecycle ends when the component or its parent is disconnected from the DOM, at which point it is considered **off the page** (or **unmounted**).

To help you manage these lifecycle transitions, Anvil provides [page events](#anvil-page-events) that fire at key points in this lifecycle, allowing you to track and respond to these changes.

For most use cases, the [`show` and `hide` events](/docs/client/events#the-show-and-hide-events) are sufficient for responding to a component being on or off the page. The lifecycle events described in this document are primarily for advanced use cases that require lightweight resource setup and cleanup.

## [Anvil Page Events](#anvil-page-events)

Anvil components have four primary page events that signal changes in their lifecycle:

### 1\. `x-anvil-page-added`

This event fires when a component or its parent is added to the browser’s DOM, whether or not the component is visible. At this point, the component is considered mounted. This event is triggered for a component when:

-   The component or its parent is a [startup Form](/docs/client/forms#the-startup-form) and the application launches.
-   The component or its parent Form is opened with `open_form()`.
-   The component is added to an already open Form using `add_component()`.

### 2\. `x-anvil-page-shown`

This event fires when a mounted component becomes visible (`visible = True`). This can happen when:

-   A visible component or its parent is added to the page.
-   A mounted component’s visibility is changed from `False` to `True` by itself or its parent.

All components are visible by default.

### 3\. `x-anvil-page-hidden`

This event fires when a visible component becomes not visible. This happens when:

-   The `visible` property of the component or its parent is toggled from `True` to `False`.
-   A visible component or its parent is removed from the page.

### 4\. `x-anvil-page-removed`

This event fires when the component or its parent is removed from the page. Once this event fires, none of the other page events will fire for that component until it’s added back onto the page.

Page events cascade from parent to children. If a visible parent is removed from the DOM, `x-anvil-page-hidden` and `x-anvil-page-removed` will fire for the parent and all its visible children. Children that are already hidden won’t fire `x-anvil-page-hidden` again.

## [Component Lifecycle Diagram](#component-lifecycle-diagram)

The diagram below summarizes how these page events, along with the `show` and `hide` events, fit into the overall lifecycle of an Anvil component:

## [Using Page Events](#using-page-events)

Here is an example of how you can use page events for lightweight setup and cleanup:

```python
def Form(FormTemplate):
    def __init__(self, **properties):
        super().__init__(**properties)

        # Perform basic setup when component is mounted
        self.add_event_handler("x-anvil-page-added", self._setup)

        # Perform basic cleanup when component is unmounted
        self.add_event_handler("x-anvil-page-removed", self._cleanup)
    
    def _setup(self, **event_args):
        document.addEventListener("click", self._document_click_handler)

    def _cleanup(self, **event_args):
        document.removeEventListener("click", self._document_click_handler)
```

While you can run suspending functions in your `show` and `hide` events, functions called within page events should be lightweight and should not call `open_form`, suspend, or invoke server functions.
