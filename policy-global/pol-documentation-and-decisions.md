# Policy — Documentation and Decisions

**Binding.** All development work on any Anvil.works project under this operation must
conform. No exceptions without documented justification.

---

## What

### Four Document Kinds, Never Confused

- **Spec** — what must be true. A standing constraint. Doesn't say what to do, says what
  the system is.
- **ADR** — why a decision was made, once, permanently. Doesn't change once accepted;
  gets superseded by a new ADR, not silently edited.
- **Policy** — a rule about how decisions get made and how the team operates. Not a
  technical constraint (that's a spec), not a one-time decision (that's an ADR).
- **SOP** — a repeatable, trigger-based procedure for a recurring operational task.
  Action-oriented: when X happens, do these steps, verify Y.

A document mixing two of these kinds is a defect, not a style choice — split it.

### When an ADR Is Required

A decision gets an ADR only when it clears all three:
1. Hard to reverse
2. Surprising without context
3. Result of a genuine trade-off, not an obvious choice

Most decisions don't clear this bar. Don't write an ADR for every decision — that
produces noise that buries the ones that matter.

### Stale Documentation Is a Failure Condition

A document that no longer reflects reality is not a low-priority cleanup item — it's a
failure condition, the same severity class as a bug in code. A stale spec or policy
actively misleads whoever reads it next.

### No Duplicate Sources of Truth

The same fact does not live authoritatively in two documents. If a spec states a rule and
a policy also states the same rule, one of them is wrong or redundant — resolve it, don't
let both stand.

---

## Why

This operation has repeatedly found the same failure pattern: two documents claiming
authority over the same fact, silently drifting apart until one is simply wrong. The
four-kind split exists so each fact has exactly one correct home. The ADR bar exists
because an ADR for every decision stops functioning as a signal — it's supposed to mark
the decisions worth a future developer reading in full, not document routine choices.

---

## Where

Every project this operation builds, and this operation's own shared documentation
(`specifications-global`, `adr-global`, `policy-global`, `standard-operating-procedures-global`,
`docs-standard-global`, `templates-global`) alike.

**Source:** consolidated from this operation's own document-classification practice.
