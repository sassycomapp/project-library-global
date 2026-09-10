---
title: "Quickstart: Files and Media"
url: "/docs/other-concepts/working-with-files/media/quickstart"
doc-id: media-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Files, Media and Binary Data](#quickstart-files-media-and-binary-data)

### Make your app handle files

Anvil has built-in support for uploading, storing, downloading, and manipulating files and other binary data.

Follow this quickstart to load files into your app, access their contents and properties, and display an image file on the page.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Add a FileLoader component](#add-a-fileloader-component)

You will see your app in the centre of the screen. On the right is the Toolbox, which contains components to drag-and-drop.

Drop a FileLoader into the page.

## [Print the properties of your files](#print-the-properties-of-your-files)

Click on the FileLoader component to bring up the Object Palette. Click `on change event` to create a function that will run when a file is uploaded.

You will be taken to the Code View. The `file_loader_1_change` method runs when a file is loaded into the FileLoader:

```python
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass
```

There is a Python object named `file` that represents whatever file the user loads in. It is an Anvil `Media` object.

Add some print statements to output the properties and contents of the file:

```python
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    print(f"The file's name is: {file.name}")
    print(f"The number of bytes in the file is: {file.length}")
    print(f"The file's content type is: {file.content_type}")
    print(f"The file's contents are: '{file.get_bytes()}'")
```

## [Run your app](#run-your-app)

Now click the ‘Run’ button at the top of the screen.

You’ll see your app running. Click the ‘upload’ button - you will get a file selection dialog.

Upload a short text file. Here’s what happens if you upload a file containing the text `Anvil represents files as Media objects`.

## [Display an image file](#display-an-image-file)

Stop the app and go back to the Design View of the [Form Editor](/docs/editor#form-editor).

Drag-and-drop an Image component onto the page and change its `display_mode` to `original_size` in the Properties Panel.

Go back to the code view and modify the `file_loader_1_change` event handler to this:

```python
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.image_1.source = file
```

Run your app again and upload an image file. Your image will be displayed in the app.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:GCUJJIODWBECDDZB%3dMGJDYORVZTPA3L2R3Q2PILWZ)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [Files, Media and Binary Data](/docs/working-with-files/media) to see what else you can do with Media Objects.

Media objects are a powerful way to handle binary data: Anvil supports storing, downloading, emailing, displaying as images, streaming into Server Modules, saving as temporary files in Server Modules, and more.

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
