---
title: Plan Preview Generator
description: "Transform implementation plans into concise stakeholder-friendly summaries with file change overviews, component listings, and optional flow diagrams."
---

# Plan Preview Generator

> Transform implementation plans into concise stakeholder-friendly summaries with file change overviews, component listings, and optional flow diagrams.

:material-tag: `planning`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/plan-preview/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/plan-preview/SKILL.md){ .md-button .md-button--primary }

---

Transforms detailed implementation plans into concise, stakeholder-friendly summaries with file change overviews, component listings, and optional flow diagrams. Configurable detail levels.

## Usage Examples

### Summarize a plan

```
Generate a stakeholder-friendly preview of this implementation plan.
```

### Low-detail preview

```
Create a high-level plan summary — just objective, approach, and file count.
```

### Detailed preview with diagrams

```
Generate a detailed plan preview with flow diagrams and method signatures.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Plan Preview Workflow
    
    ## Purpose
    
    Generate concise, stakeholder-ready summaries from detailed implementation plans. Enables developers, tech leads, and project owners to understand and approve planned changes without reviewing full technical details.
    
    ## Input Sources
    
    Accept plan from one of:
    
    | Source | Format | Example |
    |--------|--------|---------|
    | Issue ID | `{TYPE}-{NUMBER}@{HASH}` | `PLAN-0295@a1b2c3` |
    | File path | Absolute or relative path | `project docs` |
    | Current context | Plan in conversation | (no argument needed) |
    
    **Resolution order**:
    1. If issue ID provided → resolve to `project docs`
    2. If path provided → read directly
    3. If neither → check if plan exists in current conversation context
    
    ## Comment Markers
    
    Plans or updated content may contain embedded review comments. The skill recognizes these markers:
    
    ### Standard Comment Format
    
    ```markdown
    <!-- COMMENT: @reviewer: comment text -->
    ```
    
    ### File-Specific Comment Format
    
    ```markdown
    <!-- COMMENT: @reviewer [file.py:42]: comment about specific line -->
    ```
    
    ### Resolved Comment Format
    
    ```markdown
    <!-- COMMENT-RESOLVED: @reviewer: original comment text -->
    ```
    
    ### Examples
    
    ```markdown
    <!-- COMMENT: @sarah: Should we add input validation here? -->
    <!-- COMMENT: @john [api/handler.py:156]: Consider using async here for better performance -->
    <!-- COMMENT-RESOLVED: @mike: Add error logging — addressed in commit abc123 -->
    ```
    
    ### Comment Parsing Rules
    
    1. Reviewer name follows `@` and ends at `:` or `[`
    2. Optional file:line reference in `[brackets]`
    3. Everything after the last `:` is the comment text
    4. `COMMENT-RESOLVED` indicates the comment has been addressed
    5. Comments without the marker prefix are not parsed
    
    ## Procedure
    
    ### Step 0: Check for Preferences
    
    **At the start of the skill, check for `preferences.md` next to this SKILL.md:**
    
    **CRITICAL: File Path Resolution**
    
    The skill implementation must resolve the preferences.md file path **relative to the location of this SKILL.md file**, not relative to the current working directory or  folder.
    
    ```
    # Pseudocode for path resolution:
    SKILL_DIR = directory_containing_this_file  # e.g., skills/plan-preview/
    PREFERENCES_PATH = SKILL_DIR / "preferences.md"
    
    IF file_exists(PREFERENCES_PATH):
        content = read_file(PREFERENCES_PATH)
        Parse frontmatter to extract: language, confidence_level, mermaid_charts, comment_integration, template_sections, exclude_sections
        Use stored preferences for language, confidence, sections, diagram rules, comment handling
        Log: "Loaded preferences from {PREFERENCES_PATH}"
    ELSE:
        Log: "No preferences found at {PREFERENCES_PATH}, will proceed to standard interview"
        Proceed to standard interview (will create preferences.md after Step 3)
    ```
    
    **Implementation Notes:**
    - Resolve skill directory dynamically (do NOT hardcode paths)
    - Verify file can be read before attempting to parse
    - Log all path operations for debugging
    - If preferences file is corrupt or unreadable, warn user and proceed to recreate
    
    **Note**: If preferences.md doesn't exist, after collecting user input in Steps 2-3, the skill should offer to create it. The user can answer "Yes" to create, and preferences will be saved for future runs. Users can later update preferences by asking "Update my preferences for plan-preview."
    
    ### Step 1: Resolve Input
    
    ```
    IF issue_id provided:
        path = issues/references/{issue_id}-plan.md
        IF NOT exists(path):
            ERROR "Plan file not found for issue {issue_id}"
    ELSE IF file_path provided:
        path = file_path
    ELSE:
        Scan conversation context for plan content
    ```
    
    ### Step 2: Language Selection
    
    **Ask user** (one question):
    
    > "What language should the summary be in? (default: English)"
    
    Common choices:
    - English (default)
    - Norwegian (Norsk)
    - Other (specify)
    
    **Wait for response before proceeding.**
    
    ### Step 3: Confidence Level Selection
    
    **Ask user** (one question):
    
    > "What confidence level is this plan? This affects detail level in the summary:
    > - **LOW** — More details, explicit changes, method signatures
    > - **NORMAL** — Balanced overview (default)
    > - **HIGH** — Sparse, broad outlines only"
    
    **Wait for response before proceeding.**
    ### Step 3.5: Additional Detail Collection
    
    After language and confidence, ask targeted questions to tailor the preview based on plan content:
    
    1. Objective emphasis: "Any key outcomes to highlight in the objective?"
    2. Sections: "Which sections should be included or excluded? (Objective, Approach, Files Changed, New Components, Dependencies, Flow, Risks, Edge Cases)"
    3. Diagram preference: "Include a flow diagram if applicable? (Yes/No/Minimal)"
    4. Special preferences: "Any formatting or terminology preferences to apply?"
    
    Wait for responses before proceeding.
    
    ### Step 3.6: Comment Mode Selection
    
    **Ask user** (one question):
    
    > "Does this plan have embedded review comments to include?
    > - **YES** — Parse `<!-- COMMENT: ... -->` markers and render in summary
    > - **NO** — Ignore any comment markers (default)"
    
    **Wait for response before proceeding.**
    
    If YES, the skill will:
    1. Scan plan content for comment markers
    2. Parse reviewer, optional file:line, and comment text
    3. Group comments by status (open vs resolved)
    4. Include "Review Comments" section in output
    
    ### Step 3.7: GitHub Comment Fetching (Optional)
    
    **If gh CLI integration desired, ask user:**
    
    > "Is this plan linked to a GitHub PR or Issue? Provide the number to fetch comments, or press Enter to skip."
    
    **Processing logic:**
    
    ```
    IF github_number provided:
        IF NOT gh_cli_available():
            WARN "gh CLI not found. Skipping GitHub comment fetch."
            CONTINUE without GitHub comments
        
        IF NOT gh_authenticated():
            WARN "gh not authenticated. Run 'gh auth login' first."
            CONTINUE without GitHub comments
        
        TRY:
            IF input looks like PR (starts with # or is just a number):
                comments = run_command("gh pr view {number} --json comments")
            ELSE IF input is "issue:{number}":
                comments = run_command("gh issue view {number} --json comments")
            
            Convert to internal comment marker format
            Merge with any existing embedded comments
            Mark source: <!-- COMMENT: @user [from-github]: text -->
        CATCH error:
            WARN "Could not fetch comments: {error}"
            CONTINUE without GitHub comments
    ELSE:
        Skip GitHub comment fetching
    ```
    
    **Note**: This step is entirely optional and degrades gracefully if gh CLI is unavailable.
    
    ### Step 4: Extract Plan Elements
    
    Parse the implementation plan and extract elements **based on confidence level**:
    
    #### Detail Level by Confidence
    
    | Element | LOW Confidence | NORMAL Confidence | HIGH Confidence |
    |---------|----------------|-------------------|-----------------|
    | **Objective** | 2-3 sentences with context | 1-2 sentences | 1 sentence |
    | **Approach** | 5-7 sentences, edge cases noted | 2-3 sentences | 1 sentence max |
    | **Files** | Full paths + line estimates + change description | Paths + change type + brief purpose | Count only ("3 files modified") |
    | **Components** | Name + signature + params + return type | Name + one-line purpose | Category counts ("2 endpoints, 1 validator") |
    | **Dependencies** | Package names + versions + why needed | Package names | "New dependencies: Yes/No" |
    | **Risks** | Detailed risk analysis with mitigations | Bullet list of risks | Omit unless critical |
    | **Diagram** | Always if any flow exists | Only if branching logic | Never |
    
    ### Step 5: Flow Diagram Decision
    
    **Confidence-aware diagram rules:**
    
    | Confidence | Diagram Rule |
    |------------|--------------|
    | LOW | Include diagram if plan has ANY sequential flow |
    ### Step 5.5: Template Override (template.md)
    
    Before generating, check for `template.md` in the same directory as this SKILL.md. If present, use it instead of built-in templates.
    
    Pseudocode:
    ```
    SKILL_DIR = directory_containing_this_SKILL.md
    TEMPLATE_PATH = SKILL_DIR / "template.md"
    IF file_exists(TEMPLATE_PATH):
        template = read_file(TEMPLATE_PATH)
        Log: "Using custom template at {TEMPLATE_PATH}"
    ELSE:
        template = select_built_in_template_by_confidence_and_language()
    ```
    Notes:
    - Resolve path relative to SKILL location (no hardcoded CWD)
    - Support placeholders used in built-in templates
    - If template.md is malformed, warn and fall back to built-in
    ```
    | NORMAL | Include only if branching logic or state transitions |
    | HIGH | Never include diagrams |
    
    **Standard criteria (NORMAL confidence):**
    - Plan has branching logic (if/else paths)
    - Plan has multi-step sequences with dependencies
    - Plan involves state transitions
    - Plan has complex component interactions
    
    ### Step 6: Generate Summary
    
    Structure varies by confidence level:
    
    #### LOW Confidence Template
    
    ```markdown
    # Plan Summary: {objective_short}
    
    **Issue**: {issue_id}
    **External reference**: {if applicable, like JIRA-issue or GitHub link}
    **Generated**: {date}
    **Confidence**: LOW (detailed preview)
    
    ## Objective
    
    {2-3 sentences with full context and background. If a bug, what is the problem, if a feature, what is solved or provided. If an enhancement, what is improved. When can this be considered done? Concrete and testable success criteria.}
    
    ## Approach
    
    {5-7 sentences explaining the implementation strategy}
    
    **Edge Cases Considered:**
    - {edge case 1}
    - {edge case 2}
    
    ## Files Changed
    
    { for each file changed or created, list the following formatted structure:
    
    ### File: `{file_path}`
    - **Change Type**: {New/Modified/Deleted}
    - **Purpose**: {brief description of why this file is changed/created}
    - **Gherkin-feature or User-story association**: {if applicable}
    - **UX reference**: {if applicable, link to designs or mockups}
    
    ```language/format
    
    class Example: // always mention the class or function
    
        def method_name(param1: Type1, param2: Type2) -> ReturnType: // always type the function or method signature, including parameter and return types
            { 
                - brief summary of implementation logic, a bulleted list if complex, edge cases handled, etc.
                - if there are larger changes to existing code or new complex methods, include full samples of that code with explanatory comments; otherwise, just summarize
            }
    ```
    }
    ```
    
    #### NORMAL Confidence Template
    
    (Use existing Step 5 template from original skill)
    
    #### HIGH Confidence Template
    
    ```markdown
    # Plan Summary: {objective_short}
    
    **Issue**: {issue_id}
    **External reference**: {if applicable, like JIRA-issue or GitHub link}
    **Generated**: {date}
    **Confidence**: NORMAL
    
    ## Objective
    
    {2-3 sentences with full context and background. If a bug, what is the problem, if a feature, what is solved or provided. If an enhancement, what is improved. When can this be considered done? Concrete and testable success criteria.}
    
    ## Approach
    
    {5-7 sentences explaining the implementation strategy}
    
    **Edge Cases Considered:**
    - {edge case 1}
    - {edge case 2}
    
    ## Files Changed
    
    { for each file changed or created, list the following formatted structure:
    
    ### File: `{file_path}`
    - **Change Type**: {New/Modified/Deleted}
    - **Purpose**: {brief description of why this file is changed/created}
    - **Gherkin-feature or User-story association**: {if applicable}
    - **UX reference**: {if applicable, link to designs or mockups}
    
    }
    ```
    
    #### HIGH Confidence Template
    
    (Use existing Step 5 template from original skill)
    
    #### HIGH Confidence Template
    
    ```markdown
    # Plan Summary: {objective_short}
    
    **Issue**: {issue_id}
    **External reference**: {if applicable, like JIRA-issue or GitHub link}
    **Confidence**: HIGH
    
    ## Objective
    
    {2-3 sentences with full context and background. If a bug, what is the problem, if a feature, what is solved or provided. If an enhancement, what is improved. When can this be considered done? Concrete and testable success criteria.}
    
    ```
    
    ### Step 6.5: Review Comments Section (if comment mode enabled)
    
    **If user selected YES for comment mode in Step 3.6, add this section after Files Changed:**
    
    #### Review Comments Template (LOW/NORMAL Confidence)
    
    ```markdown
    ## Review Comments
    
    {if any comments parsed from plan or fetched from GitHub}
    
    ### Open Comments
    
    {for each open comment, render as blockquote with attribution}
    
    > **@{reviewer}**{if file:line} on `{file}:{line}`{endif}:
    > "{comment_text}"
    
    ### Resolved Comments
    
    {for each resolved comment, render with strikethrough}
    
    > ~~**@{reviewer}**{if file:line} on `{file}:{line}`{endif}:~~
    > ~~"{comment_text}"~~ ✅ Resolved
    
    {if comments were fetched from GitHub}
    ---
    *Comments fetched from GitHub PR #{number} on {fetch_date}*
    {endif}
    ```
    
    #### Comment Rendering Rules
    
    | Confidence | Comment Rendering |
    |------------|-------------------|
    | LOW | Full section with all comments, grouped by file if applicable |
    | NORMAL | Summary section with open comments only |
    | HIGH | Omit comments section entirely |
    
    #### Example Output
    
    **LOW Confidence with comments:**
    
    ```markdown
    ## Review Comments
    
    ### Open Comments
    
    > **@sarah** on `api/handler.py:42`:
    > "Should we add input validation here?"
    
    > **@john** on `api/handler.py:156`:
    > "Consider using async here for better performance"
    
    ### Resolved Comments
    
    > ~~**@mike** on `utils/helpers.py:23`:~~
    > ~~"Add error logging"~~ ✅ Resolved
    
    ---
    *2 open comments, 1 resolved. Fetched from GitHub PR #123 on 2026-01-28.*
    ```
    
    **NORMAL Confidence with comments:**
    
    ```markdown
    ## Review Comments (2 open)
    
    - **@sarah** on `api/handler.py:42`: Add input validation
    - **@john** on `api/handler.py:156`: Consider async
    ```
    
    ### Step 7: Present & Offer Options
    
    Display the generated summary, then ask:
    
    > "Summary generated. What would you like to do?
    > 
    > 1. **Open in editor** — Opens as new file in VS Code
    > 2. **Save alongside plan** — Saves as `project docs`
    > 3. **Done** — Keep in chat only"
    
    ### Step 7.5: Create Validation Snapshot (MANDATORY if saved)
    
    **When user chooses option 2 (save alongside plan), this step is MANDATORY.**
    
    The validation snapshot enables post-implementation comparison to ensure actual changes match the approved preview.
    
    #### Snapshot Content
    
    Append a validation snapshot section to the preview file:
    
    ```markdown
    ---
    
    ## Validation Snapshot
    
    **Generated**: {timestamp}
    **Preview ID**: {issue_id}-preview
    **For validation by**: , 
    
    ### Expected Changes
    
    | File | Change Type | Scope Estimate |
    |------|-------------|----------------|
    | {file1} | {New/Modified/Deleted} | {lines estimate} |
    | {file2} | {New/Modified/Deleted} | {lines estimate} |
    
    ### Expected Components
    
    | Component | Type | Location |
    |-----------|------|----------|
    | {component1} | {class/function/endpoint/...} | {file:line} |
    | {component2} | {class/function/endpoint/...} | {file:line} |
    
    ### Security-Sensitive Files
    
    {List any files matching security-sensitive patterns or keywords:}
    - Path patterns: `**/auth/**`, `**/security/**`, `**/*secret*`, `**/*cred*`, `**/*token*`, `**/config/**`
    - Content keywords: password, api_key, secret, credential, auth, permission, encryption
    
    | File | Reason |
    |------|--------|
    | {file} | {matches pattern/contains keyword} |
    
    *If none: "No security-sensitive files in this preview."*
    
    ### Validation Rules
    
    - **Extra files changed**: REQUIRES explicit approval
    - **Missing planned changes**: BLOCKS completion until implemented or plan updated
    - **Scope deviation >10%**: BLOCKS completion (strict mode per interview)
    - **Security-sensitive file touched**: MANDATORY human review
    ```
    
    #### Validation Issue Creation
    
    After saving preview with snapshot, create a linked validation issue:
    
    1. Create validation issue via :
    
    ```markdown
    ## VAL-{counter}@{hash} — Validate implementation of {issue_id}
    
    id: VAL-{counter}@{hash}
    title: "Validate implementation of {issue_id}"
    type: VAL
    status: todo
    priority: critical
    confidence: {inherit from parent or low}
    created: {date}
    tags: [validation, plan-preview, mandatory]
    parent_issue: {issue_id}
    preview_file: references/{issue_id}-preview.md
    
    ### Description
    
    Validate that implementation of {issue_id} matches the approved plan preview.
    
    ### Validation Checks
    
    - [ ] All expected files were changed
    - [ ] No unexpected files were changed
    - [ ] Scope stayed within 10% of estimate
    - [ ] Security-sensitive files reviewed by human (if applicable)
    
    ### Log
    
    - {date}: Created automatically from plan-preview
    ```
    
    4. Log in original issue: `- {date}: Validation issue VAL-{counter}@{hash} created`
    5. Display to user:
    
    ```
    ✅ Preview saved: issues/references/{issue_id}-preview.md
    📋 Validation issue created: VAL-{counter}@{hash}
    
    This implementation MUST pass validation before completion.
    ```
    
    ## Completion Criteria
    
    - [ ] Plan source resolved (issue ID, path, or context)
    - [ ] Language confirmed with user
    - [ ] Confidence level confirmed with user
    - [ ] Comment mode confirmed with user (YES/NO)
    - [ ] If comment mode YES: comments parsed and rendered
    - [ ] If GitHub number provided: comments fetched (or graceful skip if gh unavailable)
    - [ ] Summary generated with appropriate detail level
    - [ ] Mermaid diagram included according to confidence rules
    - [ ] Output presented to user
    - [ ] User chose action (editor/save/done)
    
    ## Preferences Management
    
    ### Creating Preferences (First Run)
    
    If `preferences.md` does not exist after Steps 2-3, offer to create it:
    
    > "Would you like me to save these preferences? This will create `preferences.md` so I remember them for future plan previews."
    
    **If user says "Yes":**
    
    Conduct a short interview (one question at a time) to gather preferences:
    
    1. **Language** (already have from Step 2)
       > "Confirmed language: {language}. Is this your preference for future previews?"
    
    2. **Confidence Level** (already have from Step 3)
       > "Confirmed confidence level: {confidence}. Should I use this as default for future previews?"
    
    3. **Mermaid Charts**
       > "Do you want Mermaid flow diagrams in previews?
       > - YES: Always include if plan has flow logic
       > - NO: Never include diagrams
       > - MINIMAL: Only for complex flows (more detail)"
       
    4. **Template Sections to Use**
       > "Which sections should I always include in your previews? (select all that apply)
       > - ✓ Objective
       > - ✓ Approach
       > - ✓ Files Changed (table format)
       > - ✓ New Components
       > - ✓ Dependencies
       > - ✓ Flow Overview (if applicable)
       > - ✓ Risks & Considerations
       > - Other (specify)?"
    
    5. **Sections to Exclude**
       > "Are there any sections you'd prefer NOT to see in previews?
       > - Examples: Edge Cases, Detailed Risk Analysis, Dependency Versions, etc.
       > - Or leave blank to include all available sections"
    
    6. **Comment Integration**
       > "How should review comments be handled?
       > - YES: Always ask about embedded comments and GitHub fetch
       > - NO: Never include comments section
       > - ASK: Ask each time (default)"
    
    7. **Additional Preferences**
       > "Is there anything else I should remember about your preferences?
       > - Format preferences (tables, bullet points, etc.)
       > - Detail level for component descriptions
       > - Any special terminology or conventions
       > - Or leave blank if no other preferences"
    
    **After interview, create `preferences.md` with ROBUST PATH HANDLING:**
    
    **CRITICAL PATH RESOLUTION for Writing:**
    
    ```
    # Pseudocode for creating preferences file:
    SKILL_DIR = directory_containing_this_SKILL.md  # skills/plan-preview/
    PREFERENCES_PATH = SKILL_DIR / "preferences.md"
    
    TRY:
        content = generate_preferences_markdown(responses)
        write_file(PREFERENCES_PATH, content)
        IF file_exists(PREFERENCES_PATH):
            Log: "✓ Preferences saved to {PREFERENCES_PATH}"
        ELSE:
            Error: "Failed to verify file was created at {PREFERENCES_PATH}"
            Fallback: Ask user to save manually
    CATCH permission_error:
        Error: "Cannot write to {PREFERENCES_PATH} — check permissions"
        Ask user if alternative location acceptable
    ```
    
    **Template for preferences.md:**
    
    ```markdown
    ---
    name: plan-preview preferences
    description: User preferences for plan preview generation
    language: {language}
    confidence_level: {confidence}
    mermaid_charts: {YES|NO|MINIMAL}
    comment_integration: {YES|NO|ASK}
    template_sections: [list of sections to include]
    exclude_sections: [list of sections to exclude]
    date_created: {today's date}
    date_updated: {today's date}
    ---
    
    # Plan Preview Preferences
    
    ## Summary
    
    These preferences customize how plan previews are generated for the plan-preview skill.
    
    ## Settings
    
    **Language**: {language}
    **Default Confidence Level**: {confidence}
    **Mermaid Charts**: {YES/NO/MINIMAL}
    **Comment Integration**: {YES/NO/ASK}
    
    ### Sections to Include
    {bulleted list}
    
    ### Sections to Exclude
    {bulleted list}
    
    ### Additional Notes
    {any other preferences}
    
    ---
    
    *These preferences are stored in `skills/plan-preview/preferences.md`*
    *Update these preferences anytime by asking to "Update my preferences for plan-preview."*
    ```
    
    **Save location**: `skills/plan-preview/preferences.md` (same directory as SKILL.md)
    
    **Verification**: After writing, verify:
    - [ ] File exists at correct path
    - [ ] File is readable
    - [ ] Frontmatter is valid YAML
    - [ ] All required fields present
    - [ ] Log confirmation message to user
    
    ### Updating Preferences (Subsequent Runs)
    
    When user asks to update preferences (e.g., "Update my preferences for this skill"):
    
    1. **Resolve preferences.md path** (same as Step 0)
       ```
       SKILL_DIR = directory_containing_this_SKILL.md
       PREFERENCES_PATH = SKILL_DIR / "preferences.md"
       ```
    
    2. **Read current preferences.md**
       ```
       IF NOT file_exists(PREFERENCES_PATH):
           Error: "Preferences not found at {PREFERENCES_PATH}"
           Offer to create new preferences instead
       ELSE:
           Parse current settings for context
       ```
    
    3. **Re-interview user** with same 6 questions (Steps 1-6 above)
       > Show current values: "Current language: English. Keep or change?"
    
    4. **Ask at the end**: "Anything else to add or change?"
    
    5. **Update preferences.md** with new values and update `date_updated`
       ```
       content = update_preferences_markdown(old_content, responses)
       write_file(PREFERENCES_PATH, content)
       Verify file was written successfully
       Log: "✓ Preferences updated"
       ```
    
    ## Anti-patterns (avoid)
    
    - ❌ Do not repeat information from instructions in the summary
    - ❌ Generating output before asking for language preference
    - ❌ Generating output before asking for confidence level
    - ❌ Including Mermaid diagrams for HIGH confidence plans
    - ❌ Providing sparse details for LOW confidence plans
    - ❌ **CRITICAL**: Comment-only code blocks for LOW confidence — all code blocks must contain actual executable code, not just comment placeholders like `// - Does X` or `// - Returns Y`
    - ❌ Inconsistent detail levels within the same preview — if one file has full code, ALL files must have full code (for LOW confidence)
    - ❌ Assuming English without asking
    - ❌ Assuming NORMAL confidence without asking
    - ❌ Saving file without user consent
    - ❌ Creating preferences.md without user consent
    - ❌ Using old preferences without reminding user they exist
    - ❌ Creating preferences but not letting user update them
    - ❌ **CRITICAL**: Saving preferences.md to `project docs` or any location other than the skill directory
    - ❌ **CRITICAL**: Using hardcoded paths that don't account for varying working directories
    - ❌ **CRITICAL**: Saving preferences without verifying file was created successfully
    - ❌ **CRITICAL**: Not logging the file path where preferences were saved
    - ❌ **CRITICAL**: Losing preferences if unable to write to correct location (must inform user)
    - ❌ Including review comments section when user selected NO for comment mode
    - ❌ Silently skipping GitHub comment fetch without warning when gh CLI unavailable
    - ❌ Including comments in HIGH confidence previews (comments are omitted for HIGH)
    - ❌ Showing resolved comments in NORMAL confidence (NORMAL shows open only)
    
    ## Examples
    
    ### Example 1: HIGH Confidence (Brief Overview)
    
    **User**: "Preview plan for FEAT-0042@abc123"
    
    **Agent**:
    1. Resolves `project docs`
    2. Asks: "What language?" → User: "English"
    3. Asks: "What confidence level?" → User: "High"
    4. Generates brief summary (no diagram):
    
    ```markdown
    # Plan Summary: Add User Settings API
    
    **Issue**: FEAT-0042@abc123
    **Confidence**: HIGH (overview)
    
    ## Objective
    Add CRUD endpoints for user settings.
    
    ## Approach
    RESTful API with validation middleware.
    
    ## Scope
    - **Files**: 4 files (2 new, 2 modified)
    - **Components**: 1 service, 4 endpoints
    - **Dependencies**: None new
    ```
    
    ### Example 2: NORMAL Confidence (Standard)
    
    **User**: (plan in context) "Create preview in Norwegian"
    
    **Agent**:
    1. Detects plan in context
    2. Language already specified: Norwegian
    3. Asks: "What confidence level?" → User: "Normal"
    4. Generates standard summary with optional diagram (if workflow has branches)
    
    ### Example 3: LOW Confidence (Detailed Review)
    
    **User**: "Preview this complex migration plan, I need detailed review"
    
    **Agent**:
    1. Detects "detailed review" signals LOW confidence
    2. Asks: "What language?" → User: "English"  
    3. Confirms: "LOW confidence for detailed review. Correct?"
    4. Generates comprehensive summary with detailed tables, diagrams, and risk matrix
    
    ### Example 4: Diagram Decision by Confidence
    
    | Confidence | Plan Type | Diagram Decision |
    |------------|-----------|------------------|
    | HIGH | Any | ❌ Skip — keep brief |
    | NORMAL | Simple CRUD | ❌ Skip — linear operations |
    | NORMAL | Workflow with branches | ✅ Include — decision points |
    | LOW | Any | ✅ Include — detailed review |
    ### Example 5: Comment Integration from GitHub PR
    
    **User**: "Preview plan FEAT-0100@abc with comments from PR #45"
    
    **Agent**:
    1. Resolves plan file
    2. Asks: "What language?" → User: "English"
    3. Asks: "What confidence level?" → User: "Normal"
    4. Asks: "Include embedded review comments?" → User: "Yes"
    5. Asks: "GitHub PR/Issue number?" → User: "#45"
    6. Fetches comments from PR #45 via `gh pr view 45 --json comments`
    7. Generates summary with Review Comments section:
    
    ```markdown
    # Plan Summary: Add User Authentication
    
    **Issue**: FEAT-0100@abc
    **Confidence**: NORMAL
    
    ## Objective
    Implement OAuth2 authentication flow.
    
    ## Approach
    Add OAuth2 middleware with token validation.
    
    ## Files Changed
    ...
    
    ## Review Comments (2 open)
    
    - **@sarah** on `auth/middleware.py:42`: Consider rate limiting here
    - **@john** [from-github]: Should we support refresh tokens?
    
    ---
    *Comments fetched from GitHub PR #45 on 2026-01-28*
    ```
