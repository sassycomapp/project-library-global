---
document: "Best Practices"
title: "Best Practices"
url: "/docs/data-tables/model-classes/patterns"
doc-id: patterns
state: Live
date-created: 2026-09-08
---


# [Best Practices with Model Classes](#best-practices-with-model-classes)

This page describes a few best pracices for combining [model classes](../model-classes), [buffering](../buffering) and [server methods](../../server/portable-classes/server-methods) to produce robust and secure apps. All of the examples on this page refer to a To Do List app.

## [Describe all operations in your model class](#describe-all-operations-in-your-model-class)

As far as possible, describe every operation your app performs on a particular table in your model class. This gives a central location for you (or another developer) to find everything to do with that class. You should use your Form code only to manage user interactions. Use server methods to encapsulate operations on your model, rather than spreading that information across Forms and Server Modules. This makes your code much easier to maintain, as well as making it easier to re-use logic in multiple UI contexts.

If your model classes start getting too big and unwieldy, break out complex operations into functions and call them from the model. You can organise these functions by spreading them across multiple Modules – use a Package to group together all the Modules that implement a particular model.

You should use properties and methods to expose useful information about your model, rather than computing that information from column values in your UI code. For example, if you are describing a task that may be overdue, create an `is_overdue` property on the model rather than writing `row['due_date'] < date.today()`. If, however, you want to display overdue tasks in red, use Form logic (code or Data Bindings).

## [Use client-writable models](#use-client-writable-models)

By using [client-writable models](client-writable), you can define all of your permission checks in one place, in the model class, while enabling the client to write directly to model objects (eg using Data Bindings).

For more complex operations than updating column values, expose server methods. (For example, assigning the task to a random person who is currently on call.)

When writing permission checks, use the [`from_client`](/docs/data-tables/model-classes/validation#low-level-api) parameter to apply strict permission checks only to client-side code. That way, server methods can perform operations that would not be permitted directly from untrusted Form code.

## [Use Data Bindings](#use-data-bindings)

Use [Data Bindings](/docs/client/component-properties/data-bindings) liberally. Unless you are data binding to a simple column value, you should probably be creating a property on your model class.

For example, let’s say you are displaying To Do List items in a [RepeatingPanel](/docs/ui/components/repeating-panel), and you want overdue tasks to show up in red. You should create a property on your model class called `is_overdue` that returns a boolean. You can then add a Label to your ItemTemplate and bind its `foreground` property to `"#f00" if self.item.is_overdue else "#000"`

The model expresses the logic, the data binding expresses the UI.

## [Use buffering and drafts](#use-buffering-and-drafts)

It’s useful to use your model classes in Forms that allow users to edit that row data or add new rows to the Data Table. In order to allow the user to discard changes, use [buffering](../buffering) to ensure that edits to the row don’t persist until the user explicitly saves their changes. Likewise, when creating new records, use [drafts](../buffering) so that the user can discard or save a new row. Buffering and drafts support Data Binding and custom properties without immediately persisting changes to the database.

To enable buffering everywhere and ensure that nothing is saved to the database without an explicit `save()` operation, pass [`buffered=True`](creating) to the superclass when defining your model.

## [Other tips](#other-tips)

**For operations that require privileged access or need to be completed in a [transaction](../transactions)**, use server methods.

**If you don’t want your server methods’ implementatation to be publicly visible**, use [server versions of models](creating#server-versions-of-models). Create a dummy `@anvil.server.server_method` in the client-visible model, then provide the full implementation in the server-side model where it will not be exposed to client code.

**For operations that do not refer to a particular row but instead refer to the collection** (for example, if you want to return all the rows owned by the currently logged in user), create server classmethods by combining `@anvil.server.server_method` and `@classmethod`.

**For operations that do not clearly belong to a single table** and combine operations over multiple tables, continue to use [server functions](../../server) (ie `@anvil.server.callable`).

## [Ask for help on the forum](#ask-for-help-on-the-forum)

The [Anvil Forum](https://anvil.works/forum) is a great resource. It’s full of people who have built large apps before, and the Anvil team post there regularly. If you’re wondering how to structure your app, try asking there!
