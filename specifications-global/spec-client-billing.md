---
title: "spec-client-billing"
doc-id: "mb-bc4cc414"
updated: "2026-11-10"
---
# Mybizz — Client Billing (Specification)

**Scope:** Mybizz-wide. Covers how every client pays its subscription, how the money and the tax flow, what App 5 does with each payment event, how a client that does not pay is handled, and Mybizz's cash flow per client. Applies to every Mybizz business.

---

## 1. Price and Terms

- $99 a month per client instance, before tax. The terms (month to month, billed monthly in advance, cancel at any time with effect at the end of the paid month) are set in [[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md).
- Paddle sells the subscription as Merchant of Record ([[[default:adr-global/adr-client-billing-merchant-of-record|Client Billing Through a Merchant of Record]]](C:/dev/project-library-global/adr-global/adr-client-billing-merchant-of-record.md)).

---

## 2. How a Client Pays

1. At registration, the client pays the first month in Paddle's checkout. Paddle's checkout collects the client's billing country and postal code, and optionally its business name and VAT or tax number, which Paddle validates.
2. Paddle adds the tax due in the client's country. A client with a valid business tax number pays no VAT where the reverse charge applies.
3. Paddle renews the subscription every month, in advance, on the same day of the month, and emails the client its tax invoice for each payment.
4. The client changes its card, downloads its invoices and cancels through Paddle's customer portal, reached from a link in every Paddle email.
5. Paddle pays Mybizz once a month: the subscriptions collected, less Paddle's fee (5% + $0.50 per payment) and the tax. Each payout comes with Paddle's statement of every payment in it.

---

## 3. Paddle Notifications to App 5

Paddle sends a notification to App 5 for every billing event. App 5 receives them at its HTTP endpoint `/_/api/paddle`.

- App 5 checks each notification's `Paddle-Signature` header against Paddle's notification secret before it acts. A notification that fails the check is rejected and logged.
- Every accepted notification is stored as received in Mybizz's R2 bucket, in the folder `paddle/YYYY-MM/`, before App 5 acts on it. The stored notifications are Mybizz's record of every billing event.
- Paddle's notification secret and the R2 token are held in App 5's Vault.

| Paddle notification | What App 5 does |
|---|---|
| `subscription.activated` | Records the client's Paddle customer and subscription IDs in the client registry and sets `subscription_status` to active. Provisioning starts ([[[default:specifications-global/spec-client-activation-runbook\|Client Instance Activation Runbook]]](C:/dev/project-library-global/specifications-global/spec-client-activation-runbook.md)) |
| `transaction.completed` | Records the payment and the new `paid_until` date. If the client is suspended, unsuspends it (section 4) |
| `transaction.payment_failed` | Records `payment_failed_at`, the date of the first failed payment, if not already set |
| `subscription.past_due` | No action beyond recording; the timing of section 4 runs from `payment_failed_at` |
| `subscription.canceled` | When the client cancelled: runs the client exit at the end of the paid month. When the cancellation follows unpaid renewals: the timing of section 4 continues |

Mybizz's R2 bucket is in Mybizz's own Cloudflare account and is used only by App 5. It is separate from every client's R2 bucket, which sits in the client's own Cloudflare account.

---

## 4. A Client That Does Not Pay

App 5 counts the days from `payment_failed_at`. Paddle's payment recovery retries the payment and emails the client throughout.

| Day | What happens |
|---|---|
| 0 | A renewal payment fails. The client keeps full service |
| 7 | If still unpaid, App 5 suspends the client instance through `/management/suspend` ([[[default:adr-global/adr-mybizz-management-visibility\|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md)). Every page of the instance shows that payment is needed, with the link to Paddle's customer portal. The container and the database keep running, and no data is touched |
| Any day up to 37 | A completed payment clears `payment_failed_at`. App 5 unsuspends the instance through `/management/unsuspend`, and the client is back at once |
| 37 | If still unpaid, App 5 cancels the Paddle subscription, if Paddle has not already cancelled it, and runs the client exit ([[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 8) |

- **Data is never withheld.** The client owns its data. Every night, the client's data is copied into the client's own R2 bucket, in the client's own Cloudflare account, and the exit export writes the full data there too. A missed payment stops the service, never the client's access to its data.
- **An unpaid balance is never carried forward.** Billing is in advance, so every day of service up to the failed payment is paid for. A client that leaves owes nothing further to Mybizz.
- **The most Mybizz can lose on one client** is the hosting cost of the 37 days between the failed payment and the exit: about $15 for the container and up to $4 for the client's share of the database cluster.

---

## 5. Cash Flow

- Every client pays in advance, for the month ahead.
- DigitalOcean, Amazon SES and Groq charge Mybizz after use, by the second or by the item, on one bill at the end of each month. Mybizz pays only for the days a client's container and database exist.
- Each client's payment therefore reaches Mybizz before that client's costs fall due. Every client adds to Mybizz's cash from its first month.

| Per client, per month | Amount |
|---|---|
| Subscription, before tax | $99.00 |
| Paddle's fee (5% + $0.50) | −$5.45 |
| Paid out to Mybizz | $93.55 |
| Container (`apps-s-1vcpu-1gb`) | −$12.00 |
| Share of the database cluster | −$1 to −$4 |
| Left before Mybizz's fixed costs | $77.55 to $80.55 |

Mybizz's fixed costs and the totals by client count are in [[[default:specifications-global/spec-client-instance-hosting|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) section 11.

---

## 6. Mybizz's Own Books

- App 5 has no accounting module. Paddle is Mybizz's only customer for subscriptions, and Paddle carries all client tax.
- Mybizz's books are kept by its accountant from Paddle's monthly payout statements and the supplier bills (Anvil, DigitalOcean, Amazon Web Services, Groq and Paddle).

---

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-client-billing-merchant-of-record\|Client Billing Through a Merchant of Record]]](C:/dev/project-library-global/adr-global/adr-client-billing-merchant-of-record.md) | Why Paddle sells the subscription |
| [[[default:adr-global/adr-tiers-model\|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) | The price and the subscription terms |
| [[[default:adr-global/adr-mybizz-management-visibility\|Mybizz Management Visibility]]](C:/dev/project-library-global/adr-global/adr-mybizz-management-visibility.md) | The suspend and unsuspend endpoints and the client registry |
| [[[default:specifications-global/spec-client-instance-hosting\|Client Instance Hosting]]](C:/dev/project-library-global/specifications-global/spec-client-instance-hosting.md) | Client exit and the monthly cost |
| [[[default:adr-global/adr-client-r2-storage-and-exit-handover\|Client R2 Storage and Exit Handover]]](C:/dev/project-library-global/adr-global/adr-client-r2-storage-and-exit-handover.md) | The client's own R2 bucket and the exit export |
