---
title: "sec-client-provisioning-security"
doc-id: "mb-70793251"
updated: "2026-11-08"
---
# Client Instance Provisioning Security

## Applicable Threat

Provisioning a new client instance involves creating its container and database from the release image, and generating a real, unique management bearer token, `encryption_key` and two container keys, per `[[spec-security-architecture]]` §2 and `[[spec-client-instance-hosting]]` §7. A flaw in this process — a reused token or key, a database user able to reach another client's database, a secret stored insecurely at generation time — compromises that client instance from its very first moment.

## Security Requirement

Each client instance's management token is uniquely generated at provisioning and stored encrypted in both the `Mybizz_management` registry and the client instance's own config, per `[[spec-security-architecture]]` §2's Token Lifecycle. Each client instance's `encryption_key` and container keys are uniquely generated and held only as the container's encrypted environment values. Each client's database user can reach only that client's database.

## Approved Pattern

Token generation and storage exactly as specified — unique per instance, encrypted at rest in both locations, never reused from a prior provisioning.

## Prohibited Pattern

Manually copying a token from a previous client instance's provisioning as a shortcut, or storing the freshly generated token in plaintext even temporarily during the provisioning process.

## Implementation Guidance

Provisioning should be a repeatable, verified procedure, per `[[spec-client-activation-runbook]]` — not an ad-hoc process that could vary between one client and the next.

## Verification Requirements

For each newly provisioned client instance, confirm its management token, `encryption_key` and container keys are genuinely unique (not matching any other client's), confirm each is stored encrypted where required, and confirm its database user is refused by every other client's database.

## Authoritative Sources

- `[[spec-security-architecture]]` §2 — token lifecycle, generation
- `[[spec-client-activation-runbook]]` — the provisioning procedure
- `[[spec-client-instance-hosting]]` §7 — the New client action

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
