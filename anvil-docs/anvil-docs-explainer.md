---
document: "anvil-docs — Explainer"
doc-id: anvil-docs-explainer
state: Live
date-created: 2026-09-08
---

# anvil-docs — Explainer

*Companion note: for current confirmed state (scale, structure, provenance,
policies, open items) see `anvil-docs-config.md`. For navigation, verification
commands, and maintenance rules, see `anvil-docs-reference.md`.*

---

## 1. What this actually is

Building Anvil applications kept re-deriving the same answers: what does
`anvil.yaml` actually support, how does a given built-in service really work,
what does the real code do when the official documentation is ambiguous or
silent. Answering those from the live docs alone meant guessing at a framework;
answering them from raw source alone meant navigating a runtime tree organized
by how the platform is built, not by what an app builder needs. This corpus
exists so neither guess is necessary: the real, official documentation and the
real, ground-truth runtime source, merged and organized together **by subject**
— Stripe code sits with Stripe documentation, Data Tables code with Data Tables
documentation.

Its role in this system (developer-stated): the **on-disc authoritative Anvil
reference** for building Anvil web applications under PDLF in OpenCode with the
installed skill sets. It is the deep layer beneath `anvil-agent-references` —
the vendor's skill and stub layer handles how to *work* on Anvil apps; this
corpus holds the full documentation and the platform's actual source for when
the question goes deeper than the skills answer.

## 2. What it can actually do

- Answer documentation questions from a byte-faithful local snapshot of every page under `anvil.works/docs`, navigable by exact URL-slug derivation or the site map.
- Answer "how does this really work" questions from the platform's actual source, sitting beside the docs for the same subject.
- Provide a real, complete, minimal working Anvil application (`tests/apps/SmokeTest/`) as concrete reference material.
- Provide real Uplink example code (`uplink-kickstart/`) and a validated single-page re-scrape tool for keeping the docs snapshot current.

## 3. Suitability

**Best for:** authoritative answers when the official documentation is
ambiguous, silent, or suspected wrong; API and behavior ground truth for
PDLF's Anvil work; any question deep enough that the vendor skill layer's
summaries are not enough.

**Good for:** concrete working examples (the SmokeTest app, the Uplink
kickstart); single-page doc corrections via the validated strip tool; provenance
and audit work, since the absorbed source is pinned to an exact upstream commit.

**Not good for:** executing or hosting the runtime source — the corpus is
deliberately documentary, and the source is AGPL-licensed upstream; a
replacement for `anvil-agent-references` — the two layers are complements, and
the skills, not the corpus, are what agents invoke; trusting GBrain summaries
of corpus content over the files themselves — the corpus's standing principle
(developer-stated) is that GBrain can be wrong, the file wins, always.

## 4. Design reasoning

### Why organized by subject, not by the runtime's own tree

The runtime's source tree groups code by *how the Anvil Runtime is built* —
`services/`, `native_rpc_handlers/`, `dispatcher/`. A person building an app
thinks in terms of *what they are trying to do*. Absorbing the source into the
matching documentation topics was a real act of reorganization, not a copy —
and it is why "find the Stripe code" means "open the Stripe folder," not
"understand the runtime's build layout first."

### Why byte-faithful scraping with frontmatter stubs

Every scraped page preserves the real article content, including original
Unicode typography, with site chrome stripped by a validated rule, and carries
a minimal `title`/`url` frontmatter stub. The stub is what makes every page
self-describing — its own provenance and canonical URL survive any future
reorganization, which is what allows the URL→path derivation to work at all.

### Why symlinks became plain-text notes, and links stayed plain

The original clone contained 49 real symlinks — Anvil's build-deduplication.
They were converted to plain-text notes rather than preserved, for two
confirmed reasons: WSL-created symlinks pointing at Windows-drive targets are
invisible to Windows Explorer, and a documentary corpus never executes code,
so a symlink's only real value — letting running code share one file — has no
purpose here; the *information* of the relationship is what matters. The same
logic settled the wikilink question: cross-references stayed plain relative
markdown links because the corpus's links span non-markdown source files the
`mb-wikilinks` resolver cannot meaningfully cover, and a manually fixable plain
link beats a resolver whose scope doesn't fit the corpus.

