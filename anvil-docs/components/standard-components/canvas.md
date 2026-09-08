---
title: "Canvas"
url: "/docs/components/standard-components/canvas"
---


# [Canvas](#canvas)

[Properties](/docs/api/anvil#Canvas_attributes) | [Events](/docs/api/anvil#Canvas_events)

[Tutorial: Using the Canvas component](/learn/tutorials/canvas)

Canvas components allow you to draw graphics on your form. They are ideal for animations and visualisations.

Drag and drop onto your Form, or create one in code with the `Canvas` constructor:

```python
c = Canvas()
```

To draw to a Canvas, the Canvas must already be rendered to the page. So if you want to draw to a Canvas on page load, run your code in the Form’s `show` event handler, rather than its `__init__` method.

## [Path drawing](#path-drawing)

You can draw lines, arcs and circles with the methods described below. You will need to draw your shapes inside the `reset` event handler of the Canvas component.

Use `move_to` to define your start position. Then use `line_to` to draw straight lines, or `arc` to draw circles and parts of circles. Before drawing, you must run `begin_path`, and when you’ve finished drawing you must run `close_path`. Then run `stroke` to commit your path to the Canvas.

See [Colours, styles and fonts](#colours-styles-and-fonts) to see how to change line/fill colour, style and shape.

```python
  # Draw an outlined triangle
  def canvas_1_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1

    c.begin_path()
    c.move_to(100,100)
    c.line_to(100,200)
    c.line_to(200,200)
    c.close_path()

    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "#E0E0E0"

    c.fill()
    c.stroke()
```

#### `begin_path()`

Tells the canvas that you are about to start drawing a shape.

#### `close_path()`

Connects the most recent edge of the shape to the start point, closing the path.

#### `fill()`

Fills the shape you have drawn in the current `fill_style`.

#### `stroke()`

Draws the outline of the shape you have defined in the current `stroke_style`.

#### `clip()`

Clips all subsequent drawing operations to the defined shape.

#### `move_to(x, y)`

Move to position `(x, y)` without drawing anything, ready to start the next edge of the current shape. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `line_to(x, y)`

Draw a line to position `(x, y)`. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `arc(x, y, radius, start_angle, end_angle, anticlockwise)`

Draw an arc to position `(x, y)` with the specified radius. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

## [Drawing rectangles](#drawing-rectangles)

To draw rectangles, you can use `fill_rect` to draw a filled rectangle, `stroke_rect` to draw a rectangle outline, and `clear_rect` to clear an empty space.

You must set the `stroke_style` and `fill_style` first.

See [Colours, styles and fonts](#colours-styles-and-fonts) to see how to change line/fill colour, style and shape.

```python
  def canvas_1_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1

    # Set the stroke and fill styles
    c.stroke_style = "#2196F3"
    c.line_width = 3
    c.fill_style = "#E0E0E0"

    # Draw a filled rectangle
    c.fill_rect(100, 100, 50, 75)

    # Draw a rectangle outline 25 pixels right of it
    c.stroke_rect(125, 100, 50, 75)

    # Remove colour from a smaller rectangle
    c.clear_rect(120, 125, 20, 30)
```

#### `clear_rect(x, y, width, height)`

Clears a rectangle The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `fill_rect(x, y, width, height)`

Fills a rectangle with the current `fill_style`. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `stroke_rect(x, y, width, height)`

Draws the outline of a rectangle with the current `stroke_style`. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

## [Drawing an image](#drawing-an-image)

You can draw images and parts of images onto your Canvas.

```python
  def canvas_1_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""

    c = self.canvas_1

    # Get the image as a Media object
    image_media = anvil.URLMedia('https://anvil.works/img/workshops-cogwheels.jpg')

    # Draw the image at position (100,100)
    c.draw_image(image_media, 100, 100)

    # Draw a 100x100 patch from this image,
    # Starting at pixel (50, 50) on the image,
    # at position (25, 25) on the canvas,
    # at half scale (50x50)
    c.draw_image_part(image_media,
                      50, 50, 100, 100,
                      25, 25, 50, 50)
```

#### `draw_image(image_media, [x], [y], [width], [height])`

Draw an image (represented by a Media object) at position (x,y). Optionally specify width and height. If (x,y) is not specified, draws at (0,0). The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `draw_image(image_media, sx, sy, s_width, s_height, dx, dy, d_width, d_height)`

Draw a part of an image (specifically the `s_width`x`s_height` rectangle whose top-left corner is at (`sx`,`sy`)) into a `d_width`x`d_height` rectangle whose top-left corner is at (`dx`,`dy`)).

## [Writing text](#writing-text)

You can write text to your canvas.

See [Colours, styles and fonts](#colours-styles-and-fonts) to see how to change font and alignment.

```python
  def canvas_1_reset(self, **event_args):
    """This method is called when the Canvas is shown on the screen"""
    c = self.canvas_1

    c.stroke_style = "#2196F3"
    c.line_width = 1
    c.fill_style = "#E0E0E0"

    c.font = '36px montserrat'

    # Draw an image at position (100,100)
    c.fill_text('Fill Text', 100, 100)

    c.stroke_text('Stroke Text', 100, 150)
```

#### `fill_text(text, x, y)`

Renders the string `text` at position `(x, y)`. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `stroke_text(text, x, y)`

Renders an outline of the string `text` at position `(x, y)`. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `measure_text(text)`

Returns the width, in pixels, of the string `text` as it would be if rendered on the canvas in the current font.

## [Transformation methods](#transformation-methods)

A **transform** rotates, translates, or scales what you draw onto the canvas. You apply it before drawing, and once applied, everything you draw will be transformed. You can go back to using no transform using `reset_transform`.

```python
  def draw_triangle(self):
    # The triangle drawing code from the 'Path drawing' section
    # ... <omitted for brevity> ...

  def canvas_1_reset(self, **event_args):
    # Draw the triangle
    self.draw_triangle()

    # Transform the Canvas to half the scale
    self.canvas_1.scale(0.5, 0.5)

    # Draw the triangle in the new scale
    self.draw_triangle()
```

#### `translate(x, y)`

Updates the current transform so that all subsequent drawing commands are offset by `(x, y)` pixels. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `rotate(angle)`

Updates the current transform so that all subsequent drawing commands are rotated by `angle` *radians*.

#### `scale(x, y)`

Updates the current transform so that all subsequent drawing commands are scaled by a factor of `(x, y)`. The `(x,y)` coordinates are calculated with reference to the top-left corner of the Canvas.

#### `transform(a, b, c, d, e, f)`

Applies the given transformation matrix to the current transform.

#### `set_transform(a, b, c, d, e, f)`

Sets the current transform to the matrix provided.

#### `save()`

Records any transformations applied to the current canvas. This is added to the top of a stack of saved canvas states, so that it can be restored later.

#### `restore()`

Restores any saved transformations. Pops the most recent saved canvas state from the stack and applies it to the canvas. If the stack is empty, this method does nothing.

#### `reset_transform()`

Resets the current transform to the identity matrix.

## [Saving your canvas as an image](#saving-your-canvas-as-an-image)

When you’ve drawn something on your canvas, you can get the contents of your canvas as a [Media object](../../working-with-files/media#media-objects) by calling `get_image()`. You can then display this image in an [Image](basic#image) component, or upload it to [Google Drive](../../integrations/google/google-drive).

```python
img = self.canvas_1.get_image()

self.image_1.source = img

f = anvil.google.drive.app_files.my_file

f.set_media(c.get_image())
```

For more details, see the [Media object documentation](../../working-with-files/media).

## [Colours, styles and fonts](#colours-styles-and-fonts)

### Colours

There are several ways to specify colours on a Canvas. You can give a hexadecimal colour in the form `"#RRGGBB"` (where `"#FF0000"` would be bright red), or specify red, green, blue and alpha values separately: `"rgba(255,0,0,1)"`. It is also possible to specify gradients and patterns - see [HTML5 Canvas Docs](https://mislav.github.io/diveintohtml5/canvas) for details.

### Stroke and fill colour attributes

#### `stroke_style`

The colour of lines drawn on the canvas.

#### `fill_style`

The colour of solid fill on the canvas.

### Shadow attributes

#### `shadow_offset_x`

How far shadows should be displaced from drawn shapes (in `x` direction).

#### `shadow_offset_y`

How far shadows should be displaced from drawn shapes (in `y` direction).

#### `shadow_blur`

Blur amount, in pixels, for shadows.

#### `shadow_color`

The colour of shadows.

### Line attributes

#### `line_width`

The width of the line in pixels.

#### `line_cap`

The style of line ends.

#### `line_join`

The style of line joins.

#### `miter_limit`

Used to prevent `miter` corners from extending too far.

### Text attributes

#### `font`

The font to use when rendering text.

```python
 self.canvas1.font = "10px sans-serif"
```

#### `text_align`

How text should be aligned horizontally. Can be any of `start`, `end`, `left`, `right`, and `center`.

#### `text_baseline`

How text should be aligned vertically. One of `top`, `hanging`, `middle`, `alphabetic`, `ideographic` and `bottom`.

## [Get Canvas width](#get-canvas-width)

#### `get_width()`

Returns the width of the canvas, in pixels

#### `get_height()`

Returns the width of the canvas, in pixels

## [Reset Canvas after resize](#reset-canvas-after-resize)

#### `reset_context()`

Should be called after manually changing the width or height of the canvas. Used to trigger a redraw via the `reset` event handler.
