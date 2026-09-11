---
document: "Attachments"
title: "Attachments"
url: "/docs/server/email/attachments"
doc-id: attachments
state: Live
date-created: 2026-09-08
---


# [Sending and Receiving Email Attachments](#sending-and-receiving-email-attachments)

As well as text and HTML content, email messages can contain binary attachments. Like all other binary data in Anvil, attachments are [Media objects](/docs/working-with-files/media).

This makes it easy to store attachments in [Data Tables](/docs/data-tables), display them on [Image components](/docs/api/anvil#Image), accept them from [browser uploads](/docs/api/anvil#FileLoader), and more.

## [Sending attachments](#sending-attachments)

To add attachments to an email, pass a list of Media objects to the `anvil.email.send(...)` function:

```python
anvil.email.send(
    to="me@example.com",
    text="See files attached",
    attachments=[media1, media2])
```

## [Receiving attachments](#receiving-attachments)

When you receive an email via `@anvil.email.handle_message`, a list of all attachments is available as the `attachments` property of the Message object:

```python
@anvil.email.handle_message
def incoming_email(msg):
  for attachment in msg.attachments:
    app_tables.received_files.add_row(file=attachment,
                                      from=msg.envelope.sender)
```

## [Using inline attachments](#using-inline-attachments)

Normally, an attachment is a file sent alongside an email. But sometimes, you want to use binary within the email body – for example, an image in an HTML email.

To do this, we use **inline attachment**, and refer to it from the HTML of your email. Each inline attachment has an id, and we can refer to that within an HTML email with a url like `cid:my_id_here`.

When calling `anvil.email.send(...)`, you can specify `inline_attachments` as a dictionary whose keys are the (string) IDs and values are (Media) attachments.

When receiving email via `@anvil.email.handle_message`, the `inline_attachments` attribute of the Message object will be a similar dictionary of IDs to data.

Here is a code sample that sends an image as an inline attachment in an HTML email:

```python
@anvil.server.callable
def send_picture(picture):
  anvil.email.send(
    to="me@example.com",
    subject="Picture",
    html="""
      Here's a picture:<br>
      <img src="cid:mypic"><br>
      Wasn't that cute?
    """,
    inline_attachments={'mypic': picture})
```

And here’s what that email looks like, when opened in Gmail:

![Screenshot of an HTML email with an image](img/attachments/email-with-inline-attachment.jpg)
