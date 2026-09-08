---
title: "anvil.tables"
url: "/docs/api/anvil.tables"
---


## `anvil.tables` Module

#### Classes

[`Row`](#Row) [`SearchIterator`](#SearchIterator) [`Table`](#Table) [`Transaction`](#Transaction)

#### Functions

[`get_connection_string`](#get_connection_string) [`get_table_by_id`](#get_table_by_id) [`in_transaction`](#in_transaction) [`order_by`](#order_by)

#### Globals

[`app_tables`](#app_tables)

#### Exceptions

[`NoSuchColumnError`](#NoSuchColumnError) [`QuotaExceededError`](#QuotaExceededError) [`RowDeleted`](#RowDeleted) [`TableError`](#TableError) [`TransactionConflict`](#TransactionConflict)

## Classes

### `Row`

A table row

#### Instance Methods

**delete()** — Delete the row from its data table

**get_id() → id** — Get the unique ID of the table row

**update(**column_values)** — update the data for multiple columns

---

### `SearchIterator`

An iterator of table rows returned from a search()

#### Instance Methods

**to_csv([escape_for_excel=False]) → Media object** — Get the results of the SearchIterator in CSV format, optionally escaped for use in Excel. Returns a downloadable Media object; use its url property.

---

### `Table`

A table returned from app_tables

#### Instance Methods

**add_row(**column_values) → table row** — Add a row to the data table. Use keyword arguments to specify column values.

**client_readable() → client readable view** — Return a view on the table that can be read by client code. Use keyword arguments to specify view restrictions

**client_writable() → client writable view** — Return a view on the table that can be written by client code. Use keyword arguments to specify view restrictions. This does not give the client write access to other tables referred to by the table.

**client_writable_cascade() → client writable view** — Return a view on this table that can be written by client code. Use keyword arguments to specify view restrictions.

**delete_all_rows()** — Delete all the rows from the data table

**get()** — Get a single matching row from the data table whose columns match the keyword arguments. Returns None if no matching row exists, and raises an exception if more than one row matches. Eg: app_tables.table_1.get(name='John Smith')

**get_by_id(id) → row** — Get the matching row from this data table, by its unique ID

**has_row(row) → bool** — Returns true if the table (or view) contains the provided row.

**list_columns() → list of dicts** — Get the spec for the table as a list of dicts. Each dict contains the name and type of a column.

**search() → Row or None** — Get rows from a data table. If you specify keyword arguments, you will retrieve only rows whose columns match those values. Eg: app_tables.table_1.search(name='John Smith')

**to_csv([escape_for_excel=False]) → Media object** — Get the table in CSV format, optionally escaped for use in Excel. Returns a downloadable Media object; use its url property.

---

### `Transaction`

Create a new 'Transaction' object

#### Constructor

`Transaction()`

#### Instance Methods

**__enter__() → anvil.tables.Transaction instance** — Begin the transaction

**__exit__()** — End the transaction

**abort()** — Abort this transaction. When it ends, all write operations performed during it will be cancelled

---

## Functions

#### `get_connection_string([via_host=], [via_port=])`

Get a Postgres connection string for accessing this app's Data Tables via SQL.

The returned string includes temporary login credentials and sets the search path to a schema representing this app's Data Table environment.

You can override the host and port for the database connection to connect via a secure tunnel.

(Available on the Dedicated Plan only.)

---

#### `get_table_by_id(table_id) → anvil.tables.Table` [(more info)](/docs/data-tables/accelerated-tables)

Get a table by id. Can pass a row id in, and the table the row belongs to will be returned.

---

#### `in_transaction(function, server_function)` [(more info)](/docs/data-tables/transactions)

When applied to a function (as a decorator), the whole function will run in a data tables transaction. If it conflicts with another transaction, it will retry up to five times.

---

#### `order_by(column_name, ascending=)`

Sort the results of this table search by a particular column. Default to ascending order.

---

## Globals

#### `app_tables` [(more info)](/docs/data-tables/data-tables-in-code)

Access Table objects from the datatables services. You can access a Table object with dot notation e.g. `app_tables.my_table`. To access a table with strings use `getattr(app_tables, 'my_table')`. If no table is present an AttributeError will be thrown.

---

## Exceptions

#### `NoSuchColumnError`

Raised when attempting to access a column that does not exist in this table.

#### `QuotaExceededError`

Raised when an app has exceeded its quota.

#### `RowDeleted`

Raised when attempting to accessing a table row that has been deleted - for example, accessing a row after calling its delete() method, or following a link to a deleted row.

#### `TableError`

Superclass of all table exceptions

#### `TransactionConflict`

Raised when a transaction conflicts and has been aborted.
