---
title: "Cache Updates"
url: "/docs/other-concepts/portable-classes/capability-scoped-cache-updates"
doc-id: capability-scoped-cache-updates
state: Live
date-created: 2026-09-08
---


# [Capability-Scoped Cache Updates](#capability-scoped-cache-updates)

If you’re using portable objects to represent long-lived server-side resources, you probably don’t want to go back to the server every time you fetch a property from your object. You want to *cache* that information as part of your object.

But what happens when some server-side code updates that object? You want to update that cache, otherwise your client side will see stale data.

**But**, sometimes the server-side code is updating something secret that we don’t want the client to know about! So we only *sometimes* want to transmit cache updates.

To solve this problem, Anvil allows you to transmit updates about a *particular Capability scope*, by calling [`send_update()`](/docs/api/anvil.server#Capability_methods) on a Capability object. These updates will only be transmitted to the client if the client supplied that Capability as part of this call. The code at the other end can register a callback (using [`set_update_handler()`](/docs/api/anvil.server#Capability_methods)), which will be called with any updates when the server call completes.

## [Example](#example)

Let’s expand our [YouTube editor example](capabilities#example) from last time, to cache some information about each video.

We update the `Video` class to store the video description in the `description` attribute, so it can easily be displayed in the UI:

```python
@anvil.server.portable_class
class Video:
  def __init__(self, youtube_id, full_control):
    self.id = youtube_id
    # NEW: Cache the video description when we construct the object
    self.description = requests.get("https://www.googleapis.com/youtube/v3/videos", ...)

    if full_control:
      self.cap = anvil.server.Capability(["youtube_videos", self.id])
    else:
      self.cap = anvil.server.Capability(["youtube_videos", self.id, "update"])

  def set_description(self, new_description):
    anvil.server.call('set_video_description', self.cap, new_description)

  def delete(self):
    anvil.server.call('delete_video', self.cap)
```

And let’s create a server function that clears the description:

```python
@anvil.server.callable
def reset_description(video):
    video.set_description("© 2000 Anvil Records")
```

### Problem: Stale cache

Now, of course, we have a problem! After we call that function, the `description` property is out of date:

```python
    my_video = ...
    print(my_video.description)
    # prints "Charlie Bit My Finger"

    anvil.server.call('reset_description', my_video)

    print(my_video.description)
    # STILL prints "Charlie Bit My Finger"
```

But we can fix it! First, let’s alter the `set_video_description()` server function to transmit a capability-scoped update:

```python
@anvil.server.callable
def set_video_description(cap, new_description):
  video_id = cap.scope[1]
  anvil.server.unwrap_capability(cap, ["youtube_videos", video_id, "update"])]

  requests.put("https://www.googleapis.com/youtube/v3/videos", ...)

  # NEW: transmit an update
  cap.send_update({"description": new_description})
```

Now, let’s make our `Video` class understand these updates:

```python
@anvil.server.portable_class
class Video:
  def __init__(self, youtube_id, full_control):
    self.id = youtube_id
    self.description = requests.get("https://www.googleapis.com/youtube/v3/videos", ...)

    if full_control:
      self.cap = anvil.server.Capability(["youtube_videos", self.id])
    else:
      self.cap = anvil.server.Capability(["youtube_videos", self.id, "update"])

    # NEW: Handle updates on our capability

    self.cap.set_update_handler(self._handle_cache_update)

  def __deserialize__(self, data, global_data):
    self.__dict__.update(data)
    self.cap.set_update_handler(self._handle_cache_update)

  def _handle_cache_update(self, update):
    self.description = update['description']

  def set_description(self, new_description):
    anvil.server.call('set_video_description', self.cap, new_description)

  def delete(self):
    anvil.server.call('delete_video', self.cap)
```

Note that we have to set the update handler whether the object is constructed from scratch (with `__init__`) or reconstructed off the wire (with `__deserialize__`). We rely on the default `__serialize__` behaviour, which just returns `self.__dict__`.

You can [read more about serialisation](custom-serialisation) in our docs.

### Problem solved.

Now, when we call `reset_description`, our `Video` object will be updated:

```python
    my_video = ...
    print(my_video.description)
    # prints "Charlie Bit My Finger"

    anvil.server.call('reset_description', my_video)

    print(my_video.description)
    # prints "© 2000 Anvil Records"
```

#### How it works

When we call `reset_description()`, we’re passing the whole `Video` object, including its capability – so Anvil’s serialisation machinery *knows* that we have access to this capability. When `reset_description()` calls `set_video_description()`, it also passes the capability. So Anvil knows to transmit the update to the calling code, where it triggers the update handler and updates.

Remember, this only happens because the client has *proven* that it’s allowed to see these updates. If the client hadn’t passed the `Video` object to the server, then the update would have stayed secret.

When you build an API like this, things “just work”. For example, whoever wrote the `reset_description()` function never had to worry about caching! That’s an internal detail, handled by the `Video` class – just as it should be.
