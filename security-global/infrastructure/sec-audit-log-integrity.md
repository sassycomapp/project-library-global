---
title: "sec-audit-log-integrity"
doc-id: "mb-fc351b71"
updated: "2026-10-23"
---
# Audit Log Integrity Across Systems

## Applicable Threat

This environment has multiple, separate audit/logging systems — the memory governor's own compliance ledger, Cupcake's Observability logging, GBrain's own history. None are cryptographically tamper-proof, an accepted risk. Treating any of them as authoritative proof of what happened, rather than a record for human review, is a real risk if that distinction is forgotten.

## Security Requirement

Every audit/logging system in this environment is treated consistently as evidence for human review, never as self-proving authorization — the same standard already explicitly decided for the compliance ledger.

## Approved Pattern

Use logs to inform a human decision, cross-referencing multiple independent sources where a real question exists (as was done this session, cross-checking the governor's own event log against a direct database query, rather than trusting either alone).

## Prohibited Pattern

Treating a log entry alone as sufficient proof an action was correctly authorized, without independent verification, especially for a high-consequence decision.

## Implementation Guidance

Apply the same "evidence, not authority" standard already decided for the compliance ledger uniformly across every logging system in this environment, not just the one it was originally decided for.

## Verification Requirements

For any real decision resting on log content, confirm at least one independent source corroborates it before treating it as settled fact.

## Authoritative Sources

This document is the authority.

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
