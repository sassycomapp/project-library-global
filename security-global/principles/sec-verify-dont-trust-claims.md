---
title: "sec-verify-dont-trust-claims"
doc-id: "mb-0db0d898"
updated: "2026-10-23"
---
# Principle — Verify, Don't Trust Claims

## Statement

A claim that something was checked, secured, or verified is not itself proof that it was. Verification requires a real, independent, reproducible action — not an assertion, however confidently stated.

## Real Precedent in This Project

- An agent can fabricate or assert compliance without it being true.
- `[[sec-ai-agent-introduced-vulnerabilities]]` — this exact failure mode named as the central reason Sentinel exists.
- This session's own recurring practice: every real claim (a schema change, a successful push, a service being up) was checked directly — `git ls-remote`, `ss -tlnp`, a real query — not accepted from a success message alone.

## Why This Matters

An AI agent, or any automated process, can produce a plausible, confident-sounding claim that is simply wrong, without any intent to deceive. Treating the claim as fact rather than verifying it directly is how a real problem goes unnoticed.

## Application

For any consequential claim ("this is fixed," "this is secure," "this was checked"), ask: what independent action would actually confirm this, and has that action been taken? If not, the claim is unverified, not false — but also not yet trustworthy.

## Known Exceptions

None — this applies to claims made by this project's own AI agents and by external sources equally.
