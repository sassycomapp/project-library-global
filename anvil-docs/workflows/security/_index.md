---
title: "Building Secure Apps"
url: "/docs/workflows/security"
---


# [Building Secure Apps](#building-secure-apps)

Anvil intends to provide an intuitive security model. The basic principle is, **“If you can see it, you can use it”**. This is more formally known as a *capability system*.

For example, one cannot access any of an app’s back-end services without knowing the (possibly secret) URL of that app. If a server module returns an object representing a database row or piece of media, the calling code can always read it.

Let’s look at this in a little more detail:

## [The “Share” URL](#the-share-url)

The first layer of security protecting every app is a secret URL. An app’s “Share” link contains an authentication token that is required in order to load the app. All apps on [anvil.works](https://anvil.works) are loaded over HTTPS.

You can reset and re-generate this authentication token from the [“Share” dialog](/docs/deployment/choosing-urls). This makes all previous Share links useless, as the token they contain is now invalid.

This makes it safe to have entire apps secured only by their “Share” link. You can give the client code great privileges (eg write access to [data tables](/docs/data-tables), or Google Drive [app files](/docs/integrations/google/google-drive)), as long as the URL is only shared with users who are trusted with full access to that data.

## [Client vs server code](#client-vs-server-code)

Once the app is loaded, Forms and Modules (“client code”) execute in the user’s web browser. Because the user has full control over their own web browser, a malicious user can edit Form and Module code to do whatever they want. We call this *untrusted code*: we can’t trust that Forms and Modules will do what we tell them, and we must write our app knowing that any user (with the Share link) can edit the client code to do whatever they like.

[Server modules](/docs/server), by contrast, cannot be edited by the user, so we can trust them to do what we tell them.

For example, if you wanted to check a user’s identity before letting them download a document, this should **not** be done in Form code. Forms code runs in the browser, so a malicious user could just edit the code to remove the authentication check! Instead, the Form should call a Server Module, which performs the identity check and then returns the document. (We should then use [data table permissions](/docs/data-tables/data-security) to make sure the client code can’t access the document directly.) You can read more about the difference between client and server code [here](/articles/client-vs-server).

## [Server communication](#server-communication)

The app’s communication with server code (either explicitly, with server modules, or implicitly, by the use of services) occurs over WebSockets. This connection is authenticated with the token from the app URL, and secured over HTTPS.

Server communication occurs via an RPC (Remote Procedure Call) mechanism, as described in the [Server Modules](/docs/server) section.

Arguments and return values to RPC calls can be strings, numbers, `dict`s, `list`s, `datetime.date`/`datetime`, and `None`, and may not be circular. There are also two “special” sorts of objects that can be passed to and from the server:

1.  “Live Objects” such as rows from [data tables](/docs/data-tables) and [Google Sheets](/docs/integrations/google/google-drive)

2.  [Media](/docs/working-with-files/media) objects: Any media can be sent over RPC.

    Media objects that have an authoritative source (eg Google Drive files) will have valid `url` attributes. This makes them downloadable from the client’s browser, but this is a restricted URL that will only be accessible from that browser session. Media objects that do not have an authoritative source (eg `BlobMedia`) will be copied into a new `BlobMedia` object.

Returning a “special” object to the client automatically grants read access to that object.

### Example 1:

If a server module returns one or more rows from a [data table](/docs/data-tables) to client code, that client code can read what is in the row (and any linked rows), regardless of its permissions.

The client code cannot update that row unless the [table permissions](/docs/data-tables/data-security) allow it to. However, the client code *can* pass that row back over RPC to a server module. The server module can then change the data in that row (presumably after checking that this operation should be permitted).

### Example 2:

If a Google Drive [app file](/docs/integrations/google/google-drive)’s permissions are set to “No client access”, but it is returned from a call to a server module, the client code can still use that file as a Media object. It cannot, however, edit that file’s data or properties: the client just sees a read-only `Media` object.

## [Anvil security policy](#anvil-security-policy)

We take security very seriously. If you have a query or issue with the Anvil security model or implementation, please contact us at [security@anvil.works](mailto:security@anvil.works).
