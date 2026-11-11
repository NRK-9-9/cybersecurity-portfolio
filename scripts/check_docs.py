#!/usr/bin/env python3
"""Check local Markdown links and required documents, without network access."""
import re
from pathlib import Path
from urllib.parse import unquote
root = Path(__file__).resolve().parents[1]
errors = []
for required in ("README.md", "AGENTS.md", "SECURITY.md", "CONTRIBUTING.md"):
    if not (root / required).is_file():
        errors.append(f"Missing required document: {required}")
files = list(root.rglob("*.md"))
for file in files:
    if ".git" in file.parts:
        continue
    body = file.read_text(encoding="utf-8")
    if not body.strip():
        errors.append(f"Empty document: {file.relative_to(root)}")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
        target = target.strip().split(" ")[0].strip("<>")
        if not target or target.startswith(("#", "https://", "http://", "mailto:")):
            continue
        path = unquote(target.split("#")[0])
        if not (file.parent / path).resolve().exists():
            errors.append(f"{file.relative_to(root)}: missing link target {path}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: required documents, nonempty Markdown and local file links ({len(files)} documents).")
