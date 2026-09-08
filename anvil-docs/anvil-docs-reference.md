# anvil-docs — Reference: Navigation, Verification, Maintenance

Companion to `anvil-docs-config.md` (current state, open items) and
`anvil-docs-explainer.md` (what this is and why, incident history).
Agent-facing — exact commands, exact rules.

---

## Finding documentation content

`site-map.md` is the authoritative URL → path lookup for every scraped
documentation page. Given a real `anvil.works/docs/...` URL, the exact local
file path is directly derivable from it — URL-slug naming, no separate lookup
beyond `site-map.md` for confirming a page's location.

Example: `anvil.works/docs/users` → `users/_index.md`.
`anvil.works/docs/users/presenting-a-login-form` → `users/presenting-a-login-form.md`.

## Finding absorbed runtime source

**No separate index exists — real source was placed by subject during
absorption, directly into the matching documentation topic folder.** To find
real source code for a given Anvil feature, go to that feature's own topic
folder first (`integrations/stripe/` for Stripe, `data-tables/` for Data
Tables) — the source sits alongside the documentation for the same subject.

Do not search for runtime source by the Anvil Runtime's own internal folder
names (`services/`, `native_rpc_handlers/`, `dispatcher/`) — that structure
does not exist in this corpus.

## Verifying file counts

```bash
find /mnt/c/mybizz/mybizz-config-docs/anvil-docs -type f | wc -l
```

Baseline at this suite's rewrite (2026-09-06): **730 files** (326 `.md` + 404
other). **No standing backup exists.** Any bulk operation must be preceded by
a real count like this and followed by the same command to confirm the
expected before/after delta.

## Re-scraping a documentation page

`step1b-strip-write.py` is a real, working, reusable tool (verified 2026-09-06):

```bash
python3 step1b-strip-write.py TARGET_RELPATH < RAW_MARKDOWN_FILE
```

- `TARGET_RELPATH` — the file's real path relative to the corpus root (e.g. `overview/faq.md`).
- `RAW_MARKDOWN_FILE` — a real `webfetch` markdown capture of the live page, piped via stdin.
- The script preserves the target file's existing frontmatter byte-for-byte and replaces only the body.
- Validated strip rule (proven on the original scrape): article body starts at the page's own first `# ` heading, ends at `### Do you still have questions?` or a `TM[](` footer-logo marker.
- Do not modify the script before reuse — it is generic and validated.

## Runtime re-absorption

Only relevant when upstream `master` moves past the absorbed commit
(`34067eb` — it was upstream HEAD at verification, 2026-09-06). Re-absorption
is a deliberate construction event: fresh clone → subject-mapped placement
alongside matching documentation → count-verified before/after. It is a
developer decision, not routine maintenance.

## Cross-references — plain links, not wikilinks

Links inside scraped pages (e.g. `[Quickstart for logins](users/quickstart-login)`)
are plain, relative markdown links — not GBrain wikilinks, by design
(`mb-wikilinks`'s resolver is scoped to markdown and would not cover the
corpus's non-markdown source files). A broken relative link is fixed directly
in the file; there is no automatic resolution mechanism.

## Using GBrain against this corpus

The corpus is searchable via its host source `mybizz-config-docs`. Precedence
rule: **corpus files are ground truth; GBrain summaries of corpus content are
secondary** — verify against the file when they disagree (settled policy;
reasoning in `anvil-docs-explainer.md`). Content reaches GBrain by ordinary
host-source sync only — never through Memory Governor's API (settled policy:
no bypass exemption for this corpus).

## Licence posture

Absorbed runtime source is AGPL-licensed upstream. This corpus is
reference-only: read, diff, and cite the source — never execute, serve, or
distribute it as part of an application (reasoning in `anvil-docs-explainer.md`).

## Do not

- Do not perform a bulk operation against this corpus without a real, independent file-count check before and after — there is no backup to fall back on.
- Do not re-run scaffold-generation against the populated corpus — it really did wipe every scraped page once (see `anvil-docs-explainer.md` §5, incident 3A).
- Do not assume a wikilink (`[[name]]`) will resolve anything in this corpus — none exist here by design.
- Do not search for runtime source by the runtime's own internal folder names — search by subject.
- Do not attempt to resolve `_components.py` — confirmed upstream as having no real source; its claimed orphan notes in the corpus are themselves unverified (config.md, content gaps).
- Do not execute, serve, or distribute the absorbed runtime source — reference-only material (AGPL upstream; see `anvil-docs-explainer.md`).
- Do not treat the 91 excluded `server/` files as missing by accident — deliberately excluded, per category, in `anvil-docs-explainer.md`.
- Do not submit corpus content through Memory Governor — ordinary host-source sync only (settled policy, config.md).
- Do not treat GBrain summaries of corpus content as authoritative over the files themselves — the file wins (settled policy).
