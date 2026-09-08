---
title: "SQL Access"
url: "/docs/data-tables/sql-access"
---


# [Direct SQL Access](#direct-sql-access)

Direct SQL access to your Anvil Data Tables is available only on the [Production Plan](/docs/plans-and-accounts/free-vs-paid#production-plan) or [Enterprise deployments](/docs/overview/enterprise). Users on any plan can still connect to external SQL databases. See [here](/docs/data-tables/external-database) for more details.

## [SQL queries on your Data Tables](#sql-queries-on-your-data-tables)

Developers more familiar with traditional database systems may prefer to access their data using SQL (a specialised database query language).

Users on the Production or [Enterprise](/docs/overview/enterprise) plans can access the data in their Data Tables using SQL. Anvil Data Tables are stored in PostgreSQL, and by connecting directly to the Postgres server, apps can get access to *writeable views* of these tables through SQL.

To connect to your database, call `anvil.tables.get_connection_string()` to get a Postgres connection string you can use with `psycopg2`, the Python module for connecting to Postgres.

For example, if your app has a Data Table called `users`:

```python
import psycopg2
import anvil.tables

conn = psycopg2.connect(anvil.tables.get_connection_string())
with conn.cursor() as cur:
    cur.execute("SELECT * FROM users")
    all_users = list(cur)
```

### Schema Layout

Anvil automatically creates a Postgres schema for each application environment, with views on all the Data Tables to which this application has access. These views may be read-only, depending on this app’s [server permissions](data-security) on that table. The connection string returned by `get_connection_string()` sets up the Postgres search path so that bare relation names (eg `users` in the example above) are resolved in this schema.

Within this schema, table views have the same name as the Python identifier for the table. So, if you access your table from Python as `app_tables.my_table`, you can access it from SQL with `SELECT * FROM my_table`.

### Security

The connection string returned by `get_connection_string()` contains temporary, expiring credentials for logging into the Postgres database, as a user which only has access to tables in this app’s environment. Don’t save and re-use the connection string. If you need to log into the database again at a later time, call `get_connection_string()` again to get a fresh set of temporary credentials, then use them immediately.

By default, your [Extra Server Resource](https://anvil.works/docs/overview/free-vs-paid#extra-server-resources) database is behind a firewall, and only accessible from your app’s Server Modules.

### Connecting from outside Anvil

If you do want to connect directly to your database from outside Anvil, you will need:

1.  An SSH tunnel, to get through the firewall and ensure your connection is strongly encrypted. (Contact `support@anvil.works` for help getting this set up.)

2.  An [Uplink](/docs/uplink) connection, to call `get_connection_string()` and obtain temporary credentials.

Once you have set up your SSH tunnel, you will need to connect to the hostname and port corresponding to your SSH tunnel, rather than the underlying Anvil database. To do this, pass the `via_host=` and `via_port=` arguments to `get_connection_string()`.

For example, if your SSH tunnel is running on `localhost` port `5433`:

```python
conn = psycopg2.connect(
    anvil.tables.get_connection_string(
        via_host="localhost",
        via_port=5433
    )
)
```

## [View Structure](#view-structure)

Every row in these views has an `_id` column, which is a unique identifier for the row. Columns that link to other tables show the ID of the linked row, so you can use standard `JOIN` queries if you wish.

Assuming your app has write access to the table, these views are writeable, meaning you can update the data in your tables in the usual way with `INSERT`, `UPDATE` and `DELETE` queries. Note that you cannot update Media objects or links between tables via SQL right now - you must use the [Python APIs](/docs/data-tables/data-tables-in-code) for that.

In order to prevent malformed queries from harming performance or security for other users, we do not permit users to execute SQL queries against data tables for apps hosted on our shared hosting plans. For that ability, consider upgrading to a Production plan.

If you are used to using SQL, there are three options available:

1.  **Use our [Python APIs](/docs/data-tables/data-tables-in-code).** It is often sufficient to use Python list comprehensions instead of complicated `SELECT` statements.

2.  **Connect to an [existing, external database](/docs/data-tables/external-database).** Anvil’s [self-service package installation](https://anvil.works/docs/server/custom-packages) (available with the Python 3.10 server environment) allows you to install and manage Python libraries, including those required for connecting to popular databases such as PostgreSQL, MySQL, MongoDB, Microsoft SQL Server, and Oracle. If you need help installing a driver for an external database, please email [contact@anvil.works](mailto:contact@anvil.works).

3.  **Purchase a Production Plan or Enterprise installation of Anvil.** With a Production Plan or a private installation, you will receive full SQL access to all of your data tables. Please email [sales@anvil.works](mailto:sales@anvil.works) for more details.
