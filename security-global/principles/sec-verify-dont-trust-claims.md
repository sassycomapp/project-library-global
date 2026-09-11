---
document: "Principle — Verify, Don't Trust Claims"
doc-id: sec-verify-dont-trust-claims
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Verify, Don't Trust Claims

## Statement

A claim that something was checked, secured, or verified is not itself proof that it was. Verification requires a real, independent, reproducible action — not an assertion, however confidently stated.

## Real Precedent in This Project

- the retired `the retired structural-compliance-enforcement-architecture-v3.md`'s own threat model names this directly: an agent can fabricate or assert compliance without it being true.
- `[[sec-ai-agent-introduced-vulnerabilities]]` — this exact failure mode named as the central reason Sentinel exists.
- This session's own recurring practice: every real claim (a schema change, a successful push, a service being up) was checked directly — `git ls-remote`, `ss -tlnp`, a real query — not accepted from a success message alone.

## Why This Matters

An AI agent, or any automated process, can produce a plausible, confident-sounding claim that is simply wrong, without any intent to deceive. Treating the claim as fact rather than verifying it directly is how a real problem goes unnoticed.

## Application

For any consequential claim ("this is fixed," "this is secure," "this was checked"), ask: what independent action would actually confirm this, and has that action been taken? If not, the claim is unverified, not false — but also not yet trustworthy.

## Known Exceptions

None — this applies to claims made by this project's own AI agents and by external sources equally.
