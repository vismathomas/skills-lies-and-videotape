---
title: Git Story Generator
description: "Generate narrative summaries from git history for onboarding, retrospectives, changelogs, and exploration. LLM-enhanced when available, works without LLM too."
---

# Git Story Generator

> Generate narrative summaries from git history for onboarding, retrospectives, changelogs, and exploration. LLM-enhanced when available, works without LLM too.

:material-tag: `git`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/git-story/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/git-story/SKILL.md){ .md-button .md-button--primary }

---

Generates human-readable narratives from git commit history. Useful for onboarding new team members, creating retrospective summaries, building changelogs, and exploring project evolution.

## Usage Examples

### Onboarding summary

```
Generate a story of how this project evolved over the last 6 months for a new team member.
```

### Sprint retrospective

```
Create a narrative summary of what was accomplished in the last sprint from git history.
```

### Feature evolution

```
Tell the story of how the authentication module was built, from the first commit.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Git Story Skill
    
    Generate human-readable narratives from git commit history. Useful for:
    - **Onboarding** — Help new team members understand project evolution
    - **Retrospectives** — Create sprint/milestone summaries
    - **Changelogs** — Generate release notes from commits
    - **Exploration** — Understand "what happened here?" for any period
    
    ## Requirements
    
    - **Git**: Must be installed locally and available on PATH
    - **LLM**: Optional — enhanced narratives when available, templated output without
    
    ## Data Extraction
    
    Story generation uses raw `git log` commands.
    
    ### Git Commands
    
    | Operation | Command |
    |---------|---------|
    | Recent commits | `git log --oneline -N` |
    | Date range | `git log --since="YYYY-MM-DD" --until="YYYY-MM-DD"` |
    | By author | `git log --author="name"` |
    | Detailed | `git log --stat --since="YYYY-MM-DD"` |
    | JSON-like | `git log --format="%H|%an|%ad|%s" --date=short` |
    
    ### Examples
    
    ```bash
    # Last 30 days of activity
    git log --oneline --since=2026-01-01
    
    # Generate detailed log for changelog
    git log --stat --since=2026-01-01
    
    # Filter by author
    git log --author="John Doe" --oneline
    
    # Export to file
    git log --oneline -100 > story.md
    ```
    
    ## Agent Workflow
    
    When user requests a git story or narrative:
    
    ### 1. Gather Requirements
    
    ```
    What kind of git story do you need?
    
    A) **Recent activity** — Last N days or commits
    B) **Release notes** — Changelog format for a version
    C) **Sprint retrospective** — Specific date range
    D) **Author focus** — Contributions by a specific person
    E) **Full history** — Complete project evolution
    ```
    
    ### 2. Extract Data
    
    Run appropriate `git log` command based on requirements:
    
    ```bash
    # For recent activity
    git log --oneline -30
    
    # For date range (sprint)
    git log --since=2026-01-01 --until=2026-01-15 --stat
    
    # For changelog (since last tag)
    git log $(git describe --tags --abbrev=0)..HEAD --oneline
    ```
    
    ### 3. Enhance with LLM (Optional)
    
    When LLM is available, transform raw data into rich narrative:
    
    **Input (from CLI JSON output):**
    ```json
    {
      "title": "Git Story",
      "period": "January 1-15, 2026",
      "total_commits": 45,
      "groups": [...]
    }
    ```
    
    **LLM Prompt:**
    ```
    Transform this git commit data into a human-readable narrative.
    
    Context: {purpose - onboarding/retrospective/changelog}
    Audience: {who will read this}
    Tone: {technical/casual/formal}
    
    Data:
    {json_output}
    
    Create a narrative that:
    1. Opens with an overview of the period
    2. Highlights major themes/features
    3. Groups related changes logically
    4. Notes significant contributors
    5. Ends with a summary
    
    Format: Markdown with headers, bullets, and emphasis.
    ```
    
    **Output (LLM-enhanced):**
    ```markdown
    # Development Update: January 1-15, 2026
    
    ## Overview
    The first two weeks of January saw intense development activity with 45 commits 
    from 5 contributors. The focus was on authentication improvements and API stability.
    
    ## Major Themes
    
    ### 🔐 Authentication Overhaul
    John and Sarah led a comprehensive rework of the auth system:
    - Implemented OAuth2 with Google and GitHub providers
    - Added session management with automatic refresh
    - Fixed critical security vulnerability in token validation
    
    ### 🚀 API Performance
    The API team delivered significant improvements:
    - Reduced average response time by 40%
    - Added pagination to all list endpoints
    - Implemented request rate limiting
    
    ## Contributors
    - **John Doe** (18 commits) — Auth system, security fixes
    - **Sarah Smith** (12 commits) — OAuth integration, tests
    - **Mike Chen** (10 commits) — API optimization
    - 2 others with 5 commits total
    
    ## What's Next
    The groundwork for v2.0 is complete. Next sprint focuses on the dashboard UI.
    ```
    
    ### 4. Without LLM
    
    When LLM is not available, use templated output from git:
    
    ```bash
    # Detailed log (human-readable)
    git log --stat --since=2026-01-01
    
    # One-line format (simple list)
    git log --oneline -50
    
    # Grouped by author
    git shortlog --since=2026-01-01
    ```
    
    ## Output Formats
    
    ### Narrative (default)
    Rich markdown with sections for contributors, grouped commits, and context.
    Best for: Onboarding docs, retrospectives
    
    ### Changelog
    Conventional changelog format grouped by commit type (feat, fix, etc.).
    Best for: Release notes, CHANGELOG.md updates
    
    ### Bullets
    Simple bullet list of commits.
    Best for: Quick summaries, PR descriptions
    
    ### JSON
    Structured data for further processing.
    Best for: Feeding to LLM, programmatic use
    
    ## Integration Points
    
    ### With versioning
    ```
    When generating release notes:
    1. Determine version range (last tag to HEAD)
    2. Run: git log $(git describe --tags --abbrev=0)..HEAD --oneline
    3. Insert into CHANGELOG.md
    ```
    
    ### With documentation
    ```
    When updating project documentation:
    1. Generate story for significant period
    2. Add to docs/history/ or similar
    3. Link from main README if appropriate
    ```
    
    ## Best Practices
    
    1. **Be specific about time range** — "Last 30 days" is better than "recent"
    2. **Exclude merge commits** — Default behavior, cleaner output
    3. **Use appropriate format** — Changelog for releases, narrative for humans
    4. **Filter by author** when highlighting individual contributions
    5. **Group by type** for release notes, by date for retrospectives
    
    ## Example Session
    
    **User:** Generate a summary of what happened in the codebase this month.
    
    **Agent:**
    ```
    I'll generate a git story for January 2026.
    
    Running: git log --since=2026-01-01 --stat
    
    [Output displayed]
    
    Key highlights:
    - 127 commits from 8 contributors
    - Major features: OAuth integration, API pagination, Dashboard redesign
    - Notable fixes: Security vulnerability patched, performance improvements
    
    Would you like me to:
    1. Generate a more detailed breakdown by feature?
    2. Create a changelog format for release notes?
    3. Focus on a specific contributor's work?
    ```
    
    ## Troubleshooting
    
    | Issue | Solution |
    |-------|----------|
    | "git is not available" | Install git and ensure it's on PATH |
    | No commits found | Check date range, verify you're in a git repo |
    | Merge commits cluttering output | Default excludes merges; add `--merges` if needed |
    | Large output | Use `--last N` to limit, or filter by date |
