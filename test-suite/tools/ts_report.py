#!/usr/bin/env python3
"""Mybizz test suite: receipt counts from saved test output (test PR-05).

Reads every JUnit XML file in a step's output folder (pytest, ts_scan,
ts_contrast, bandit and other tools that write JUnit XML) and prints the counts
a step receipt must carry: per file and in total, passed, failed, for review,
skipped and errors, with every failing test named. Nothing in a receipt's test
counts is written by hand; it is pasted from this output, or checked against
it with --check.

Usage (WSL):
    python3 ts_report.py OUTPUT_FOLDER --prefix {slug}-{step}-{run}- [--markdown OUT.md]
    python3 ts_report.py OUTPUT_FOLDER --prefix {slug}-{step}-{run}- --check RECEIPT.md

--prefix counts only the evidence of one run of the step, because a step's
output folder holds the files of every run (the whole application, and each
feature).
"""
from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def cases(root):
    if root.tag == "testsuites":
        for s in root.iter("testsuite"):
            yield from s.findall("testcase")
    else:
        yield from root.findall("testcase")


def summarise(path: Path) -> dict:
    root = ET.parse(path).getroot()
    out = {"file": path.name, "passed": 0, "failed": 0, "review": 0, "skipped": 0, "errors": 0, "failing": []}
    for c in cases(root):
        name = f"{c.get('classname', '')}::{c.get('name', '')}".strip(":")
        f, e, s = c.find("failure"), c.find("error"), c.find("skipped")
        if e is not None:
            out["errors"] += 1
            out["failing"].append(f"ERROR {name}")
        elif f is not None and f.get("type") == "review":
            out["review"] += 1
            out["failing"].append(f"REVIEW {name}")
        elif f is not None:
            out["failed"] += 1
            out["failing"].append(f"FAIL {name}")
        elif s is not None:
            out["skipped"] += 1
        else:
            out["passed"] += 1
    return out


def render(rows: list[dict], folder: Path) -> str:
    keys = ("passed", "failed", "review", "skipped", "errors")
    total = {k: sum(r[k] for r in rows) for k in keys}
    lines = [f"Test evidence in `{folder}`", "",
             "| File | Passed | Failed | Review | Skipped | Errors |", "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['file']} | " + " | ".join(str(r[k]) for k in keys) + " |")
    lines.append("| **Total** | " + " | ".join(f"**{total[k]}**" for k in keys) + " |")
    failing = [f for r in rows for f in r["failing"]]
    if failing:
        lines += ["", "Not passed:"] + [f"- {f}" for f in failing]
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("folder")
    ap.add_argument("--markdown")
    ap.add_argument("--check", help="a receipt whose Total row must equal the evidence")
    ap.add_argument("--prefix", default="", help="count only files whose name starts with this, e.g. mb-3-cs-b12-app1-")
    a = ap.parse_args(argv)
    folder = Path(a.folder)
    files = sorted(p for p in folder.rglob("*.xml") if p.name.startswith(a.prefix))
    rows = []
    for p in files:
        try:
            rows.append(summarise(p))
        except ET.ParseError:
            rows.append({"file": p.name, "passed": 0, "failed": 0, "review": 0, "skipped": 0, "errors": 1,
                         "failing": [f"ERROR unreadable XML {p.name}"]})
    if not rows:
        print(f"no JUnit XML files in {folder}", file=sys.stderr)
        return 2
    text = render(rows, folder)
    print(text)
    if a.markdown:
        Path(a.markdown).write_text(text, encoding="utf-8")
    if a.check:
        receipt = Path(a.check).read_text(encoding="utf-8")
        m = re.search(r"\|\s*\*\*Total\*\*\s*\|(.*)\|", receipt)
        expected = re.search(r"\|\s*\*\*Total\*\*\s*\|(.*)\|", text).group(1)
        if not m or re.sub(r"\s", "", m.group(1)) != re.sub(r"\s", "", expected):
            print("PR-05 FAIL: the receipt's Total row does not match the evidence", file=sys.stderr)
            return 1
        print("PR-05 pass: the receipt matches the evidence")
    return 0


if __name__ == "__main__":
    sys.exit(main())
