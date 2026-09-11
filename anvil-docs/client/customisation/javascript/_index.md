---
document: "Using JavaScript"
title: "Using JavaScript"
url: "/docs/client/customisation/javascript"
doc-id: javascript-_index
state: Live
date-created: 2026-09-08
---


# [Using JavaScript](#using-javascript)

**This feature is optional** - you do not need to know JavaScript to use Anvil!

However, if you do know JavaScript, and want to integrate with a low-level browser API or an existing JavaScript library, this reference will allow you to access all those low-level details from Anvil.

Check the [Quickstart](javascript/quickstart) to see this feature in action.

## [Client-side Python and JavaScript](#client-side-python-and-javascript)

When you write **client-side code** in Anvil, Anvil translates it to Javascript, and that’s how the browser executes it. This means that you can interact with Javascript libraries from your Python code, or even write your own Javascript.

## [Injecting your own JavaScript](#injecting-your-own-javascript)

You can inject your own JavaScript in various ways:

-   by writing JavaScript in the [Native Libraries](#using-native-javascript-libraries)
-   by writing JavaScript in [Custom HTML Templates](/docs/ui/custom-styling/custom-html-forms)
-   by importing JavaScript from [external libraries](javascript/quickstart)
-   by including JavaScript files in [theme assets](/docs/client/customisation) and referencing [these files](/docs/client/customisation#asset-file-url) in Native Libraries or HTML Forms

## [Accessing JavaScript from Python](#accessing-javascript-from-python)

### anvil.js

Anvil’s [`js module`](/docs/api/anvil.js) is the rosetta stone for accessing JavaScript variables in Python code. Check the [Quickstart](javascript/quickstart) for a worked example, or get a more in-depth look at [how this works](javascript/accessing-javascript).

### HTML Forms

HTML Forms can also include `<script>` tags. HTML Forms can interact with JavaScript functions using their `self.call_js()` method. [Find out how](javascript/html-forms).

## [Using Native JavaScript libraries](#using-native-javascript-libraries)

To use Native Libraries with Anvil, select the **Native Libraries** option in the [App Browser](/docs/editor#app-browser).

Any HTML you add to the “Native Libraries” section will be inserted into the `<head>` tag of your Anvil app’s HTML. This is a great place to add a `<script>` tag to pull in an external library (or a `.js` file in your app’s Assets). You can also use `<link>` tags to refer to external CSS.

## [Anvil already includes some JavaScript](#anvil-already-includes-some-javascript)

If your JavaScript is acting weird, it might be because you have overwritten something important.

For example, it is a bad idea to load jQuery or Bootstrap JavaScript explicitly from an HTML template — it will overwrite the versions Anvil has already loaded. Here is a partial list of JavaScript libraries Anvil loads:

-   jQuery version 3 (minor versions may be upgraded without warning)
-   Bootstrap version 3.4 (minor versions may be upgraded without warning)
-   The [Skulpt](https://github.com/skulpt/skulpt) Python-to-JavaScript compiler

## [Anvil Examples](#anvil-examples)

### Driving JavaScript APIs

-   [A mapping app](/articles/mapbox-isochrone) - built with [Mapbox](https://mapbox.com/)’s [Isochrone](https://docs.mapbox.com/api/navigation/isochrone/) and [Geocoding APIs](https://docs.mapbox.com/api/search/geocoding/)
-   [Analytics Data](/articles/segment-tracking) - using [Segment](https://segment.com/), a tool for collecting customer interaction data from your apps and websites
-   [A simple dashboard](/articles/fusion-charts) - using the [FusionCharts library](https://www.fusioncharts.com/)
-   [3d Christmas Tree](/advent/3d-tree) - using [Three.js](https://threejs.org/), a library for displaying 3D content on the web
-   [Tabulator](https://anvil.works/forum/t/tabulator-with-anvil-components/4646) - a [libary](http://tabulator.info/) for creating rich tables on the web
-   [HashRouting](https://anvil.works/forum/t/hashrouting-routing-navigation-with-url-hash/3949) - drive window navigation from Python
-   [Popover](/library/popovers) - using `jQuery` to implement [bootstrap popovers](https://getbootstrap.com/docs/3.3/Javascript/#popovers)
-   [AnvilAugment](https://anvil.works/forum/t/anvilaugment-hover-focus-key-bindings-dependency/3809) - using `jQuery` events on anvil components
