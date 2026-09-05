---
document: "Adversarial Verification"
doc-id: sec-testing-adversarial-verification
state: Live
date-created: 2026-08-27
category: testing
---
# Adversarial Verification

## Applicable Threat

A security control is believed to work because the intended, correct-behavior test passes — but nobody actually attempted the specific attack it's meant to prevent.

## Security Requirement

Every threat-model document in this library defines a Prohibited Pattern. For every corresponding Approved Pattern actually implemented, the Prohibited Pattern is deliberately, literally attempted against the real, running code — not just reasoned about.

## Approved Pattern

Each threat-model document's own Verification Requirements section, executed for real: log in as the lower-privileged role, attempt the exact prohibited action, confirm rejection — the same discipline already specified in `sec-broken-access-control-within-instance.md`, `sec-privilege-escalation.md`, and every other threat-model document in this library.

## Prohibited Pattern

Marking a security control verified because its own correct-path test passes, without ever attempting the specific attack it exists to stop.

## Implementation Guidance

For every feature reviewed against this library, the corresponding threat-model document's Verification Requirements are executed literally, not approximated or assumed satisfied by unrelated testing.

## Verification Requirements

For a sample of implemented features, confirm the specific adversarial test from the relevant threat-model document was actually run, with a real, recorded result — not inferred from the feature "working correctly."

## Authoritative Sources

- Every threat-model document in `security-global/threat-models/` — each one's own Verification Requirements section

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
