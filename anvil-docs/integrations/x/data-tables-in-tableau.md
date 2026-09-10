---
title: "Using Data Tables from Tableau"
url: "/docs/integrations/x/data-tables-in-tableau"
doc-id: data-tables-in-tableau
state: Live
date-created: 2026-09-08
---


# [Access Data Tables from Tableau](#access-data-tables-from-tableau)

All Anvil apps, including Tableau Extensions built with Anvil X, have a built-in database called [Data Tables](../../data-tables). You can connect your extension’s Data Tables as a data source in Tableau.

## [Enable access in Anvil](#enable-access-in-anvil)

To do this, open the Anvil X configuration in the left-hand sidebar of the Anvil Editor.

Scroll down to “Access your Data Tables from Tableau”, and click **Enable**.

You will now see the authentication details required to access your extension’s Data Tables from Tableau.

## [Add the data source to Tableau](#add-the-data-source-to-tableau)

Now, you can add your app’s Data Tables to your Tableau dashboard as a Postgres data source. Follow [Tableau’s instructions](https://help.tableau.com/current/pro/desktop/en-us/examples_postgresql.htm) to add and query the data source.

For security reasons, Anvil X does not permit Tableau to make direct connections to Anvil’s internal Postgres database. Instead, the connection details provided go via a “virtual database” that provides access to only your own Data Tables. This may affect performance for complex queries.

## [Testing and Published versions](#testing-and-published-versions)

If you have [published](publishing) your extension, it’s possible you are using separate databases for your personal testing and for your deployed extension. Anvil will offer you connection details for both testing and published versions of your extension.

In order to make sure that your Tableau dashboard sees the correct data, make sure that dashboards using the *testing* version of your extension use the *testing* password, and dashboards using the *published* version use the *published* password.

Learn more about [testing vs published versions](publishing) of your extension.
