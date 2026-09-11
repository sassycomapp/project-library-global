---
document: "Principle — Detective vs. Preventive Controls"
doc-id: sec-detective-vs-preventive-controls
state: Live
date-created: 2026-08-27
category: principles
---
# Principle — Detective vs. Preventive Controls

## Statement

A preventive control stops a bad action before it happens. A detective control notices it happened, afterward. The two are not interchangeable, and a detective control is never treated as if it were preventive.

## Real Precedent in This Project

- Cupcake policy and native permission config are preventive — they block a matching action before it executes.
- `gbrain doctor`, Cupcake's Observability logging, and the compliance ledger are detective — they record or check after the fact, per `structural-compliance-enforcement-architecture-v3.md` Section 5's own classification table.
- `[[sec-audit-log-integrity]]` — logs are evidence for human review, never self-proving authorization.

## Why This Matters

A detective control tells you something went wrong after the damage may already be done. Relying on one where a preventive control was actually needed means real harm can occur before anyone notices.

## Application

For any given risk, ask explicitly: does this control stop the action, or only notice it afterward? A high-consequence risk needs a preventive control; a detective control alone is not sufficient for it.

## Known Exceptions

Some risks genuinely cannot be prevented structurally (e.g. semantic/judgment errors) and rely on detective controls plus human review by necessity — see `[[sec-ai-agent-introduced-vulnerabilities]]`. This is a real, accepted limitation, not a violation of this principle.
