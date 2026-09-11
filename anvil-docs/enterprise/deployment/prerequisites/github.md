---
document: "GitHub SSO"
title: "GitHub SSO"
url: "/docs/enterprise/deployment/prerequisites/github"
doc-id: github
state: Live
date-created: 2026-09-08
---


# [GitHub SSO](#github-sso)

Anvil Enterprise supports using GitHub or GitHub Enterprise to log in to the Anvil Editor, as well as for storing app source code.

To prepare for this, create a new GitHub App by using the following link as a template. Replace `anvil.example.com` with the primary domain of your Anvil Enterprise installation. If you are using GitHub Enterprise, replace `github.com` with the address of your GitHub Enterprise instance.

```python
https://github.com/settings/apps/new?name=Anvil%20Editor&contents=write&emails=read&administration=write&webhook_active=true&webhook_url=https://anvil.example.com/ide/github-webhook&events[]=create&events[]=delete&events[]=push&setup_on_update=true&setup_on_update=true&setup_url=https://anvil.example.com/ide/github/post-install&url=https://anvil.example.com&callback_urls[]=https://anvil.example.com/sso/github/callback&callback_urls[]=https://anvil.example.com/ide/github/callback&public=true
```

Copy the updated link into your browser and follow the steps to create the GitHub App. Generate a new Client Secret, and note it down along with the Client ID. Also note the app URL of the “Public page” link of the app.

You’ll also need to generate a random webhook secret and add it to the GitHub App configuration. Note the webhook secret down too.

Finally, if you want Anvil to access repositories associated with a GitHub Organization, go to “Advanced” and click the “Make Public” button. You can then click “Install App” and select the accounts that you wish to grant access to.
