---
document: Agent Readiness Framework
doc-id: global-0080
state: Live
date-created: 2026-07-25T150027+0200
---
# Agent Readiness Framework

**For:** Development team leads, architects, and prompt engineers  
**Purpose:** Understanding how to prepare codebases for effective autonomous AI-assisted development  
**Not for:** The coding agent itself (use rules-set4 policies instead)

**Last updated:** 2026-04-10  
**Source:** anvil-set3 / Agent Readiness CoP preparation

---

## Core Principle

> **Invisible Bottleneck in AI Coding Tasks**
>
> Uneven performance of AI coding agents is commonly misattributed to the model or agent choice.  
> **The primary limiting factor is typically the codebase environment, not the agent.**

Poor feedback loops and unclear instructions compound inefficiency and negate agent effectiveness.  
Fast feedback, explicit documentation, and deterministic build processes significantly amplify the effectiveness of any AI coding agent.

---

## Key Environment Failures (Eliminate These)

- **Absence of pre-commit hooks** → slow feedback (e.g. long CI wait times instead of immediate validation)
- **Undocumented environment variables** → repeated agent trial-and-error and failures
- **Build/test dependent on tribal knowledge** (e.g. Slack threads) → agent cannot self-verify changes

These are **environment and process deficiencies**, not AI capability issues.

---

## 8 Technical Pillars: Anvil / Python Apps

Use these pillars to audit your codebase and identify gaps. Each pillar directly impacts whether agents can work autonomously.

### 1. Style & Validation

Automated checks to catch errors immediately and enforce consistency across server and client code.

**Anvil/Python Examples:**
- `black` for formatting
- `ruff` or `flake8` for linting
- `mypy` (where applicable) for type checking
- Pre-commit hooks running locally

**Without this:** Agent introduces style or syntax issues, deploys to Anvil, waits for runtime failure, iterates blindly.

**MyBizz Status:** Documented in `policy_development.md`

---

### 2. Build & Run Model (Anvil Context)

Clear, documented rules for how code is executed in Anvil's runtime.

**Anvil/Python Examples:**
- Documented separation of **client code vs server modules**
- Explicit notes on startup behaviour (module import side effects)
- Clear guidance on background tasks and scheduled jobs
- CI checks that mirror Anvil runtime constraints

**Without this:** Agent places logic in the wrong execution context or relies on unsupported runtime behaviour.

**MyBizz Status:** Documented in `policy_development.md` §1

---

### 3. Testing

Fast, deterministic tests that can run outside Anvil before deployment.

**Anvil/Python Examples:**
- `pytest` for server-module logic
- Mocking Anvil APIs (`anvil.server`, `anvil.tables`)
- Test suite runnable locally in < 1 minute
- Test commands documented

**Without this:** Agent cannot validate changes locally and breaks the deployed app.

**MyBizz Status:** See `ref_anvil_testing.md` for testing patterns

---

### 4. Documentation

Explicit capture of Anvil-specific conventions and constraints.

**Anvil/Python Examples:**
- `AGENTS.md` describing:
  - Where business logic belongs (server vs client)
  - How to access Data Tables safely
  - Naming and module conventions
- `README.md` covering app structure
- Architecture notes for forms, services, and tables

**Without this:** Agent guesses Anvil conventions and produces structurally incorrect code.

**MyBizz Status:** Continue.dev rules in `rules-set4/` provide this for MyBizz

---

### 5. Development Environment

Reproducible local tooling aligned with Anvil's Python runtime.

**Anvil/Python Examples:**
- Pinned Python version matching Anvil
- `requirements.txt` for local testing tools
- Mock environment variables documented
- Clear guidance on what *cannot* be reproduced locally

**Without this:** Agent encounters environment mismatches invisible to human developers.

**MyBizz Status:** Required for Phase 1 onboarding

---

### 6. Code Quality

Clear boundaries and small units of logic to fit agent context limits.

**Anvil/Python Examples:**
- Server modules organised by responsibility
- Minimal logic in Forms; UI delegates to server functions
- Small, single-purpose functions
- Avoidance of large "god" server modules

**Without this:** Agent cannot reason about data flow or dependencies within context limits.

**MyBizz Status:** Enforced by `policy_development.md` §3 and `ref_anvil_coding.md`

---

### 7. Observability

Actionable runtime feedback from deployed Anvil apps.

**Anvil/Python Examples:**
- Structured logging in server modules
- Consistent error messages returned to clients
- Centralised error tracking (where available)
- Explicit logging around Data Table access and background tasks

**Without this:** Agent receives vague runtime failures with no diagnostic signal.

**MyBizz Status:** Required for Phase 2+ (production stability)

---

### 8. Security & Governance

Controls aligned with Anvil's secrets and permission model.

**Anvil/Python Examples:**
- Clear rules for:
  - Server-only secrets
  - Never exposing secrets to client code
- Documented use of Anvil's built-in secrets management
- Review requirements for Data Table schema changes

**Without this:** Agent leaks secrets into client code or weakens access controls.

**MyBizz Status:** Enforced by `policy_security.md` and `ref_anvil_coding.md` §2

---

## 5 Maturity Levels

