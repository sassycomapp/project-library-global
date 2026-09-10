---
title: "URL Routing"
url: "/docs/client/navigation/routing"
doc-id: routing-_index
state: Live
date-created: 2026-09-08
---


# [URL Routing](#url-routing)

**This feature is optional** - you can make perfectly functional apps in Anvil without routing.

This documentation will primarily be focused on Anvil’s **Routing dependency**.

Using this dependency is not the only way to implement routing in an Anvil app, but we recommend using it above all other solutions.

Routing enables URL-based navigation in your app. Instead of the entirety of your app being bound to a single URL, every page and state of your app can be given a URL address.

This allows things like using the browser’s back and forward buttons, or bookmarking specific pages of your app.

## [Feature overview](#feature-overview)

Among several others, Routing offers the following features:

-   **URL navigation through routes**: By setting up Route objects with a Form and a URL path, the Routing dependency can take care of opening Forms based on which URL is currently being navigated to.

-   **Caching**: Routes can be configured to perform Form caching and/or data caching, storing Forms or data for later use instead of repeating the instantiation process every time a Form needs to be opened.

-   **URL parametrization**: Parameters can be embedded in a URL and passed to the Form. This allows access to specific Form states directly through URL history or bookmarks.

## [Installation](#installation)

If you are installing Routing as a dependency, you will need to migrate your app to make use of Layouts. For a how-to on porting your app to use Layouts, see [our documentation here](/docs/how-to/porting-app-to-new-layouts).

The Routing dependency can be installed through Anvil’s [dependency framework](https://anvil.works/docs/deployment-new-ide/dependencies#using-other-apps-as-libraries).

Routing’s app token is:

-   **`3PIDO5P3H4VPEMPL`**

If you are on a self-hosted plan, either via an enterprise plan or by using the [Anvil App Server](https://anvil.works/docs/how-to/app-server), this code might not work.

This code must be pasted into the third-party dependencies section of your app. In your app, go into settings, then dependencies, click on third party and paste in the dependency code. You will need to migrate your app to make use of layouts.

The Routing app can also be cloned, allowing you to use it as an app of your own.

[Clone the Routing App](https://anvil.works/build?l=clone-link#clone:3PIDO5P3H4VPEMPL%3d6EBCIZ4W4ZHU2IFHY3XGP6VG)

Alternatively, you can clone the Routing app directly from [its GitHub repository](https://github.com/anvil-works/routing). This will let you use the clone of Routing from your own apps as your dependency. After cloning the Routing app, in your other app, go into settings, then dependencies, and select the Routing app out of the dependencies dropdown. You will need to migrate your app to make use of layouts.

You can find the full in-depth technical documentation for the Routing dependency [here](https://routing-docs.anvil.works/).
