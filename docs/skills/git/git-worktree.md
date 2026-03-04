---
title: Git Worktree Management
description: "Manage git worktrees for isolated development. Create, list, remove, and work in worktrees."
---

# Git Worktree Management

> Manage git worktrees for isolated development. Create, list, remove, and work in worktrees.

:material-tag: `git`

---

Manages git worktrees for isolated development. Create, list, remove, and work in worktrees to develop multiple features simultaneously without switching branches.

## Usage Examples

### Create a worktree for a feature

```
Create a worktree for the feat/new-api branch so I can work on it without disrupting my current work.
```

### List active worktrees

```
Show me all active worktrees and their branches.
```

### Clean up a completed worktree

```
Remove the worktree for feat/auth-refactor — it's been merged.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Git Worktree Workflow
    
    ## When to Use
    
    Use git worktrees when you need to:
    - Work on multiple branches simultaneously without stashing
    - Isolate experimental work from main repository
    - Safely test changes without affecting main working tree
    - Create temporary development contexts
    
    ## Preconditions
    
    - `project docs` exists
    - Git repository initialized
    - Worktrees directory exists: `C:\dev\temp\worktrees` (or configured in constitution)
    
    ## Procedure
    
    > **Credit**: Safety verification concepts adapted from obra/superpowers by Jesse Vincent (MIT License). See `skills/using-git-worktrees/SKILL.md`.
    
    ### Create Worktree
    
    1. **Safety Check — .gitignore Verification** (MANDATORY):
       ```bash
       # Before creating any worktree, verify the worktrees directory is gitignored
       grep -q "worktrees" .gitignore 2>/dev/null || echo "⚠️ WARNING: worktrees dir not in .gitignore"
       
       # If not gitignored, add it:
       echo ".worktrees/" >> .gitignore
       git add .gitignore
       git commit -m "chore: add worktrees directory to .gitignore"
       ```
    
    2. **Directory Selection**:
       ```bash
       # Preferred: project-local .worktrees/ directory
       git worktree add .worktrees/<branch-name> -b <branch-name>
       
       # Alternative: external directory (from constitution)
       git worktree add <external-path> -b <branch-name>
       
       # Example:
       git worktree add .worktrees/feat-123 -b feat/feature-123
       ```
    
    3. **Verify worktree**:
       ```bash
       git worktree list
       
       # Verify directory structure
       ls -la <worktree-path>/.git
       # Should be a file (pointer to main repo .git)
       ```
    
    4. **Auto-Setup** (MANDATORY for projects with dependencies):
       ```bash
       cd <worktree-path>
       
       # Detect and install dependencies
       # Node.js
       [ -f package.json ] && npm install
       
       # Python
       [ -f requirements.txt ] && pip install -r requirements.txt
       [ -f pyproject.toml ] && pip install -e .
       
       # Run build to verify clean state
       # (use commands from )
       ```
    
    5. **Clean Baseline Verification** (MANDATORY):
       ```bash
       cd <worktree-path>
       
       # Verify correct branch
       git branch --show-current
       
       # Verify tests pass in clean worktree BEFORE making changes
       # This catches pre-existing failures vs. your changes
       <run test command from constitution>
       
       # If tests fail here, the baseline is broken — report before proceeding
       ```
    
    ### List Worktrees
    
    ```bash
    # List all worktrees
    git worktree list
    
    # Detailed list with branches
    git worktree list --porcelain
    ```
    
    ### Remove Worktree
    
    **After work is complete and merged**:
    ```bash
    # Navigate out of worktree
    cd <main-repo>
    
    # Remove worktree
    git worktree remove <worktree-path>
    
    # Delete feature branch (if merged)
    git branch -d <feature-branch>
    ```
    
    ### Worktree Cleanup
    
    **Remove stale worktrees**:
    ```bash
    # List all worktrees
    git worktree list
    
    # Remove worktrees for deleted branches
    git worktree remove <worktree-path>
    ```
    
    ## Integration with Issue Tracking
    
    When working in a worktree:
    1. Update `project docs` to reflect worktree location
    2. Track issue progress normally (updates worktree's git state)
    3. When committing, reference issue ID in commit message
    
    ## Example Workflow
    
    ```bash
    # In main repo (C:\dev\myproject)
    git worktree add C:/dev/worktrees/myproject-feature feat/opencode-bundle
    
    # In worktree
    cd C:/dev/worktrees/myproject-feature
    # ... implement changes ...
    git add .
    git commit -m "feat: implement OpenCodeGenerator enhancements"
    
    # Merge back to main
    cd C:/dev/myproject
    git merge feat/opencode-bundle
    git worktree remove C:/dev/worktrees/myproject-feature
    ```
    
    ## Scope
    
    - ✅ Create worktrees
    - ✅ List worktrees
    - ✅ Remove worktrees
    - ✅ Work in worktrees (normal git operations)
    - ❌ Prune worktrees (use git worktree prune, which is built-in)
    
    ## Notes
    
    - Worktrees are lightweight (share same .git directory)
    - Safe to delete worktree directory after removal
    - No risk to main repository when working in worktree
    - Perfect for feature development, bug fixes, testing
    
    ## Important Rules
    
    **Never push without explicit user permission:**
    - Git push requires explicit user request before execution
    - This is enforced by `git` skill and applies to all workflows
    - Auto-push is NEVER permitted, even for successful merges
    - Always ask for confirmation before: `git push`
