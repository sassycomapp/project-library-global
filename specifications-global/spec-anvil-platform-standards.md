---
document: PDLF Standards Library — Anvil Platform Mechanics
doc-id: global-0057
state: Live
date-created: 2026-07-25
---
# PDLF Standards Library — Anvil Platform Mechanics

**Location:** `C:\pdlf\standards-library\anvil-platform-standards.md`
**Scope:** Project-agnostic. Extracted patterns and rules — not any single project's specific
values, keys, or data.
**Source:** Extracted from `mb-3-cs` project documentation (anvil-spec-table.md, architecture.md,
scaffold-spec.md), generalized for reuse across any PDLF-run Anvil project.

---

## 1. Form File Structure

- Forms are folders: `FormName/`
- Code lives in `FormName/__init__.py`
- Designer config lives in `FormName/form_template.yaml`
- **Never modify `form_template.yaml` programmatically** — it's Designer-managed.

## 2. Server Function Pattern

Every server function should:
- Return a response envelope, not a bare value or exception:
  ```python
  {'success': True, 'data': result}
  {'success': False, 'error': msg}
  ```
- Have a docstring with Args, Returns, Raises.
- Have type hints on all public functions.
- Log via `logging.getLogger(__name__)` — never `print` in server code.
- Check authentication at entry: `user = anvil.users.get_user()`.
- Avoid bare `except:` and `except: pass` — preserve tracebacks with `raise` / `raise ... from e`.

## 3. Three-Tier Module Pattern (+ Pure Logic)

1. **Forms** — presentation only. Event handlers call methods; methods contain logic.
2. **Client Modules** — UI coordination, input validation, server-call orchestration.
3. **Server Modules** — business rules, persistence, security enforcement, external API calls.
4. **Pure Logic Modules** — zero Anvil imports, no side effects, deterministic. This is what
   makes Level 1 testing possible (see `testing-methodology-standards.md`) — not a style
   preference.

## 4. Data Binding Pattern

- Set `self.item` before calling `self.init_components()`.
- **Write Back toggle (W) must be enabled in the Designer's Data Bindings panel** — it cannot be
  set in code.
- Call `refresh_data_bindings()` after modifying `self.item` in place.
- Do not use data bindings on forms that manage their own server calls directly (e.g. settings
  forms) — the two patterns conflict.

## 5. Background Tasks

