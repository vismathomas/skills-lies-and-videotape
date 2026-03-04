---
title: Plan Review Import
description: "Parse exported PR review comments into structured review format for plan integration"
---

# Plan Review Import

> Parse exported PR review comments into structured review format for plan integration

:material-tag: `planning`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/plan-review-import/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/plan-review-import/SKILL.md){ .md-button .md-button--primary }

---

Parses exported PR review comments into structured review format for plan integration. Enables importing external feedback into the planning workflow.

## Usage Examples

### Import PR review feedback

```
Import the review comments from PR #42 into our plan review format.
```

### Parse review export

```
Parse this exported review comments file into structured review format.
```

### Integrate feedback into plan

```
Import review feedback and merge it into the current implementation plan.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    ## Purpose
    
    Transform raw review feedback (from GitHub PR exports or manual paste) into a structured `.review.md` file that can be programmatically integrated into the canonical plan.
    
    ## When to Use
    
    - After running `scripts/get-plan-review.sh` or `scripts/Get-PlanReview.ps1`
    - When manually pasting review comments into a file
    - As part of the plan review round-trip workflow
    
    ## Input Sources
    
    ### 1. GitHub Export (Preferred)
    
    Run the export script first:
    ```bash
    # Bash
    ./scripts/get-plan-review.sh 42
    
    # PowerShell
    .\scripts\Get-PlanReview.ps1 -PrNumber 42
    ```
    
    This creates `project docs`.
    
    ### 2. Manual Paste
    
    Create a file with raw comments:
    ```
    issues/references/<issue>.github-review.md
    ```
    
    Paste PR discussion content directly.
    
    ## Output Format
    
    Produces `project docs`:
    
    ```markdown
    # Review for <ISSUE-ID>
    
    ## Metadata
    
    - **PR**: #<number>
    - **Reviewers**: alice, bob
    - **Status**: pending | accepted | blocked
    - **Imported**: <timestamp>
    
    ## Accepted Changes
    
    Changes reviewers explicitly approved or suggested:
    
    - [Section: Overview] Clarify success metrics for the feature
    - [Section: Risks] Add risk about dependency X being in beta
    
    ## Open Questions
    
    Questions needing resolution before implementation:
    
    - [Section: Data Model] Should we normalize table Y or keep it denormalized?
    - [Section: API] What authentication method should the endpoint use?
    
    ## Blockers
    
    Issues that must be resolved before proceeding:
    
    - [Section: API] Security review required for exposed endpoint Z
    - [Section: Dependencies] License compatibility check needed
    
    ## Conflicts
    
    Contradictory feedback requiring human resolution:
    
    - [Section: Architecture] alice suggests microservices, bob prefers monolith
      - Keep both as open questions per workflow rules
    
    ## Raw Comments
    
    Original comments preserved for reference:
    
    > **alice** on `src/api.ts`:
    > "Consider adding rate limiting here"
    
    > **bob** (general):
    > "Overall LGTM, minor suggestions inline"
    ```
    
    ## Parsing Rules
    
    ### Comment Classification
    
    The skill uses best-effort parsing with these heuristics:
    
    | Pattern | Classification |
    |---------|----------------|
    | `suggestion`, `consider`, `maybe`, `could` | Open Question |
    | `must`, `required`, `blocking`, `critical` | Blocker |
    | `LGTM`, `approved`, `looks good` | Accepted |
    | `?` at end of comment | Open Question |
    | GitHub suggestion block | Accepted Change |
    | Contradictory comments on same section | Conflict |
    
    ### Section Mapping
    
    Comments are mapped to plan sections by:
    1. File path mentioned (`src/api.ts` → API section)
    2. Line reference in preview file
    3. Explicit section mention (`## Overview` → Overview)
    4. Keyword matching as fallback
    
    ### Template Recognition
    
    If reviewers use the suggested template:
    ```markdown
    ### Review comment
    - Section: <section>
    - Type: question | suggestion | blocker
    - Comment: ...
    ```
    
    Parsing is deterministic. Otherwise, best-effort heuristics apply.
    
    ## Conflict Handling
    
    When multiple reviewers disagree:
    1. Both positions are recorded
    2. Classified as "Conflict"
    3. **No auto-resolution** — human must decide
    4. Conflicts appear prominently in review file
    
    ## Workflow Integration
    
    ```
    ┌─────────────────┐    ┌──────────────────────┐    ┌─────────────────────┐
    │ GitHub PR       │───▶│ Export Script        │───▶│ .github-review.md   │
    │ Comments        │    │ (bash/ps1)           │    │ (raw export)        │
    └─────────────────┘    └──────────────────────┘    └──────────────────────┘
                                                                  │
                                                                  ▼
    ┌─────────────────┐    ┌──────────────────────┐    ┌─────────────────────┐
    │ Updated Plan    │◀───│ plan-integrate-      │◀───│ .review.md          │
    │ + Preview       │    │ review skill         │    │ (structured)        │
    └─────────────────┘    └──────────────────────┘    └─────────────────────┘
    ```
    
    ## Example Invocation
    
    ```
    /plan-review-import FEAT-0123
    
    Importing review for FEAT-0123...
    Source: issues/references/FEAT-0123.github-review.md
    
    Parsed:
    - 3 accepted changes
    - 5 open questions
    - 1 blocker
    - 1 conflict
    
    Output: issues/references/FEAT-0123.review.md
    
    Next: Run / FEAT-0123 to apply changes
    ```
    
    ## Error Handling
    
    | Condition | Action |
    |-----------|--------|
    | No export file found | Prompt user to run export script or paste comments |
    | Empty comments | Create minimal review file with "No feedback" status |
    | Malformed export | Best-effort parse, preserve raw in "Raw Comments" section |
    | Missing issue ID | Prompt for issue ID |
    
    ## Related Skills
    
    -  — Consumes review file to update plan
    - `plan-preview` — Regenerates preview after plan update
    -  — Creates the initial plan
