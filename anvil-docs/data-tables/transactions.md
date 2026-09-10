---
title: "Transactions"
url: "/docs/data-tables/transactions"
doc-id: transactions
state: Live
date-created: 2026-09-08
---


# [Transactions](#transactions)

If multiple users are accessing data at the same time, you might want to place your data table operations in a *transaction*. This ensures your Data Table operations are carried out as a group.

If multiple transactions are taking place at once, Anvil ensures each transaction’s Data Tables operations are completed together. From the Data Table’s perspective, it’s as if every transaction block is executing one after another.

If an exception is raised before the transaction is complete, all changes are discarded. If two transactions *conflict* - that is, they’ve written to the same row of a Data Table, or one transaction writes into a row another is reading from - one or both of them will be aborted.

Transactions are only available from server code ([Server Modules](/docs/server) and the [Uplink](/docs/uplink)).

Database expert note: Anvil provides full serialisable transaction isolation by default.

## [Using a decorator](#using-a-decorator)

The easiest way to perform operations in a transaction is to call a function decorated with `@anvil.tables.in_transaction`. If an `@anvil.tables.in_transaction` function aborts due to conflict, it will try again (after a short timeout) up to 5 times before throwing an exception.

```python
# Server code only
import anvil.tables

@anvil.server.callable
@anvil.tables.in_transaction
def do_update():
  jane_smith = app_tables.people.get(Name="Jane Smith")
  jane_smith['age'] = 21
  app_tables.notes.add(Person=jane_smith,
                       Text="She's old enough to fly an aeroplane.")
```

You can specify `@anvil.tables.in_transaction` after `@anvil.server.callable` to make a [callable server function](/docs/server#calling-server-functions-from-client-code) transactional. Make sure to specify `@anvil.tables.in_transaction` *after* `@anvil.server.callable`. Python applies function decorators from “inside” to “outside”, and you want the `in_transaction` decorator applied *before* you make the function callable.)

## [In a context manager](#in-a-context-manager)

You can also create transactions by creating a `with anvil.tables.Transaction():` block. This will *not* automatically retry conflicting transactions: If a transaction is aborted because of a conflict, a `tables.TransactionConflict` exception is thrown. You can also abort a transaction manually by calling `.abort()` on a transaction.

```python
import anvil.tables

with anvil.tables.Transaction() as txn:
  jane_smith = app_tables.people.get(Name="Jane Smith")
  jane_smith['age'] += 10
```

If you observe a `TransactionConflict`, it is generally safe to retry. You could write a loop that detects a conflict and tries again, but this is such a common pattern that it is usually preferable to use `@anvil.tables.in_transaction` (which retries the transaction automatically, up to 5 times, before throwing the `TransactionConflict` as normal.)

## [Relaxed transactions](#relaxed-transactions)

By default, Anvil provides fully serialisable transactions. These ensure that the database effects of your transactions are as if they occurred one after another, rather than concurrently. This makes it much easier to reason about, but the conservative bookkeeping required can result in *false aborts*, where a transaction is aborted even though it hasn’t conflicted with anything else.

If false aborts are causing performance issues in your application, you might be able to increase throughput with *relaxed transactions*, which omit the most conservative checks.

Using relaxed transactions can cause subtle and hard-to-debug correctness issues that only appear under load. If in doubt, don’t use them.

The difference between normal and relaxed transactions is that relaxed transactions do not detect conflicts with search queries. For example, the following code is **not safe** with relaxed transactions:

```python
@tables.in_transaction
def get_or_create_row(name):
    row = app_tables.people.get(name=name)
    if row is None:
        row = app_tables.people.add_row(name=name)
    return row
```

This is because, if a concurrent operation creates a row with the specified `name` in between the calls to `get()` and to `add_row()`, the relaxed transaction scheme will not detect it, and you will end up with two duplicate rows with the same value for the `name` column.

By contrast, conflicts between specific rows that are read or written during the transaction will be detected. The only conflicts that won’t be detected are changes that *would have* caused a row to match a search query.

For experienced database users, Anvil’s relaxed transactions have the semantics of SQL’s `REPEATABLE READ`, whereas normal transactions are `SERIALIZABLE`.

To use a relaxed transaction, add the argument `relaxed=True` to the `in_transaction` decorator or the `Transaction()` constructor:

```python
@tables.in_transaction(relaxed=True)
def foo():
    # This code will execute in a relaxed transaction
    # (with automatic retries)
```

```python
with tables.Transaction(relaxed=True):
    # This code will also execute in a relaxed transaction
    # (without automatic retries)
```
