---
title: "Google Drive"
url: "/docs/integrations/google/google-drive"
doc-id: google-drive
state: Live
date-created: 2026-09-08
---


# [Google Drive](#google-drive)

You can use the Google Service to integrate Google Drive functionality into your Anvil app.

You can designate some of your Drive files as “app files” to which all users have access, or ask users to log in and then create, update and delete files in their own Google Drives.

## [Connecting to Google Drive](#connecting-to-google-drive)

To connect your Anvil app to Google Drive, click the blue plus button in the [Sidebar Menu](/docs/editor#sidebar-menu) and choose “Google API”.

From the Google API configuration page, select “Add files from Google Drive to this app”. This will prompt you to log into your Google account and give the app permission to access your Drive files. You can then select a file from your Drive that will be accessible from your app.

## [Drive App Files](#drive-app-files)

App files are files or folders from your Google Drive that are available to any user of the app. Your users do not have to log in with Google; these files can always be accessed by this app.

To access a file or folder in Google Drive, click “Add files from Google Drive to this app” from the Google API configuration tab.

Added files will show up in the Google API configuration page, where you can edit their Python name and their [client permissions](#permissions).

Each app file has a Python identifier derived from its filename. You can access these files as `app_files.*<python-identifier>*`.

For example, to read from a text file `hello.txt` uploaded to Google Drive, call:

```python
from anvil.google.drive import app_files

f = app_files.hello_txt
print("File contents: " + f.get_bytes())
```

You can also create new files in your connected Google Drive by clicking “Add new file to Google Drive”. Clicking the three dots menu next to this Button will give you options for creating different types of files.

### Permissions

App files can have three levels of permission, indicated by symbols in the Google configuration page:

#### **Client can read and write**

By default, any code in your app can read or modify an app file. This is convenient, but it also means anyone who can access your app could read or modify that file. (This is because the code in your forms - the *client code* - runs in the user’s browser, so a malicious person could change that code to do whatever they like.) This is fine if you only share the app with people you trust - or if the app file is something you deliberately want the world to have access to.

#### **Client can read**

You can also make app files “read-only” for clients. This means that all of your code can read this app file, but only your [server modules](/docs/server) can change it.

#### **No client access**

Finally, you can make your app file entirely private. This means only your [server modules](/docs/server) can read or write it.

## [File IO](#file-io)

If you have an object representing a Google Drive file, you can get or set its contents as a string with the `get_bytes()` and `set_bytes()` functions.

Native Google files such as Docs, Slides and Sheets [are not really files](https://developers.google.com/drive/api/v3/reference/files/get) so they do not support `get_bytes()`. If you want to download their full contents you should first export them to [an appropriate filetype](https://developers.google.com/drive/api/guides/ref-export-formats). All other uploaded file types support `get_bytes()`.

```python
from anvil.google.drive import app_files

f = app_files.hello_txt
f.set_bytes("My name is Bob.")
```

You can also upload a [Media](/docs/working-with-files/media) object (for example, from a [FileLoader](/docs/client/components/basic#fileloader) component) to a Google File.

```python
from anvil.google.drive import app_files

f = app_files.my_file
f.set_media(self.file_loader_1.file)
```

You can use a Google Drive file as a [Media](/docs/working-with-files/media) object. Here we use a Google Drive file as the source of an [Image](/docs/client/components/basic#image) component:

```python
from anvil.google.drive import app_files

f = app_files.my_image

self.image_1.source = f
```

To create files, use the `Folder.create_file` method.

```python
from anvil.google.drive import app_files

folder = app_files.my_folder

new_file = folder.create_file("new_file.txt")
```

Calling `create_file` with a single file name argument creates a new file with MIME type `text/plain`.

```python
new_file = folder.create_file("new_file.txt",
                              "Hello, world!")

new_image = folder.create_file("new_file.jpg",
                               file_loader_1.file)
```

You can also pass an optional second argument, providing the initial content of the file. This can either be a string, or a [Media object](/docs/working-with-files/media). If it is a Media object, the new file is automatically created with the correct MIME type.

If possible, you should provide initial content when creating a file, rather than creating an empty file and then uploading its content. This way, if something goes wrong during upload then you won’t end up with a new empty file.

## [Folders](#folders)

If you have an object representing a Google Drive folder, you can list the files in that folder with `list_files()`. `list_files()` returns an iterator, so you can loop over it in a `for` loop.

```python
from anvil.google.drive import app_files

folder = app_files.my_folder

for f in folder.list_files():
  print(f["title"])
```

If you want to do more than just loop through the files, you can request a full list of files directly. Bear in mind that this might be slow if there are many files in the folder.

```python
l1 = folder.files
l2 = folder.folders
print(f"This folder has {len(l1)} files and {len(l2)} folders in it")
```

Remember, a folder can contain other folders as well as files.

You can even get an item by its title:

```python
my_file = folder.get("my_file.txt")
my_folder = folder.get("My Subfolder")
```

Every file has an ID, and you can get a file from a folder by its ID too, with `get_by_id`:

```python
f = folder.create_file("new_file.txt")

id = f.id

# ... later ...

my_file = folder.get_by_id(id)
```

## [File Management](#file-management)

You can move a Drive item (file or folder) from one folder to another by calling `move(*<destination-folder>*)`.

```python
from anvil.google.drive import app_files

my_file = app_files.my_file
folder = app_files.my_folder

my_file.move(folder)
```

You can create a new file or folder, by calling `create_file(*<title>*)` or `create_folder(*<title>*)` on a folder.

```python
new_file = folder.create_file("new_file.txt")
new_folder = folder.create_folder("new_folder")
```

Google Drive permits you to create many files or folders with the same title. You can tell them apart by their `id` property, which is a unique string. If you want to store a reference to a file, you should use the `id`.

```python
file1 = folder.create_file("new_file.txt")
file2 = folder.create_file("new_file.txt")

saved_id = file1.id

# (... some time later ...)

# This will retrieve file1, not file2
f = folder.get_by_id(saved_id)
```

You can put a Drive item in the trash by calling `trash()`, or delete it forever by calling `delete()` (this cannot be undone).

```python
new_file.trash()
new_folder.delete()
```

## [Google Sheets](#google-sheets)

Anvil has a Python API to access your Google Sheets.

[Tutorial: Using Google Sheets](/learn/tutorials/sheets)

You can access sheets using Google Drive in the same way you access files.

```python
db = app_files.my_sheet
```

Once you have an object representing a Google Sheet, you can look up its individual worksheets. (It is also possible to look up a worksheet by number, eg `db[0]`, or obtain a list with `list(db.worksheets)`.)

```python
ws = db["Sheet1"]
```

You should set up your Sheet using [Google Drive](https://drive.google.com) so that the column names are in the first row. Once your sheet is set up, you can get a list of the fields in a worksheet using the `fields` attribute.

```python
print(db["Sheet1"].fields)
# Expect output similar to: '[name, age]'
```

You can access rows of data like so:

```python
# Assuming columns "name" and "age"
for r in db["Sheet1"].rows:
  print(f"{r['name']} is {r['age']} years old")
```

You can update them as well as reading them. You can assign numbers or strings, but the data you read from a row will always be a string:

```python
# Convert age to dog years:
for r in db["Sheet1"].rows:
  r["age"] = 7 * int(r["age"])
```

An Exception will be raised if you try to set a non-existent field on a row.

You can add rows to your spreadsheet using the `add_row(...)` method:

```python
ws = db["Sheet 1"]
row = ws.add_row(name="Bob", age=56)
```

(Note: `add_row()` normally returns the new created row. However, if you attempt to insert an empty row, it will return `None`.)

You can delete a row using the `delete()` method.

```python
row.delete()
```

If you delete a row, other rows in the worksheet may shift unpredictably. If you delete a row, you should not re-use any other `row` objects from that worksheet. Call `list_rows()` again to find the rows you want again.

It is also possible to access individual cells of your spreadsheet.

```python
## Display the calculated value of
## the cell in row 1, col 2

print(ws[1, 2].value)

## Display the formula in cell (1,2)

print(ws[1, 2].input_value)

## Set the value of a cell

ws[3, 4].value = "Some text"
```

## [User files](#user-files)

As well as app files, you can use the Google service to access your users’ own files when they log into your app with Google.

To do this, you will need a Google API Client ID and secret (same as for the [Google REST API](google-rest-apis)). See [Linking Google and Anvil](linking-google-and-anvil) for instructions on how to get these.

To read and write files in a user’s Google Drive, you must first call `anvil.google.drive.login()`, which will ask the user for permission to access their files. This is different from calling `anvil.google.auth.login()`, which only asks for their email address.

Once a user has logged into your app using `anvil.google.drive.login()` you can read and write files in their Google Drive. (You can also pass a list of extra scopes to `anvil.google.drive.login()`, just like `anvil.google.auth.login()`.)

You can get the top-level folder containing all the files in their drive by calling `anvil.google.drive.get_user_files()`.

```python
import anvil.google.drive

anvil.google.drive.login()

folder = anvil.google.drive.get_user_files()

for f in folder.list_files():
  print(f["title"])
```
