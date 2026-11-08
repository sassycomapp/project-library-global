---
title: "sec-anvil-platform-responsibility-boundary"
doc-id: "mb-b889a077"
updated: "2026-11-08"
---
# Anvil Platform Responsibility Boundary

## Applicable Threat

A security control is assumed to exist because "the platform handles it," when it is actually the application's own responsibility — or the reverse, application code duplicates something the platform already guarantees, adding complexity with no benefit.

## Security Requirement

Every security control in this library must be explicitly assigned to the platform (Anvil's runtime, DigitalOcean, or Mybizz's release and provisioning procedures) or to the application code. No control may be left unassigned.

## Approved Pattern

Anvil's runtime, confirmed structural per `[[spec-five-app-architecture-model]]`: cross-client data isolation (a separate App Server and a separate database per client instance — architecturally impossible to breach from application code); Data Table access control at the "no client access" level (`[[spec-security]]` §1).

DigitalOcean's responsibility, per `[[spec-client-instance-hosting]]`: the servers and their operating-system updates, TLS certificates on each client's domain, container restarts, database patching, backups, standby failover and infrastructure uptime.

Mybizz's release and provisioning procedures, per `[[spec-client-instance-hosting]]`: a separate database user per client, unique keys and tokens per client, the pinned App Server version, and the release checks.

Application code's responsibility: everything documented elsewhere in this library — within-instance RBAC (`[[sec-broken-access-control-within-instance]]`), payment logic (`[[sec-payment-manipulation]]`), session validation (`[[sec-authentication-session]]`), secret handling (`[[spec-vault-system]]`, `[[sec-secret-exposure-response]]`).

## Prohibited Pattern

Treating within-instance role separation (Staff vs. Customer, Manager vs. Staff) as covered by the platform's cross-client isolation. They are not the same guarantee — cross-client isolation is structural; within-instance role separation is application logic, and is not automatic.

## Implementation Guidance

Before writing any new security-relevant code, confirm which side of this boundary it falls on. If it's the platform's responsibility, no application code is needed. If it's the application's, the relevant document in this library applies.

## Verification Requirements

For any new feature, confirm its security controls are explicitly listed as either platform-provided or application-implemented — never left unstated.

## Authoritative Sources

- `[[spec-five-app-architecture-model]]` — structural data isolation
- `[[spec-client-instance-hosting]]` — DigitalOcean and the release and provisioning procedures
- `[[spec-security]]` §1 — RBAC and Data Access

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
