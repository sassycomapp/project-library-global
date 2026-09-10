---
title: "anvil.email.Message"
url: "/docs/api/anvil.email.message"
doc-id: anvil.email.message
state: Live
date-created: 2026-09-08
---


## `anvil.email.Message` Module

#### Classes

[`Addressees`](#Addressees) [`DKIM`](#DKIM) [`Envelope`](#Envelope)

## Classes

### `Addressees`

-   [Attributes](#Addressees_attributes)

---

---

#### Addressees Attributes

**cc_addresses** - *list(anvil.email.Address instance)*

The addresses this message was copied to.

**from_address** - *anvil.email.Address instance*

The address this message was sent from.

**to_addresses** - *list(anvil.email.Address instance)*

The addresses this message was sent to.

---

### `DKIM`

-   [Attributes](#DKIM_attributes)

---

---

#### DKIM Attributes

**domains** - *list(string)*

A list of the DKIM domains that signed this message.

**valid_from_sender** - *boolean*

Was this message signed by the domain in its envelope “from” address?

---

### `Envelope`

-   [Attributes](#Envelope_attributes)

---

---

#### Envelope Attributes

**from_address** - *string*

The email address from which this message was sent, according to the SMTP envelope.

**recipient** - *string*

The email address that received this message.

Note that this email address may not appear in any of the headers (eg if the email has been BCCed or blind forwarded).
