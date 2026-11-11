---
title: "sec-client-provisioning-security"
doc-id: "mb-70793251"
updated: "2026-11-11"
---
# Client Instance Provisioning Security

## Applicable Threat

Provisioning a new client instance involves creating its container and database from the release image, and generating a real, unique management bearer token, `encryption_key` and two container keys, per `[[spec-security-architecture]]` §2 and `[[spec-client-instance-hosting]]` §7. A flaw in this process — a reused token or key, a database user able to reach another client's database, a secret stored insecurely at generation time — compromises that client instance from its very first moment. App 5 reaches DigitalOcean with access keys that can create and delete every client's container and database; a leaked key with full scope could delete every client.

## Security Requirement

Each client instance's management token is uniquely generated at provisioning and stored encrypted in both the `Mybizz_management` registry and the client instance's own config, per `[[spec-security-architecture]]` §2's Token Lifecycle. Each client instance's `encryption_key` and container keys are uniquely generated and held only as the container's encrypted environment values. Each client's database user can reach only that client's database.

## Approved Pattern

Token generation and storage exactly as specified — unique per instance, encrypted at rest in both locations, never reused from a prior provisioning.

**Two DigitalOcean access keys with custom scopes,** both in App 5's Vault:

| Key | Scope | Used by |
|---|---|---|
| Automatic-tasks key | Read and update apps and databases; no create, no delete | Scheduled checks, both resize actions, **Release**, **Suspend** |
| Provisioning key | Create and delete apps and databases | **New client**, **Remove** and **Rebuild** only |

A leak of the automatic-tasks key, which is used every day, cannot create or delete a client. Both keys expire after a year and are rotated per `[[sec-secret-rotation-policy]]`.

**The provisioning job.** The cluster accepts connections from inside DigitalOcean only (trusted sources), so client database users are created by a provisioning job that runs inside DigitalOcean. The job creates each client's database and its user with a connection limit of 3, a statement timeout of 60 seconds and an idle-in-transaction timeout of 120 seconds, per `[[sec-database-access-control]]`.

## Prohibited Pattern

Manually copying a token from a previous client instance's provisioning as a shortcut, or storing the freshly generated token in plaintext even temporarily during the provisioning process.

A single DigitalOcean key with full access; the provisioning key used for any action other than **New client**, **Remove** and **Rebuild**; creating a database user from outside DigitalOcean by opening the cluster's trusted sources.

## Implementation Guidance

Provisioning should be a repeatable, verified procedure, per `[[spec-client-activation-runbook]]` — not an ad-hoc process that could vary between one client and the next.

## Verification Requirements

For each newly provisioned client instance, confirm its management token, `encryption_key` and container keys are genuinely unique (not matching any other client's), confirm each is stored encrypted where required, and confirm its database user is refused by every other client's database and carries its three limits. Confirm the automatic-tasks key is refused when it tries to create or delete an app or a database.

## Authoritative Sources

- `[[spec-security-architecture]]` §2 — token lifecycle, generation
- `[[spec-client-activation-runbook]]` — the provisioning procedure
- `[[spec-client-instance-hosting]]` §7 — the New client action

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
