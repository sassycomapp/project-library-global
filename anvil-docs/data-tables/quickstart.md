---
title: "Quickstart"
url: "/docs/data-tables/quickstart"
doc-id: data-tables-quickstart
state: Live
date-created: 2026-09-08
---


# [Quickstart: Databases](#quickstart-databases)

### Learn how to store data in Anvil’s hosted database system

Anvil provides a robust Python-based database system built on top of PostgreSQL.

Follow this quickstart to create a data table in your app’s default database, get your app to store data in it, and read the data back.

## [Create an app](#create-an-app)

Log in to Anvil and click ‘New Blank App’. Choose the Material Design theme.

## [Create a table](#create-a-table)

Navigate to “Data” in the [Sidebar Menu](/docs/editor#sidebar-menu) and click “+ Add Table”.

Change the name to be `square_numbers`.

## [Add columns](#add-columns)

Click New Column, and in the menu that pops up, name the new column `base_number`. Change the Column Type to “Number”.

Then add another Number column named `squared`.

## [Make the table client-writable](#make-the-table-client-writable)

In the bar above the columns, there are some controls relating to this table.

Use the dropdown menu that says ‘Client code’ to select ‘Client code can search, edit and delete’. This gives our client-side Forms [permission](data-security) to read from and write to this table.

Client-side code permission is set to ‘No access’ by default because Anvil applies [security best-practice by default](../security). Click the ‘more info’ link in that dropdown menu to read more about this.

## [Write to the database from Python code](#write-to-the-database-from-python-code)

Under Forms in the App Browser, select Form1.

Click on the ‘Code’ tab to see the Python code for `Form1`.

You will see a few lines of pre-written code. Your Form is represented as a class called Form1. It currently has only one method, the `__init__` method.

At the top of the file, import the `random` module:

```python
import random
```

And at the end of the `__init__` method, write these lines:

```python
base_number = random.randint(1, 100)
app_tables.square_numbers.add_row(base_number=base_number, squared=base_number**2)
```

## [Run your app](#run-your-app)

Now click the ‘Run’ button at the top of the screen.

Stop the app and look back at the Data service. Your table now contains some data.

Run your app a few times to get some more data in the database.

## [Read from the database](#read-from-the-database)

Go back to the Code View for Form1 and add these lines to the end of the `__init__` method:

```python
for row in app_tables.square_numbers.search():
  print(f"{row['base_number']} squared is {row['squared']}")
```

Run your app again and you’ll get the contents of your table printed to the App Console.

## [Copy the example app](#copy-the-example-app)

Click on the button below to clone a finished version of this app into your account.

[Open in Anvil](https://anvil.works/build?l=clone-link#clone:CLNLJTIX2M33VTTR%3dWLSEB4LIE447QMOVVNNO5ZDU)

## [Next up](#next-up)

### Want more depth on this subject?

Read more about [databases](/docs/data-tables).

### Want another quickstart?

Every quickstart is on the [Quickstarts](/docs/overview/quickstarts) page.
