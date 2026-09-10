---
title: "Commands"
url: "/docs/using-another-ide/commands"
doc-id: commands
state: Live
date-created: 2026-09-08
---


# [Anvil CLI commands](#anvil-cli-commands)

**The Anvil CLI is currently in beta** while we continue to make improvements.

Here you can find a list of the most useful Anvil CLI commands.

For the full list of commands and flags, run

```bash
anvil --help
anvil <command> --help
```

## [`configure`](#configure)

Set up your default Anvil server, editor preferences, and login.

```bash
anvil configure
```

Use this when:

-   you are setting up the CLI for the first time
-   you want to run the guided setup again
-   you want the guided setup instead of configuring pieces manually

## [`checkout`](#checkout)

Checkout an Anvil app locally using the interactive picker, the app’s URL in Anvil, or the app ID.

Alias: `anvil co`

```bash
anvil checkout [input] [directory]
anvil co [input] [directory]
```

Key options:

-   `-O, --open`: open the app folder after checkout. If a preferredEditor is set, the app folder will open in that editor.
-   `-b, --branch <BRANCH>`: check out a specific branch
-   `-Q, --query <QUERY>`: prefill the interactive search

Examples:

```bash
anvil checkout https://anvil.works/build/apps/W36XUTXGNPDK6VEA my-app
anvil checkout W36XUTXGNPDK6VEA my-app --url anvil.works
anvil co -Q "dashboard"
```

Use this when:

-   you want a fresh local copy of an app
-   you want interactive app selection
-   you want to start from an app URL copied from Anvil

If you need to work across multiple accounts or Anvil installations, see [Multiple accounts](../using-another-ide#multiple-accounts).

## [`watch`](#watch)

Keep your local app folder synced with Anvil while you work.

```bash
anvil watch [path]
```

Key options:

-   `-A, --appid <APP_ID>`: specify the app directly
-   `-s, --staged-only`: sync only staged files
-   `-a, --auto`: automatically handle some branch and sync transitions
-   `-O, --open`: open the watched path in your preferred editor

Use this when:

-   you want local edits to sync to Anvil
-   you want compatible Anvil changes to sync back to your local files
-   you are doing normal day-to-day local development

## [`validate`](#validate)

Check that the specified `.yaml` file is formatted correctly and thus valid.

```bash
anvil validate <file>
```

You’ll need to specify the path to the file or run the command from the relevant directory and provide the file name.

If the file is valid, the command prints a success message and exits successfully. If the file is invalid, it prints the fields that need attention and exits with an error.

Supported files:

-   `anvil.yaml`
-   `.yaml` files under `client_code/`, including `client_code/**/form_template.yaml`

Key options:

-   `--json`: output from the command is structured as JSON. Useful for feeding the output to an agent

Examples:

```bash
anvil validate anvil.yaml
anvil validate client_code/Form1/form_template.yaml
anvil validate client_code/Form1.yaml
```

## [Other useful commands](#other-useful-commands)

### Login and account fixes

-   `anvil login` to log in again, or to a specific installation such as `anvil login anvil.company.com`
-   `anvil logout` if the CLI is using the wrong account

### Config commands

-   `anvil config list` to check which server URL and CLI settings are currently in effect
-   `anvil config set <key> <value>` to update a config value directly
-   `anvil config get <key>` to inspect one config value directly
-   `anvil config reset` to reset CLI configuration back to its defaults and clear saved logins

### Troubleshooting and maintenance

-   `anvil version` when troubleshooting
-   `anvil update` if the CLI tells you a newer version is available
-   `anvil help <command>` or `anvil <command> --help` for full command details
