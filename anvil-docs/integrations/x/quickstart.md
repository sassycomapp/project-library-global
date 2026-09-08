---
title: "Quickstart"
url: "/docs/integrations/x/quickstart"
---


# [Quickstart: Tableau Integration](#quickstart-tableau-integration)

This quickstart will guide you through the process of creating an Anvil app that can be used as a Tableau extension, and connecting it to a dashboard in Tableau.

## [Creating a new Anvil app for Tableau](#creating-a-new-anvil-app-for-tableau)

Go to the [Anvil IDE](/new-build) and click on `Blank App`. Select the `Tableau Extension` theme from the window that appears.

In the top right of the Anvil Editor, there is a green button that says `Test in Tableau`.

When the button is clicked, it brings up a dialog box which explains the steps needed to connect your app to Tableau.

The next sections of this guide explain those steps in more detail.

## [Downloading your app’s manifest file](#downloading-your-apps-manifest-file)

In order to load local extensions, Tableau requires a manifest file in `.trex` format. This can be downloaded from Step 1 in the `Test in Tableau` dialog box.

This file will be used later when adding your extension into a dashboard.

## [Adding your app to Tableau’s safe list](#adding-your-app-to-tableaus-safe-list)

**Note:** This step is only required if you are using Tableau Cloud or Tableau Server. The safe-list is not required for Tableau Desktop.

In Step 2 of the dialog box, a web link to your app is supplied. This link needs to be [added to your Safe List](https://help.tableau.com/current/online/en-us/dashboard_extensions_server.htm#add-extensions-to-the-safe-list-and-configure-user-prompts) in Tableau. Once added, change `Full Data Access` to `Allow` and `User Prompts` to `Hide`.

## [Adding your app into your dashboard as an extension](#adding-your-app-into-your-dashboard-as-an-extension)

In Tableau, navigate to the dashboard to which you’d like to add your Anvil app extension.

In the top navigation bar, select `Edit`. From the `Objects` section at the bottom left of the screen, drag `Extension` to the dashboard. In the `Add an Extension` dialog box, click `Access Local Extensions`, and select the extension manifest file we downloaded earlier.

## [Showing the Tableau dashboard in the Anvil Editor](#showing-the-tableau-dashboard-in-the-anvil-editor)

**Note:** This step is only available if you are using Tableau Cloud or Tableau Server.

To have your full Tableau dashboard show when you run your app in the [Anvil Editor](https://anvil.works/docs/editor#the-anvil-editor) you need to add your Tableau dashboard’s URL to your Anvil app.

Select `Publish` from the navigation bar above of the Tableau Workbook. A notification will appear saying the notebook has been published. Click the `Go to Workbook` button in the notification. Copy the Workbook URL and paste it under Step 4 in the `Test in Tableau` dialog box.

The URL should look something like this:

`https://prod-uk-a.online.tableau.com/#/site/anviltest2/views/superstore-anvil-extension-workbook/Overview`

Once that’s done, simply hit `Run` at the top of the Anvil Editor to see the full dashboard and embedded Anvil app.

## [Using the Tableau API in code](#using-the-tableau-api-in-code)

Once the integration is set up, we can access data and worksheets within the Tableau dashboard through Tableau’s [Extensions API](https://tableau.github.io/extensions-api/docs/trex_api_about.html).

To access elements within our dashboard, we access `dashboardContent` by following the [Tableau Extensions API documentation](https://tableau.github.io/extensions-api/docs/index.html). For example, to access all the worksheets in the current dashboard, we would write the following within our Anvil app’s client-side code:

```python
my_worksheets = tableau.extensions.dashboardContent.dashboard.worksheets
```

From our worksheets we can access things like the worksheet’s name:

```python
first_worksheet = tableau.extensions.dashboardContent.dashboard.worksheets[0].name
```

Another useful thing to do via the Extensions API is [add event listeners](https://tableau.github.io/extensions-api/docs/interfaces/worksheet.html#addeventlistener). Below we are adding a listener to our worksheet that will call our [Form’s](https://anvil.works/docs/client/ui#forms) `print_mark()` function when a mark on our Tableau worksheet is selected.

```python
first_worksheet.addEventListener("mark-selection-changed", self.print_mark)
```

For full details of the Tableau API, including its namespace hierarchy, please see the [Tableau’s API reference documentation.](https://tableau.github.io/extensions-api/docs/index.html) and/or [Tableau Extensions API Basics page](https://tableau.github.io/extensions-api/docs/trex_api_about.html).
