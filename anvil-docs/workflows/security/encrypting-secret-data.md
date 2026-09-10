---
title: "Encrypting Secret Data"
url: "/docs/workflows/security/encrypting-secret-data"
doc-id: encrypting-secret-data
state: Live
date-created: 2026-09-08
---


# [Encrypting Secret Data with App Secrets](#encrypting-secret-data-with-app-secrets)

[Watch our App Secrets tutorial](/blog/app-secrets)

When your web app is handling sensitive information — be it API credentials, database passwords, or sensitive personal data — it’s important to keep it protected. It certainly shouldn’t be sitting in your source code, for anyone to see. It should be kept encrypted, until the time it’s needed. This is called **encryption at rest**.

The App Secrets service provides easy-to-use encrypted storage of secrets (e.g. passwords) and encryption keys (which can be used to encrypt your data).

To store encrypted secrets in your apps, first add App Secrets by clicking the **+** button in the [Sidebar Menu](/docs/editor#sidebar-menu).

## [Configuration](#configuration)

When you select the App Secrets service, you see a list of your app’s secrets and encryption keys, which you can add, edit or delete.

Each secret has a name, and a value (a text string). The value is stored, encrypted, in the application source code. It is possible to extract the value from this service, but if you do so, an email will be sent to the application’s owner.

**Set Value** - Set the value of a secret, overwriting any previous value. Use this to store known values, such as API credentials or the connection string for an external database.

**Generate Value** - This generates a strong random value (currently a 128-bit value expressed as base64). Use this to generate a new value (eg for a password).

You can also add, remove, or reset encryption keys. If you reset an encryption key, you replace it with a newly-generated key with the same name. Encryption keys are also stored, encrypted, as part of your application’s source code.

## [Using secrets from code](#using-secrets-from-code)

To get the value of a secret, call `anvil.secrets.get_secret()`.

```python
token = anvil.secrets.get_secret('github_token')
```

### Using encryption keys from code

You can encrypt or decrypt strings using an encryption key.

```python
def encrypt_value(plaintext):
  return anvil.secrets.encrypt_with_key('encryption_key',
                                        plaintext)

def decrypt_value(ciphertext):
  return anvil.secrets.decrypt_with_key('encryption_key',
                                        ciphertext)
```

If the string you attempt to decrypt is not a valid ciphertext (i.e. it was not encrypted with the same key you are using for decryption, or it has been tampered with), an `anvil.secrets.SecretError` will be raised.

`anvil.secrets` functions can only be called from [Server Module](/docs/server) code (not client code, or even [Uplink](/docs/uplink) code).

## [Secrets versioning](#secrets-versioning)

Secrets are versioned along with the code.

If you’ve published a particular version of your app using the Version History window, the published app will use the secrets as they were at that version. This ensures that the secrets and the code are always consistent. To update the secrets in your published app, you will need to save a new version and publish that.

If you are not pinning the published app to a particular version, but simply using the latest version as the published app, the latest secrets will be used.

## [Encryption architecture](#encryption-architecture)

App secrets are stored, encrypted, with the source code to your app.

App Secrets are encrypted with an **app-specific key**, meaning that encrypted secrets cannot be copied into another app and used there.

If you have separate [Development and Production apps](/docs/how-to/development-production) and would like secrets to persist between your apps, email [support@anvil.works](mailto:support@anvil.works) with the App IDs for your two Apps, and we’ll set the internal encryption key to be the same on both apps.

All encryption is performed with 128-bit AES-GCM:

-   The secret’s value (which you can extract with the IDE) is a base64-encoded 128-bit AES key.
-   The encrypted payload is base64 encoded.
-   Encryption is done in AES-GCM, with the IV transmitted as the first 12 bytes of the payload

This standard encryption operation avoids many common cryptographic pitfalls.

## [Threat model](#threat-model)

The App Secrets service protects you against the following threats:

-   **Database disclosure** - Encrypting your data at rest means that, if your application contains a security vulnerability that discloses data, the data will remain encrypted and therefore useless to an attacker. (Successful breach would then require a *second* vulnerability that exposed decryption functionality. This is an example of defence in depth.)
-   **Editor visibility** - It prevents secrets from being visible “over-the-shoulder” while developers are working on the application, or when they have the application checked out with Git.
-   **Cryptographic misuse** - Cryptographic primitives are commonly misapplied, even by experts, leading to vulnerabilities. Anvil exposes a simple set of safe cryptographic operations that prevent common errors.

## [Security feedback](#security-feedback)

We welcome engagement from the security community. If you need to know more, have questions, or need to report a security vulnerability, please get in touch by email at [security@anvil.works](mailto:security@anvil.works).

## [Customised audit](#customised-audit)

Anvil supports customised audit capabilities that enhance traceability of material from the app secrets service, protecting against insider threats. For more information on these enterprise features, please get in touch with us at [security@anvil.works](mailto:security@anvil.works).
