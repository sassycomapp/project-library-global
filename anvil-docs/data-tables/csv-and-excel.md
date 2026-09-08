---
title: "CSV and Excel import"
url: "/docs/data-tables/csv-and-excel"
---


# [Importing data from CSV and Excel](#importing-data-from-csv-and-excel)

## [Using Data Files](#using-data-files)

The [Data Files](/docs/working-with-files/data-files) service makes it straightforward to import data from CSVs and Excel files into your Data Tables. The Data Files documentation shows you how to upload files to your Anvil app and interact with those files from Python code. Learn more here: [Anvil Docs | Data Files](/docs/working-with-files/data-files)

## [Using the Uplink](#using-the-uplink)

Instead of using [Data Files](/docs/working-with-files/data-files) to upload files to your app, you can use the [Uplink](/docs/uplink) to access your files locally. You can download our sample files here:

-   [colours.csv](img/import-data/colours.csv)
-   [colours.xlsx](img/import-data/colours.xlsx)

Create a new app, navigate to the [Data service](/docs/data-tables) and create a table.

Navigate to ‘Settings’ in the [Sidebar Menu](/docs/editor#sidebar-menu), and ensure that ‘Auto create missing columns’ is checked in the ‘Data Tables’ tab.

We’ll use the [`pandas`](https://pypi.org/project/pandas/) and [`xlrd`](https://pypi.org/project/xlrd/) libraries, so install these:

```python
pip install pandas
pip install xlrd
```

### Import from CSV

This Python script will import data from a CSV file to your Data Table:

```python
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables

def import_csv_data(file):
  with open(file, "r") as f:
    df = pd.read_csv(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.your_table_name_here.add_row(**d)
```

Make sure you change `your_table_name_here` to the name of the Data Table you just created!

### Import from Excel

This Python script will import data from an Excel file to your Data Table:

```python
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables

def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.your_table_name_here.add_row(**d)
```

Make sure you change `your_table_name_here` to the name of the Data Table you just created!

Next, install the Anvil Uplink library:

```python
pip install anvil-uplink
```

[Enable the Uplink](/docs/uplink/setting_up#enabling-the-uplink) in your app, and then paste the connection code into your script:

```python
# Add these lines underneath your import statements
import anvil.server
anvil.server.connect("YOUR-UPLINK-KEY")  # Make sure you replace this with your own Uplink key
```

### Run your scripts

Run your script, calling your functions and passing in the CSV or Excel files you want to import.

Stop your app, navigate to your Data Tables, and you’ll see your data has been imported.

### Example script

Here’s an example script that uploads both `colours.csv` and `colours.xlsx` to an Anvil Data Table:

```python
import pandas as pd
import anvil.tables as tables
from anvil.tables import app_tables

import anvil.server
anvil.server.connect("YOUR-UPLINK-KEY")  # Make sure you replace this with your own Uplink key

def import_csv_data(file):
  with open(file, "r") as f:
    df = pd.read_csv(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.your_table_name_here.add_row(**d)

def import_excel_data(file):
  with open(file, "rb") as f:
    df = pd.read_excel(f)
    for d in df.to_dict(orient="records"):
      # d is now a dict of {columnname -> value} for this row
      # We use Python's **kwargs syntax to pass the whole dict as
      # keyword arguments
      app_tables.your_table_name_here.add_row(**d)

import_csv_data("colours.csv")
import_excel_data("colours.xlsx")
```
