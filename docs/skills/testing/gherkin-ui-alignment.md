---
title: Gherkin UI Alignment Validation
description: "Validate alignment between Gherkin feature files, UI helper functions, and frontend source code. Detect drift, orphaned references, and dead steps."
---

# Gherkin UI Alignment Validation

> Validate alignment between Gherkin feature files, UI helper functions, and frontend source code. Detect drift, orphaned references, and dead steps.

:material-tag: `testing`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/gherkin-ui-alignment/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/gherkin-ui-alignment/SKILL.md){ .md-button .md-button--primary }

---

Validates alignment between Gherkin feature files, UI helper functions, and frontend source code. Detects drift where steps reference UI elements that no longer exist or helpers that don't match the current UI.

## Usage Examples

### Check for UI drift

```
Validate that all Gherkin steps still match the current UI components.
```

### Find orphaned helpers

```
Identify UI helper functions that are no longer referenced by any feature file.
```

### Alignment audit

```
Run a full alignment check between our feature files, step helpers, and React components.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Gherkin UI Alignment — Contract Validation
    
    ## Purpose
    
    Validate alignment between Gherkin feature files, UI helper functions, and frontend source code. Detects drift where steps reference UI elements that no longer exist, helpers that don't match the current UI, or frontend changes that break existing steps.
    
    ## When to Use
    
    - After frontend refactoring — check if Gherkin steps still match
    - During code review — verify UI contract consistency
    - Before release — full alignment audit
    - When adding new UI components — ensure step coverage
    
    ---
    
    ## The Alignment Problem
    
    In a BDD workflow, three layers must stay synchronized:
    
    ```
    Layer 1: Gherkin Feature Files
      "When I fill in Customer name with Acme"
             ↕ (must match)
    Layer 2: Helper Functions / Page Objects
      fillField(page, "Customer name", "Acme")
      → page.getByLabel("Customer name").fill("Acme")
             ↕ (must match)
    Layer 3: Frontend Source Code
      <label for="customer-name">Customer name</label>
      <input id="customer-name" ... />
    ```
    
    If any layer changes without updating the others, tests break silently or give false positives.
    
    ---
    
    ## Alignment Checks
    
    ### Check 1: Step Coverage
    
    **Scan**: All `.feature` files
    **Verify**: Every step has a matching step definition
    **Report**: Unimplemented steps (no matching `@Given`/`@When`/`@Then`)
    
    ```
    ❌ UNIMPLEMENTED: "When I assign the case to {agent}" (customer/assign.feature:12)
       No matching step definition found in any adapter
    ```
    
    ### Check 2: Locator Validity
    
    **Scan**: All helper functions / page objects
    **Verify**: Referenced locators exist in frontend source
    **Report**: Orphaned locators (reference elements that don't exist)
    
    ```
    ❌ ORPHAN LOCATOR: getByLabel("Customer name")
       Used in: pages/CustomerFormPage.ts:15
       Not found in: src/components/CustomerForm.tsx
       Suggestion: Label changed to "Company name" in commit abc1234
    ```
    
    ### Check 3: Vocabulary Consistency
    
    **Scan**: Step definitions across all language adapters
    **Verify**: Same Gherkin step maps to equivalent logic in all adapters
    **Report**: Divergent implementations
    
    ```
    ⚠️ DIVERGENT: "When I create a customer named {string}"
       TypeScript: calls POST /api/customers (API-first)
       Python: calls POST /api/customers (API-first) ✅
       C#: fills form and clicks Save (UI-first) ← INCONSISTENT
    ```
    
    ### Check 4: Dead Steps
    
    **Scan**: All step definitions
    **Verify**: Every step definition is used by at least one feature file
    **Report**: Unused step definitions (dead code)
    
    ```
    ⚠️ DEAD STEP: @When("I archive the customer")
       Defined in: step_definitions/customer_steps.ts:45
       Not referenced by any feature file
    ```
    
    ### Check 5: Element Inventory
    
    **Scan**: Frontend source code (React/Vue/Angular/Blazor components)
    **Extract**: All testable elements (those with labels, test-ids, roles)
    **Compare**: Against elements referenced in step definitions
    
    ```
    📊 ELEMENT INVENTORY: CustomerForm.tsx
       Elements with test-ids: 8
       Elements with labels: 6
       Elements with ARIA roles: 12
       
       Referenced in steps: 5 of 8 test-ids, 4 of 6 labels
       Unreferenced: data-testid="customer-type", data-testid="customer-notes"
    ```
    
    ---
    
    ## Alignment Report Format
    
    ```markdown
    ## UI Alignment Report — {date}
    
    ### Summary
    | Check | Pass | Warn | Fail |
    |-------|------|------|------|
    | Step Coverage | {N} | {N} | {N} |
    | Locator Validity | {N} | {N} | {N} |
    | Vocabulary Consistency | {N} | {N} | {N} |
    | Dead Steps | {N} | {N} | {N} |
    | Element Inventory | {N} | {N} | {N} |
    
    ### Critical Issues (FAIL)
    1. {description}
    
    ### Warnings
    1. {description}
    
    ### Coverage
    - Feature files: {N}
    - Scenarios: {N}
    - Unique steps: {N}
    - Step definitions: {N} ({N} dead)
    - Frontend components scanned: {N}
    - Testable elements found: {N}
    - Elements referenced in steps: {N} ({%})
    ```
    
    ---
    
    ## Manual Alignment Workflow
    
    When using this skill manually (not automated):
    
    1. **Identify change scope**: What changed? (frontend, steps, features)
    2. **Run relevant checks**: Focus on checks affected by the change type:
       - Frontend changed → Check 2 (locators), Check 5 (inventory)
       - Steps changed → Check 1 (coverage), Check 3 (consistency), Check 4 (dead)
       - Features changed → Check 1 (coverage)
    3. **Prioritize fixes**: Critical (broken tests) > Warnings (drift risk) > Info (coverage gaps)
    4. **Update all layers**: Change propagation must touch all three layers
    5. **Verify**: Run affected Gherkin scenarios to confirm alignment
    
    ---
    
    ## CI Integration Guidance
    
    Trigger alignment checks when any of these paths change:
    
    | Path Pattern | Checks to Run |
    |-------------|--------------|
    | `src/components/**` | Locator validity, element inventory |
    | `qa/features/**` | Step coverage |
    | `qa/adapters/**` | Vocabulary consistency, dead steps |
    | All three | Full alignment report |
    
    ---
    
    ## Change Propagation Matrix
    
    When a change is made in one layer, which other layers need updating:
    
    | Changed | Must Check | Likely Needs Update |
    |---------|-----------|-------------------|
    | Frontend label renamed | Locator validity | Page objects, step helpers |
    | Frontend component removed | Element inventory | Feature files, step defs |
    | New feature file added | Step coverage | Step definitions (all adapters) |
    | Step definition changed | Vocabulary consistency | Other adapter step defs |
    | Gherkin step renamed | Step coverage | Step definitions (all adapters) |
    | data-testid added | Element inventory | (opportunity: add step coverage) |
    
    ---
    
    ## Relationship Diagram
    
    ```
    gherkin-review ──────────► Feature file quality
          │
          ▼
    gherkin-architecture ────► Project structure & CI
          │
          ├──► gherkin-playwright ──► Browser automation
          │         │
          │         ▼
          ├──► gherkin-ui-vocabulary ─► Controlled step library
          │         │
          │         ▼
          └──► gherkin-ui-alignment ──► Contract validation (this skill)
    ```
    
    ---
    
    ## Related Skills
    
    - `gherkin-review` — Feature file quality (invoked for step analysis)
    - `gherkin-ui-vocabulary` — Controlled vocabulary (invoked for consistency checks)
    - `gherkin-playwright` — Locator strategy used in Check 2
    - `gherkin-architecture` — Suite structure and CI pipeline integration
