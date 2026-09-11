---
document: "Links Between Tables"
title: "Links Between Tables"
url: "/docs/data-tables/links-between-tables"
doc-id: links-between-tables
state: Live
date-created: 2026-09-08
---


# [Links Between Tables](#links-between-tables)

You can store a reference to one table in another table, using a link column. In this example, we have a `people` table, and a `notes` table containing notes about a person. The `notes` table has a “Person” column, which links to a row from the `people` table.

```python
# Get Jane Smith's row from the table
jane_smith = app_tables.people.get(Name="Jane Smith")

# Add a row to the 'notes' table, referencing her
n = app_tables.notes.add_row(Person=jane_smith,
                             Text="Jane is a good kid")

# Print the name of the person this note is linked to
# (prints "Jane Smith")
print(n["Person"]["Name"])

# Search by reference to a row. Eg,
# How many notes do we have about Jane?
jane_notes = app_tables.notes.search(Person=jane_smith)
print(f"There are {len(jane_notes)} notes about Jane.")
```

Once we have a row object representing Jane Smith’s row in the `people` table, we can add a new row to the `notes` table that refers to her, by passing that row object into `add_row()`. We can also search for all notes that refer to this person, by passing her row object into `search()`.

Note that we use the `len()` function here - `len()` runs very efficiently over search iterators.

## [Link to multiple rows](#link-to-multiple-rows)

You can also create columns that link to multiple rows from another table. In this example, the “Friends” column links to multiple rows from the “People” table. We set it to a list of row objects.

```python
jane_smith = app_tables.people.get(Name="Jane Smith")
john_smith = app_tables.people.get(Name="John Smith")
zaphod = app_tables.people.get(Name="Zaphod Beeblebrox")

zaphod["Friends"] = [jane_smith, john_smith]
```

You can search using a “link to multiple rows” column. If you pass a list of row objects to `search()`, it will return only rows that link to all of those rows. (If you specify multiple rows, the order doesn’t matter - it matches anything that links to all of them.)

```python
friends_of_jane = app_tables.people.search(Friends=[jane_smith])

mutual_friends = app_tables.people.search(Friends=[jane_smith, john_smith])
```

## [Updating Multiple Links and Simple Objects](#updating-multiple-links-and-simple-objects)

Values in Multiple Link columns are represented as lists in Python. Lists from Simple Objects are also Python lists.

To add a new item to a Multiple Link or a Simple Object, use the `+=` operator.

```python
zaphod = app_tables.people.get(Name="Zaphod Beeblebrox")
ford_prefect = app_tables.people.get(Name="Ford Prefect")

zaphod["Friends"] += [ford_prefect]
```

Ensure the right-hand-side of the operation is a list, since the Multiple Link column behaves like a list.

This will work: `zaphod["Friends"] += [ford_prefect]`

This will raise an exception: `zaphod["Friends"] += ford_prefect`

Empty multiple link columns are `None` until they contain at least one element. To initialise a mulitple link column with one element, use:

`zaphod["Friends"] = [ford_prefect]`

To remove rows, remove the item from the list and re-assign it using the `=` operator.

```python
zaphod = app_tables.people.get(Name="Zaphod Beeblebrox")
ford_prefect = app_tables.people.get(Name="Ford Prefect")

zaphod["Friends"] = [r for r in zaphod['Friends'] if r != ford_prefect]
```

## [Deleting linked rows](#deleting-linked-rows)

When you delete a row that is referenced by a single-link column, you can configure what happens to that link.

To configure this behaviour, click on the next to a link column, then select **‘Edit column’**.

On-delete behaviours are available only for tables using [Faster Storage](/docs/data-tables/faster-storage). Legacy tables do not support configurable on-delete behaviours.

### On-delete behaviours

When configuring a link column that references a single row, you can choose from three on-delete behaviours:

-   **Set to None**: When the referenced row is deleted, the link is cleared automatically by setting the column value to `None`.
-   **Cascade Delete**: When the referenced row is deleted, any row containing the link is also deleted. This is useful when child rows should not exist without their parent.
-   **Restrict**: Deleting a referenced row is prevented while it is still being referenced by another row. Attempting to delete the row raises an exception until those references have been removed.
