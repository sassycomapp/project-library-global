---
title: "Files, Media Objects and Binary Data"
url: "/docs/other-concepts/working-with-files/media"
doc-id: media-_index
state: Live
date-created: 2026-09-08
---


# [Files, Media and Binary Data](#files-media-and-binary-data)

All binary data (pictures, uploaded files, etc.) is represented in Anvil as **Media objects**. Check the [Quickstart](/docs/working-with-files/media/quickstart) to see some examples using them.

## [Media Objects](#media-objects)

Media objects are created by Anvil APIs such as FileLoader components and the Google Drive API. You can also create them directly in Python code from byte strings or source URLs.

You can pass Media objects to and from [server functions](/docs/server), store them in [Data Tables](/docs/data-tables), and use them with Anvil components.

Here are a few things you can do with Media objects:

-   Display a picture in an [Image](/docs/client/components/basic#image) component by setting its `source` property to a Media object.
-   When a user uploads a file into a [FileLoader](/docs/client/components/basic#fileloader) component, the FileLoader’s `file` property is a Media object.
-   You can send and receive [email attachments](/docs/email/attachments) as Media objects.
-   You can open any Media object by setting the `url` property of a [Link](/docs/client/components/basic#link) to a Media object. This opens or downloads the media when the link is clicked.
-   You can trigger a Media object download in the user’s browser by calling `anvil.media.download(my_media_object)` in any client-side code. (Remember to import `anvil.media` first!)
-   You can store media in a [Data Table](/docs/data-tables), with the “Media” column type.
-   [Canvas](/docs/client/components/canvas) components can take a snapshot of what you’ve drawn as a Media object by calling `get_image()`.
-   [Google Drive](/docs/integrations/google/google-drive) files are Media objects. You can set the contents of a new Google Drive by passing a Media object to `create_file()`, or you can upload new contents to an existing file by calling `set_media()`.
-   You can [create a PDF file](/docs/working-with-files/creating-pdf-files) from any component or Form.

You can do all these things without needing to manually manipulate the binary data.

If you do need to access the underlying data and metadata, you can use the attributes and methods of the `anvil.Media` class listed below.

## [Using Media Objects directly](#using-media-objects-directly)

API Docs: [anvil.Media](/docs/api/anvil#Media) | [anvil.URLMedia](/docs/api/anvil#URLMedia) | [anvil.BlobMedia](/docs/api/anvil#BlobMedia)

All Media objects are subclasses of `anvil.Media` and all have these attributes and methods:

---

#### `content_type`

Tells you the MIME type of this media. This is a string with values like `"text/plain"` or `"image/png"`.

---

#### `length`

A number that tells you how many bytes long this media is.

---

#### `name`

A string containing the filename of this Media object (or `None` if it is anonymous)

---

#### `url`

Gives you a URL where this media can be downloaded, *if* this Media is “permanent” (e.g. if it is stored in [Data Tables](/docs/data-tables), or a [Google Drive](/docs/integrations/google/google-drive) file). If a Media object is not permanent (e.g. it is an anonymous `BlobMedia` object), its `url` property will be `None`. However, you can still download non-permanent Media objects using [Link](/docs/client/components/basic#link) components, or display them with [Image](/docs/client/components/basic#image) components.

Some media’s URLs are accessible from anywhere on the web (e.g. `URLMedia('https://anvil.works/')`).

But some media objects provide a special URL, which is only valid for this browser session using this app. For example, the `url` of media from a data table is only valid in the session when it was generated.

---

#### `get_bytes()`

A method that returns the content as a string. For binary content such as images, this isn’t very pretty to print out, but it gives you direct access to the raw content of this Media.

---

#### `get_url()`

A method that returns the `url` property or None if the Media object doesn’t have one. By default, the returned URL will auto-download the file. You can pass `False` as an argument to `get_url` to return the non-auto-downloading version of the URL. The file will instead be opened by the browser.

### Example

This example gets the `anvil.works` website and prints the data and metadata made available by its Media object.

```python
my_media = anvil.URLMedia('https://anvil.works')

print(f'url: {my_media.url}')
print(f'content_type: {my_media.content_type}')
print(f'length: {my_media.length} bytes')
# This will be `None` since this is a website, not a file
print(f'name: {my_media.name}')
# Only print the first 15 bytes
print(f'raw bytes: {my_media.get_bytes()[:15]} ...')
```

This prints:

```
url: https://anvil.works
content_type: text/html
length: 38653 bytes
name: None
raw bytes: <!DOCTYPE html> ...
```

---

## [Constructing Media Objects](#constructing-media-objects)

As well as getting Media objects from FileLoaders, Google Drive and other Anvil APIs, you can construct them yourself in code.

`URLMedia` gets media from a URL. This example gets media for the Anvil logo, and displays it in an [Image](/docs/client/components/basic#image) component called `image_1`.

```python
my_media = anvil.URLMedia("https://anvil.works/ide/img/banner-100.png")

self.image_1.source = my_media
```

`URLMedia` only stores a URL; it does not fetch its data unless the `length` or `content_type` attributes are accessed, or `get_bytes()` is called.

Because of browser security restrictions, it is often not possible to directly grab the bytes in client-side code, although you will still be able to display it in an Image component.

If you get an exception like `Failed to load media: https://anvil.works`, the endpoint you are trying to access may not allow requests from client-side code. Try fetching the bytes from a [Server Module](/docs/server) or [Uplink](/docs/uplink) script instead.

See [Browser Restrictions](/docs/http-apis/making-http-requests#browser-restrictions) for more info.

[`BlobMedia`](/docs/api/anvil#BlobMedia) gets its media from a byte-string you specify. This example makes a new BlobMedia containing a string of text, and then uploads it to an [app file](/docs/integrations/google/google-drive#drive-app-files) on Google Drive.

```python
file_contents = "Hello, world".encode()      # String as bytes

my_media = anvil.BlobMedia(content_type="text/plain", content=file_contents, name="hello.txt")

anvil.google.drive.app_files.my_file.set_media(my_media)
```

You can also use JavaScript [`File` objects](https://developer.mozilla.org/en-US/docs/Web/API/File) and convert these to Anvil Media objects using `anvil.js.to_media()`. The following example gets a `File` from an HTML element and converts it to a Media object:

```python
js_file = self.dom_nodes["my-file-component"].files[0]
file = anvil.js.to_media(js_file)
```

## [Uploading and downloading files](#uploading-and-downloading-files)

### Uploading

Files can be loaded into the browser using the [FileLoader](/docs/client/components/basic#fileloader) component.

To upload them to your server-side code, simply pass the FileLoader’s `file` property as an argument to a server function.

The uploaded file will be a [`Media` object](/docs/working-with-files/media#media-objects). These can be stored directly in Anvil’s [Data Tables](/docs/data-tables) in a `Media` column.

### Downloading

The `anvil.media.download()` function allows you to download any [Media object](#media-objects) as a file in the user’s web browser. This example creates and downloads a file called `hello.txt`.

```python
import anvil.media

text_file = anvil.BlobMedia('text/plain', b'Hello, world', name='hello.txt')
anvil.media.download(text_file)
```

`anvil.media.download()` is available in Form code only.

Since you can store `Media` objects in your [Data Tables](/docs/data-tables), you can download files stored in Data Tables. Retrieve them in the same way as you would a string, integer or other data type. When the `Media` object is retrieved, it will still be a `Media` object; its format does not change from when it was originally loaded into the browser.

You can also create a download button with a [Link](/docs/client/components/basic#link). `Media` objects have a `url` property containing a URL that the user can access to download the file. Set this as a Link component’s `url` to give the user a clickable link that downloads the file. Media objects must be ‘permanent’ in order to have a URL - this means they must be stored in a Data Table, Google Drive, or originally retrieved from a URL.

### Temporary URLs

You can also create temporary client-side URLs for Media Objects, even if the media has no permanent URL, using `anvil.media.TempURL(media)`.

```python
from anvil.js import window
b = BlobMedia('text/plain', b"foo")

with anvil.media.TempUrl(b) as url:
    window.open(url)
```

This URL should be revoked when you are finished with it. If you use TempUrl as a context manager (`with TempUrl(media) as url:`), this happens automatically; if you instantiate it manually you must call `revoke()` on the instance.

```python
temp_url = anvil.media.TempUrl(b)
url = temp_url.url

# When you're done, revoke the URL
temp_url.revoke()
```

## [Files in Server Modules](#files-in-server-modules)

You can read and write to/from the filesystem in Server Modules just as you would in any Python environment. Your filesystem is your own; other users do not have access to it.

```python
def write_a_file(my_string):
  with open('/tmp/my-file.txt', 'w+') as f:
    f.write(my_string)
```

```python
def read_a_file():
  with open('/tmp/my-file.txt', 'r') as f:
    contents = f.read()
    print(contents)
```

Anvil also has methods to [write to files from Media objects](/docs/working-with-files/media/files_on_disk#media-object-to-temporary-file).

If you’re using a Python library that wants you to pass it a filename, this can be really useful for writing some data into a file, then passing the `file_name` to the library you’re using.

```python
import anvil.media

media_object = anvil.BlobMedia('text/plain', b'Hello, world', name='new.txt')

with anvil.media.TempFile(media_object) as file_name:
    # Now there is a file in the filesystem containing the contents of media_object.
    # The file_name variable is a string of its full path.
```

Read from files to Media objects using this function:

```python
import anvil.media

anvil.media.from_file(file_name, [content_type], [name])
```
