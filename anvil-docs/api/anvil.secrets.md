---
title: "anvil.secrets"
url: "/docs/api/anvil.secrets"
---


## `anvil.secrets` Module

#### Classes

[`SecretError`](#SecretError)

#### Functions

[`decrypt_with_key`](#decrypt_with_key) [`encrypt_with_key`](#encrypt_with_key) [`get_secret`](#get_secret)

## Classes

### `SecretError`

---

Create a new 'SecretError' object

#### Constructor

`SecretError()`

---

## Functions

#### `decrypt_with_key(key_name, value)`

Decrypt a string with a cryptographic key derived from the named secret

---

#### `encrypt_with_key(key_name, value)`

Encrypt a string with a cryptographic key derived from the named secret

---

#### `get_secret(secret_name)`

Retrieve the named secret
