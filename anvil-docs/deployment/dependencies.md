---
document: "Depending On Other Apps"
title: "Depending On Other Apps"
url: "/docs/deployment/dependencies"
doc-id: deployment-dependencies
state: Live
date-created: 2026-09-08
---


# [Depending On Other Apps](#depending-on-other-apps)

## [Reusing Components and Code](#reusing-components-and-code)

You can reuse [Forms](/docs/client/components/forms), [Custom Components](/docs/client/custom-components) and code from one Anvil app in another by making the app available as a library. Choose “Dependencies” from the Settings Menu.

## [Making an app available as a library](#making-an-app-available-as-a-library)

In the example below, we have made the current app available under the package name “`my_app`”. This means that [Forms](/docs/client/components/forms), [Custom Components](/docs/client/custom-components) and modules from this app can be used by any app that has this app as a dependency.

## [Using other apps as libraries](#using-other-apps-as-libraries)

In the App Dependencies dialog, you can also import other apps as dependencies.

To use your own apps (or apps you have cloned into your account), click the “My Apps” tab in the dialog and select the app you want to use.

You can also use third-party dependencies by choosing “Third Party” in the App Dependencies dialog and entering a third-party app token. If you would like to enable your app as a third-party dependency, please contact [support@anvil.works](mailto:support@anvill.works).

In this example, we’ve imported the **Useful Components** app (which has the package name `useful_components`). Any custom components in that app will now show up in the [Toolbox](/docs/editor/form-editor#toolbox) in this app.

You can choose to depend on the **Published** or **Development** (most recent) version of the app. Note that if the library app does not have a published version, both options will refer to the most recent version.

You can also refer to library apps in code by importing them as packages. In this way, you can use custom components and modules from libraries directly.

```python
from useful_components.Widget import Widget

self.add_component(Widget())
```

Any dependencies of an app you depend on will also be available to your app (dependencies are *transitive*).

It is possible to depend on apps that you own (or your organisation owns), or on public “third-party dependencies”. If you would like to make your app a third-party dependency so that others can rely on it, email `support@anvil.works`. Otherwise, to use an app that someone else wrote as a library, you should clone their app and then depend on your copy.

## [Depending on a version of an app](#depending-on-a-version-of-an-app)

By default, when you add a dependency on an app, you depend on the `master` branch. However, it is also possible to depend on a particular version of a dependency’s code. You can depend on:

-   **Released versions:** If an app has tagged a particular version with a tag that begins with `v` and then dot-separated numbers (eg `v1.0.1`), you can choose that version when depending on the app.

-   **Other branches:** If an app has branches other than `master`, then you can depend on any of those branches. (Branch names containing the `/` character will not be available to choose.)
