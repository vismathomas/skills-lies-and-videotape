---
name: narrative-audit
title: Narrative Coherence Audit
description: "Audit the project's story for coherence. Ensure issues, commits, plans, docs, and changelog tell a consistent narrative."
category: review
---
# narrative-audit

Audit the project's story for coherence. Ensure issues, commits, plans, docs, and changelog tell a consistent narrative.

## Purpose

Great projects tell a consistent story. Broken projects have unexplained decisions, orphaned features, contradictory docs, and missing chapters. This skill identifies narrative gaps.

## Trigger

- Before major releases
- During documentation updates
- After significant refactoring
- On demand for project health check

## Narrative Sources

| Source | Story Contribution | Location |
|--------|-------------------|----------|
| **Issues** | What we intended to do | `project docs` |
| **Commits** | What we actually did | Git log |
| **Plans** | How we thought to do it | `project docs` |
| **Docs** | What we say we did | `.github/docs/`, README |
| **Changelog** | What we tell users | CHANGELOG |

## Narrative Gaps

| Gap Type | Example | Detection |
|----------|---------|-----------|
| **Orphaned feature** | Code exists, no issue | Commits without issue ref |
| **Zombie issue** | Issue closed, no code | Done but no implementation |
| **Contradiction** | Docs say X, code does Y | Doc vs code mismatch |
| **Silent change** | Code changed, no docs | Missing changelog entry |

## Related Skills

- `git` — commit history analysis
-  — documentation consistency
-  — includes narrative checks
