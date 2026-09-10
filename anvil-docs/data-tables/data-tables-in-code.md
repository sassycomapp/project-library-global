---
title: "Using Data Tables from Python"
url: "/docs/data-tables/data-tables-in-code"
doc-id: data-tables-in-code
state: Live
date-created: 2026-09-08
---


# [Using Data Tables from Python](#using-data-tables-from-python)

Anvil represents Data Tables in code as Python objects. You can imagine a Data Table in Python as a list of dictionaries, although they have many extra methods as described on this page, and they have caching and lazy loading for efficiency.

Client-side code can access Data Tables in this way, if you [give it permission](data-security) to do so. This allows you to use one representation for your data from the database all the way to the UI.

## [Python Names](#python-names)

Each table has a **Python name** that you use to reference it in your code. By default, this matches the table’s title and updates automatically when you rename the table. To set a different Python name independent of the table’s title, click the Python name in the top right of the data table window in the IDE and edit it directly.

When you delete an app, all its tables will be deleted as well (if no other apps are using it).

## [Accessing tables](#accessing-tables)

Your app’s Data Tables are accessible in code through the `app_tables` module, which you can import in both [Client](/docs/client) and [Server](/docs/server) code like so:

```python
from anvil.tables import app_tables
```

If you have [auto-import services enabled](/docs/editor/look-and-feel#auto-import-services), this line of code will be automatically added to the top of your Forms and Server Modules, as long as you have a Data Table created in your app.

You can then access a Table object either through dot notation or square bracket notation.

```python
from anvil.tables import app_tables
my_table = app_tables.my_table
my_table = app_tables["my_table"]
# The two above lines of code are equivalent.
```

You can also call the Python `list` constructor on your app tables to return a list of the names of all Data Tables present in your app.

```python
from anvil.tables import app_tables
table_names = list(app_tables)
```

## [Column types](#column-types)

All columns of a data table have fixed types. You choose the column type when it is created or, if it does not already exist, when a value is first set from code using `add_row`. The available types are listed below, along with their corresponding python types.

-   **Text** - A Python `str`
-   **Number** - Any Python number
-   **True/False** - A Python boolean, `True` or `False`
-   **Date** - A Python `datetime.date`
-   **Date and Time** - A Python `datetime.datetime`
-   **Simple Object** - Can hold Python strings, numbers (not NaN), dicts or lists
-   **Media** - Binary data (a [Media object](/docs/working-with-files/media))
-   **Link** - A row (or list of rows) from another table

You can list all the columns in a Data Table by calling `list_columns()` on the table object. This returns a list of dicts representing each column in your Data Table. Each dict contains a `name` and `type` key. For example:

```python
# list_columns() returns a list of dicts, like this:
[
  {'type': 'liveObject', 'name': 'category'}, 
  {'type': 'string', 'name': 'content'}, 
  {'type': 'datetime', 'name': 'created'}, 
  {'type': 'media', 'name': 'image'}
]
```

## [Adding Data](#adding-data)

You can add a new row to a data table with the `add_row()` method. Use keyword arguments to specify the value for each column.

```python
from anvil.tables import app_tables

app_tables.people.add_row(name="Jane Smith",
                          age=7,
                          employed=False)
```

If you have enabled “Auto-create missing columns” in your app’s settings, naming a column that does not exist will create a new one with that name. Remember that in Python, `"Name"` and `"name"` are two different strings, and they will create two different columns if you mix them up.

Data Table rows cache their data. This cache doesn’t automatically update if other code modifies that table row. If you want to refresh the data in a row object, call `row.update()`. However, if you pass a data table row into a server function, and update it there, then its cache will be automatically updated (this makes things like “call a server function to apply changes to this table row” work).

## [Row Objects](#row-objects)

In Python, your table is represented by `Row` Objects. `Row` Objects behave like Python dictionaries. You can get, set and update values in Rows using square brackets.

The `add_row()` method returns a row object, which you can use to get or set column values:

```python
james_row = app_tables.people.add_row(name="James Smith")
james_row["age"] = 12
```

Using square brackets on `Row` objects reads and writes to the database, with built-in caching:

```python
zaphod_row = app_tables.people.get(name="Zaphod Beeblebrox")
print(f"Zaphod is currently {zaphod_row['age']} years old")

# It's Zaphod's birthday, update the database
zaphod_row['age'] += 1
```

## [Searching (querying) a Table](#searching-querying-a-table)

You can list the contents of a table with the `search()` method.

```python
for row in app_tables.people.search():
  print(f"{row['name']} is {row['age']} years old")
```

Use keyword arguments to search for a particular value in a particular column.

```python
people_called_dave = app_tables.people.search(name="Dave")
```

The return value is a `SearchIterator`, an iterator of Row objects. You can think of a `SearchIterator` like a list, and since the Row objects are like dictionaries, the whole structure behaves like a list of dictionaries.

```python
# It can be useful to imagine SearchIterators like this:
[
  {"name": "Dave", "age": 34},
  {"name": "James Smith", "age": 12},
  {"name": "Zaphod Beeblebrox", "age": 42},
]
```

### Getting values from a single column

You can use Python list comprehension to get the values from a particular column in your Data Table:

```python
# Get a list of values from the 'name' column of your 'people' Data Table:
names = [r['name'] for r in app_tables.people.search()]
```

### Getting values from several columns

To get the values from several columns in your Data Table, you can use a list comprehension to return a list of dictionaries with the desired values:

```python
info = [
  {
    'name': r['name'],
    'employed': r['employed'],
  }
  for r in app_tables.people.search()
]
```

### Query operators

Use the Query Operators from the `anvil.tables.query` module to perform more complex searches.

```python
import anvil.tables.query as q

people_over_50 = app_tables.people.search(age=q.greater_than(50))

from datetime import date
late_projects = app_tables.projects.search(
  Complete=False,
  Due_Date=q.less_than(date.today())
)
```

The following query functions are available (here’s the relevant [API Docs entry](/docs/api/anvil.tables.query)). These can only be used as values of keyword arguments to match column values:

-   **`between(*min*, *max*, [*min_inclusive*=True], [*max_inclusive*=False])`** - Match values between ***`min`*** and ***`max`***. By default, ***`min`*** is inclusive and ***`max`*** is exclusive. This can be changed by supplying alternative values as keyword arguments.

-   **`full_text_match(*pattern*, [*raw*=False])`** - By default, matches values which contain all the words in ***`pattern`***, ignoring the particular form of the word (e.g. ‘Walk’, ‘walk’, ‘walked’ and ‘walking’ will all match one another). For more control, set ***`raw`*** to `True`, then provide a full [PostgreSQL `tsquery` pattern](https://www.postgresql.org/docs/10/datatype-textsearch.html#DATATYPE-TSQUERY).

    The match function ignores ‘stop words’: certain words that appear commonly in text, and therefore usually cloud the results of a natural language search. If you need to search for a string containing stop words, consider using `like` or `ilike` instead. These are intended for a literal text match, whereas `full_text_match` is intended for a natural language query.

-   **`greater_than(*value*)`** - Matches any values greater than ***`value`***.

-   **`greater_than_or_equal_to(*value*)`** - Matches any values greater than or equal to ***`value`***.

-   **`ilike(*pattern*)`** - Provides case-insensitive string matching using the [PostgreSQL pattern-matching syntax](https://www.postgresql.org/docs/10/functions-matching.html#FUNCTIONS-LIKE).

-   **`less_than(*value*)`** - Matches any values less than ***`value`***.

-   **`less_than_or_equal_to(*value*)`** - Matches any values less than or equal to ***`value`***.

-   **`like(*pattern*)`** - Provides case-sensitive string matching using the [PostgreSQL pattern-matching syntax](https://www.postgresql.org/docs/10/functions-matching.html#FUNCTIONS-LIKE).

See [Querying Data Tables](/blog/querying-data-tables) for more examples.

### Combining query operators

The `any_of`, `all_of` and `none_of` functions let you build up arbitrary expressions. When used as values for keyword arguments, the arguments to these functions should also be values, as in the example below.

```python
# Find anyone called Dave or Brian
x = app_tables.people.search(name=q.any_of("Dave", "Brian"))

# Find anyone not called Steve or John
x = app_tables.people.search(name=q.none_of("Steve", "John"))
```

Alternatively, when used as positional arguments, the `any_of`, `all_of` and `none_of` functions allow you to build up arbitrarily complex nested search expressions.

```python
# Find anyone called Dave *or* 35 years old.
y = app_tables.people.search(q.any_of(name="Dave", age=35))

# Find anyone less than 20 or more than 30 years old
x = app_tables.people.search(
  age=q.any_of(q.less_than(20), q.greater_than(30))
)

# Find anyone who is 35 years old, or 34 and called Dave or Brian
z = app_tables.people.search(
  q.any_of(
    age=35,
    q.all_of(age=34, name=q.any_of("Dave", "Brian")),
  )
)
```

### Column-restricted views

You can control which columns are accessible from a [view](data-security#views), by passing `q.only_cols()`. For example, the following code will return a view of the `users` table that contains only the `email` and `enabled` columns:

```python
@anvil.server.callable
def get_users():
    return app_tables.users.client_readable(q.only_cols("email", "enabled"))
```

### Sorting and slicing

Use `tables.order_by()` to sort the rows returned. This takes the name of the column to sort by, and a keyword argument `ascending`, which defaults to `True`.

```python
oldest_first = app_tables.people.search(
  tables.order_by("age", ascending=False)
)
```

You can also use `tables.order_by()` to sort by multiple columns. This sorts by “name” in ascending order, and rows that have the same value for “name” will be sorted by “age” in descending order:

```python
oldest_first = app_tables.people.search(
  tables.order_by("name"),
  tables.order_by("age", ascending=False)
)
```

Slice a table search to return just a portion of the results.

```python
oldest_first = app_tables.people.search(
  tables.order_by("age", ascending=False)
)
ten_oldest = oldest_first[:10]
```

### Unpacking a dictionary

You can also search a table by unpacking a dictionary of arguments.

```python
kwargs = {'age': 42, 'employed': True}
filtered_table = app_tables.people.search(**kwargs)
```

This can be used in conjunction with a query operator.

```python
kwargs = {'age': 42, 'employed': True}
filtered_table = app_tables.people.search(q.any_of(**kwargs))
```

### Search is lazy

`search()` returns a *search object*, which is iterable - you can use it in a `for` loop or a list comprehension. If your search returns lots of results, Anvil only loads a few at a time.

You can call `len()` on a search object to efficiently find out how many rows it would return (without loading them all!).

```python
print(f"There are {len(app_tables.people.search())} people")
```

You can also access the returned rows by index. Because `search()` is sensibly lazy, it will only load as many results as is necessary to retrieve the value at a given index. If your search returns lots of results, Anvil only loads a few at a time.

```python
first_person = app_tables.people.search(tables.order_by("Name"))[0]

print(f"First alphabetical name: {first_person['name']}")
```

You can use Python’s normal sequence operations to work with search results.

```python
# Print the names of all the adults:

adult_names = " and ".join([p['name'] for p in app_tables.people.search(age=q.greater_than_or_equal_to(18))])

print(adult_names)
# ^^ Prints "Tom and Dick and Harry"
```

## [Searching Simple Objects](#searching-simple-objects)

You can think of a Simple Object column as storing a JSON object. A Simple Object column can store strings, numbers (not NaN), `None`, lists of any simple object, and dictionaries whose keys are strings and whose values are any simple object. (In other words, it’s the values that can be represented as JSON.)

You can search within Simple Objects using `search`:

```python
# This finds all rows where object_col is a
# dict and contains a key 'the_answer' with
# the value '42' - no matter what other keys
# are in the dict.
r = app_tables.my_table.search(object_col={'the_answer': 42})
```

When you search on a Simple Object column, you search by object specifying an object pattern. The rules are:

-   If you specify a dictionary, all specified keys must be present in the column, and all values must match the pattern specified in the dictionary.
-   If you specify a list, the object you’re matching must be a list, and it must contain elements matching all elements you specify. Order doesn’t matter, though, so if you specify `[1,3]` as your search you will match a column containing `[3,2,1]`.
-   If you specify a string, number or `None` (a “primitive value”), the object you’re matching must be exactly the same, **or** be a list containing that primitive value.

The Simple Object search semantics are derived directly from the Postgres [JSON containment](https://www.postgresql.org/docs/9.5/static/datatype-json.html#JSON-CONTAINMENT) rules.

## [Getting One Row from a Table](#getting-one-row-from-a-table)

Sometimes, you only want a single row. The `get()` method returns a single row that matches the arguments (which are the same as those for the `search` method), or `None` if no such row exists. If more than one row matches, it raises an exception.

```python
zaphod_row = app_tables.people.get(name="Zaphod Beeblebrox")
```

You can use this neat trick to fetch a row if it exists, or create a new one if it does not. Because `get()` returns `None` if a row does not exist, we use “short circuiting” of the `or` operator to make sure we only run the `add_row()` if no such row already exists.

```python
zaphod_row = (app_tables.people.get(name="Zaphod Beeblebrox")
               or app_tables.people.add_row(name="Zaphod Beeblebrox", age=42))
```

### Row IDs

Each row of each table has unique ID, which is a string. You can get the ID of any row, and use it to retrieve that row later.

```python
# 'jane_smith' is a Row object from the 'people' table
janes_id = jane_smith.get_id()

r = app_tables.people.get_by_id(janes_id)

# r and jane_smith are equal, as they both
# point to the same row.
# (jane_smith == r)
```

This is useful if you want to store a reference to a table row somewhere else (for example, in a file).

If you just want to refer to one row in a data table from another row in a data table, don’t mess with IDs – create [links between tables](links-between-tables) instead!

## [Updating and Deleting Rows](#updating-and-deleting-rows)

You can set new values for a row in the same way as you would update a Python dictionary. This updates the database, not just the data on the client side.

```python
jane_row = app_tables.people.get(name="Jane Smith"):
# Increase Jane Smith's age (from 7 to 8)
jane_row["age"] += 1
```

You can set the value of multiple columns at once by calling the `update()` method on a row. Again, this updates the database.

```python
# Set Jane Smith's age to 9 and her middle initial
jane_row.update(age=9, name="Jane E. Smith")
```

You can also delete a row by calling its `delete()` method. The row is removed from the database.

```python
# Remove Jane Smith from the table
jane_row = app_tables.people.get(name="Jane E. Smith"):
if jane_row is not None:
  jane_row.delete()
```

You can delete all rows in a table by calling the table’s `delete_all_rows()` method. All data is cleared from the database for this table!

```python
# Delete all rows in the table
app_tables.people.delete_all_rows()
```

## [Batch add, update and delete rows](#batch-add-update-and-delete-rows)

You can add, update and delete rows in batches, saving round trips to the database.

To [add](/docs/data-tables/data-tables-in-code#adding-data) multiple rows to a Data Table at once, you can pass a list of dictionaries to `add_rows()`:

```python
app_tables.my_table.add_rows([
    {'name': 'Ada', 'age': 36},
    {'name': 'Katherine', 'age': 101}
])
```

Use the `anvil.tables.batch_update` context handler to [update rows](/docs/data-tables/data-tables-in-code#updating-and-deleting-rows) in batches:

```python
ada_row = app_tables.my_table.get(name='Ada')
katherine_row = app_tables.my_table.get(name='Katherine')

with anvil.tables.batch_update:
    ada_row['name'] = 'Ada Lovelace'
    katherine_row['name'] = 'Katherine Johnson'
```

To [delete](/docs/data-tables/data-tables-in-code#updating-and-deleting-rows) multiple rows at once, you can use `delete_all_rows()` or the `anvil.tables.batch_delete` context handler:

```python
#using the context handler
rows = app_tables.my_table.search(name=None)

with anvil.tables.batch_delete:
    for row in rows:
        row.delete()
```

```python
#using delete_all_rows()
app_tables.my_table.search(name=None).delete_all_rows()
```

Combine batched updates and deletes with a batch context handler

```python
from anvil.tables import app_tables

rows = app_tables.my_table.search(status='old')

with anvil.tables.batch:
    for row in rows:
        # Archive high-priority old rows, delete the rest
        if row['priority'] == 'high':
            row['status'] = 'archived'
        else:
            row.delete()
```

## [Explicit cache control](#explicit-cache-control)

You can control which columns are loaded from a table search, using the `fetch_only` search modifier.

For example, if you are querying the `users` table, but only need the values of the `"email"` and `"enabled"` columns, you can write:

```python
from anvil.tables import query as q

rows = app_tables.users.search(q.fetch_only("email", "enabled"))
```

This will speed up the query, by only fetching the data you need. It is possible to access other columns in rows returned from this search, but it requires a round-trip to fetch that data from the database.

You can also control what data is fetched from linked rows, by using nested `fetch_only` specifications. For example, if your `users` table had a link column called `group`, and you only want the `"name"` column from those columns, you can write:

```python
rows = app_tables.users.search(q.fetch_only("email", group=q.fetch_only("name")))
```

You also have access to the `.fetch()` and `.refresh()` methods that take a `q.fetch_only()` argument.

```python
# explicitly fetch only the email and enabled columns
row.fetch(q.fetch_only("email", "enabled"))
```

In the above example, the `fetch()` method will only fetch the columns specified in the `q.fetch_only()` argument. Any other cached/uncached columns will remain cached/uncached. If you want to clear the cache and fetch values, you can call the `.refresh()` method.

```python
# refresh all columns - this will fetch all columns
row.refresh()

# refresh all columns and fetch specific columns
row.refresh(q.fetch_only("email", "enabled"))
```

## [CSV Export](#csv-export)

You can call `to_csv()` to obtain a downloadable [Media object](/docs/working-with-files/media) from any `search()`. You can access the `url` property of this Media Object to provide a link to download that data.

```python
self.link_1.url = app_tables.people.search().to_csv().url
```

You can also call `to_csv()` on [table views](data-security#views). This can be used to provide downloads of only certain columns of a data table. In this example, the `person` column will not be included in the download.

```python
janes_notes = app_tables.notes.client_readable(person=jane_smith)
self.link_1.url = janes_notes.search().to_csv().url
```
