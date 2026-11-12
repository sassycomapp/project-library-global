---
title: "spec-client-billing"
doc-id: "mb-bc4cc414"
updated: "2026-11-12"
---
# Mybizz — Client Billing (Specification)

**Scope:** Mybizz-wide. Covers how every client pays its subscription, how the money and the tax flow, what App 5 does with each payment event, how a client that does not pay is handled, and Mybizz's cash flow per client. Applies to every Mybizz business.

---

## 1. Price and Terms

- £119 a month per client instance, before tax, charged at the fixed price for the client's currency: £119, $149, C$199, €139 or CHF 139 ([[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md)).
- The annual plan: 10 times the monthly price for 12 months, paid up front: £1,190, $1,490, C$1,990, €1,390 or CHF 1,390.
- Assisted setup: one month's price, once, as a separate one-off Paddle price.
- The terms (monthly or annual plan, billed in advance, cancel at any time with effect at the end of the paid month or year) and the referral credit are set in [[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md).
- Paddle sells the subscription as Merchant of Record ([[[default:adr-global/adr-client-billing-merchant-of-record|Client Billing Through a Merchant of Record]]](C:/dev/project-library-global/adr-global/adr-client-billing-merchant-of-record.md)).

---

## 2. Currency

- Mybizz's reference currency is the pound sterling (GBP). Mybizz's prices, revenue, margins and books are stated in GBP.
- Every supplier cost is stated in the currency the supplier bills: DigitalOcean, Anvil, Amazon Web Services and Groq bill in US dollars. Beside each dollar cost, the GBP figure is given at Mybizz's planning rate of **$1 = £0.75**. This planning rate is the only exchange rate used in Mybizz's documents.
- Paddle pays Mybizz out in GBP.

---

## 3. How a Client Pays

- Registration accepts only businesses based in Mybizz's markets: the United States, Canada, the United Kingdom, the European Union, the European Economic Area and Switzerland. Paddle's checkout is limited to the same countries.

1. At registration, the client chooses the monthly or the annual plan, and assisted setup if wanted, and pays the first month or the first year in Paddle's checkout. A client referred by an annual client enters that client's referral code at registration. Paddle's checkout collects the client's billing country and postal code, and optionally its business name and VAT or tax number, which Paddle validates.
2. Paddle adds the tax due in the client's country. A client with a valid business tax number pays no VAT where the reverse charge applies.
3. Paddle renews the subscription in advance, every month on the monthly plan or every year on the annual plan, on the same day, and emails the client its tax invoice for each payment.
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
| `transaction.completed` | Records the payment and the new `paid_until` date. If the client is suspended, unsuspends it (section 5). When the payment is a referred client's first annual payment, adds one referral credit to the referring client (section 4.1) |
| `adjustment.created` (a refund) | When the refund is of a referred client's first annual payment, removes the referral credit it earned (section 4.1) |
| `transaction.payment_failed` | Records `payment_failed_at`, the date of the first failed payment, if not already set |
| `subscription.past_due` | No action beyond recording; the timing of section 5 runs from `payment_failed_at` |
| `subscription.canceled` | When the client cancelled: runs the client exit at the end of the paid month or year. When the cancellation follows unpaid renewals: the timing of section 5 continues |

### 4.1 Referral Credits

- App 5 gives every client on the annual plan a referral code, shown on the client's subscription page.
- A new client that enters the code at registration and buys the annual plan earns the referring client one credit when its first annual payment completes.
- App 5 holds the credits in the client registry, at most 5 for the next renewal. A credit earned beyond 5 is recorded and not applied.
- After each change to a client's credits, App 5 sets a discount on the referring client's Paddle subscription for its next billing period only: one month's price for each credit. Paddle applies the discount at the renewal, and App 5 sets the credits back to zero when the renewal payment completes.
- A credit is never paid out in cash, and a client that leaves loses its credits.

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

- Every client pays in advance, for the month or the year ahead.
- DigitalOcean, Amazon SES and Groq charge Mybizz after use, by the second or by the item, on one bill at the end of each month. Mybizz pays only for the days a client's container and database exist.
- Each client's payment therefore reaches Mybizz before that client's costs fall due. Every client adds to Mybizz's cash from its first month.

### Per client

| Per client, per month, at £119 | GBP | Billed as |
|---|---|---|
| Subscription, before tax | £119.00 | |
| Paddle's fee (5% + $0.50) | −£6.33 | |
| Paid out to Mybizz | £112.67 | |
| Container (`apps-s-1vcpu-1gb`) | −£9.00 | $12.00 |
| Usage: email £1.00, AI writing and insight £0.50, speech to text £0.10, text to speech £5.00, data transfer over the allowance £1.00 | −£7.60 | |
| Left toward the database cluster and Mybizz's fixed costs | £96.07 | |

An annual-plan client pays £1,190 once a year, less Paddle's fee of £59.88, and leaves £77.58 a month toward the database cluster and Mybizz's fixed costs.

The usage figure budgets each client at medium-to-heavy use: a team of about six using email, AI and voice every working day.

**Highest cost of one client.** With every fair-use limit reached ([[[default:adr-global/adr-fair-use-limits]]](C:/dev/project-library-global/adr-global/adr-fair-use-limits.md)), one client costs at most £54.78 a month: container £18.75, email £3.75, AI and voice £16.80, data transfer £5.25, Paddle's fee £6.33 and a database share of £3.90. Each client's £119 covers this.

### Database cluster

The cluster is Advanced Edition with a standby from go-live: 8 GiB, £195 ($260) a month, to client 59; 16 GiB, about £390 ($520), from client 60; and 32 GiB, about £780 ($1,040), from client 130 ([[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 4).

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
| Marketing: paid search and social advertising, a budget allowance spent as results justify | £350.00 |
| **Total, to client 19** | **£586.49** |
| Part-time support, from client 20 | £1,000.00 |
| **Total, from client 20** | **£1,586.49** |
| **Total, from client 25** | **£1,653.16** |

### Totals by client count

Revenue is shown on the monthly plan.

| Clients | Revenue | Client-related costs | Fixed costs | Net profit |
|---|---|---|---|---|
| 1 | £119.00 | £217.93 | £586.49 | −£685.42 |
| 9 | £1,071.00 | £401.37 | £586.49 | £83.14 |
| 25 | £2,975.00 | £768.25 | £1,653.16 | £553.59 |
| 50 | £5,950.00 | £1,341.50 | £1,653.16 | £2,955.34 |
| 60 | £7,140.00 | £1,765.80 | £1,653.16 | £3,721.04 |
| 100 | £11,900.00 | £2,683.00 | £1,653.16 | £7,563.84 |

Client-related costs are the containers, the usage, Paddle's fees and the database cluster. **Break-even is 9 clients.** At 20 clients the gross profit covers the fixed costs and the part-time support, so Mybizz is profitable at every client number from break-even onwards.

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
