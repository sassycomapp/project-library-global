---
document: "The Anvil Editor"
title: "The Anvil Editor"
url: "/docs/editor"
doc-id: editor-_index
state: Live
date-created: 2026-09-08
---


# [The Anvil Editor](#the-anvil-editor)

This is a picture of the Anvil Editor, with the most important parts labelled:

1.  **The [App Browser](#the-app-browser)** is open by default and can be found by clicking the App button in the Sidebar Menu. It lets you select which part of your app you are editing:
    -   **[Client code](/docs/client)** (user interfaces and Python code that runs in the web browser)
    -   **[Server code](/docs/server)** (code that runs in a server-side Python environment)
    -   Assets (HTML, CSS and other uploaded files for your app. Editing these assets is entirely optional.)
2.  **The [Sidebar Menu](#sidebar-menu)** is where you configure your application, find your apps logs, and add pre-built libraries and integrations like [Data Tables](/docs/data-tables), [User management](/docs/users), etc.
3.  **The [Form Editor](/docs/editor/form-editor)** displays what your user interface will look like, and lets you drag and drop components to create your UI. The Form Editor has three modes:
    -   **Design View**, which shows you how your [Form](client/ui#forms) will look when your app is running
    -   **Code View**, which shows you the Python class that describes how your [Form](client/ui#forms) behaves.
    -   **Split View**, which gives you the option of displaying any combination of Design View, Code View and HTML View.

4.  **The [Object Palette](/docs/editor/form-editor#object-palette)** lets you quickly and easily edit your component’s most commonly edited properties
5.  **The [Version History](/docs/version-control) Panel** displays your app’s commit history and allows you to create new branches and clone your app with Git.
6.  **The [Background Tasks](/docs/background-tasks) Panel** shows any running background tasks.
7.  **The [App Console](#bottom-panel)** will appear after running your app. It shows the app’s output from `print` statements and exceptions.
8.  **The Run Button** runs the app in the Editor and shows the App Console (shortcut: `Ctrl-Enter`). Clicking the dots menu gives you the option to run the app in split view or in a new window.
9.  **The [Publish Button](/docs/deployment)** allows you to publish your app publicly or privately. Here, you can add and configure environments for your app.
10.  **The [Toolbox](/docs/editor/form-editor#toolbox)** is where you pick new components to add to your UI.
11.  **The [Properties Panel](/docs/editor/form-editor#properties-panel)** lets you configure the component you have selected in the Form Editor. (You can select components by clicking on them.)
12.  **The [Component Tree](/docs/editor/form-editor#component-tree)** shows the hierarchy of components within the current Form and let’s you move components in the Form

## [Sidebar Menu](#sidebar-menu)

The Sidebar Menu contains more options for building and configuring your app.

These are the options given in the Sidebar Menu:

-   **App**: The default view. Shows the App Browser.
-   **Data**: Add and configure [Data Tables](data-tables) and Databases
-   **Settings**: Configure settings for your app:
    -   **General**: Change the name, description and logo of your app
    -   **Python versions**: Choose the version of Python running on the server.
    -   **[Dependencies](deployment/dependencies)**: Add other apps to use as libraries or configure your app to use as a library
    -   **Data Tables**: Configure settings for Data Tables
    -   **Collaboration**: Configure sharing and cloning of your app
-   **[App logs](editor/app-logs)**: Get a log of exceptions and `print()`ed output from your app, split by user session and a list of current and past background tasks
-   **Theme**: Change the app’s colour scheme and add CSS [roles](client/customisation/using-css/roles) to style components
-   **Search**: Search through your app

Clicking the blue plus button brings up a menu to add more features to your app, including [the Email service](email), [the Users service](users), [the Uplink](uplink), [App Secrets](security/encrypting-secret-data) and [built-in integrations](integrations). Selecting a feature will add it to the [Sidebar Menu](/docs/editor#sidebar-menu). It will also automatically add all the necessary imports to your code.

To remove a feature, right click over its corresponding icon in the [Sidebar Menu](/docs/editor#sidebar-menu) and select ‘Remove Service’. This will also remove all the imports that are no longer necessary from your code.

## [The App Browser](#the-app-browser)

The App Browser can be found by clicking the app icon. It lists the main parts of your app:

-   [Client code](client) - the [Forms](ui/forms), [Modules](client/modules) and [Packages](app-architecture/structuring-your-app) that define your app’s UI design and client-side behaviour
-   [Server code](server) - the Server Modules that run secure server-side Python
-   [Scripts](server/scripts) - server-side Scripts that you can run in the Editor or invoke from your app
-   Assets - the HTML, CSS and other uploaded files for your app

You can add Forms, Server Modules, Modules, Folders and Services to your app by clicking on `+ Add Form` or the dots menu.

You can also use the dots next to existing Forms and Packages to add new ones as well as to delete and rename things. For Forms and Modules, this menu also allows to choose [what runs when your app starts](client#when-your-app-starts). Forms have a few other options: you can duplicate them, or click ‘use as component’ to make them appear in the Toolbox as [Custom Components](client/customisation/custom-components):

## [Bottom Panel](#bottom-panel)

### App Console

The App Console will appear after you run your app. It shows the output of `print` statements within your app. It also shows tracebacks from unhandled exceptions, and (occasionally) messages from the Anvil system about your app.

Output from Server Modules will appear with an orange border on the left-hand margin, while output from Client Forms and Modules will appear with a blue border.

Exceptions will show a traceback - if the exception occurred on the server, the traceback will still show the whole call stack as if the code ran on the same machine. Clicking a link in the traceback will take you to the problematic line of code in the Code View.

### Background Tasks

Click on the [Background Tasks](background-tasks) tab to see the tasks that are currently running.

### Version History

The [Version History](version-control) tab shows recent changes to your app and allows you to add and switch branches as well as clone your app with Git.

### Designer Output

When in the design view, the Designer Output Console will appear if there are any component errors or a [custom component](/docs/client/customisation/custom-components) prints something to the console.

### Server Console

To launch a server console, click the button in the top right. This will bring up a REPL where you can connect directly to your chosen Python environment on the server.

## [Zen Mode and Quick Switcher](#zen-mode-and-quick-switcher)

Activating **Zen mode** maximises an editor tab and simplifies the IDE view so that you can focus on your code. You can activate Zen mode by:

-   Using `Alt+Shift+Z` on Windows or `Option+Shift+Z` on Mac
-   Double clicking on a tab in the tab bar
-   Right clicking on the active tab

You can use the quick switcher to easily jump between tabs or files without using your mouse, which is particularly helpful while in Zen mode. Press `Ctrl+P` (or `Cmd+P` on Mac) to open it, then press it again to cycle through files.

## [Linting and Formatting](#linting-and-formatting)

The Anvil Editor has [Ruff](https://docs.astral.sh/ruff/) linting and formatting built in. The linter shows warnings in your code as a yellow squiggly line. If you hover over the highlighted code, you’ll see more information about the warning in a tooltip.

You can auto-format your code using Alt+Shift+F on Windows or Option+Shift+F on Mac.

The Ruff linter is also configurable. You can configure the linter per app by:

1.  Opening your app locally
2.  Creating a `pyproject.toml` or `ruff.toml` file in the root directory
3.  Adding your preferred configuration (see the [Ruff documentation](https://docs.astral.sh/ruff/configuration/) for details)
4.  Pushing your changes back to Anvil

## [Code Styles](#code-styles)

Anvil apps use Python code on client and server side. The Editor uses different visual styles for client and server code.

In [Modules](client/python/modules), code is styled like client code. Module code can be run on both client and server.

In this documentation, client and server code are styled as follows:

```python
def client_code():
  """This is a function in the client"""
  # This is client code
  print("This is what client code looks like")
```

```python
def server_code():
  """This is a function on the server"""
  # This is server code
  print("This is what server code looks like")
```

## [Deleting Apps](#deleting-apps)

To delete an app, go to Settings, by pressing on the gear button of the [Sidebar Menu](#sidebar-menu). Click on **Delete app**, under the **Manage this App** section.

You can also delete an app from the Start Page. Find the app in the ‘My Apps’ list and hover over it to reveal the delete button.

Once you click on one of the delete buttons, this pop-up will appear:

You’ll need to type in the name of the app to confirm you want to delete your app then press the delete button. Once this is done, your app will be permanently deleted.
