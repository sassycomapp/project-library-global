---
document: "anvil.google.mail"
title: "anvil.google.mail"
url: "/docs/api/anvil.google.mail"
doc-id: anvil.google.mail
state: Live
date-created: 2026-09-08
---


## `anvil.google.mail` Module

#### Functions

[`send`](#send)

## Functions

#### `send([to=], [subject=None], [text=None], [html=None], [cc=], [bcc=], [from_address=None], [draft=False])`

Send an email via GMail. 'to', 'cc' and 'bcc' may be strings (email addresses) or lists of strings (multiple addresses). At least one of 'text' and 'html' need to be provided (both strings). Passing draft=True will create a draft message rather than sending it.
