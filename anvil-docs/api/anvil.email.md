---
title: "anvil.email"
url: "/docs/api/anvil.email"
---


## `anvil.email` Module

The `anvil.email` module contains functions for sending and receiving email in your Anvil app.

#### Classes

[`Address`](#Address) [`DeliveryFailure`](#DeliveryFailure) [`Message`](#Message) [`SendFailure`](#SendFailure) [`SendReport`](#SendReport)

#### Functions

[`send`](#send)

## Classes

### `Address`

-   [Attributes](#Address_attributes)

---

---

#### Address Attributes

**address** - *string*

The email address this object represents.

**name** - *string*

The name associated with the address this object represents.

**raw_value** - *string*

The full string value of this address.

---

### `DeliveryFailure` [(more info)](/docs/email/sending_and_receiving#rejecting-email)

---

While handling an error, you can raise a DeliveryFailure exception to reject email delivery. Optionally, you may specify a message and SMTP error code with the rejection.

#### Constructor

`DeliveryFailure(message=None, smtp_code=554)`

---

### `Message`

-   [Methods](#Message_methods)
-   [Attributes](#Message_attributes)

---

---

#### Instance Methods

**get_header(header_name, [default=None])**

Return the value of the specified header, or default value if it is not present.

Case-insensitive. If the header is specified multiple times, returns the first value.

**list_header(header_name)**

Return a list containing every value of the specified header. Case-insensitive.

**reply([cc=], [bcc=], [from_address=], [from_name=], [text=], [html=], [attachments=])**

Reply to this email.

---

#### Message Attributes

**addressees** - *anvil.email.Message.Addressees instance*

The addresses this email was sent from and to, according to the headers.

**attachments** - *list(anvil.Media instance)*

A list of this email’s attachments.

**dkim** - *anvil.email.Message.DKIM instance*

Object describing whether this message was signed by the sending domain

**envelope** - *anvil.email.Message.Envelope instance*

The sender and receipient of this email, according to the SMTP envelope.

**headers** - *list*

All the headers in this email, as a list of (name,value) pairs.

**html** - *string*

The HTML content of this email, or None if there is no HTML part.

**inline_attachments** - *dict(string,anvil.Media instance)*

A dictionary of this email’s inline attachments. Keys are ContentID headers, values are the attachments as Media Objects.

**subject** - *string*

The subject of this email, or None if there is no subject.

**text** - *string*

The plain-text content of this email, or None if there is no plain-text part.

---

### `SendFailure`

---

Create a new ‘SendFailure’ object

#### Constructor

`SendFailure()`

---

### `SendReport`

-   [Attributes](#SendReport_attributes)

---

---

#### SendReport Attributes

**message_id** - *string*

The Message-ID header given to this outgoing message.

---

## Functions

#### `send([to=], [cc=], [bcc=], [from_address="no-reply"], [from_name=], [subject=], [text=], [html=], [attachments=], [inline_attachments=]) → anvil.email.SendReport instance` [(more info)](/docs/email)

Send an email

-   `to` - The email recipient[s] in the 'To' field. Can be a string or list of strings. Each string can be a bare address (eg 'joe@example.com') or include a display name (eg 'Joe Bloggs <joe@example.com>').

-   `cc` - The email recipient[s] in the 'Cc' field. Can be a string or list of strings. Each string can be a bare address (eg 'joe@example.com') or include a display name (eg 'Joe Bloggs <joe@example.com>').

-   `bcc` - The email recipient[s] in the 'Bcc' field. Can be a string or list of strings. Each string can be a bare address (eg 'joe@example.com') or include a display name (eg 'Joe Bloggs <joe@example.com>').

-   `from_address` - The From: address from this email. Can be a bare address (eg 'joe@example.com') or include a display name (eg 'Joe Bloggs <joe@example.com>'). If no domain is specified, or the specified domain is not a legal sending domain for this app, the address will be replaced with a valid domain. So if you specify 'noreply', the email will come from 'noreply@your-app-domain.anvil.app'.

-   `from_name` - The name associated with the From: address for this email. (Only valid if the from_address is a bare email address.)

-   `subject` - The subject line for this email.

-   `text` - The plain-text (no HTML) content for this email. You must specify at least one of 'text' and 'html'.

-   `html` - The HTML content for this email. You must specify at least one of 'text' and 'html'.

-   `attachments` - A list of Media objects to send as attachments with this email.

-   `inline_attachments` - Inline that can be used in this email's HTML, for example in <img> tags. Must be a dictionary whose keys are IDs and values are Media objects. IDs can then be used in a message's HTML with 'cid:xxx' URIs.
