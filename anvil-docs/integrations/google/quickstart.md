---
title: "Quickstart"
url: "/docs/integrations/google/quickstart"
doc-id: google-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Google integration](#quickstart-google-integration)

### Upload a file to Google Drive

The Anvil Google API Service gives you a simple way to use a range of Google services.

In this quickstart, we’ll build an app that uploads files to your Google Drive.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Enable the Google API Service](#enable-the-google-api-service)

In the [Sidebar Menu](/docs/editor#sidebar-menu), click the blue plus button. You’ll see a list of available services and integrations. Click on Google API.

## [Create a folder in your Google Drive](#create-a-folder-in-your-google-drive)

If you don’t have a Google account, you need to [create one](https://accounts.google.com) - it’s free and they’re really useful.

Create an empty folder (right-click in Google Drive to get the context menu).

## [Add a file to your Anvil app](#add-a-file-to-your-anvil-app)

Go back to the Anvil Editor.

In the Google API Service, click the Add App File button.

A Google login dialog will open in a separate browser window. Log in to see this dialog in the Anvil Editor.

Browse your Google Drive and select the folder you created earlier.

It will be displayed in the Google API Service. There’s a configurable Python Identifier you can use to access it in Python code, and you can set read and write permissions for client code.

## [Add a FileLoader to your app](#add-a-fileloader-to-your-app)

Go to the [Design View](/docs/editor/form-editor#design-view) for Form1. Drag-and-drop a FileLoader component into your app.

Double-click the FileLoader in the Design View to configure a `change` event. This code will be automatically written for you in the Code View:

```python
  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass
```

Delete the `pass` and write this line in its place:

```python
    app_files.my_folder_name.create_file(file.name, file)
```

Where `my_folder_name` is the name of the Google Drive folder you added to the app. In my case, that’s `production_data_06_2019`:

```python
    app_files.production_data_06_2019.create_file(file.name, file)
```

## [Run your app](#run-your-app)

Run your app. Click on the Upload button, select a file from your computer and hit ‘open’.

Check your Google Drive - the file you uploaded will be in the folder.

Success! If you don’t see your file, try logging out of Google Drive and back in again. Sometimes the Google Drive UI takes a while to refresh.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:LZBYOASAGWHP4ZDS%3dKUEAUGEAKAQRUE4NSE6NIOP5)

The cloned version will not have the permissions that were granted to the original, of course!

You’ll need to click the button to set up your own Google account, and add your own files rather than ours.

## [Next up](#next-up)

### Want more depth on this subject?

There’s much more to the Google API Service.

-   You can do much more with your [Google Drive files](google-drive)
-   You can [log users in to your app with their Google accounts](authenticating-users)
-   And you can [access your *users* Google Drive files](google-drive#drive-app-files)

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
