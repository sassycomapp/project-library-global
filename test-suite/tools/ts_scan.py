#!/usr/bin/env python3
"""Mybizz test suite: static and conformance scanner for an Anvil app folder.

Runs the automatic checks of the test catalogue's ST tests (ST-02 to ST-12)
over one Anvil app folder and writes a JUnit XML report: one test case per
check, named with the catalogue test it belongs to. A check fails when it finds a violation. A check that only flags
lines for review is reported as a failure of type "review"; it passes once the
review note confirms each flagged line (the catalogue entry says so).

Usage (WSL):
    python3 ts_scan.py APP_DIR [--config tests/ts-config.yaml]
                       [--junit OUT.xml] [--role app1|app2|app3|client_instance]

Needs Python 3.10 and PyYAML. Reads only; never changes the app.
"""
from __future__ import annotations

import argparse
import ast
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - reported to the user
    sys.stderr.write("ts_scan needs PyYAML: pip install pyyaml\n")
    sys.exit(2)


# --------------------------------------------------------------------------- model

@dataclass
class Finding:
    path: str
    line: int
    message: str


@dataclass
class Result:
    test_id: str
    title: str
    findings: list[Finding] = field(default_factory=list)
    review: bool = False          # findings need review rather than being violations
    skipped: str | None = None    # reason the check does not apply
    note: str = ""

    @property
    def status(self) -> str:
        if self.skipped:
            return "skipped"
        if not self.findings:
            return "passed"
        return "review" if self.review else "failed"


DEFAULT_CONFIG = {
    "role": "app1",
    "access_decorators": ["require_role"],
    "rate_limit_markers": ["rate_limited"],
    "public_functions": [],
    "public_endpoints": [],
    "webhook_paths": [],
    "management_paths": [],
    "vault_module": "",
    "constants_module": "",
    "outbound_module": "",
    "pure_modules": [],
    "approved_dependencies": ["4UK6WHQ6UX7AKELK", "3PIDO5P3H4VPEMPL"],
    "core_tables": [],
    "approved_client_views": [],
    "approved_components": [],
    "max_remember_me_days": 7,
    "max_mfa_timeout_days": 7,
    "allow_embedding": False,
    "allow_signup": None,
}

SECRET_PATTERNS = [
    (re.compile(r"\bsk_(live|test)_[0-9A-Za-z]{10,}"), "Stripe secret key"),
    (re.compile(r"\brk_(live|test)_[0-9A-Za-z]{10,}"), "Stripe restricted key"),
    (re.compile(r"\bsk_(live|test)_[0-9a-f]{20,}"), "Paystack secret key"),
    (re.compile(r"\bxkeysib-[0-9a-f]{20,}"), "Brevo API key"),
    (re.compile(r"\bxsmtpsib-[0-9a-f]{20,}"), "Brevo SMTP key"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"), "AI provider key"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "access key id"),
    (re.compile(r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----"), "private key"),
    (re.compile(r"Bearer\s+[A-Za-z0-9._~+/-]{20,}"), "bearer token"),
    (re.compile(r"(?i)(password|passwd|secret|api_key|apikey|token)\s*[:=]\s*['\"][^'\"\s]{8,}['\"]"),
     "credential in a string"),
]

COLOUR_RE = re.compile(r"#[0-9A-Fa-f]{3,8}\b|\b(rgba?|hsla?)\s*\(")
TENANT_RE = re.compile(r"\b(tenant|tenant_id|org_id|organisation_id|organization_id|instance_id)\b", re.I)
URL_RE = re.compile(r"^https?://")
MONEY_RE = re.compile(r"(price|amount|total|tax|discount|fee|balance)", re.I)
BANNED_COMPONENTS = ("HtmlTemplate", "HTMLTemplate", "HtmlPanel", "Label", "SidesheetContent")
EXTRAS_HINT = re.compile(r"anvil_extras|anvil-extras", re.I)
SECRET_COLUMN_RE = re.compile(r"(secret|password|api_key|private_key|token|smtp_key|access_key)", re.I)
TIME_NAME_RE = re.compile(r"(_at|_on|_date|_time|^date|^time)$", re.I)
SENSITIVE_RANDOM_RE = re.compile(r"(token|code|key|secret|otp|nonce|salt|password)", re.I)


# --------------------------------------------------------------------------- helpers

def rel(app: Path, p: Path) -> str:
    try:
        return str(p.relative_to(app))
    except ValueError:
        return str(p)


def py_files(app: Path, sub: str) -> list[Path]:
    base = app / sub
    return sorted(base.rglob("*.py")) if base.exists() else []


def parse(path: Path):
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeDecodeError):
        return None


def dotted(node) -> str:
    """Return a dotted name for Name/Attribute/Call nodes, or ''."""
    if isinstance(node, ast.Call):
        return dotted(node.func)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        left = dotted(node.value)
        return f"{left}.{node.attr}" if left else node.attr
    return ""


def decorator_names(fn) -> list[str]:
    return [dotted(d) for d in fn.decorator_list]


def kind_of(fn) -> str | None:
    for name in decorator_names(fn):
        last = name.split(".")[-1]
        if last == "callable":
            return "callable"
        if last in ("http_endpoint", "route"):
            return "endpoint"
        if last == "background_task":
            return "background"
    return None


def endpoint_path(fn) -> str:
    for d in fn.decorator_list:
        if isinstance(d, ast.Call) and dotted(d).split(".")[-1] in ("http_endpoint", "route"):
            if d.args and isinstance(d.args[0], ast.Constant) and isinstance(d.args[0].value, str):
                return d.args[0].value
    return ""


def functions(tree):
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield node


def docstring_nodes(tree) -> set[int]:
    ids = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, "body", [])
            if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant) \
                    and isinstance(body[0].value.value, str):
                ids.add(id(body[0].value))
    return ids


