---
title: "Deployment Environments"
url: "/docs/deployment/environments"
---


# [Deployment Environments](#deployment-environments)

Every time you run an Anvil app, it’s running in some *environment* - that’s the configuration that determines:

-   What URL you can visit to open the app
-   What [version](/docs/version-control) of your code is running
-   Which [database](/docs/data-tables) is accessed when your code uses the Data Tables API
-   Which [Uplink keys](/docs/uplink) can be used to access this environment
-   Whether this app’s [Scheduled Tasks](/docs/background-tasks/scheduled-tasks) execute in this environment

To deploy your application – that is, to configure its environments – click the **Publish** button, in the top right of the editor.

This will open the Environments dialog.

Select an environment to configure it. Let’s look at each option in turn:

## [Choosing a URL](#choosing-a-url)

Use this URL to access this environment. An environment can have:

-   **A Private URL** – this URL contains a hard-to-guess token, so that it is only accessible by users to whom you have given the URL. This is useful for applications you don’t want to share widely. A private URL looks like this:

    `https://34AMG5SX7Z6AGNLJ.anvil.app/4ZYKZOBG34CIZNQVCYFMOI2B`

    If the URL *does* get out accidentally, you can click **Reset secret link**, which will generate a new token, and invalidate the old URL – so anyone with the old URL can no longer access your app. (For more robust authentication, you can use [user authentication](/docs/users)).

-   **A Public URL** – this URL is easy to remember and type, so anyone can open your app. A public URL looks like this:

    `https://my-cool-app.anvil.app`

-   **A Custom Domain** – this allows an application to appear on your own domain name. For information on using your own domain name with an Anvil app, [click here](/docs/deployment/custom-domains). A custom domain URL looks like this:

    `https://my-cool-app.com`

    Custom domains are available on the [Hobby Plan](https://anvil.works/pricing) and above.

-   **No URL at all** – this means this environment cannot be accessed from a web browser, although it may still be accessed via the [Uplink](/docs/uplink), or run [Scheduled Tasks](/docs/background-tasks/scheduled-tasks), if those are configured.

## [Choosing an App Version](#choosing-an-app-version)

You might want to make different versions of your app available at the same time. For example, your main site might be running well-tested code, while a “staging” URL allows you to test a new release, and individual developers can set up their own temporary environments running new code. To enable this, each environment can choose a version of the app. You can choose a branch, or a specific commit – see [Version Control](/docs/version-control) for more details.

## [Configuring the Uplink](#configuring-the-uplink)

If you’re using the [Uplink](/docs/uplink), you have to connect your Uplink code to a particular environment. You can configure, reset and remove uplink keys for each environment here.

### Allowing other environments to call Uplink code

When Uplink code registers a server function with `@anvil.server.callable`, that function can normally only be called from code running in the same environment.

However, you can choose to **Share uplinks with other environments**. In this case, your Uplink code can be called from *any* environment. This is useful, for example, to access production Uplink functions when you click **Run** in the Editor (ie from the [Development Environment](#development-environments)).

## [Choosing a Database](#choosing-a-database)

You might want different environments to use different databases for your [data tables](/docs/data-tables) – for example, so you can test your app without affecting production data. You can choose which database each environment uses. The tables in this database will be available via `anvil.tables.app_tables` in this environment.

## [Scheduled Tasks](#scheduled-tasks)

Your application can define [Scheduled Tasks](/docs/background-tasks/scheduled-tasks), which execute at specified intervals. You might not want to run Scheduled Tasks in every environment, however – for example, your Development Environment might not need to send “weekly digest” emails to all users.

Scheduled Tasks are specified as part of your app’s source code. Therefore, the app version [chosen for this environment](#choosing-an-app-version) specifies which tasks will run. (This may differ from the tasks specified in the version you’re currently editing!)

If you’ve added a Scheduled Task and it’s not running in your desired environment, check:

1.  Whether the task exists in the version used by this environment
2.  Whether the environment has Scheduled Tasks enabled

## [Error Digests](#error-digests)

You can set up recurring error digests emails for your published apps. That way, you can be alerted of uncaught errors in your app without needing to check your App Session Logs regularly.

Error Digest Emails are available on the [Business Plan](https://anvil.works/pricing) and above.

Error digest emails summarise uncaught errors that have occurred in your app sessions over the interval of time that you have selected, from latest to earliest. You will only receive emails if there have been sessions with errors, otherwise the email won’t send, and it will list a maximum of 10 app sessions. After that, the email will just indicate that there are 10+ sessions with errors.

To set up error digests for an environment, click on the dropdown and select the frequency at which you would like to receive emails. You can enter multiple email addresses to send the digest to, separated by commas.

---

## [Multiple Environments](#multiple-environments)

An app can have multiple environments. For example, you might have a production environment for your live app and a separate staging environment for testing.

To add a new environment, click **\+ Add another environment** in the Environments dialog. You can then configure the environment by choosing its URL, app version, and other settings.

Creating and managing multiple deployment environments is available on the [Business Plan](/pricing) and above.

---

## [Migrating apps from the Classic Editor](#migrating-apps-from-the-classic-editor)

If you created an application with the Classic Anvil Editor, you will see one or two pre-created environments representing the current deployment state.

If you alter your application’s deployment from the Beta Anvil Editor, you will be prompted to migrate this app to Environments, after which you will no longer be able to edit its deployment configuration from the Classic Editor. You will still be able to edit code and other configuration in the Classic Editor.

---

## [Development Environments](#development-environments)

When you run an app in the Anvil Editor, it runs in a special *Development Environment*, specific to your user account. In the Environments dialog, you can select **Get a link to my development environment**. This will give you a private URL (and, optionally, Uplink keys) to access whatever you currently have open in the editor.

This is particularly useful for testing [HTTP endpoints](/docs/http-apis), or for connecting Uplinks to untested code, without each developer needing to create a new Environment, which creates clutter in collaborative projects.

A Development Environment uses:

-   The version you most recently viewed or edited (see [Version Control](/docs/version-control))

-   The database you currently have selected (see [Data Tables](/docs/data-tables))

Development Environments do not run Scheduled Tasks.
