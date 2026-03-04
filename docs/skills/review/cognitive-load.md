---
title: Cognitive Load Tracker
description: "Track and budget cognitive complexity introduced by changes. Complexity debt is worse than technical debt."
---

# Cognitive Load Tracker

> Track and budget cognitive complexity introduced by changes. Complexity debt is worse than technical debt.

:material-tag: `review`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/cognitive-load/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/cognitive-load/SKILL.md){ .md-button .md-button--primary }

---

Tracks and budgets cognitive complexity introduced by code changes. Measures complexity across indirection, abstraction depth, state mutations, and naming clarity — because complexity debt is worse than technical debt.

## Usage Examples

### Analyze a file's complexity

```
Measure the cognitive load of src/services/orderProcessor.ts — is it too complex?
```

### Budget a refactoring change

```
Before I refactor auth, give me the current cognitive load budget for src/auth/.
```

### Complexity trend report

```
Show the complexity trend for the last 5 changes to the API module.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # cognitive-load
    
    Track and budget cognitive complexity introduced by changes. Complexity debt is worse than technical debt.
    
    ## Purpose
    
    Every abstraction, indirection, and concept increases the cognitive load for future readers. This skill quantifies complexity and enforces budgets.
    
    ## Trigger
    
    - After implementation (before commit)
    - During review
    - On demand for codebase analysis
    - During planning (to estimate complexity)
    
    ## Complexity Metrics
    
    | Metric | Description | Weight | Example |
    |--------|-------------|--------|---------|
    | **New Concepts** | Novel abstractions, patterns, terminology | 3x | New factory pattern |
    | **Indirection Layers** | Files that exist only to call other files | 2x | Wrapper classes |
    | **Branching Logic** | if/else depth, switch cases | 1.5x | Nested conditionals |
    | **State Management** | Mutable state, side effects | 2x | Global state, caches |
    | **Coupling Points** | Dependencies between modules | 1.5x | Cross-module imports |
    | **Naming Opacity** | Unclear or misleading names | 1x | Generic names like "data", "handler" |
    
    ## Workflow
    
    ### Phase 1: Change Identification
    
    **Identify what changed:**
    
    ```
    added/ → New files, functions, classes
    modified/ → Changed logic, new branches
    dependencies/ → New imports, coupling
    ```
    
    ### Phase 2: Metric Collection
    
    **For each metric, count occurrences:**
    
    #### New Concepts (3x weight)
    ```
    □ New class/interface introduced
    □ New design pattern used
    □ New domain term introduced
    □ New abstraction layer created
    □ New configuration concept
    ```
    
    #### Indirection Layers (2x weight)
    ```
    □ Wrapper class that adds no logic
    □ Facade that just forwards calls
    □ Adapter with 1:1 mapping
    □ Service that only calls repository
    □ Helper that could be inlined
    ```
    
    #### Branching Logic (1.5x weight)
    ```
    □ Each if/else branch
    □ Each switch case
    □ Each ternary operator
    □ Each early return condition
    □ Nested conditionals (count depth)
    ```
    
    #### State Management (2x weight)
    ```
    □ Mutable class field
    □ Global/singleton state
    □ Cache implementation
    □ Side effect in function
    □ Implicit state dependency
    ```
    
    #### Coupling Points (1.5x weight)
    ```
    □ Import from different module
    □ Event/callback registration
    □ Shared mutable resource
    □ Cross-service communication
    □ Database transaction boundary
    ```
    
    #### Naming Opacity (1x weight)
    ```
    □ Single-letter variable (except loops)
    □ Generic name (data, info, helper, utils)
    □ Abbreviation not obvious
    □ Name doesn't match behavior
    □ Misleading name
    ```
    
    ### Phase 3: Score Calculation
    
    ```
    Cognitive Load Score = Σ(metric_count × metric_weight)
    ```
    
    ### Phase 4: Budget Comparison
    
    **Default budgets by confidence:**
    
    | Confidence | Budget | Rationale |
    |------------|--------|-----------|
    | LOW | 5 | Strict — minimize risk |
    | NORMAL | 15 | Standard allowance |
    | HIGH | 25 | Lenient — trusted change |
    
    ### Phase 5: Output
    
    **Produce cognitive load report:**
    
    ```markdown
    ## Cognitive Load Analysis
    
    **Issue**: FEAT-0123 — Add user authentication
    **Confidence**: NORMAL
    **Budget**: 15
    **Actual**: 18 ⚠️ OVER BUDGET (+3)
    
    ### Breakdown
    
    | Metric | Count | Weight | Score |
    |--------|-------|--------|-------|
    | New Concepts | 2 | 3x | 6 |
    | Indirection | 1 | 2x | 2 |
    | Branching | 4 | 1.5x | 6 |
    | State | 2 | 2x | 4 |
    | Coupling | 0 | 1.5x | 0 |
    | Naming | 0 | 1x | 0 |
    | **Total** | | | **18** |
    
    ### Verdict
    
    ⚠️ **OVER BUDGET** — Review required before merge
    
    ### Reduction Recommendations
    
    1. **Remove AuthFactory abstraction** (-6 points)
       - Use direct instantiation instead
       - Factory adds no dynamic behavior
    
    2. **Inline validateToken helper** (-2 points)
       - Called only once
       - Adds indirection without reuse benefit
    ```
    
    ## Constitution Configuration
    
    ```yaml
    # In cognitive_load:
      enabled: true
      budgets:
        low: 5
        normal: 15
        high: 25
    
      enforcement:
        low: block        # cannot merge
        normal: review    # warning + review required
        high: warn        # warning only
    
      weights:
        new_concepts: 3
        indirection: 2
        branching: 1.5
        state: 2
        coupling: 1.5
        naming: 1
    ```
    
    ## Blocking Rules
    
    | Confidence | Over Budget Action |
    |------------|-------------------|
    | LOW | **HARD BLOCK** — cannot merge without reduction |
    | NORMAL | **SOFT BLOCK** — warning + explicit review approval |
    | HIGH | **WARNING** — logged but not blocked |
    
    ## Complexity Delta Report
    
    **Track complexity over time:**
    
    ```markdown
    ## Complexity Delta — Week of 2026-01-27
    
    | Issue | Before | After | Delta | Status |
    |-------|--------|-------|-------|--------|
    | FEAT-0123 | 0 | 18 | +18 | ⚠️ High |
    | BUG-0456 | 12 | 10 | -2 | ✅ Reduced |
    | FEAT-0789 | 25 | 28 | +3 | ⚠️ Growing |
    
    **Net Delta**: +19 complexity points
    **Trend**: 📈 Increasing (needs attention)
    ```
    
    ## Reduction Strategies
    
    ### For New Concepts (3x)
    ```
    - Use existing patterns instead of inventing new ones
    - Adopt well-known library patterns
    - Reduce domain terminology
    - Merge similar concepts
    ```
    
    ### For Indirection (2x)
    ```
    - Inline wrappers with no added value
    - Remove pass-through layers
    - Consider direct calls where abstraction unused
    - Delete "just in case" abstractions
    ```
    
    ### For Branching (1.5x)
    ```
    - Extract complex conditions into named predicates
    - Use polymorphism over switch statements
    - Apply guard clauses for early returns
    - Flatten nested conditionals
    ```
    
    ### For State (2x)
    ```
    - Prefer immutable data
    - Make side effects explicit
    - Reduce mutable class fields
    - Use dependency injection over globals
    ```
    
    ### For Coupling (1.5x)
    ```
    - Introduce interfaces at boundaries
    - Use events for loose coupling
    - Batch cross-module operations
    - Reduce circular dependencies
    ```
    
    ### For Naming (1x)
    ```
    - Use descriptive names that match behavior
    - Avoid abbreviations
    - Name functions for what they return
    - Name booleans as questions (isValid, hasPermission)
    ```
    
    ## Anti-Patterns (What NOT to Do)
    
    - ❌ Block all changes to reduce score
    - ❌ Optimize for score at expense of readability
    - ❌ Apply same budget to all issue types
    - ❌ Ignore context when scoring
    - ❌ Treat score as absolute truth
    
    ## Invocation
    
    ```
    /cognitive-load              # analyze current changes
    /cognitive-load scope=file path=src/auth.ts
    /cognitive-load report=delta # show complexity trend
    /cognitive-load budget=10    # set custom budget
    ```
    
    ## Output Location
    
    - Inline in chat (default)
    - `project docs` (when persisting)
    - Added to issue log when over budget
    
    ## Related Skills
    
    -  — includes complexity assessment
    - `improvement-discovery` — finds simplification opportunities
