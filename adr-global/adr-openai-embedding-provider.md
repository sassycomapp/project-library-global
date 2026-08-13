---
document: OpenAI Must Remain the Embedding Provider
doc-id: openai-must-remain-embedding-provider
state: Live
date-created: 2026-08-12T000000+0200
---
# OpenAI Must Remain the Embedding Provider

Date: 2026-08-12
Status: Accepted
Source: GBrain PostgreSQL migration project; confirmed during the GBrain audit

---

## Context

GBrain's embedding pipeline runs on OpenAI's `text-embedding-3-large` model. This is the model that converts stored content into the vectors semantic search depends on.

---

## Decision

**OpenAI must remain GBrain's embedding provider.** This applies regardless of any future change to which provider handles chat, reasoning, or subagent routing — those are separate, independent choices from embedding specifically.

---

## Rationale

1. **Anthropic cannot perform embeddings at all** — confirmed directly via `gbrain providers list`. Anthropic's `EMBED` column shows a structural gap (a dash), not a missing-key or misconfiguration state. This is not a preference between providers; it is the absence of a capability.
2. Switching embedding providers requires re-embedding the entire existing corpus — a real, non-trivial cost, not a simple config flip.
3. OpenAI's `text-embedding-3-large` is already confirmed working correctly, system-wide, verified during the GBrain audit (direct database query: 1084 of 1084 chunks embedded, zero missing).

---

## Consequences

- Any future GBrain schema-pack upgrade or provider-migration decision must explicitly preserve OpenAI as the embedding provider.
- The chat/reasoning model GBrain uses may still change independently of this decision — this ADR governs embedding only.
- No action is required to enforce this today; it documents an existing, already-correct configuration as a binding constraint against future drift.

---

*End of `openai-must-remain-embedding-provider` ADR*