### Why the tests folder was kept

`tests/apps/SmokeTest/` is a genuine, complete, minimal working Anvil app that
a first-pass classification would have discarded as scaffolding. It was kept
deliberately as working reference material. The standing lesson from that
rescue, and others like it during absorption: a file's location inside a
"test" or "scaffolding" folder is not evidence it lacks value — check the
actual content before excluding anything.

## 5. Real incidents that shaped the corpus

**An accidental wipe, and a verified recovery.** During scraping, a
scaffold-generation script was accidentally re-run against the populated
corpus, wiping every page back to empty placeholders. Recovery reassembled
content from several real sources at once — and, critically, was verified by
programmatic byte-diffs against fresh re-fetches of the highest-risk files,
not trusted from a self-report. If content is ever suspected of drift, that
direct-diff method is the correct check.

**A real process violation, caught.** Partway through absorption, several
folders were processed consecutively without the standing per-folder review
pause. The completed work was independently spot-verified on disk afterward
and checked out — but the failure itself is the lesson: pacing discipline
exists to catch problems before they compound, and skipping it removes exactly
that margin.

## 6. What was deliberately excluded from `server/`, and why

91 real files from the runtime clone's `server/core/` were excluded by
category, not oversight: **platform operations** (worker pools, accounting,
metrics, quotas — Anvil's hosted platform's internal infrastructure, never
seen by an app builder); **SSO protocol internals below what app code touches**
(relevant only for debugging a genuine protocol-level failure); **the runtime's
own build/test tooling** (exists to build the runtime, not an app);
**`app-server/` packaging and standalone-hosting code** (relevant only to
self-hosting the platform, a deployment model this project has explicitly
decided never to use).

## 7. Where this sits relative to the rest of the system

- **Relative to GBrain:** searchable through its host source
  (`mybizz-config-docs`), synced the ordinary way. **No Memory Governor bypass**
  — a deliberate, settled distinction: `anvil-agent-references` is pure vendor
  material with nothing to judge, while this corpus embeds real reorganization
  and synthesis decisions, so the "nothing to judge" rationale would be false
  here. The practical expression of the same judgment is the corpus's own
  principle: the files, not any summary of them, are the ground truth.
- **Relative to Cupcake:** no dedicated rule targets the corpus. The
  cross-project grants once recorded for it no longer exist (grants file
  verified empty, 2026-09-06) — and none are needed for ordinary in-project
  work, since the corpus lives inside the current project. Enforcement status
  is a changeable fact (see `cupcake-config.md`'s Current Operational Status);
  none of the corpus's own rules depend on it.
- **Relative to `anvil-agent-references`:** complements, not duplicates. The
  vendor layer is generated from Anvil's source and stays authoritative through
  its release workflow; this corpus is a frozen, pinned snapshot (commit
  `34067eb` — which was upstream HEAD at verification) plus the full
  documentation scrape. The skills say how to work; the corpus says what the
  platform actually is.
- **Relative to PDLF:** the on-disc authoritative Anvil reference beneath
  PDLF's Anvil application work — the deep layer that makes the platform's
  real behavior checkable without leaving the machine.
- **Relative to security-global:** the supply-chain review standard applies to
  the corpus's adoption; publishers are the platform vendor itself and the
  absorbed commit was upstream HEAD, but no adoption review is on record, and
  the AGPL licence of the absorbed source is documented rather than formally
  assessed — both recorded as open items, not silently resolved.

## 8. Known limitations, honestly stated

**No standing backup exists.** The corpus's own construction learned this the
hard way once; every bulk operation carries the count-discipline requirement.

**The docs side is a snapshot.** Scrape window 2026-09-02 → 2026-09-04; the
live site can drift. The strip tool makes single-page correction cheap; a full
re-scrape would be a deliberate construction event.

**The `_components.py` orphan is now doubly unresolved.** Upstream: confirmed,
directly, that no real source file exists anywhere in the original checkout.
Locally: the prior suite's claim that two plain-text orphan notes exist in the
corpus did not survive verification — a name-based search finds no such files.
What is certain: there is no `_components.py` source and this corpus should not
acquire one by inference. What is not certain: where the described notes went.
