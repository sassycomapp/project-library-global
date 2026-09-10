---
title: "Gmail"
url: "/docs/integrations/google/gmail"
doc-id: gmail
state: Live
date-created: 2026-09-08
---


# [Gmail](#gmail)

You can use Anvil to send email via your Gmail account.

Gmail is not intended for heavy usage. If you send more than ~100 messages per day through Anvil, consider using the [Email Service](/docs/email)

To send emails via your Gmail account, you first need to enable the Gmail service.

In the [Sidebar Menu](/docs/editor#sidebar-menu), click the blue plus button, then select ‘Google API’. In the Google API dialog, expand the section named ‘Send email from your Gmail address’, and click ‘Enable email’.

You’ll be prompted to log in and connect your Gmail account.

Once you’ve enabled the Gmail service, you can send emails via your Gmail account from code. Here is a simple example, sending a text-only email to one address.

```python
import anvil.google.mail

anvil.google.mail.send(
    to = "Sarah <sarah@example.com>",
    subject = "Meeting today",
    text = "See you at 5pm")
```

Here is a more complex example, illustrating all the possible parameters to `anvil.google.mail.send`:

-   `from_address` - The email address from which this email is sent. Must be a string. You can add a name to the From field with a string like `"Name <email@address.com>"`. (You can specify any name, but the email address must be an address registered to this Gmail account.)
-   `to` - The email address(es) this email is sent to. Can be a string or a list of strings.
-   `cc` - The email address(es) to which this email is CCed. Can be a string or a list of strings.
-   `bcc` - The email address(es) to which this email is Blind CCed. Can be a string or a list of strings.
-   `subject` - The subject line of the email
-   `text` - The plain text of the email. You must specify either **text** or **html** (or both).
-   `html` - An HTML-formatted version of the email. You must specify either **text** or **html** (or both).

```python
anvil.google.mail.send(
   from_address = "Al <al@example.com>",
   to = ["sarah@example.com",
         "Bob <bob@example.com>"],
   cc = "jane@example.com",
   bcc = "mark@example.com",
   subject = "Meeting today",
   text =
   """
   Dear all,

   There will be a meeting today at 5pm.

   Best Regards,
   Joseph
   """,
   html =
   """
   Dear all,

   <p>There will be a meeting today at <b>5pm</b>.

   <p>Best regards,
   <p>Joseph
   """)
```
