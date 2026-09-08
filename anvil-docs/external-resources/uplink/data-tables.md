---
title: "Connecting to Data Tables"
url: "/docs/external-resources/uplink/data-tables"
---


# [Connecting to Data Tables](#connecting-to-data-tables)

Once you have set up the Anvil Uplink, your local Python code can do anything a Server Module can do. This includes connecting to [Data Tables](/docs/data-tables) in your Anvil App from your own machine.

## [Accessing your Data Tables](#accessing-your-data-tables)

First, make sure you have [enabled the Uplink](/docs/uplink/setting_up#setting-up-the-uplink).

Say, for example, we have a Data Table called ‘people’. We’ll define a `get_people` server function to access data in this table, and mark it as `@anvil.server.callable`. Then, we’ll call this function from our local machine:

```python
# In a script on your own machine (or anywhere)

# Connect the Uplink
import anvil.server
anvil.server.connect("<your Uplink key>")

# import app_tables to access your data tables
from anvil.tables import app_tables

@anvil.server.callable
def get_people():
  people = app_tables.people.search()
  for p in people:
  	print(f"This person's name is {p['name']}")

# Call the server function
anvil.server.call('get_people')

anvil.server.wait_forever()
```

## [Querying your Data Tables](#querying-your-data-tables)

To use Anvil’s [Query Operators](/docs/data-tables/data-tables-in-code#searching-querying-a-table), just add this line at the top of your code:

```python
# In a script on your own machine (or anywhere)

import anvil.tables.query as q
```
