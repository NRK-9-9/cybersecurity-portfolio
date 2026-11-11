# Minimal development environment

Use Default Codex Cloud with this repository selected. Read AGENTS.md first. Documentation requires Git, Python 3 and a text editor; no custom environment snapshot, application server, SIEM, Vercel account or production credentials are needed.

Run `python3 scripts/check_docs.py` and `git diff --check`. In the academy also run `python3 scripts/check_synthetic_events.py`. These checks do not contact external systems. They validate document links/fixture structure, not security effectiveness or professional proficiency.

Use separate company-authorized tasks for real source reviews. Keep company evidence out of personal repositories. For ordinary application code changes in other tasks, inspect that repository's instructions and install only its required pinned dependencies; dependency installation is not needed for initial static review.

A saved custom environment is optional. Committed instructions and standard-library checks make the documentation workflow portable. A fresh Default instance has not been provisioned or tested here; verify tool availability at task start.
