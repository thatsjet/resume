#!/usr/bin/env -S uv run python
"""Inject override.css link into resume.html before </head>. Idempotent."""
from pathlib import Path
import sys

HTML_PATH = Path("resume.html")
LINK_TAG = '<link rel="stylesheet" href="override.css">'
HEAD_CLOSE = "</head>"

html = HTML_PATH.read_text(encoding="utf-8")

if LINK_TAG in html:
    print(f"✓ override.css link already present in {HTML_PATH} — no changes")
    sys.exit(0)

idx = html.find(HEAD_CLOSE)
if idx == -1:
    print(f"✗ could not find {HEAD_CLOSE} in {HTML_PATH}", file=sys.stderr)
    sys.exit(1)

updated = html[:idx] + f"  {LINK_TAG}\n  " + html[idx:]
HTML_PATH.write_text(updated, encoding="utf-8")
print(f"✓ injected override.css link into {HTML_PATH} before {HEAD_CLOSE}")
