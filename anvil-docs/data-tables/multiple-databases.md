---
title: "Using Multiple Databases"
url: "/docs/data-tables/multiple-databases"
---


# [Using Multiple Databases](#using-multiple-databases)

To use multiple databases in your app, upgrade to the [**Business Plan**](/pricing) or higher.

Each Anvil app can have multiple databases. You might want different [deployment environments](../deployment/environments) to use different databases – for example, so you can test your app without affecting production data. You can choose which database each environment uses. The tables in this database will be available via `anvil.tables.app_tables` in this environment.

## [Adding an additional database](#adding-an-additional-database)

To add an additional database to your Anvil app, open “Data” in the [Sidebar Menu](/docs/editor#sidebar-menu) and click “+ Add New Database”.

This will create a new database in your app with copies of the data tables from the default database. The data tables in the new database won’t contain any data.

## [Switching between databases in the editor](#switching-between-databases-in-the-editor)

To change which database your app uses when it runs in the Editor, click on the three dots next to the `+ Add Table` button of your desired database.

Then select `Use when debugging`. The selected database will now say ‘DEBUG’ to denote that the Editor is currently using that database.

## [Assigning databases to environments](#assigning-databases-to-environments)

To use your new database in an environment, click the **Publish** button in the top right of the editor.

This will open the Environments dialog.

Click “Advanced settings” and you will see a database section where you can select which database the environment should use.

## [Migrating databases](#migrating-databases)

A database schema contains information on the structure of a database i.e. what tables and columns a database should have. Each Anvil app has a database schema and when you load an app in the editor, Anvil checks to make sure the database the app is using matches the app’s database schema.

When you have multiple databases, they can fall out of sync. For example, if you add a new table to your development database, it will no longer match your app’s database schema.

The next time you begin using a database that is out of sync with the app’s schema, you will be prompted to resolve the schema mismatch.

Clicking the `Resolve` button in the prompt will open the database schema window. This will tell you how the [database schemas](https://www.ibm.com/think/topics/database-schema) don’t match and give you options to resolve the mismatch.

Modifying the [database the editor is currently using](#switching-between-databases-in-the-editor) will update the app’s database schema.
