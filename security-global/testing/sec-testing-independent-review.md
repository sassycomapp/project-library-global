---
title: "sec-testing-independent-review"
doc-id: "mb-be081259"
updated: "2026-10-22"
---
# Independent Security Review

## Applicable Threat

The same agent that implemented a feature reviews its own security — carrying forward the same blind spots or assumptions that shaped the implementation in the first place, since a mistake in reasoning is unlikely to be caught by the same reasoning that produced it.

## Security Requirement

Security-relevant code is checked by genuinely separate reviewers — Matt Pocock's `code-review`, GStack's `/cso --diff` and Sentinel, each run in its own session — not solely by the session or agent that wrote it.

## Approved Pattern

The pattern of Matt Pocock's own `code-review` skill: isolated reviewers check the same work independently, so neither one's judgment influences the other's. PDLF applies it to security with `code-review`, `/cso --diff` and Sentinel at Step 37, each in a separate session (test SC-15).

## Prohibited Pattern

Treating the implementing agent's own stated confidence in its work as equivalent to independent review.

## Implementation Guidance

Each reviewer runs in a fresh session that did not write the change, and its findings are recorded in the ledger before the change is accepted.

## Verification Requirements

For security-relevant changes, confirm that `code-review`, `/cso --diff` and Sentinel each reviewed the change in a separate session, with their output saved as evidence, not just the implementer's own confidence.

## Authoritative Sources

- Matt Pocock's `code-review` skill — the parallel-isolated-reviewer pattern

## Known Exceptions

Low-risk changes, per Sentinel's own step-intensity table (Section 9), may not warrant this — the requirement scales with the same intensity already defined there.

## Lessons Learned

None yet. Populated as real findings occur.