Repositories progress through five levels. Each level represents a qualitative shift in what autonomous agents can accomplish.

### Level 1: Functional

**Code runs, requires manual setup**

Basic tooling signals that every repository should have. Without these, development is unpredictable for humans and impossible for agents.

**Key Signals:**
- README exists
- Linter configured
- Type checker active
- Unit tests present

**Agent Capability:** Agents struggle with simple tasks. High failure rate, constant intervention.

**Examples:** Personal projects, early prototypes

---

### Level 2: Documented

**Workflows are written down**

Documentation and basic automation exist. New contributors can onboard with docs alone.

**Key Signals:**
- AGENTS.md exists
- Reproducible dev env
- Pre-commit hooks
- Branch protection

**Agent Capability:** Simple tasks with supervision. Bug fixes, small features.

---

### Level 3: Standardized

**Production-ready for agents** ← **TARGET FOR MyBizz**

Clear processes defined and enforced. Minimum bar for production-grade autonomous operation.

**Key Signals:**
- E2E tests exist
- Docs maintained
- Security scanning
- Observability

**Agent Capability:** Routine maintenance: bug fixes, tests, docs, dependency upgrades.

**MyBizz Target:** Reach Level 3 by end of Phase 1

---

### Level 4: Optimized

**Fast feedback loops**

Systems designed for productivity. Sub-minute feedback on code quality.

**Key Signals:**
- Sub-minute validation
- Full observability
- Canary deploys
- Build optimization

**Agent Capability:** Complex multi-step tasks. Features, refactoring, migrations.

**MyBizz Timeline:** Phase 2+

---

### Level 5: Autonomous

**Self-improving systems**

Sophisticated orchestration and self-healing. Few organizations reach this level.

**Key Signals:**
- Task decomposition
- Multi-service orchestration
- Self-healing
- Auto-remediation

**Agent Capability:** Portfolio management. Humans set direction, agents execute.

**MyBizz Timeline:** Aspirational for future

---

## How to Use This Framework

### For Team Leads

1. **Audit current state** against the 8 pillars and 5 levels
2. **Identify gaps** in documentation, testing, observability, etc.
3. **Prioritize fixes** — address foundational gaps first (Pillars 1-4)
4. **Measure progress** — track movement through maturity levels

### For Prompt Engineers / Architects

1. **Understand what's missing** in the codebase that prevents autonomous development
2. **Design prompts accordingly** — if testing is weak, provide explicit guidance on manual verification
3. **Request improvements** from the team — "agent is failing because X isn't documented"
4. **Use readiness level** to set expectations on what agents can accomplish

### For Developers / Continue.dev

1. **You don't read this** — you read `rules-set4/` policies instead
2. **But understand why** — the policies exist because the team chose to improve codebase readiness

---

## Evaluation Methodology

### Consistent Evaluations

Agent Readiness evaluates 60+ criteria using LLM-based analysis.

**Stabilisation Approach:**
- Each evaluation is grounded against the repository's previous readiness report
- This enforces continuity and reduces scoring drift

**Observed Impact:**
- Pre-grounding variance: Average 7%, peaks up to 14.5%
- Post-grounding variance: Average 0.6%, sustained over six weeks
- Validation confirmed across 9 benchmark repositories covering low, medium, and high readiness tiers

### Scoring Model

**Binary Criteria:**
- All criteria are binary: pass or fail
- Signals are objective and machine-verifiable:
  - File existence (e.g. `AGENTS.md`, `CODEOWNERS`)
  - Configuration presence and validity (linters, tests, branch protection)
  - Ability to execute checks locally

**Evaluation Scope:**
- **Repository-scoped criteria:** evaluated once per repository (e.g. branch protection enabled, `CODEOWNERS` present)
- **Application-scoped criteria:** evaluated per app in monorepos (e.g. linter and tests configured for each app) — results expressed as ratios

**Level Progression:**
- Each level requires ≥ 80% of criteria at that level, **and** 100% of criteria from all preceding levels
- Enforces dependency order and foundational maturity before higher-level capabilities

**Organization Metrics:**
- Tracked as percentage of active repositories reaching Level 3+
- Example: "80% of active repositories are agent-ready"
- Favoured over aggregate or averaged scores

---

## The Compounding Effect

Improvements compound over time:

- Better environments → more effective agents
- More effective agents → increased capacity
- Increased capacity → further environment improvements

**Teams that measure and iterate systematically gain accelerating advantage.**  
**The maturity gap between teams widens over time.**

### Tool-Agnostic Benefit

Agent readiness improvements are not platform-specific.  
Any AI-assisted development workflow benefits from the same environmental investments.  
Returns persist regardless of agent or vendor choice.

---

## MyBizz Readiness Roadmap

| Phase | Target Level | Key Deliverables |
|-------|------|----------|
| **Phase 1** | Level 3 (Standardized) | policies, docs, tests, linting |
| **Phase 2** | Level 4 (Optimized) | observability, fast feedback loops |
| **Phase 3+** | Level 5 (Autonomous) | self-healing, auto-remediation |

---

**Questions?** Refer to the corresponding `rules-set4/` files for implementation details.
