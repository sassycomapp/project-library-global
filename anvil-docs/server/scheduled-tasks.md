---
title: "Scheduled Tasks"
url: "/docs/server/scheduled-tasks"
---


# [Scheduled Tasks](#scheduled-tasks)

Sometimes you want to run server functions at particular times, regardless of user activity on your app. For example, you might need to run analytics on your [Data Tables](/docs/data-tables) every night, or send out a daily [email](/docs/email) digest. For users on paid plans, Scheduled Tasks let you do just that - you can choose to run any [Background Task](/docs/background-tasks) every minute, hour, day, week, or month, on a schedule you configure.

Scheduled Tasks are available on the [Hobby Plan](https://anvil.works/pricing) and above

Scheduled Tasks are for **running Background Tasks on the server**. To repeatedly run client code in the user’s browser, use [the Timer Component](/docs/client/components/basic#timer).

Scheduled Tasks run in the [Published](/docs/version-control#published-vs-dev-versions) version of your app. When configuring Scheduled Tasks, make sure you’re using the ‘published’ version of your app.

Scheduled Tasks launch standard [Background Tasks](/docs/background-tasks), as if you had launched them manually using `anvil.server.launch_background_task(...)`. You can see the launched Background Tasks in the [Background Tasks dialog](/docs/background-tasks), and find output in the [App Logs](/docs/editor/app-logs)

In a typical use-case, we may have defined two [Background Tasks](/docs/background-tasks) in a [Server Module](/docs/server):

-   `poll_sensor` collects data from a remote sensor (probably using the [Uplink](/docs/uplink)).
-   `send_email_digest` sends a summary email, and should be run once a week.

To get started, add the Scheduled Tasks Service to your app by clicking the blue plus button in the [Sidebar Menu](/docs/editor#sidebar-menu).

Then, select the Scheduled Tasks Service.

## [Add a Scheduled task](#add-a-scheduled-task)

In the Scheduled Tasks tab, click `+ Add task`.

Choose `poll_sensor` from the `Task to Run` drop-down menu, confirm that we want to run it every 10 minutes, then click the `Add` button.

Next, Choose `send_email_digest` from the `Task to Run` drop-down menu, and configure it to run every Monday at 8am. Note that all Scheduled Tasks are configured in UTC - the same time zone your [Server Modules](/docs/server) run in.

## [Configure environments](#configure-environments)

You might want different [environments](/docs/deployment/environments) to run different Scheduled Tasks. You might not want to run Scheduled Tasks in every environment – for example, your development environment might not need to send “weekly digest” emails to all users.

To select which environments run Scheduled Tasks, click on `Configure Environments` in the Scheduled Tasks tab.

Then select `Show advanced settings` for the Environment you’d like to run your Scheduled Tasks and tick `Run scheduled tasks`.

The Scheduled Tasks tab will now list which environments are running the Scheduled Tasks.

## [See when a task last ran](#see-when-a-task-last-ran)

Click on a Scheduled Task to see when it last ran, and when it will next run.
