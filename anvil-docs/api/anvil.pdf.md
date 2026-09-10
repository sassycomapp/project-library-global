---
title: "anvil.pdf"
url: "/docs/api/anvil.pdf"
doc-id: anvil.pdf
state: Live
date-created: 2026-09-08
---


## `anvil.pdf` Module

#### Classes

[`PDFRenderer`](#PDFRenderer)

#### Functions

[`render_form`](#render_form)

## Classes

### `PDFRenderer` [(more info)](/docs/media/creating_pdfs)

Configure options for PDF rendering. Returns an object with a render_form() method.

#### Constructor

`PDFRenderer([filename="print.pdf"], [landscape=False], [margins=], [page_size="letter"], [quality="default"], [scale=1.0])`

-   `filename` - The name of the generated PDF file.

-   `landscape` - Generate a PDF in landscape orientation.

-   `margins` - Page margins (in centimetres), as a dictionary specifying margins on each side (eg {'top': 1.0, 'bottom': 1.0, 'left': 1.0, 'right': 1.0}) or as a number specifying a global margin. The default value is 1.0

-   `page_size` - Can be the name of a standard page size ('letter' or 'A0'-'A10'), or a tuple of (width, height) in centimetres.

-   `quality` - The quality of the generated PDF, which has a large impact on file size. Available values are: - 'original': All images will be embedded at original resolution. Output file can be very large. - 'screen': Low-resolution output similar to the Acrobat Distiller 'Screen Optimized' setting. - 'printer': Output similar to the Acrobat Distiller 'Print Optimized' setting. - 'prepress': Output similar to Acrobat Distiller 'Prepress Optimized' setting. - 'default': Output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file.

-   `scale` - The scale (zoom level) at which you are printing. The default value is 1.0.

#### Instance Methods

**render_form(form_name, *args, **kwargs) → anvil.Media instance**

Render an Anvil form to PDF. Pass the name of the form you want to render, plus any arguments you want to pass to its constructor.

Returns a PDF as an Anvil Media object.

---

## Functions

#### `render_form(form_name, *args, **kwargs) → anvil.Media instance` [(more info)](/docs/working-with-files/creating-pdf-files)

Render an Anvil form to PDF. Pass the name of the form you want to render, plus any arguments you want to pass to its constructor.

Returns a PDF as an Anvil Media object.
