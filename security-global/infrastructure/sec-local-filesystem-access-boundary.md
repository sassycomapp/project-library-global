---
document: "Local Filesystem Access Boundary"
doc-id: sec-local-filesystem-access-boundary
state: Live
date-created: 2026-08-27
category: infrastructure
---
# Local Filesystem Access Boundary

## Applicable Threat

This environment spans two real, distinct filesystems — WSL's native Linux filesystem and the Windows-mounted drive (`/mnt/c/...`) — with tools and processes crossing between them. An agent action assumed to be scoped to one project's folder could reach further than intended if the boundary isn't explicitly enforced.

## Security Requirement

Per the native OpenCode permission system (the retired `the retired structural-compliance-enforcement-architecture-v3.md` Section 6.3): `external_directory` scoping is correctly configured and verified, not assumed, for every project.

## Approved Pattern

The already-built and verified native permission config — confirmed this project, a real file survived an attempted destructive command via OpenCode chat, blocked at the permission level, physically confirmed in WSL.

## Prohibited Pattern

Assuming a project's file access is scoped correctly without the same kind of live verification already performed once — a written config rule is not itself proof it's actually enforced.

## Implementation Guidance

Any new project onboarded should have its `external_directory` scoping explicitly checked, the same way the existing verification was performed, not assumed correct because it follows the same template as an already-verified project.

## Verification Requirements

Attempt a file operation outside the intended project boundary; confirm it is blocked, physically verified on disk, not merely assumed from the permission config's written rule.

## Authoritative Sources

- the retired `the retired structural-compliance-enforcement-architecture-v3.md` Section 6.3, Implementation Status — the real, already-performed live test

## Known Exceptions

None identified.

## Lessons Learned

None yet. Populated as real findings occur.
