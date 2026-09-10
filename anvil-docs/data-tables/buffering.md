---
title: "Buffering Changes"
url: "/docs/data-tables/buffering"
doc-id: buffering
state: Live
date-created: 2026-09-08
---


# [Buffering Changes](#buffering-changes)

If an app displays tabular data that users can edit, it’s common to save all the edits to the table at once or discard the changes. For example, after a user makes edits to the table data, they would need to click “Save” or “Discard” before proceeding. Similarly, if they want to add a new record to the table, the user will need to enter (and validate) the data for an entire record before saving it to the database.

You can do this in Anvil with [**buffered changes**](#buffered-changes) to Data Tables and [**draft** Row objects](#drafts).

## [Buffered changes](#buffered-changes)

Enabling buffered changes on a Row from a Data Table means that edits to that Row will not be saved to the database until the Row’s `save()` method is called.

To temporarily buffer changes for an individual Row, use `with row.buffer_changes():`. Code inside the `with` block will see a buffered version of the Row, but any buffered changes will be discarded at the end of the block. If you want to retain the changes, call the row’s `save()` method.

For example, you could [data bind](/docs/client/component-properties/data-bindings) a Data Table Row to an editing Form and display this Form as a pop-up to the user. If the user confirms the changes, then the Row is saved:

```python
with row.buffer_changes():
    # Pop up an editor for this row
    if confirm(EditForm(item=row)):
      row.save()
    # else, discard changes
```

It is also possible to switch a Row into buffered mode until further notice, by calling `row.buffer_changes(True)`. In this case, the row will remain in buffered mode unless you call `row.buffer_changes(False)`. Calling `row.buffer_changes(False)` discards any buffered changes.

You can view all the changes that have been buffered for a Row by accessing its `buffered_changes` property. `row.buffered_changes` will return a `dict` of the changes that have been buffered. If no changes have been buffered, it will instead return `None`.

### Saving and resetting

Calling `row.save()` will save all buffered changes to the database. If the row contains links to other rows that are buffering changes, or to [draft rows](#drafts), they will also be saved.

Calling `row.reset()` will discard all buffered changes. If the row contains links to other rows that are buffering changes, they will also be reset.

The `save()` and `reset()` methods do not affect whether an existing row is in buffered mode.

## [Drafts](#drafts)

If you create a new instance of a Data Table Row, this object will be a draft. A draft Row will not be added to the database and will have no unique ID until and unless it is saved.

To create a draft, construct a new instance of `app_tables.[tablename].Row`. You may then update this object and either discard it or save it. For example:

```python
person = app_tables.people.Row()
if confirm(PersonEditor(item=person)):
  person.save()
# else, discard the new instance
```

Once a draft has been saved, that object now represents an existing row in the Data Table and reverts to the default behaviour of that table. Unless you have created a [model class](model-classes) for that table with `buffered=True`, the row will no longer buffer changes.

Until a draft has been saved, its `get_id()` method will return `None` as it has no unique identity.

## [Security](#security)

Buffered changes respect all the usual security boundaries of Data Tables - they merely defer the update or creation of a row.

However, buffered changes are most useful on the client, where they allow you to use [Data Bindings](/docs/client/component-properties/data-bindings) on a row object without committing changes to the database on every UI operation. By default, client-side code cannot write to the database, so the examples on this page only work if Data Tables have [write access](/docs/data-tables/data-security#permissions). However, you can now use [model classes](/docs/data-tables/model-classes) to support client-side operations where appropriate (e.g. by setting `client_writable` to `True` and overwriting the Row’s [`_do_update`](/docs/data-tables/model-classes/validation#low-level-api) method to check the user’s permissions when the update comes from the client).
