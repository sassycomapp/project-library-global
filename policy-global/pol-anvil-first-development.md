# Policy — Anvil-First Development

**Binding.** All development work on any Anvil.works project under this operation must
conform. No exceptions without documented justification.

---

## What

### The Anvil-First Mandate

Every technical decision defaults to the Anvil way. Where Anvil provides a facility —
authentication, data persistence, background tasks, email, secrets — that facility is
used. Custom alternatives are not introduced unless Anvil's facility is genuinely
inadequate.

**Before implementing any feature, check in this order:**
1. Anvil's built-in components and services
2. Anvil documentation for native solutions
3. Anvil's example apps for established patterns
4. Anvil community forum for community approaches
5. Only then consider a custom implementation — and document the justification

**Approved standing exception:** the Vault. Client API keys cannot go in Anvil Secrets
because doing so would require giving clients IDE access. The Vault is an
application-level encrypted secrets store — see `spec-anvil-platform-standards.md` for the
technical pattern. Any further exception beyond the Vault requires the same
documented-justification standard as any other custom implementation, not a blanket
extension of this one.

### Version Control

Commit format: `[TYPE] Brief description`, where TYPE is one of FEATURE, FIX, REFACTOR,
SECURITY.

Branching: `master` (production), `dev` (development integration), `feature/{name}`,
`fix/{description}`.

### Backup Protocol

Two backup points per feature, both mandatory — see
`spec-testing-methodology-standards.md` §4 for the full discipline. Never back up a red
or failing state.

### Development Tooling

The Anvil app is connected to GitHub as the shared source of truth. Changes made in an
external editor are pushed to GitHub; Anvil syncs from GitHub. Changes made in the Anvil
Designer are pulled to local before any further code work on the affected form.

### Enforcement Severity

| Level | Definition | Response |
|---|---|---|
| Critical | Security issue or data loss risk | Immediate fix — do not proceed |
| High | Policy violation | Fix before moving to next task |
| Medium | Best practice deviation | Document and schedule |
| Low | Style or formatting | Fix when convenient |

Security issues are always Critical. RBAC violations, secret-handling errors, and any code
path that returns sensitive data to the client are Critical without exception — no
judgment call reduces their severity.

---

## Why

Anvil is the platform this operation has standardized on. Reinventing what Anvil already
provides adds maintenance burden, drifts from platform upgrades, and produces code a new
developer joining any project won't recognize. The checking order exists so "custom" is a
documented last resort, not a default habit. The enforcement table exists so severity is
argued once, here, rather than re-litigated on every finding.

---

## Where

Every project this operation builds on Anvil.works. Applies from the first line of code.

**Source:** consolidated from prior project practice; the Anvil-First mandate and
enforcement table are proven patterns, carried forward deliberately, not invented fresh.
