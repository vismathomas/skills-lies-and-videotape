---
title: GitHub Pull-Request Info
description: "Extract comprehensive information from a GitHub pull request using gh CLI including metadata, reviews, and inline comments"
---

# GitHub Pull-Request Info

> Extract comprehensive information from a GitHub pull request using gh CLI including metadata, reviews, and inline comments

:material-tag: `git`

---

Extracts comprehensive information from a GitHub pull request using the gh CLI and GitHub REST API. Fetches metadata, reviews, inline comments, status checks, and file changes.

## Usage Examples

### Get PR overview

```
Get all information about the current PR — reviews, comments, status checks.
```

### Extract PR review details

```
Show me all review comments and their resolution status for PR #42.
```

### PR metadata for documentation

```
Extract the PR description, linked issues, and reviewer list for PR #15.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # GitHub PR Info Extraction — Complete Reference
    
    ## Purpose
    
    Extract **ALL** available information from a GitHub pull request for analysis, documentation, or workflow integration. Uses the GitHub CLI (`gh`) and GitHub REST API to fetch every piece of data associated with a PR.
    
    ## Prerequisites
    
    - GitHub CLI (`gh`) installed and authenticated
    - Current directory is within a git repository connected to GitHub
    - PR number or branch name known
    - Repository owner and name (for API calls)
    
    ---
    
    ## Complete Data Extraction Procedure
    
    ### Step 1: Set Variables
    
    ```powershell
    $owner = "OWNER"    # e.g., "Visma-WFM-Gat"
    $repo = "REPO"      # e.g., "GatPlus"
    $pr = 124           # PR number (or use: gh pr view --json number -q .number)
    ```
    
    ### Step 2: Main PR Metadata (gh pr view)
    
    ```powershell
    gh pr view $pr --json number,title,body,state,author,assignees,labels,milestone,reviewRequests,reviewDecision,additions,deletions,changedFiles,commits,comments,reviews,latestReviews,files,headRefName,baseRefName,headRefOid,baseRefOid,url,createdAt,updatedAt,closedAt,mergedAt,mergeable,mergeStateStatus,isDraft,statusCheckRollup,closingIssuesReferences,reactionGroups,projectItems
    ```
    
    **All available `gh pr view --json` fields:**
    
    | Field | Description |
    |-------|-------------|
    | `additions` | Lines added |
    | `assignees` | Assigned users |
    | `author` | PR author |
    | `autoMergeRequest` | Auto-merge configuration |
    | `baseRefName` | Target branch name |
    | `baseRefOid` | Target branch SHA |
    | `body` | PR description (markdown) |
    | `changedFiles` | Number of files changed |
    | `closed` | Is closed (boolean) |
    | `closedAt` | Close timestamp |
    | `closingIssuesReferences` | Linked issues to close |
    | `comments` | Conversation comments |
    | `commits` | Commit list |
    | `createdAt` | Creation timestamp |
    | `deletions` | Lines deleted |
    | `files` | Changed files with stats |
    | `fullDatabaseId` | Internal DB ID |
    | `headRefName` | Source branch name |
    | `headRefOid` | Source branch SHA |
    | `headRepository` | Source repository |
    | `headRepositoryOwner` | Source repo owner |
    | `id` | Node ID |
    | `isCrossRepository` | Is cross-repo PR |
    | `isDraft` | Is draft PR |
    | `labels` | Applied labels |
    | `latestReviews` | Most recent review per reviewer |
    | `maintainerCanModify` | Maintainer push access |
    | `mergeCommit` | Merge commit (if merged) |
    | `mergeStateStatus` | Merge state (BLOCKED, CLEAN, etc.) |
    | `mergeable` | Can be merged |
    | `mergedAt` | Merge timestamp |
    | `mergedBy` | Who merged |
    | `milestone` | Associated milestone |
    | `number` | PR number |
    | `potentialMergeCommit` | Potential merge commit SHA |
    | `projectCards` | Project board cards |
    | `projectItems` | Project items (v2) |
    | `reactionGroups` | Reactions on PR body |
    | `reviewDecision` | Overall review status |
    | `reviewRequests` | Pending review requests |
    | `reviews` | All reviews |
    | `state` | PR state (OPEN, CLOSED, MERGED) |
    | `statusCheckRollup` | CI/CD status checks |
    | `title` | PR title |
    | `updatedAt` | Last update timestamp |
    | `url` | Web URL |
    
    ### Step 3: Detailed PR Data (REST API)
    
    The REST API provides additional fields not in `gh pr view`:
    
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr
    ```
    
    **Additional REST API fields:**
    
    | Field | Description |
    |-------|-------------|
    | `locked` | Is conversation locked |
    | `active_lock_reason` | Lock reason |
    | `merge_commit_sha` | Merge commit SHA |
    | `rebaseable` | Can be rebased |
    | `requested_reviewers` | Requested reviewer details |
    | `requested_teams` | Requested team reviews |
    | `review_comments` | Count of review comments |
    | `maintainer_can_modify` | Maintainer push access |
    | `diff_url` | URL to raw diff |
    | `patch_url` | URL to patch file |
    
    ### Step 4: Inline Code Review Comments
    
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr/comments
    ```
    
    **Fields per comment:**
    
    | Field | Description |
    |-------|-------------|
    | `id` | Comment ID |
    | `body` | Comment text |
    | `path` | File path |
    | `line` | Current line number |
    | `original_line` | Original line number |
    | `start_line` | Range start (for multi-line) |
    | `side` | LEFT or RIGHT side of diff |
    | `diff_hunk` | Code context (patch snippet) |
    | `commit_id` | Commit SHA at comment time |
    | `original_commit_id` | Original commit SHA |
    | `user` | Commenter details |
    | `created_at` | Creation timestamp |
    | `updated_at` | Edit timestamp |
    | `author_association` | MEMBER, CONTRIBUTOR, etc. |
    | `reactions` | Reaction counts |
    | `pull_request_review_id` | Parent review ID |
    | `in_reply_to_id` | Parent comment (for threads) |
    | `subject_type` | `line` or `file` |
    
    ### Step 5: PR Conversation Comments
    
    These are comments on the PR itself (not on code):
    
    ```powershell
    gh api repos/$owner/$repo/issues/$pr/comments
    ```
    
    **Fields per comment:**
    
    | Field | Description |
    |-------|-------------|
    | `id` | Comment ID |
    | `body` | Comment text (markdown) |
    | `user` | Author details |
    | `created_at` | Creation timestamp |
    | `updated_at` | Edit timestamp |
    | `author_association` | Association type |
    | `reactions` | Reaction counts |
    
    ### Step 6: Full Review Details
    
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr/reviews
    ```
    
    **Fields per review:**
    
    | Field | Description |
    |-------|-------------|
    | `id` | Review ID |
    | `user` | Reviewer details |
    | `body` | Review summary text |
    | `state` | APPROVED, CHANGES_REQUESTED, COMMENTED, DISMISSED, PENDING |
    | `commit_id` | Commit SHA reviewed |
    | `submitted_at` | Submission timestamp |
    | `author_association` | MEMBER, CONTRIBUTOR, etc. |
    | `html_url` | Web URL to review |
    
    ### Step 7: Detailed Commits
    
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr/commits
    ```
    
    **Fields per commit:**
    
    | Field | Description |
    |-------|-------------|
    | `sha` | Full commit SHA |
    | `commit.message` | Commit message (headline + body) |
    | `commit.author` | Author name, email, date |
    | `commit.committer` | Committer name, email, date |
    | `commit.verification` | Signature verification status |
    | `author` | GitHub user (if linked) |
    | `committer` | GitHub committer user |
    | `parents` | Parent commit SHAs |
    | `html_url` | Web URL to commit |
    
    ### Step 8: Files with Diff Patches
    
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr/files
    ```
    
    **Fields per file:**
    
    | Field | Description |
    |-------|-------------|
    | `sha` | Blob SHA |
    | `filename` | File path |
    | `status` | added, removed, modified, renamed, copied, changed |
    | `additions` | Lines added |
    | `deletions` | Lines deleted |
    | `changes` | Total lines changed |
    | `patch` | Unified diff patch content |
    | `blob_url` | URL to file blob |
    | `raw_url` | URL to raw file |
    | `contents_url` | API URL to contents |
    | `previous_filename` | Original name (for renames) |
    
    ### Step 9: Full Unified Diff
    
    ```powershell
    gh pr diff $pr                    # Full diff
    gh pr diff $pr --name-only        # Just file names
    ```
    
    ### Step 10: Timeline Events
    
    Complete history of all PR events:
    
    ```powershell
    gh api repos/$owner/$repo/issues/$pr/timeline
    ```
    
    **Event types returned:**
    
    | Event | Description |
    |-------|-------------|
    | `committed` | Commit added |
    | `reviewed` | Review submitted |
    | `review_requested` | Review requested |
    | `review_request_removed` | Review request removed |
    | `commented` | Comment added |
    | `labeled` | Label added |
    | `unlabeled` | Label removed |
    | `assigned` | User assigned |
    | `unassigned` | User unassigned |
    | `milestoned` | Milestone set |
    | `demilestoned` | Milestone removed |
    | `renamed` | Title changed |
    | `locked` | Conversation locked |
    | `unlocked` | Conversation unlocked |
    | `head_ref_deleted` | Source branch deleted |
    | `head_ref_restored` | Source branch restored |
    | `base_ref_changed` | Target branch changed |
    | `merged` | PR merged |
    | `closed` | PR closed |
    | `reopened` | PR reopened |
    | `convert_to_draft` | Converted to draft |
    | `ready_for_review` | Marked ready for review |
    | `cross-referenced` | Referenced from another issue/PR |
    
    ### Step 11: Check Runs (CI/CD Details)
    
    ```powershell
    # Get the head SHA first
    $headSha = gh pr view $pr --json headRefOid -q .headRefOid
    
    # Then get check runs
    gh api repos/$owner/$repo/commits/$headSha/check-runs
    ```
    
    **Fields per check run:**
    
    | Field | Description |
    |-------|-------------|
    | `id` | Check run ID |
    | `name` | Check name |
    | `status` | queued, in_progress, completed |
    | `conclusion` | success, failure, neutral, cancelled, timed_out, action_required, skipped |
    | `started_at` | Start timestamp |
    | `completed_at` | Completion timestamp |
    | `output` | Summary, title, text, annotations |
    | `html_url` | Web URL |
    | `app` | GitHub App that created it |
    
    ### Step 12: Status Checks
    
    ```powershell
    gh api repos/$owner/$repo/commits/$headSha/status
    ```
    
    **Fields:**
    
    | Field | Description |
    |-------|-------------|
    | `state` | pending, success, failure, error |
    | `statuses` | Array of individual status checks |
    | `total_count` | Number of statuses |
    
    ---
    
    ## Complete Extraction Script
    
    ```powershell
    # Configuration
    $owner = "OWNER"
    $repo = "REPO"
    $pr = 124
    $outDir = "pr-$pr-data"
    
    New-Item -ItemType Directory -Force -Path $outDir | Out-Null
    
    # 1. Main PR data (gh pr view)
    gh pr view $pr --json number,title,body,state,author,assignees,labels,milestone,reviewRequests,reviewDecision,additions,deletions,changedFiles,commits,comments,reviews,latestReviews,files,headRefName,baseRefName,headRefOid,baseRefOid,url,createdAt,updatedAt,closedAt,mergedAt,mergeable,mergeStateStatus,isDraft,statusCheckRollup,closingIssuesReferences,reactionGroups > "$outDir/01-pr-main.json"
    
    # 2. REST API PR details
    gh api repos/$owner/$repo/pulls/$pr > "$outDir/02-pr-rest.json"
    
    # 3. Inline code review comments
    gh api repos/$owner/$repo/pulls/$pr/comments > "$outDir/03-review-comments.json"
    
    # 4. PR conversation comments
    gh api repos/$owner/$repo/issues/$pr/comments > "$outDir/04-pr-comments.json"
    
    # 5. All reviews
    gh api repos/$owner/$repo/pulls/$pr/reviews > "$outDir/05-reviews.json"
    
    # 6. Commits with details
    gh api repos/$owner/$repo/pulls/$pr/commits > "$outDir/06-commits.json"
    
    # 7. Files with patches
    gh api repos/$owner/$repo/pulls/$pr/files > "$outDir/07-files.json"
    
    # 8. Full diff
    gh pr diff $pr > "$outDir/08-full-diff.patch"
    
    # 9. Timeline events
    gh api repos/$owner/$repo/issues/$pr/timeline > "$outDir/09-timeline.json"
    
    # 10. Check runs (CI/CD)
    $headSha = gh pr view $pr --json headRefOid -q .headRefOid
    gh api repos/$owner/$repo/commits/$headSha/check-runs > "$outDir/10-check-runs.json"
    gh api repos/$owner/$repo/commits/$headSha/status > "$outDir/11-status.json"
    
    Write-Host "All PR data extracted to $outDir/"
    ```
    
    ---
    
    ## Document Generation
    
    After extraction, generate a single comprehensive document (`PR-{number}-report.md`) that is:
    - **Human-readable**: Clear markdown with structured sections
    - **Machine-parseable**: YAML frontmatter + JSON code blocks for raw data
    
    ### Document Template
    
    ```markdown
    ---
    # PR Report — Machine-Readable Metadata
    pr_number: {number}
    title: "{title}"
    url: "{url}"
    state: "{state}"
    author: "{author.login}"
    created_at: "{createdAt}"
    updated_at: "{updatedAt}"
    merged_at: {mergedAt or null}
    closed_at: {closedAt or null}
    base_branch: "{baseRefName}"
    head_branch: "{headRefName}"
    head_sha: "{headRefOid}"
    base_sha: "{baseRefOid}"
    additions: {additions}
    deletions: {deletions}
    changed_files: {changedFiles}
    mergeable: "{mergeable}"
    merge_state: "{mergeStateStatus}"
    is_draft: {isDraft}
    review_decision: "{reviewDecision}"
    labels: [{labels as comma-separated strings}]
    assignees: [{assignees as comma-separated strings}]
    reviewers_approved: [{list}]
    reviewers_changes_requested: [{list}]
    reviewers_commented: [{list}]
    ---
    
    # PR #{number}: {title}
    
    > **URL**: {url}
    > **Author**: @{author.login}
    > **Branch**: `{headRefName}` → `{baseRefName}`
    > **State**: {state} | **Review**: {reviewDecision} | **Mergeable**: {mergeable}
    
    ## Summary
    
    {body - truncated if very long, with link to full}
    
    ---
    
    ## Statistics
    
    | Metric | Value |
    |--------|-------|
    | Additions | +{additions} |
    | Deletions | -{deletions} |
    | Files Changed | {changedFiles} |
    | Commits | {commits.length} |
    | Reviews | {reviews.length} |
    | Inline Comments | {review_comments.length} |
    | Conversation Comments | {pr_comments.length} |
    
    ---
    
    ## Files Changed
    
    | File | Status | +/- |
    |------|--------|-----|
    {for each file: | `{filename}` | {status} | +{additions}/-{deletions} |}
    
    ---
    
    ## Commits
    
    | SHA | Author | Date | Message |
    |-----|--------|------|---------|
    {for each commit: | `{sha:7}` | @{author.login} | {date} | {messageHeadline} |}
    
    ---
    
    ## Reviews
    
    ### Latest Review Status (per reviewer)
    
    | Reviewer | State | Date | Summary |
    |----------|-------|------|---------|
    {for each latestReview: | @{author.login} | {state} | {submittedAt} | {body:truncated} |}
    
    ### Full Review History
    
    {for each review in chronological order}
    #### Review by @{user.login} — {state} ({submittedAt})
    
    {body if any}
    
    ---
    {end for}
    
    ---
    
    ## Inline Code Comments
    
    {for each comment grouped by file}
    ### `{path}`
    
    {for each comment on file}
    **Line {line}** — @{user.login} ({created_at})
    > {body}
    
    {if has suggestion}
    ```suggestion
    {suggestion content}
    ```
    {end if}
    
    ---
    {end for}
    {end for}
    
    ---
    
    ## Conversation Comments
    
    {for each comment}
    ### @{user.login} ({created_at})
    
    {body}
    
    ---
    {end for}
    
    ---
    
    ## Timeline
    
    | Time | Event | Actor | Details |
    |------|-------|-------|---------|
    {for each timeline event: | {timestamp} | {event} | @{actor.login} | {details} |}
    
    ---
    
    ## CI/CD Status
    
    ### Check Runs
    
    | Check | Status | Conclusion | Duration |
    |-------|--------|------------|----------|
    {for each check_run: | {name} | {status} | {conclusion} | {duration} |}
    
    ### Status Checks
    
    **Overall**: {state}
    
    | Context | State | Description |
    |---------|-------|-------------|
    {for each status: | {context} | {state} | {description} |}
    
    ---
    
    ## Raw Data
    
    <details>
    <summary>PR Metadata (JSON)</summary>
    
    ```json
    {JSON from 01-pr-main.json}
    ```
    
    </details>
    
    <details>
    <summary>Inline Comments (JSON)</summary>
    
    ```json
    {JSON from 03-review-comments.json}
    ```
    
    </details>
    
    <details>
    <summary>Reviews (JSON)</summary>
    
    ```json
    {JSON from 05-reviews.json}
    ```
    
    </details>
    
    <details>
    <summary>Commits (JSON)</summary>
    
    ```json
    {JSON from 06-commits.json}
    ```
    
    </details>
    
    <details>
    <summary>Files (JSON)</summary>
    
    ```json
    {JSON from 07-files.json}
    ```
    
    </details>
    
    <details>
    <summary>Timeline (JSON)</summary>
    
    ```json
    {JSON from 09-timeline.json}
    ```
    
    </details>
    
    <details>
    <summary>Full Diff</summary>
    
    ```diff
    {content from 08-full-diff.patch}
    ```
    
    </details>
    
    ---
    
    *Generated: {timestamp}*
    *Tool: gh-pr-info skill*
    ```
    
    ### PowerShell Document Generator
    
    Add this after the extraction script to generate the document:
    
    ```powershell
    # Generate PR Report Document
    $prData = Get-Content "$outDir/01-pr-main.json" | ConvertFrom-Json
    $reviewComments = Get-Content "$outDir/03-review-comments.json" | ConvertFrom-Json
    $prComments = Get-Content "$outDir/04-pr-comments.json" | ConvertFrom-Json
    $reviews = Get-Content "$outDir/05-reviews.json" | ConvertFrom-Json
    $commits = Get-Content "$outDir/06-commits.json" | ConvertFrom-Json
    $files = Get-Content "$outDir/07-files.json" | ConvertFrom-Json
    $diff = Get-Content "$outDir/08-full-diff.patch" -Raw
    $timeline = Get-Content "$outDir/09-timeline.json" | ConvertFrom-Json
    
    # Categorize reviewers
    $approved = ($prData.latestReviews | Where-Object { $_.state -eq "APPROVED" }).author.login -join ", "
    $changesRequested = ($prData.latestReviews | Where-Object { $_.state -eq "CHANGES_REQUESTED" }).author.login -join ", "
    $commented = ($prData.latestReviews | Where-Object { $_.state -eq "COMMENTED" }).author.login -join ", "
    
    $report = @"
    ---
    # PR Report — Machine-Readable Metadata
    pr_number: $($prData.number)
    title: "$($prData.title -replace '"', '\"')"
    url: "$($prData.url)"
    state: "$($prData.state)"
    author: "$($prData.author.login)"
    created_at: "$($prData.createdAt)"
    updated_at: "$($prData.updatedAt)"
    merged_at: $(if ($prData.mergedAt) { "`"$($prData.mergedAt)`"" } else { "null" })
    closed_at: $(if ($prData.closedAt) { "`"$($prData.closedAt)`"" } else { "null" })
    base_branch: "$($prData.baseRefName)"
    head_branch: "$($prData.headRefName)"
    head_sha: "$($prData.headRefOid)"
    base_sha: "$($prData.baseRefOid)"
    additions: $($prData.additions)
    deletions: $($prData.deletions)
    changed_files: $($prData.changedFiles)
    mergeable: "$($prData.mergeable)"
    merge_state: "$($prData.mergeStateStatus)"
    is_draft: $($prData.isDraft.ToString().ToLower())
    review_decision: "$($prData.reviewDecision)"
    labels: [$($prData.labels.name -join ", ")]
    assignees: [$($prData.assignees.login -join ", ")]
    reviewers_approved: [$approved]
    reviewers_changes_requested: [$changesRequested]
    reviewers_commented: [$commented]
    ---
    
    # PR #$($prData.number): $($prData.title)
    
    > **URL**: $($prData.url)
    > **Author**: @$($prData.author.login)
    > **Branch**: ``$($prData.headRefName)`` → ``$($prData.baseRefName)``
    > **State**: $($prData.state) | **Review**: $($prData.reviewDecision) | **Mergeable**: $($prData.mergeable)
    
    ## Summary
    
    $($prData.body)
    
    ---
    
    ## Statistics
    
    | Metric | Value |
    |--------|-------|
    | Additions | +$($prData.additions) |
    | Deletions | -$($prData.deletions) |
    | Files Changed | $($prData.changedFiles) |
    | Commits | $($commits.Count) |
    | Reviews | $($reviews.Count) |
    | Inline Comments | $($reviewComments.Count) |
    | Conversation Comments | $($prComments.Count) |
    
    ---
    
    ## Files Changed
    
    | File | Status | +/- |
    |------|--------|-----|
    $($files | ForEach-Object { "| ``$($_.filename)`` | $($_.status) | +$($_.additions)/-$($_.deletions) |" } | Out-String)
    
    ---
    
    ## Commits
    
    | SHA | Author | Date | Message |
    |-----|--------|------|---------|
    $($commits | ForEach-Object { "| ``$($_.sha.Substring(0,7))`` | @$($_.author.login) | $($_.commit.author.date) | $($_.commit.message -split "`n" | Select-Object -First 1) |" } | Out-String)
    
    ---
    
    ## Reviews
    
    ### Latest Review Status (per reviewer)
    
    | Reviewer | State | Date | Summary |
    |----------|-------|------|---------|
    $($prData.latestReviews | ForEach-Object { "| @$($_.author.login) | $($_.state) | $($_.submittedAt) | $($_.body -replace "`n", " " -replace "\|", "\\|" | Select-Object -First 100)... |" } | Out-String)
    
    ---
    
    ## Inline Code Comments
    
    $($reviewComments | Group-Object -Property path | ForEach-Object {
        $file = $_.Name
        $comments = $_.Group
            @"
    ### ``$file``
    
    $($comments | ForEach-Object {
            @"
    **Line $($_.line)** — @$($_.user.login) ($($_.created_at))
    > $($_.body -replace "`n", "`n> ")
    
    ---
    "@
    } | Out-String)
    "@
    } | Out-String)
    
    ---
    
    ## Conversation Comments
    
    $(if ($prComments.Count -eq 0) { "*No conversation comments*" } else {
        $prComments | ForEach-Object {
            @"
    ### @$($_.user.login) ($($_.created_at))
    
    $($_.body)
    
    ---
    "@
        } | Out-String
    })
    
    ---
    
    ## Timeline
    
    | Time | Event | Actor | Details |
    |------|-------|-------|---------|
    $($timeline | Where-Object { $_.event } | ForEach-Object {
        $actor = if ($_.actor) { "@$($_.actor.login)" } elseif ($_.author) { $_.author.name } else { "-" }
        $details = switch ($_.event) {
            "committed" { $_.message -split "`n" | Select-Object -First 1 }
            "reviewed" { $_.state }
            "review_requested" { "requested @$($_.requested_reviewer.login)" }
            default { "-" }
        }
        $time = if ($_.created_at) { $_.created_at } elseif ($_.committer) { $_.committer.date } else { "-" }
        "| $time | $($_.event) | $actor | $details |"
    } | Out-String)
    
    ---
    
    ## Raw Data
    
    <details>
    <summary>PR Metadata (JSON)</summary>
    
    ``````json
    $(Get-Content "$outDir/01-pr-main.json" -Raw)
    ``````
    
    </details>
    
    <details>
    <summary>Inline Comments (JSON)</summary>
    
    ``````json
    $(Get-Content "$outDir/03-review-comments.json" -Raw)
    ``````
    
    </details>
    
    <details>
    <summary>Reviews (JSON)</summary>
    
    ``````json
    $(Get-Content "$outDir/05-reviews.json" -Raw)
    ``````
    
    </details>
    
    <details>
    <summary>Commits (JSON)</summary>
    
    ``````json
    $(Get-Content "$outDir/06-commits.json" -Raw)
    ``````
    
    </details>
    
    <details>
    <summary>Files (JSON)</summary>
    
    ``````json
    $(Get-Content "$outDir/07-files.json" -Raw)
    ``````
    
    </details>
    
    <details>
    <summary>Timeline (JSON)</summary>
    
    ``````json
    $(Get-Content "$outDir/09-timeline.json" -Raw)
    ``````
    
    </details>
    
    <details>
    <summary>Full Diff</summary>
    
    ``````diff
    $diff
    ``````
    
    </details>
    
    ---
    
    *Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")*
    *Tool: gh-pr-info skill*
    "@
    
    $report | Out-File -FilePath "$outDir/PR-$pr-report.md" -Encoding utf8
    Write-Host "Report generated: $outDir/PR-$pr-report.md"
    ```
    
    ---
    
    ## Output Interpretation
    
    ### Review States
    | State | Meaning |
    |-------|---------|
    | `APPROVED` | Reviewer approved changes |
    | `CHANGES_REQUESTED` | Reviewer requested modifications |
    | `COMMENTED` | Reviewer left comments only |
    | `DISMISSED` | Review was dismissed |
    | `PENDING` | Review in progress |
    
    ### Review Decision
    | Decision | Meaning |
    |----------|---------|
    | `APPROVED` | Required approvals met |
    | `CHANGES_REQUESTED` | Changes requested by reviewer |
    | `REVIEW_REQUIRED` | Awaiting required reviews |
    | `null` | No review policy or not applicable |
    
    ### Mergeable States (mergeStateStatus)
    | State | Meaning |
    |-------|---------|
    | `MERGEABLE` | Can be merged |
    | `CONFLICTING` | Has merge conflicts |
    | `UNKNOWN` | State not yet computed |
    | `BLOCKED` | Blocked by branch protection |
    | `BEHIND` | Base branch has new commits |
    | `CLEAN` | Ready to merge |
    | `DIRTY` | Merge would create conflicts |
    | `DRAFT` | PR is in draft state |
    | `HAS_HOOKS` | Pre-receive hooks must pass |
    | `UNSTABLE` | Checks are pending or failed |
    
    ### File Status
    | Status | Meaning |
    |--------|---------|
    | `added` | New file |
    | `removed` | Deleted file |
    | `modified` | Content changed |
    | `renamed` | File renamed |
    | `copied` | File copied |
    | `changed` | File mode changed |
    
    ### Author Association
    | Type | Meaning |
    |------|---------|
    | `OWNER` | Repository owner |
    | `MEMBER` | Organization member |
    | `COLLABORATOR` | Repository collaborator |
    | `CONTRIBUTOR` | Has contributed before |
    | `FIRST_TIMER` | First contribution to this repo |
    | `FIRST_TIME_CONTRIBUTOR` | First contribution to any repo |
    | `NONE` | No association |
    
    ---
    
    ## Useful Filters (jq examples)
    
    ### Human reviewers only (exclude bots)
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr/comments --jq '[.[] | select(.user.type != "Bot")]'
    ```
    
    ### Reviewers who requested changes
    ```powershell
    gh pr view $pr --json latestReviews -q '.latestReviews[] | select(.state == "CHANGES_REQUESTED") | .author.login'
    ```
    
    ### Files changed (names only)
    ```powershell
    gh pr view $pr --json files -q '.files[].path'
    ```
    
    ### Inline comments grouped by file
    ```powershell
    gh api repos/$owner/$repo/pulls/$pr/comments --jq 'group_by(.path) | .[] | {file: .[0].path, comments: [.[] | {line: .line, author: .user.login, body: .body}]}'
    ```
    
    ### Failed check runs
    ```powershell
    gh api repos/$owner/$repo/commits/$headSha/check-runs --jq '.check_runs[] | select(.conclusion == "failure") | {name: .name, url: .html_url}'
    ```
    
    ### Timeline summary
    ```powershell
    gh api repos/$owner/$repo/issues/$pr/timeline --jq '[.[] | .event] | group_by(.) | map({event: .[0], count: length})'
    ```
    
    ---
    
    ## Error Handling
    
    | Error | Cause | Solution |
    |-------|-------|----------|
    | `unknown field` | Field not in gh version | Remove field from --json |
    | `Could not resolve to a PullRequest` | PR doesn't exist | Verify PR number |
    | `HTTP 404` | Repo or PR not found | Check owner/repo/PR |
    | `HTTP 401` | Not authenticated | Run `gh auth login` |
    | `HTTP 403` | Rate limited or no access | Check permissions, wait |
    
    ---
    
    ## Completion Criteria
    
    - [ ] Main PR metadata retrieved (gh pr view)
    - [ ] REST API PR data retrieved
    - [ ] Inline code review comments retrieved
    - [ ] PR conversation comments retrieved
    - [ ] All reviews retrieved
    - [ ] Commits with details retrieved
    - [ ] Files with patch content retrieved
    - [ ] Full diff retrieved
    - [ ] Timeline events retrieved
    - [ ] Check runs / status retrieved
    
    ---
    
    ## Anti-patterns (avoid)
    
    - Using `reviewers` field (doesn't exist — use `reviewRequests`)
    - Forgetting inline comments are separate from `gh pr view`
    - Missing conversation comments (`/issues/{pr}/comments` vs `/pulls/{pr}/comments`)
    - Assuming all comments are from humans (check `user.type`)
    - Using only `reviews` instead of `latestReviews` (latter is deduplicated)
    - Forgetting timeline for complete history
    - Not fetching check runs separately (need head SHA first)
