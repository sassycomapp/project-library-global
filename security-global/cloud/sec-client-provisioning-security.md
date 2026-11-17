---
title: "sec-client-provisioning-security"
doc-id: "mb-70793251"
updated: "2026-11-17"
---
# Client Instance Provisioning Security

## Applicable Threat

Provisioning a new client instance involves creating its container and database from the release image, and generating a real, unique management bearer token, `encryption_key` and two container keys, per `[[spec-security-architecture]]` §2 and `[[spec-client-instance-hosting]]` §7. A flaw in this process — a reused token or key, a database user able to reach another client's database, a secret stored insecurely at generation time — compromises that client instance from its very first moment. App 5 reaches the platform through each server's provisioning runner and through Hetzner and Ubicloud API keys; a runner able to run any command, or a key with wider scope than its use, could harm every client.

## Security Requirement

Each client instance's management token is uniquely generated at provisioning and stored encrypted in both the `Mybizz_management` registry and the client instance's own config, per `[[spec-security-architecture]]` §2's Token Lifecycle. Each client instance's `encryption_key` and container keys are uniquely generated and held only as the container's encrypted environment values. Each client's database user can reach only that client's database.

## Approved Pattern

Token generation and storage exactly as specified — unique per instance, encrypted at rest in both locations, never reused from a prior provisioning.

**The provisioning runner.** A small Python service on each application server connects out to App 5 through Anvil Uplink, so no inbound port is opened for it. It exposes only fixed functions (create, release, resize, suspend, resume and remove an instance, approve a domain, report server health), each running fixed commands with checked arguments, and never a free-form command. Each server's Uplink key is held in App 5's Vault and on that server, readable only by the system administrator account.

**Platform keys,** in App 5's Vault:

| Key | Scope | Used by |
|---|---|---|
| Hetzner API key, one per business | Read and write in that business's Hetzner project only | **Add server**, **Rebuild server** |
| Ubicloud API key | Mybizz's database service | The database stages, **Rebuild** |

A leak of one business's Hetzner key cannot reach another business's servers or any database. Every key expires after a year, or is rotated yearly where the supplier sets no expiry, per `[[sec-secret-rotation-policy]]`.

**The provisioning database role.** The database service accepts connections only from Mybizz's Hetzner servers, so client databases are created by the runner with the provisioning database role, which may create databases and roles and nothing else. The runner creates each client's database and its user with a connection limit of 3, a statement timeout of 60 seconds and an idle-in-transaction timeout of 120 seconds, per `[[sec-database-access-control]]`.

## Prohibited Pattern

Manually copying a token from a previous client instance's provisioning as a shortcut, or storing the freshly generated token in plaintext even temporarily during the provisioning process.

A Hetzner key with access to more than one business's project; a runner function that runs a free-form command; creating a database user from outside Mybizz's servers by opening the database firewall.

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
