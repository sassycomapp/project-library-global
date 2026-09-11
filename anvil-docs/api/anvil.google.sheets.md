---
document: "anvil.google.sheets"
title: "anvil.google.sheets"
url: "/docs/api/anvil.google.sheets"
doc-id: anvil.google.sheets
state: Live
date-created: 2026-09-08
---


## `anvil.google.sheets` Module

#### Classes

[`Cell`](#Cell) [`Row`](#Row) [`Spreadsheet`](#Spreadsheet) [`Worksheet`](#Worksheet)

## Classes

### `Cell`

-   [Attributes](#Cell_attributes)

---

---

#### Cell Attributes

**col** - *number*

This cell’s column index (starting from 1)

**input_value** - *string*

The value that was entered into the cell

**row** - *number*

This cell’s row index (starting from 1)

**value** - *string*

The value in this cell

---

### `Row`

-   [Methods](#Row_methods)

---

---

#### Instance Methods

**delete()**

Delete this row from the worksheet. (This will cause data in subsequent rows to shift up)

---

### `Spreadsheet`

-   [Methods](#Spreadsheet_methods)
-   [Attributes](#Spreadsheet_attributes)

---

---

#### Instance Methods

**list_worksheets() → list(anvil.google.sheets.Worksheet instance)**

Get a list of all worksheets in this spreadsheet

---

#### Spreadsheet Attributes

**id** - *string*

The ID of this spreadsheet in Google Drive

**title** - *string*

The title of this spreadsheet.

**worksheets** - *list(anvil.google.sheets.Worksheet instance)*

The worksheets in this spreadsheet.

---

### `Worksheet`

-   [Methods](#Worksheet_methods)
-   [Attributes](#Worksheet_attributes)

---

---

#### Instance Methods

**add_row(**fields) → anvil.google.sheets.Row instance**

Add a row to the end of the worksheet, specifying values for columns as keywords arguments

**get_cell(row, col) → anvil.google.sheets.Cell instance**

Get a particular cell from the spreadsheet

**list_cells([min_row=], [max_row=], [min_col=], [max_col=]) → list(anvil.google.sheets.Cell instance)**

List cells in the worksheet, optionally specifying a region

**list_rows(**query) → list(anvil.google.sheets.Row instance)**

List rows in this worksheet, optionally restricting to rows with the specified column values specified as keyword arguments

---

#### Worksheet Attributes

**cells** - *list(anvil.google.sheets.Cell instance)*

A list of all the cells in this worksheet

**column_count** - *number*

The number of columns in this worksheet

**fields** - *list*

The fields in this worksheet (ie the column headers, or the values in the first row)

**row_count** - *number*

The number of rows in this worksheet

**rows** - *list(anvil.google.sheets.Row instance)*

The rows in this worksheet (excluding the header)

**title** - *string*

The title of this worksheet
