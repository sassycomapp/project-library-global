---
title: "adr-business-insurance"
doc-id: "mb-e72ca98e"
updated: "2026-11-11"
---
# Business Insurance

Status: Accepted

---

## Context

Mybizz-Live Ltd hosts every client's business on its own platform. A fault, an outage, lost data or a cyber incident can cost a client money, and the client can claim that money from Mybizz-Live Ltd. A cyber incident also costs Mybizz-Live Ltd directly: incident response, data restoration, lost income, client notification and regulatory investigation. Mybizz-Live Ltd is a micro company that must keep its fixed costs low enough to break even at 9 clients.

---

## Decision

1. **One combined policy from one insurer, renewed yearly,** holding three covers:

| Cover | Limit | What it pays |
|---|---|---|
| Technology professional indemnity | £1m | A client's claim for loss caused by a fault, an outage or lost data in the Mybizz service, and the legal costs of defending it |
| Cyber liability | £500,000 | Incident response through the insurer's 24-hour line, data restoration, lost income, client notification, regulatory investigation, and claims from affected people |
| Public liability | £1m | Injury to a person or damage to property in connection with Mybizz's business |

2. **The Cyber Essentials cover is kept as well.** Whole-organisation Cyber Essentials certification includes £25,000 of cyber liability insurance with incident response, which Mybizz-Live Ltd opts into ([[[default:security-global/compliance/sec-cyber-essentials-compliance]]](C:/dev/project-library-global/security-global/compliance/sec-cyber-essentials-compliance.md)).

3. **Employers' liability.** The law does not require it while David is the sole director, owns more than half the shares and no one else works for Mybizz. Employers' liability of at least £5m is bought before anyone other than David works for Mybizz, paid or unpaid.

4. **Liability cap.** The client service agreement caps Mybizz-Live Ltd's total liability to a client at the fees that client paid in the 12 months before the claim. The cap sits inside the £1m professional indemnity.

5. **Policy conditions.** Each condition the insurer sets is met by a safeguard and checked by a test:

| Condition | Safeguard | Test |
|---|---|---|
| Multi-factor authentication on every service | Hardware security keys on every cloud service ([[[default:security-global/compliance/sec-cyber-essentials-compliance]]](C:/dev/project-library-global/security-global/compliance/sec-cyber-essentials-compliance.md)) | Register check before each renewal |
| Backups kept separately, protected and tested | Nightly copy of each client into the client's own R2 bucket with a 30-day retention lock; monthly restore drill ([[[default:security-global/infrastructure/sec-backup-recovery-integrity]]](C:/dev/project-library-global/security-global/infrastructure/sec-backup-recovery-integrity.md)) | Locked-backup deletion test; monthly restore drill |
| Security updates applied promptly | High and critical fixes within 14 days ([[[default:adr-global/adr-dependency-update-model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md)) | Release readiness check on scan findings |
| Supported software only | End-of-life software fails the image build | Release readiness check on end-of-life software |
| Incidents reported to the insurer first | The incident response plan calls the insurer's incident line before engaging any outside supplier | Incident drill on the test client instance |

6. **Renewal.** App 5 records the policy dates and sends David a reminder 30 days before expiry. The renewal proposal form is answered from the Cyber Essentials asset and software register.

7. **Cost.** The budget figure is £1,700 a year including Insurance Premium Tax, replaced by the quoted premium when the policy is bought.

---

## Rationale

1. Professional indemnity is the cover a software service most needs: the largest risk is a client's own loss caused by the service.
2. One insurer for professional indemnity and cyber liability means a claim that is both an error and a breach cannot fall between two policies.
3. £500,000 of cyber cover is the common level for a micro business and keeps break-even at 9 clients; the Cyber Essentials cover adds incident response on top.
4. A liability cap inside the insurance limit means no single claim can exceed the cover.
5. Tying each policy condition to a tested safeguard means a claim cannot be refused for a condition that was not met.

---

## Consequences

- The client service agreement carries the liability cap and the breach notice clause.
- The incident response plans of every business name the insurer's incident line as the first call.
- App 5 holds the policy dates and the renewal reminder ([[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)).

---

## Related Documents

- [[[default:security-global/compliance/sec-cyber-essentials-compliance]]](C:/dev/project-library-global/security-global/compliance/sec-cyber-essentials-compliance.md)
- [[[default:adr-global/adr-company-compliance]]](C:/dev/project-library-global/adr-global/adr-company-compliance.md)
- [[[default:adr-global/adr-mybizz-management-visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)
