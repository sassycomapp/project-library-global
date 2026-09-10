---
title: "Image Manipulation"
url: "/docs/other-concepts/working-with-files/media/image-manipulation"
doc-id: image-manipulation
state: Live
date-created: 2026-09-08
---


# [`image` module](#image-module)

[API Docs](/docs/api/anvil.image)

The `image` module allows you to manipulate images in your Anvil app. It is only available on the client side.

Begin by importing the `anvil.image` module.

## [Get dimensions](#get-dimensions)

To get the width and height of an image, use `get_dimensions`:

```python
import anvil.image

# The image can be any Media object containing an image
image_media = URLMedia('https://anvil.works/img/workshops-cogwheels.jpg')

width, height = anvil.image.get_dimensions(image_media)

print(f"The image is {width} pixels wide and {height} pixels high")
```

## [Generating thumbnails](#generating-thumbnails)

To generate a thumbnail of an image (for uploading, for example) use the `generate_thumbnail` method.

In order for `generate_thumbnail()` to work, the image itself will either need to allow for [cross-origin access](https://developer.mozilla.org/en-US/docs/Web/HTML/CORS_enabled_image), or it will need to be loaded from your Anvil app. The image can be loaded from [app assets](https://anvil.works/docs/client/themes-and-styling#adding-your-own-asset-files), a [HTTP endpoint](https://anvil.works/docs/http-apis/making-http-requests) or as a [BlobMedia object](https://anvil.works/docs/api/anvil#BlobMedia).

```python
# Resize the image to have a maximum dimension of 120px.
small_img = anvil.image.generate_thumbnail(image_media, 120)
```

## [Rotating](#rotating)

To rotate an image clockwise by some number of degrees, use the `rotate` method. The `rotate` method works on images uploaded to your app, but will not work for third-party images. See below for more information.

```python
# Get the 'forest.jpg' image previously uploaded to Assets
my_image = "_/theme/forest.jpg"
image_media = URLMedia(my_image)

# Rotate the image by 90 degrees.
rotated_img = anvil.image.rotate(image_media, 90)
self.image_1.source = rotated_img
```

It’s not possible to rotate a cross-origin image. Browsers don’t allow you to access the raw bytes of a third-party image from code, for security reasons. This is true in any application.

For this reason, `anvil.image.rotate` will not work on third party images.

## [Display mode](#display-mode)

To configure how the image is displayed, use the `display_mode` property. This determines how the size of the image should be adjusted to fit the size of the [Image component](/docs/client/components/basic#image).

The available options are:

1.  `shrink_to_fit` - (**default**) - this scales the image to fit in the Image component while maintiaining its aspect ratio.
2.  `zoom_to_fill` - this scales the image to fill the entire Image component while maintaining its aspect ratio. If the image is too big, it will be cropped to fit.
3.  `fill_width` - this scales the image until it fills the width of the Image component while maintaining its aspect ratio.
4.  `original_size` - this displays the image at whatever the browser thinks the original size is. If that would cause the image to be wider than the Image component, it shrinks the image to ensure it fits within the width of the Image component.
