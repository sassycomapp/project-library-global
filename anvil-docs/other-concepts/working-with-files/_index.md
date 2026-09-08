---
title: "Files, Media and Binary Data"
url: "/docs/other-concepts/working-with-files"
---


# [Working With Files, Media And Binary Data](#working-with-files-media-and-binary-data)

Anvil has built-in support for uploading, storing, downloading, and manipulating files and other binary data.

There are 3 ways to work with files in Anvil:

### [Dynamic Files, Media and Binary data](/docs/working-with-files/media)

Dynamic Files, media and other binary data (pictures, uploaded files, etc.) are represented in Anvil as **Media objects**. Media objects are created by Anvil APIs such as [FileLoader](/docs/client/components/basic#fileloader) components and the [Google Drive API](/docs/integrations/google/google-drive). You can also create them directly in Python code from [byte strings or source URLs](/docs/working-with-files/media).

Media objects allow you to pass binary data between client and server code.

### [Static Data Files](/docs/working-with-files/data-files)

Static Data Files are files that you, as the app developer, can attach to your app. These files are available in your [Server Modules](https://anvil.works/docs/server#server-modules). Static Data Files are useful for machine learning models, large datasets and data that stays constant or changes rarely.

To add Data Files to your Anvil app, click the **+** button in the Sidebar Menu, and select **Data Files**.

### [Assets](/docs/client/customisation/assets)

Assets are files that are part of your app’s source code. For development of your app, you can add your own HTML templates, CSS files, JavaScript or images to [Assets](/docs/client/themes-and-styling#adding-your-own-asset-files). Files in Assets are mostly used to customise your app’s [Theme](/docs/client/themes-and-styling) or to inject your own [JavaScript objects](/docs/client/customisation/javascript).

You don’t need to write HTML, CSS or JS to use Anvil - but [we know it’s nice to have the option.](https://anvil.works/blog/escape-hatches-and-ejector-seats)
