---
title: "Security and DKIM"
url: "/docs/server/email/security-and-dkim"
doc-id: security-and-dkim
state: Live
date-created: 2026-09-08
---


# [Trusting Incoming Email](#trusting-incoming-email)

Email is easy to *spoof* - to give it an inaccurate `From` address. Therefore, it’s important not to do drastic things (eg release sensitive data) just because you got an email claiming to be from someone.

## [Use a secret address](#use-a-secret-address)

One way to verify that a message is genuine is to have a secret email address (for example `8317bb91@myapp.anvil.app`). This functions like a password - only genuine users would know to send an email to that address!

A variation is to send an email *from* a secret address, and tell the user to reply to it. The real user’s replies will go to the secret address, but nobody else knows the secret address.

## [Verify the sender with DKIM](#verify-the-sender-with-dkim)

Anvil has built-in support for DKIM, which lets the sending domain prove that an email is genuine. For example, every mail from `someone@gmail.com` is signed by Gmail, so you can prove it’s genuine.

If you specify `@anvil.email.handle_message(require_dkim=True)`, then you will *only* allow messages with valid DKIM signatures for the domain in `msg.envelope.from`. So, if `msg.envelope.from` is `"someone@gmail.com"`, the email must have been signed by `gmail.com`.

```python
@anvil.email.handle_message(require_dkim=True)
def handle_message(msg):
  print(f"This message is definitely from {msg.envelope.from}")
```

You can also check this by hand. `msg.dkim.domains` is a list of all the domains that have signed this email (sometimes there can be more than one, but usually there are none or one).

```python
@anvil.email.handle_message
def handle_message(msg):
  if msg.dkim.domains is not None and 
      "gmail.com" in msg.dkim.domains:
    print("This message was signed by Gmail")

  elif msg.dkim.domains == []:
    print("This message wasn't signed at all")
```

`msg.dkim.valid_from_sender` is `True` if one of those domains is the domain of the sending address (`msg.envelope.sender`).

### Technical notes for experts

Anvil’s DKIM support accepts only signatures that cover the entire message (no `l=` parameter).

`msg.dkim.domains` is a list of the `d=` fields of all acceptable DKIM signatures.

`msg.dkim.valid_from_sender` is `True` only if the SMTP envelope `from` address ends in `@<domain>`, where `domain` is the `d=` field in an acceptable DKIM signature.
