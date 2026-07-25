---
document: "{Project Name} — Custom Component Requirements Matrix"
doc-id: global-0087
state: Live
date-created: 2026-07-25T150027+0200
---
# {Project Name} — Custom Component Requirements Matrix

**Date:** **[PROJECT]**
**Status:** **[PROJECT]**
**Project:** **[PROJECT]**
**Platform:** Anvil.works with Material Design 3 (M3)

---

## Definition

Fixed — this is the qualifying test, not project content. A component only belongs in
this matrix if it meets **both**:

1. Is not adequately provided by native Anvil Material 3 components
2. Is intended for use in more than one location

A component failing either test doesn't belong here — it's local, form-specific UI, not a
shared custom component. Applying this test correctly is what keeps this matrix meaningful
instead of becoming a list of every non-trivial widget in the app.

---

## Custom Component Matrix

| Component | Reused In | Usage Count | Justification |
|---|---|---|---|
| *(example)* `ClauseBuilder` (mb0test) | *PrivacyPolicyEditor, TermsConditionsEditor* | *2* | *Reusable clause-level editor, parameterized by document type — not provided by native M3. Meets both criteria: no native equivalent, used in 2+ locations.* |
| **[PROJECT]** | | | |

**Justification quality bar:** a justification must name *why native M3 can't do this* —
"not in native Anvil" restated without saying what was actually missing is not a real
justification. The worked example above shows the bar: state what native M3 lacks, state
where it's reused.

### Downgraded Components

Fixed discipline — keep this section even if empty at first. A component that no longer
meets the two-part test gets tracked here, with the reason, not silently deleted from the
matrix. This preserves the decision trail; a future developer shouldn't have to wonder
whether a component was never custom or used to be and stopped qualifying.

| Component | Previous Status | Current Status | Reason |
|---|---|---|---|
| *(example)* `PaletteSettingsForm` (mb0test) | *Shared custom component* | *Local/form-specific UI* | *Only used in one form — no longer meets the reuse criterion.* |
| **[PROJECT]** | | | |

---

## Implementation Notes

One sub-section per component in the matrix above. Shape, per component:

### {Component Name}
- What it does, in one or two lines
- Must be implemented as a reusable/standalone component (state this explicitly — it's a
  constraint on *how* it's built, not just a note that it exists)
- Any parameterization (what varies between its uses)
- What it writes to, if it persists data
- Use in: {every location listed in the matrix row above — keep these in sync, don't let
  the matrix and this section disagree}

**[PROJECT]** — one of these per matrix row.

---

## {Version} Custom Component Count

Fixed shape — a closing count table, matching the matrix above exactly. If these two
numbers ever disagree, the matrix is wrong until reconciled — don't let the count table
silently drift from the actual row count.

| Component | Count |
|---|---|
| **[PROJECT]** | |
| **Total Shared Custom Components** | **[PROJECT]** |

---

*This is the global starter model. Copy into a new project's `docs-local/`, fill every
**[PROJECT]** marker, replace the two `mb0test` example rows with this project's real
components, remove this closing note. The Definition and the Downgraded Components
discipline are the actual reusable learning here — keep both. The five example components
in the source this template was built from were mb-3-cs-specific and are not carried
forward.*
