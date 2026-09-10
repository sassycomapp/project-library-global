---
title: "Two-Factor Authentication"
url: "/docs/users/two-factor-authentication"
doc-id: two-factor-authentication
state: Live
date-created: 2026-09-08
---


# [Two-Factor Authentication](#two-factor-authentication)

The Users service comes with the ability to add Two-Factor Authentication, also known as Multi-Factor Authentication, out of the box.

## [Types of Two-Factor Authentication](#types-of-two-factor-authentication)

Your app’s users choose between two different types of second factor authentication. The first option is to use a hardware token such as a [YubiKey](https://www.yubico.com/) or other FIDO/FIDO2 device – this includes hardware keys built into Android phones and laptop fingerprint readers (where supported by your operating system and browser).

The second option is to use an authenticator app. Users use their authenticator app to scan the QR code provided when they are signing up to your app. This will then provide them with a six digit code they can use to log in.

Kaspersky provides a good [beginner’s guide to 2-factor authentication methods](https://www.kaspersky.com/blog/2fa-practical-guide/24219/). The guide covers both hardware keys and authenticator apps.

## [Configuring Two-Factor Authentication](#configuring-two-factor-authentication)

After [adding the Users Service](/docs/users/quickstart-login) to your application, you can enable two-factor authentication by checking the ‘Require 2-factor authentication’ box.

If you would like to handle the login process manually, you can configure two-factor authentication using code. For more details please visit [logging in using code](/docs/users/logging_in_using_code#log-in-with-two-factor-authentication).

**This is an advanced feature**, and not required if you just want to enable two-factor authentication for your app. To do that, read on.

## [Remember the Two-Factor Authentication state](#remember-the-two-factor-authentication-state)

Your app can remember the two-factor authentication state of a user’s device from 30 minutes to a year. This means that once the user has successfully provided two factors of authentication on a particular device, they won’t be prompted for the second factor again until after the selected time period.

## [Resetting a user’s second factor of authentication](#resetting-a-users-second-factor-of-authentication)

There are two ways to reset a user’s second factor of authentication:

1.  Allowing two-factor reset by email
2.  Managing two-factor for your users as an administrator

### Allow two-factor reset by email

Firstly, you can allow users to manage their second factor of authentication. To enable this simply tick the ‘Allow two-factor reset by email’ option in the Users Service. A reset link will then be visible in the Two-Factor Authentication window when users log in.

When resetting their second factor authentication, users will receive an email with a link to a reset form, the link expires in ten minutes. The reset form requires the user to provide their password and authenticate by using either their hardware token or authenticator app. You can [configure this email from the Users service](configuring-emails).

### Manage two-factor for your users

The second way to reset a user’s second factor of authentication is to manage it as the administrator of your app. Application administrators can manage the user’s second factor of authentication with the [Users Table](the_users_table).

Administrators can clear the remembered two-factor authentication state for the user by clicking the DropDown for a specific row in the User Table, and selecting ‘Clear two-factor authentication methods’. This logs the user out of all devices and requires them to enter their second factor authentication the next time they log in on each device.

Administrators can also force the user to reset their two-factor authentication the next time they log in, by selecting ‘Force two-factor authentication on next login’ from the Dropdown in the Users Table.

This forces the user to complete the reset form, which requires both their password and second factor authentication using either a hardware token or authenticator app.
