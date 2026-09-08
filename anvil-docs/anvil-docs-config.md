# anvil-docs — Configuration

Canonical current-state configuration record for the anvil-docs corpus.
Agent-facing. Reflects the live-verified state as of 2026-09-06. States facts
about this specific corpus, not general Anvil knowledge — where the reasoning
matters, see `anvil-docs-explainer.md`; for operational commands and rules,
see `anvil-docs-reference.md`.

---

## Identity

| Item | Value |
|---|---|
| Name | `anvil-docs` (prior name `anvil-synthesized-reference`, still referenced in `site-map.md`'s own header) |
| Real location | `C:\mybizz\mybizz-config-docs\anvil-docs\` |
| Nature | Developer-synthesized hybrid reference corpus — scraped official documentation + absorbed runtime source, reorganized by subject. Documentary reference material, never executed |
| Host GBrain source | `mybizz-config-docs` (registered, federated) — the corpus is searchable through it today |
| Scale (verified 2026-09-06) | 730 files total: 326 `.md` → 321 corpus pages (excl. the 3 canonical files, README, site-map) + 404 runtime-source files (110 `.ts`, 98 `.py`, 58 `.clj`, 39 `.tsx`, 13 `.scss`, 12 `.yml`, 12 `.js`, 10 `.html`, remainder misc) |
| Composition | (1) scraped `anvil.works/docs` — the original scrape record counts 298 pages across 19 site areas; (2) absorbed runtime source from `github.com/anvil-works/anvil-runtime` |
| Status | Complete — scrape and absorption finished; the original `anvil-runtime-reference` clone fully absorbed and removed |

## Provenance (verified against upstream 2026-09-06)

| Item | Value |
|---|---|
| Runtime absorption commit | `34067eb48f36f2bfc97227bb019b0fc4c8116e1f` — "Anvil App Server v1.17.0", 2026-06-24, author s-cork |
| Upstream match | `34067eb` is upstream `master`'s current HEAD — zero drift; the runtime side is current as of verification |
| Runtime repo | `github.com/anvil-works/anvil-runtime` — "The runtime engine for hosting Anvil web apps"; ~1k stars, 133 forks |
| Licence | Upstream runtime is **AGPL** (with an explicit app-hosting exception). **No LICENSE file was absorbed** — none exists anywhere in the corpus. Absorbed source is reference-only, never executed or hosted (see explainer) |
| Docs scrape window | 2026-09-02 → 2026-09-04 (file mtimes) |
| Docs-side drift | Possible since the snapshot — the live site may change; pages are re-scrapeable (see `anvil-docs-reference.md`) |

## Structure (verified 2026-09-06)

23 top-level directories = **19 scraped site areas + 4 non-site folders**, reconciled exactly against `site-map.md`'s 19 `##` area headings.

| Group | Members |
|---|---|
| Site areas (19) | `overview`, `plans-and-accounts`, `editor`, `ai`, `client`, `server`, `data-tables`, `deployment`, `users`, `external-resources`, `integrations`, `other-concepts`, `workflows`, `enterprise`, `using-another-ide`, `get-started`, `components`, `api`, `how-to` |
| Non-site top-level folders (4) | `app-structure/` — the real `anvil.yaml` schema and app directory layout (from the clone's `doc/app-structure.md`); `debugging-guide/`; `tests/` — a real, preserved example application plus its original CI scaffolding; `uplink-kickstart/` — real Uplink example code (`uplink.py`, `test_uplink.py`, run-report YAMLs; the oldest corpus content, Jul 22) |
| Runtime-source subfolders inside site areas | `integrations/segment/`, `integrations/airtable/`, `integrations/oauth/` (shared `oauth.clj` protocol engine used underneath Google/Facebook/Microsoft), `client/forms/html-form-parser/` (real `.cljc`/`.cljs` form-template parser) |

## Conventions (verified)

| Convention | Rule |
|---|---|
| URL-slug naming | Folder/file name = exact last path segment of the real `anvil.works/docs/...` URL |
| Parent vs. leaf | A page with children is a directory; a childless page is `{slug}.md` |
| `_index.md` | Every directory's own page content lives in `_index.md` inside it |
| Frontmatter | Every scraped page starts with a stub: `title`, `url` (sample verified) |
| Runtime source placement | Not a 1:1 mirror of the runtime's own tree — absorbed **by subject**, alongside the matching documentation topic |

## `tests/` — a real, preserved example application

`tests/apps/SmokeTest/` is a genuine, complete, minimal working Anvil application — real `anvil.yaml` with a real `db_schema`, real client/server code, real theme configuration. The surrounding CI/test-harness files (`run_tests`, `Dockerfile*`, `py_tests/`, `configs/`) were kept by explicit developer decision.

## Settled policies (developer decisions on record)

Cupcake-based statements in this suite describe standing policy and what
enforcement blocks when active — enforcement status is not fixed and is not
restated as current anywhere in this suite; check `cupcake-config.md`'s
Current Operational Status for the live state.

| Policy | Detail |
|---|---|
| Memory Governor treatment | **No special bypass exemption.** Ordinary sync via the host source (`mybizz-config-docs`), same as any other content there. Developer decision 2026-09-06: unlike `anvil-agent-references`, this corpus is not pure vendor material with no judgment to make about it — it is a developer-synthesized hybrid (scraped docs + absorbed runtime source + real reorganization decisions), so a "nothing to judge" bypass would not be true. This lines up with the corpus's own stated design principle (developer-stated): GBrain can be wrong, the file wins, always — corpus files are ground truth, not competing governed facts. |
| Corpus changes | Deliberate construction events only — single-page re-scrapes via `step1b-strip-write.py`; runtime re-absorption only if upstream moves past the absorbed commit (currently HEAD == absorbed commit). |
| Cupcake grants | No cross-project grants currently exist (grants data file verified empty, 2026-09-06). The corpus sits inside the current project, so ordinary in-project work needs none. The prior suite's "cross-project whitelisted + `.clj` exemption" claim did not match the verified-empty grants file and is retired. |

## Known content gaps

| Gap | Status |
|---|---|
| 91 files deliberately excluded from `server/` | Platform operations, deep SSO protocol internals, the runtime's own build/test tooling, `app-server/` packaging/self-hosting code. Deliberate exclusion, not an oversight — reasoning per category in `anvil-docs-explainer.md` |
| 33 of the original 49 real filesystem symlinks | Converted to plain-text reference notes during absorption; the remaining 16 were confirmed byte-identical duplicates and deleted — see the entry below |
| 16 "Group C" duplicate files deleted | Confirmed byte-identical to counterparts absorbed via `services/`/`client/`; deleted as genuine duplicates |
| `_components.py` orphan | The prior suite described two plain-text notes referencing a nonexistent source. A name-based search (`find -name "_components.py*"`) found **no such files** in the corpus — the orphan claim's artifacts are unverified as of this rewrite |

## Open items

| # | Item | Status |
|---|---|---|
| 1 | No adoption-time review record for the corpus construction, per `sec-dependency-skill-supply-chain` / `sec-review-before-trust`. Axes at verification: publishers ✓ (Anvil docs; anvil-works runtime), maintenance ✓ (absorbed commit == upstream HEAD), spawn capability ✓ (none — corpus, not a skill), licence = AGPL, documented but not formally judged. | Open |
| 2 | Docs-side drift vs. the live site since the Sep 2–4 snapshot — re-scrapeable per `anvil-docs-reference.md`. | Open |
| 3 | No standing backup exists for this corpus — bulk operations require the before/after count discipline in `anvil-docs-reference.md`. | Open |
| 4 | `_components.py` orphan artifacts unverified (see content gaps). | Open |
