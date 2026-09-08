---
title: "Usable configuration with Git"
url: "/docs/how-to/git-configuration"
---


# [Usable configuration with Git](#usable-configuration-with-git)

**This article is archived.**

The example presented on this page uses discontinued services from Heroku. The content and source code is preserved if you’d like to adapt it, but the embedded examples don’t work any more.

Check out up-to-date examples of what you can do with Anvil in our [tutorials](/learn/tutorials) or on the [Anvil blog](/blog)!

If you want to use Git version control with your Anvil apps, check out, Anvil’s [Version Control](/docs/version-control) documentation.

## [The configuration dilemma](#the-configuration-dilemma)

As developers, almost every app we write has configuration. Often, that configuration should really be accessible to our less technical colleagues: feature flags, rate limits, deployment signoffs, and so forth.

However, these changes also need to be tracked and audited. *“The app just broke. Did someone change the config?” “Quick, revert it to last week’s settings!”*

As programmers, we know exactly the right tool for this: Text files in version control. They’re diffable, trackable and comprehensible, and if anything goes badly wrong we can dive in with a text editor.

The problem comes when we present this solution to our non-technical colleagues. *“So, I open the terminal? And then I type `git clone` and a string of gibberish you made me memorise?”*

It’s tempting to give up and say, *“I’ll do it for you”*. Developers end up as gatekeepers, with every change coming through us.

## [GitHub API to the rescue](#github-api-to-the-rescue)

We can fix this. With the [GitHub API](https://developer.github.com/v3/), we can build an app in minutes that empowers our colleagues to change configuration on their own – with all the power of Git’s versioning and auditing.

I’ve built a simple app, hosted on Heroku (source at [github.com/anvil-ph-test/edit-demo](https://github.com/anvil-ph-test/edit-demo)). It has a configuration file (called `config.json`) that determines vital parameters such as the font and background colour.

Here’s how I built an Anvil app to edit that configuration, with less than a dozen lines of code:

## [Getting the config](#getting-the-config)

First, we need to grab the latest version of our config file:

```python
self.gh_record = anvil.http.request("https://api.github.com/repos/anvil-ph-test/edit-demo/contents/config.json", json=True, username="abc", password="123")
```

Github returns some information about this file, and its content in base64:

```python
  {
    "name": "config.json",
    "encoding": "base64",
    "size": 67
    """...several other bits omitted..."""
    "content": "eyJ1cHBlcmNhc2UiOnRydWUsImZvbnQiOiJIZWx2ZXRpY2EiLCJiYWNrZ3Jv\ndW5kIjoiYmxhbmNoZWRhbG1vbmQifQ==\n",
    "sha": "bfb17ee5edf43a54f6756f032603872ca7dce320",
  }
```

The content is what we care about:

```python
  self.item = json.loads(base64.b64decode(self.gh_record["content"]))
```

The decoded data looks like this:

```python
  {
    "background": "blanchedalmond",
    "font": "Helvetica",
    "uppercase": true
  }
```

All we need now is to design our configuration interface. With Anvil’s [data bindings](https://anvil.works/doc#data_bindings), it’s all drag-and-drop - we can just specify which JSON key (in `self.item`) each text-box or check-box corresponds to. That’s all we need for a read-only interface.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:VQCJ2FA53XBJAHQQ%3dQOC34HWBQ73FL4M34GVY6YTK)

## [Committing our config](#committing-our-config)

Now we have read-only access to our configuration, the next step is to save our changes. As we interact with the text-boxes and check-box, `self.item` is automatically updated.

Now we just push this data back to the server, with an HTTP `PUT` request to the same URL. All GitHub needs is the new content for the file, a commit message, and the previous SHA hash of this file:

```python
  new_record = {'content', base64.b64encode(json.dumps(self.item)),
                'message', 'Edit from the web'}
                'sha': self.gh_record["sha"]}

  anvil.http.request("https://api.github.com/repos/anvil-ph-test/edit-demo/contents/config.json", method="PUT", data=new_record, json=True, username="abc", password="123")
```

And here’s the working app, capable of updating the settings:

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:HWXTRQXTLJMXJEM2%3dS7KOIA2QBEJB4LTCNCS2A24Y)

Once you’ve saved your changes, scroll up and refresh the example app. Be patient - it may take a few seconds to re-deploy with the new config.

## [Increased security](#increased-security)

OK, we’re not quite done. So far, we’re doing everything on the client side, which means everyone with the URL can access our authentication information! Even if we only give that URL out to people we (mostly) trust, it’s far too easy for it to end up in the wrong hands.

Instead, we’ll do our GitHub API calls on the server side, and expose only two functions to the client: `save_config` and `load_config`. All the rest is safely on the server, where the user can’t see it:

```python
# This code runs on the server
@anvil.server.callable
def load_config():
  gh_record = anvil.http.request("https://api.github.com/repos/anvil-ph-test/edit-demo/contents/config.json", json=True, username="abc", password="123")

  return (gh_record['sha'], json.loads(base64.b64decode(gh_record['content'])))


@anvil.server.callable
def save_config(data, last_sha):
  new_record = {'content': base64.b64encode(json.dumps(data)),
                'message': 'Edit from the web',
                'sha': last_sha}
  r = anvil.http.request("https://api.github.com/repos/anvil-ph-test/edit-demo/contents/config.json", method="PUT", data=new_record, json=True, username="abc", password="123")

  return r['content']['sha']
```

## [Job done.](#job-done)

There you have it - a secure, functional configuration editor, ready for our non-technical colleagues to use. You don’t need to know Git to use it, but it does have full tracing and history of every change.

## [Conclusions](#conclusions)

**1.** We don’t have to sacrifice the benefits of Git for our configuration, just in order to get a user-friendly admin interface. We can have both!

**2.** The [GitHub API](https://developer.github.com/v3/) is awesome.

**3.** [Anvil](https://anvil.works) lets you build useful web apps very, *very* quickly.

Why not [clone this example app](/ide#clone:HWXTRQXTLJMXJEM2=S7KOIA2QBEJB4LTCNCS2A24Y), read its source code, and try it out yourself?

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:HWXTRQXTLJMXJEM2%3dS7KOIA2QBEJB4LTCNCS2A24Y)
