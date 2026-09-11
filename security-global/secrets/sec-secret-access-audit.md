---
document: "Secret Access Audit"
doc-id: sec-secret-access-audit
state: Live
date-created: 2026-08-27
category: secrets
---
# Secret Access Audit

## Applicable Threat

`[[spec-vault-system]]` §1 requires a notification on every Vault access, but a single notification per event is not the same as an ongoing review of the access pattern over time — a slow, low-and-slow pattern of access by a compromised account could still go unnoticed if nobody reviews the accumulated history.

## Security Requirement

Vault access notifications (already required, per `[[spec-vault-system]]` §1) are periodically reviewed as an aggregate pattern, not only reacted to individually as they arrive.

## Approved Pattern

A real, periodic review of accumulated Vault access notifications, looking for unexpected frequency, timing, or a pattern inconsistent with normal operation.

## Prohibited Pattern

Treating each Vault access notification as fully handled once read, with no aggregate review ever performed.

## Implementation Guidance

This is a genuinely open gap, not yet resolved by anything in this project — no periodic review process currently exists beyond the individual, real-time notification already required by `[[spec-vault-system]]`.

## Verification Requirements

Confirm a real, periodic review of Vault access history actually occurs, not just individual notifications being sent.

## Authoritative Sources

- `[[spec-vault-system]]` §1 — access control, per-access notification requirement

## Known Exceptions

None identified — this document names a real, currently unaddressed gap rather than a solved pattern.

## Lessons Learned

None yet. Populated as real findings occur.
