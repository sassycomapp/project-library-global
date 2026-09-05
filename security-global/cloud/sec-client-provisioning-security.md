---
document: "Client Instance Provisioning Security"
doc-id: sec-client-provisioning-security
state: Live
date-created: 2026-08-27
category: cloud
---
# Client Instance Provisioning Security

## Applicable Threat

Provisioning a new client instance involves cloning `blank_client_template` and generating a real, unique management bearer token, per `spec-security-architecture.md` §2. A flaw in this process — a reused token, an incomplete clone, a token stored insecurely at generation time — compromises that client instance from its very first moment.

## Security Requirement

Each client instance's management token is uniquely generated at provisioning and stored encrypted in both the `Mybizz_management` registry and the client instance's own config, per `spec-security-architecture.md` §2's Token Lifecycle.

## Approved Pattern

Token generation and storage exactly as specified — unique per instance, encrypted at rest in both locations, never reused from a prior provisioning.

## Prohibited Pattern

Manually copying a token from a previous client instance's provisioning as a shortcut, or storing the freshly generated token in plaintext even temporarily during the provisioning process.

## Implementation Guidance

Provisioning should be a repeatable, verified procedure, per `spec-client-activation-runbook.md` — not an ad-hoc process that could vary between one client and the next.

## Verification Requirements

For each newly provisioned client instance, confirm its management token is genuinely unique (not matching any other client's) and confirm it's stored encrypted in both required locations.

## Authoritative Sources

- `spec-security-architecture.md` §2 — token lifecycle, generation
- `spec-client-activation-runbook.md` (referenced, not yet reviewed directly)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
