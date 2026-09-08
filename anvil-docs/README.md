# Anvil Docs

The complete, canonical reference corpus for building Anvil applications —
official documentation and real runtime source code, combined, organized
by subject.

## What this folder actually contains

- **Scraped official documentation** — the real content of every page
  under anvil.works/docs, organized to mirror the site's own structure.
  See `site-map.md` for the authoritative URL → path reference.
- **Absorbed runtime source code** — real Python and Clojure source from
  the official Anvil Runtime, moved in and organized by subject
  alongside the matching documentation (e.g. real Stripe integration
  code sits in `integrations/stripe/`, alongside its docs).
- **Five additional topic folders**, not present on the official site,
  created to hold runtime source with no natural documentation-page
  home: `app-structure/`, `integrations/segment/`, `integrations/airtable/`,
  `integrations/oauth/`, `client/forms/html-form-parser/`.
- **`tests/`** — a real, complete example Anvil application
  (`apps/SmokeTest/`), preserved as working reference material, plus its
  original test/CI scaffolding.

## Conventions (unchanged from the original scaffold)

1. **URL-slug naming.** Every folder and file name is the exact last path
   segment of the corresponding `anvil.works/docs/...` URL, verbatim.
2. **Parent page = directory; leaf page = file.**
3. **`_index.md` in every directory** — the placeholder for that
   directory's own page content.
4. **3-line frontmatter stub** (`title`, `url`) at the top of every
   scraped page.

## Status

Complete. Both the documentation scrape and the runtime source
absorption are finished. The original source clone
(`anvil-runtime-reference`) has been fully absorbed and its content
removed.
