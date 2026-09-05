---
document: "Anvil Platform Responsibility Boundary"
doc-id: sec-anvil-platform-responsibility-boundary
state: Live
date-created: 2026-08-27
category: cloud
---
# Anvil Platform Responsibility Boundary

## Applicable Threat

A security control is assumed to exist because "Anvil handles it," when it is actually the application's own responsibility — or the reverse, application code duplicates something Anvil already guarantees, adding complexity with no benefit.

## Security Requirement

Every security control in this library must be explicitly assigned to either Anvil's platform or the application code. No control may be left unassigned.

## Approved Pattern

Anvil's responsibility, confirmed structural per `spec-five-app-architecture-model.md`: cross-client data isolation (separate app, separate database per client instance — architecturally impossible to breach from application code); Data Table access control at the "no client access" level (`spec-security.md` §1); hosting, TLS, infrastructure uptime.

Application code's responsibility: everything documented elsewhere in this library — within-instance RBAC (`sec-broken-access-control-within-instance`), payment logic (`sec-payment-manipulation`), session validation (`sec-authentication-session`), secret handling (`spec-vault-system.md`, `sec-secret-exposure-response`).

## Prohibited Pattern

Treating within-instance role separation (Staff vs. Customer, Manager vs. Staff) as covered by Anvil's cross-client isolation. They are not the same guarantee — cross-client isolation is structural; within-instance role separation is application logic, and is not automatic.

## Implementation Guidance

Before writing any new security-relevant code, confirm which side of this boundary it falls on. If it's Anvil's responsibility, no application code is needed. If it's the application's, the relevant document in this library applies.

## Verification Requirements

For any new feature, confirm its security controls are explicitly listed as either Anvil-provided or application-implemented — never left unstated.

## Authoritative Sources

- `spec-five-app-architecture-model.md` — structural data isolation
- `spec-security.md` §1 — RBAC and Data Access

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
