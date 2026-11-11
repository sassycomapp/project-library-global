---
title: "sec-backup-recovery-integrity"
doc-id: "mb-4189f46c"
updated: "2026-11-11"
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

Keeping backups that the keys Mybizz holds can delete or overwrite. An intruder with those keys could then destroy the backups along with the data.

## Implementation Guidance

Every component holding data that would be genuinely costly to lose (the PDLF ledger, GBrain's own database, the compliance library itself) should have its own real recovery drill performed at least once, following the same pattern already proven for the memory governor.

### Client instances

- **Two copies of every client's data:** DigitalOcean's daily cluster backups with 7-day point-in-time recovery, inside DigitalOcean; and each client's nightly copy in its own R2 bucket, outside DigitalOcean.
- **Locked copies:** the copies sit under `backups/` in the client's R2 bucket, and each copy is locked for its whole retention period: a daily copy (`backups/daily/`, the last 7 kept) for 7 days, and a weekly copy (`backups/weekly/`, the last 4 kept) for 28 days. No key, Mybizz's included, can delete or overwrite a copy while it is locked ([[[default:adr-global/adr-client-r2-storage-and-exit-handover|Client R2 Storage and Exit]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md)).
- **Daily backup check:** App 5 checks that each client's nightly copy arrived, with the right date and a plausible size.
- **Monthly restore drill:** the test client instance restores one client's nightly copy into a scratch database in the cluster, compares its row counts with the source, deletes the scratch database and reports the result to App 5.
- **Rebuild:** App 5's **Rebuild** action is proven by restoring the test client instance in another region before the first paying client ([[[default:specifications-global/spec-deployment|Deployment Specification]]](C:/dev/project-library-global/specifications-global/spec-deployment.md) section 10).

## Verification Requirements

For each critical data store, confirm: a real drill has been performed, not merely a backup schedule configured; the reconstructed state was directly compared against the original, not assumed correct.

For client instances, also confirm: an attempt to delete a locked nightly copy fails; the latest monthly restore drill passed; the daily backup check reported every active client.

## Authoritative Sources

- Memory governor disaster-recovery drills (this project), both runs, real deletion and reconstruction, independently verified

## Known Exceptions

None identified. Client instances are covered by the monthly restore drill above.

## Lessons Learned

None yet. Populated as real findings occur.
