---
title: Gherkin Feature File Review
description: "Review and lint Gherkin feature files for quality, consistency, and BDD best practices. Multi-language (EN/NO). Catches anti-patterns before CI."
---

# Gherkin Feature File Review

> Review and lint Gherkin feature files for quality, consistency, and BDD best practices. Multi-language (EN/NO). Catches anti-patterns before CI.

:material-tag: `testing`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/gherkin-review/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/gherkin-review/SKILL.md){ .md-button .md-button--primary }

---

Reviews and lints Gherkin feature files for quality, consistency, and BDD best practices. Catches anti-patterns before CI. Supports English and Norwegian (bokmål) localization.

## Usage Examples

### Review feature files

```
Review all .feature files in qa/features/ for BDD best practices.
```

### Check for anti-patterns

```
Lint this feature file for common Gherkin anti-patterns like incidental details and conjunction steps.
```

### Review Norwegian feature file

```
Review this Norwegian Gherkin feature file for consistency with our conventions.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Gherkin Review — Feature File Linting & Quality
    
    ## Purpose
    
    Review and lint Gherkin feature files for quality, consistency, and adherence to BDD best practices. Catches common anti-patterns before they reach CI. Works with English and Norwegian (bokmål) localization.
    
    ## When to Use
    
    - Before PR submission — review `.feature` files for quality
    - During code review — verify Gherkin follows team conventions
    - When onboarding — teach BDD writing patterns
    - When converting imperative steps to declarative style
    
    ## Procedure
    
    1. Identify all `.feature` files in scope (changed files, directory, or full suite)
    2. For each file, run through the **Anti-Pattern Detection** checklist
    3. Check **Localization** rules
    4. Check **Linting Rules** (machine-checkable)
    5. Produce a **Structured Review Report**
    
    ---
    
    ## Anti-Pattern Detection
    
    | Anti-Pattern | Problem | Fix |
    |-------------|---------|-----|
    | Implementation details in steps | Brittle, couples to UI | Use declarative business language |
    | Long scenarios (>10 steps) | Hard to understand | Split into focused scenarios |
    | Missing `Background` for shared setup | Repeated Given steps | Extract to Background |
    | Incidental details | Noise in scenarios | Remove irrelevant data |
    | Conjunctive chains (And/And/And) | Hidden complexity | Consolidate or split |
    | UI-coupled language ("click", "fill", "type") | Fragile, not behavior-focused | Use business intent language |
    | No `# language:` header | Ambiguous localization | Always declare language |
    | Missing tags | No traceability | Add `@feature`, `@priority`, `@sprint` tags |
    | Steps calling other steps | Hidden dependencies | Use helper functions instead |
    | Massive Background blocks | Slow setup, unclear relevance | Extract to hooks or factories |
    
    ---
    
    ## Bad vs Good Examples
    
    ### English — Imperative (BAD)
    
    ```gherkin
    Scenario: Create customer
      Given I navigate to "/customers/new"
      And I fill in the field "name" with "Acme Corp"
      And I fill in the field "org-number" with "123456789"
      And I click the "Save" button
      Then I should see "Customer created" on the page
      And the URL should contain "/customers/"
    ```
    
    ### English — Declarative (GOOD)
    
    ```gherkin
    Scenario: Create a new customer with valid data
      Given I am logged in as an administrator
      When I create a customer named "Acme Corp" with org number "123456789"
      Then the customer "Acme Corp" should exist in the system
      And I should see a confirmation message
    ```
    
    ### Norwegian — Imperative (BAD)
    
    ```gherkin
    # language: no
    Egenskap: Opprett kunde
      Scenario: Lag ny kunde
        Gitt at jeg går til "/kunder/ny"
        Og jeg fyller inn feltet "navn" med "Acme Corp"
        Og jeg klikker på "Lagre"-knappen
        Så skal jeg se "Kunde opprettet" på siden
    ```
    
    ### Norwegian — Declarative (GOOD)
    
    ```gherkin
    # language: no
    Egenskap: Kundebehandling
    
      Bakgrunn:
        Gitt at jeg er innlogget som administrator
    
      Scenario: Opprette ny kunde med gyldig data
        Når jeg oppretter en kunde med navn "Acme Corp" og organisasjonsnummer "123456789"
        Så skal kunden "Acme Corp" eksistere i systemet
        Og jeg skal se en bekreftelsesmelding
    ```
    
    ---
    
    ## Rule/Example Structure (Gherkin 6+)
    
    Encourage `Rule` blocks for grouping related scenarios:
    
    ```gherkin
    Feature: Customer management
    
      Rule: Administrators can create customers
        Example: Create customer with valid data
          Given I am logged in as an administrator
          When I create a customer named "Acme Corp"
          Then the customer should exist
    
        Example: Cannot create duplicate customers
          Given a customer named "Acme Corp" already exists
          When I try to create another customer named "Acme Corp"
          Then I should see a duplicate error
    
      Rule: Regular users cannot create customers
        Example: Access denied for regular user
          Given I am logged in as a regular user
          When I try to create a customer
          Then I should see an access denied message
    ```
    
    ---
    
    ## Scenario Outline Guidance
    
    ```gherkin
    Scenario Outline: Validate customer fields
      Given I am creating a new customer
      When I submit with <field> set to "<value>"
      Then I should see the error "<error>"
    
      Examples:
        | field      | value | error                    |
        | name       |       | Name is required         |
        | org_number | abc   | Must be numeric          |
        | org_number | 12345 | Must be 9 digits         |
    ```
    
    ---
    
    ## Tag Strategy
    
    | Tag Category | Examples | Purpose |
    |-------------|----------|---------|
    | Feature area | `@customer`, `@order`, `@auth` | Filtering by domain |
    | Priority | `@priority-high`, `@priority-low` | CI tier selection |
    | Test type | `@smoke`, `@regression`, `@e2e` | Pipeline stage |
    | Status | `@wip`, `@skip`, `@flaky` | Execution control |
    | Sprint/iteration | `@sprint-42`, `@mvp` | Traceability |
    
    ---
    
    ## Localization Checklist
    
    - [ ] `# language:` header present on first line
    - [ ] Keywords match declared language (no mixing)
    - [ ] Step text is natural in the declared language
    - [ ] No English keywords in non-English files (common mistake)
    - [ ] `ReqnRoll.json` or `cucumber.yml` configured for language
    
    ---
    
    ## Linting Rules (Machine-Checkable)
    
    | Rule | Severity | Description |
    |------|----------|-------------|
    | `no-missing-language` | error | `# language:` header required |
    | `no-empty-scenario` | error | Scenarios must have steps |
    | `no-duplicate-scenario-name` | error | Names must be unique within feature |
    | `max-steps-per-scenario` | warning | >10 steps suggests splitting |
    | `no-background-with-single-scenario` | info | Background unnecessary with 1 scenario |
    | `no-unnamed-feature` | error | Feature must have a name |
    | `no-imperative-steps` | warning | Detect "click", "fill", "navigate" in steps |
    | `consistent-then-language` | warning | Then steps should assert, not act |
    | `tag-format` | info | Tags should follow convention |
    
    ---
    
    ## Review Report Format
    
    Produce output in this structure:
    
    ```markdown
    ## Gherkin Review: {filename}
    
    ### Critical Issues
    - Line {N}: {description} — {fix suggestion}
    
    ### Warnings
    - {description}
    
    ### Suggestions
    - {description}
    
    ### Summary: {X} critical, {Y} warnings, {Z} suggestions
    ```
    
    ### Example Output
    
    ```markdown
    ## Gherkin Review: features/customer.feature
    
    ### Critical Issues
    - Line 12: Imperative step "I click the Save button" — use declarative business language
    - Line 3: Missing `# language:` header
    
    ### Warnings
    - Scenario "Create customer" has 14 steps — consider splitting
    - Lines 8-11: Conjunctive chain (4 And steps) — consolidate
    
    ### Suggestions
    - Consider adding `Rule` blocks to group related scenarios
    - Add `@smoke` tag to the critical path scenario
    
    ### Summary: 2 critical, 2 warnings, 2 suggestions
    ```
    
    ---
    
    ## Related Skills
    
    - `gherkin-step-generator` — ReqnRoll/C# step generation (narrower scope)
    - `gherkin-architecture` — Suite structure and CI design
    - `gherkin-ui-vocabulary` — Controlled step vocabulary
