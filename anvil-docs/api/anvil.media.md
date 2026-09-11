---
document: "anvil.media"
title: "anvil.media"
url: "/docs/api/anvil.media"
doc-id: anvil.media
state: Live
date-created: 2026-09-08
---


## `anvil.media` Module

#### Classes

[`TempFile`](#TempFile) [`TempUrl`](#TempUrl)

#### Functions

[`download`](#download) [`from_file`](#from_file) [`open`](#open) [`print_media`](#print_media) [`write_to_file`](#write_to_file)

## Classes

### `TempFile`

Create a temporary file initialised with the contents of the provided media, if any.

#### Constructor

`TempFile([media])`

#### Instance Methods

**__enter__() → string**

**__exit__()**

---

### `TempUrl`

Creates a temporary client-side URL for a Media object, even if the media has no permanent URL. This URL should be revoked when you are finished with it. If you use TempUrl as a context manager ('with TempUrl(media) as url:'), this happens automatically; if you instantiate it manually you must call 'revoke()' on the instance.

The download argument only affects LazyMedia objects

#### Constructor

`TempUrl(media, download=True)`

#### Instance Methods

**__enter__() → url** — get the url using a 'with' block.

**__exit__()** — Revoke a url when exiting a 'with' block

**revoke()** — revoke a url from a media object

#### TempUrl Attributes

**url** - *string* — the temporary url

---

## Functions

#### `download(media)`

Download the given Media Object immediately in the user's browser.

---

#### `from_file(filename, [mime_type], [name]) → anvil.Media instance`

Creates a Media object from the given file.

---

#### `open(media) → BytesIO`

Open a media file as Python BytesIO object

---

#### `print_media(media)`

Print the given Media Object immediately in the user's browser.

---

#### `write_to_file(media, filename)`

Write a Media object to the given file
