---
document: "Requirement — Architecture Review"
doc-id: sec-requirements-architecture-review
state: Live
date-created: 2026-08-27
category: requirements
---
# Requirement — Architecture Review

Maps to Sentinel's own step-intensity table, Step 34 — Very High scrutiny: "Where are the trust boundaries?"

## Applicable Threat

An architecture is locked (per PDLF's own gate discipline) without its trust boundaries having been explicitly identified, leaving security review at later steps with nothing concrete to check against.

## Security Requirement

Before architecture is locked, all of the following are explicitly documented:

1. Every point where data crosses from one trust level to another (client to server, this application to an external service, one role's data to another's) is named explicitly.
2. For each named boundary, which document in this library governs it is identified — or, if none exists yet, that gap is flagged for a new document.
3. Responsibility for each boundary is assigned per `sec-explicit-responsibility-assignment.md` — platform, or application code, never left implicit.

## Approved Pattern

A real, explicit list of trust boundaries produced as part of the architecture step's own deliverable, not reconstructed after the fact during code review.

## Prohibited Pattern

Treating "no trust boundaries were mentioned" as equivalent to "there are none" — every real application has boundaries; an architecture that names none has not actually examined this.

## Implementation Guidance

Cross-reference every named boundary against this library's existing documents before assuming a new one is needed — most real boundaries in this project already have a governing document.

## Verification Requirements

Confirm the architecture's own deliverable contains an explicit trust-boundary list, not just infer one from the diagram.

## Authoritative Sources

- `sentinel-security-system-plan.md` Section 9 — Step 34
- `sec-explicit-responsibility-assignment.md`

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
