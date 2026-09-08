---
title: "Google"
url: "/docs/integrations/google"
---


# [Google Service](#google-service)

Anvil has built-in functionality to integrate your apps with Google services.

The [Quickstart](google/quickstart) shows you how to upload a file to Google Drive from your app’s User Interface.

Here’s what else you can do:

### Google Authentication

You can log users in with their Google accounts, meaning they don’t have to sign up for your app - this is analogous to the login options for [Microsoft](microsoft) and [Google](google) accounts.

### Google Drive

You can create, view, edit and delete files in [Google Drive](google/google-drive) - these can be your own files, or you can use your users' files (after displaying a permissions dialog).

### Google Sheets

Anvil’s [Google Drive](google/google-drive) integration has a Python API for reading and editing Google Sheets that works in a similar way to Data tables. This is a good alternative data store, and it’s useful to be able to import data from spreadsheets or export data to spreadsheets.

### Sending emails with Gmail

You can automate sending of emails using Gmail (although check whether the [Email Service](/docs/email) suits your needs first as it allows larger volumes of mail.)

### Using Google REST APIs

There are also convenient ways to get and refresh [Google REST API](google/google-rest-apis) access tokens. In combination with Anvil’s [HTTP module](/docs/http-apis/making-http-requests), this makes it easy to integrate your Anvil app with any Google APIs. In our code example, we show you how to get emails from the logged-in user’s Gmail inbox.
