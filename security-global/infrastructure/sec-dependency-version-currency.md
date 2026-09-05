---
document: "Dependency and Tool Version Currency"
doc-id: sec-dependency-version-currency
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Dependency and Tool Version Currency

## Applicable Threat

Real, confirmed gap: GBrain is running version `0.46.1.0` while `0.46.32.0` is available — flagged repeatedly across this session's own work, never actually resolved. An outdated tool can carry known, already-fixed vulnerabilities or bugs the current version no longer has.

## Security Requirement

A known available upgrade for a security-relevant tool is tracked as a real, standing item until deliberately addressed or deliberately deferred with a stated reason — not silently repeated as a passing flag indefinitely.

## Approved Pattern

Recording the gap explicitly, as was done this session, as its own separate, real task — not folded into unrelated work and left unresolved by default.

## Prohibited Pattern

Noting a version gap in passing multiple times across a session without it ever becoming a real, tracked, actionable item.

## Implementation Guidance

The GBrain version gap flagged this session should become a genuine, standalone task — the same standard this whole document set exists to apply to security findings generally.

## Verification Requirements

Confirm every core tool in this environment (GBrain, Cupcake, GStack, Matt Pocock skills) has its current version checked against the latest available at reasonable intervals, with any gap tracked as a real item, not just mentioned.

## Authoritative Sources

- This session's own repeated, unresolved flag of the GBrain version gap

## Known Exceptions

None identified.

## Lessons Learned

Confirmed this session: flagging a gap multiple times without converting it into a tracked task means it stays open indefinitely by default.
