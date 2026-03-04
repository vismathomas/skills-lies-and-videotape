---
title: GitHub PR Actionable Comments
description: "Analyze PR review comments using gh CLI to identify actionable items from reviewer feedback and author replies."
---

# GitHub PR Actionable Comments

> Analyze PR review comments using gh CLI to identify actionable items from reviewer feedback and author replies.

:material-tag: `git`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/gh-actionable-comments/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/gh-actionable-comments/SKILL.md){ .md-button .md-button--primary }

---

Analyzes pull request review comments using the gh CLI to identify actionable items from reviewer feedback and author replies. Tracks which comments have been acknowledged and still need to be addressed.

## Usage Examples

### Analyze current PR comments

```
Analyze the review comments on the current PR and list what needs to be fixed.
```

### Check a specific PR

```
Analyze actionable comments on PR #106.
```

### Find unresolved feedback

```
Which review comments on this PR still need a response from the author?
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # PR Actionable Comments Analyzer
    
    > **Why `gh` CLI?** The VS Code GitHub Pull Requests extension's `activePullRequest` tool flattens review threads and omits nested replies. The `gh` CLI returns all comments including threaded replies, giving us the complete picture.
    
    ## Purpose
    
    Analyze pull request review comments using the `gh` CLI to identify actionable items — especially replies from the PR author that indicate work to be done. This helps teams track which comments have been acknowledged by the author and still need to be addressed.
    
    ## Prerequisites
    
    - `gh` CLI installed and authenticated (`gh auth status`)
    - Current directory is inside a git repository
    - An active pull request exists (or PR number provided)
    
    ## Procedure
    
    ### Step 1: Determine PR details
    
    If no PR number is provided, detect it from the current branch:
    
    ```bash
    gh pr view --json number,title,author,url,headRefName --jq '{number: .number, title: .title, author: .author.login, url: .url, branch: .headRefName}'
    ```
    
    Store the PR number, title, author login, URL, and branch name.
    
    ### Step 2: Fetch ALL review comments (including threaded replies)
    
    ```bash
    # First get owner/repo from git remote
    REMOTE_URL=$(git config --get remote.origin.url)
    REPO_SLUG=$(echo $REMOTE_URL | sed -E 's|.*[:/]([^/]+/[^/]+)\.git$|\1|')
    
    # Fetch review comments with threading info
    gh api "repos/${REPO_SLUG}/pulls/${PR_NUMBER}/comments" --paginate --jq '.[] | {id: .id, body: .body, path: .path, user: .user.login, created_at: .created_at, in_reply_to_id: .in_reply_to_id, commit_id: .commit_id, line: .original_line}'
    ```
    
    This returns every review comment, including nested replies (identified by `in_reply_to_id`).
    
    ### Step 3: Build threaded conversations
    
    Group comments into threads:
    
    - **Root comments** have no `in_reply_to_id` — these are the original reviewer comments.
    - **Replies** have `in_reply_to_id` pointing to a root comment or another reply.
    
    For each thread, build a conversation chain: root comment → replies in chronological order.
    
    ### Step 4: Classify each thread
    
    For each thread, determine:
    
    1. **Author involvement**: Did the PR author reply in this thread?
    
    2. **Resolution signal**: Look for signals in the PR author's replies that indicate intent:
    
       **Will fix signals:**
       - "Fixed", "Will do", "Will fix", "Done", "Fixed it"
       - Norwegian: "Fikser", "Flyttes", "Fjernes", "De fjernes", "Det skal jeg fikse", "Ordner dette", "Enig"
       - Acknowledgments: "Sounds good", "Agreed", "Good catch", "Thanks", "Makes sense"
    
       **Question signals:**
       - Replies ending with `?`
       - "Hvordan", "Hva", "Skal det", "Skjønner ikke" (Norwegian)
       - "How", "What", "Should", "Don't understand"
    
       **No reply**: PR author hasn't responded yet
    
    3. **Confidence level** for automated fix:
    
       - **🟢 HIGH** — Clear action: remove code, rename field, move file/code, add attribute. The reviewer's comment describes a specific, mechanical change.
    
       - **🟡 MEDIUM** — Action is understandable but requires some design decisions or broader context.
    
       - **🔴 LOW** — Ambiguous, needs discussion, or involves architectural decisions.
    
    ### Step 5: Also fetch issue/PR-level comments
    
    ```bash
    gh api "repos/${REPO_SLUG}/issues/${PR_NUMBER}/comments" --jq '.[] | {id: .id, body: .body, user: .user.login, created_at: .created_at}'
    ```
    
    These are conversation-level comments (not tied to specific files/lines).
    
    ### Step 6: Generate formatted output
    
    ## Output Format
    
    ### Header
    
    ```markdown
    # PR #{number}: {title}
    
    **Author:** {author} | **URL:** {url} | **Branch:** {branch}
    
    **Analysis:** {total_count} review comments across {thread_count} threads
    ```
    
    ### Summary Table
    
    A table of ALL comment threads, sorted by actionability:
    
    ```markdown
    ## Summary
    
    | # | File | Reviewer | Comment (truncated) | Author Reply | Actionable | Confidence |
    |---|------|----------|-------------------|-------------|------------|------------|
    | 1 | path/to/File.cs | reviewer | "Remove this field..." | "Will do" | ✅ Yes | 🟢 HIGH |
    | 2 | path/to/Other.cs | reviewer | "Add SoftDelete..." | "Will do" | ✅ Yes | 🟢 HIGH |
    | 3 | path/to/File.cs | reviewer | "This should be..." | "Hvordan...?" | ❓ Question | 🔴 LOW |
    | 4 | path/to/New.cs | reviewer | "Consider using..." | — | ⏳ No reply | 🟡 MEDIUM |
    ```
    
    ### Actionable Items Detail
    
    For each thread where the PR author signaled intent to fix (🟢 HIGH or 🟡 MEDIUM confidence), provide:
    
    ```markdown
    ## Actionable Items
    
    ### 1. 🟢 [File.cs] — Remove LinkedModules from entity
    
    **Reviewer** (@username): "Full reviewer comment text"
    
    **Author reply**: "Will do"
    
    **Suggested change**: Remove the `LinkedModules` and `LinkedModuleIds` properties and their associated `Apply()` methods from the entity class.
    ```
    
    ### Questions / Needs Clarification
    
    List threads where the author asked a follow-up question — these need reviewer response before action.
    
    ### No Reply Yet
    
    List threads where the author hasn't responded — these may need attention.
    
    ## Usage Examples
    
    **Analyze current branch's PR:**
    ```
    /gh-actionable-comments
    ```
    
    **Analyze specific PR:**
    ```
    /gh-actionable-comments #106
    ```
    
    **Analyze PR in specific repository:**
    ```
    /gh-actionable-comments Owner/Repo#106
    ```
    
    ## Action Item Signals
    
    ### Will Fix (🟢 HIGH / 🟡 MEDIUM)
    | Pattern | Examples |
    |---------|----------|
    | Explicit agreement | "Will do", "Will fix", "Fixed", "Done", "On it" |
    | Norwegian acknowledgments | "Fikser", "Flyttes", "Fjernes", "Ordner dette", "Enig" |
    | Acknowledgment + thanks | "Good catch", "Thanks for pointing this out" |
    
    ### Questions (🔴 LOW)
    | Pattern | Examples |
    |---------|----------|
    | Question mark | Any reply ending with `?` |
    | Norwegian questions | "Hvordan", "Hva", "Skal det", "Skjønner ikke" |
    | English questions | "How should I", "What do you mean", "Should I" |
    
    ### No Reply (⏳)
    - PR author has not responded to the review comment
    - May need follow-up or discussion
    
    ## Confidence Levels
    
    | Level | Description | Example |
    |-------|-------------|---------|
    | **🟢 HIGH** | Specific, mechanical change | "Remove unused field X" |
    | **🟡 MEDIUM** | Requires some decisions | "Refactor this for clarity" |
    | **🔴 LOW** | Ambiguous or architectural | "Consider redesigning this" |
    
    ## Anti-patterns (avoid)
    
    - ❌ Don't guess the PR number — always detect via `gh pr view` or require explicit argument
    - ❌ Don't skip threaded replies — `in_reply_to_id` is critical for understanding conversation flow
    - ❌ Don't ignore PR-level comments — they may contain important context
    - ❌ Don't assume language — check for both English and Norwegian acknowledgment phrases
