---
title: "The Users Table"
url: "/docs/users/the-users-table"
doc-id: the-users-table
state: Live
date-created: 2026-09-08
---


# [The Users Table](#the-users-table)

The [table](/docs/data-tables) of users is created for you automatically when you configure the Users service. Many of the columns are automatically added at the moment they’re first needed.

You don’t have to use this table, you can use any table you like. Just delete the auto-generated table from your apps default database and you’ll see a message at the bottom of the Users Service. Click ‘Choose existing table’ to select a different table from this app or from any of your other apps.

## [Single Sign-On between apps](#single-sign-on-between-apps)

To share users between apps, use the Users table from another app. By sharing one Users table between many apps, you can provide single-sign-on for all your apps simultaneously.

## [Users Table Columns](#users-table-columns)

The following columns will be automatically added to the Users table. Feel free to use or manipulate them yourself, or add more:

-   `email` - The user’s email address
-   `enabled` - A boolean value indicating whether this user is allowed to log in. Uncheck to lock an account.
-   `last_login` - The date and time when this user most recently logged in
-   `password_hash` - A bcrypt hash of the user’s password (password-based authentication only)
-   `n_password_failures` - The number of consecutive times a user has failed to login due to using an incorrect password. Resets back to 0 upon a successful login.
-   `confirmed_email` - A boolean value indicating whether this user has confirmed their email address (password-based authentication only; only if email confirmation is enabled)
-   `signed_up` - The date and time when this user registered
-   `confirmation_key` - A secret value used in the confirmation and password-reset links (password-based authentication only)

Add columns to your Users table to store extra information about a user. It’s very common to add a `role` column to store user roles (e.g. “is this user an administrator?”).

## [Case Sensitivity](#case-sensitivity)

When a user signs up for your app with any of the built-in sign-up functions (e.g. `signup_with_email()`), their email is lowercased before being stored in the Users table. When a user logs in, the Users table is searched for the exact email address entered and its lowercase equivalent. For example, if a user logins in with `Customer@example.com`, this will match both `Customer@example.com` and `customer@example.com`.

If you are manually entering log-in information into a Users table, you should lowercase the login emails. This way, all logins will be case-insensitive.
