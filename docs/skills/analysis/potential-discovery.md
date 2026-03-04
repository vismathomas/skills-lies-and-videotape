---
title: Potential Discovery
description: "Analyze incoming content (text, files, folders, URLs) to extract purpose, create summaries, and identify potential value for the current project."
---

# Potential Discovery

> Analyze incoming content (text, files, folders, URLs) to extract purpose, create summaries, and identify potential value for the current project.

:material-tag: `analysis`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/potential-discovery/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/potential-discovery/SKILL.md){ .md-button .md-button--primary }

---

Analyzes incoming content (text, files, folders, URLs) to extract purpose, create extensive summaries, and identify potential value for the current project. Suggests concrete integration opportunities.

## Usage Examples

### Analyze a library

```
Analyze the ./incoming/result-monad/ library and assess its potential for our project.
```

### Evaluate a competitor

```
Analyze https://github.com/competitor/tool — what can we learn from their approach?
```

### Review a spec document

```
Analyze this API spec and identify what's useful for our implementation.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Potential Discovery Workflow
    
    ## Purpose
    
    Perform deep analysis of incoming content to:
    1. Extract and understand its core purpose
    2. Create extensive, structured summaries
    3. Identify potential value and applications for the current project
    4. Suggest concrete integration opportunities or inspired improvements
    
    ## When to Use
    
    - Evaluating a new library, tool, or framework
    - Reviewing incoming code contributions or PRs
    - Analyzing competitor products or similar solutions
    - Assessing documentation, specs, or RFCs
    - Exploring repositories for reusable patterns
    - Reviewing articles, blog posts, or research papers
    
    ## Input Types
    
    | Type | Description | Example |
    |------|-------------|---------|
    | **Text** | Raw text, markdown, documentation | Pasted README, spec doc |
    | **File** | Single file analysis | `analyze: ./incoming/proposal.md` |
    | **Folder** | Directory tree analysis | `analyze: ./incoming/new-library/` |
    | **URL** | Web content (requires fetch capability) | `analyze: https://github.com/user/repo` |
    
    ## Procedure
    
    ### Phase 1: Content Ingestion
    
    1. **Identify content type** (text/file/folder/URL)
    2. **Load content**:
       - Text: Use directly
       - File: Read file contents
       - Folder: Scan structure, read key files (README, package.json, etc.)
       - URL: Fetch content (if MCP fetch available) or note for manual review
    3. **Assess scope**: Estimate content size and complexity
    
    ### Phase 2: Purpose Extraction
    
    Analyze content to identify:
    
    | Aspect | Questions to Answer |
    |--------|---------------------|
    | **Core Purpose** | What problem does this solve? What is its primary function? |
    | **Target Audience** | Who is this for? What skill level? |
    | **Key Features** | What are the main capabilities? |
    | **Architecture** | How is it structured? What patterns does it use? |
    | **Dependencies** | What does it rely on? What ecosystem? |
    | **Maturity** | How stable/complete is it? Active development? |
    
    **Output format:**
    ```markdown
    ### Purpose Analysis
    
    **Core Purpose:** {one-sentence summary}
    
    **Problem Solved:** {what pain point it addresses}
    
    **Target Audience:** {who would use this}
    
    **Key Features:**
    - {feature 1}
    - {feature 2}
    - {feature 3}
    
    **Architecture/Approach:** {how it works at a high level}
    
    **Maturity:** {early/stable/mature} — {evidence}
    ```
    
    ### Phase 3: Extensive Summary
    
    Create a comprehensive summary covering:
    
    ```markdown
    ### Detailed Summary
    
    #### Overview
    {2-3 paragraphs explaining what this is and how it works}
    
    #### Structure
    {File/folder organization, key components}
    
    #### Technical Details
    - **Language/Runtime:** {languages, versions}
    - **Dependencies:** {key dependencies}
    - **Build System:** {how to build/run}
    - **Testing:** {test approach}
    
    #### Strengths
    - {strength 1}
    - {strength 2}
    
    #### Limitations
    - {limitation 1}
    - {limitation 2}
    
    #### Notable Patterns
    - {interesting pattern or technique}
    - {reusable approach}
    ```
    
    ### Phase 4: Potential Assessment
    
    Evaluate relevance to current project:
    
    1. **Read project context**:
       - Check `project docs` for project scope
       - Check `project docs` for codebase structure
       - Check current project state for active work
    
    2. **Identify alignment**:
       - Technology overlap (same language, framework, etc.)
       - Problem overlap (solves similar issues)
       - Pattern overlap (uses approaches we could adopt)
    
    3. **Generate potential opportunities**:
    
    ```markdown
    ### Potential for Current Project
    
    **Relevance Score:** {low/medium/high}
    
    **Alignment:**
    - ✅ {alignment point 1}
    - ✅ {alignment point 2}
    - ⚠️ {partial alignment}
    - ❌ {misalignment}
    
    **Opportunities:**
    
    1. **{Opportunity Title}**
       - What: {description}
       - Effort: {low/medium/high}
       - Value: {low/medium/high}
       - How: {brief approach}
    
    2. **{Opportunity Title}**
       - What: {description}
       - Effort: {low/medium/high}
       - Value: {low/medium/high}
       - How: {brief approach}
    
    **Risks/Concerns:**
    - {risk 1}
    - {risk 2}
    
    **Recommendation:** {adopt/adapt/inspire/skip}
    ```
    
    ### Phase 5: Issue Creation
    
    Convert opportunities into trackable IDEA issues using  skill:
    
    **For each identified opportunity:**
    
    1. **Create IDEA issue** (minimal mode via ):
       ```markdown
       ## IDEA-{N}@{hash} — {Opportunity Title}
       
       **Status:** `idea`
       **Type:** IDEA
       **Created:** {date}
       **Source:** Potential discovery from {content identifier}
       
       ### Original Opportunity
       {opportunity description from Phase 4}
       
       ### Context
       - **Discovered in:** {source content}
       - **Relevance:** {low/medium/high}
       - **Effort:** {low/medium/high}
       - **Value:** {low/medium/high}
       
       ### Notes
       {any additional context or caveats}
       ```
    
    2. **Present summary to user**:
       ```
       ## Potential Discovery Complete
       
       **Analyzed:** {content identifier}
       **Relevance:** {overall score}
       
       **Issues Created:**
       - IDEA-{N}@{hash}: {title} (effort: X, value: Y)
       - IDEA-{N}@{hash}: {title} (effort: X, value: Y)
       
       These are now in the backlog for later triage.
       Use triage to review and prioritize.
       ```
    
    **No opportunities found:**
    ```
    ## Potential Discovery Complete
    
    **Analyzed:** {content identifier}
    **Relevance:** Low
    
    No actionable opportunities identified for the current project.
    The content may still be useful as reference material.
    ```
    
    ## Output Locations
    
    | Output | Location | When |
    |--------|----------|------|
    | Console | Displayed directly | Always — analysis report shown to user |
    | IDEA issues |  | Opportunities converted to trackable issues |
    
    **IMPORTANT**: This skill does NOT:
    - Create report files in `project docs`
    - Modify project state files
    - Make any code changes
    
    All findings become IDEA issues for later review and triage.
    
    ## Integration with 
    
    This skill uses  to convert opportunities into issues:
    
    1. **Analysis complete** → Opportunities identified
    2. **For each opportunity** → Invoke  (minimal mode)
    3. **Create IDEA issue** — Added to backlog (`priority:backlog`) with:
       - Original opportunity description
       - Source reference (what content it came from)
       - Relevance assessment
    4. **User reviews later** → Triage to promote or drop
    
    ## Integration with Other Skills
    
    | Skill | Integration |
    |-------|-------------|
    |  | Convert opportunities into enriched IDEA issues |
    | `project-sections` | Understand current project structure for alignment |
    | `context-map` | Reference codebase overview |
    |  | Create follow-up issues from discoveries |
    
    ## Customization Options
    
    User can specify intent to focus analysis:
    
    ```
    /discover ./incoming/auth-library/ --intent "improve our authentication"
    /discover https://github.com/user/tool --intent "CLI patterns"
    /discover spec.md --intent "API design inspiration"
    ```
    
    When intent is provided:
    - Purpose analysis weighted toward intent
    - Potential assessment focused on stated goal
    - Opportunities filtered for relevance
    
    ## Completion Criteria
    
    - [ ] Content successfully ingested
    - [ ] Purpose clearly identified and documented
    - [ ] Comprehensive summary created
    - [ ] Potential assessed against project context
    - [ ] Opportunities converted to IDEA issues in backlog
    - [ ] User presented with summary of created issues
    
    ## Anti-patterns (avoid)
    
    - ❌ Shallow analysis (just reading README)
    - ❌ Missing project context (analyzing in isolation)
    - ❌ Vague opportunities ("could be useful")
    - ❌ Ignoring limitations or risks
    - ❌ Over-promising value without evidence
    - ❌ Creating files outside of project docs
    - ❌ Modifying project state files
    - ❌ Making code changes
    
    ## Examples
    
    ### Example 1: Library Analysis
    
    **Input:** `analyze: ./incoming/result-monad/`
    
    **Output:**
    ```markdown
    # Potential Discovery Report
    
    **Content:** ./incoming/result-monad/
    **Analyzed:** 2026-01-17
    **Context:** Python CLI tool
    
    ### Purpose Analysis
    
    **Core Purpose:** Rust-style Result type for Python error handling
    
    **Problem Solved:** Replaces exceptions with explicit error returns
    
    **Key Features:**
    - Result[T, E] generic type
    - Pattern matching support
    - Railway-oriented programming helpers
    
    ### Potential for Current Project
    
    **Relevance Score:** Medium
    
    **Alignment:**
    - ✅ Same language (Python)
    - ✅ We have error handling inconsistencies
    - ⚠️ Would require refactoring existing code
    
    **Opportunities:**
    
    1. **Adopt for new modules**
       - What: Use Result type in kg module
       - Effort: Low
       - Value: Medium
       - How: Add as optional dependency, use in new code
    
    **Recommendation:** Adapt — use pattern for new code, don't refactor existing
    ```
    
    ### Example 2: URL Analysis
    
    **Input:** `analyze: https://github.com/anthropics/anthropic-cookbook --intent "prompt engineering patterns"`
    
    **Output:**
    ```markdown
    # Potential Discovery Report
    
    **Content:** anthropic-cookbook repository
    **Analyzed:** 2026-01-17
    **Context:** Prompt/skill design
    
    ### Purpose Analysis
    
    **Core Purpose:** Collection of Anthropic API usage patterns and examples
    
    ### Potential for Current Project
    
    **Relevance Score:** High
    
    **Opportunities:**
    
    1. **Prompt structure patterns**
       - What: XML-tagged prompt sections
       - Value: High
       - How: Review and adopt in skill prompts
    
    2. **Tool use examples**
       - What: Function calling patterns
       - Value: High  
       - How: Reference for harness tool design
    ```
