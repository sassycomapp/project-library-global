---
document: "Connecting to GitHub and Git Remotes"
title: "Connecting to GitHub and Git Remotes"
url: "/docs/workflows/version-control/git"
doc-id: git-_index
state: Live
date-created: 2026-09-08
---


# [Connecting to GitHub and Other Git Remotes](#connecting-to-github-and-other-git-remotes)

When collaborating in Anvil, you can [add collaborators](collaborators) to your app in order to work on the same codebase. Anvil also allows you to connect to an external (“remote”) Git repository, such as one provided by [GitHub](https://github.com). This allows you to collaborate with developers in different organisations, work on open source projects, or make use of external code review and CI/CD tools.

Anvil makes it easy to save your app’s code to GitHub or other Git remotes. Just save your app to GitHub, or clone an existing GitHub repository, then edit your app as normal. Anvil takes care of keeping local and remote repositories in sync: All your changes will automatically be pushed to the remote repository, and other developers’ changes will show up live in your app.

All Anvil accounts can use GitHub repositories for open source projects. If you want to use private repositories you’ll need a Business plan or higher.

## [Saving an app to a new GitHub repo](#saving-an-app-to-a-new-github-repo)

To connect your Anvil app to a GitHub repository, click the “Save app to GitHub” button, at the top right of the [Version History tab](/docs/version-control) in the Bottom Panel.

First, authorise Anvil for your GitHub account and/or organisations and choose where you want to create your repository.

Now, choose whether you want your repository to be private (only for you and chosen collaborators) or public (visible to everyone, like open source projects). For public repositories, you can choose from some popular open-source licences - if you’re not sure, the MIT licence is a good choice.

Finally, give your GitHub repository a name and click “OK” to create it.

## [Cloning a GitHub repo into a new app](#cloning-a-github-repo-into-a-new-app)

In order to clone a GitHub repository into an Anvil app go to the Anvil Start Page and choose “Clone from GitHub”, underneath the “Blank App” option.

Enter the URL of the Git repository you wish to clone and choose your preferred authentication method:

-   **Anonymous**: for read-only access to public repositories.
-   **GitHub Account**: for private repositories or a public ones that you’d like to edit.
-   **Username and password**: for non-GitHub remotes, like Gitlab or a private Git server.

Finally, click on “Clone App”.

## [Synchronising changes](#synchronising-changes)

Every time you change your app, Anvil will save that change to GitHub, and every time someone else changes the app on GitHub, that change will be reflected in your Anvil app.

Once you’ve set up a Git remote, whenever you edit a branch or create a tag, Anvil will push that change to your remote repository. If you’re using GitHub, GitHub will notify Anvil every time another developer edits a branch and Anvil will pull the changes into your local app. If you’re using a non-GitHub remote, you’ll have to do this manually by clicking the “Sync Git Remotes” button.

If a push or pull fails, you’ll see an error symbol indicating that the branch is now “out of sync”.

The most common cause for this is if someone else is modifying the branch at the same time as you, which can result in the branch moving in both the branch and the remote.

Check out the branch that has moved – you’ll get a pop-up dialog. The pop-up offers you a few options:

-   **Start a new branch** just with your changes: This is the best option if you’re not sure what to do.

-   **Discard your local changes**: Reset the local branch to where the remote one is.

-   **Discard the remote changes**: Force-push the remote branch to where the local one is.

-   **Merge changes**: This will merge your changes into the remote changes and push.

Alternatively, you can also choose to stay out of sync by simply closing the modal. If you do this, the changes won’t be synchronized with the remote repository.

## [Working with other Git remotes](#working-with-other-git-remotes)

Anvil supports other Git remotes, not just GitHub. To add one, click on the three dots next to the “Save app to GitHub” button in the Version Control tab and choose “Manage Git remotes” from the drop-down.

A pop-up will show up, click on “+ Add new Remote” and select “Add remote by URL…”. You can choose to add username + password authentication for your remote.
