---
title: Safe Git Operations
description: "Manage git operations safely. Includes stale state detection, branch/commit management. Never pushes without explicit user confirmation."
---

# Safe Git Operations

> Manage git operations safely. Includes stale state detection, branch/commit management. Never pushes without explicit user confirmation.

:material-tag: `git`

---

Manages git operations safely with built-in protections. Includes stale state detection, branch/commit management, and protected branch enforcement. Never pushes without explicit user confirmation.

## Usage Examples

### Create a feature branch

```
Create a feature branch for issue BUG-123 and commit the current changes.
```

### Check for stale state

```
Check if my local repo state is stale — did someone else push changes?
```

### Safe commit workflow

```
Stage and commit all changes in src/ with a conventional commit message.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Git Workflow (active-safe)
    
    Issue tracking can be done via direct file editing or the `gh` CLI.
    
    ## Git Commands
    
    | Operation | Command | Notes |
    |-----------|---------|-------|
    | Check current branch | `git branch --show-current` | |
    | Check current commit | `git rev-parse --short HEAD` | |
    | Check uncommitted changes | `git status --porcelain` | |
    | Create branch | `git checkout -b <branch>` | From constitution branch policy |
    | Stage changes | `git add <files>` | |
    | Commit | `git commit -m "..."` | Use structured message format |
    | Stash work | `git stash push -m "..."` | |
    | Unstash work | `git stash pop` | |
    | View stash | `git stash list` | |
    | Revert commit | `git revert <commit>` | Requires confirmation |
    
    ## Issue Integration (File-Based)
    
    | Operation | How to Do It |
    |-----------|--------------|
    | Start work | Edit issue file: set `status: in_progress` |
    | Close issue | Set `status: done`, add log entry with commit hash |
    
    ## Never Auto-Execute
    
    ```bash
    # These require explicit user confirmation:
    git push           # Never auto-push
    git push --force   # Never force push
    git branch -D      # Never delete branches
    ```
    
    ## Protected Branches (HARD BLOCK)
    
    **Agents can NEVER push to protected branches, regardless of user request.**
    
    ### Default Protected Patterns
    
    ```
    main, master, develop, next, release/*
    ```
    
    ### Pre-Push Validation (MANDATORY)
    
    Before ANY push operation:
    
    1. Get target branch: `git rev-parse --abbrev-ref HEAD` or explicit target
    2. Load protected patterns from `project docs`
    3. Check if target matches any protected pattern:
    
    ```python
    def is_protected(branch: str, patterns: list[str]) -> bool:
        for pattern in patterns:
            if pattern.endswith("/*"):
                if branch.startswith(pattern[:-1]):
                    return True
            elif branch == pattern:
                return True
        return False
    ```
    
    4. If protected:
       ```
       ⛔ REFUSED: Cannot push to protected branch '{branch}'
       
       Protected branches: main, master, develop, next, release/*
       
       This protection cannot be overridden.
       Create a feature branch instead: git checkout -b feat/<issue-id>
       ```
    
    5. If NOT protected and user has explicitly requested push:
       - Proceed with push
       - Log the push
    
    ### Feature Branch Naming
    
    Agents should push only to branches following these patterns:
    - `feat/<issue-id>` or `feature/<issue-id>`
    - `bug/<issue-id>` or `fix/<issue-id>`
    - `chore/<issue-id>`
    - `refac/<issue-id>` or `refactor/<issue-id>`
    - `docs/<issue-id>`
    - `test/<issue-id>`
    
    ## Scope
    
    - ✅ Detect stale state (authoritative source)
    - ✅ Create feature branches
    - ✅ Commit checkpoints with structured messages
    - ✅ Detect uncommitted changes
    - ✅ Stash/unstash work in progress
    - ✅ Revert agent's own commits (with confirmation)
    - ❌ Never push without explicit user request
    - ❌ Never force push
    - ❌ Never delete remote branches
    
    ## Stale State Detection (authoritative)
    
    Called by  at session start. This is the single source of truth for staleness.
    
    ### Procedure
    
    1. Read `project docs` session info:
       - `branch`: expected branch name
       - `last_commit`: expected HEAD commit (short hash)
       - `last_updated`: timestamp
    
    2. Get current git state:
       ```bash
       git branch --show-current    # current branch
       git rev-parse --short HEAD   # current commit
       git status --porcelain       # uncommitted changes
       ```
    
    3. Compare and categorize:
    
       | Check | Mismatch | Severity | Action |
       |-------|----------|----------|--------|
       | Branch changed | Expected `main`, now on `feature-x` | ⚠️ WARN | Ask user |
       | Commit changed | Expected `abc123`, HEAD is `def456` | ⚠️ WARN | Ask user |
       | Uncommitted changes | `git status` shows changes | ℹ️ INFO | Note, may continue |
       | All match | — | ✅ OK | Continue |
    
    4. If any WARN:
       ```
       ⚠️ State may be stale.
       - Expected branch: X, actual: Y
       - Expected commit: A, actual: B
       
       Options:
       A) Continue anyway (I made these changes)
       B) Update session state to current
       C) Stop and investigate
       ```
    
    ## Branch Strategy
    
    Read `project docs` for project-specific rules:
    - Branch naming pattern
    - When to create branches
    - Whether to work on main directly
    
    ## Commit Message Format
    
    Default format:
    ```
    <type>: <short summary>
    
    <body - what and why>
    
    Task: T-XXXX
    ```
    
    Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
    
    ## Issue Reference in Commits
    
    **Every commit should reference an issue ID:**
    
    ```
    fix: Resolve login timeout
    
    Fixed the session expiry logic that was causing premature logouts.
    
    Issue: BUG-0023@efa54f
    ```
    
    If no issue exists for the work being committed:
    ```
    ⚠️ No issue found for this commit.
    
    Create an issue first? [Y]es / [N]o, commit without issue
    
    Note: All work should be tracked for auditability.
    ```
    
    ## Checkpoint Commits
    
    Create commits at these moments:
    - Before risky changes (labeled `[checkpoint]`)
    - After each implementation step completes successfully
    - Before switching tasks
    
    ## Branch Finishing Workflow
    
    > **Credit**: Branch finishing concept adapted from obra/superpowers by Jesse Vincent (MIT License). See `skills/finishing-a-development-branch/SKILL.md`.
    
    When work on a feature branch is complete, present the user with structured options rather than auto-merging.
    
    ### Pre-Finish Verification (MANDATORY)
    
    Before presenting options, verify:
    ```bash
    # 1. All tests pass on the feature branch
    <run test command from constitution>
    
    # 2. No uncommitted changes
    git status --porcelain
    
    # 3. Branch is up-to-date with target
    git fetch origin
    git log HEAD..origin/main --oneline  # check for upstream changes
    ```
    
    If tests fail or uncommitted changes exist → STOP and resolve first.
    
    ### Present Finish Options
    
    After verification passes, present exactly 4 options:
    
    ```
    Branch work complete. All tests pass. Choose how to finish:
    
    1. **Merge locally** — Merge into target branch (e.g., main)
       - git checkout main && git merge feat/<id> && git branch -d feat/<id>
       
    2. **Push and create PR** — Push branch and create a pull request
       - git push origin feat/<id>
       - Create PR via gh CLI or provide URL
       
    3. **Keep as-is** — Leave branch for later
       - Branch stays, no merge, can resume later
       
    4. **Discard** — Delete the branch and all its changes
       - git checkout main && git branch -D feat/<id>
       - ⚠️ This is destructive — requires explicit confirmation
    ```
    
    ### Post-Finish Cleanup
    
    After option 1 or 2:
    - If worktree was used: `git worktree remove <path>`
    - Update `project docs` with new branch state
    - Update issue status to `done` (option 1) or `review` (option 2)
    
    After option 4:
    - Confirm with user before deletion
    - Update issue status to `cancelled` or `dropped`
    
    ## Rollback Procedure
    
    When rolling back:
    1. List commits made by agent (search for `` prefix)
    2. Show user what will be reverted
    3. Ask for confirmation
    4. Use `git revert` (not reset) to preserve history