def code_lines(path: Path) -> list[tuple[int, str]]:
    """Lines with comments stripped (simple: text after an unquoted #)."""
    out = []
    for i, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        stripped = re.sub(r"(^|\s)#.*$", "", line)
        out.append((i, stripped))
    return out


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return None


def walk_components(node, found):
    """Collect component dicts from a form_template structure."""
    if isinstance(node, dict):
        if "type" in node and isinstance(node.get("type"), str):
            found.append(node)
        for v in node.values():
            walk_components(v, found)
    elif isinstance(node, list):
        for v in node:
            walk_components(v, found)


# --------------------------------------------------------------------------- scanner

class Scanner:
    def __init__(self, app: Path, cfg: dict):
        self.app = app
        self.cfg = cfg
        self.anvil = load_yaml(app / "anvil.yaml") or {}
        self.server = py_files(app, "server_code")
        self.client = py_files(app, "client_code")
        self.forms = sorted((app / "client_code").rglob("form_template.yaml")) if (app / "client_code").exists() else []
        self.theme = sorted(p for p in (app / "theme").rglob("*") if p.suffix in (".css", ".html")) \
            if (app / "theme").exists() else []
        self.trees = {p: parse(p) for p in self.server + self.client}
        self.results: list[Result] = []

    # -- utility
    def add(self, r: Result):
        self.results.append(r)

    def is_module(self, p: Path, cfgkey: str) -> bool:
        target = self.cfg.get(cfgkey) or ""
        return bool(target) and rel(self.app, p).replace("\\", "/") == target.replace("\\", "/")

    def server_functions(self):
        for p in self.server:
            t = self.trees.get(p)
            if t is None:
                continue
            for fn in functions(t):
                k = kind_of(fn)
                if k:
                    yield p, fn, k

    # -- ST-01 is run by `anvil --json validate .` itself.

    def st02(self):
        r = Result("ST-02", "Every server function carries its access rule")
        access = set(self.cfg["access_decorators"])
        public = set(self.cfg["public_functions"])
        allowed_paths = set(self.cfg["webhook_paths"]) | set(self.cfg["management_paths"]) | set(self.cfg["public_endpoints"])
        for p, fn, k in self.server_functions():
            names = {n.split(".")[-1] for n in decorator_names(fn)}
            if k == "callable" and not (names & access) and fn.name not in public:
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"callable '{fn.name}' has no access decorator and is not on the public list"))
            if k == "endpoint":
                path = endpoint_path(fn)
                if path not in allowed_paths and not (names & access):
                    r.findings.append(Finding(rel(self.app, p), fn.lineno, f"HTTP endpoint '{path or fn.name}' is not a listed webhook, management or public endpoint"))
        self.add(r)

    def st05(self):
        r = Result("ST-03", "Only the vault service reads Anvil Secrets")
        calls = []
        for p, t in self.trees.items():
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.Call) and dotted(node).endswith("secrets.get_secret"):
                    calls.append((p, node.lineno))
        for p, line in calls:
            if not self.is_module(p, "vault_module"):
                r.findings.append(Finding(rel(self.app, p), line, "anvil.secrets.get_secret called outside the vault-service module"))
        if len(calls) > 1:
            r.findings.append(Finding("(app)", 0, f"{len(calls)} call sites; exactly one is allowed"))
        r.note = f"{len(calls)} call site(s)"
        self.add(r)

    def st06_07(self):
        r6 = Result("ST-03", "No secret is in the code (patterns; gitleaks covers history)")
        r7 = Result("ST-03", "Nothing secret is in client code or theme")
        for p in self.server + self.client + self.theme + [self.app / "anvil.yaml"]:
            if not p.exists():
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            for i, line in enumerate(text.splitlines(), 1):
                for rx, label in SECRET_PATTERNS:
                    if rx.search(line):
                        r6.findings.append(Finding(rel(self.app, p), i, label))
        for p in self.client + self.theme:
            for i, line in code_lines(p):
                if "get_vault_secret" in line or "anvil.secrets" in line:
                    r7.findings.append(Finding(rel(self.app, p), i, "client code reaches for a secret"))
        r7.findings.extend(f for f in r6.findings if f.path.startswith(("client_code", "theme")))
        self.add(r6)
        self.add(r7)

    def st08(self):
        r = Result("ST-04", "No dangerous construct is used")
        bad_calls = {"eval", "exec", "compile", "os.system", "os.popen", "pickle.load", "pickle.loads",
                     "marshal.loads", "__import__"}
        for p, t in self.trees.items():
            if t is None:
                continue
            for node in ast.walk(t):
                if not isinstance(node, ast.Call):
                    continue
                name = dotted(node)
                if name in bad_calls:
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"call to {name}"))
                if name.startswith("subprocess.") and any(
                        kw.arg == "shell" and isinstance(kw.value, ast.Constant) and kw.value.value is True
                        for kw in node.keywords):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, "subprocess with shell=True"))
                if name in ("yaml.load",) and not any(kw.arg == "Loader" for kw in node.keywords):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, "yaml.load without a safe Loader"))
                if name.endswith(".execute") and node.args and isinstance(node.args[0], (ast.JoinedStr, ast.BinOp)):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, "SQL built from a string"))
        self.add(r)

    def st09(self):
        r = Result("ST-05", "Server code logs, never prints")
        for p in self.server:
            t = self.trees.get(p)
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.Call) and dotted(node) == "print":
                    r.findings.append(Finding(rel(self.app, p), node.lineno, "print() in server code"))
        self.add(r)

    def st10(self):
        r = Result("ST-05", "No error is swallowed")
        for p, t in self.trees.items():
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.ExceptHandler):
                    if node.type is None:
                        r.findings.append(Finding(rel(self.app, p), node.lineno, "bare except"))
                    elif all(isinstance(s, ast.Pass) for s in node.body):
                        r.findings.append(Finding(rel(self.app, p), node.lineno, "handler that only passes"))
            for fn in functions(t):
                if re.search(r"save", fn.name, re.I):
                    self.guard_order(p, fn, r)
        self.add(r)

    def guard_order(self, p, fn, r):
        """In a save function, AssertionError must be re-raised before any broad handler."""
        for node in ast.walk(fn):
            if not isinstance(node, ast.Try):
                continue
            types = [dotted(h.type) if h.type is not None else "" for h in node.handlers]
            if "AssertionError" not in types:
                continue
            idx = types.index("AssertionError")
            broad = [i for i, ty in enumerate(types) if ty in ("Exception", "BaseException", "")]
            if broad and min(broad) < idx:
                r.findings.append(Finding(rel(self.app, p), node.lineno,
                                          f"'{fn.name}': a broad handler comes before AssertionError"))

    def st12(self):
        r = Result("ST-05", "Errors reach the client only as plain messages")
        for p, fn, k in self.server_functions():
            if k not in ("callable", "endpoint"):
                continue
            exc_names = {h.name for h in ast.walk(fn) if isinstance(h, ast.ExceptHandler) and h.name}
            for node in ast.walk(fn):
                if isinstance(node, ast.Return) and node.value is not None:
                    for sub in ast.walk(node.value):
                        if isinstance(sub, ast.Call) and dotted(sub) in ("str", "repr") and sub.args \
                                and isinstance(sub.args[0], ast.Name) and sub.args[0].id in exc_names:
                            r.findings.append(Finding(rel(self.app, p), node.lineno, f"'{fn.name}' returns an exception's text"))
                        if isinstance(sub, ast.Call) and dotted(sub).startswith("traceback."):
                            r.findings.append(Finding(rel(self.app, p), node.lineno, f"'{fn.name}' returns a traceback"))
        self.add(r)

    def st13(self):
        r = Result("ST-10", "Public functions are documented and typed")
        for p, fn, k in self.server_functions():
            if k != "callable":
                continue
            missing = []
            if ast.get_docstring(fn) is None:
                missing.append("docstring")
            args = fn.args.args + fn.args.kwonlyargs
            if any(a.annotation is None for a in args if a.arg not in ("self", "cls")) or fn.returns is None:
                missing.append("type hints")
            if missing:
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"'{fn.name}' lacks {' and '.join(missing)}"))
        self.add(r)

    def st14(self):
        r = Result("ST-10", "No address or magic value is hard-coded")
        for p, t in self.trees.items():
            if t is None or self.is_module(p, "constants_module"):
                continue
            docs = docstring_nodes(t)
            for node in ast.walk(t):
                if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docs \
                        and URL_RE.match(node.value):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"address literal {node.value[:60]}"))
        self.add(r)

    def st15(self):
        r = Result("ST-06", "No code separates clients")
        for p, t in self.trees.items():
            if t is None:
                continue
            docs = docstring_nodes(t)
            for node in ast.walk(t):
                hit = None
                if isinstance(node, ast.Name) and TENANT_RE.search(node.id):
                    hit = node.id
                elif isinstance(node, ast.Attribute) and TENANT_RE.search(node.attr):
                    hit = node.attr
                elif isinstance(node, ast.keyword) and node.arg and TENANT_RE.search(node.arg):
                    hit = node.arg
                elif isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in docs \
                        and TENANT_RE.search(node.value):
                    hit = node.value[:40]
                if hit:
                    r.findings.append(Finding(rel(self.app, p), getattr(node, "lineno", 0), f"tenant-style name: {hit}"))
        self.add(r)

    def st16(self):
        r = Result("ST-10", "A client instance holds no code of its own")
        if self.cfg["role"] not in ("app3", "client_instance"):
            r.skipped = "applies to App 3 and client instances"
            self.add(r)
            return
        if self.forms:
            for f in self.forms:
                r.findings.append(Finding(rel(self.app, f), 0, "form in a client instance"))
        if self.server:
            for f in self.server:
                r.findings.append(Finding(rel(self.app, f), 0, "server module in a client instance"))
        client_py = [p for p in self.client]
        if len(client_py) > 1:
            r.findings.append(Finding("client_code", 0, f"{len(client_py)} client modules; only the startup module is allowed"))
        if not any((self.app / n).exists() for n in ("README.md", "readme.md", "README")):
            r.findings.append(Finding("(app)", 0, "README missing"))
        deps = [d.get("resolution_hints", {}).get("app_id", "") for d in self.anvil.get("dependencies", []) or []]
        if not deps:
            r.findings.append(Finding("anvil.yaml", 0, "no dependency on App 2"))
        self.add(r)

    def st18(self):
        r = Result("ST-10", "Only approved dependency apps are used")
        approved = set(self.cfg["approved_dependencies"])
        for d in self.anvil.get("dependencies", []) or []:
            hints = d.get("resolution_hints", {}) or {}
            app_id = hints.get("app_id", "")
            if app_id not in approved:
                r.findings.append(Finding("anvil.yaml", 0, f"dependency {hints.get('name', '?')} ({app_id}) is not approved"))
            if EXTRAS_HINT.search(str(hints)):
                r.findings.append(Finding("anvil.yaml", 0, "Anvil Extras dependency"))
        self.add(r)

    def st23(self):
        r = Result("ST-10", "Nothing test-only is in the application")
        for p, fn, k in self.server_functions():
            if re.match(r"(test|debug|dev_)", fn.name, re.I) or re.search(r"(helper|backdoor)", fn.name, re.I):
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"{k} '{fn.name}' looks test-only"))
        for p in self.server + self.client:
            if p.name.startswith("test_") or p.name.endswith("_test.py"):
                r.findings.append(Finding(rel(self.app, p), 0, "test file inside application code"))
        for p in self.server + self.client:
            for i, line in code_lines(p):
                if re.search(r"\bif\s+.*\b(TEST|DEBUG|TESTING)\b", line):
                    r.findings.append(Finding(rel(self.app, p), i, "branch on a test or debug flag"))
        self.add(r)

    def st24(self):
        r = Result("ST-10", "The repository keeps out what it must")
        gi = self.app / ".gitignore"
        text = gi.read_text(encoding="utf-8") if gi.exists() else ""
        for pat in (".env", "__pycache__", "*.pyc", ".pytest_cache"):
            if pat not in text:
                r.findings.append(Finding(".gitignore", 0, f"does not ignore {pat}"))
        if (self.app / ".git").exists():
            try:
                out = subprocess.run(["git", "-C", str(self.app), "ls-files"], capture_output=True, text=True, timeout=60).stdout
                for f in out.splitlines():
                    if f.endswith(".pyc") or os.path.basename(f) == ".env" or "__pycache__" in f:
                        r.findings.append(Finding(f, 0, "tracked file that must be ignored"))
            except Exception as e:  # git missing: report, do not hide
                r.findings.append(Finding("(git)", 0, f"git ls-files could not run: {type(e).__name__}"))
        self.add(r)

    def st25(self):
        r = Result("ST-08", "Times are made in UTC on the server")
        for p, t in self.trees.items():
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.Call):
                    name = dotted(node)
                    if name.endswith("datetime.now") and not node.args and not node.keywords:
                        r.findings.append(Finding(rel(self.app, p), node.lineno, "datetime.now() without a time zone"))
                    if name.endswith("datetime.utcnow"):
                        r.findings.append(Finding(rel(self.app, p), node.lineno, "datetime.utcnow() gives a naive time"))
                    if p in self.client and (name.endswith("astimezone") or "pytz" in name or "zoneinfo" in name):
                        r.findings.append(Finding(rel(self.app, p), node.lineno, "time zone conversion in client code"))
        self.add(r)

    def st26(self):
        r = Result("ST-08", "Money is never a floating-point sum", review=True)
        for p, t in self.trees.items():
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.Call) and dotted(node) == "float" and node.args \
                        and MONEY_RE.search(ast.unparse(node.args[0])):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"float() on {ast.unparse(node.args[0])[:40]}"))
                if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) and MONEY_RE.search(ast.unparse(node)):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"division on money: {ast.unparse(node)[:50]}"))
        self.add(r)

    def st28(self):
        r = Result("ST-09", "Outbound calls go through the shared caller")
        prefixes = ("anvil.http.request", "requests.", "urllib.request", "httpx.", "http.client")
        for p in self.server:
            t = self.trees.get(p)
            if t is None or self.is_module(p, "outbound_module"):
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.Call) and dotted(node).startswith(prefixes):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"outbound call {dotted(node)} outside the shared caller"))
        self.add(r)

    def st09_webhooks(self):
        r = Result("ST-09", "Webhook handlers verify, log, hand off and return")
        hooks = set(self.cfg["webhook_paths"])
        for p, fn, k in self.server_functions():
            if k != "endpoint" or endpoint_path(fn) not in hooks:
                continue
            calls = [(n.lineno, dotted(n)) for n in ast.walk(fn) if isinstance(n, ast.Call)]
            verify = [ln for ln, name in calls if "verify" in name.lower() or "signature" in name.lower()]
            launch = [ln for ln, name in calls if name.endswith("launch_background_task")]
            if not verify:
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"'{fn.name}' does not verify a signature"))
            if not launch:
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"'{fn.name}' does not hand off to a background task"))
            if verify and launch and min(verify) > min(launch):
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"'{fn.name}' hands off before verifying"))
        if not hooks:
            r.skipped = "no webhook paths listed in ts-config.yaml"
        self.add(r)

    def st29(self):
        r = Result("ST-09", "No search is read without a bound", review=True)
        for p, fn, k in self.server_functions():
            if k != "callable":
                continue
            for node in ast.walk(fn):
                if isinstance(node, ast.Call) and dotted(node) in ("list", "len") and node.args \
                        and isinstance(node.args[0], ast.Call) and dotted(node.args[0]).endswith(".search"):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"{dotted(node)}() over a whole search in '{fn.name}'"))
                if isinstance(node, ast.For) and isinstance(node.iter, ast.Call) and dotted(node.iter).endswith(".search"):
                    r.findings.append(Finding(rel(self.app, p), node.lineno, f"loop over a whole search in '{fn.name}'"))
        self.add(r)

    def st30(self):
        r = Result("ST-02", "Every entry point is rate-limited")
        markers = set(self.cfg["rate_limit_markers"])
        for p, fn, k in self.server_functions():
            if k not in ("callable", "endpoint"):
                continue
            names = {n.split(".")[-1] for n in decorator_names(fn)}
            called = {dotted(c).split(".")[-1] for c in ast.walk(fn) if isinstance(c, ast.Call)}
            if not ((names | called) & markers):
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"{k} '{fn.name}' has no rate-limit marker"))
        self.add(r)

    def st31(self):
        r = Result("ST-09", "Every export is audited", review=True)
        for p, fn, k in self.server_functions():
            if not re.search(r"(export|download|report|backup)", fn.name, re.I):
                continue
            text = ast.unparse(fn)
            if not re.search(r"audit", text, re.I):
                r.findings.append(Finding(rel(self.app, p), fn.lineno, f"'{fn.name}' writes no visible audit record"))
        self.add(r)

    def st34(self):
        r = Result("ST-10", "Anvil's structural rules hold")
        if (self.app / "client_code" / "__init__.py").exists():
            r.findings.append(Finding("client_code/__init__.py", 0, "client_code must not have __init__.py"))
        self.add(r)

    def st35(self):
        r = Result("ST-10", "Pure modules are pure")
        mods = self.cfg["pure_modules"]
        if not mods:
            r.skipped = "no pure modules listed in ts-config.yaml"
            self.add(r)
            return
        for m in mods:
            p = self.app / m
            t = parse(p) if p.exists() else None
            if t is None:
                r.findings.append(Finding(m, 0, "pure module missing or unreadable"))
                continue
            for node in ast.walk(t):
                if isinstance(node, (ast.Import, ast.ImportFrom)):
                    mod = node.module if isinstance(node, ast.ImportFrom) else ",".join(a.name for a in node.names)
                    if mod and re.match(r"(anvil|requests|urllib|httpx|socket|os|subprocess|random|time)\b", mod):
                        r.findings.append(Finding(m, node.lineno, f"imports {mod}"))
                if isinstance(node, ast.Name) and node.id == "app_tables":
                    r.findings.append(Finding(m, node.lineno, "uses app_tables"))
                if isinstance(node, ast.Call) and dotted(node) in ("open", "print") or (
                        isinstance(node, ast.Call) and dotted(node).endswith(("datetime.now", "date.today", "time.time"))):
                    r.findings.append(Finding(m, node.lineno, f"side effect or clock: {dotted(node)}"))
                if isinstance(node, ast.Global):
                    r.findings.append(Finding(m, node.lineno, "changes global state"))
        self.add(r)

    def st37(self):
        r = Result("ST-04", "Email headers cannot be injected", review=True)
        for p, fn, k in self.server_functions():
            params = {a.arg for a in fn.args.args + fn.args.kwonlyargs}
            for node in ast.walk(fn):
                if isinstance(node, ast.Call) and re.search(r"(email\.send|send_email|send_mail)", dotted(node)):
                    for kw in node.keywords:
                        if kw.arg in ("to", "cc", "bcc", "subject", "from_name", "from_address") and \
                                any(isinstance(n, ast.Name) and n.id in params for n in ast.walk(kw.value)):
                            r.findings.append(Finding(rel(self.app, p), node.lineno, f"'{kw.arg}' built from caller input in '{fn.name}'"))
        self.add(r)

    def st39(self):
        r = Result("ST-04", "Random values that guard access are unguessable")
        for p in self.server:
            t = self.trees.get(p)
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call) and dotted(node.value).startswith("random."):
                    targets = " ".join(ast.unparse(tg) for tg in node.targets)
                    if SENSITIVE_RANDOM_RE.search(targets):
                        r.findings.append(Finding(rel(self.app, p), node.lineno, f"{targets} made with {dotted(node.value)}"))
        self.add(r)

    def st41(self):
        r = Result("ST-12", "The Users service and app settings are as required")
        users = None
        for s in self.anvil.get("services", []) or []:
            if str(s.get("source", "")).endswith("users.yml"):
                users = s.get("client_config", {}) or {}
        if self.cfg["role"] in ("app3", "client_instance"):
            r.skipped = "settings are carried by App 2's code and checked there and at RL-10"
            self.add(r)
            return
        if users is None:
            r.findings.append(Finding("anvil.yaml", 0, "Users service is not configured"))
        else:
            def need(cond, msg):
                if not cond:
                    r.findings.append(Finding("anvil.yaml", 0, msg))
            need(users.get("require_secure_passwords") is True, "require_secure_passwords is not on")
            need(users.get("require_mfa") is True, "require_mfa (Require 2-factor authentication) is not on")
            need(users.get("confirm_email") is True, "confirm_email is not on")
            if users.get("allow_remember_me"):
                need((users.get("remember_me_days") or 0) <= self.cfg["max_remember_me_days"],
                     f"remember_me_days is over {self.cfg['max_remember_me_days']}")
            need((users.get("mfa_timeout_days") or 0) <= self.cfg["max_mfa_timeout_days"],
                 f"mfa_timeout_days is over {self.cfg['max_mfa_timeout_days']}")
            if self.cfg["allow_signup"] is not None:
                need(bool(users.get("allow_signup")) == bool(self.cfg["allow_signup"]),
                     "allow_signup differs from the access matrix")
        need_embed = bool(self.anvil.get("allow_embedding")) == bool(self.cfg["allow_embedding"])
        if not need_embed:
            r.findings.append(Finding("anvil.yaml", 0, "allow_embedding differs from the approved setting"))
        self.add(r)

    # -- DD scans
    def tables(self) -> dict:
        db = self.anvil.get("db_schema") or {}
        if isinstance(db, list):  # older layout
            return {t.get("name") or t.get("python_name"): t for t in db}
        return db

    def dd_scans(self):
        tables = self.tables()
        r = {k: Result("ST-06" if k == "DD-06" else "ST-07", t) for k, t in [
            ("DD-02", "Every table refuses client access"),
            ("DD-04", "Core tables can grow without schema changes"),
            ("DD-05", "Every table has its timestamps"),
            ("DD-06", "No column separates clients"),
            ("DD-08", "No column holds a secret"),
            ("DD-13", "The standard log and control tables exist"),
            ("DD-15", "Times are datetimes in UTC")]}
        r["DD-08"].review = r["DD-15"].review = True
        for name, t in tables.items():
            self.dd_table(name, t, r)
        for needed in ("health_log", "audit_log", "error_log", "webhook_log", "rate_limits"):
            if needed not in tables:
                r["DD-13"].findings.append(Finding("anvil.yaml", 0, f"table '{needed}' missing"))
        if not self.cfg["core_tables"]:
            r["DD-04"].skipped = "no core tables listed in ts-config.yaml"
        for res in r.values():
            self.add(res)

    def dd_table(self, name, t, r):
        cols = {c.get("name"): c.get("type") for c in (t.get("columns", []) or [])}
        if (t.get("client") or "none") != "none" and name not in set(self.cfg["approved_client_views"]):
            r["DD-02"].findings.append(Finding("anvil.yaml", 0, f"table '{name}' client access is '{t.get('client')}'"))
        if name in set(self.cfg["core_tables"]) and cols.get("metadata") != "simpleObject":
            r["DD-04"].findings.append(Finding("anvil.yaml", 0, f"core table '{name}' has no Simple Object 'metadata' column"))
        if name != "users" and cols.get("created_at") != "datetime":
            r["DD-05"].findings.append(Finding("anvil.yaml", 0, f"table '{name}' has no datetime 'created_at'"))
        if TENANT_RE.search(name):
            r["DD-06"].findings.append(Finding("anvil.yaml", 0, f"table name '{name}'"))
        for cname, ctype in cols.items():
            if not cname:
                continue
            if TENANT_RE.search(cname) or cname.lower() == "client_id":
                r["DD-06"].findings.append(Finding("anvil.yaml", 0, f"column '{name}.{cname}'"))
            if name not in ("vault", "users") and SECRET_COLUMN_RE.search(cname):
                r["DD-08"].findings.append(Finding("anvil.yaml", 0, f"column '{name}.{cname}' ({ctype})"))
            if TIME_NAME_RE.search(cname) and ctype not in ("datetime", "date"):
                r["DD-15"].findings.append(Finding("anvil.yaml", 0, f"column '{name}.{cname}' is {ctype}"))

    # -- UI scans
    def ui_forms(self, r10, r11, r12):
        approved = set(self.cfg["approved_components"])
        for f in self.forms:
            data = load_yaml(f)
            if data is None:
                r11.findings.append(Finding(rel(self.app, f), 0, "unreadable form template"))
                continue
            comps = []
            walk_components(data, comps)
            for c in comps:
                self.ui_component(f, c, approved, r10, r11)
            text = f.read_text(encoding="utf-8", errors="replace")
            for i, line in enumerate(text.splitlines(), 1):
                if COLOUR_RE.search(line) and "theme:" not in line:
                    r12.findings.append(Finding(rel(self.app, f), i, line.strip()[:70]))
        if not approved:
            r10.skipped = "no approved component list in ts-config.yaml"

    def ui_component(self, f, c, approved, r10, r11):
        ty = c.get("type", "")
        short = ty.split(":")[-1].split(".")[-1] if ty.startswith("form:") else ty
        if short in BANNED_COMPONENTS or ty in BANNED_COMPONENTS:
            r11.findings.append(Finding(rel(self.app, f), 0, f"component type {ty} ({c.get('name', 'container')})"))
        if EXTRAS_HINT.search(ty):
            r11.findings.append(Finding(rel(self.app, f), 0, f"Anvil Extras component {ty}"))
        if approved and ty not in approved and short not in approved and not ty.startswith("form:"):
            r10.findings.append(Finding(rel(self.app, f), 0, f"component type {ty} is not on the approved list"))

    def ui_theme(self, r12, r16):
        for p in self.theme:
            text = p.read_text(encoding="utf-8", errors="replace")
            in_tokens, depth = False, 0
            for i, line in enumerate(text.splitlines(), 1):
                if re.search(r":root\s*\{", line):
                    in_tokens, depth = True, 0
                if in_tokens:
                    depth += line.count("{") - line.count("}")
                    if depth <= 0 and "}" in line:
                        in_tokens = False
                    continue
                if COLOUR_RE.search(line) and not re.match(r"\s*--[\w-]+\s*:", line):
                    r12.findings.append(Finding(rel(self.app, p), i, line.strip()[:70]))
                if re.search(r"@media[^{]*\(\s*(max|min)-width\s*:\s*\d+px", line):
                    r16.findings.append(Finding(rel(self.app, p), i, line.strip()[:70]))

    def ui_loop(self, p, node, r26, r29):
        loopvars = {n.id for n in ast.walk(node.target) if isinstance(n, ast.Name)} if isinstance(node, ast.For) else set()
        for sub in ast.walk(node):
            if isinstance(sub, ast.Lambda) and loopvars:
                used = {n.id for n in ast.walk(sub.body) if isinstance(n, ast.Name)}
                bound = {a.arg for a in sub.args.args + sub.args.kwonlyargs}
                if (used & loopvars) - bound:
                    r26.findings.append(Finding(rel(self.app, p), sub.lineno,
                                                "lambda uses a loop variable without binding it"))
            if isinstance(sub, ast.Call) and dotted(sub).endswith("server.call"):
                r29.findings.append(Finding(rel(self.app, p), sub.lineno, "anvil.server.call inside a loop"))

    def ui_client(self, r26, r27, r29):
        for p in self.client:
            t = self.trees.get(p)
            if t is None:
                continue
            for node in ast.walk(t):
                if isinstance(node, (ast.For, ast.While)):
                    self.ui_loop(p, node, r26, r29)
                if isinstance(node, ast.Call) and dotted(node).endswith("navigate_to"):
                    r27.findings.append(Finding(rel(self.app, p), node.lineno, "navigate_to"))

    def ui_scans(self):
        r10 = Result("ST-11", "Forms use only approved components")
        r11 = Result("ST-11", "No banned component appears")
        r12 = Result("ST-11", "No colour is hard-coded")
        r16 = Result("ST-11", "Responsiveness uses wrap_on (no pixel media queries)")
        r26 = Result("ST-11", "Loop handlers capture their variables")
        r27 = Result("ST-11", "navigate_to is not used")
        r29 = Result("ST-11", "No server call inside a loop")
        self.ui_forms(r10, r11, r12)
        self.ui_theme(r12, r16)
        self.ui_client(r26, r27, r29)
        for r in (r10, r11, r12, r16, r26, r27, r29):
            self.add(r)

    def run(self) -> list[Result]:
        for check in (self.st02, self.st05, self.st06_07, self.st08, self.st09, self.st10, self.st12,
                      self.st13, self.st14, self.st15, self.st16, self.st18, self.st23, self.st24,
                      self.st25, self.st26, self.st28, self.st09_webhooks, self.st29, self.st30, self.st31, self.st34,
                      self.st35, self.st37, self.st39, self.st41, self.dd_scans, self.ui_scans):
            try:
                check()
            except Exception as e:  # a broken check is a failure, never a pass
                name = getattr(check, "__name__", "check")
                self.add(Result(name.upper().replace("_", "-"), f"check {name} crashed",
                                findings=[Finding("(scanner)", 0, f"{type(e).__name__}: {e}")]))
        return self.results


