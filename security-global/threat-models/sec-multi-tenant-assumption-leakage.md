---
document: "Threat Model — Multi-Tenant Assumption Leakage"
doc-id: sec-multi-tenant-assumption-leakage
state: Live
date-created: 2026-08-27
category: threat-models
---
# Threat Model — Multi-Tenant Assumption Leakage

## Applicable Threat

An AI agent, trained on far more common multi-tenant SaaS patterns than this project's own dependency-based architecture, introduces a tenant-discriminator column, a `tenant_id`-filtered query, or other multi-tenant-style code — directly prohibited by `dependency-based-not-multi-tenant.md`, but a pattern the agent may reach for by default, since it's the far more common industry pattern.

## Security Requirement

No code introduces a tenant discriminator column or tenant-filtered query of any kind, per `dependency-based-not-multi-tenant.md`. Data isolation is structural — separate app, separate database, per client instance — never enforced by a filter within shared code.

## Approved Pattern

`app_tables` resolves to the current client's own data automatically, by virtue of running in that client's own separate app instance — no filtering code needed or permitted.

## Prohibited Pattern

```python
app_tables.bookings.search(tenant_id=current_tenant)  # this pattern should never exist
```

Any query, column, or check referencing a "tenant" concept — this architecture has none.

## Implementation Guidance

If an AI agent's proposed implementation includes any tenant-style filtering, this is an automatic, high-confidence Sentinel finding — the ADR is unambiguous and the risk of an agent defaulting to a more common pattern is real and named directly in `dependency-based-not-multi-tenant.md` itself.

## Verification Requirements

Grep the codebase for `tenant`, `tenant_id`, or similar terms; confirm zero real matches outside comments explicitly explaining why the pattern is prohibited.

## Authoritative Sources

- `dependency-based-not-multi-tenant.md` — the definitive, binding ADR
- `spec-five-app-architecture-model.md` — structural basis for why this isn't needed

## Known Exceptions

None — this ADR has no stated exception.

## Lessons Learned

None yet. Populated as real findings occur.
