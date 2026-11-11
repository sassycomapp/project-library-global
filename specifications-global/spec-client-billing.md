---
title: "spec-client-billing"
doc-id: "mb-bc4cc414"
updated: "2026-11-11"
---
# Mybizz — Client Billing (Specification)

**Scope:** Mybizz-wide. Covers how every client pays its subscription, how the money and the tax flow, what App 5 does with each payment event, how a client that does not pay is handled, and Mybizz's cash flow per client. Applies to every Mybizz business.

---

## 1. Price and Terms

- £79 a month per client instance, before tax, charged at the fixed price for the client's currency: £79, $99, C$135, €89 or CHF 89 ([[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md)). The terms (month to month, billed monthly in advance, cancel at any time with effect at the end of the paid month) are set in [[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md).
- Paddle sells the subscription as Merchant of Record ([[[default:adr-global/adr-client-billing-merchant-of-record|Client Billing Through a Merchant of Record]]](C:/dev/project-library-global/adr-global/adr-client-billing-merchant-of-record.md)).

---

## 2. Currency

- Mybizz's reference currency is the pound sterling (GBP). Mybizz's prices, revenue, margins and books are stated in GBP.
- Every supplier cost is stated in the currency the supplier bills: DigitalOcean, Anvil, Amazon Web Services and Groq bill in US dollars. Beside each dollar cost, the GBP figure is given at Mybizz's planning rate of **$1 = £0.75**. This planning rate is the only exchange rate used in Mybizz's documents.
- Paddle pays Mybizz out in GBP.

---

## 3. How a Client Pays

- Registration accepts only businesses based in Mybizz's markets: the United States, Canada, the United Kingdom, the European Union, the European Economic Area and Switzerland. Paddle's checkout is limited to the same countries.

1. At registration, the client pays the first month in Paddle's checkout. Paddle's checkout collects the client's billing country and postal code, and optionally its business name and VAT or tax number, which Paddle validates.
2. Paddle adds the tax due in the client's country. A client with a valid business tax number pays no VAT where the reverse charge applies.
3. Paddle renews the subscription every month, in advance, on the same day of the month, and emails the client its tax invoice for each payment.
4. The client changes its card, downloads its invoices and cancels through Paddle's customer portal, reached from a link in every Paddle email.
5. Paddle pays Mybizz once a month, in GBP: the subscriptions collected, less Paddle's fee (5% + $0.50 per payment) and the tax. Each payout comes with Paddle's statement of every payment in it.

---

## 4. Paddle Notifications to App 5

Paddle sends a notification to App 5 for every billing event. App 5 receives them at its HTTP endpoint `/_/api/paddle`.

- App 5 checks each notification's `Paddle-Signature` header against Paddle's notification secret before it acts. A notification that fails the check is rejected and logged.
- Every accepted notification is stored as received in Mybizz's R2 bucket, in the folder `paddle/YYYY-MM/`, before App 5 acts on it. The stored notifications are Mybizz's record of every billing event.
- Paddle's notification secret and the R2 token are held in App 5's Vault.

| Paddle notification | What App 5 does |
|---|---|
| `subscription.activated` | Records the client's Paddle customer and subscription IDs in the client registry and sets `subscription_status` to active. Provisioning starts ([[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)) |
| `transaction.completed` | Records the payment and the new `paid_until` date. If the client is suspended, unsuspends it (section 5) |
| `transaction.payment_failed` | Records `payment_failed_at`, the date of the first failed payment, if not already set |
| `subscription.past_due` | No action beyond recording; the timing of section 5 runs from `payment_failed_at` |
| `subscription.canceled` | When the client cancelled: runs the client exit at the end of the paid month. When the cancellation follows unpaid renewals: the timing of section 5 continues |

Mybizz's R2 bucket is in Mybizz's own Cloudflare account and is used only by App 5. It is separate from every client's R2 bucket, which sits in the client's own Cloudflare account.

---

## 5. A Client That Does Not Pay

App 5 counts the days from `payment_failed_at`. Paddle's payment recovery retries the payment and emails the client throughout.

