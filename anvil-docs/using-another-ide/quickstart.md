---
title: "Quickstart"
url: "/docs/using-another-ide/quickstart"
---


# [Quickstart: Build an app locally with the Anvil CLI](#quickstart-build-an-app-locally-with-the-anvil-cli)

**The Anvil CLI is currently in beta** while we continue to make improvements.

You don’t need to use the Anvil Editor to build Anvil apps. [The Anvil CLI](/docs/using-another-ide) lets you write code locally in your preferred IDE and see the changes instantly in the Anvil Editor.

Follow this quickstart to learn how to set up the Anvil CLI and get started editing apps locally.

In order to follow this quickstart guide, you’ll need to have an Anvil app in your account that you want to edit locally. If you don’t have an Anvil app to use, you can clone this example app: [https://anvil.works/build#clone:IMO5DXF6HDBJA6YB=SN4DTPLWFG5UYM3IP24YKUMF](https://anvil.works/build#clone:IMO5DXF6HDBJA6YB=SN4DTPLWFG5UYM3IP24YKUMF).

## [Install the Anvil CLI](#install-the-anvil-cli)

Open a terminal and install the Anvil CLI with one of the following commands:

**macOS/Linux**

```bash
curl -fsSL https://anvil.works/install-cli.sh | sh
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

## [Configure the CLI](#configure-the-cli)

After the Anvil CLI has finished installing, run `anvil configure`. This will prompt you with some options to configure your Anvil CLI setup.

1.  The Anvil CLI will first check if the anvil-cli is up to date. If the package is out of date, we recommend running `anvil update` before continuing with the configuration.

2.  Next, you’ll be asked to set the default Anvil server. Press enter to set the default Anvil server as [https://anvil.works](https://anvil.works). This means that you’ll be connecting to an Anvil app running on Anvil’s servers. If you are an Enterprise customer, [read here](/docs/using-another-ide#syncing-to-enterprise-apps) to find out how to set the default server to your Enterprise installation.

3.  You’ll be asked for your preferred editor. Choose None, this can be set later by running `anvil configure` again or from your [config file](/docs/using-another-ide#anvil-config-file).

4.  The CLI will ask if you want to enable verbose logging. Type ‘N’ to set this to False. This can be changed by running `anvil configure` again or by updating your [config file](/docs/using-another-ide#anvil-config-file)

5.  You’ll then be prompted to log into Anvil. Type ‘Y’ then press enter to open up your browser and grant access to the Anvil CLI. In the browser window, click “Grant Access”.

## [Checkout your Anvil app](#checkout-your-anvil-app)

Now that you’ve configured the CLI and logged into Anvil, you’ll need to checkout your Anvil app locally.

In the directory where you’d like the app folder to live, run the following command:

```bash
anvil checkout
```

This will present you with a list of your Anvil apps. Choose the one you’d like to edit locally.

The Anvil CLI will then create a directory with all your app files.

## [Sync your local app to Anvil](#sync-your-local-app-to-anvil)

We can now sync changes between the local app and the app running on Anvil.

Next, navigate into this newly created directory and run `anvil watch`:

```python
cd Anvil_CLI_Example_App
anvil watch
```

The Anvil CLI will now sync changes between your local Anvil app and the Anvil Editor.

## [Make a change locally](#make-a-change-locally)

Open your local Anvil app in your preferred code editor, such as VSCode. Open one of the code files in your app and edit the code.

If you are using the sample app, you can open up `ServerModule1` which can be found in the `server_code` directory. Edit the `say_hello` function so that it prints out the `name` argument:

```python
@anvil.server.call
def say_hello(name):
    print(name)
```

Now, open the same file in the Anvil Editor. You should see the changes to the function appear instantly.

Try making an edit from the Anvil Editor. If you are using the sample app, switch to Form1 and modify the `say_hello_button_click` to clear the TextBox after the server function is called:

```python
    @handle("say_hello_button", "click")
    def say_hello_button_click(self, **event_args):
        """This method is called when the component is clicked."""
        anvil.server.call('say_hello', self.name_box.text)
        self.name_box.text = ""
```

Back in your local code editor, open up Form1 to see the change has appeared.

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [building apps from your preferred IDE](/docs/using-another-ide).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
