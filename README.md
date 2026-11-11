# Cybersecurity Engineering Portfolio

A developing portfolio of security engineering methods, source-code review practices, vulnerability remediation documentation, and SOC investigation writing.

This repository contains reusable templates and synthetic demonstrations. It does not claim completed client engagements, certifications, or production incident experience. No confidential company material is included.

## Explore

- [Portfolio projects](projects/README.md)
- [Source review methodology](docs/audit-methodology.md)
- [Evidence and publication rules](docs/publication-policy.md)
- [Audit templates](templates/README.md)
- [Skills matrix](trackers/skills-matrix.md)
- [Project progress](trackers/projects.md)
- [Learning and change log](trackers/activity.md)

## Workflow

Scope → review source → record evidence → assess risk → propose remediation → independently retest → write a cleared summary. Real reviews stay in the data owner's approved workspace. Only recreated synthetic examples belong here.

Documentation requires Git, Python 3 and a text editor. No application server, cloud account, production credentials, or external scanning is required. Run `python3 scripts/check_docs.py` and `git diff --check` locally.

Read [agent instructions](AGENTS.md), [contribution guidance](CONTRIBUTING.md), and [security guidance](SECURITY.md) before contributing.

See the [minimal environment workflow](docs/environment-workflow.md) for portable setup.
