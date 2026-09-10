---
title: "Clone your app locally"
url: "/docs/workflows/version-control/git/direct-checkout"
doc-id: direct-checkout
state: Live
date-created: 2026-09-08
---


# [Clone Your App’s Source Code Locally](#clone-your-apps-source-code-locally)

You can check your source code out directly from Anvil – for example, to view or edit it on your local machine. You don’t need to set up a GitHub repository to do this: you can use your Anvil app as a Git remote.

## [Cloning your app](#cloning-your-app)

If you open the drop-down menu in the in the [Version History](/docs/version-control) tab in the [Bottom Panel](/docs/editor#bottom-panel), you can click **Clone with Git** to clone the your app’s source code.

You can either copy the Git remote URL (for use in a GUI tool like Fork or Sourcetree), or a git command line that will clone your app into a directory named after the app. (You can safely rename this directory to whatever you like.)

## [Structure of the Git repository](#structure-of-the-git-repository)

The files in the repository are everything Anvil uses to represent an app - there are no hidden configuration files that don’t get cloned.

The Git repository for your app contains:

-   `anvil.yaml`: The configuration relating to your app as a whole.
-   `__init__.py`: Sets the Python path for the app
-   `client_code`: This is an ordinary Python source tree containing the code and config for your client-side Forms and Modules.
    -   `<form name>`: Each Form, by default, is a Python package; a directory containing an `__init__.py` file (plus a config file defining the design layout). The Python code for each Form is in a separate file.
        -   `__init__.py`: The Python code for each Form is in this file. This is exactly the code you see in the Code View of the Editor.
        -   `form_template.yaml`: This file defines the Form’s template, its properties, its components and their properties. It is a representation of what the visual designer knows about that Form.
-   `server_code`: This is an ordinary Python source tree containing the code for your Server Modules.
    -   `<server module name>`: The Python code for each Server Module is in this file. This is exactly the code you see in your Server Modules in the Editor.
-   `theme`: This contains the configuration files relating to the functionality found in the Theme section of the App Browser.
    -   `assets`: The files contained in the Assets part of the Theme section.

For more information about how an Anvil app’s source code is laid out, consult the [Anvil App Structure guide](https://github.com/anvil-works/anvil-runtime/blob/master/doc/app-structure.md) from the GitHub repository for Anvil’s [open-source runtime](/open-source).

You can edit the files in the repo and make commits. You can then push these commits back to Anvil and you will see them in the Editor. If you have made changes in the Anvil Editor as well, you can pull these and merge or rebase, as you normally would when collaborating on a project using Git. That way, you can use the drag-and-drop Anvil Editor and modify the code in a local editor - there should rarely be merge conflicts if you do this.

## [Authenticating](#authenticating)

To authenticate your local Git with Anvil, you can either use your Anvil username and password, or add an SSH public key. To do this, click “add your SSH public key to Anvil” in the Clone with Git dialog. This will open up your account settings where you can enter the SSH key. This must be the SSH key you’re using with Git.

If you’re using two factor authentication you must use SSH rather than username and password.
