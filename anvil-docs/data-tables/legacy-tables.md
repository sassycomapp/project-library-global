---
title: "Legacy Tables"
url: "/docs/data-tables/legacy-tables"
---


# [Legacy Tables](#legacy-tables)

**Legacy Tables** is the deprecated [Data Tables](/docs/data-tables) API. It has been replaced with the Accelerated Tables API, which was previously a beta release. Legacy Tables are still available for LTS purposes.

## [Using Legacy Tables](#using-legacy-tables)

Reverting back to Legacy Tables will **render certain features unusable** and result in **diminished Data Table performance**.

In order to revert back to Legacy Tables in your app, open **Settings**, then choose **Data Tables**, then check the **Legacy Tables** option. You do not need to change your app’s code.

## [Missing functionality](#missing-functionality)

The Legacy Tables API is deprecated, and as a result does not feature all the functionality of the modern API. Here follows a list of features that are not available with Legacy Tables:

-   [Batching additions, updates and deletions of rows](/docs/data-tables/data-tables-in-code#batch-add-update-and-delete-rows)
-   [Model Classes](/docs/data-tables/model-classes)
-   [Explicit cache control](/docs/data-tables/data-tables-in-code#explicit-cache-control)
-   [Listing available tables by calling `list(anvil.tables.app_tables)`](/docs/data-tables/data-tables-in-code#accessing-tables)
-   [Accessing a table by using square bracket notation, i.e. `app_tables["my_table"]`](/docs/data-tables/data-tables-in-code#accessing-tables)
