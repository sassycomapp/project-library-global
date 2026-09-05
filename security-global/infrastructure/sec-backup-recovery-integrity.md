---
document: "Backup and Recovery Integrity"
doc-id: sec-backup-recovery-integrity
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Backup and Recovery Integrity

## Applicable Threat

Real, permanent data loss — a table deleted, a bad migration applied, corrupted state — with no verified way to recover, discovered only when recovery is actually attempted and found not to work.

## Security Requirement

Recovery from real data loss must be proven by an actual, live drill, not assumed from the existence of a backup mechanism. Confirmed real precedent: the memory governor's own disaster-recovery drill this project, run twice, deliberately deleting real data and reconstructing it, with every step verified live.

## Approved Pattern

Real deletion, real reconstruction attempt, real verification the reconstructed state matches the original — the same discipline already applied twice to the memory governor.

## Prohibited Pattern

Treating "a backup process exists" as equivalent to "recovery is proven." An unexercised backup is an unverified claim, not a guarantee.

## Implementation Guidance

Every component holding data that would be genuinely costly to lose (the PDLF ledger, GBrain's own database, the compliance library itself) should have its own real recovery drill performed at least once, following the same pattern already proven for the memory governor.

## Verification Requirements

For each critical data store, confirm: a real drill has been performed, not merely a backup schedule configured; the reconstructed state was directly compared against the original, not assumed correct.

## Authoritative Sources

- Memory governor disaster-recovery drills (this project), both runs, real deletion and reconstruction, independently verified

## Known Exceptions

None identified — no other component in this project has yet had its own recovery drill performed; this is a real, open item, not a completed one.

## Lessons Learned

None yet. Populated as real findings occur.
