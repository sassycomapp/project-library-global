---
document: "Independent Security Review"
doc-id: sec-testing-independent-review
state: Live
date-created: 2026-08-27
category: testing
---
# Independent Security Review

## Applicable Threat

The same agent that implemented a feature reviews its own security — carrying forward the same blind spots or assumptions that shaped the implementation in the first place, since a mistake in reasoning is unlikely to be caught by the same reasoning that produced it.

## Security Requirement

Security-relevant code is checked by a genuinely separate reviewer — a different AI session, GStack's own `/review` security specialist, or `/cso`'s independent audit — not solely by the same session or agent that wrote it.

## Approved Pattern

The pattern already identified in Matt Pocock's own `code-review` skill: two isolated reviewers checking the same work independently, so neither one's judgment influences the other's — the same principle, applied here to security specifically via `/review`'s security specialist (already part of PDLF Step 37) or `/cso`'s own periodic audit.

## Prohibited Pattern

Treating the implementing agent's own stated confidence in its work as equivalent to independent review.

## Implementation Guidance

`/review`'s security specialist, already present at PDLF Step 37 per `sentinel-security-system-plan.md` Section 3, is confirmed under-used — actually invoking it for security-relevant changes is the concrete action this requirement calls for, not new infrastructure.

## Verification Requirements

For security-relevant changes, confirm a genuinely separate review (a different session, `/review`'s security specialist, or `/cso`) actually occurred, not just the implementer's own confidence.

## Authoritative Sources

- `sentinel-security-system-plan.md` Section 3 — `/review`'s security specialist, confirmed under-used
- Matt Pocock's `code-review` skill — the parallel-isolated-reviewer pattern

## Known Exceptions

Low-risk changes, per Sentinel's own step-intensity table (Section 9), may not warrant this — the requirement scales with the same intensity already defined there.

## Lessons Learned

None yet. Populated as real findings occur.
