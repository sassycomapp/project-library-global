---
title: "Using Anvil in a Local IDE"
url: "/docs/using-another-ide"
doc-id: using-another-ide-_index
state: Live
date-created: 2026-09-08
---

# [Using Anvil from a Local IDE](#using-anvil-from-a-local-ide)

**The Anvil CLI is currently in beta** while we continue to make improvements.

The Anvil CLI allows you to work in your preferred IDE and sync your changes instantly to the Anvil Editor.

Follow the quickstart guide to get started:

[Get Started with the Anvil CLI](using-another-ide/quickstart)

## [Installing the Anvil CLI](#installing-the-anvil-cli)

To use the Anvil CLI, you first need to install it:

**macOS/Linux**

```bash
curl -fsSL https://anvil.works/install-cli.sh | sh
```

**Windows PowerShell**

```bash
irm https://anvil.works/install-cli.ps1 | iex
```

**Windows CMD**

```bash
curl -fsSL https://anvil.works/install-cli.cmd -o install.cmd && install.cmd && del install.cmd
```

**Using npm**

```bash
npm install -g @anvil-works/anvil-cli@latest
```

If you run into a permissions error when installing with `npm`, run the command with `sudo` instead: `sudo npm install -g @anvil-works/anvil-cli@latest`

### Configuring the CLI

After installing the Anvil CLI, we recommend you first configure the CLI by running:

```bash
anvil configure
```

This will prompt you with the following configuration options:

1.  **Default Anvil server**: Set the default server to use when running `anvil login` and `anvil watch`. Press enter to set the default server as [https://anvil.works](https://anvil.works). Enterprise customers will need to enter the URL for their Enterprise installation.

2.  **Preferred Editor**: Set your preferred local IDE to use when running [`anvil checkout --open`](/docs/using-another-ide/commands#checkout). If you have any code editor command line tools installed, these will show up here.

3.  **Enable verbose logging**: Set this to True to see detailed output in the terminal.

The CLI will then ask you to log in. You will then be directed to the browser to log into Anvil and grant the Anvil CLI access to your account.

Your configuration options will be saved in your [config file](#anvil-config-file).

## [Logging into Anvil](#logging-into-anvil)

In order to use the Anvil CLI, you’ll need to log into your Anvil account. You can do this by running `anvil login`. You can log out of your account by running `anvil logout`.

## [Connecting to your Anvil app](#connecting-to-your-anvil-app)

If you already have an [Anvil app cloned locally](/docs/version-control/git/direct-checkout), you can skip this step and directly run [`anvil watch`](#syncing-changes) in your local app’s directory.

After logging in, you’ll need to checkout the Anvil app you want to work on locally. There are two ways to do this.

### Choose your app from the terminal

Run the following command:

```bash
anvil checkout
```

This will present you with a list of your apps. Choose the app you’d like to checkout, and the CLI will create a directory with the same name as your app with all your app files inside.

### Provide the app URL

You can also `anvil checkout` with your app’s URL and the name of the git directory that will be created. For example:

```bash
anvil checkout https://anvil.works/build/apps/W36XUTXGNPDK6VEA my-app
cd my-app
```

## [Syncing changes](#syncing-changes)

In order to sync changes between your local app and the Anvil Editor, you’ll need to run `anvil watch` inside your app’s local directory.

```bash
cd my-app
anvil watch
```

The Anvil CLI will auto-detect which Anvil app to sync to.

If this fails, you can specify the app ID explicitly. For example:

```bash
anvil watch -A W36XUTXGNPDK6VEA
```

## [Syncing to Enterprise apps](#syncing-to-enterprise-apps)

When [running `anvil configure`](#configuring-the-cli), you can set your Enterprise installation as your default server URL. This updates your [config file](#anvil-config-file) to set `anvilUrl` as your Enterprise URL.

You can also directly update the `anvilUrl` value in your config file:

```bash
anvil config set anvilUrl https://anvil.mycompany.com
```

Setting `anvilUrl` means that CLI commands such as `login` and `watch` will use that server by default.

Alternatively, you can manually specify the server URL to use each time you run `login` and `watch`.

```bash
anvil login anvil.mycompany.com
```

```bash
anvil watch --url anvil.mycompany.com
```

## [Multiple accounts](#multiple-accounts)

If you are logged in to more than one Anvil account or more than one Anvil installation, the Anvil CLI will usually infer the right installation and account from your setup. If there is any ambiguity, it will usually prompt you.

However, you can use `--url` and `--user` with the `watch` and `logout` commands to manually specify which installation and account to use.

For example

```bash
anvil watch --url anvil.company.com --user user@example.com
anvil logout --url anvil.company.com --user user@example.com
```

## [Anvil config file](#anvil-config-file)

The Anvil CLI is configured using a `config.json` file stored locally on your machine.

File locations:

-   macOS: `~/Library/Preferences/anvil-cli/config.json`
-   Linux: `~/.config/anvil-cli/config.json`
-   Windows: `%APPDATA%\anvil-cli\Config\config.json`

The config file stores:

-   Authentication tokens (one per logged-in account)
-   The default Anvil server URL (`anvilUrl`)
-   CLI settings such as `devMode`, `verbose` and `preferredEditor`

You can view your current configuration by running `anvil config list`.

You can also set values directly from the command line:

```bash
anvil config set anvilUrl https://anvil.mycompany.com
```

For more details, [see the npm page](https://www.npmjs.com/package/@anvil-works/anvil-cli).
