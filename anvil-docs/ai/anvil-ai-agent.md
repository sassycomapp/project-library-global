---
title: "anvil-ai-agent"
doc-id: "mb-53f8aa46"
updated: "2026-11-01"
---
# The Anvil AI Agent — What It Can Do and How MyBizz Uses It

What the AI agent inside the Anvil editor can and cannot do, how a change it makes reaches an app, and the rules MyBizz applies when using it. Verified against the live page `anvil.works/docs/ai` on 2026-10-31.

**Sources in this corpus:** [[[default:anvil-docs/ai/_index|AI Agents in Anvil]]](C:/dev/project-library-global/anvil-docs/ai/_index.md), [[[default:anvil-docs/ai/agent-chat-window|The Agent chat window]]](C:/dev/project-library-global/anvil-docs/ai/agent-chat-window.md), [[[default:anvil-docs/ai/connecting-your-account|Connecting Your Account]]](C:/dev/project-library-global/anvil-docs/ai/connecting-your-account.md), [[[default:anvil-docs/how-to/prompting-best-practices|Prompting best practices]]](C:/dev/project-library-global/anvil-docs/how-to/prompting-best-practices.md), [[[default:anvil-docs/data-tables/multiple-databases|Multiple databases]]](C:/dev/project-library-global/anvil-docs/data-tables/multiple-databases.md).

---

## What the agent is

The Anvil agent is an AI agent built into the Anvil editor. It reads an app's code, changes the files a request needs, checks its work, and explains what it did. It works inside one app, in the Anvil editor, and runs on the developer's own AI account: Claude (an Anthropic API key or a Claude Code token) or ChatGPT/Codex. It is available on every Anvil plan.

---

## What the agent can change

| Area | What it changes |
|---|---|
| Forms and client code | Forms, Components, client Modules |
| Server code | Server Modules |
| Styling | The app's theme and CSS |
| App configuration | Dependencies, services, and the Data Tables schema (tables, columns, column types) |

Its changes appear live in the Anvil editor and are kept in Version History.

## What the agent cannot do

- **Apply a schema change to the tables.** Anvil states that "any Data Tables schema changes must be applied manually in the Data Tables view."
- **Read or change the data** stored in the tables.
- **Read the app's Secrets** (for MyBizz apps, `encryption_key`).
- **Run git operations.** The only git action is the automatic commit it makes whenever it edits the app.

---

## How a schema change reaches the tables

1. The agent changes the app's database schema: the tables and columns the app declares.
2. The tables in the database no longer match that schema. Anvil checks this whenever the app is open in the editor and shows a prompt.
3. The developer clicks **Resolve**. Anvil's database schema window lists every difference between the schema and the database.
4. The developer checks each difference and applies it.

The agent therefore prepares a schema change, and only the developer can make the change real. Removing a column in the Resolve window deletes that column's data. Renaming a column by hand in the Data Tables view keeps its data, so MyBizz renames columns by hand, not through the agent.

---

## The chat window

- Opened from the editor's sidebar menu; it can sit in the sidebar, the bottom panel or an editor tab.
- `@` names a Form or Module so that the agent knows exactly where to work.
- `/` lists the agent's skills and commands; `/compact` shortens a long conversation.
- Images up to 10 MB can be attached (for MyBizz, the screen PNG at Step 29).
- A model and an effort level are chosen per prompt; higher effort gives better results and takes longer.
- **Reset all my Agents** stops every running agent session in the app; unsaved progress is lost.

---

## Prompting rules (Anvil's advice)

- Name exactly what to change: the Form, the Module, the table, the column.
- Describe the result wanted, not only what to add.
- Say what must stay the same.
- Ask for a plan first, and wait to approve it before any change is made.
- Break large tasks into small steps, and check each step in the running app before the next.
- Correct the agent with specifics, in the same conversation.
- Start a new conversation for each unrelated task; compact after a finished task or an approved plan.

---

## How MyBizz uses the agent

| Use | PDLF step | Rule |
|---|---|---|
| Building each form from its approved wireframe, screen HTML and screen PNG | Step 29 | One form per conversation; the agent is told not to touch other forms, server modules or the schema |
| Preparing schema changes from a project's `schema-migration-log.md` | Step 17 | One group of tables per conversation; the developer applies every change through **Resolve**; renames are done by hand |

Every agent prompt MyBizz uses states three things: exactly what to change, everything that must not change, and that the agent lists its plan and waits for confirmation. Because the agent commits automatically, its work is pulled to the local copy afterwards (Steps 30 and 33) before any other agent works on the app.

---

*End of file — anvil-ai-agent.md*
