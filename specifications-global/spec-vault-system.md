---
title: "spec-vault-system"
doc-id: "mb-4960a0bb"
updated: "2026-10-22"
---
# Mybizz — The Vault System

**Scope:** Mybizz-wide. This is the single authoritative document on the Vault system — its architecture, pattern, enforcement rules, and implementation. All other documents reference this one; none duplicate or restate its content.

**Authority:** [[[default:adr-global/adr-payment-security-boundary-vault|Payment Security Boundary Vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) ADR ([[[default:adr-global/adr-payment-security-boundary-vault|Payment Security Boundary: Secret Keys Deferred to the Vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md))

---

## 1. Two-Level Secrets Model

- **Anvil Secrets** holds exactly one item: a master encryption key, set at provisioning, never changed, used exclusively inside a dedicated vault-service module to encrypt/decrypt application-level secrets. No other code calls `anvil.secrets.get_secret()` directly.
- **The Vault** (an application-level encrypted Data Table) holds every other credential — client API keys, integration tokens. Retrieved only via a `get_vault_secret(name)` function, never accessed directly by integration modules.
- **Access control:** restrict Vault access to the Owner role, require a fresh second factor on every open with no grace period (the Owner's is FIDO2, per [[[default:specifications-global/spec-security]]](C:/dev/project-library-global/specifications-global/spec-security.md)), and send a notification on every access.

## 2. Secret Enforcement and Masking

Enforce at the point of persistence, not just at the point of retrieval — use a hard-fail assert so a secret can never be accidentally saved outside the Vault:

```python
_PAYMENT_SECRET_COLUMNS = frozenset({
    'stripe_secret_key', 'paystack_secret_key', 'paypal_secret'
})
assert not (_PAYMENT_SECRET_COLUMNS & set(data.keys())), (
    f"Secret key columns must not be saved here: "
    f"{_PAYMENT_SECRET_COLUMNS & set(data.keys())}"
)
```

`AssertionError` must always be re-raised before any broader exception handler — never swallowed.

**Masking:** any function returning configuration containing a secret field returns `'***'` for that field, never the real value. Client-side save methods must never include a secret field in an outbound payload, even a masked one — omit the field entirely rather than round-trip it.

## 3. What's Stored in the Vault (per application)

Each application lists its own Vault contents, its Vault form and its build sequence in its own project library; `mb-3-cs` holds them in `docs-local\mb-3-cs-vault-implementation.md`. Publishable keys (for example a Stripe publishable key) are safe for client-side use and are stored in the payment configuration table, not the Vault.

## 4. Second-Factor Recovery

If the Owner loses their second-factor device, the following recovery path applies:

1. Owner contacts Mybizz support (Mybizz_management)
2. Mybizz_management verifies the Owner's identity through out-of-band process
3. Mybizz_management resets the Owner's second-factor configuration
4. Owner enrols a new FIDO2 key or passkey
5. The reset event is logged in the Mybizz_management amendment log (append-only)

**Constraints:**
- Only Mybizz_management can reset the Owner's second factor — no self-service recovery
- The reset event is permanently logged for audit

**Source:** [[[default:adr-global/adr-anvil-platform-constraints|Anvil Platform Constraints and Design Boundaries]]](C:/dev/project-library-global/adr-global/adr-anvil-platform-constraints.md) ADR, CEO review 2026-06-15 Section 3

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-payment-security-boundary-vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) | Architectural decision |
| [[[default:adr-global/adr-anvil-platform-constraints]]](C:/dev/project-library-global/adr-global/adr-anvil-platform-constraints.md) | Anvil secrets limits, Owner second-factor recovery |
| [[[default:adr-global/adr-brevo-replaces-zoho-email]]](C:/dev/project-library-global/adr-global/adr-brevo-replaces-zoho-email.md) | Vault credentials for Brevo |
| [[[default:adr-global/adr-observability-architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md) | Vault access audit logging |
| [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) | Vault access event forwarding |
| [[[default:specifications-global/spec-security-architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md) | RBAC role limits, sign-in, token security |
| [[[default:specifications-global/spec-client-activation-runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Client provisioning — Vault setup steps |
| Each project library's Vault implementation document | That application's Vault contents, form and build sequence |
