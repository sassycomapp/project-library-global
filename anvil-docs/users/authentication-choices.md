---
title: "Authentication Choices"
url: "/docs/users/authentication-choices"
---


# [Authentication Choices](#authentication-choices)

The Users service supports the following sign-in methods:

## [Email + Password](#email--password)

Users sign in with an email address and a password. These will be stored in the `email` and `password_hash` columns of the Users table. The password is hashed with the industry standard [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) algorithm, which means that knowing the `password_hash` does not tell you the password. (You should still keep the hashes secret, to avoid [brute force attacks](https://en.wikipedia.org/wiki/Password_cracking) on weak passwords; you can enable ‘Require secure passwords’ to help mitigate this too.)

Email and password sign in can also use [Two-Factor Authentication](two_factor_authentication) to improve security.

If email confirmation is enabled (the default), a user cannot use their account until they confirm ownership of their email address by clicking a confirmation link.

A user can reset their password by confirming ownership of their email address. If authentication fails, the built-in log-in form (`login_with_form()`) will offer a password reset option. If you are not using the built-in log-in form, [see here for instructions](logging-in-using-code#password-reset) on using `anvil.users.send_password_reset_email()`.

Email + password authentication is enabled by default. The confirmation and password reset emails can be [configured through the Users service](configuring-emails).

### Too many password failures

To protect users from brute-force password guessing attacks, if an incorrect password is entered for a user ten times in a row, that user will be unable to log in with password authentication, and must reset their password via email. If you are logging from code, you can identify this situation by [catching the `anvil.users.TooManyPasswordFailures` exception](logging-in-using-code#handling-exceptions) (a subclass of `AuthenticationFailed`).

## [Sign in with Google](#sign-in-with-google)

Users sign in with a Google account. Their identity is stored in the `email` column of the Users table. (This means that a user who registers with “Email + Password” can then sign in with Google if the email address is the same.)

Google authentication is disabled by default. If you enable Google authentication, the Google Service will be added to your app automatically for you as well.

## [Sign in with Facebook](#sign-in-with-facebook)

Users sign in with a Facebook account.

Facebook authentication is disabled by default. If you enable Facebook authentication, the Facebook Service will be added to your app automatically. You need to register your app in the Facebook for Developers Console, see [Connecting Facebook to Anvil](../integrations/facebook/linking-facebook-and-anvil) for a step-by-step guide.

## [Sign in with Email Link](#sign-in-with-email-link)

Users sign in by following a link in their email. This email can be [configured in the Users service](configuring-emails).

The Email Link sign in method is disabled by default. If you enable Email Link sign in, any user who’s email is in your user table can request a login link get sent to their email from the login page. The user simply follows the link to be signed in to the app.

Each link expires after 10 minutes.

## [Sign in with Microsoft](#sign-in-with-microsoft)

Users sign in with a Microsoft account.

You can choose who can log in:

-   Users with any Microsoft account
-   Users in your own Microsoft Entra organisation

You configure this when you connect Microsoft Entra ID to Anvil - see [Connecting Entra ID to Anvil](../integrations/microsoft/linking-azure-and-anvil) for a step-by-step guide

Microsoft authentication is disabled by default. If you enable Microsoft authentication, the Microsoft Service will be added to your app automatically. You need to register your app in the Microsoft Entra admin center, as explained in [Connecting Entra ID to Anvil](../integrations/microsoft/linking-azure-and-anvil).

This is available to users on Business plans and above. Please email [contact@anvil.works](mailto:contact@anvil.works?subject=Microsoft+authentication) for more information.

## [Local Active Directory](#local-active-directory)

Anvil can authenticate users against your organisation’s Active Directory. This means you can easily re-use your existing security investments for your business applications.

This is available on our Enterprise plans. Please email [contact@anvil.works](mailto:contact@anvil.works?subject=Active+Directory) for more information.

## [Client certificates](#client-certificates)

Anvil can authenticate users using X.509 client certificates or PKI (Public Key Infrastructure). This means you can easily re-use your existing security investments for your business applications.

This is available on our Enterprise plans. Please email [contact@anvil.works](mailto:contact@anvil.works?subject=Client+certificates) for more information.

## [SAML Authentication](#saml-authentication)

Anvil can authenticate users using SAML Authentication - see [SAML Authentication](../integrations/saml) for more information.

This is available to users on Business plans and above. Please email [contact@anvil.works](mailto:contact@anvil.works?subject=SAML+authentication) for more information.
