---
title: "Keyboard Shortcuts"
url: "/docs/editor/keyboard-shortcuts"
doc-id: keyboard-shortcuts
state: Live
date-created: 2026-09-08
---


# [Keyboard Shortcuts](#keyboard-shortcuts)

There are several keyboard shortcuts available in the Anvil Editor. If you are using a Mac, you can use `Cmd` instead of `Ctrl` everywhere if you prefer, but you’ll need to use `Option` instead of `Alt`.

## [From Any Screen In the Editor](#from-any-screen-in-the-editor)

-   `Ctrl-B` — Open or close the [App Browser](https://anvil.works/docs/editor#app-browser) panel.
-   `Ctrl-Shift-F` — Search all code in the app.
-   `Ctrl-P` — Open the [Quick Switcher](https://anvil.works/docs/editor#zen-mode-and-quick-switcher) window to easily jump between tabs.
-   `Alt-PgDown or Alt-PgUp` — Goes to the next or previous editor tab, respectively.
-   `Ctrl-Enter` - Run the app.

## [In the Form Editor](#in-the-form-editor)

The following shortcuts are available in both Design and Code view.

-   `Alt-Shift-Z` or `Double Click` the tab bar - Maximize the current tab and enter [Zen mode](https://anvil.works/docs/editor#zen-mode-and-quick-switcher).
-   `Ctrl-Y` or `Ctrl-Shift-Z` - Redo the latest change.
-   `Ctrl-Z` - Undo the latest change.
-   `Shift-Click` on a file name in the [App Browser](https://anvil.works/docs/editor#app-browser) or in the [Quick Switcher](https://anvil.works/docs/editor#zen-mode-and-quick-switcher) window — Open the file in a new web browser window

### Design View Only

-   `Ctrl-C` — Copy the currently selected component(s).
-   `Ctrl-V` - Paste the cut/copied components into the selected container.
-   `Ctrl-X` — Cut the currently selected code
-   `Delete` or `Backspace` - Delete the currently selected component(s).
-   `Ctrl-Drag` - Fine-grained control over column resizing.
-   `Double Click` on column separator of column panel — Reset column width, so the two columns have the same width.

## [Code Editing](#code-editing)

#### General Shortcuts

-   `Alt-Up` or `Alt-Down` — Move the current or the selected lines up or down.
-   `Alt-Shift-Up` or `Alt-Shift-Down` — Duplicate the current or the selected lines above or below.
-   `Ctrl-C` — Copy the currently selected code.
-   `Ctrl-D` — Delete current line.
-   `Ctrl-F` - Search the current file. Hit enter repeatedly to find subsequent matches.
-   `Ctrl-G` - Find next. Repeats previous search.
-   `Ctrl-Shift-G` - Find previous. Repeats previous search backwards.
-   `Ctrl-H` - Replace occurrences of a particular string in the current file one by one.
-   `Ctrl-Shift-H` - Replace all occurrences of a particular string in the current file.
-   `Ctrl-Alt-G` - Go to line
-   `Ctrl-V` - Paste the cut/copied code at the cursor.
-   `Ctrl-Q` - Expand/collapse currently selected block of code.
-   `Ctrl-X` — Cut the currently selected code
-   `Ctrl-/` - Comment/uncomment a line or block of code.
-   `Ctrl-Click-Function` - Click on a function to jump to its definition.
-   `Ctrl-Click-Variable` - Click on a variable to jump to its definition.

#### Multiple Cursors and Selection Ranges

Anvil offers support for multiple cursors (also known as carets), allowing for rapid simultaneous editing.

-   `Alt-Click` — Add a new cursor while retaining the existing cursors and selections.
-   `Alt-Drag` — Add a new rectangular selection while keeping the current cursors and selections intact.
-   `Alt-Shift-Drag` — Create a new rectangular selection, replacing any previous selections.

#### Linting and Formatting

-   `F8` — Jump to the next lint warning in the editor.
-   `Ctrl-I` — Reindent the code to match your tabsize preference.
-   `Ctrl-Shift-M` — Show all lint warnings in a bottom panel.
-   `Alt-Shift-F` — Auto-format your code using the [Ruff](https://docs.astral.sh/ruff/) formatter.

#### Regions

You can fold regions of source code using the folding icons on the gutter between line numbers and line start. Move the mouse over the gutter and click to fold and unfold regions.

-   `Ctrl-Alt-[` — Fold all regions recursively
-   `Ctrl-Alt-]` — Unfold all regions recursively
-   `Shift-Click-Chevron` - Fold/Unfold clicked region recursively. Child regions will fold or unfold to match their parent region.
-   `Alt-Click-Chevron` - Fold/Unfold all other regions recursively. Child regions will fold or unfold to match their parent region.
-   `Ctrl-Alt-k, Ctrl-Alt-0` — Fold All Code Recursively
-   `Ctrl-Alt-k, Ctrl-Alt-1` — Fold level 1
-   `Ctrl-Alt-k, Ctrl-Alt-3` — Fold level 3
-   `Ctrl-Alt-k, Ctrl-Alt-2` — Fold level 2
-   `Ctrl-Alt-k, Ctrl-Alt-4` — Fold level 4
-   `Ctrl-Alt-k, Ctrl-Alt-5` — Fold level 5
-   `Ctrl-Alt-k, Ctrl-Alt-6` — Fold level 6
-   `Ctrl-Alt-k, Ctrl-Alt--` — Fold All except selected region
-   `Ctrl-Alt-k, Ctrl-Alt-j` — Unfold All

## [In Data Tables](#in-data-tables)

-   `Delete` or `Backspace` - Delete the currently selected row(s) or column(s), or set the currently selected cell value to `None`.
-   `Up`, `Down`, `Left`, `Right` - Move between cells.
-   `Enter` - Edit the currently selected cell, or move to the cell below if already editing.
-   `Tab` - Move to the cell on the right.
-   `Shift-Tab` - Move to the cell on the left.
-   `Escape` - Clear the current selection.
