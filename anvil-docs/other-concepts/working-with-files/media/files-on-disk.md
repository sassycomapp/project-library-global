---
title: "Files on Disk"
url: "/docs/other-concepts/working-with-files/media/files-on-disk"
doc-id: files-on-disk
state: Live
date-created: 2026-09-08
---


# [Files on Disk](#files-on-disk)

You can write to and from files in Server Modules using Media objects.

You can also write to and from files using Python’s `open`.

## [Media Object to temporary file](#media-object-to-temporary-file)

To write to a temporary file, use `anvil.media.TempFile(media_object)` in a `with` block.

If you’re using a Python library that wants you to pass it a filename, this can be really useful for writing some data into a file, then passing the `file_name` to the library you’re using.

```python
import anvil.media

@anvil.server.callable
def write_media_to_file(media_object):
  with anvil.media.TempFile(media_object) as file_name:
    # Now there is a file in the filesystem containing the contents of media_object.
    # The file_name variable is a string of its full path.
```

The file is written to the filesystem as soon as the `with` block begins. The file will be deleted when the `with` block exits.

## [Media Object to file](#media-object-to-file)

You can use Python’s `open` to write Media Objects to your filesystem, and read them back.

```python
def write_a_media_object():
  media_object = anvil.BlobMedia('text/plain', b'Hello, world', name='hello_world.txt')
  with open('/tmp/hello_world.txt', 'wb+') as f:
    # Write the byte contents of the media object to 'tmp/my-file.txt'
    # (we opened the file in binary mode, so f.write() accepts bytes)
    f.write(media_object.get_bytes())
```

```python
def read_a_file():
  with open('/tmp/hello_world.txt', 'r') as f:
    contents = f.read()
    print(contents)
```

## [Media Object from file](#media-object-from-file)

To read from an existing file, use `anvil.media.from_file(file_name, [content_type], [name])`.

```python
import anvil.media

@anvil.server.callable
def read_from_file():
  media_object = anvil.media.from_file('/tmp/hello_world.txt', "text/plain")
  return media_object
```

This creates a Media object with the contents of the file. If you don’t supply a name, the Media object’s `name` will be the filename (in this case, `hello_world.txt`).

## [Read and write files as normal](#read-and-write-files-as-normal)

You can also use Python’s `open` to read and write files as normal. Your filesystem is your own; other users do not have access to it.

Files in your filesystem are temporary, and may be removed without warning. We advise you only to access files in the `/tmp` directory.

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
