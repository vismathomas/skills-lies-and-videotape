---
title: Narrative Coherence Audit
description: "Audit the project's story for coherence. Ensure issues, commits, plans, docs, and changelog tell a consistent narrative."
---

# Narrative Coherence Audit

> Audit the project's story for coherence. Ensure issues, commits, plans, docs, and changelog tell a consistent narrative.

:material-tag: `review`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/narrative-audit/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/narrative-audit/SKILL.md){ .md-button .md-button--primary }

---

Audits a project's story for coherence. Ensures that issues, commits, plans, documentation, and changelog all tell a consistent narrative without contradictions or gaps.

## Usage Examples

### Full narrative audit

```
Audit the project narrative — do our issues, commits, and docs tell a coherent story?
```

### Check docs/code alignment

```
Verify that the README and docs accurately describe what the code actually does.
```

### Changelog consistency

```
Check if the changelog entries match the actual commits and closed issues.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

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
