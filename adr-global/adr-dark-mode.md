---
title: "adr-dark-mode"
doc-id: "mb-c66b42b5"
updated: "2026-10-23"
---
# Dark Mode

## Status

**Accepted**

## Context

Every screen already carries a `@media (prefers-color-scheme: dark)` block with token overrides, and each palette's token set includes the surface and neutral tokens that dark mode swaps. Dark mode is therefore another set of token overrides, not a separate design system.

## Decision

**Every Mybizz application supports dark mode from its first release.**

Every screen includes a `@media (prefers-color-scheme: dark)` block with alternate values for these CSS custom properties:

- `--surface`
- `--on-surface`
- `--surface-variant`
- `--on-surface-variant`
- `--outline`
- `--outline-variant`
- `--surface-container-low`

Dark mode token values are palette-specific: each of an application's palettes defines its own dark surface and neutral tokens.

## Consequences

- Every screen file includes a `@media (prefers-color-scheme: dark)` block.
- The application's theme stylesheet holds the dark token overrides for every palette.
- The application's palette definition (in its own `DESIGN.md`) states dark tokens beside light tokens.
- Dark mode is a required item of every screen compliance checklist.
