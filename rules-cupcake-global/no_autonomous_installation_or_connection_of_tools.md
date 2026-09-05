# Rule: No Autonomous Installation or Connection of Tools

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
configuration file where a tool, MCP server, extension, or plugin is
registered or enabled — `opencode.json`'s `mcp` section, a global or
project skill-registration file, or an equivalent — unless the
developer has explicitly approved that specific tool or connection in
the current session.

## Decision
Block (deny). Do not allow the tool or service change to proceed
without explicit approval.

## Message shown to the agent on block
"New tools, MCP servers, extensions, or plugins may not be registered or
enabled autonomously. Stop and obtain explicit developer approval
first."

## Reason
Every new tool or external connection can introduce additional
permissions, instruction sources, supply-chain exposure, and data
access. Such connections must remain under explicit developer control.
