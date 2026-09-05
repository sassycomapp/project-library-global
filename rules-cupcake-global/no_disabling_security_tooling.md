# Rule: No Disabling Security Tooling

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) targeting a
known security-tooling configuration file — dependency audit config
(e.g. `.snyk`, `audit-ci.json`), static-analysis config (e.g.
`.semgrepignore`, SAST tool config files), secret-scanning config (e.g.
`.gitleaks.toml`, `.secretsignore`), or a pre-commit hook configuration
file (e.g. `.pre-commit-config.yaml`) — unless the developer has
explicitly approved that specific change in the current session.

## Decision
Block (deny). Do not allow the change to proceed without explicit
approval.

## Message shown to the agent on block
"Security tooling configuration is protected. Do not disable, weaken, or
reconfigure security scanning, dependency auditing, static analysis, or
pre-commit hooks without explicit developer approval. Address the
underlying issue instead."

## Reason
Security tooling provides an independent control over the agent's
output. Allowing the agent to weaken that control would permit it to
remove the evidence of a problem rather than correct the problem itself.
This rule covers the specific, known configuration files where that
control is defined — it cannot detect a change made elsewhere for the
purpose of weakening a finding indirectly.
