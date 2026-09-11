---
document: "Publishing your extension"
title: "Publishing your extension"
url: "/docs/integrations/x/publishing"
doc-id: publishing
state: Live
date-created: 2026-09-08
---


# [Publishing a version of your extension](#publishing-a-version-of-your-extension)

While you’re developing your Tableau Extension, you’ll be using a “testing” version of your extension. This means that:

-   The dashboard will always load the version you have open in the Anvil Editor.
-   Every change you make is immediately visible to viewers.
-   Each time the dashboard is opened, a “Tableau Output” tab appears in the Anvil Editor, showing the extension’s output and errors.

This is great for rapidly developing an extension, but it could be inconvenient if you’re deploying it for others to use. For this reason, you can *publish* a version of your extension. If you add the “published” trex manifest to a Tableau dashboard, it will always load the published version of your extension.

## [Publishing your extension](#publishing-your-extension)

To publish your extension, click the **Publish** button at the top right of the Anvil Editor.

Then click **Publish now**.

You will then be able to download a “Published” trex file, which will load the published version of your extension.

When your published extension is loaded in a dashboard, output and errors will no longer appear in the “Tableau Output” panel – but it will still be recorded in the [App Logs](../../editor/app-logs).

## [Publishing a particular version](#publishing-a-particular-version)

By default, the Published trex file will load the `master` branch of your application’s repository. Unless you’re working on multiple branches, this is probably the latest version you’re editing – which might not be what you want! Typically you’ll want to “freeze” a snapshot of your code, so that the users of your published extension see a stable version of your code.

Is all this talk of “branches” confusing? Don’t worry – you can learn more about [version control in Anvil](../../workflows/version-control).

To publish a specific, frozen version of your app, open **Version Control** at the bottom of the Anvil Editor. This will show you a list of versions (or “commits”) of your app that Anvil has saved automatically, along with the dates and what changed in each commit. To publish a particular commit, right-click on it and choose **Publish this commit**.

You can also do this from the Publish dialog, by choosing **Publish a particular version**.

## [Collaborating](#collaborating)

Anvil X makes it straightforward to collaborate with colleagues on the same Tableau Extension. When you’re collaborating:

-   Each developer will typically work on a separate branch, merging changes into `master` when they are complete and tested.

-   Each developer will have their own “debug” trex, allowing them to test their current working version in a private dashboard.

-   The published extension will be based on a particular branch (typically `master`) or manually updated to a particular commit, allowing new changes to be rolled out to production users in a controlled manner.

Learn more about collaborating on Anvil apps in our [Version Control documentation](../../workflows/version-control).

## [Advanced deployment options](#advanced-deployment-options)

You’re not restricted to a single published version of your extension! Anvil X provides rich, configurable [deployment environments](../../deployment/environments), accessible via “**Advanced publication settings**” in the Publish dialog.

Among other things, you can configure:

-   Separate databases for each environment, so that you can test with different data to your production extension
-   [Uplink](../../external-resources/uplink) and [database access](data-tables-in-tableau) keys for each environment
-   Whether your app runs [Scheduled Tasks](../../server/scheduled-tasks) in each environment

To learn more, read about [deployment environments in Anvil](../../deployment/environments).
