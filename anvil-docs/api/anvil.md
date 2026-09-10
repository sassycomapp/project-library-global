---
title: "anvil"
url: "/docs/api/anvil"
doc-id: anvil
state: Live
date-created: 2026-09-08
---

## `anvil` Module

#### Classes

[`AppEnvironment`](#AppEnvironment) [`AppInfo`](#AppInfo) [`BlobMedia`](#BlobMedia) [`Button`](#Button) [`Canvas`](#Canvas) [`CheckBox`](#CheckBox) [`Classes`](#Classes) [`ColumnPanel`](#ColumnPanel) [`Component`](#Component) [`Container`](#Container) [`DataGrid`](#DataGrid) [`DataRowPanel`](#DataRowPanel) [`DatePicker`](#DatePicker) [`DropDown`](#DropDown) [`FileLoader`](#FileLoader) [`FlowPanel`](#FlowPanel) [`GoogleMap`](#GoogleMap) [`GridPanel`](#GridPanel) [`HtmlComponent`](#HtmlComponent) [`HtmlTemplate`](#HtmlTemplate) [`Image`](#Image) [`Label`](#Label) [`LinearPanel`](#LinearPanel) [`Link`](#Link) [`Media`](#Media) [`Notification`](#Notification) [`Plot`](#Plot) [`RadioButton`](#RadioButton) [`RepeatingPanel`](#RepeatingPanel) [`RichText`](#RichText) [`Slot`](#Slot) [`Spacer`](#Spacer) [`Style`](#Style) [`TextArea`](#TextArea) [`TextBox`](#TextBox) [`Timer`](#Timer) [`URLMedia`](#URLMedia) [`WithLayout`](#WithLayout) [`XYPanel`](#XYPanel) [`YouTubeVideo`](#YouTubeVideo)

#### Functions

[`alert`](#alert) [`confirm`](#confirm) [`download`](#download) [`get_focused_component`](#get_focused_component) [`get_open_form`](#get_open_form) [`get_url_hash`](#get_url_hash) [`handle`](#handle) [`is_server_side`](#is_server_side) [`open_form`](#open_form) [`set_default_error_handling`](#set_default_error_handling) [`set_url_hash`](#set_url_hash)

#### Globals

[`app`](#app)

## Classes

### `AppEnvironment`

-   [Attributes](#AppEnvironment_attributes)

---

---

#### AppEnvironment Attributes

**name** - *string*

The name of the current environment

**tags** - *list*

tags associated with the current environment

---

### `AppInfo`

-   [Methods](#AppInfo_methods)
-   [Attributes](#AppInfo_attributes)

---

---

#### Instance Methods

**get\_asset(\[path\])**

Get an asset file from the app’s theme assets.

**get\_client\_config(\[package\_name\])**

Get the client config for the specified package. If no package name is specified, the client config for the current app is returned.

**get\_server\_config(\[package\_name\])**

Get the server config for the specified package. If no package name is specified, the server config for the current app is returned.

---

#### AppInfo Attributes

**branch** - *string*

The Git branch from which the current app is being run. This is ‘master’ for development apps or apps without a published version, and ‘published’ if this app is being run from its published version.

**environment** - *anvil.AppEnvironment instance*

The environment in which the current app is being run.

**id** - *string*

A unique identifier for the current app

**package\_name** - *string*

The package name of this app

**theme\_colors** - *mapping*

Theme colors for this app as a readonly dict.

---

### `BlobMedia`

---

Create a Media object with the specified content\_type (a string such as ’text/plain’) and content (a binary string). Optionally specify a filename as well.

---

##### Base class: anvil.Media

#### Constructor

`BlobMedia(content_type, content, [name=None])`

---

### `Button` [(more info)](https://anvil.works/doc#button)

-   [Methods](#Button_methods)
-   [Properties](#Button_attributes)
-   [Events](#Button_events)

---

Create a new ‘Button’ object

---

##### Base class: anvil.Component

#### Constructor

`Button([spacing_above=], [spacing_below=], [spacing=], [enabled=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [background=], [foreground=], [border=], [visible=], [role=], [icon=], [icon_align=], [tag=], [tooltip=])`

---

#### Button Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### Button Properties

**align** - *enum: `"left"`, `"center"`, `"right"`, `"full"`*

The position of this button in the available space.

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**icon** - *icon*

The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.

**icon\_align** - *enum: `"left_edge"`, `"left"`, `"top"`, `"right"`, `"right_edge"`*

The alignment of the icon on this component. Set to ’top’ for a centred icon on a component with no text.

**italic** - *boolean*

Display this component’s text in italics

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### Button Events

**click(keys)**

When the button is clicked

-   `keys` - A dictionary of keys including 'shift', 'alt', 'ctrl', 'meta'. Each key's value is a boolean indicating if it was pressed during the click event. The meta key on a mac is the Command key

**show()**

When the Button is shown on the screen

**hide()**

When the Button is removed from the screen

---

### `Canvas` [(more info)](https://anvil.works/doc#canvas)

-   [Methods](#Canvas_methods)
-   [Properties](#Canvas_attributes)
-   [Events](#Canvas_events)

---

Create a new ‘Canvas’ object

---

##### Base class: anvil.Component

#### Constructor

`Canvas([spacing_above=], [spacing_below=], [margin=], [height=], [background=], [foreground=], [border=], [visible=], [role=], [tag=], [tooltip=])`

---

#### Canvas Methods

**add\_color\_stop(offset, color)**

Creates a new color stop on the gradient object. The offset argument is a number between 0 and 1, and defines the relative position of the color in the gradient. The color argument must be a string representing a CSS color.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**arc(x, y, radius, start\_angle=0, end\_angle=PI\*2, anticlockwise=False)**

Adds an arc to the end of the current path with specified center and radius.

**begin\_path()**

Begin a path on the canvas.

**bezier\_curve\_to(cp1x, cp1y, cp2x, cp2y, x, y)**

Adds a Bezier curve at the end of the current path to (x,y) with control points (cp1x,cp1y) and (cp2x,cp2y).

**clear\_rect(x, y, width, height)**

Clear the specified rectangle with the background color of the canvas.

**clip()**

Turn the current path into the clipping region of the canvas.

**close\_path()**

Close the current path with a straight line back to the start point.

**create\_linear\_gradient(x0, y0, x1, y1)**

Returns a gradient object representing a linear gradient from (x0,y0) to (x1,y1).

**create\_radial\_gradient(x0, y0, x1, y1)**

Returns a gradient object representing a radial gradient from (x0,y0) with radius r0 to (x1,y1) with radius r1.

**draw\_image(media, \[x\], \[y\], \[width\], \[height\])**

Draw an image (from a Media object) onto the canvas at the specified coordinates (optionally scaling to the specified width and height)

**draw\_image\_part(media, sx, sy, s\_width, s\_height, dx, dy, d\_width, d\_height)**

Draw a subset of an image (from a Media object) onto the canvas.

sx, sy, s\_width and s\_height specify which pixels within the source image of the source image to draw. dx and dy (and optionally d\_width and d\_height) specify where (and optionally what dimensions) on the canvas to draw the image.

**fill()**

Fill the current path with the current fill style of the canvas.

**fill\_rect(x, y, width, height)**

Fill the specified rectangle with the current fill style of the canvas.

**fill\_text(text, x, y)**

Draw the specified text at the required position.

**get\_height()**

Get the pixel height of this canvas.

**get\_image()**

Take a snapshot of the canvas and return an image as a Media object.

**get\_width()**

Get the pixel width of this canvas.

**line\_to(x, y)**

Adds a straight line segment at the end of the current path to the specified position.

**measure\_text(text)**

Get the size of the specified text in the current font.

**move\_to(x, y)**

Moves the current path position to the specified point without drawing.

**quadratic\_curve\_to(cpx, cpy, x, y)**

Adds a quadratic curve at the end of the current path to (x,y) with control point (cpx, cpy).

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**reset\_context()**

Reset the drawing context for this canvas. Called automatically after a window resize.

**reset\_transform()**

Reset the current transform to the identity matrix.

**restore()**

Restores a drawing transform saved by the ‘save()’ function

**rotate(angle)**

Rotate all subsequent drawing by ‘angle’ radians.

**save()**

Saves the current drawing transform, which can be restored by calling ‘restore()’

**scale(x, y)**

Scale all subsequent drawing operations by ‘x’ horizontally and ‘y’ vertically.

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

**set\_transform()**

Set the current transform matrix to the specified values.

**stroke()**

Draw the current path with the current stroke style of the canvas.

**stroke\_rect(x, y, width, height)**

Outline the specified rectangle with the current stroke style of the canvas.

**stroke\_text(text, x, y)**

Draw the outline of the specified text at the required position.

**transform(a, b, c, d, e, f)**

Multiply the current transform matrix by the specified matrix.

**translate(x, y)**

Translate all subsequent drawing by ‘x’ pixels across and ‘y’ pixels down.

---

#### Canvas Properties

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**fill\_style** - *string*

The color or gradient to use when filling shapes and paths.

**font** - *string*

The font to use when drawing text on this canvas.

**foreground** - *color*

The foreground colour of this component.

**global\_alpha** - *number*

The global opacity to draw with, in the range 0-1.

**global\_composite\_operation** - *string*

The global composite operation to draw with. Defaults to ‘source-over’

**height** - *string*

The height of this component.

**line\_cap** - *string*

The line cap to use when drawing lines on this canvas.

**line\_join** - *string*

The line join to use when connecting lines on this canvas.

**line\_width** - *number*

The width of lines drawn on this canvas.

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**miter\_limit** - *number*

The limit of line join miters, in pixels.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**shadow\_blur** - *number*

The required shadow blur, in pixels.

**shadow\_color** - *string*

The color to use for shadows.

**shadow\_offset\_x** - *number*

The horizontal shadow offset, in pixels.

**shadow\_offset\_y** - *number*

The vertical shadow offset, in pixels.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**stroke\_style** - *string*

The color or gradient to use when drawing outlines.

**tag** - *object*

Use this property to store any extra information about this component

**text\_align** - *string*

Text alignment, relative to the drawing point.

**text\_baseline** - *string*

Text baseline, relative to the drawing point.

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### Canvas Events

**reset()**

When the canvas is reset and cleared, such as when the window resizes, or the canvas is added to a form.

**show()**

When the Canvas is shown on the screen

**hide()**

When the Canvas is removed from the screen

**mouse\_enter(x, y)**

When the mouse cursor enters this component

-   `x` - The x coordinate of the mouse pointer, within this component
-   `y` - The y coordinate of the mouse pointer, within this component

**mouse\_leave(x, y)**

When the mouse cursor leaves this component

-   `x` - The x coordinate of the mouse pointer relative to this component
-   `y` - The y coordinate of the mouse pointer relative to this component

**mouse\_move(x, y)**

When the mouse cursor moves over this component

-   `x` - The x coordinate of the mouse pointer within this component
-   `y` - The y coordinate of the mouse pointer within this component

**mouse\_down(x, y, button, keys)**

When a mouse button is pressed on this component

-   `x` - The x coordinate of the mouse pointer within this component
-   `y` - The y coordinate of the mouse pointer within this component
-   `button` - The button that was pressed (1 = left, 2 = middle, 3 = right)
-   `keys` - A dictionary of keys including 'shift', 'alt', 'ctrl', 'meta'. Each key's value is a boolean indicating if it was pressed during the click event. The meta key on a mac is the Command key

**mouse\_up(x, y, button, keys)**

When a mouse button is released on this component

-   `x` - The x coordinate of the mouse pointer within this component
-   `y` - The y coordinate of the mouse pointer within this component
-   `button` - The button that was released (1 = left, 2 = middle, 3 = right)
-   `keys` - A dictionary of keys including 'shift', 'alt', 'ctrl', 'meta'. Each key's value is a boolean indicating if it was pressed during the click event. The meta key on a mac is the Command key

---

### `CheckBox` [(more info)](https://anvil.works/doc#checkbox)

-   [Methods](#CheckBox_methods)
-   [Properties](#CheckBox_attributes)
-   [Events](#CheckBox_events)

---

Create a new ‘CheckBox’ object

---

##### Base class: anvil.Component

#### Constructor

`CheckBox([checked=], [allow_indeterminate=], [enabled=], [spacing_above=], [spacing_below=], [spacing=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### CheckBox Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**focus()**

Set the keyboard focus to this component

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### CheckBox Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**allow\_indeterminate** - *boolean*

Support an indeterminate state. The indeterminate state can only be set in code by setting checked=None.

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**checked** - *boolean*

The status of the checkbox

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**italic** - *boolean*

Display this component’s text in italics

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### CheckBox Events

**change()**

When this checkbox is checked or unchecked

**show()**

When the CheckBox is shown on the screen

**hide()**

When the CheckBox is removed from the screen

---

### `Classes`

-   [Methods](#Classes_methods)

---

Create a live class-list helper. `value` may be `None`, a string, a list of strings, a dictionary of class names to booleans, or another `Classes` object.

#### Constructor

`Classes([value=None])`

---

#### Instance Methods

**add(value)**

Add one or more class names. Strings are split on whitespace; duplicate classes are ignored.

**clear()**

Remove all class names.

**remove(value)**

Remove one or more class names. Missing classes are ignored.

**update(updates=None, \*\*kwargs)**

Merge class names into this class-list helper. Truthy values add classes; falsey values remove them.

---

### `ColumnPanel` [(more info)](https://anvil.works/doc#columnpanel)

-   [Methods](#ColumnPanel_methods)
-   [Properties](#ColumnPanel_attributes)
-   [Events](#ColumnPanel_events)

---

Create a new ‘ColumnPanel’ object

---

##### Base class: anvil.Container

#### Constructor

`ColumnPanel([col_widths=], [wrap_on=], [col_spacing=], [spacing_above=], [spacing_below=], [spacing=], [background=], [foreground=], [border=], [visible=], [role=], [tag=], [tooltip=])`

---

#### ColumnPanel Methods

**add\_component(component, \[index=None\], full\_width\_row=False, \*\*layout\_props)**

Add a component to this ColumnPanel at the ‘index’th position. If ‘index’ is not specified, adds to the bottom. Useful layout properties:

full\_width\_row = True|False row\_background = \[colour\]

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### ColumnPanel Properties

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**col\_spacing** - *enum: `"none"`, `"tiny"`, `"small"`, `"medium"`, `"large"`, `"huge"`*

Space between columns

**col\_widths** - *string*

Custom column widths in this panel

**foreground** - *color*

The foreground colour of this component.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

**wrap\_on** - *enum: `"never"`, `"mobile"`, `"tablet"`*

The largest display on which to wrap columns in this panel

---

#### ColumnPanel Events

**show()**

When the ColumnPanel is shown on the screen

**hide()**

When the ColumnPanel is removed from the screen

---

### `Component`

-   [Methods](#Component_methods)

---

Create a new ‘Component’ object

#### Constructor

`Component()`

---

#### Instance Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**get\_event\_handlers(event\_name) → tuple\_of\_event\_handlers**

Get the current event\_handlers for a given event\_name

**raise\_event(event\_name, \*\*event\_args)**

Trigger the event on this component. Any keyword arguments are passed to the handler function.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**remove\_from\_parent()**

Remove this component from its parent container.

**scroll\_into\_view(smooth=False, align="center")**

Scroll the window to make sure this component is in view.

-   `smooth` - Determines whether the scroll should be smooth or instant.
    
-   `align` - Determines where the component should be aligned within the viewport. Options are 'start', 'center', 'end', and 'nearest'.
    

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

### `Container`

-   [Methods](#Container_methods)

---

Create a new ‘Container’ object

---

##### Base class: anvil.Component

#### Constructor

`Container()`

---

#### Instance Methods

**add\_component(component)**

Add a component to this container.

**clear()**

Remove all components from this container

**get\_components()**

Get a list of components in this container

**raise\_event\_on\_children(event\_name, \*\*event\_args)**

Trigger the ’event\_name’ event on all children of this component. Any keyword arguments are passed to the handler function.

---

### `DataGrid` [(more info)](https://anvil.works/doc#datagrid)

-   [Methods](#DataGrid_methods)
-   [Properties](#DataGrid_attributes)
-   [Events](#DataGrid_events)

---

Create a new ‘DataGrid’ object

---

##### Base class: anvil.Container

#### Constructor

`DataGrid([columns=], [auto_header=], [show_page_controls=], [rows_per_page=], [wrap_on=], [spacing_above=], [spacing_below=], [margin=], [background=], [foreground=], [border=], [visible=], [role=], [tag=], [tooltip=])`

---

#### DataGrid Methods

**add\_component(component, \[index=None\], \[pinned=False\])**

Add a component to this DataGrid, in the ‘index’th position. If ‘index’ is not specified, adds to the bottom.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**get\_page()**

Get the current page number of this DataGrid

**jump\_to\_first\_page()**

Jump to the first page of this DataGrid

**jump\_to\_last\_page()**

Jump to the last page of this DataGrid

**next\_page()**

Jump to the next page of this DataGrid

**previous\_page()**

Jump to the previous page of this DataGrid

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

**set\_page(page)**

Set the page number of this DataGrid. The page number must be positive

---

#### DataGrid Properties

**auto\_header** - *boolean*

Whether to display an automatic header at the top of this Data Grid.

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**columns** - *dataGridColumns*

A list of columns to display in this Data Grid.

**foreground** - *color*

The foreground colour of this component.

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**rows\_per\_page** - *number*

The maximum number of rows to display at one time.

**show\_page\_controls** - *boolean*

Whether to display the next/previous page buttons.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

**wrap\_on** - *enum: `"never"`, `"mobile"`, `"tablet"`*

The largest display on which to wrap columns in this DataGrid

---

#### DataGrid Events

**show()**

When the DataGrid is shown on the screen

**hide()**

When the DataGrid is removed from the screen

---

### `DataRowPanel` [(more info)](https://anvil.works/doc#datarowpanel)

-   [Methods](#DataRowPanel_methods)
-   [Properties](#DataRowPanel_attributes)
-   [Events](#DataRowPanel_events)

---

Create a new ‘DataRowPanel’ object

---

##### Base class: anvil.Container

#### Constructor

`DataRowPanel([item=], [auto_display_data=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [spacing_above=], [spacing_below=], [margin=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### DataRowPanel Methods

**add\_component(component, \[column=None\])**

Add a component to the specified column of this DataRowPanel. TODO: If ‘column’ is not specified, adds the component full-width.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### DataRowPanel Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**auto\_display\_data** - *boolean*

Whether to automatically display data in this row.

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**italic** - *boolean*

Display this component’s text in italics

**item** - *object*

The data to display in this row by default.

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### DataRowPanel Events

**show()**

When the DataRowPanel is shown on the screen

**hide()**

When the DataRowPanel is removed from the screen

---

### `DatePicker` [(more info)](https://anvil.works/doc#datepicker)

-   [Methods](#DatePicker_methods)
-   [Properties](#DatePicker_attributes)
-   [Events](#DatePicker_events)

---

Create a new ‘DatePicker’ object

---

##### Base class: anvil.Component

#### Constructor

`DatePicker([date=], [format=], [pick_time=], [min_date=], [max_date=], [placeholder=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [spacing_above=], [spacing_below=], [margin=], [enabled=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### DatePicker Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**focus()**

Set the keyboard focus to this DatePicker

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### DatePicker Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**date** - *string*

The date selected on this component.

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**format** - *string*

The format in which to display the selected date.

**italic** - *boolean*

Display this component’s text in italics

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**max\_date** - *string*

The maximum date the user can select.

**min\_date** - *string*

The minimum date the user can select.

**parent**

**pick\_time** - *boolean*

Whether the user should be able to select a time as well as a date

**placeholder** - *string*

A string to display when the DatePicker is empty.

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### DatePicker Events

**change()**

When the selected date changes

**show()**

When the DatePicker is shown on the screen

**hide()**

When the DatePicker is removed from the screen

---

### `DropDown` [(more info)](https://anvil.works/doc#dropdown)

-   [Methods](#DropDown_methods)
-   [Properties](#DropDown_attributes)
-   [Events](#DropDown_events)

---

Create a new ‘DropDown’ object

---

##### Base class: anvil.Component

#### Constructor

`DropDown([items=], [selected_value=], [include_placeholder=], [placeholder=], [spacing_above=], [spacing_below=], [margin=], [enabled=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [background=], [foreground=], [border=], [visible=], [role=], [tag=], [tooltip=])`

---

#### DropDown Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**focus()**

Set the keyboard focus to this component

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### DropDown Properties

**align** - *enum: `"left"`, `"center"`, `"right"`, `"full"`*

The position of this dropdown in the available space.

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**include\_placeholder** - *boolean*

Whether to add a placeholder item to the list with value None

**italic** - *boolean*

Display this component’s text in italics

**items** - *text\[\]*

The items to display in this dropdown.

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**placeholder** - *string*

The text to be displayed when the selected\_value is None.

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**selected\_value** - *object*

The value of the currently selected item. Can only be set at runtime.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### DropDown Events

**change()**

When an item is selected

**show()**

When the DropDown is shown on the screen

**hide()**

When the DropDown is removed from the screen

---

### `FileLoader` [(more info)](https://anvil.works/doc#fileloader)

-   [Methods](#FileLoader_methods)
-   [Properties](#FileLoader_attributes)
-   [Events](#FileLoader_events)

---

Create a new ‘FileLoader’ object

---

##### Base class: anvil.Component

#### Constructor

`FileLoader([multiple=], [show_state=], [file=], [files=], [file_types=], [spacing_above=], [spacing_below=], [spacing=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [background=], [foreground=], [border=], [visible=], [role=], [icon=], [icon_align=], [enabled=], [tag=], [tooltip=])`

---

#### FileLoader Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**clear()**

Clear any selected files from this FileLoader

**focus()**

Set the keyboard focus to this FileLoader

**open\_file\_selector()**

Open the file selector from code, this should be called within a click event handler for another component

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### FileLoader Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**enabled** - *boolean*

True if this component should allow user interaction.

**file** - *anvil.Media instance*

The currently selected file (or the first, if multiple files are selected). This is a Media object.

**file\_types** - *string*

Specify what type of file to upload. Can accept a MIME type (eg “image/png” or “image/\*”), or an extension (eg “.png”), or a comma-separated set of them (eg “.png,.jpg,.jpeg”)

**files** - *list(anvil.Media instance)*

A list of currently selected files. Each file is a Media object.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**icon** - *icon*

The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.

**icon\_align** - *enum: `"left_edge"`, `"left"`, `"top"`, `"right"`, `"right_edge"`*

The alignment of the icon on this component. Set to ’top’ for a centred icon on a component with no text.

**italic** - *boolean*

Display this component’s text in italics

**multiple** - *boolean*

If True, this FileLoader can load multiple files at the same time

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**show\_state** - *boolean*

If True, display a message describing selected files.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### FileLoader Events

**change(file, files)**

When a new file is loaded into this FileLoader

-   `file` - The first selected file. Set the 'multiple' property to allow loading more than one file.
-   `files` - A list of loaded files. Set the 'multiple' property to allow loading more than one file.

**show()**

When the FileLoader is shown on the screen

**hide()**

When the FileLoader is removed from the screen

**focus()**

When the FileLoader gets focus

**lost\_focus()**

When the FileLoader loses focus

---

### `FlowPanel` [(more info)](https://anvil.works/doc#flowpanel)

-   [Methods](#FlowPanel_methods)
-   [Properties](#FlowPanel_attributes)
-   [Events](#FlowPanel_events)

---

Create a new ‘FlowPanel’ object

---

##### Base class: anvil.Container

#### Constructor

`FlowPanel([align=], [vertical_align=], [gap=], [background=], [foreground=], [border=], [visible=], [role=], [tag=], [spacing_above=], [spacing_below=], [spacing=], [tooltip=])`

---

#### FlowPanel Methods

**add\_component(component, \[index=\], \[width=\], \[expand=\])**

Add a component to this panel. Optionally specify the position in the panel to add it, or the width to apply to components that can’t self-size width-wise.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### FlowPanel Properties

**align** - *enum: `"left"`, `"center"`, `"right"`, `"justify"`*

Align this component’s content

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**foreground** - *color*

The foreground colour of this component.

**gap** - *enum: `"none"`, `"tiny"`, `"small"`, `"medium"`, `"large"`, `"huge"`*

Gap between components

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**vertical\_align** - *enum: `"top"`, `"middle"`, `"bottom"`, `"full"`*

Align this component’s content

**visible** - *boolean*

Should this component be displayed?

---

#### FlowPanel Events

**show()**

When the FlowPanel is shown on the screen

**hide()**

When the FlowPanel is removed from the screen

---

### `GoogleMap` [(more info)](https://anvil.works/doc#googlemap)

-   [Methods](#GoogleMap_methods)
-   [Properties](#GoogleMap_attributes)
-   [Events](#GoogleMap_events)

---

Create a new ‘GoogleMap’ object

---

##### Base class: anvil.Container

#### Constructor

`GoogleMap([map_data=], [background_color=], [center=], [clickable_icons=], [disable_default_ui=], [disable_double_click_zoom=], [draggable=], [draggable_cursor=], [dragging_cursor=], [fullscreen_control=], [fullscreen_control_options=], [gesture_handling=], [heading=], [keyboard_shortcuts=], [map_type_control=], [map_type_control_options=], [map_type_id=], [max_zoom=], [min_zoom=], [rotate_control=], [rotate_control_options=], [scale_control=], [scale_control_options=], [scroll_wheel=], [street_view_control=], [street_view_control_options=], [zoom=], [zoom_control=], [zoom_control_options=], [spacing_above=], [spacing_below=], [margin=], [height=], [visible=], [tag=])`

---

#### GoogleMap Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**compute\_area()**

Returns the area of a closed path in square meters.

**compute\_length()**

Returns the length of a path in meters.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### GoogleMap Properties

**background\_color** - *string*

Color used for the background of the Map div. This color will be visible when tiles have not yet loaded as the user pans.

**center** - *anvil.GoogleMap.LatLng instance*

The Map center.

**clickable\_icons** - *boolean*

When false, map icons are not clickable. A map icon represents a point of interest

**disable\_default\_ui** - *boolean*

Enables/disables all default UI.

**disable\_double\_click\_zoom** - *boolean*

Enables/disables zoom and center on double click.

**draggable** - *boolean*

If false, prevents the map from being dragged.

**draggable\_cursor** - *string*

The name or url of the cursor to display when mousing over a draggable map.

**dragging\_cursor** - *string*

The name or url of the cursor to display when the map is being dragged.

**fullscreen\_control** - *boolean*

The enabled/disabled state of the Fullscreen control.

**fullscreen\_control\_options** - *anvil.GoogleMap.FullscreenControlOptions instance*

The display options for the Fullscreen control.

**gesture\_handling** - *string*

This setting controls how gestures on the map are handled.

**heading** - *number*

The heading for aerial imagery in degrees measured clockwise from cardinal direction North.

**height** - *string*

The height of this component.

**keyboard\_shortcuts** - *boolean*

If false, prevents the map from being controlled by the keyboard.

**map\_data** - *anvil.GoogleMap.Data instance*

Map data

**map\_type\_control** - *boolean*

The enabled/disabled state of the Map type control.

**map\_type\_control\_options** - *anvil.GoogleMap.MapTypeControlOptions instance*

The display options for the Map type control.

**map\_type\_id** - *anvil.GoogleMap.MapTypeId*

The map type ID. Defaults to MapTypeId.ROADMAP

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**max\_zoom** - *number*

The maximum zoom level which will be displayed on the map.

**min\_zoom** - *number*

The minimum zoom level which will be displayed on the map.

**parent**

**rotate\_control** - *boolean*

The enabled/disabled state of the rotate control.

**rotate\_control\_options** - *anvil.GoogleMap.RotateControlOptions instance*

The display options for the rotate control.

**scale\_control** - *boolean*

The enabled/disabled state of the scale control.

**scale\_control\_options** - *anvil.GoogleMap.ScaleControlOptions instance*

The display options for the scale control.

**scroll\_wheel** - *boolean*

If false, disables scrollwheel zooming on the map.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**street\_view\_control** - *boolean*

The enabled/disabled state of the street view control.

**street\_view\_control\_options** - *anvil.GoogleMap.StreetViewControlOptions instance*

The display options for the street view control.

**tag** - *object*

Use this property to store any extra information about this component

**visible** - *boolean*

Should this component be displayed?

**zoom** - *number*

The map zoom level.

**zoom\_control** - *boolean*

The enabled/disabled state of the zoom control.

**zoom\_control\_options** - *anvil.GoogleMap.ZoomControlOptions instance*

The display options for the zoom control.

---

#### GoogleMap Events

**bounds\_changed()**

when the viewport bounds have changed.

**center\_changed()**

when the map center property changes.

**click(lat\_lng, pixel)**

when the user clicks on the map.

-   `lat_lng` - The position that was clicked.
-   `pixel` - The position that was clicked.

**dbl\_click(lat\_lng, pixel)**

when the user double-clicks on the map.

-   `lat_lng` - The position that was double-clicked.
-   `pixel` - The position that was double-clicked.

**drag()**

This event is repeatedly fired while the user drags the map.

**dragend()**

when the user stops dragging the map.

**dragstart()**

when the user starts dragging the map.

**heading\_changed()**

when the map heading property changes.

**idle()**

when the map becomes idle after panning or zooming.

**maptypeid\_changed()**

when the mapTypeId property changes.

**mousemove(lat\_lng, pixel)**

whenever the user's mouse moves over the map container.

-   `lat_lng` - The position of the cursor.
-   `pixel` - The position of the cursor.

**mouseout(lat\_lng, pixel)**

when the user's mouse exits the map container.

-   `lat_lng` - The position of the cursor.
-   `pixel` - The position of the cursor.

**mouseover(lat\_lng, pixel)**

when the user's mouse enters the map container.

-   `lat_lng` - The position of the cursor.
-   `pixel` - The position of the cursor.

**projection\_changed()**

when the projection has changed.

**rightclick(lat\_lng, pixel)**

when the user right-clicks on the map container.

-   `lat_lng` - The position that was right-clicked.
-   `pixel` - The position that was right-clicked.

**tilesloaded()**

when the visible tiles have finished loading.

**tilt\_changed()**

when the map tilt property changes.

**zoom\_changed()**

when the map zoom property changes.

**data\_addfeature(feature)**

when the viewport bounds have changed.

-   `feature` - The feature that was added.

**data\_click(feature, lat\_lng)**

for a click on the geometry.

-   `feature` - The feature that was clicked.
-   `lat_lng` - The position that was clicked.

**data\_dbl\_click(feature, lat\_lng)**

for a double click on the geometry.

-   `feature` - The feature that was double-clicked.
-   `lat_lng` - The position that was double-clicked.

**data\_mousedown(feature, lat\_lng)**

for a mousedown on the geometry.

-   `feature` - The feature the mouse is over.
-   `lat_lng` - The position of the cursor.

**data\_mouseout(feature, lat\_lng)**

when the mouse leaves the area of the geometry.

-   `feature` - The feature the mouse left.
-   `lat_lng` - The position of the cursor.

**data\_mouseover(feature, lat\_lng)**

when the mouse enters the area of the geometry.

-   `feature` - The feature the mouse is over.
-   `lat_lng` - The position of the cursor.

**data\_mouseup(feature, lat\_lng)**

for a mouseup on the geometry.

-   `feature` - The feature the mouse is over.
-   `lat_lng` - The position of the cursor.

**data\_removefeature(feature)**

when a feature is removed from the collection.

-   `feature` - The feature that was removed.

**data\_removeproperty(feature, name, old\_value)**

when a feature's property is removed.

-   `feature` - The feature whose property was removed.
-   `name` - The name of the property that was removed.
-   `old_value` - The old value of the property that was removed.

**data\_rightclick(feature, lat\_lng)**

for a right-click on the geometry.

-   `feature` - The feature that was right-clicked.
-   `lat_lng` - The position that was right-clicked.

**data\_setgeometry(feature, new\_geometry, old\_geometry)**

when a feature's geometry is set.

-   `feature` - The feature that was removed.
-   `new_geometry` - The geometry that was set.
-   `old_geometry` - The geometry that was replaced.

**data\_setproperty(feature, name, new\_value, old\_value)**

when a feature's property is set.

-   `feature` - The feature whose property was set.
-   `name` - The name of the property that was set.
-   `new_value` - The new value of the property that was set.
-   `old_value` - The old value of the property that was set.

**show()**

When the GoogleMap is shown on the screen

**hide()**

When the GoogleMap is removed from the screen

---

### `GridPanel` [(more info)](https://anvil.works/doc#gridpanel)

-   [Methods](#GridPanel_methods)
-   [Properties](#GridPanel_attributes)
-   [Events](#GridPanel_events)

---

Create a new ‘GridPanel’ object

---

##### Base class: anvil.Container

#### Constructor

`GridPanel([spacing_above=], [spacing_below=], [spacing=], [background=], [foreground=], [border=], [visible=], [role=], [tag=], [tooltip=])`

---

#### GridPanel Methods

**add\_component(component, \[row=\], \[col\_xs=\], \[width\_xs=\])**

Add a component to this GridPanel

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### GridPanel Properties

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**foreground** - *color*

The foreground colour of this component.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### GridPanel Events

**show()**

When the GridPanel is shown on the screen

**hide()**

When the GridPanel is removed from the screen

---

### `HtmlComponent` [(more info)](https://anvil.works/doc#htmlcomponent)

-   [Methods](#HtmlComponent_methods)
-   [Properties](#HtmlComponent_attributes)

---

Create a new ‘HtmlComponent’ object

---

##### Base class: anvil.Container

#### Constructor

`HtmlComponent([visible=], [tag=], [html=], [classes=], [style=])`

---

#### HtmlComponent Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### HtmlComponent Properties

**classes** - *anvil.Classes instance*

The class names applied to this HtmlComponent’s root element.

**html** - *html*

The HTML from which this component is defined.

**parent**

**style** - *anvil.Style instance*

The inline styles applied to this HtmlComponent’s root element.

**tag** - *object*

Use this property to store any extra information about this component

**visible** - *boolean*

Should this component be displayed?

---

### `HtmlTemplate` [(more info)](https://anvil.works/doc#htmltemplate)

-   [Methods](#HtmlTemplate_methods)
-   [Properties](#HtmlTemplate_attributes)
-   [Events](#HtmlTemplate_events)

---

Create a new ‘HtmlTemplate’ object

---

##### Base class: anvil.Container

#### Constructor

`HtmlTemplate([html=], [tag=], [tooltip=], [background=], [foreground=], [border=], [visible=], [role=])`

---

#### HtmlTemplate Methods

**add\_component(component, \[slot="default"\])**

Add a component to the named slot of this HTML templated panel. If no slot is specified, the ‘default’ slot will be used.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**call\_js(js\_function\_name, \*args)**

Call a Javascript function

**clear(\[slot="default"\])**

clear the HTML template of all components or clear a specific slot of components.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### HtmlTemplate Properties

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**dom\_nodes** - *dict*

A read-only dictionary allowing you to look up the DOM node by name for any HTML tag in this component’s HTML that has an anvil-name= attribute.

**foreground** - *color*

The foreground colour of this component.

**html** - *html*

The HTML from which this panel is defined

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### HtmlTemplate Events

**show()**

When the HtmlTemplate is shown on the screen

**hide()**

When the HtmlTemplate is removed from the screen

---

### `Image` [(more info)](https://anvil.works/doc#image)

-   [Methods](#Image_methods)
-   [Properties](#Image_attributes)
-   [Events](#Image_events)

---

Create a new ‘Image’ object

---

##### Base class: anvil.Component

#### Constructor

`Image([alt_text=], [display_mode=], [border_radius=], [horizontal_align=], [vertical_align=], [source=], [spacing_above=], [spacing_below=], [margin=], [height=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### Image Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### Image Properties

**alt\_text** - *string*

Textual replacement for the image used by screen readers and displayed on the page if the image can’t be loaded

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**border\_radius** - *string*

The border radius of this component

**display\_mode** - *enum: `"shrink_to_fit"`, `"zoom_to_fill"`, `"fill_width"`, `"original_size"`*

Determines how the image’s size should be adjusted to fit the size of this Image component.

-   `shrink_to_fit` scales the image to fit while maintaining its aspect ratio.
-   `zoom_to_fill` scales the image to fill the entire container while maintaining its aspect ratio. If the image is too large, it will be cropped to fit.
-   `fill_width` shrinks or grows the image so the width fits the container.
-   `original_size` - displays the image at whatever the browser thinks the original size is. If that would cause the image to be wider than the Image component, it shrinks the image to ensure it fits within the width of the Image component.

**foreground** - *color*

The foreground colour of this component.

**height** - *string*

The height of this component.

**horizontal\_align** - *enum: `"left"`, `"center"`, `"right"`*

Position the image horizontally within this component

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**source** - *uri*

The image source - set a string for a URL or a Media object in code

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**vertical\_align** - *enum: `"top"`, `"center"`, `"bottom"`*

Position the image vertically within this component

**visible** - *boolean*

Should this component be displayed?

---

#### Image Events

**show()**

When the Image is shown on the screen

**hide()**

When the Image is removed from the screen

**mouse\_enter(x, y)**

When the mouse cursor enters this component

-   `x` - The x coordinate of the mouse pointer, within this component
-   `y` - The y coordinate of the mouse pointer, within this component

**mouse\_leave(x, y)**

When the mouse cursor leaves this component

-   `x` - The x coordinate of the mouse pointer relative to this component
-   `y` - The y coordinate of the mouse pointer relative to this component

**mouse\_move(x, y)**

When the mouse cursor moves over this component

-   `x` - The x coordinate of the mouse pointer within this component
-   `y` - The y coordinate of the mouse pointer within this component

**mouse\_down(x, y, button, keys)**

When a mouse button is pressed on this component

-   `x` - The x coordinate of the mouse pointer within this component
-   `y` - The y coordinate of the mouse pointer within this component
-   `button` - The button that was pressed (1 = left, 2 = middle, 3 = right)
-   `keys` - A dictionary of keys including 'shift', 'alt', 'ctrl', 'meta'. Each key's value is a boolean indicating if it was pressed during the click event. The meta key on a mac is the Command key

**mouse\_up(x, y, button, keys)**

When a mouse button is released on this component

-   `x` - The x coordinate of the mouse pointer within this component
-   `y` - The y coordinate of the mouse pointer within this component
-   `button` - The button that was released (1 = left, 2 = middle, 3 = right)
-   `keys` - A dictionary of keys including 'shift', 'alt', 'ctrl', 'meta'. Each key's value is a boolean indicating if it was pressed during the click event. The meta key on a mac is the Command key

---

### `Label` [(more info)](https://anvil.works/doc#label)

-   [Methods](#Label_methods)
-   [Properties](#Label_attributes)
-   [Events](#Label_events)

---

Create a new ‘Label’ object

---

##### Base class: anvil.Component

#### Constructor

`Label([spacing_above=], [spacing_below=], [spacing=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [background=], [foreground=], [border=], [visible=], [role=], [icon=], [icon_align=], [tooltip=], [tag=])`

---

#### Label Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### Label Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**icon** - *icon*

The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.

**icon\_align** - *enum: `"left_edge"`, `"left"`, `"top"`, `"right"`, `"right_edge"`*

The alignment of the icon on this component. Set to ’top’ for a centred icon on a component with no text.

**italic** - *boolean*

Display this component’s text in italics

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### Label Events

**show()**

When the Label is shown on the screen

**hide()**

When the Label is removed from the screen

---

### `LinearPanel` [(more info)](https://anvil.works/doc#linearpanel)

-   [Methods](#LinearPanel_methods)
-   [Properties](#LinearPanel_attributes)
-   [Events](#LinearPanel_events)

---

Create a new ‘LinearPanel’ object

---

##### Base class: anvil.Container

#### Constructor

`LinearPanel([spacing_above=], [spacing_below=], [spacing=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### LinearPanel Methods

**add\_component(component, \[index=None\])**

Add a component to this LinearPanel, in the ‘index’th position. If ‘index’ is not specified, adds to the bottom.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### LinearPanel Properties

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**foreground** - *color*

The foreground colour of this component.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### LinearPanel Events

**show()**

When the LinearPanel is shown on the screen

**hide()**

When the LinearPanel is removed from the screen

---

### `Link` [(more info)](https://anvil.works/doc#link)

-   [Methods](#Link_methods)
-   [Properties](#Link_attributes)
-   [Events](#Link_events)

---

Create a new ‘Link’ object

---

##### Base class: anvil.ColumnPanel

#### Constructor

`Link([url=], [text_padding=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [icon=], [icon_align=], [tooltip=], [tag=])`

---

#### Link Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### Link Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**bold** - *boolean*

Display this component’s text in bold

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**icon** - *icon*

The icon to display on this component. Either a URL, or a FontAwesome Icon, e.g. ‘fa:user’.

**icon\_align** - *enum: `"left_edge"`, `"left"`, `"top"`, `"right"`, `"right_edge"`*

The alignment of the icon on this component. Set to ’top’ for a centred icon on a component with no text.

**italic** - *boolean*

Display this component’s text in italics

**parent**

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**text\_padding** - *padding*

Padding for the link text. Only available in apps that have been migrated to use Layouts.

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**url** - *string*

The target URL of the link. Can be set to a URL string or to a Media object.

---

#### Link Events

**click(keys)**

When the link is clicked

-   `keys` - A dictionary of keys including 'shift', 'alt', 'ctrl', 'meta'. Each key's value is a boolean indicating if it was pressed during the click event. The meta key on a mac is the Command key

---

### `Media`

-   [Methods](#Media_methods)
-   [Attributes](#Media_attributes)

---

Create a new ‘Media’ object

#### Constructor

`Media()`

---

#### Instance Methods

**get\_bytes()**

Get a binary string of the data represented by this Media object

**get\_url()**

Get a Media object’s URL, or None if there isn’t one associated with it.

---

#### Media Attributes

**content\_type** - *string*

The MIME type of this Media

**length** - *number*

The length of this Media, in bytes

**name** - *string*

The file name associated with this Media, or None if it has no name

**url** - *string*

The URL where you can download this Media, or None if it is not downloadable

---

### `Notification`

-   [Methods](#Notification_methods)

---

Create a popup notification. Call the show() method to display it.

#### Constructor

`Notification(message, [title=""], [style="info"], [timeout=2])`

---

#### Instance Methods

**\_\_enter\_\_() → anvil.Notification instance**

Show the notification when entering a ‘with’ block

**\_\_exit\_\_() → anvil.Notification instance**

Hide the notification when exiting a ‘with’ block

**hide()**

Hides the notification immediately

**show() → anvil.Notification instance**

Shows the notification

---

### `Plot` [(more info)](https://anvil.works/doc#plot)

-   [Methods](#Plot_methods)
-   [Properties](#Plot_attributes)
-   [Events](#Plot_events)

---

Create a new ‘Plot’ object

---

##### Base class: anvil.Component

#### Constructor

`Plot([data=], [layout=], [config=], [figure=], [interactive=], [spacing_above=], [spacing_below=], [margin=], [height=], [visible=], [tooltip=], [tag=])`

---

#### Plot Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**extend\_traces(data, traces)**

Adds data to an existing trace.

**prepend\_traces(data, traces)**

Prepends data to an existing trace.

**redraw()**

Redraws the chart. Call this function if you have updated data or layout properties.

**relayout(update)**

A more efficient means of updating just the layout in a graphDiv. The call signature and arguments for relayout are similar (but simpler) to restyle.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**restyle(update, traces)**

A more efficient means of changing attributes in the data array. When restyling, you may choose to have the specified changes effect as many traces as desired.

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

**to\_image(options) → anvil.URLMedia instance**

Returns a Media object containing a snapshot of this plot. The argument is a dictionary specifying image options.

---

#### Plot Properties

**config** - *dict*

Plot config

**data** - *object*

Plot traces

**figure** - *dict*

The Plotly figure to display. Specifies layout and data.

**height** - *string*

The height of this component.

**interactive** - *boolean*

Whether this plot should be interactive

**layout** - *plotly.graph\_objs.Layout instance*

Plot layout

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**templates** - *mapping*

plotly templates, see plotly docs for valid template names. Set the default template using Plot.templates.default = ‘seaborn’.

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### Plot Events

**click(points)**

when a data point is clicked.

-   `points` - A list of the data points that were clicked.

**double\_click()**

when the plot is double-clicked.

**afterplot()**

after then plot is redrawn.

**select(points)**

when a data point is selected.

-   `points` - A list of the data points that were selected.

**hover(points)**

when a data point is hovered.

-   `points` - A list of the data points that were hovered.

**unhover(points)**

when a data point is unhovered.

-   `points` - A list of the data points that were unhovered.

**show()**

When the Plot is shown on the screen

**hide()**

When the Plot is removed from the screen

---

### `RadioButton` [(more info)](https://anvil.works/doc#radiobutton)

-   [Methods](#RadioButton_methods)
-   [Properties](#RadioButton_attributes)
-   [Events](#RadioButton_events)

---

Create a new ‘RadioButton’ object

---

##### Base class: anvil.Component

#### Constructor

`RadioButton([selected=], [value=], [group_name=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [spacing_above=], [spacing_below=], [spacing=], [enabled=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### RadioButton Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**get\_group\_value() → str**

returns the value of the button in the group which is pressed.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### RadioButton Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**group\_name** - *string*

The name of the group this radio button belongs to.

**italic** - *boolean*

Display this component’s text in italics

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**selected** - *boolean*

The status of the radio button

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**value** - *string*

The value of the group when this radio button is selected

**visible** - *boolean*

Should this component be displayed?

---

#### RadioButton Events

**clicked()**

When this radio button is selected

**show()**

When the RadioButton is shown on the screen

**hide()**

When the RadioButton is removed from the screen

---

### `RepeatingPanel` [(more info)](https://anvil.works/doc#repeatingpanel)

-   [Methods](#RepeatingPanel_methods)
-   [Properties](#RepeatingPanel_attributes)
-   [Events](#RepeatingPanel_events)

---

Create a new ‘RepeatingPanel’ object

---

##### Base class: anvil.Component

#### Constructor

`RepeatingPanel([item_template=], [items=], [background=], [foreground=], [border=], [visible=], [role=], [spacing_above=], [spacing_below=], [margin=], [tooltip=], [tag=])`

---

#### RepeatingPanel Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**get\_components()**

Get the list of components created by this Repeating Panel. Each will be an instance of ‘item\_template’, one for each item in ‘items’.

**raise\_event\_on\_children(event\_name, \*\*event\_args)**

Trigger the ’event\_name’ event on all children of this component. Any keyword arguments are passed to the handler function.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### RepeatingPanel Properties

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**foreground** - *color*

The foreground colour of this component.

**item\_template** - *form*

The name of the form to repeat for every item

**items** - *object*

A list of items for which the ‘item\_template’ will be instantiated.

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### RepeatingPanel Events

**show()**

When the RepeatingPanel is shown on the screen

**hide()**

When the RepeatingPanel is removed from the screen

---

### `RichText` [(more info)](https://anvil.works/doc#richtext)

-   [Methods](#RichText_methods)
-   [Properties](#RichText_attributes)
-   [Events](#RichText_events)

---

Create a new ‘RichText’ object

---

##### Base class: anvil.Container

#### Constructor

`RichText([content=], [format=], [enable_slots=], [data=], [align=], [font_size=], [font=], [spacing_above=], [spacing_below=], [spacing=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### RichText Methods

**add\_component(component, slot)**

Add a component to this panel, in the specified slot

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**clear(\[slot="slot\_name"\])**

clear the Rich Text Component of all components or clear a specific slot of components.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### RichText Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**content** - *string*

The content to render in this component, in the format specified by the ‘format’ property

**data** - *object*

A dict of data or Components to populate the named content {slots}. Can also be a dict-like object.

**enable\_slots** - *boolean*

If true {braces} in content define slots. If false, braces in content display normally.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**format** - *enum: `"markdown"`, `"plain_text"`, `"restricted_html"`*

The format of the content of this component.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing** - *spacing*

Margin and padding for this container. Only available in apps that have been migrated to use Layouts.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### RichText Events

**show()**

When the RichText is shown on the screen

**hide()**

When the RichText is removed from the screen

---

### `Slot`

-   [Methods](#Slot_methods)

---

A Slot class represents a way to add components to an underlying container. You will rarely instantiate a Slot on its own; instead your form’s layout will contain Slots to which you can add components.

#### Constructor

`Slot(target_container, insertion_index, [layout_properties])`

-   `target_container` - The target container into which components added to this slot will be added.
    
-   `insertion_index` - The starting index (within the target container) at which components added to this slot will be inserted.
    
-   `layout_properties` - A dictionary of layout properties that will be passed as keyword arguments to the target container's add\_component() call, overriding any values provided to the slot's add\_component().
    

---

#### Instance Methods

**add\_component(component, \[index=None\], \*\*layout\_properties)**

Add a component to this slot.

Calling add\_component() on a Slot will add the specified component to its target container.

-   `component` - The component to add to this slot.
    
-   `index` - The index, within the slot, at which the component is to be inserted. Note: This argument is index is within the Slot, not within the target container. The Slot will adjust for its own insertion\_index, as well as components in any previous slots registered with offset\_by\_slot(), when computing the index= parameter to the target container's add\_component() method.
    
-   `layout_properties` - Layout properties will be passed on as keyword arguments to the target container's add\_component() method, unless overridden by the Slot.
    

**offset\_by\_slot(offset\_by\_slot)**

Inform this Slot of an earlier Slot with the same target container. Future calls to add\_component() will take account of any components inserted into the earlier slot when calculating the insertion index for the target container, thereby preserving ordering between the two slots’ components.

---

### `Spacer` [(more info)](https://anvil.works/doc#spacer)

-   [Methods](#Spacer_methods)
-   [Properties](#Spacer_attributes)
-   [Events](#Spacer_events)

---

Create a new ‘Spacer’ object

---

##### Base class: anvil.Component

#### Constructor

`Spacer([visible=], [spacing_above=], [spacing_below=], [height=], [tooltip=], [tag=])`

---

#### Spacer Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### Spacer Properties

**height** - *string*

The height of this component.

**parent**

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### Spacer Events

**show()**

When the Spacer is shown on the screen

**hide()**

When the Spacer is removed from the screen

---

### `Style`

-   [Methods](#Style_methods)

---

Create a live style helper. `value` may be `None`, a CSS string, a dictionary of CSS property names to values, or another `Style` object.

#### Constructor

`Style([value=None])`

---

#### Instance Methods

**clear()**

Remove all CSS properties.

**get(property, \[default=""\])**

Return a CSS property value, or `default` when it is not set.

**items() → iterator**

Return an iterator over `(property, value)` pairs for this style object.

**keys() → iterator\[string\]**

Return an iterator over the CSS property names in this style object.

**update(updates=None, \*\*kwargs)**

Merge CSS properties into this style object. `None` or empty values remove properties.

**values() → iterator\[string\]**

Return an iterator over the CSS property values in this style object.

---

### `TextArea` [(more info)](https://anvil.works/doc#textarea)

-   [Methods](#TextArea_methods)
-   [Properties](#TextArea_attributes)
-   [Events](#TextArea_events)

---

Create a new ‘TextArea’ object

---

##### Base class: anvil.Component

#### Constructor

`TextArea([placeholder=], [auto_expand=], [spacing_above=], [spacing_below=], [margin=], [height=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [enabled=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### TextArea Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**focus()**

Set the keyboard focus to this TextArea

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**select()**

Select all the text in this TextArea

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### TextArea Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**auto\_expand** - *boolean*

If true, the text area will expand vertically to fit its contents

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**height** - *string*

The height of this component.

**italic** - *boolean*

Display this component’s text in italics

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**placeholder** - *string*

The text to be displayed when the component is empty.

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### TextArea Events

**change()**

When the text in this text area is edited

**show()**

When the TextArea is shown on the screen

**hide()**

When the TextArea is removed from the screen

**focus()**

When the TextArea gets focus

**lost\_focus()**

When the TextArea loses focus

---

### `TextBox` [(more info)](https://anvil.works/doc#textbox)

-   [Methods](#TextBox_methods)
-   [Properties](#TextBox_attributes)
-   [Events](#TextBox_events)

---

Create a new ‘TextBox’ object

---

##### Base class: anvil.Component

#### Constructor

`TextBox([placeholder=], [hide_text=], [type=], [spacing_above=], [spacing_below=], [margin=], [text=], [align=], [font_size=], [font=], [bold=], [italic=], [underline=], [enabled=], [background=], [foreground=], [border=], [visible=], [role=], [tooltip=], [tag=])`

---

#### TextBox Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**focus()**

Set the keyboard focus to this TextBox

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**select()**

Select the text in this TextBox

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### TextBox Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s text

**background** - *color*

The background colour of this component.

**bold** - *boolean*

Display this component’s text in bold

**border** - *string*

The border of this component. Can take any valid CSS border value.

**enabled** - *boolean*

True if this component should allow user interaction.

**font** - *string*

The font to use for this component.

**font\_size** - *number*

The height of text displayed on this component in pixels

**foreground** - *color*

The foreground colour of this component.

**hide\_text** - *boolean*

Display stars instead of the text in this box

**italic** - *boolean*

Display this component’s text in italics

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**placeholder** - *string*

The text to be displayed when the component is empty.

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**text** - *string*

The text displayed on this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**type** - *enum: `"text"`, `"number"`, `"email"`, `"tel"`, `"url"`*

What type of data will be entered into this box?

**underline** - *boolean*

Display this component’s text underlined

**visible** - *boolean*

Should this component be displayed?

---

#### TextBox Events

**change()**

When the text in this text box is edited

**pressed\_enter()**

When the user presses Enter in this text box

**show()**

When the TextBox is shown on the screen

**hide()**

When the TextBox is removed from the screen

**focus()**

When the TextBox gets focus

**lost\_focus()**

When the TextBox loses focus

---

### `Timer` [(more info)](https://anvil.works/doc#timer)

-   [Methods](#Timer_methods)
-   [Properties](#Timer_attributes)
-   [Events](#Timer_events)

---

Create a new ‘Timer’ object

---

##### Base class: anvil.Component

#### Constructor

`Timer([interval=])`

---

#### Timer Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### Timer Properties

**interval** - *number*

The number of seconds between each tick. 0 switches the timer off.

**parent**

---

#### Timer Events

**tick()**

Every \[interval\] seconds. Does not trigger if \[interval\] is 0.

**show()**

When this timer's form is shown on the screen (or it is added to a visible form)

**hide()**

When this timer's form is hidden from the screen (or it is removed from a visible form)

---

### `URLMedia`

---

Create a Media object representing the data at a specific URL. Caution: Getting data from URLs directly in your code will often fail for security reasons, or fail to handle binary data.

---

##### Base class: anvil.Media

#### Constructor

`URLMedia(url)`

---

### `WithLayout`

-   [Attributes](#WithLayout_attributes)

---

Parent class of any form with a layout.

---

##### Base class: anvil.Component

#### Constructor

`WithLayout()`

---

#### WithLayout Attributes

**layout** - *anvil.Component instance*

This form’s layout.

---

### `XYPanel` [(more info)](https://anvil.works/doc#xypanel)

-   [Methods](#XYPanel_methods)
-   [Properties](#XYPanel_attributes)
-   [Events](#XYPanel_events)

---

Create a new ‘XYPanel’ object

---

##### Base class: anvil.Container

#### Constructor

`XYPanel([spacing_above=], [spacing_below=], [margin=], [height=], [background=], [foreground=], [border=], [visible=], [role=], [align=], [tooltip=], [tag=])`

---

#### XYPanel Methods

**add\_component(component, \[x=0\], \[y=0\], \[width=None\])**

Add a component to this XYPanel, at the specified coordinates. If the component’s width is not specified, uses the component’s default width.

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**get\_width() → number**

Get the width of this XYPanel, in pixels.

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

---

#### XYPanel Properties

**align** - *enum: `"left"`, `"center"`, `"right"`*

Align this component’s content

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**foreground** - *color*

The foreground colour of this component.

**height** - *string*

The height of this component.

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**tag** - *object*

Use this property to store any extra information about this component

**tooltip** - *string*

Text to display when you hover the mouse over this component

**visible** - *boolean*

Should this component be displayed?

---

#### XYPanel Events

**show()**

When the XYPanel is shown on the screen

**hide()**

When the XYPanel is removed from the screen

---

### `YouTubeVideo` [(more info)](https://anvil.works/doc#youtubevideo)

-   [Methods](#YouTubeVideo_methods)
-   [Properties](#YouTubeVideo_attributes)
-   [Events](#YouTubeVideo_events)

---

Create a new ‘YouTubeVideo’ object

---

##### Base class: anvil.Component

#### Constructor

`YouTubeVideo([youtube_id=], [autoplay=], [loop=], [current_time=], [volume=], [state=], [duration=], [mute=], [spacing_above=], [spacing_below=], [margin=], [height=], [background=], [foreground=], [border=], [visible=], [role=], [tag=])`

---

#### YouTubeVideo Methods

**add\_event\_handler(event\_name, handler\_func)**

Add an event handler function to be called when the event happens on this component. Event handlers will be called in the order they are added. Adding the same event handler multiple times will mean it gets called multiple times.

**pause()**

Pause this YouTube video

**play()**

Start playing this YouTube video

**remove\_event\_handler(event\_name, \[handler\_func\])**

Remove a specific event handler function for a given event. Calling remove\_event\_handler with just the event name will remove all the handlers for this event

**set\_event\_handler(event\_name, handler\_func)**

Set a function to call when the ’event\_name’ event happens on this component. Using set\_event\_handler removes all other handlers. Setting the handler function to None removes all handlers.

**stop()**

Stop playing this YouTube video

---

#### YouTubeVideo Properties

**autoplay** - *boolean*

Set to true to play this video immediately

**background** - *color*

The background colour of this component.

**border** - *string*

The border of this component. Can take any valid CSS border value.

**current\_time** - *object*

Get or set the current playback position, in seconds.

**duration** - *object*

Get the duration of the video in seconds.

**foreground** - *color*

The foreground colour of this component.

**height** - *string*

The height of this component.

**loop** - *boolean*

Set to true to play this video repeatedly

**margin** - *margin*

Margin for this component. Only available in apps that have been migrated to use Layouts.

**mute** - *boolean*

Set whether the video is muted or not.

**parent**

**role** - *themeRole*

Choose how this component can appear, based on your app’s visual theme.

**spacing\_above** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space above this component.

**spacing\_below** - *enum: `"none"`, `"small"`, `"medium"`, `"large"`*

The vertical space below this component.

**state** - *object*

Get the current playback state of the video as a string. E.g. PLAYING

**tag** - *object*

Use this property to store any extra information about this component

**visible** - *boolean*

Should this component be displayed?

**volume** - *object*

Get or set the current volume, from 0 - 100.

**youtube\_id** - *string*

The ID of the YouTube video to play

---

#### YouTubeVideo Events

**state\_change(state)**

When the video changes state (eg PAUSED to PLAYING)

-   `state` - The new state of the video (values from the YouTube API)

**show()**

When this video is shown on the screen (or it is added to a visible form)

**hide()**

When this video is hidden from the screen (or it is removed from a visible form)

---

## Functions

#### `alert(content, [title=""], [buttons=], [large=False], [dismissible=True], [role=])`

Pop up an alert box. By default, it will have a single “OK” button which will return True when clicked.

---

#### `confirm(content, [title=""], [buttons=], [large=False], [dismissible=False], [role=])`

Pop up a confirmation box. By default, it will have “Yes” and “No” buttons which will return True and False respectively when clicked.

---

#### `download(media)`

Download the given Media Object immediately in the user’s browser.

---

#### `get_focused_component() → anvil.Component instance`

Get the currently focused Anvil component, or None if focus is not in a component.

---

#### `get_open_form()`

Returns the form most recently opened with open\_form().

---

#### `get_url_hash()`

Get the decoded hash (the part after the ‘#’ character) of the URL used to open this app. If the first character of the hash is a question mark (eg ‘#?a=foo&b=bar’), it will be interpreted as query-string-type parameters and returned as a dictionary (eg {‘a’: ‘foo’, ‘b’: ‘bar’}).

---

#### `handle(component_name, event_name)`

When applied to a form method as a decorator, sets the decorated method as an event handler for the specified component event.

---

#### `is_server_side() → boolean`

Check whether Anvil is running server side or not.

---

#### `open_form(form, *args, **kwargs)`

Open the specified form as a new page.

If ‘form’ is a string, a new form will be created (extra arguments will be passed to its constructor). If ‘form’ is a Form object, it will be opened directly.

---

#### `set_default_error_handling(handler_fn)`

Set a function to be called when an uncaught exception occurs. If set to None, a pop-up will appear letting the user know that an error has occurred.

---

#### `set_url_hash(val)`

Sets the hash of the currently open URL. If val is a string, it is added to the URL after a #. If val is a dictionary, it will be interpreted as query-string-type parameters and added to the URL after a hash and question mark (eg ‘#?a=foo&b=bar’).

---

## Globals

#### `app`

Information about the current app, as an instance of [anvil.AppInfo](#AppInfo)

---
