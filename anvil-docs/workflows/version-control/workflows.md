---
document: "Workflows"
title: "Workflows"
url: "/docs/workflows/version-control/workflows"
doc-id: workflows
state: Live
date-created: 2026-09-08
---


# [Workflows for Collaborating on Anvil Apps](#workflows-for-collaborating-on-anvil-apps)

If you’re working in a team, it’s a good idea to adopt a standard workflow so you can collaborate smoothly. Below is a series of suggested workflows suitable for small teams and large enterprises alike. There are a lot of different ways to work with Git, but these are recommended approaches. The workflows are ordered from the simplest to the most powerful, but we recommend choosing the simplest approach that works for your use case.

[How To: Collaborate as a team on Anvil](/docs/how-to/collaborate-in-anvil)

## [Table of contents](#table-of-contents)

### 1. [Simple Multi-Dev](#simple-multi-dev)

A simple pattern for working in a small team on one Anvil app.

### 2. [Dev, Staging and Production](#dev-staging-and-production)

Use separate deployment environments and databases to stay out of each others’ way and test changes before they’re visible to everyone.

### 3. [Separate Production App](#separate-production-app)

Don’t want everyone having access to your production data? Create a separate app and sync the code via GitHub.

### 4. [Every Developer Has Their Own App](#every-developer-has-their-own-app)

Follow existing corporate workflows by giving every developer their own checkout.

---

## [Simple Multi-Dev](#simple-multi-dev)

In this workflow, everyone [collaborates](collaborators) on the same app, and the `master` branch is published. Developers make changes on private branches, and merge those changes into master to deploy them.

#### Publish the `master` branch

Publish the `master` branch of your repository as the main URL for your app. Everything that gets merged into `master` will be published to your users. (This is called “continuous deployment”; with Anvil it comes built-in.)

#### Always edit on a branch

Invite all your teammates to [collaborate](collaborators) on the app. Whenever you or any any developer edits the app, you should first create a new branch. Make your changes on that branch, and test them there.

If you’ve been working on your branch for a long time, and you want to pick up changes from `master` in the meantime, go ahead and merge from `master` into your branch. Just don’t merge your branch into `master` until it’s ready, because that publishes the changes!

#### Merge when you’re done

When your changes are working and it’s time to make them public, merge your changes into `master`. Because that’s the branch you’ve deployed, as soon as you merge your changes will be live.

#### If something goes wrong, roll back

If your change causes problems and you want to undo them, no problem! Just switch your **Editing branch** to `master`, then right click on an older, working commit and select **Reset ‘master’ branch to here**. You’ve moved the `master` branch to point at an older commit, and users are now seeing the older working version of your app!

---

## [Dev, Staging and Production](#dev-staging-and-production)

This workflow extends the [Simple Multi-Dev](#simple-multi-dev) workflow, by separating development from production databases to avoid messing with real user data, and adding an extra testing step before you deploy code to everyone.

#### Use separate databases for development

To avoid affecting your production data while testing, you can [create a separate database](/docs/data-tables/multiple-databases) for development. If you make changes that alter the schema of that database – for example by adding or removing columns or tables – you should make those changes to the development database and then [migrate](../../data-tables/multiple-databases#migrating-databases) the production database when you deploy the new code.

Smaller teams might want to share a single development database, but on larger teams each developer might want their own database to avoid stepping on each other’s toes.

#### Create a staging environment

A staging environment is a way to test your changes after you merge them but before sending them to the production environment. To create a staging environment:

1.  Create a new branch, called `production`. You will make sure that it always points to a well-tested version of your app that you want your users to see.

2.  Configure the [deployment environment](/docs/deployment) for your main URL (eg `my-app.com`) to serve the `production` branch. This means that any public users of your app get a well-tested version of the app.

3.  Create a new deployment environment, with a URL such as `my-app-staging.anvil.app`, and point it at the `master` branch.

Now, every change that gets merged into `master` is instantly available at `my-app-staging.anvil.app` so you and your team can check that it’s still working. When you’re confident that this version is good, and you want to release it to your users, reset the `production` branch to point at your newly merged commit (and migrate the production database if required).

---

## [Separate Production App](#separate-production-app)

In order to protect your production deployment, data and secrets from interference or accidental changes, you can create a separate Anvil app just for your production environment. Developers will continue to work on the development app, and the production app will be used only for deployment, using [GitHub](git) to sync approved changes from development to production.

#### Set up the development app

Create an app for development as described above:

1.  Invite everyone as a [collaborator](collaborators), and make each change on a private branch. Developers can share development data or create their own databases for testing. You might also want to publish a [staging environment](#create-a-staging-environment).

2.  Connect this app to a private [GitHub repository](git), and use [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) to protect the `master` branch. This prevents individual developers from altering the `master` branch directly: they must instead submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests).

You can use GitHub to configure policies for who can merge a pull request – for example, you can require code review and approval from a designated reviewer.

#### Deploy with the production app

Now create the app that will hold your production data. Clone your repository into a new Anvil app, and deploy the `master` branch as your main URL.

Collaborators on the development app cannot edit this deployment environment, view production secrets, or see the data in your production app’s database. The only way to deploy code into this environment is via GitHub, which means getting a pull request approved. When a pull request is merged on GitHub, the `master` branch will update on both the development and production apps, and this will cause the new code to be deployed in production.

GitHub’s branch protection prevents a single accident (or malicious developer) from altering `master` without review, and because access to the production app is limited, individual developers cannot see or edit production data.

#### Set up production-only secrets

If your app uses App Secrets, you need to configure values for your secrets in this app. These values will not be accessible to the development app, which means ordinary developers will not have access to them.

First, create a new branch – we’re about to save new encrypted secrets into our source code, but `master` is now a protected branch, so we can’t alter it directly! Open the [Secrets Service configuration](../security/encrypting-secret-data) and set the values for each secret. Now create a pull request on GitHub to merge these new values into `master`.

To learn more about how App Secrets work with multiple checkouts, read [App Secrets and Multiple Checkouts](git/secrets-across-repos).

---

## [Every Developer Has Their Own App](#every-developer-has-their-own-app)

It’s possible to take the [Separate Production App](#separate-production-app) one step further: The app’s source code lives in a central GitHub repository, and each developer clones this repository into a private app in their account. Anvil automatically synchronises changes between all of these repositories, but each developer has their own values for their secrets, and their own private database. To make a change, a developer creates a branch, makes the change, and then opens a pull request on GitHub. Only when a pull request is approved do these changes reach the `master` branch and get deployed to production (or staging).

This approach can be a good fit for enterprises that have already standardised on a GitHub-based workflow. If you already have procedures, authentication, auditing, and third-party integrations via GitHub, you can re-use your investment with your Anvil applications just as for any other development framework.
