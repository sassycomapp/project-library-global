---
document: "Structuring your app"
title: "Structuring your app"
url: "/docs/workflows/app-architecture/structuring-your-app"
doc-id: structuring-your-app
state: Live
date-created: 2026-09-08
---


# [Structuring your app](#structuring-your-app)

Anvil apps are made up of:

**Client Side**

Forms | Packages | Modules

**Server Side**

Server Packages | Server Modules

### Packages

Your app can be organised using Packages. Packages can contain Forms, Modules, and other Packages.

### Forms can contain things

[Forms](/docs/client/ui#forms) can contain other Forms, as well as Modules and Packages. Technically, [Forms are just Python Packages](/docs/app-architecture/python-directory-structure#forms).

### Server Modules and Server Packages

There are also [Server Modules](https://anvil.works/docs/server#server-modules) and Server Packages. These are just like ordinary Modules and Packages, but they can only be run or imported on the server.

They are found in the ‘Server Code’ section of the App Browser.

## [Adding things](#adding-things)

To add a new Form, Module or Package, click the three dots menu next to ‘Client Code’ or ‘Server Code’.

Or use the dropdown menu next to a Form or Package to add things inside it.

You can create new Server Modules and Server Packages in the same way.

## [Moving things](#moving-things)

Drag-and-drop existing Forms, Packages and Modules to put them in a new place within your app structure.

If you move a Form, Module or Package, be sure to [rewrite its imports](/docs/app-architecture/how-to-import-things) and the imports of things that refer to it - the [all-app search function](/docs/editor/keyboard-shortcuts#in-the-form-editor) can help you here.
