---
title: "sec-cyber-essentials-compliance"
doc-id: "mb-98a2bbec"
updated: "2026-11-11"
---
# Cyber Essentials Compliance

## Applicable Threat

The common internet attacks that reach a small company: a stolen password used on a supplier account, a known vulnerability left unpatched, malware on a laptop, an administrator account used for everyday work, and a cloud service left without multi-factor authentication. Any one of them can expose every client's data, because every client runs on Mybizz's suppliers.

## Security Requirement

Mybizz-Live Ltd holds Cyber Essentials certification for the whole organisation, renewed every year, and meets its five controls at all times, not only on the day of assessment. The requirements are the NCSC's Requirements for IT Infrastructure version 3.3, assessed with the Danzell question set. Whole-organisation scope also qualifies Mybizz-Live Ltd for the £25,000 cyber liability insurance included with certification.

## Scope

The whole organisation, with nothing excluded:

| Area | In scope |
|---|---|
| Organisation | Mybizz-Live Ltd, with David as its only director and user |
| Devices | David's laptop and David's phone |
| Cloud services | Every cloud service Mybizz uses: DigitalOcean, Anvil, AWS, Cloudflare, Paddle, GitHub, Groq, FreeAgent, Wise, the business email account and the IASME portal |
| Applications | Apps 1 to 5 of every Mybizz business, and the client hosting platform: the release image, the client containers and the database cluster |

Cloud services cannot be excluded from scope. The asset and software register lists every item in scope.

## Approved Pattern

| Control | How Mybizz meets it |
|---|---|
| Firewalls | Microsoft Defender Firewall on the laptop, always on; the home router supplied by the internet provider is out of scope, so the laptop's own firewall is the boundary. The database cluster accepts connections from DigitalOcean only (trusted sources). Client domains sit behind Cloudflare's web application firewall. |
| Secure configuration | Unused software and accounts removed; screen lock on the laptop and phone; default passwords changed; automatic running of downloaded files switched off. |
| Security update management | Automatic updates on the laptop and phone. Every high or critical fix (vendor-rated high or critical, or CVSS 7 or above, or with no rating given) is installed within 14 days of the vendor's release. The release image is scanned weekly and at every build; a high or critical finding is released to every client within 14 days. Software the vendor no longer supports is removed, and a release image containing it fails its build. |
| User access control | A standard Windows account for daily work and a separate administrator account used for administration only. Multi-factor authentication on every cloud service, through two hardware security keys (FIDO2): one carried, one stored safely. AWS's root user is used for nothing except the tasks only it can do. Access no longer needed is removed. |
| Malware protection | Microsoft Defender Antivirus on the laptop, always on and updated automatically. Apps on the phone come from the official app store only. |

## Prohibited Pattern

- A cloud service in scope without multi-factor authentication.
- A high or critical fix left uninstalled for more than 14 days.
- Software the vendor no longer supports on any device or in the release image.
- Daily work, email or browsing done from an administrator account.
- A device used for Mybizz work that is missing from the register.

Each of these fails the assessment automatically.

## Implementation Guidance

1. Keep the asset and software register current: every device, its operating system and version; every cloud service and its multi-factor method; every application and its supported-until date.
2. Answer the self-assessment from the register.
3. App 5 records the certificate's issue and expiry dates and sends the renewal reminder 60 days before expiry.
4. The yearly business insurance renewal is answered from the same register ([[[default:adr-global/adr-business-insurance]]](C:/dev/project-library-global/adr-global/adr-business-insurance.md)).

## Verification Requirements

- Before each submission, run the NCSC's free Cyber Essentials Readiness Tool against the register and close every gap it reports.
- The release image's weekly scan shows no high or critical finding older than 14 days, and no end-of-life software.
- Every cloud service in the register shows a hardware security key as its sign-in factor.

## Authoritative Sources

- NCSC, Cyber Essentials: Requirements for IT Infrastructure, version 3.3
- IASME, Cyber Essentials Danzell question set

## Known Exceptions

None.

## Related Documents

- [[[default:adr-global/adr-business-insurance]]](C:/dev/project-library-global/adr-global/adr-business-insurance.md)
- [[[default:adr-global/adr-dependency-update-model]]](C:/dev/project-library-global/adr-global/adr-dependency-update-model.md)
- [[[default:security-global/secrets/sec-secret-rotation-policy]]](C:/dev/project-library-global/security-global/secrets/sec-secret-rotation-policy.md)
- [[[default:specifications-global/spec-security-architecture]]](C:/dev/project-library-global/specifications-global/spec-security-architecture.md)
