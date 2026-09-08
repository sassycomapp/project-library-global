---
title: "anvil.google.mail"
url: "/docs/api/anvil.google.mail"
---


## `anvil.google.mail` Module

#### Functions

[`send`](#send)

## Functions

#### `send([to=], [subject=None], [text=None], [html=None], [cc=], [bcc=], [from_address=None], [draft=False])`

Send an email via GMail. 'to', 'cc' and 'bcc' may be strings (email addresses) or lists of strings (multiple addresses). At least one of 'text' and 'html' need to be provided (both strings). Passing draft=True will create a draft message rather than sending it.
