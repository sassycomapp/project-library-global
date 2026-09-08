---
title: "Accessing an External Database"
url: "/docs/external-resources/external-database"
---


# [Accessing an external database](#accessing-an-external-database)

[Tutorial: Using an external database with Anvil](/learn/tutorials/external-database)

Because Anvil apps have a full Python instance in the back-end, you can use a database driver to access an external database from your [Server Modules](/docs/server).

## [MySQL](#mysql)

You can use a MySQL driver such as [Pymysql](https://pymysql.readthedocs.io/) to control your MySQL database server, as you would in any Python environment.

Here’s an example of querying a MySQL database from an Anvil server function:

```python
import pymysql

def connect():
  connection = pymysql.connect(host='db.example.com',
                               port=3306,
                               user='root',
                               password=anvil.secrets.get_secret('db_password'),
                               cursorclass=pymysql.cursors.DictCursor)
  return connection

@anvil.server.callable
def get_people():
  conn = connect()
  with conn.cursor() as cur:
    cur.execute("SELECT name,date_of_birth,score FROM users")
    return cur.fetchall()
```

And here’s how you’d use it in your Forms to display data with a [Data Grid](/docs/client/components/data-grids):

```python
class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

    self.repeating_panel_1.items = anvil.server.call('get_people')
```

*(Note 1: This example uses the [App Secrets service](/docs/security/encrypting-secret-data) to store your database password encrypted, rather than leaving it “in the clear” in your source code.)*

*(Note 2: This example uses `DictCursor` to return SELECT results as lists of dictionaries. This data format is easy to use with Anvil’s [Data Grids](/docs/client/components/data-grids).)*

## [PostgreSQL](#postgresql)

You can use a Postgres driver such as [`Psycopg2`](http://initd.org/psycopg/docs/usage.html) from a [Server Module](/docs/server) to control your Postgres database, as you would in any Python environment.

Here’s example code to query a Postgres database from an Anvil server function:

```python
import psycopg2
import psycopg2.extras

def connect():
  connection = psycopg2.connect(dbname='mydatabase',
                                host='db.example.com',
                                user='postgres',
                                password=anvil.secrets.get_secret('db_password'))
  return connection

@anvil.server.callable
def get_people():
  conn = connect()
  with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
    cur.execute("SELECT name,date_of_birth,score FROM users")
    return cur.fetchall()
```

And here’s how you’d use it in your Forms to display data with a [Data Grid](/docs/client/components/data-grids):

```python
class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

    self.repeating_panel_1.items = anvil.server.call('get_people')
```

*(Note 1: This example uses the [App Secrets service](/blog/app-secrets) to store your database password encrypted, rather than leaving it “in the clear” in your source code.)*

*(Note 2: This example uses `RealDictCursor` to return SELECT results as lists of dictionaries. This data format is easy to use with Anvil’s [Data Grids](/docs/client/components/data-grids).)*
