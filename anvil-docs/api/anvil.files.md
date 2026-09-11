---
document: "anvil.files"
title: "anvil.files"
url: "/docs/api/anvil.files"
doc-id: anvil.files
state: Live
date-created: 2026-09-08
---


## `anvil.files` Module

#### Classes

[`EditingContextManager`](#EditingContextManager) [`Files`](#Files) [`OpenContextManager`](#OpenContextManager)

#### Globals

[`data_files`](#data_files)

## Classes

### `EditingContextManager`

-   [Methods](#EditingContextManager_methods)

---

[Context manager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) for editing data files.

---

#### Instance Methods

**__enter__() → string**

Begin editing the file.

**__exit__()**

End editing the file, uploading its new contents.

---

### `Files`

-   [Methods](#Files_methods)

---

Create a new ‘Files’ object

#### Constructor

`Files()`

---

#### Instance Methods

**__getitem__() → string**

Return the path of a file

**editing(path) → anvil.files.EditingContextManager instance**

Edit a file. To ensure the proper acquisition and release of the file, use the `editing` function in a `with` statement e.g. `with data_files.editing('test.txt') as file:`

**open(path, [mode="r"]) → anvil.files.OpenContextManager instance**

The open() function opens the file (if possible) and returns the corresponding file object.

---

### `OpenContextManager`

-   [Methods](#OpenContextManager_methods)

---

[Context manager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager) for opening data files.

---

#### Instance Methods

**__enter__() → File object**

Open the file.

**__exit__()**

Close the file, uploading its contents if it was opened for writing or appending.

---

## Globals

#### `data_files`

Access Data Files from the [Data Files Service](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager). To access a file stored in the Data Files Service use square brackets containing the path of the desired file - `data_files['<file_path>']`.
