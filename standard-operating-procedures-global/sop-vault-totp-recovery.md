# {Project Name} — SOP: Vault TOTP Recovery

**Authority:** **[PROJECT]** cite this project's Vault/security ADR (TOTP step-up
requirement).

---

## Procedure — Owner Lost TOTP Device

**Trigger:** An Owner cannot complete TOTP step-up to access the Vault because they've
lost their authenticator device.

**Preconditions:**
- Requester confirmed to be contacting through the platform's own support channel, not
  responding to an inbound request for credentials

**Steps:**
1. Owner contacts platform support
2. Support verifies the Owner's identity through an out-of-band process — **[PROJECT]**
   state this project's actual verification method(s): government ID, registered email,
   security questions, or equivalent
3. Support resets the Owner's TOTP configuration
4. Owner re-enrolls TOTP on their new device
5. The reset event is logged in an append-only amendment log

**Constraints — fixed, do not weaken:**
- Only platform support/operator tooling can perform this reset — no self-service
  recovery path exists or should be added
- The reset event is permanently logged for audit, no exceptions
- This is an operational requirement independent of any specific code feature — it must
  work even if the supporting tooling is still being built

**Verification:**
- [ ] Identity verification actually completed and recorded, not skipped under urgency
- [ ] Owner successfully re-enrolled and can access the Vault
- [ ] Reset event appears in the amendment log with timestamp and operator identity

**Escalation:** if identity cannot be verified through the standard out-of-band process,
do not reset TOTP on the requester's assurance alone — escalate per **[PROJECT]** this
project's identity-verification escalation path. Resetting TOTP for an unverified
requester is a security incident, not a convenience shortcut.

---

*This is the global starter model. Copy into a new project's
`standard-operating-procedures-local/`, fill every **[PROJECT]** marker, remove this
closing note. The core constraints — no self-service recovery, mandatory audit logging —
are standing security posture; keep them as-is regardless of project.*
