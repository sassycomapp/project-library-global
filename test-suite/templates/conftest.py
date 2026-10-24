"""Mybizz test suite: shared pytest fixtures for an Anvil app's tests.

Copy to the app repository as tests/conftest.py at Step 11. Fixtures:

- load_module(path): loads a module by file path, so tests test the real code;
- corpus: the hostile inputs every input test uses;
- server: a privileged Uplink connection, to set up and inspect data only;
- test_user(role): a TEST_ user of that role with its second factor, removed
  afterwards;
- client_as(role): a client Uplink connection signed in as a TEST_ user of
  that role, with its second factor; the only way access rules are proven;
- signed_out: a client connection with nobody signed in;
- parallel(target, args_list): runs target in separate processes at once,
  each with its own connection (race tests);
- automatic on hosted App 1: single-row settings restored and TEST_ users
  removed after every test.

Settings come from .env, never from code:
  TS_TARGET            local | hosted
  TS_UPLINK_URL        ws://localhost:3030/_/uplink (local) or wss://anvil.works/uplink
  ANVIL_UPLINK_KEY     server key          ANVIL_CLIENT_KEY   client key
  TS_TEST_PASSWORD     password for TEST_ users
  TS_ROLE_COLUMN       Users-table column holding the role (default: role)
  TS_SINGLE_ROW_TABLES comma-separated settings tables holding one row
  TS_MAIL_DIR          the local mail catcher's folder, set by tools/ts_local.sh

The Uplink parts are proven by test PR-09 before other tests rely on them.
"""
from __future__ import annotations

import importlib.util
import multiprocessing as mp
import os
import sys
import uuid
from pathlib import Path

import pytest

APP_DIR = Path(__file__).resolve().parent.parent
TARGET = os.environ.get("TS_TARGET", "local")
UPLINK_URL = os.environ.get("TS_UPLINK_URL", "ws://localhost:3030/_/uplink")
ROLE_COLUMN = os.environ.get("TS_ROLE_COLUMN", "role")
PREFIX = "TEST_"

CORPUS = [
    "<script>alert(1)</script>", '"><img src=x onerror=alert(1)>', "javascript:alert(1)",
    "' OR '1'='1", '"; DROP TABLE x; --', "{{7*7}}", "${7*7}",
    '=HYPERLINK("http://example.invalid","x")', "+SUM(1+1)", "-1+1", "@SUM(1)",
    "line one\nline two", "header\r\nBcc: victim@example.invalid", "null\x00byte",
    "right‮to-left", "zero​width", "emoji 😀", "../../etc/passwd",
    '{"__proto__": {"admin": true}}', "1e309", "-0", "", "x" * 10_000,
]


# ----------------------------------------------------------------- Level 1

@pytest.fixture
def load_module():
    def load(relative_path: str):
        path = APP_DIR / relative_path
        name = "ts_" + path.stem
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        return module
    return load


@pytest.fixture
def corpus():
    return list(CORPUS)


# ----------------------------------------------------------------- Level 2

def _key(var: str) -> str:
    value = os.environ.get(var)
    if not value:
        pytest.fail(f"{var} is not set; it belongs in .env")
    return value


def connect(key_var: str):
    import anvil.server
    anvil.server.disconnect()
    anvil.server.connect(_key(key_var), url=UPLINK_URL, quiet=True)
    return anvil.server


def make_test_user(role: str) -> dict:
    """Create a TEST_ user with an authenticator-app second factor (server connection)."""
    import anvil.server
    import anvil.users
    from anvil.tables import app_tables
    connect("ANVIL_UPLINK_KEY")
    email = f"test_{role.lower()}_{uuid.uuid4().hex[:8]}@test.mybizz.invalid"
    password = _key("TS_TEST_PASSWORD")
    user = anvil.users.signup_with_email(email, password) or app_tables.users.get(email=email)
    enrol = anvil.server.call("anvil.private.users.totp.generate_secret", email)
    user.update(enabled=True, confirmed_email=True, mfa=[enrol["mfa_method"]], **{ROLE_COLUMN: role})
    return {"email": email, "password": password, "totp_secret": enrol["secret"]}


def remove_test_users():
    from anvil.tables import app_tables
    connect("ANVIL_UPLINK_KEY")
    for row in app_tables.users.search():
        if (row["email"] or "").startswith("test_"):
            row.delete()


@pytest.fixture
def test_user():
    """Creates TEST_ users of a role on request; removes every TEST_ user afterwards."""
    yield make_test_user
    remove_test_users()


@pytest.fixture
def server():
    conn = connect("ANVIL_UPLINK_KEY")
    yield conn
    conn.disconnect()


@pytest.fixture
def client_as():
    def sign_in(role: str, second_factor: bool = True):
        import pyotp
        user = make_test_user(role)
        conn = connect("ANVIL_CLIENT_KEY")
        import anvil.users
        mfa = {"type": "totp", "code": pyotp.TOTP(user["totp_secret"]).now()} if second_factor else None
        anvil.users.login_with_email(user["email"], user["password"], mfa=mfa)
        return conn
    yield sign_in
    remove_test_users()
    import anvil.server
    anvil.server.disconnect()


@pytest.fixture
def signed_out():
    conn = connect("ANVIL_CLIENT_KEY")
    yield conn
    conn.disconnect()


@pytest.fixture
def parallel():
    def run(target, args_list, timeout: int = 60):
        with mp.get_context("spawn").Pool(len(args_list)) as pool:
            return pool.starmap_async(target, args_list).get(timeout)
    return run


@pytest.fixture(autouse=True)
def hosted_guard():
    if TARGET != "hosted":
        yield
        return
    from anvil.tables import app_tables
    tables = [t for t in os.environ.get("TS_SINGLE_ROW_TABLES", "").split(",") if t]
    connect("ANVIL_UPLINK_KEY")
    saved = {t: dict(getattr(app_tables, t).get() or {}) for t in tables}
    yield
    connect("ANVIL_UPLINK_KEY")
    for t, values in saved.items():
        row = getattr(app_tables, t).get()
        if row is not None and values:
            row.update(**values)
    remove_test_users()
    import anvil.server
    anvil.server.disconnect()
