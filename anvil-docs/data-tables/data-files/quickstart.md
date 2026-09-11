---
document: "Quickstart: Data Files"
title: "Quickstart: Data Files"
url: "/docs/data-tables/data-files/quickstart"
doc-id: data-files-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Data Files](#quickstart-data-files)

Data Files are static files you can attach to your app that are available in your Server Modules.

Follow this quickstart to load files into your app, access their contents and properties, and let the user of your app edit the text file’s contents.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Add the Data Files service](#add-the-data-files-service)

Click the **+** button in the Sidebar Menu, and select **Data Files**.

## [Upload a text file](#upload-a-text-file)

Upload a text file for your users to edit by clicking the **Upload** button and selecting a text file.

For this example, I’m using a simple text file that contains the string “Hello, World!”.

[Download the test.txt I'm using](./img/test.txt)

Once the file is uploaded, you can rename and delete it in this interface.

### Data Files storage

Data Files are stored in your app’s database. When you add the Data Files service to your app, Anvil creates a `Files` table where your files are stored as [Media objects](https://anvil.works/docs/working-with-files/media#media-objects).

As each database has its own set of files, if you’re using multiple [environments](https://anvil.works/docs/deployment/environments) with different databases you’ll need to set up each database’s Data Files separately.

## [Use the file in Python](#use-the-file-in-python)

You access your files in code using the `data` API in a [Server Module](https://anvil.works/docs/server). You get the path to the file on disk from `data_files['filename']`. That’s a path to the file on disk, where your Server Modules are running. You can get individual files or directories.

```python
from anvil.files import data_files

@anvil.server.callable
def return_text_from_file():
    # Read the contents of a file
    with open(data_files['test.txt']) as f:
        text = f.read()
    return text
```

The [`@anvil.server.callable`](https://anvil.works/docs/server#calling-server-functions-from-client-code) decorator means this function can be called from the client code.

## [Use file data on the client side](#use-file-data-on-the-client-side)

Now you have a server function to interact with your file, you can call that function from the client side to return the file’s data to your user. In the [App Browser](https://anvil.works/docs/editor#the-anvil-editor), open one of your app’s forms and select the [code view](https://anvil.works/docs/editor/form-editor#code-view). In the `__init__` method, you can call the server function you created earlier with [`anvil.server.call('return_text_from_file')`](https://anvil.works/docs/client/python#python-in-the-browser). Then you can print the file’s text.

```python
class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run when the form opens.

    # Call the server function which returns the text from your text file
    file_text = anvil.server.call('return_text_from_file')
    
    # Print what's returned
    print(file_text)
```

Finally, run your app. In the [app logs](https://anvil.works/docs/editor/app-logs), you will see the contents of your text file printed.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:M2AHDDHEVJVN63AZ%3dQ4L4FZCZUHHOJLT37CKTAQF2)

---

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
