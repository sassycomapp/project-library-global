---
title: "spec-testing-methodology-standards"
doc-id: "mb-0ab4d14d"
updated: "2026-10-23"
---
# Testing Methodology

**Location:** `C:\dev\project-library-global\specifications-global\spec-testing-methodology-standards.md`
**Scope:** The testing method every Mybizz application follows. The test suite in `C:\dev\project-library-global\test-suite\` holds the rules ([[[default:test-suite/ts-method]]](C:/dev/project-library-global/test-suite/ts-method.md)), the tests ([[[default:test-suite/ts-catalogue]]](C:/dev/project-library-global/test-suite/ts-catalogue.md)) and the tools; each step's `{step}-test-spec.md` names the tests it runs. A project's own test plan (which flows, which roles) is that project's own document, written at Step 15.

---

## 1. Testing Levels

| Level | Scope | Runtime | Rule |
|---|---|---|---|
| 0 | Static checks of code and schema | Local code folder (`ts_scan.py`) | Before code runs |
| 1 | Pure logic | Local Python (pytest) | On every change |
| 2 | Integration through Uplink | The local Anvil App Server; hosted App 1 only for hosted services | After Level 1 passes |
| 3 | Browser | Hosted App 1 | After a full work increment |
| 4 | Release | App 2, App 3, the test client and every client instance | At release |

## 2. Pure Function Characteristics (Level 1)

- No `import anvil` statements.
- No Data Tables access, no server function calls.
- No side effects.
- Deterministic: time is passed in as an input; money is whole cents.
- Scope: calculations, validations, transformations — not orchestration.

## 3. Test Structure Standard

```python
def test_feature_scenario(load_module):
    """Test: Clear description"""
    module = load_module("server_code/pricing.py")
    # Arrange
    input_value = ...
    expected_output = ...
    # Act
    result = module.function_under_test(input_value)
    # Assert
    assert result == expected_output
```

- Naming: `test_[feature]_[scenario]`, snake_case, grouped by prefix.
- Assertions: plain `assert`. Tests run under pytest, and every test loads the real module, never a copy.
- A failed test stops progress and gets fixed immediately — it is not logged and deferred.

## 4. Integration Testing Safety Protocol (Level 2)

**Where:** first on the Anvil App Server on the developer's computer, started on an empty database each run. Only sign-up and reset emails, real webhooks, scheduled tasks and headers are tested on hosted App 1.

**Before:** all Level 1 tests pass; the Uplink connections are verified (test PR-09); before a hosted run, App 1 is backed up.

**During:** every test value starts with `TEST_`; read before writing; verify each write after it happens.

**After:** clean up test data and verify the cleanup succeeded; after a passing hosted run, App 1 is backed up again. Local runs need no backup.

**Two connections:** a server Uplink key sets up and inspects data only, because it passes every access check. A client Uplink key, signed in as a `TEST_` user of a role, is the only way access rules are proven.

## 5. Common Test Patterns

**Happy path:**
```python
def test_function_valid_input():
    result = function(valid_input)
    assert result == expected_output
```

**Error handling:**
```python
import pytest

def test_function_invalid_input():
    with pytest.raises(ExpectedException, match="expected message"):
        function(invalid_input)
```

**Boundary conditions:** test zero, minimum, and maximum values explicitly — not just "typical"
inputs.

## 6. Test Plan Shape (for any project's own test plan)

A concrete test plan, regardless of project, includes:
- **E2E happy-path specs** per critical flow: preconditions, a numbered steps table (action →
  expected result), a performance gate where relevant, explicit data-validation checks.
- **Edge cases**, listed separately from the happy path.
- **Error-path test cases**, one per named failure scenario, each with its own specific expected
  behavior.
- **An access matrix** (`access-matrix.yaml`), if the project has roles: every server function, form and settings tab against every role.

## 7. RBAC Verification Procedure

1. Every server function carries its access rule, naming exactly the allowed roles; the scanner refuses a server function without one unless it is listed as intentionally public (test ST-02).
2. Every server function is called as every role, and signed out, through the client Uplink key; each call succeeds or is refused exactly as `access-matrix.yaml` says, and a refused call changes nothing (test IN-02).
3. Each role's navigation shows only what it may use: a restricted link is **hidden**, not merely disabled (test BR-03).

```python
@authenticated_endpoint(roles=['Owner', 'Manager', 'Admin'])
def get_contacts():
    ...
```

This procedure runs at Steps 35, 38 and 42A and is a gate condition at `build-verified`.
