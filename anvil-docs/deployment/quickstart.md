---
title: "Quickstart"
url: "/docs/deployment/quickstart"
---


# [Quickstart: Deployment](#quickstart-deployment)

### Learn how to publish your app

Once you’ve built an app in Anvil, you can deploy it on the internet with two clicks! (You can also deploy Anvil apps on your own network or cloud server – [see here](hosting-options) for details – but today we will be using Anvil’s built-in cloud hosting.)

In this quickstart, we will create an app and publish it online at a URL of our choice.

## [Create an app](#create-an-app)

Log in to Anvil and click **New Blank App**. Choose the Material Design theme.

## [Publish your app](#publish-your-app)

Find the **Publish** button at the top-right of the editor.

When you click it, you will see this dialog.

Click **Publish This App**, and you will see that your app has been deployed at a new, public URL.

That’s it - **your app is now online**. Click the link and try it!

## [Choose your own URL](#choose-your-own-url)

Right now, your app is published with a randomly generated URL. You can change it to any available subdomain of `anvil.app` such as `health-tracker.anvil.app`, or use your own domain such as `health-tracker.com`. (You can also use a [private link](environments#choosing-a-url) to restrict access to your app.)

For this example, we’ll use a public URL ending in `anvil.app`. Click **Change URL**.

Now you can choose any available subdomain of `anvil.app`.

## [See your app online](#see-your-app-online)

In your app, go to the code for Form1. It looks like this.

Write this line in the `__init__` method:

```python
    alert('This is the app I just built')
```

Change the message to something that proves it’s your app.

Open the Publish App dialog again to copy the URL of your app, then visit that URL in a web browser. You’ll see your app with your message in an alert box.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:RZN66N3E5A5YDYCH%3dRFUUU2FSB3NFL6GE7OSUHMHB)

---

## [Deploying on your servers](#deploying-on-your-servers)

In this Quickstart, we’ve deployed an application on Anvil’s hosted service, but other options are available. If you want to run your applications on your own servers or network, you can use the Anvil App Server to deploy individual applications, or get a full Anvil Enterprise installation so that your editor, source code, apps and data all stay on your corporate network.

For more information about these options, check out [Hosting Options](hosting-options).

### Want more depth on this subject?

Read more in depth about [deploying your app](/docs/deployment).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
