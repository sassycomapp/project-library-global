---
title: "Storing Data in Data Tables"
url: "/docs/data-tables"
doc-id: data-tables-_index
state: Live
date-created: 2026-09-08
---

# [Storing Data in Data Tables](#storing-data-in-data-tables)

Every Anvil app comes with a built-in database. Each database stores tables of information for your Anvil app. It’s a full database system built on top of PostgreSQL.

If you’re not familiar with databases, it’s also similar to a spreadsheet - data is stored in tables with rows and columns.

To add a data table to your app’s Default database, open the database window from the [Sidebar Menu](/docs/editor#sidebar-menu). Then click `+ Add Table` button. Check the [Quickstart](data-tables/quickstart) to see how to get up and running.

[Quickstart: Data Tables](/docs/data-tables/quickstart)

## [Editing Data Tables in the Anvil Editor](#editing-data-tables-in-the-anvil-editor)

Each table contains columns and rows. Columns define the type of data you’re storing, while each row represents a single item. For example, in a table of people for an organisation, you might have columns for name, age, and employment status, with each row representing one person.

Each column can contain data of a particular type. For example, in the table above, *Name* is always a string, *Age* is always a number, and *Employed* is always a boolean value (either True or False). Any column can also be empty (`None` in Python).

Click to edit any data in the table (just like a spreadsheet). To add a new row, click the ‘+’ button at the bottom of the table, or click in the blank row, and start typing! You can add more columns with the ‘+’ button at the top right of the table.

To change a table’s title, double click on its name in the data tables list on the left.

## [Sharing Databases and Data Tables Between Apps](#sharing-databases-and-data-tables-between-apps)

You can add existing Data Tables and Databases from other apps in your account.

### Adding an Existing Table

To add an existing table to your app:

-   Click the three-dot menu on the database you want to add the table to, then select “Add Existing Table”.
-   In the dialog that appears, select the table you want to add.

### Adding an Existing Database

To add an existing database to your app:

-   Click the “+ Add Database” button and select “Add Existing Database”.
-   In the dialog that appears, select the database you want to add.

Adding an existing table or database does not create a copy. Instead, it creates a shared connection.

Changes made to a shared table will be visible in all databases that contain that table. Similarly, changes made to a shared database will be visible in all apps connected to it.

## [Downloading a Data Table as CSV](#downloading-a-data-table-as-csv)

To export a data table in CSV format, click the **Download** button in the Data Tables editor.

## [Using Data Tables from Python](#using-data-tables-from-python)

Add, search, update and delete rows, query, and export your Data Tables with Python.

## [Data Security](#data-security)

You can control which code can read or write each table, using permissions and views.

## [Static Data Files](#static-data-files)

Attach static files such as datasets or text files to your app and access them from your Server Module.

## [Links Between Tables](#links-between-tables)

You can store references to one table in another table, and traverse those relationships in Python.

## [Using Multiple Databases](#using-multiple-databases)

Add extra databases to your Anvil app and assign them to different deployment environments.

## [Transactions](#transactions)

You can group Data Table operations so they succeed or fail together, with automatic conflict retry.

## [Buffering Changes](#buffering-changes)

Use buffered changes to defer changes to the database until the `save()` method is called.

## [Model Classes](#model-classes)

Add extra logic directly to your table rows as Python classes.

## [Faster Storage](#faster-storage)

Use the new Faster storage engine for faster queries and better parallelism.

## [Indexes](#indexes)

Add indexes to speed up frequent queries on your Data Tables.

## [SQL Access](#sql-access)

Query your data tables directly with SQL.

## [CSV and Excel Import](#csv-and-excel-import)

Import data from CSV or Excel files into your Data Tables using Data Files or the Uplink.