| Day | What happens |
|---|---|
| 0 | A renewal payment fails. The client keeps full service |
| 7 | If still unpaid, App 5 suspends the client instance through `/management/suspend` ([[[default:adr-global/adr-mybizz-management-visibility\|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)). Every page of the instance shows that payment is needed, with the link to Paddle's customer portal. The container and the database keep running, and no data is touched |
| Any day up to 37 | A completed payment clears `payment_failed_at`. App 5 unsuspends the instance through `/management/unsuspend`, and the client is back at once |
| 37 | If still unpaid, App 5 cancels the Paddle subscription, if Paddle has not already cancelled it, and runs the client exit ([[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 8) |

- **Data is never withheld.** The client owns its data. Every night, the client's data is copied into the client's own R2 bucket, in the client's own Cloudflare account, and the exit export writes the full data there too. A missed payment stops the service, never the client's access to its data.
- **An unpaid balance is never carried forward.** Billing is in advance, so every day of service up to the failed payment is paid for. A client that leaves owes nothing further to Mybizz.
- **The most Mybizz can lose on one client** is the hosting cost of the 37 days between the failed payment and the exit: about £11 ($15) for the container. The database cluster's cost does not change with one client.

---

## 6. Cash Flow

- Every client pays in advance, for the month ahead.
- DigitalOcean, Amazon SES and Groq charge Mybizz after use, by the second or by the item, on one bill at the end of each month. Mybizz pays only for the days a client's container and database exist.
- Each client's payment therefore reaches Mybizz before that client's costs fall due. Every client adds to Mybizz's cash from its first month.

### Per client

| Per client, per month, at £79 | GBP | Billed as |
|---|---|---|
| Subscription, before tax | £79.00 | |
| Paddle's fee (5% + $0.50) | −£4.33 | |
| Paid out to Mybizz | £74.67 | |
| Container (`apps-s-1vcpu-1gb`) | −£9.00 | $12.00 |
| Usage: email £1.00, AI writing and insight £0.50, speech to text £0.10, text to speech £5.00, data transfer over the allowance £1.00 | −£7.60 | |
| Left toward the database cluster and Mybizz's fixed costs | £58.07 | |

The usage figure budgets each client at medium-to-heavy use: a team of about six using email, AI and voice every working day.

**Highest cost of one client.** With every fair-use limit reached ([[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)), one client costs at most £52.98 a month: container £18.75, email £3.75, AI and voice £16.80, data transfer £5.25, Paddle's fee £4.33 and a database share of £3.90. Each client's £79 covers this.

### Database cluster

The cluster grows in stages with the client count: Standard Edition at 2 GiB, £22.50 ($30) a month, to client 11; Standard at 4 GiB, £45 ($60), from client 12; Advanced Edition with a standby at 8 GiB, £195 ($260), from client 25; and Advanced at 16 GiB, about £390 ($520), from client 60 ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 4).

### Mybizz's fixed costs

| Cost | Per month |
|---|---|
| Anvil Business account (Apps 1, 2, 3, 5 and the demo apps) | £74.25 |
| Container Registry, Basic plan | £3.75 |
| Test client instance | £9.00 |
| `mybizz.live` domain | £1.58 |
| Email reputation alarms (two AWS CloudWatch alarms) | £0.15 |
| Cyber Essentials certification, renewed yearly | £26.67 |
| Business insurance, starting covers, paid monthly ([[[default:adr-global/adr-business-insurance]]](C:/dev/project-library-global/adr-global/adr-business-insurance.md)); £141.67 from client 25 | £75.00 |
| ICO data protection fee | £3.92 |
| Companies House confirmation statement | £4.17 |
| FreeAgent accounting software | £33.00 |
| UK address package: registered office and director's service address | £5.00 |
| Marketing: paid search and social advertising | £100.00 |
| **Total, to client 24** | **£336.49** |
| **Total, from client 25** | **£403.16** |

### Totals by client count

| Clients | Revenue | Client-related costs | Fixed costs | Net profit |
|---|---|---|---|---|
| 1 | £79.00 | £43.43 | £336.49 | −£300.92 |
| 7 | £553.00 | £169.01 | £336.49 | £47.50 |
| 25 | £1,975.00 | £718.25 | £403.16 | £853.59 |
| 50 | £3,950.00 | £1,241.50 | £403.16 | £2,305.34 |
| 60 | £4,740.00 | £1,645.80 | £403.16 | £2,691.04 |
| 100 | £7,900.00 | £2,483.00 | £403.16 | £5,013.84 |

Client-related costs are the containers, the usage, Paddle's fees and the database cluster. **Break-even is 7 clients.**

---

## 7. Mybizz's Own Books

- App 5 has no accounting module. Paddle is Mybizz's only customer for subscriptions, and Paddle carries all client tax.
- Mybizz-Live Ltd is registered for VAT from incorporation. Paddle's payouts carry no VAT, because Paddle accounts for the VAT itself. Overseas suppliers charge no VAT to a VAT-registered business, and VAT charged by UK suppliers is reclaimed on the quarterly VAT return. Every supplier price in Mybizz's documents excludes VAT.
- Mybizz-Live Ltd's books are kept in GBP in FreeAgent, which receives every Wise transaction through its bank feed and files the VAT returns, the annual accounts and the company tax return ([[[default:adr-global/adr-company-compliance]]](C:/dev/project-library-global/adr-global/adr-company-compliance.md)). App 5 reads FreeAgent's deadlines and figures, and never writes to it ([[[default:adr-global/adr-freeagent-integration]]](C:/dev/project-library-global/adr-global/adr-freeagent-integration.md)).

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-client-billing-merchant-of-record\|Client Billing Through a Merchant of Record]]](C:/dev/project-library-global/adr-global/adr-client-billing-merchant-of-record.md) | Why Paddle sells the subscription |
| [[[default:adr-global/adr-tiers-model\|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) | The price and the subscription terms |
| [[[default:adr-global/adr-mybizz-management-visibility\|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) | The suspend and unsuspend endpoints and the client registry |
| [[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) | Client exit and the monthly cost |
| [[[default:adr-global/adr-client-r2-storage-and-exit-handover\|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md) | The client's own R2 bucket and the exit export |
