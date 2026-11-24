---
title: "adr-system-currency-selection-and-immutability"
doc-id: "mb-4b5f697c"
updated: "2026-11-24"
---
# System Currency and Local Currencies
Status: Accepted

**Applies to:** every Mybizz application. This ADR is the single standard for currency. Every other document states the same rule and links here.

---

## The rule

1. **System currency:** one system currency, set at onboarding, for books, reports and tax returns.
2. **Prices:** the client prices every product and service in the system currency.
3. **Choice:** the client sells in the system currency, or in a customer's local currency, market by market.
4. **Local currency:** the client sets the local price; the shop shows that price; Stripe or PayPal charges the price.
5. **Books:** each sale is recorded at the system-currency amount Stripe or PayPal pays in.
6. **Refunds:** paid in the currency the customer paid in, for the same amount.

---

## How the rule works

### System currency

- The Owner chooses the system currency in onboarding and confirms the choice. From confirmation, the system currency never changes.
- Stored in `business_profile.system_currency` as an ISO 4217 code.
- The client's books, accounts, reports, dashboard, tax figures and exports are all in the system currency.

### Local currencies, market by market

- Selling in the system currency is the default. Every customer pays in the system currency until the client turns on a local currency.
- The Owner or a Manager turns local currencies on and off on the Settings page of the dashboard, one local currency at a time, for one market: a currency and the countries that pay in that currency. Example: US dollars for the USA. US customers then pay in US dollars; every other customer still pays in the system currency.
- A country belongs to at most one local currency. A country with no local currency pays in the system currency.
- The client turns on the same currency in the client's own Stripe and PayPal accounts. PayPal is offered in a market only when the market's currency is a PayPal currency.
- Stored in the common table `local_currencies`, one row per local currency the client turns on.

### Local prices

- For each local currency, the client either types the local price of each product or service, or sets one rate of the client's own choosing; the application then works out each local price from the system price at that rate and rounds the price by the client's rounding rule. A typed local price always wins over the worked-out price.
- The rate is the client's pricing decision, not an exchange rate service. Mybizz uses no exchange rate service.
- Each application keeps typed local prices beside the priced item (for example `service_local_prices`, `variant_local_prices`), one row per item and local currency.

### The customer's currency

- The customer's country decides the customer's currency. The website shows a country selector, so a customer can change country; the prices then change to that country's currency.
- The customer sees, pays, receives invoices and receipts, and is refunded in that currency, at exactly the price shown.

### Payments and the books

- Stripe or PayPal charges the customer in the customer's currency, into the client's own account.
- Every payment and refund record holds two amounts:
  - `amount` and `currency`: what the customer paid or received back, in the customer's currency;
  - `system_amount`: what Stripe or PayPal paid into, or took out of, the client's account in the system currency, from the provider's own report of that payment.
- For a payment outside Stripe and PayPal (bank transfer, cash), the team member who records the payment enters the system-currency amount received.
- Every invoice is issued in the customer's currency. An invoice in a local currency also shows the tax total in the system currency, at the client's rate on the invoice date. The invoice's `system_amount` is the sum of the `system_amount` of the invoice's payments.
- Books, accounts reports, tax reports and the dashboard use `system_amount` only, so the books always match the bank.

### Refunds

- A refund is paid in the currency the customer paid in, for the same amount, through the provider that took the payment.
- The refund's `system_amount` comes from the provider's report of the refund. A difference between the payment's and the refund's `system_amount` is an exchange gain or loss in the client's accounts.

---

## Data

| Table | Columns |
|---|---|
| `business_profile` | `system_currency` (ISO 4217; fixed once confirmed in onboarding) |
| `local_currencies` | `currency` (ISO 4217), `country_codes` (list of ISO 3166-1 codes), `rate` (units of the local currency per 1 unit of the system currency, the client's own), `rounding` (`none` / `whole` / `ninety_nine`), `enabled` (bool) |
| priced items (per application) | the price in the system currency; local prices in the application's `{item}_local_prices` table |
| `invoice` | `currency` (the customer's currency), amounts in that currency, `system_amount` |
| `payments` | `currency` (the customer's currency), `amount`, `system_amount`, `gateway_fee` (in the system currency) |

All amounts are whole cents of the currency named on the record.

---

## Consequences

- The books always match what Stripe and PayPal pay into the client's account.
- The customer always pays exactly the price shown, in the currency shown.
- The client controls every local price; no exchange rate service, no conversion by Mybizz.
- A client cannot change the system currency after onboarding. A client that moves country opens a new account.

---

## Related Documents

- [[[default:adr-global/adr-timezone-utc-storage-display-conversion|Client Timezone: UTC Storage, Display Conversion]]](C:/dev/project-library-global/adr-global/adr-timezone-utc-storage-display-conversion.md)
- [[[default:specifications-global/spec-onboarding-implementation-plan|Onboarding System — Engineering Plan]]](C:/dev/project-library-global/specifications-global/spec-onboarding-implementation-plan.md)
- [[[default:specifications-global/spec-integration|Integration]]](C:/dev/project-library-global/specifications-global/spec-integration.md)
