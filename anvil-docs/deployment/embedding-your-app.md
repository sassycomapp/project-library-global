---
document: "Embedding Your App"
title: "Embedding Your App"
url: "/docs/deployment/embedding-your-app"
doc-id: embedding-your-app
state: Live
date-created: 2026-09-08
---


# [Embedding Your App in a Web Page](#embedding-your-app-in-a-web-page)

You can allow embedding of your published Anvil apps into other web pages. To do this, go to your app’s settings from the Sidebar menu and choose Embedding. There, tick the checkbox next to “Allow this app to be embedded in other pages”. If your app is published, a block of code will appear that you can copy and paste into a page to display your app.

If embedding is disabled, your app will be served with the `X-Frame-Options: deny` header. When that’s the case, browsers will refuse to load your app if it is embedded inside another page.

## [Running your app in an IFrame](#running-your-app-in-an-iframe)

If embedding is enabled and your app is published, you’ll see an HTML snippet you can copy and paste into any page.

```html
<script src="https://anvil.works/embed.js" async></script>
<iframe style="width:100%" data-anvil-embed src="https://online-store.anvil.app"></iframe>
```

The `<script>` tag automatically resizes the `<iframe>` to fit the vertical space used by your apps. If you omit the `<script>` tag entirely, your apps will still load, but the `<iframe>` will no longer automatically resize.

## [Embedding Multiple Apps](#embedding-multiple-apps)

You can embed multiple apps into one page using multiple `<iframe>`s with different `src` URLs. If you are embedding multiple apps into one page, you only need to include the `<script>` tag once.

```html
<!-- Include the Anvil script that handles automatic vertical resizing of the IFrame -->
<script src="https://anvil.works/embed.js" async></script>

<!-- Embed one app -->
<iframe style="width:100%" data-anvil-embed src="https://online-store.anvil.app"></iframe>

<!-- Embed another app -->
<iframe style="width:100%" data-anvil-embed src="https://chatbot.anvil.app"></iframe>
```
