---
document: "Connecting Your Account"
title: "Connecting Your Account"
url: "/docs/ai/connecting-your-account"
doc-id: connecting-your-account
state: Live
date-created: 2026-09-08
---


# [Connecting Your Account](#connecting-your-account)

To use AI agents in Anvil, you need to connect your account to an AI provider. When you open the agent chat window for the first time, you’ll be prompted to choose a provider.

Anvil supports the following providers:

-   [ChatGPT/Codex](#chatgptcodex)
-   [Claude](#claude)
-   [Custom Model Provider](#custom-model-provider) (Enterprise only)

## [ChatGPT/Codex](#chatgptcodex)

Click **ChatGPT/Codex** in the agent chat window.

There are two ways to connect your ChatGPT/Codex account:

1.  [Log in with ChatGPT](#log-in-with-chatgpt)
2.  [Log in with an API key](#log-in-with-an-api-key)

### Log in with ChatGPT

A one-time login code will be displayed in the chat window, and a link to sign in at [https://auth.openai.com/codex/device](https://auth.openai.com/codex/device).

Do not share your login code with anyone else.

Copy the code and open the link. Log in or choose an account to open the **Sign in to Codex with ChatGPT** confirmation window. When prompted, paste the code and click **Continue**.

Once connected, return to the Anvil Editor and click **Continue to conversation**.

#### Troubleshooting

-   Make sure you are already logged into your OpenAI account before opening the link. If you are not logged in, the option to enter the code may not appear.
-   If you still do not see the option to enter the code, go to [ChatGPT Settings](https://chatgpt.com/#settings) and under [Security and login](https://chatgpt.com/#settings/Security), toggle on “Enable device code authorisation for Codex”. Then, reopen the link from Anvil.

### Log in with an API key

Generate an API key from the [OpenAI dashboard](https://platform.openai.com/api-keys). In the dialog that appears, paste your API key and click **Log in**.

## [Claude](#claude)

Click **Claude** in the agent chat window.

There are two ways to connect your Claude account:

1.  [Anthropic API key](#anthropic-api-key)
2.  [Claude Code token](#claude-code-token)

### Anthropic API key

Generate an API key from the [Anthropic Console](https://platform.claude.com/). In the dialog that appears, paste your API key and click **Log in**.

### Claude Code token

With [Claude Code](https://claude.ai/code) installed on your machine, run the following command in your terminal:

```
claude setup-token
```

Copy the generated OAuth token, paste it into the dialog, and click **Log in**.

## [Custom Model Provider](#custom-model-provider)

Custom Model Provider is available on [Anvil Enterprise](/enterprise). Click **Custom Model Provider** in the agent chat window to get in touch and discuss your requirements.

## [Disconnecting your AI account](#disconnecting-your-ai-account)

To disconnect an AI provider, open your account settings by clicking **Manage agent authentication** from the menu at the top of the Chats panel or from the menu next to the **Move** button in the open conversation. Under **AI Connections**, click **Remove connection** next to the provider you want to disconnect.
