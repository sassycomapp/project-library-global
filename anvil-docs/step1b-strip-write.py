#!/usr/bin/env python3
"""Step 1b pipeline: strip site chrome from webfetch markdown and write the
article body into a scaffold placeholder file, preserving its existing
frontmatter byte-for-byte.

Usage:
    python3 step1b-strip-write.py TARGET_RELPATH < RAW_MARKDOWN_FILE

  TARGET_RELPATH   path relative to ROOT (e.g. "overview/faq.md")
  RAW_MARKDOWN     the webfetch tool's markdown output for that page, on stdin

Strip rule (validated on the Overview pilot — both anchors held):
  start = first line matching ^#  (the page's own H1 heading)
  end   = first line at/after start that is a footer marker:
            - "### Do you still have questions?"  (case-insensitive), or
            - "TM[]("                              (universal footer logo marker)
  Then walk back from `end` over blank lines and a single trailing "---"
  separator, so the chrome rule sitting between body and footer is excluded.
  The article body is the slice [start, j] inclusive. No other rewriting.

Unicode is preserved byte-faithfully: the script never touches characters
inside the slice (curly apostrophes, em/en dashes pass through untouched).
"""
import os
import re
import sys

ROOT = "/mnt/c/mybizz/config/anvil/anvil-synthesized-reference"

H1_RE = re.compile(r"^#\s")
FAQ_RE = re.compile(r"^###\s+Do you still have questions\??\s*$", re.IGNORECASE)


def strip_article(lines):
    start = None
    for i, ln in enumerate(lines):
        if H1_RE.match(ln):
            start = i
            break
    if start is None:
        raise SystemExit("ERROR: no H1 (^# ) found — cannot strip")

    end = None
    for i in range(start, len(lines)):
        if FAQ_RE.match(lines[i]) or lines[i].startswith("TM[]("):
            end = i
            break
    if end is None:
        raise SystemExit("ERROR: no end marker found — cannot strip")

    # Exclude the chrome separator between body and footer:
    #   <body>\n\n---\n\n### Do you still have questions?
    j = end - 1
    while j >= start and lines[j].strip() == "":
        j -= 1
    if j >= start and lines[j].strip() == "---":
        j -= 1
        while j >= start and lines[j].strip() == "":
            j -= 1
    return lines[start : j + 1]


def read_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    dashes = 0
    idx = 0
    for i, ln in enumerate(lines):
        if ln.strip() == "---":
            dashes += 1
            if dashes == 2:
                idx = i
                break
    return "\n".join(lines[: idx + 1])


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    relpath = sys.argv[1]
    raw = sys.stdin.read()
    body_lines = strip_article(raw.splitlines())
    body = "\n".join(body_lines).rstrip("\n") + "\n"

    path = os.path.join(ROOT, relpath)
    fm = read_frontmatter(path)
    final = fm + "\n\n" + body
    with open(path, "w", encoding="utf-8") as f:
        f.write(final)
    print(
        "WROTE %s | body_lines=%d | total_bytes=%d"
        % (relpath, len(body_lines), len(final.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
