---
document: "anvil.google.drive"
title: "anvil.google.drive"
url: "/docs/api/anvil.google.drive"
doc-id: anvil.google.drive
state: Live
date-created: 2026-09-08
---


## `anvil.google.drive` Module

#### Classes

[`DriveItem`](#DriveItem) [`File`](#File) [`Folder`](#Folder)

#### Functions

[`get_user_files`](#get_user_files) [`login`](#login)

## Classes

### `DriveItem`

-   [Methods](#DriveItem_methods)
-   [Attributes](#DriveItem_attributes)

---

---

#### Instance Methods

**delete()**

Delete the DriveItem (this cannot be undone)

**move(dest_folder)**

Move the DriveItem from one folder to another

**trash()**

Move the DriveItem to the trash folder

---

#### DriveItem Attributes

**id** - *string*

ID of the DriveItem

---

### `File`

-   [Methods](#File_methods)
-   [Attributes](#File_attributes)

---

---

##### Base classes: anvil.google.drive.DriveItem, anvil.Media

---

#### Instance Methods

**get_bytes()**

Get the contents of an object representing a Google Drive file. Native Google files such as Docs, Slides and Sheets must first be exported to an appropriate file type. All other file types support get_bytes().

**set_bytes(content)**

Set the contents of an object representing a Google Drive file.

**set_media(media)**

Upload new contents to an existing File. Media must be a Media object.

---

#### File Attributes

**id** - *string*

ID of the file

---

### `Folder` [(more info)](/docs/integrations/google/google-drive#folders)

-   [Methods](#Folder_methods)
-   [Attributes](#Folder_attributes)

---

---

##### Base class: anvil.google.drive.DriveItem

---

#### Instance Methods

**create_file(title, [content_bytes=None], [content_type='text/plain'])**

Create a new file within the Folder.

**create_folder(title)**

Create a new folder within the Folder.

**get(title) → anvil.google.drive.File instance**

Get the File item by title. The title argument should be a string.

**get_by_id(id) → anvil.google.drive.File instance**

Get the File item by ID. The ID argument should be a string.

**list_files() → generator(anvil.google.drive.File instance)**

List the files (not folders) in the Folder.

**list_folders() → generator(anvil.google.drive.Folder instance)**

List the folders (not files) in the Folder.

---

#### Folder Attributes

**files** - *list(anvil.google.drive.File instance)*

List of File items in the Folder

**folders** - *list(anvil.google.drive.Folder instance)*

List of Folder items in the Folder

---

## Functions

#### `get_user_files() → anvil.google.drive.Folder instance` [(more info)](/docs/integrations/google/google-drive#user-files)

Return the top-level folder containing all the files in the Users drive. anvil.google.drive.login() must be called first.

---

#### `login([extra_scopes=])` [(more info)](/docs/integrations/google/google-drive#user-files)

Prompt the user to log in to their Google account and ask permission to access their Google Drive files.
