---
title: "spec-security-architecture"
doc-id: "mb-9112b5a3"
updated: "2026-10-23"
---
# Mybizz — Security & Secrets Architecture

**Related ADRs:** [[[default:adr-global/adr-payment-security-boundary-vault|Payment Security Boundary Vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) (Vault), [[[default:adr-global/adr-client-instance-architecture|Client Instance Architecture]]](C:/dev/project-library-global/adr-global/adr-client-instance-architecture.md), [[[default:adr-global/adr-mybizz-management-visibility|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)

**Note:** Reusable security patterns (the two-level secrets model, secret enforcement/masking,
RBAC/data access pattern, rate limiting) live in [[[default:specifications-global/spec-security|Security Specification]]](C:/dev/project-library-global/specifications-global/spec-security.md). The
regulatory baseline (POPIA, GDPR, PCI DSS, standard retention periods) is Mybizz-wide — see
[[[default:specifications-global/spec-regulatory-compliance-baseline|Regulatory Compliance Baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md). This document contains the Mybizz-wide security architecture and token model that applies to every application.

---

## 1. RBAC — Role Limits

Five roles, per the standard RBAC pattern (see [[[default:specifications-global/spec-security|Security Specification]]](C:/dev/project-library-global/specifications-global/spec-security.md)). The standard per-instance limits that apply to all Mybizz applications:

| Role | Access | Instance Limit |
|---|---|---|
| Owner | Full access including Vault, financial data, user management | 1 per instance |
| Manager | Operational management — bookings, customers, marketing, reporting. No Vault or financial config | 0–3 per instance |
| Admin | Booking and customer management. No financial reporting, settings, or Vault | 0–10 per instance |
| Staff | Own calendar and bookings only | 0–20 per instance |
| Customer | Own bookings, invoices, account in the customer portal | Unlimited |

### Sign-in

- Every account holder signs in with a password and a second factor. Anvil can require a second factor only for the whole app, so every account holder has one, a Customer with a portal account included. Shoppers who only buy check out as guests, without an account.
- The Owner uses only FIDO2 (a hardware key or the device's passkey), which resists phishing. The Owner's high-value functions are refused while any other kind of second factor is enrolled.
- Vault access, refunds above the set limit, role changes, exports, gateway changes and price changes need a second factor given in the last five minutes. The user re-confirms by signing in again with password and second factor (for FIDO2, Anvil's `anvil.users.mfa.get_fido_mfa_login` and `anvil.users.login_with_email`); the server accepts these calls only within five minutes of the user's `last_login`. Vault access needs this on every open.

### Ending a user's sessions

The Owner can end any user's sessions. A server function clears that user's remembered logins and remembered second factor, and records the time; every server function refuses a session that began before that time.

## 2. Mybizz_management Token Security (per [[[default:adr-global/adr-mybizz-management-visibility|Mybizz_management Visibility and Control]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) ADR)

Mybizz_management communicates with client instances via bidirectional HTTP endpoints secured
with per-client Bearer tokens. This is the standard Mybizz service-to-service authentication
pattern — there is no reusable pattern here beyond the general "use Bearer tokens for
service-to-service auth" idea, which isn't specific enough to be worth extracting.

### Token Types

| Direction | Token Type | Storage |
|---|---|---|
| Mybizz → Client | Per-client Bearer token (unique per instance) | Mybizz_management client registry (encrypted); client instance management config |
| Client → Mybizz | Shared event push token | Each client instance's Vault |

### Security Properties

- **Per-client isolation:** a unique management Bearer token per client instance — compromise of
  one instance does not affect others.
- **Encrypted storage:** management tokens stored encrypted in Mybizz_management's client
  registry.
- **Server-side validation:** all management endpoints validate the Bearer token before
  processing; invalid tokens receive HTTP 403.
- **Non-blocking event push:** client-to-Mybizz event push calls are non-blocking — failure to
  reach Mybizz_management does not block client instance processing.

### Token Lifecycle

- **Generation:** unique token generated at provisioning (see [[[default:specifications-global/spec-client-activation-runbook|Client Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) in
  `specifications/`).
- **Storage:** stored in both the Mybizz_management registry (encrypted) and the client
  instance's own config.
- **Rotation:** not automated in V1 — manual rotation via re-provisioning if compromise is
  suspected.
- **Revocation:** delete from both the Mybizz_management registry and the client instance config.

## 3. Regulatory Compliance

The regulatory baseline (POPIA, GDPR, PCI DSS, standard retention periods) is Mybizz-wide — see
[[[default:specifications-global/spec-regulatory-compliance-baseline|Regulatory Compliance Baseline]]](C:/dev/project-library-global/specifications-global/spec-regulatory-compliance-baseline.md). The standard applicability:

- **PCI DSS applies** — Mybizz processes payments via Stripe and Paystack, placing
  it in SAQ A scope per the Mybizz-wide standard.
- **GDPR applies conditionally** — if an app serves EU customers (determined by actual client
  base, not fixed at build time).
- No data categories beyond the Mybizz-wide retention defaults are tracked.

