---
title: "Email"
url: "/docs/server/email"
doc-id: email-_index
state: Live
date-created: 2026-09-08
---


# [Email](#email)

[Email Service tutorial and code snippets](/blog/email-driven-apps)

Your apps can send and receive email using the built-in Email Service.

Start by adding the Email service to your app using the [App Browser](/docs/editor#app-browser), or check the [Quickstart](/docs/email/quickstart) for more.

## [Sending and Receiving Email from your apps](#sending-and-receiving-email-from-your-apps)

To send an email, run `anvil.email.send()`.

To receive an email, decorate a function as `@anvil.email.handle_message`. this function will run when emails are received and the contents will be available as the first positional argument.

For more information, see [Sending and Receiving Email](/docs/email/sending_and_receiving).

## [Security and DKIM](#security-and-dkim)

If you’re working with sensitive data, it’s important to verify that emails come from who they claim to. Anvil has built-in support for DKIM, a system that allows senders to sign emails. You can also use some simple techniques of your own.

For more information see [Security and DKIM](/docs/email/security_and_dkim)
