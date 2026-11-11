# Contribution workflow

1. Pick a scoped documentation task and update its tracker to in progress.
2. Use the appropriate template. Identify synthetic examples prominently.
3. Support claims with evidence and references; record uncertainties.
4. Review privacy and accuracy. Confirm that every artifact is invented or separately cleared for release.
5. Run `python3 scripts/check_docs.py` and `git diff --check`; inspect the complete staged diff.
6. Commit with a descriptive message. Push only within the user's authorization. Prefer reviewable branches for later substantive work.
7. Mark completed only after verification, linking the artifact and review record.

Do not add real company audit artifacts here, even if redacted casually. Public examples should be recreated from scratch with fictional data.
