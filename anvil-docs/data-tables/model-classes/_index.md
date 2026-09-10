---
title: "Model Classes"
url: "/docs/data-tables/model-classes"
doc-id: model-classes-_index
state: Live
date-created: 2026-09-08
---


# [Model Classes](#model-classes)

Model classes allow you to add extra logic to rows in your Data Tables by providing a Python class that extends the [Row class](/docs/data-tables/data-tables-in-code#row-objects) for a particular table. That class will be instantiated anywhere that table is accessed. You can use model classes to provide properties and operations that are meaningful to your application, and to enforce permissions and constraints on your data.

## [Why use model classes?](#why-use-model-classes)

You can build complex, secure applications without using model classes by calling functions that update table rows. So what do model classes add?

Let’s imagine you’re building a To Do List application. With model classes, you can:

-   Add extra properties to your rows that expose meaningful information rather than raw column values (for example, “is this task critically overdue?” rather than “what is this task’s due date?”).

-   Add methods to your rows that represent meaningful actions on your objects, which might affect more than one row (for example, “assign this task to whoever is on-call”).

-   Enforce permissions and validation (for example, “a task’s priority can only be a number between 1 and 10”, or “this task cannot be updated except by its assigned owner or by an administrator”).

-   Allow direct interaction with data objects from client-side code, while still enforcing permissions and validation.

-   Express all of this logic in one place, rather than scattering your logic across Forms, Modules and Server Modules.

This documentation will explain how to do each of these things.

## [Contents](#contents)

1.  [Creating model classes](model-classes/creating): How to create model classes for tables and add extra behaviour to them

2.  [Checks and validations](model-classes/validation): How to enforce constraints by writing code that runs before rows are created, updated or deleted

3.  [Client-writable models](model-classes/client-writable): Skip the server functions and allow UI code to operate on model classes directly

4.  [Best practices](model-classes/patterns): Tips on using model classes to create robust and secure apps
