---
title: Shadow Plan Generator
description: "Generate an alternative plan that deliberately disagrees with the primary plan to expose blind spots"
---

# Shadow Plan Generator

> Generate an alternative plan that deliberately disagrees with the primary plan to expose blind spots

:material-tag: `planning`

---

Generates an alternative plan that deliberately disagrees with the primary plan to expose blind spots. Forces consideration of different architectures, tradeoffs, and approaches.

## Usage Examples

### Generate an alternative plan

```
Here's our plan for the new auth system — create a shadow plan that takes a completely different approach.
```

### Challenge assumptions

```
This plan assumes a monolithic architecture — generate a shadow plan that challenges that assumption.
```

### Expose blind spots

```
Create an alternative plan for the migration — what are we not seeing?
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # shadow-plan
    
    Generate an **alternative plan** that deliberately disagrees with the primary plan to expose blind spots and hidden assumptions.
    
    ## Purpose
    
    Single plans hide blind spots. The first approach isn't always the best, but we often commit to it without exploring alternatives. This skill forces consideration of competing approaches.
    
    ## When to Use
    
    - **Recommended** for `confidence: low` issues
    - **Required** for architectural decisions
    - **Optional** for standard feature work
    - **Useful** when primary plan feels "obvious"
    
    ## CRITICAL: No Assumptions
    
    > **NEVER assume. NEVER guess. ALWAYS ask.**
    
    **Before generating shadow plan, confirm:**
    
    | If unclear about... | ASK |
    |---------------------|-----|
    | Primary plan | "What's the current plan I should challenge?" |
    | Constraints | "Are there constraints that limit alternatives?" |
    | Trade-off priorities | "What matters most: speed, maintainability, or safety?" |
    
    ## Core Principle
    
    > **The shadow plan must be viable, not a strawman.**
    
    A shadow plan that's obviously worse serves no purpose. The goal is to surface legitimate alternatives that might actually be better in some dimensions.
    
    ## Shadow Plan Requirements
    
    The shadow plan MUST:
    - ✅ Use a different architectural approach
    - ✅ Prioritize different trade-offs
    - ✅ Challenge at least one assumption of the primary plan
    - ✅ Be implementable (not theoretical)
    - ✅ Have clear benefits in at least one dimension
    
    The shadow plan MUST NOT:
    - ❌ Be an obvious strawman
    - ❌ Violate hard constraints (constitution limits)
    - ❌ Require unavailable resources
    - ❌ Simply be "do less"
    
    ## Workflow Overview
    
    ```mermaid
    flowchart LR
        A[1. Understand Primary] --> B[2. Identify Assumptions]
        B --> C[3. Find Divergence Axis]
        C --> D[4. Generate Shadow]
        D --> E[5. Compare & Recommend]
    ```
    
    ## Phase 1: Understand Primary Plan
    
    **Extract key elements from the primary plan:**
    
    ```markdown
    ### Primary Plan Analysis
    
    **Approach**: {high-level strategy}
    **Key Decisions**:
    1. {decision_1}: {rationale}
    2. {decision_2}: {rationale}
    3. {decision_3}: {rationale}
    
    **Trade-offs Accepted**:
    - {trade_off_1}
    - {trade_off_2}
    
    **Assumptions**:
    - {assumption_1}
    - {assumption_2}
    
    **Confidence**: {high | normal | low}
    ```
    
    ## Phase 2: Identify Hidden Assumptions
    
    **Every plan has implicit assumptions. Surface them:**
    
    | Assumption Type | Examples |
    |-----------------|----------|
    | **Technical** | "This library is stable", "API won't change" |
    | **Resource** | "Team knows this technology", "Time is flexible" |
    | **Scope** | "Requirements are complete", "No edge cases" |
    | **Risk** | "Failure is recoverable", "Performance is acceptable" |
    
    **Questions to surface assumptions:**
    
    1. What would make this plan fail?
    2. What's the plan betting on?
    3. What's not explicitly stated but required?
    4. What changes would invalidate this approach?
    
    ## Phase 3: Find Divergence Axis
    
    **Choose how the shadow plan will differ:**
    
    ### Divergence Axes
    
    | Axis | Primary Direction | Shadow Direction |
    |------|-------------------|------------------|
    | **Abstraction** | Build framework/lib | Use primitives/stdlib |
    | **Dependency** | Add external library | Implement in-house |
    | **Pattern** | OOP with classes | Functional/procedural |
    | **Scope** | Full feature complete | MVP / iterative |
    | **Risk Profile** | Conservative / proven | Experimental / novel |
    | **Performance** | Optimize early | Optimize later |
    | **Coupling** | Centralized / monolith | Distributed / modular |
    | **State** | Mutable / stateful | Immutable / stateless |
    
    **Selection criteria:**
    1. Which axis challenges the most critical assumption?
    2. Which provides the most distinct trade-offs?
    3. Which is actually viable given constraints?
    
    ## Phase 4: Generate Shadow Plan
    
    **Create a complete alternative approach:**
    
    ```markdown
    ### Shadow Plan
    
    **Divergence Axis**: {axis_name}
    **Core Difference**: {one-sentence summary}
    
    **Approach**: {high-level strategy}
    
    **Implementation Outline**:
    1. {step_1}
    2. {step_2}
    3. {step_3}
    
    **Trade-offs Accepted**:
    - ✅ {benefit_1}
    - ✅ {benefit_2}
    - ❌ {cost_1}
    - ❌ {cost_2}
    
    **Assumptions**:
    - {assumption_1}
    - {assumption_2}
    
    **Confidence**: {high | normal | low}
    ```
    
    ## Phase 5: Compare & Recommend
    
    **Structured comparison of both approaches:**
    
    ### Comparison Template
    
    ```markdown
    ## Shadow Plan Analysis
    
    ### Executive Summary
    
    | Plan | Approach | Confidence |
    |------|----------|------------|
    | Primary | {summary} | {level} |
    | Shadow | {summary} | {level} |
    
    ### Trade-off Comparison
    
    | Factor | Primary | Shadow | Winner |
    |--------|---------|--------|--------|
    | Setup Time | {estimate} | {estimate} | {which} |
    | Complexity | {rating} | {rating} | {which} |
    | Maintainability | {rating} | {rating} | {which} |
    | Risk | {rating} | {rating} | {which} |
    | Flexibility | {rating} | {rating} | {which} |
    | Performance | {rating} | {rating} | {which} |
    
    ### Scenario Analysis
    
    **Choose Primary if:**
    - {condition_1}
    - {condition_2}
    
    **Choose Shadow if:**
    - {condition_1}
    - {condition_2}
    
    ### Recommendation
    
    **Selected**: {Primary | Shadow | Hybrid}
    **Rationale**: {explanation}
    
    ### Hybrid Option (if applicable)
    
    {Description of how elements from both could be combined}
    ```
    
    ## Output Formats
    
    ### Quick Comparison (for simple decisions)
    
    ```markdown
    ## Shadow Plan: {title}
    
    **Primary**: {one-line summary}
    **Shadow**: {one-line summary}
    
    | Factor | Primary | Shadow |
    |--------|---------|--------|
    | {key_factor_1} | {value} | {value} |
    | {key_factor_2} | {value} | {value} |
    
    **Recommendation**: {Primary | Shadow} because {reason}
    ```
    
    ### Full Analysis (for architectural decisions)
    
    Use the complete comparison template from Phase 5.
    
    ## Examples
    
    ### Example 1: State Management
    
    **Primary Plan**: Add Redux for global state management
    - Uses proven library with large ecosystem
    - Standard patterns for async, testing, devtools
    - Team will need to learn Redux patterns
    
    **Shadow Plan (Divergence: Dependency)**:
    - Use React Context + useReducer
    - Zero additional dependencies
    - Simpler mental model
    - Less ecosystem support
    
    | Factor | Redux | Context |
    |--------|-------|---------|
    | Setup | 2h | 30m |
    | Learning | High | Low |
    | Ecosystem | Excellent | Limited |
    | Scale | 100+ components | ~50 components |
    
    **Recommendation**: Choose Redux if scaling beyond 50 components likely. Choose Context for smaller apps or time constraints.
    
    ### Example 2: API Design
    
    **Primary Plan**: REST with resource-based endpoints
    - Standard, well-understood
    - Easy caching with HTTP semantics
    - Multiple round trips for complex queries
    
    **Shadow Plan (Divergence: Pattern)**:
    - GraphQL single endpoint
    - Client-driven queries
    - Single request for complex data
    - More setup, custom caching
    
    | Factor | REST | GraphQL |
    |--------|------|---------|
    | Setup | 2h | 6h |
    | Flexibility | Fixed | High |
    | Caching | Built-in | Manual |
    | Mobile Efficiency | Low | High |
    
    **Recommendation**: Choose GraphQL if mobile clients have bandwidth constraints. Choose REST if simplicity and caching matter more.
    
    ## Integration with Other Skills
    
    | Skill | Integration |
    |-------|-------------|
    |  | Shadow plan generated during planning cycles |
    |  | Use shadow comparison to validate primary choice |
    |  | Record which plan was chosen and outcome |
    
    ## Configuration
    
    In `project docs`:
    
    ```yaml
    shadow_plan:
      enabled: true
      auto_trigger:
        confidence: [low]
        tags: [architecture, design, infrastructure]
      require_for_architectural: true
      min_divergence_axes: 1
    ```
    
    ## Troubleshooting
    
    ### "Shadow plan looks better than primary"
    
    **This is fine.** The skill is working as intended. Consider:
    1. Switching to shadow plan
    2. Creating a hybrid
    3. Re-evaluating original assumptions
    
    ### "Can't find meaningful divergence"
    
    The primary plan may genuinely be the only viable approach. Document:
    1. Why alternatives don't work
    2. Which divergence axes were considered
    3. Why primary wins on all
    
    ### "Both plans seem equally good"
    
    This is valuable information. It means:
    1. Decision has low stakes (either works)
    2. Need more constraints to differentiate
    3. Consider other factors (team preference, learning value)
