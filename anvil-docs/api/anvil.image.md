---
title: "anvil.image"
url: "/docs/api/anvil.image"
---


## `anvil.image` Module

#### Classes

[`ImageException`](#ImageException)

#### Functions

[`generate_thumbnail`](#generate_thumbnail) [`get_dimensions`](#get_dimensions) [`rotate`](#rotate)

## Classes

### `ImageException`

---

Create a new 'ImageException' object

#### Constructor

`ImageException()`

---

## Functions

#### `generate_thumbnail(image_media, max_size) → anvil.Media instance`

Resize the supplied image so that neither width nor height exceeds max_size (in pixels).

Pass in an anvil.Media object representing the image.

---

#### `get_dimensions(image_media)`

Get the dimensions of an image (width, height).

Pass in an anvil.Media object representing the image.

---

#### `rotate(image_media, angle) → anvil.Media instance`

Rotate the supplied image clockwise by the given number of degrees.

Pass in an anvil.Media object representing the image.
