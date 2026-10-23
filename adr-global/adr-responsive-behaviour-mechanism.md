---
title: "adr-responsive-behaviour-mechanism"
doc-id: "mb-c7aafcbe"
updated: "2026-10-23"
---
# `responsive-behaviour-mechanism` ADR: Responsive Behaviour Mechanism

## Status

Accepted

## Context

Design documents commonly describe responsive behaviour as pixel breakpoints (a binary split, or tiers such as 640px and 1024px) with column-count and typography rules per tier. No such model matches how Anvil achieves responsive behaviour.

### What Anvil's own documentation and forum say

- Anvil staff (`stucork`), answering this exact question on the forum: responsive behaviour is controlled by a per-container property called **`wrap_on`**, not CSS breakpoints.
- Confirmed in Anvil's official Changelog: *"DataGrids are now responsive: Make your tables wrap easily on mobile devices with the new wrap_on property."*
- `wrap_on` is available on ColumnPanel, FlowPanel, and DataGrid. M3 does not have its own container components; it uses these same classic ones, so `wrap_on` applies identically inside M3 apps.
- Separately and additionally confirmed: NavigationRailLayout and NavigationDrawerLayout auto-collapse to a modal drawer or app bar on small screens. This is genuinely native and automatic, and is a different mechanism from `wrap_on`.

## Decision

Responsive behaviour is achieved via `wrap_on`, set per-container:

- `mobile` where the wireframe shows wrapping or stacking behaviour.
- `never` where the wireframe shows a fixed layout that should not rearrange.

No breakpoint-pixel table is used. Navigation collapse remains separately automatic and requires no instruction.

## Consequences

- No design document of any application states responsive behaviour as a breakpoint table; responsiveness is stated around `wrap_on`.
- Developers set a single property per container rather than managing CSS media queries or pixel thresholds.

## Alternatives Considered

- **CSS breakpoint tables (binary or three-tier).** Rejected. Anvil does not expose CSS media query control to the developer in its component model. A breakpoint table has no corresponding Anvil mechanism and cannot be implemented as specified.
- **No responsive instruction (rely entirely on native auto-collapse).** Rejected. NavigationRailLayout and NavigationDrawerLayout auto-collapse natively, but content containers (ColumnPanel, FlowPanel, DataGrid) do not rearrange without explicit `wrap_on` instruction. Both mechanisms are needed.

## Related Documents

| Document | Relationship |
|---|---|
| [[[default:adr-global/adr-design-rules\|Design Rules]]](C:/dev/project-library-global/adr-global/adr-design-rules.md) | Wireframe design rules; wireframes must annotate `wrap_on` where applicable |
| [[[default:adr-global/adr-ui-customization-approach\|UI Customization Approach]]](C:/dev/project-library-global/adr-global/adr-ui-customization-approach.md) | Broader UI customization approach; this ADR is a specific responsive instance |

