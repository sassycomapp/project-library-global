---
title: "Environments and Code"
url: "/docs/deployment/environments/environments-and-code"
---


# [Learning about Environments from Code](#learning-about-environments-from-code)

In a typical application, the same source code will run in several different environments – a developer’s personal [Development Environment](../environments#development-environments), then perhaps a testing environment, then production. It might need to behave differently in different environments: for example, if it is generating links to its own HTTP endpoints, those links should include the URL for the current environment. As another example, an application that connects to an external database server might connect to a testing database in development and testing environments, and a production database in production.

In order to “ship what we tested”, we shouldn’t need to change our code between each of these stages (for example, changing the database connection string before each production deploy). Instead, our code should dynamically change its behaviour, based on the environment it is in.

## [Getting the app’s URL](#getting-the-apps-url)

You can get your app’s root URL programmatically using [`anvil.server.get_app_origin()`](/docs/api/anvil.server#get_app_origin). This will return the URL for the environment you are currently running in.

If you wish to programmatically construct URLs pointing at a different environment (for example, your app’s main production environment), hard-code a constant containing your custom domain and construct URLs from that.

## [Getting the current environment](#getting-the-current-environment)

The [`anvil.app.environment`](/docs/api/anvil#AppEnvironment) object represents the current environment. You can retrieve the environment’s name with `anvil.app.environment.name`.

If your application contains configuration values (such as database connections) that should be different between environments, we recommend creating a Module (or Server Module) with global constants for all of these configuration values, then centralise the code for changing them based on environment. For example:

```python
if anvil.app.environment.name == "Production":
    IS_PRODUCTION = True
    DB_URL = "postgres:prod_database"
    DB_PASSWORD = anvil.secrets.get_secret("db_pw_prod")
elif anvil.app.environment.name == "Staging":
    IS_PRODUCTION = False
    DB_URL = "postgres:staging_database"
    DB_PASSWORD = anvil.secrets.get_secret("db_pw_staging")
else:
    # Probably a personal Development Environment
    IS_PRODUCTION = False
    DB_URL = "postgres:test_database"
    DB_PASSWORD = anvil.secrets.get_secret("db_pw_test")
```