- Decorator: `@anvil.server.background_task`
- No timeout limit (unlike the standard server call's ~30-second limit).
- **Threshold rule:** any operation expected to exceed roughly 75% of the server-call timeout
  (i.e. ~22 seconds against a 30-second limit) must use a background task instead of a normal
  server call.

**Plan-dependent limits:**

| Plan | Timeout | Scheduled Tasks | Notes |
|---|---|---|---|
| Free | 30 seconds | None | Core background-task-dependent features non-functional |
| Personal | Limited | Limited | Insufficient for production use |
| Business | Unlimited | Available | Required for any production deployment using this pattern |

**[EXAMPLE]** For a multi-instance deployment (e.g. 100 client instances, each running
several scheduled tasks — health heartbeat, reminders, webhook processing), verify total
per-account task load against the Business plan's actual limits before scaling further.
The specific instance count and task list are project data — track them in that project's
own deployment/authoritative-schema documents, not here.

## 6. Uplink — Mechanics and Safety

Full testing usage: see `testing-methodology-standards.md`. Platform mechanics:

```python
import anvil.server, os
anvil.server.connect(os.environ['ANVIL_UPLINK_KEY'])
try:
    result = anvil.server.call('server_function_name')
finally:
    anvil.server.disconnect()
```

- Always use a **Server** Uplink key for server-side work (not Client).
- **Never hardcode Uplink keys** — read from environment variables.
- Always disconnect after the operation.
- Restart the Anvil server runtime after making changes in the Designer, before the next Uplink
  session — stale runtime state is a real, documented failure mode.
- Uplink-connected code can call an app's *own* already-deployed server-module functions directly
  (`anvil.server.call('function_name')`), not only functions defined in the Uplink script itself —
  this is what makes remote integration testing possible without a browser.

## 7. Deployment Environments

- Anvil deploys via named Deployment Environments, each with its own URL, code version
  (branch/commit), and database — not a generic CI/CD pipeline.
- Code can branch on environment to avoid per-deploy edits:
  ```python
  if anvil.app.environment.name == "Production":
      ...
  elif anvil.app.environment.name == "Staging":
      ...
  ```
- Rollback is re-pointing an environment to a different commit and republishing — not a code
  revert, which does not un-publish an app.

## 8. Debugging Tools (Interactive, Not Autonomous)

- **Interactive Debugger**: breakpoints, call-stack inspection, works client- and server-side.
  Breakpoints only fire in the Development Environment, never in published versions.
  Server-code breakpoints require the Business Plan or above.
- **Server Console / App Console**: Python REPLs for manually executing and inspecting code.
- These are tools for a human at the keyboard. There is no confirmed autonomous "runs tests and
  repairs code by itself" capability built into Anvil.works — don't assume one exists without
  direct confirmation.

## 9. Anvil AI — UI Construction Inputs

Anvil AI can build a competent Designer UI, but needs three specific inputs, not one:
1. Wireframe HTML
2. Screen HTML (see `screen-and-wireframe-production-standards.md`)
3. A screen PNG (rendered from the screen HTML via an external tool)

Given all three, it also wires components to their code-behind functions as part of the build.

**Vault System:** For the two-level secrets model, enforcement/masking pattern, implementation, and TOTP recovery — see `spec-vault-system.md`. This document does not duplicate that content.

## 10. RBAC and Data Access Pattern

- Every server function operating on application data carries an RBAC decorator
  (`@require_role` / `@require_permission` or equivalent).
- Role enforcement is always server-side. Client-side navigation visibility (hiding a nav link
  for a restricted role) is a UX convenience only — never the actual security boundary.
- All Data Tables are set to "No access" for client code, without exception. All data access
  goes through server functions, which enforce authentication and input
  validation that direct client access would bypass.

## 11. Rate Limiting Pattern

Enforce rate limits via a Data Table, not an in-memory counter — a Data Table survives server
restarts and works correctly across Anvil's multi-server environment; an in-memory counter does
not. Clean up expired rate-limit records on a background task schedule rather than letting the
table grow unbounded.

## 12. Shared Numeric Security Standards

These values are fixed platform defaults — the same values referenced by both a project's
canonical security document and its development policy, so they exist in exactly one place:

| Standard | Value |
|---|---|
| Password minimum length | 8 characters |
| Password complexity | At least one uppercase, one lowercase, one number |
| Rate limit — unauthenticated | 10 requests/minute/IP |
| Rate limit — authenticated | 100 requests/minute/user |
| Session inactivity timeout | 30 minutes |
| Audit log retention | 2 years |
| Background-task threshold | Any operation expected to exceed ~22 seconds (75% of Anvil's 30-second server-call timeout) |

A project may override any of these explicitly in its own canonical document, stating the
override and the reason — never silently diverge.

## 13. Data Table Access Patterns

- **Row identification:** use Anvil's built-in Row IDs (`row.get_id()`). Do not create custom
  auto-increment columns.
- **Table linking:** store Row objects directly in link columns, not integer IDs. Each client
  instance has its own isolated database — no tenant discriminator columns or tenant-filtered
  queries are needed. See `dependency-based-not-multi-tenant` ADR.
- **Mandatory columns:** `created_at` (datetime) and `updated_at` (datetime, if the row is
  mutable) on every table.
- **Query patterns:** `get()` for a single record (returns `None` if not found); `search()` for
  multiple records (returns a `SearchIterator`); paginate with slicing (`[:50]`); sort with
  `tables.order_by()`; avoid converting a `SearchIterator` to a list unless actually necessary.
- **Transactions:** use `@tables.in_transaction` for counter increments and any multi-step
  operation that requires atomicity.

## 14. Constants

No hardcoded URLs, API keys, or magic strings in code. Use a dedicated `constants.py` module.
Sensitive values go in Anvil Secrets or the Vault (see `spec-vault-system.md`), never in `constants.py` itself.

## 15. Global Client-Side Error Handler

Register one global handler rather than relying solely on per-call `try/except`:

```python
def global_error_handler(err):
    anvil.server.call('log_error_to_server', repr(err))
    alert("An unexpected error occurred. Please try again.", title="System Error")

anvil.set_default_error_handling(global_error_handler)
```

## 16. File and Module Naming Conventions

| Element | Convention | Example |
|---|---|---|
| Folders | PascalCase | `ServerAuth`, `ContactListForm` |
| Files | lowercase_with_underscores | `contact_service.py` |
| Server modules | `{purpose}_service.py` | `booking_service.py` |
| Integration modules | `{purpose}_integration.py` | `brevo_integration.py` |
| Client modules | `{purpose}_utils.py` | `validation_utils.py` |
| Database tables | lowercase_snake | `contacts`, `bookings` |
| Link columns | `{table}_id` or singular name | `contact_id`, `service_id` |

A project's own terminology mapping (e.g. what "Client" vs "Customer" means for that business)
belongs in that project's own nomenclature document, not here — this table is the reusable
file/module naming pattern only.

## 17. Platform Constraints Checklist

Every design decision is verified against Anvil's platform boundaries. This checklist captures
the known constraints as a structured catalog with ADR back-references:

| Constraint | Description | ADR |
|---|---|---|
| Skulpt client runtime | Client-side Python is Skulpt, not CPython — no native Python libraries | design-rules |
| No native URL routing | Anvil forms, not URL-based routing | navigation-lambda-link-open-form |
| Lazy-loaded Data Tables | Tables load progressively; no eager bulk queries | data-access-patterns |
| Server call latency | Every `anvil.server.call()` is a network round-trip | design-rules |
| No WebSocket push | Real-time is polling, not push | real-time-and-background-tasks |
| No complex aggregations | Data Tables have no GROUP BY / aggregate query support | data-access-patterns |
| Designer-first forms | Anvil Designer work precedes code work for any given form | design-rules |

Before any design decision, run this checklist. If a decision conflicts with a constraint,
it must be justified and documented as an ADR.

## 18. Timezone Architecture Pattern

All datetimes are stored as UTC in Data Tables. The client's IANA timezone string is stored
in the business profile. All conversion to local time occurs at display time in server
functions only.

**Why server-side only:** Anvil's Skulpt client runtime cannot reliably handle timezone logic.
Server modules use `pytz` and standard Python `datetime` to convert, format, and return
localized display strings. Client code receives pre-formatted strings, never raw datetimes
to convert.

## 19. Globals Contract Pattern

Every shared state variable in `globals.py` is documented with a standardized template:

| Field | Content |
|---|---|
| Variable name | The attribute name on `globals` |
| Type | Python type annotation |
| Set by | Which form or module sets the value |
| Read by | Which forms or modules read it |
| None behavior | What happens when the value is `None` |

**Binding rules:**
1. Every reader form uses `getattr(globals, 'var_name', None)` — never direct attribute
   access. Direct access raises `AttributeError` if the variable was never set.
2. Every `None` case has a documented recovery action (redirect to a list form or initialize
   an empty container).
3. Multi-step flow state uses a dict with explicitly documented keys, and is cleared on
   completion or cancellation.
4. The globals contract document is a living file — it is updated whenever a new shared
   variable is added or an existing one changes behavior.

## 20. Anvil-First Mandate

Every technical decision defaults to Anvil's built-in facilities. A 5-step escalation is
mandatory before any custom implementation is permitted:

1. Check Anvil's built-in components and services
2. Check Anvil documentation for native solutions
3. Check Anvil's example apps for established patterns
4. Check the Anvil community forum for community approaches
5. Only then consider a custom implementation — and document the justification

A named exception exists for components that genuinely have no Anvil equivalent (The Vault
serves as the canonical example of a justified step-5 custom component). Any exception
must cite either platform impossibility or a specific, measurable limitation of the
built-in facility.

## 21. Enforcement Severity Classification

Development policy violations are classified into four enforcement tiers with explicit
triggers and responses:

| Severity | Triggers | Response |
|---|---|---|
| **Critical** | Security issues, RBAC violations, secret-handling errors, code returning sensitive data to client | Immediate fix — do not proceed past this step |
| **High** | Policy violations, design standard breaches | Fix before moving to next task |
| **Medium** | Naming convention deviations, missing documentation | Fix before shipping (accumulate, address together) |
| **Low** | Style inconsistencies, formatting differences | Logged for improvement cycle; does not block progress |

Any violation classified as Critical or High that is found during a sanity audit (Steps 8a,
15c) blocks the gate. The gate does not pass until all Critical and High violations are
resolved.

## 22. Skulpt Runtime — Known Module Limitations

§17 flags Skulpt as a constraint; this section is the operational detail behind that flag.
Anvil's client-side Python runs on Skulpt (a Python-to-JavaScript compiler), not CPython —
not all Python 3 standard library modules behave identically.

| Area | Issue | Workaround |
|---|---|---|
| `re` module | Subtle bugs and gaps vs. CPython regex | Use server-side for complex regex |
| `json` module | Minor differences in edge cases | Use server-side for critical JSON processing |
| `datetime` | Arithmetic and timezone handling quirks | All date logic lives in server modules |
| Currency formatting | Client-side formatting unreliable | All money display goes through server functions |
| Number formatting | Locale-specific formatting gaps | Server-side formatting for all financial display |

**Rule of thumb:** anything touching money or dates lives in server modules only.
Client-side Skulpt handles UI logic, form handling, and display formatting that involves
no calculation.

## 23. Git Integration Constraint

Anvil's built-in Git integration is one-way friendly (Anvil ← GitHub). Branching and
merging within the Anvil IDE are awkward and error-prone.

**Rule:** all branching and merging happens in GitHub. Never merge branches within the
Anvil IDE.

## 24. Media/File Handling

`BlobMedia` stored directly in Data Tables has row size limits that aren't always
obvious — large file uploads may silently fail or degrade performance.

**Rule:** store file references (URLs) in Data Tables, not file contents. Use external
storage for large media.

## 25. Persistent Server Requirement

Anvil's free tier has no persistent server. The Business plan's persistent server
capability is required for any performance-sensitive operation — do not design a feature
that assumes persistent-server behavior without confirming the plan tier supports it.

## 26. `app_tables` Resolution Failure

When a server module in a shared template app (the app every client instance depends on)
calls `app_tables`, Anvil resolves the tables to the *calling client instance's* Data
Tables. If that instance is corrupted, misconfigured, or missing a required table,
resolution may fail or return incomplete results.

**Required failure behavior:**
- The server function must not crash with a raw 500 error
- Show the user a generic, non-technical message ("Something went wrong. Please try again
  or contact support.")
- Log the failure with status `"unhealthy"` and the specific missing-table detail
- Alert the platform's monitoring/management layer, if one exists
- Never expose internal error detail to the client user

**Prevention:**
- The provisioning clone source (see the Five-App pattern in this operation's project
  templates) must always carry the complete, current table set
- Schema migrations follow the project's own deployment SOP without exception
- A periodic health-check task should verify critical table accessibility

---



*Anvil Platform Standards v1.6 — merged `anvil-platform-constraints.md` (ADR, misfiled —
reclassified as spec content, this file, per single-source-of-truth review). Added §22
Skulpt runtime workarounds (expands §17's existing flag), §23 Git integration constraint,
§24 media/file handling, §25 persistent server requirement, §26 `app_tables` resolution
failure. Background-task plan-tier limits merged into existing §5. Project-specific
figures (client-instance count) stripped or tagged [EXAMPLE]; app names generalized to
role descriptions. Vault TOTP recovery procedure from the source ADR was NOT merged here
— flagged as SOP-shaped content, recommended for `standard-operating-procedures-global`
instead. Prior footer: v1.4 removed `instance_id` references per
`dependency-based-not-multi-tenant` ADR; v1.5 added §17–21.*
