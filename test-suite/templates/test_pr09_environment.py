"""Mybizz test suite: test PR-09, the local test environment works.

Copy to the app repository as tests/integration/test_pr09_environment.py at
Step 11. Run on the local runtime, started with tools/ts_local.sh:

    bash ts_local.sh APP_FOLDER start
    bash ts_local.sh APP_FOLDER run pytest tests/integration/test_pr09_environment.py \
        -m local --junitxml=OUTPUT_FOLDER/{slug}-b11-{run}-pr09.xml

Proves, in order: the server connection reaches the app's data; a client
connection with nobody signed in works; a TEST_ user signs in with a second
factor through a client connection; the mail catcher receives an email the
app sends.
"""
from __future__ import annotations

import email
import mailbox
import os
import time
from pathlib import Path

import pytest

pytestmark = pytest.mark.local


def test_server_connection_reaches_data(server):
    from anvil.tables import app_tables
    # Any read of the Users table proves the connection and the schema.
    list(app_tables.users.search())


def test_client_connection_signed_out(signed_out):
    import anvil.users
    assert anvil.users.get_user() is None


def test_test_user_signs_in_with_second_factor(client_as):
    client_as("Staff")
    import anvil.users
    user = anvil.users.get_user()
    assert user is not None
    assert user["email"].startswith("test_")


def test_mail_catcher_receives_email(test_user, server):
    mail_dir = os.environ.get("TS_MAIL_DIR")
    if not mail_dir:
        pytest.fail("TS_MAIL_DIR is not set; run the test through ts_local.sh")
    user = test_user("Staff")
    import anvil.users
    anvil.users.send_password_reset_email(user["email"])
    deadline = time.time() + 30
    while time.time() < deadline:
        for message in mailbox.Maildir(Path(mail_dir), factory=None, create=False):
            parsed = email.message_from_bytes(message.as_bytes())
            if user["email"] in (parsed.get("To") or ""):
                return
        time.sleep(1)
    pytest.fail("No email reached the mail catcher within 30 seconds")
