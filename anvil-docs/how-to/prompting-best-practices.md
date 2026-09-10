---
title: "Prompting best practices"
url: "/docs/how-to/prompting-best-practices"
doc-id: prompting-best-practices
state: Live
date-created: 2026-09-08
---


# [Prompting best practices](#prompting-best-practices)

How you write your prompts affects what the agent produces. These tips will help you get more consistent results.

## [Writing clear prompts](#writing-clear-prompts)

### Name the thing you’re working on

The agent understands your code, but vague references can leave it guessing about where or what you want to change. Use specific names that tell the agent exactly where to look and what to change. You can type `@` in the prompt box to mention a Form or Module by name and the prompt box will autocomplete it.

Instead of “Add a button that saves the record”, say “In the `CustomerEdit` Form, add a Save button that calls the `save_customer` function.” The second version leaves nothing for the agent to misinterpret or guess.

### Describe what you want to happen, not just what to add

Telling the agent what you want to achieve, not just what to create, helps it make better decisions. A prompt like “Add a dropdown” tells the agent nothing about what it’s for or what should happen when someone selects one. Instead, try “Add a dropdown to the `OrderForm` Form that lets users filter the order list by status. The status values come from the `status` column in the Orders table. When the user selects a value, reload the table showing only matching rows”.

### Say what should stay the same

The agent may adjust things you weren’t expecting it to touch. If you want targeted changes, tell it what to leave alone. For example:

“Add validation to the `name` field in `CustomerEdit`. Don’t change any of the existing event handlers.”

“Restyle the `UserList` Form to match the card layout in `ProductList`. Don’t change the styling of any other components.”

This is especially useful any time you want a specific, targeted change and don’t want the agent touching anything else in your app.

### Give structure and context

If a change belongs in a specific part of a Form, or should follow a pattern already in your app, add that to your prompt. The agent can follow existing conventions, but only if you point them out.

“Add the filter controls to the top of `DataPanel`, above the Data Grid. Follow the same layout as the search bar in `ProductList`.”

Pointing to an example in your own app is often more effective than describing a layout from scratch. The agent will match the structure, style, and code patterns of whatever you reference.

## [Work iteratively](#work-iteratively)

### Break complex tasks into steps

A single large prompt asking for a full feature, database logic, server functions, UI, and event handlers, gives the agent a lot to get right at once. Smaller steps give you a chance to check each piece before the next one builds on it.

For larger tasks, you can also ask the agent to outline its approach before making any changes:

“Before making any changes, describe what you plan to do and wait for my confirmation before implementing.”

This lets you catch any misunderstandings early, before the agent has touched your code.

For example, to build a user management screen:

1.  “Create a server function `list_users` that returns all rows from the Users table, sorted by `created_at` descending.”
2.  “Add a `UserList` Form that calls `list_users` on load and displays the results in a Data Grid.”
3.  “Add a Delete button to each row that calls a `delete_user` server function and refreshes the table.”

Each step is small enough to verify before moving on, and easy to correct if it doesn’t look right.

### Correct the agent with specifics

When something isn’t right, describe exactly what needs to change rather than re-describing the whole task. “That’s not quite right, try again” gives the agent very little to work with. “The save button is inside the card. Move it below the card, aligned to the right edge” tells the agent exactly what to fix.

Follow up in the same conversation rather than starting over. The agent retains the context of what you’ve been building, so a targeted correction is usually faster than a fresh prompt.

### Test what the agent produces

AI-generated code can look correct but contain subtle mistakes. Run your app after each change and verify the behaviour. If something doesn’t work as expected, describe the issue and ask the agent to help debug it.

## [Manage your conversation](#manage-your-conversation)

### Start a new conversation for unrelated tasks

Conversation history helps the agent stay consistent within a task, but too much history from a different task can introduce confusion. When you move to a new, unrelated feature or area of your app, starting a fresh conversation gives the agent a clean slate and avoids it carrying over assumptions from earlier work.

### Manage the context window

The context window is how much conversation history the agent can hold at once. As a conversation grows, older messages start to fall outside the window and the agent can no longer see or reference them. You can check how full it is using the [Context window](/docs/ai/agent-chat-window) in the prompt box.

When the context window is full, the agent compacts automatically. You can also compact manually using `/compact` in the prompt box. Good times to compact:

-   After the agent has finished a task and you want to continue in the same conversation
-   After the agent has laid out a plan you’re happy with, before it starts implementing
-   When the context window indicator is getting high
