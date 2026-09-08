---
title: "Quickstart"
url: "/docs/server/email/quickstart"
---


# [Quickstart: Email](#quickstart-email)

### Communicate to and from your app by email

Your Anvil app can send and receive emails.

Follow this quickstart to create an app that sends you an email and automatically replies to incoming messages.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘Create a new app’. Choose the Material Design theme.

## [Add the Email Service](#add-the-email-service)

In the [Sidebar Menu](/docs/editor#sidebar-menu), click the blue plus button. You’ll see a list of available services and integrations. Click on Email.

## [Add a Server Module](#add-a-server-module)

In the [App Browser](/docs/editor#the-app-browser), click ‘+ Add Server Module’.

A tab will open a code editor with an orange background.

## [Send an email from your app](#send-an-email-from-your-app)

Write this function into the Server Module:

```python
@anvil.server.callable
def send_email(address):
    anvil.email.send(
      from_name="Anvil Forum",
      to=address,
      subject="Have you used the Anvil Forum?",
      html='The Anvil <a href="https://anvil.works/forum">Forum</a> is friendly and informative.',
      text="The Anvil Forum (https://anvil.works/forum) is friendly and informative.",
    )
```

The `anvil.email.send` function requires at least one of the `text` or `html` properties to be specified. The `html` property defines the HTML content for the email, while `text` is just plain-text. If both are added, the `html` content will be displayed unless it can’t be rendered, in which case the `text` content will be displayed.

## [Call your server function from the client](#call-your-server-function-from-the-client)

Go to the code for Form1. It looks like this:

At the end of the `__init__` method, write these lines (replace the `<your email address>` with your actual email address):

```python
    email_address = "<your email address>"
    anvil.server.call('send_email', email_address)
```

This will run the function when the app starts.

## [Run your app](#run-your-app)

Now click the ‘Run’ button at the top of the screen.

Check your email - you should receive an email from your app.

## [Receive emails from your app](#receive-emails-from-your-app)

To start receiving emails from your app, you need to [publish](/docs/deployment/quickstart#publish-your-app) it first. Stop your app and click the ‘Publish’ button at the top of the screen.

Back in your Server Module, write this function:

```python
@anvil.email.handle_message
def message_handler(msg):
  to_address = msg.addressees.to_addresses[0].raw_value
  msg.reply(text = f"Your email was sent to {to_address} and received successfully.")
```

This function runs automatically whenever your app receives an email and sends a reply back to the sender.

## [Send your app an email](#send-your-app-an-email)

At the bottom of the Server Module, you will see a notice showing the email address your app can receive messages on.

Open your favourite email client and send an email to `hey-it-works@<your-app-id>.anvil.app`, where `<your-app-id>` would be `pointed-bright-basilisk` in this example.

You should receive a reply containing the text: `Your email was sent to hey-it-works@<your-app-id>.anvil.app and received successfully`.

(To set up a nicer email address for your app, see [deployment](/docs/deployment/quickstart).)

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:AHD2UMLD63IXJ6O6%3dMEROJHETOVC34QBF2HENJH4D)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [Sending and receiving email in Anvil](/docs/email)

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
