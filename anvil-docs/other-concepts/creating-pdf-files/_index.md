---
title: "Creating PDFs"
url: "/docs/other-concepts/creating-pdf-files"
---


# [Creating PDFs](#creating-pdfs)

Anvil Forms can be converted to PDFs with a single function call. You might do this in order to attach a PDF to an email, print a PDF, or allow your users to download a PDF.

[Tutorial: Generating PDFs with Python](/learn/tutorials/pdfs)

## [Converting a Form to a PDF](#converting-a-form-to-a-pdf)

You can convert Forms to PDFs by calling `anvil.pdf.render_form()` in server code. Pass in the name of the Form you wish to print as a string. If the Form takes any arguments to its `__init__` method, you can pass these in as extra arguments to `render_form()` (this is exactly like calling [`open_form()`](/docs/client/navigation#displaying-a-new-page)):

```python
# In server code

import anvil.pdf

@anvil.server.callable
def create_zaphod_pdf():
  media_object = anvil.pdf.render_form('Form1', 42, name='Zaphod')
  return media_object
```

The return value of `render_form()` is a Media object. This means you can [download it](/docs/working-with-files/media#uploading-and-downloading-files) in client code:

```python
   # In client code
   import anvil.media

   def download_zaphod_pdf(self):
     media_object = anvil.server.call('create_zaphod_pdf')
     anvil.media.download(media_object)
```

You can attach it to an [email](/docs/email):

```python
@anvil.server.callable
def send_pdf_email():
  anvil.email.send(
    from_name="The Zaphod Generator",
    to="shaun@anvil.works",
    subject="An auto-generated Zaphod",
    text="Your auto-generated Zaphod is attached to this email as a PDF.",
    attachments=anvil.pdf.render_form('Form1', 42, name='Zaphod')
  )
```

You can also store it in a [Data Table](/docs/data-tables):

```python
app_tables.my_pdfs.add_row(
  added=datetime.now(),
  owner=anvil.users.get_user(),
  pdf=anvil.pdf.render_form('Form1', 42, name='Zaphod'),
)
```

You could [store it in Google Drive](/docs/integrations/google/google-drive) too. Anything you can do with a Media Object, you can do with your PDF file!

PDF rendering only works in [deployment environments](/docs/deployment/environments) that have a URL. If you see the error `Cannot render a PDF in an environment with no URL`, you’ll need to [choose a new URL](/docs/deployment/environments#choosing-a-url) for your environment or click “Get a link to my development environment” from the Publish modal.

## [Customising settings](#customising-settings)

You can adjust the image quality, page settings, margins or generated filename for your PDF by instantiating a `PDFRenderer()`, and calling its `render_form()` method:

```python
  from anvil.pdf import PDFRenderer

  pdf = PDFRenderer(page_size='A4').render_form('Form1')
```

You may specify the following arguments to the `PDFRenderer()` constructor:

-   `filename` (string): The name of the generated PDF file. (Default: `"print.pdf"`).

-   `landscape` (`True` or `False`): Generate a PDF in landscape orientation. (Default: `False`).

-   `page_size` (string or tuple): Can be the name of a standard page size (`"letter"` or `"A0"`-`"A10"`), or a tuple of `(width, height)` in centimetres. (Default: `"letter"`).

-   `margins` (dict or number): Page margins (in centimetres), as a dictionary specifying margins on each side (eg `{'top': 1.0, 'bottom': 1.0, 'left': 1.0, 'right': 1.0}`) or as a number specifying a global margin. (Default `1.0`).

-   `scale` (number): The scale (zoom level) at which you are printing. (Default `1.0`).

-   `quality` (string): The quality of the generated PDF, which has a large impact on file size (Default `"default"`). Available values are:

    -   `"original"`: All images will be embedded at original resolution. Output file can be very large.
    -   `"screen"`: Low-resolution output similar to the Acrobat Distiller “Screen Optimized” setting.
    -   `"printer"`: Output similar to the Acrobat Distiller “Print Optimized” setting.
    -   `"prepress"`: Output similar to Acrobat Distiller “Prepress Optimized” setting.
    -   `"default"`: Output intended to be useful across a wide variety of uses, possibly at the expense of a larger output file.
