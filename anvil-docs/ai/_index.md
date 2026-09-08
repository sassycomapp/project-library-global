---
title: "AI Agents in Anvil"
url: "/docs/ai"
---


# [AI Agents in Anvil](#ai-agents-in-anvil)

AI agents in Anvil let you build and edit your apps by describing what you want in the chat. The agent reads your code, makes the right changes across your files, and explains what it did. Everything is written in Python you can read, understand, and edit yourself.

AI agents in Anvil connect to your own Codex or Claude account. If you don’t have an AI subscription, Codex is the best place to start and you can use it for free with a ChatGPT account.

AI agents are available on all Anvil plans. See [Connecting your account](/docs/ai/connecting-your-account) to get set up.

## [How the agent works](#how-the-agent-works)

When you send a prompt, the agent reads your code, edits the relevant files, and checks its work before finishing. Changes are synced live to the Anvil Editor as they happen. You can review what changed at any time using [Version History](/docs/workflows/version-control/version-control-anvil).

The agent can access:

-   **Forms and client code**: create and edit [Forms](/docs/client/forms), [Components](/docs/components), and [Modules](/docs/client/client-code/modules)
-   **Server code**: write Python logic in [Server Modules](/docs/server/server-modules)
-   **Styling**: edit your app [theme](/docs/client/customisation/colour-schemes) and [CSS](/docs/client/customisation/using-css)
-   **App configuration**: manage [dependencies](/docs/deployment/dependencies), [services](/docs/integrations), and [Data Tables](/docs/data-tables) schema

The agent does not have access to your app’s Secrets, and cannot perform git operations aside from the automatic commits it makes when editing your app. Any Data Tables schema changes must be applied manually in the [Data Tables](/docs/data-tables) view. The agent cannot edit the data stored in your Data Tables.

## [](#connecting-your-account)[Connecting your account](/docs/ai/connecting-your-account)

Connect your Codex or Claude account to your Anvil account to get started.

## [](#the-agent-chat-window)[The Agent chat window](/docs/ai/agent-chat-window)

Learn about the agent chat interface and how to interact with the agent.

For tips on writing effective prompts, see [Prompting best practices](/docs/how-to/prompting-best-practices).
