# Rule: No Test Tampering

## Harness
opencode

## What to block
Any file-writing tool call (edit, write, or equivalent) where the target
file matches a known test-file pattern (e.g. `test_*.py`, `*_test.py`,
`*.test.js`, `*.test.ts`, `*.spec.ts`), and either:
- the tool call is a full file delete or overwrite of that test file, OR
- the content being written adds a skip marker (`@skip`,
  `@pytest.mark.skip`, `it.skip`, `describe.skip`, `xit`, `xdescribe`,
  or an equivalent), OR
- the content being written removes an existing `assert`/`expect` line
  present in the prior version of the file.

## Decision
Block (deny). Do not allow the change to proceed.

## Message shown to the agent on block
"Tests are protected verification artifacts. Do not delete, skip, or
remove an assertion to make a failure disappear. Fix the underlying
problem instead. If the test itself is genuinely incorrect, stop and ask
the developer for explicit approval before changing it."

## Reason
This is the single most commonly and consistently reported AI coding
failure mode: an agent asked to fix a failing test deletes, skips, or
guts the test instead of fixing the real bug, then reports success. A
green test suite produced this way is false evidence, not a genuine fix.
