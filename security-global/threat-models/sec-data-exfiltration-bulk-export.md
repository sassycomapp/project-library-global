---
document: "Threat Model — Data Exfiltration via Bulk Export Abuse"
doc-id: sec-data-exfiltration-bulk-export
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Data Exfiltration via Bulk Export Abuse

## Applicable Threat

A legitimate reporting or export feature, intended for normal operational use by Manager/Owner roles, is used to extract the entire customer database at once — a real risk distinct from a technical exploit, since the access itself is authorized; only the scale and intent are abusive.

## Security Requirement

Any bulk export or reporting feature returning customer data logs the export event itself (who, when, how much), separate from ordinary read access, so an unusual export can be identified after the fact even though the access was technically authorized.

## Approved Pattern

Export functions write a real log entry recording the requesting user, timestamp, and approximate scope of data exported, in addition to performing the export itself.

## Prohibited Pattern

A bulk export function that performs the export with no record of the event beyond ordinary, routine data access, indistinguishable from a single customer's normal detail view.

## Implementation Guidance

Distinguish, in logging, between routine single-record access and a bulk export touching many records at once — the second is a meaningfully different event, even when performed by an authorized role.

## Verification Requirements

Perform a real bulk export; confirm a distinct log entry exists recording it, separate from ordinary access logging.

## Authoritative Sources

- `spec-security-architecture.md` §1 — RBAC role limits (Manager/Owner have broader access, which is exactly what makes this risk real for those roles specifically)

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
