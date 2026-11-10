---
title: "adr-client-billing-merchant-of-record"
doc-id: "mb-9b20b385"
updated: "2026-11-10"
---
# Client Billing Through a Merchant of Record
Status: Accepted

---

## Context

Every Mybizz business sells its $99 monthly subscription to client businesses in many countries ([[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md)). Selling software across borders carries a tax duty in each buyer's country: VAT in the United Kingdom and the European Union, GST in Canada and Australia, and sales tax in many US states. A seller that collects the payments itself must register for tax in each place where it passes a threshold, file returns there, pay the tax over, and carry the liability in any audit.

Mybizz is a small company that sells one product at one price. The work and the liability of worldwide tax registration and filing would take time away from the product, and an error in any one country would fall on Mybizz.

Two ways of collecting the subscription are available:

- **A payment gateway with a tax engine** (Stripe with Stripe Tax and a filing service). Mybizz is the seller. Its own name appears on the bank statement and the invoice. Mybizz holds every tax registration, approves every return, pays the tax over and carries the audit liability. The cost is about 3.5% to 4.5% per payment, plus a fixed monthly fee for the filing service.
- **A Merchant of Record** (Paddle). Paddle buys the subscription from Mybizz and resells it to the client. Paddle is the seller in law, so Paddle holds every tax registration, files and pays every return, and carries the audit liability. Paddle's name appears on the client's bank statement and on the tax invoice. The cost is 5% + $0.50 per payment, with no fixed monthly fee.

---

## Decision

**Mybizz sells every client subscription through Paddle, as Merchant of Record.**

- Paddle's checkout takes the client's first payment and every monthly renewal, in advance.
- Paddle calculates, collects and pays over every sales tax, and issues the tax invoice to the client.
- Paddle pays Mybizz its revenue, net of Paddle's fee and the tax, once a month.
- The $99 price is set before tax. Each client pays its own country's tax on top. A business client that gives a valid VAT or tax number pays no VAT where the reverse charge applies.
- Every client sees Paddle's name on its bank statement (`PADDLE.NET * MYBIZZ`) and on its tax invoice, with Mybizz's product name and logo.

How billing runs, including failed payments, is set out in [[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md).

---

## Consequences

### Positive
- Mybizz holds no foreign tax registration, files no foreign tax return and carries no foreign tax audit liability.
- No fixed monthly cost: Paddle's fee is paid only when a client pays.
- Every client receives a tax invoice that is valid in its own country, with no invoicing work by Mybizz.
- Mybizz receives the same amount from every client, whatever the client's country, because the price is set before tax.

### Negative
- Paddle's name, not Mybizz's, appears on the client's bank statement and tax invoice.
- Paddle's fee, 5% + $0.50, is about $5.45 on each $99 payment, higher than a gateway's fee.
- Mybizz depends on Paddle's approval of its account and on Paddle's terms.

### Neutral
- The payment gateways each client uses for its own customers (Stripe, Paystack and PayPal) are unaffected. Paddle sells only Mybizz's subscription.

---

## Related Documents

- [[[default:specifications-global/spec-client-billing|Client Billing]]](C:/dev/project-library-global/specifications-global/spec-client-billing.md) — How billing runs
- [[[default:adr-global/adr-tiers-model|Tiers Model]]](C:/dev/project-library-global/adr-global/adr-tiers-model.md) — The price and the subscription terms
