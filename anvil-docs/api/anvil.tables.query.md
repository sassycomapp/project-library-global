---
document: "anvil.tables.query"
title: "anvil.tables.query"
url: "/docs/api/anvil.tables.query"
doc-id: anvil.tables.query
state: Live
date-created: 2026-09-08
---


## `anvil.tables.query` Module

#### Functions

[`all_of`](#all_of) [`any_of`](#any_of) [`between`](#between) [`fetch_only`](#fetch_only) [`full_text_match`](#full_text_match) [`greater_than`](#greater_than) [`greater_than_or_equal_to`](#greater_than_or_equal_to) [`ilike`](#ilike) [`less_than`](#less_than) [`less_than_or_equal_to`](#less_than_or_equal_to) [`like`](#like) [`none_of`](#none_of) [`not_`](#not_) [`only_cols`](#only_cols) [`page_size`](#page_size)

## Functions

#### `all_of(*query_expressions)`

Match all query parameters given as arguments and keyword arguments

#### `any_of(*query_expressions)`

Match any query parameters given as arguments and keyword arguments

#### `between(min, max, [min_inclusive=True], [max_inclusive=False])`

Match values between the provided min and max, optionally inclusive.

#### `fetch_only(*only_cols, **linked_cols)` [(more info)](/docs/data-tables/accelerated-tables#explicit-cache-control)

Control which columns are loaded from a table search to speed up queries by only fetching the data you need.

-   `only_cols` - Column names to fetch from the table. Example: fetch_only('email', group=q.fetch_only('name'))

-   `linked_cols` - Linked columns to fetch, specified as keyword arguments. Each value must be another fetch_only() object.

#### `full_text_match(query, [raw=False])`

Match values that match the provided full-text search query.

#### `greater_than(value)`

Match values greater than the provided value.

#### `greater_than_or_equal_to(value)`

Match values greater than or equal to the provided value.

#### `ilike(pattern)`

Match values using a case-insensitive ILIKE query, using the % wildcard character.

#### `less_than(value)`

Match values less than the provided value.

#### `less_than_or_equal_to(value)`

Match values less than or equal to the provided value.

#### `like(pattern)`

Match values using a case-sensitive LIKE query, using the % wildcard character.

#### `none_of(*query_expressions)`

Match none of the query parameters given as arguments and keyword arguments

#### `not_(*query_expressions)`

Match none of the query parameters given as arguments and keyword arguments

#### `only_cols(*cols)` [(more info)](/docs/data-tables/accelerated-tables#column-restricted-views)

Control which columns are accessible from a view, restricting access to specific columns.

-   `cols` - Column names to make accessible in the view. Example: only_cols('email', 'enabled')

#### `page_size(rows)`

Define the number of rows that are fetched per round trip to the server.
