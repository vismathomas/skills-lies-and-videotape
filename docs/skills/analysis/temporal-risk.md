---
title: Temporal Risk Analysis
description: "Analyze how current changes might fail or become liabilities in 3, 6, or 12 months."
---

# Temporal Risk Analysis

> Analyze how current changes might fail or become liabilities in 3, 6, or 12 months.

:material-tag: `analysis`

---

Analyzes how current changes might fail or become liabilities over 3, 6, and 12 month horizons. Identifies time-delayed risks that don't show up in code review.

## Usage Examples

### Analyze time-delayed risks

```
What risks could this architectural decision create in 3, 6, and 12 months?
```

### Dependency risk assessment

```
Analyze the temporal risk of our current dependency choices — what might break over time?
```

### Feature longevity analysis

```
Will this feature implementation still be viable in 12 months given industry trends?
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # temporal-risk
    
    Analyze how current changes might fail or become liabilities in 3, 6, or 12 months.
    
    ## Purpose
    
    Most bugs are time-delayed. Today's working code becomes tomorrow's incident. This skill predicts future failure modes before they manifest.
    
    ## Trigger
    
    - During planning (architectural decisions)
    - During review (implementation choices)
    - Before major releases
    - On demand for risk assessment
    
    ## Time Horizons
    
    | Horizon | Focus Areas |
    |---------|-------------|
    | **3 months** | Direct dependency updates, minor scale, immediate tech debt |
    | **6 months** | API contracts, data migrations, team changes |
    | **12 months** | Major versions, platform changes, business evolution |
    
    ## Risk Categories
    
    | Category | 3-Month Examples | 12-Month Examples |
    |----------|------------------|-------------------|
    | **Dependencies** | Package update breaks | EOL library, API deprecation |
    | **Scale** | 2x load works | 10x load fails |
    | **Team** | Original author leaves | Complete team turnover |
    | **Requirements** | Feature request removed | Product pivot |
    | **Platform** | Language version change | Framework abandoned |
    
    ## Risk Matrix
    
    ```
    Impact × Probability = Risk Score
    
    1-3: Low risk (accept)
    4-7: Medium risk (mitigate)
    8-12: High risk (block or redesign)
    ```
    
    ## Related Skills
    
    -  — includes risk assessment
    -  — checks future-proofing
    -  — reviews past predictions
