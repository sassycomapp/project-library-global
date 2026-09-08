---
title: "Capabilities"
url: "/docs/other-concepts/portable-classes/capabilities"
---


# [Capabilities](#capabilities)

Portable Classes are great for sharing data and behaviour between client and server, but we must remember that **client code is untrusted**. This means that if you need to perform a privileged action on an object, you must do it in server code, and that server code must first verify that this client is allowed to perform the action.

You could do this by checking the client is logged in, and that the user has the appropriate permissions. But it’s easy to let these permissions get out of sync: your permissions checks might permit powerful actions on objects the client shouldn’t even be able to see!

## [The Capability Model](#the-capability-model)

One way to solve this is to use **capabilities**. A capability is an object that embodies a permission – untrusted code can perform particular operations *if and only if* it holds the correct capability.

Capabilities allow permissions to travel alongside the object they refer to, for example, to ensure that the client can only alter records that have been returned to it by a server function. This allows you to write the permissions-checking code in the server function that’s returning those records, and you only have to write it once, rather than twice (once when you’re determining which records to return and once when you’re determining whether the client is allowed to update a particular record).

## [The `anvil.server.Capability` object](#the-anvilservercapability-object)

In Anvil, capabilites are represented by [`anvil.server.Capability` objects](/docs/api/anvil.server#Capability). These special objects:

-   Can only be created in server code
-   Can be passed freely between server and client code
-   Contain a scope, describing what capability they encode. The scope is a heirarchical list of strings (or lists, numbers, or other JSON-compatible data) – the longer the list, the narrower (less privileged) the capability.
-   Are cryptographically signed by the server when returned to the client, and verified when received from the client.
-   Can be *narrowed* by any code that holds them, by appending to the scope. For example, if you hold a `Capability` with scope `["youtube_videos", "dQw4w9WgXcQ"]`, you automatically have permission to get a `Capability` with scope `["youtube_videos", "dQw4w9WgXcQ", "play"]`.

Together, these properties are all we need to build secure, efficient APIs for our apps.

## [Example](#example)

Imagine that we’re building a YouTube video manager, and we want to be able to pass around objects that represent particular videos. Several users can update videos (eg by changing their description), but only administrators can delete videos.

### Client code

Let’s start by building a portable class representing a video:

```python
@anvil.server.portable_class
class Video:
  def __init__(self, youtube_id, full_control):
    self.id = youtube_id
    if full_control:
      self.cap = anvil.server.Capability(["youtube_videos", self.id])
    else:
      self.cap = anvil.server.Capability(["youtube_videos", self.id, "update"])

  def set_description(self, new_description):
    anvil.server.call('set_video_description', self.cap, new_description)

  def delete(self):
    anvil.server.call('delete_video', self.cap)
```

We can see a few things:

-   The `__init__` method creates a `Capability` object, reflecting whether this object represents full permissions over this video (a broader scope) or just permission to update it (a narrower scope).

-   Because we can only create `Capability` objects on the server, we can only create new `Video` instances on the server. However, because this class is portable, we can *pass* instances to the client (and back to the server again if we like).

-   All privileged operations happen on the server, so the `set_description()` and `delete()` methods call server functions. They pass in the `Capability` object as proof that they have permission to perform this operation.

### Server code

Now let’s see what one of those server functions looks like:

```python
@anvil.server.callable
def set_video_description(cap, new_description):
  _, video_id, _ = anvil.server.unwrap_capability(cap, ["youtube_videos", Capability.ANY, "update"])

  requests.put("https://www.googleapis.com/youtube/v3/videos", ...)
```

We can see:

-   This function gets the video ID from the Capability, rather than a separate parameter. This is a good idea, because it makes sure that we’re operating on the same video that we’re checking the permissions for!

    Remember, malicious code can pass you a valid Capability and then malicious values for other parameters – so make sure you identify the object you’re working on from the capability’s scope!

-   The server function uses `anvil.server.unwrap_capability()` to verify the capability before it does anything, and to get the `video_id` from its scope. This is important, as malicious code could have sent any old object as that parameter! This function will throw an exception unless `cap` is not a `Capability` object with the specified scope.

    `unwrap_capability()` specifies the pattern that the capability’s scope must match – in this case, the first element must be the string `"youtube_videos"`, the second can be any value, and the third (if present) must be the string `"update"`. It returns a three-element tuple.

    (Because capabilities can always be narrowed, this function will accept a broader capability than it needs – if it needs `["youtube_videos", "dQw4w9WgXcQ", "update"]`, it will accept `["youtube_videos", "dQw4w9WgXcQ"]`. If you had given it `["youtube_videos"]` – an *extremely* broad scope – then `video_id` would have been `None`.)

### Using our new API

Now, we can use this class to implement our app’s logic. For example, here’s some server code that constructs and returns Video objects from rows in the Data Tables – granting access to those videos in the process:

```python
from my_module import Video

@anvil.server.callable
def get_my_videos():
  user = anvil.users.get_user()
  is_admin = user['is_admin']

  return [Video(row['id'], is_admin)
          for row in app_tables.videos.search(owner=user)]
```

This code does the permissions check – Is this user logged in? Are they an administrator? – once, in the same place as it returns the `Video` objects. This makes it easy to reason about which users get which level of access to which objects.
