---
title: "spec-vault-system"
doc-id: "mb-4960a0bb"
updated: "2026-11-01"
---
# Mybizz — The Vault System

**Scope:** Mybizz-wide. This is the single authoritative document on the Vault system — its architecture, pattern, enforcement rules, and implementation. All other documents reference this one; none duplicate or restate its content.

---

## 1. Two-Level Secrets Model

- **Anvil Secrets** holds exactly one item: a master encryption key, set at provisioning, never changed, used exclusively inside a dedicated vault-service module to encrypt/decrypt application-level secrets. No other code calls `anvil.secrets.get_secret()` directly.
- **The Vault** (an application-level encrypted Data Table) holds every other credential — client API keys, integration tokens. Retrieved only via a `get_vault_secret(name)` function, never accessed directly by integration modules.
- **Access control:** restrict Vault access to the Owner role, require a code from the Owner's authenticator app (TOTP, the Vault's own secret `vault_totp_secret`) on every open with no remembered session, lock the Vault for 15 minutes after 5 wrong codes, and email the Owner on every access.

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

Each application lists its own Vault contents, its Vault form and its build sequence in its own project library. Publishable keys (for example a Stripe publishable key) are safe for client-side use and are stored in the payment configuration table, not the Vault.

## 4. Authenticator Enrolment and Recovery

- On the first open of the Vault, the Owner enrols an authenticator app: the instance shows a QR code and the Owner confirms with one code.
- If the Owner loses the authenticator:
  1. The Owner opens a support ticket while signed in to the instance
  2. Mybizz confirms the Owner's identity by a separate channel: a phone call to the number on the client's Mybizz_management record, where the Owner gives the client reference number
  3. Mybizz_management clears `vault_totp_secret` through the instance's management endpoint; no stored secret is read or changed
  4. On the next open of the Vault, the Owner enrols a new authenticator
  5. The reset is logged in the instance's audit log and in the Mybizz_management amendment log (append-only), and the Owner is emailed

**Constraints:**
- Only Mybizz_management can reset the Vault code — no self-service recovery and no backup codes
- Mybizz never sees, sets or sends a Vault code
- Each application's project library holds its recovery procedure

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-payment-security-boundary-vault]]](C:/dev/project-library-global/adr-global/adr-payment-security-boundary-vault.md) | Architectural decision |
| [[[default:adr-global/adr-anvil-platform-constraints]]](C:/dev/project-library-global/adr-global/adr-anvil-platform-constraints.md) | Anvil secrets limits |
| [[[default:adr-global/adr-brevo-email-and-crm]]](C:/dev/project-library-global/adr-global/adr-brevo-email-and-crm.md) | Vault credentials for Amazon SES |
| [[[default:adr-global/adr-observability-architecture]]](C:/dev/project-library-global/adr-global/adr-observability-architecture.md) | Vault access audit logging |
| [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) | Vault access event forwarding |
| [[[default:specifications-global/spec-security-architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md) | RBAC role limits, sign-in, token security |
| [[[default:specifications-global/spec-client-activation-runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md) | Client provisioning — Vault setup steps |
| Each project library's Vault implementation document | That application's Vault contents, form and build sequence |