# --------------------------------------------------------------------------- output

def write_junit(results: list[Result], path: Path, app: Path, elapsed: float):
    suite = ET.Element("testsuite", name=f"ts_scan {app.name}", tests=str(len(results)),
                       failures=str(sum(r.status in ("failed", "review") for r in results)),
                       skipped=str(sum(r.status == "skipped" for r in results)),
                       errors="0", time=f"{elapsed:.2f}")
    for r in results:
        case = ET.SubElement(suite, "testcase", classname="ts_scan", name=f"{r.test_id} {r.title}")
        if r.status == "skipped":
            ET.SubElement(case, "skipped", message=r.skipped)
        elif r.status in ("failed", "review"):
            body = "\n".join(f"{f.path}:{f.line}: {f.message}" for f in r.findings)
            el = ET.SubElement(case, "failure", type=r.status,
                               message=f"{len(r.findings)} finding(s){' (review)' if r.review else ''}")
            el.text = body
        if r.note:
            ET.SubElement(case, "system-out").text = r.note
    path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(suite).write(path, encoding="utf-8", xml_declaration=True)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("app_dir")
    ap.add_argument("--config")
    ap.add_argument("--junit")
    ap.add_argument("--role", choices=["app1", "app2", "app3", "client_instance"])
    a = ap.parse_args(argv)
    app = Path(a.app_dir).resolve()
    if not (app / "anvil.yaml").exists():
        print(f"not an Anvil app folder (no anvil.yaml): {app}", file=sys.stderr)
        return 2
    cfg = dict(DEFAULT_CONFIG)
    cfg_path = Path(a.config) if a.config else app / "tests" / "ts-config.yaml"
    if cfg_path.exists():
        cfg.update(load_yaml(cfg_path) or {})
    else:
        print(f"note: no config at {cfg_path}; defaults used", file=sys.stderr)
    if a.role:
        cfg["role"] = a.role
    start = time.time()
    results = Scanner(app, cfg).run()
    elapsed = time.time() - start
    width = max(len(r.test_id) for r in results)
    for r in results:
        print(f"{r.test_id:<{width}}  {r.status:<7}  {r.title}" + (f"  [{len(r.findings)}]" if r.findings else ""))
        for f in r.findings[:15]:
            print(f"{'':<{width}}    {f.path}:{f.line}: {f.message}")
        if len(r.findings) > 15:
            print(f"{'':<{width}}    ... {len(r.findings) - 15} more in the JUnit report")
    if a.junit:
        write_junit(results, Path(a.junit), app, elapsed)
    failed = sum(r.status == "failed" for r in results)
    review = sum(r.status == "review" for r in results)
    print(f"\n{len(results)} checks: {sum(r.status == 'passed' for r in results)} passed, "
          f"{failed} failed, {review} for review, {sum(r.status == 'skipped' for r in results)} skipped")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
