---
title: "adr-dark-mode"
doc-id: "mb-c66b42b5"
updated: "2026-11-06"
---
# Dark Mode

## Status

**Accepted**

## Context

`m3-custom-theme` holds every palette in a light and a dark version, each defining all of the theme's colour tokens. A form that takes every colour from the theme's colour roles is therefore shown correctly in both modes without colours of its own.

## Decision

**Every Mybizz application supports dark mode from its first release.** Dark mode comes from the palettes of `m3-custom-theme`. A form holds no colour scheme, colour value or media query of its own.

## Consequences

- Every colour in a form comes from the theme's colour roles, as [[[default:specifications-global/spec-ui-standards]]](C:/dev/project-library-global/specifications-global/spec-ui-standards.md) sets out.
- The test suite's form scan rejects a colour value written in a form template.
- An application's choice of palette is recorded in its own design documentation; the light and dark values belong to the theme.
- Every form is checked in light and dark mode before its feature is signed off.
