---
document: "Static Data Files"
title: "Static Data Files"
url: "/docs/data-tables/data-files"
doc-id: data-files-_index
state: Live
date-created: 2026-09-08
---


# [Data Files in Your App](#data-files-in-your-app)

Data Files are files that you, as the app developer, can attach to your app. These files are available in your [Server Modules](https://anvil.works/docs/server#server-modules). Data Files are useful for machine learning models, static datasets and data that stays constant.

In the Data Files panel, you can drag and drop, rename and delete files.

Once uploaded, you can use `data_files['test.txt']` to get the path to the `test.txt` file on disk.

Check out the [Quickstart](/docs/working-with-files/data-files) to learn how to use the Data File service.

## [Adding the Data Files service](#adding-the-data-files-service)

To add the Data Files service to your Anvil app, click the **+** button in the Sidebar Menu, and select **Data Files**.

## [Adding files and directories](#adding-files-and-directories)

You can add files or [directories](https://en.wikipedia.org/wiki/Directory_(computing)) to the Data Files service by dragging and dropping them from your computer onto the Data Files panel.

Alternatively, select the **Upload** button and select the file or directory from your local computer.

## [Using a file in Python](#using-a-file-in-python)

You access your files in code using the `data` API in a [Server Module](https://anvil.works/docs/server). You get the path to the file on disk from `data_files['filename']`. That’s a path to the file on disk, where your Server Modules are running.

```python
from anvil.files import data_files

@anvil.server.callable
def return_text_from_file():
    # Read the contents of a file
    with open(data_files['test.txt']) as f:
        text = f.read()
    return text
```

If you’re new to working with [file I/O in Python](https://docs.python.org/3/tutorial/inputoutput.html), Dan Bader’s tutorial is a great place to start: [https://dbader.org/blog/python-file-io](https://dbader.org/blog/python-file-io).

### Writing to Data Files

Although Data Files are intended for files that change rarely, it is possible to update the contents of Data Files from code, using `with data_files.editing("<filename>")` to get a filename you can write to:

```python
@anvil.server.background_task
def write_text_to_file(text):
  with data_files.editing('my_text_file.txt') as path:
    # path is now a string path on the filesystem. We can write to it with normal Python tools.
    # For example:
    with open(path, "w+") as f:
      f.write(text)
```

When the `with` block ends, changes you have made to that file will be saved to your Data Files.

Anvil provides no concurrency control over Data Files. If you update a data file from multiple places at once, there is no guarantee what will happen – perhaps one update will overwrite the other, or perhaps the two updates will execute concurrently using the same file on disk, producing corrupt data.

We recommend you update Data Files infrequently, via processes that are guaranteed to run one at a time (such as [Scheduled Tasks](/docs/background-tasks/scheduled-tasks)). For more frequently updated data, consider using [Data Tables](/docs/data-tables) with [transactions](/docs/data-tables/transactions).

## [Using a directory in Python](#using-a-directory-in-python)

You can use [directories](https://en.wikipedia.org/wiki/Directory_(computing)) you’ve uploaded to the Data Files service in Python code.

For example, you can list all the files in a directory by passing the [`scandir()`](https://docs.python.org/3/library/os.html?highlight=scandir#os.scandir) function the path of your directory. The following example displays all files in a directory path that don’t start with ‘.’.

```python
@anvil.server.callable
def list_files_in_directory():
    # Get the path of my Data Files directory
    my_directory_path = data_files['my_directory']

    with os.scandir(my_directory_path) as directory:
        for file in directory:
            if not file.name.startswith('.') and file.is_file():
                print(file.name)
```

## [Renaming a file](#renaming-a-file)

To rename a file, open the Data Files panel and select the file. Then, click the pencil icon on the right and change type the new name.

## [Deleting a file](#deleting-a-file)

To delete a file, open the Data Files panel and select the file. Then, click the trash icon on the right.

## [Data Files storage](#data-files-storage)

Data Files are stored in your app’s database. When you add the Data Files service to your app, Anvil creates a `Files` table where your files are stored as [Media objects](https://anvil.works/docs/working-with-files/media#media-objects). This means that each database has its own set of files; if you’re using multiple [environments](https://anvil.works/docs/deployment/environments) with different databases you’ll need to set up each database’s Data Files separately.

As each database has its own set of files, if you’re using multiple [environments](https://anvil.works/docs/deployment/environments) with different databases you’ll need to set up each database’s Data Files separately.

Files and directories are downloaded and cached on disk the first time they are accessed by your app. This makes it faster to access them the next time the file is used.

The version column is updated each time you upload a new file to the same path in the Data Files interface. When the version is changed, the file is re-cached the next time it is accessed.
