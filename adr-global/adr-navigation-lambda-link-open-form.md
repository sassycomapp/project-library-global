---
title: "adr-navigation-lambda-link-open-form"
doc-id: "mb-88483403"
updated: "2026-10-23"
---
# Navigation Standard: Lambda/Link/open_form

**Status:** Accepted

---

## Context

Mybizz applications use layout shells for signed-in navigation. Layout shells are the native Material 3 layouts (`NavigationRailLayout`, `NavigationDrawerLayout`), as [[[default:adr-global/adr-htmltemplate-use|HTMLTemplate Use]]](C:/dev/project-library-global/adr-global/adr-htmltemplate-use.md) sets out. This ADR sets how navigation works inside them.

---

## Decision

### The navigation pattern

**Sidebar navigation** in AdminLayout and CustomerLayout, built on the Material 3 layouts (`NavigationDrawerLayout`, `NavigationRailLayout`), uses:
- The layouts' own `NavigationLink` components in the navigation slot
- Lambda click handlers with **mandatory loop variable capture**:

```python
lambda e, fn=form_name, a=attr_name: self._nav_click(fn, a)
```

The `fn=` and `a=` keyword arguments in the lambda are not optional. Omitting them
causes all nav items to capture the last value of the loop variable — a silent bug.

**Parameterised navigation** (row clicks, detail forms with IDs) uses `open_form()`
called directly:

```python
open_form('BookingViewerForm', booking_id=row['booking_id'])
```

**`navigate_to` is never used**, neither as a function nor as a `NavigationLink` property: every navigation goes through the lambda click handler or `open_form()`, so one pattern applies everywhere.
The `nav_` prefix in component naming refers to the `NavigationLink` components in the sidebar.

---

## Consequences

- Every navigation item uses a lambda click handler with its loop variables captured, or `open_form()`; nothing else.
- `navigate_to` appearing anywhere is a defect.
