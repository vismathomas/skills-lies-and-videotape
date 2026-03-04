---
title: Context Map Generator
description: "Analyze the codebase to create a concise, LLM-optimized structured overview."
---

# Context Map Generator

> Analyze the codebase to create a concise, LLM-optimized structured overview.

:material-tag: `analysis`

---

Analyzes a codebase to create a concise, LLM-optimized structured overview. The resulting context map enables reasoning about the whole project without reading every file.

## Usage Examples

### Generate a project overview

```
Create a context map of this project.
```

### Partial refresh after changes

```
Refresh the context map for the src/api/ area — I just made significant changes there.
```

### Onboarding overview

```
Generate a context map so I can understand this unfamiliar codebase.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Context Map Generation
    
    ## Purpose
    Create a high-level, token-efficient overview of the system (`project docs`) to allow reasoning about the whole project without reading every file.
    
    ## Staleness Thresholds
    
    **Map freshness requirements:**
    
    | Age | Refresh Requirement |
    |-----|---------------------|
    | < 24 hours | Current — no refresh needed |
    | 1-7 days | RECOMMENDED if significant changes |
    | > 7 days | MANDATORY before major work |
    
    ### Staleness Check
    
    When invoked:
    
    ```
    📍 CONTEXT MAP STALENESS CHECK
    
    Map file: map.md
    Last updated: {date} ({N} days ago)
    
    {If stale:}
    ⚠️ Context map is STALE.
    Refreshing map before proceeding...
    
    {If fresh:}
    ✅ Context map is current ({N} days old)
    ```
    
    ### Refresh Options
    
    When a refresh is needed:
    1. **Check map age** — if > 24 hours, refresh is recommended
    2. **Check for recent changes** — git diff since last map update
    3. **Partial refresh option** — focus on affected areas if full refresh is expensive
    
    ```
    🔄 CONTEXT MAP REFRESH
    
    Affected areas:
    - src/services/ (target of changes)
    - src/models/ (dependencies)
    - tests/services/ (test coverage)
    
    Refresh options:
    1. Full refresh (entire codebase)
    2. Partial refresh (affected areas only)
    3. Skip (not recommended for unfamiliar codebases)
    
    Proceeding with partial refresh...
    ```
    
    ## Procedure
    1. **Scan** the file structure (limit to 2-3 levels of depth).
    2. **Identify** key architectural elements:
       - Critical configuration files (package.json, pyproject.toml, docker-compose, etc.)
       - Entry points (main.py, index.js, App.tsx)
       - Core modules and their responsibilities.
    3. **Summarize** architecture patterns and data flow.
    4. **Write/Update** `project docs` with the following structure:
       - **System Overview**: One paragraph summary of purpose and stack.
       - **Key Components**: List of major modules/folders and what they do.
       - **Patterns**: Architectural decisions (e.g., MVC, Repository pattern, Event-driven).
       - **Key Files**: Table of critical files and their specific role.
       - **Last Updated**: Timestamp for staleness tracking.
    5. **Constraint**: Keep the file concise (target < 150 lines). It is a map, not a territory.
    
    ## Map Header Template
    
    Include this header in map.md for staleness tracking:
    
    ```markdown
    # Context Map
    
    **Generated**: {YYYY-MM-DD HH:MM}
    **Scope**: {full | partial: areas}
    
    ---
    ```
