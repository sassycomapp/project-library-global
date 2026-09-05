# Rule: No Unverified Dependency Installation

## Harness
opencode

## What to block
Any bash tool call whose command installs a new package or dependency
(e.g. `npm install`, `npm add`, `pip install`, `yarn add`, `cargo add`,
`go get`, `poetry add`), unless the developer has explicitly approved
that specific package in the current session.

## Decision
Block (deny). Do not allow the dependency to be introduced without
explicit developer approval.

## Message shown to the agent on block
"Do not install a new package or dependency without explicit developer
approval for that specific package. Package recommendations must be
proposed to the developer, not installed autonomously."

## Reason
AI-generated dependency recommendations can be incorrect, hallucinated,
or introduce supply-chain risk. A dependency must be independently
verified before it becomes part of the development environment or
application. See also the separate rule covering the lockfile writes
these commands typically produce.
