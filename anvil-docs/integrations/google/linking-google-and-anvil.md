---
document: "Connecting Google to Anvil"
title: "Connecting Google to Anvil"
url: "/docs/integrations/google/linking-google-and-anvil"
doc-id: linking-google-and-anvil
state: Live
date-created: 2026-09-08
---


# [Connecting Google to Anvil](#connecting-google-to-anvil)

For advanced use of Anvil’s Google integration, you need to let Google Developer Console know about your app.

If you want to do either of these things:

-   Access users’ own Google Drive files from your app
-   Use Google’s REST APIs from Anvil

You need to configure some credentials using [Google Developer Console](https://console.developers.google.com/apis/).

[This Google support answer](https://support.google.com/googleapi/answer/6158849?ref_topic=7013279) describes the basic process. We’ll go through it in more detail in the following sections.

## [Create a Project](#create-a-project)

Open [Google Developer Console](https://console.developers.google.com/apis/). Create a project or select an existing project.

Then select ‘APIs and services’ from the hamburger menu.

Select ‘Credentials’.

First, you need to set up an OAuth consent screen. Then, you can create an OAuth Client ID that allows your Anvil app to identify your Google project.

## [Set up an OAuth consent screen](#set-up-an-oauth-consent-screen)

Click on ‘OAuth consent screen’. This is where you set up the screen that your users will see to give your app certain permissions on their Google account. You’ve probably seen this sort of screen before when using a new app, it will say something like “App X would like to: use your location”.

The first part of this form is pretty self-explanatory; keep the application type as ‘Public’ and set your application name and logo as appropriate.

The ‘Scopes for Google APIs’ section allows you to list the permissions to request from the user. If you want to access your users’ Google Drive files, you will need to add `../auth/drive.file`.

In the ‘Authorised domains’ section, add any domains your app will be running under. This may be `anvil.works` for running your app in the editor, `anvil.app` for the live version, or your own domain if you’re using a Custom Domain.

## [Create an OAuth Client ID](#create-an-oauth-client-id)

Click on ‘Credentials’, then ‘Create Credentials’ and select OAuth Client ID.

You’re given a list of application types - choose ‘Web application’.

Now enter `https://anvil.works/apps/_/client_auth_callback` in ‘Authorised redirect URIs’. Be sure to press enter in this box so that it gets added to the list.

Hit ‘create’ and you will be shown the client ID and secret.

Now go to your Anvil app and open the Google API Service. Paste the client ID and secret into the boxes in the “Access your users’ Google Drive files” section.

## [Test that it works](#test-that-it-works)

You should now be able to use any Google REST APIs you have requested scopes for. If you have requested the `../auth/drive.file` scope, you can run this code to log someone in with their Google account read the names of their Google Drive files (after they give their permission):

```python
  anvil.google.drive.login()

  folder = anvil.google.drive.get_user_files()

  for f in folder.list_files():
    print(f["title"])
```

If this works, you’ve correctly set up Anvil to access your Users’ Google Drive files and use Google REST APIs.

## [Next up](#next-up)

Now that you’ve configured Google Developer Console, you can use some of the advanced features of Anvil’s Google integration.

### Access your users’ Google Drive files

Anvil has a built-in Python API for [accessing your users’ Google Drive files](/docs/integrations/google/google-drive).

### Access Google REST APIs

You can [access any of Google’s REST APIs](/docs/integrations/google/google-rest-apis) from client or server code using Anvil’s `anvil.http.request` function.
