---
title: Junior-Level Explanations
description: "Translate complex plans or implementations into junior-level explanations. If you can't explain it simply, you don't understand it."
---

# Junior-Level Explanations

> Translate complex plans or implementations into junior-level explanations. If you can't explain it simply, you don't understand it.

:material-tag: `planning`

---

Translates complex plans or implementations into junior-level explanations. If you can't explain it simply, you don't understand it. Useful for documentation, onboarding, and validating understanding.

## Usage Examples

### Explain a complex plan

```
Explain this implementation plan for the event sourcing migration as if I'm a junior developer.
```

### Simplify architecture docs

```
Translate this architecture document into something a junior developer would understand.
```

### Explain a code change

```
Explain what this PR does and why, in simple terms for someone new to the codebase.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # junior-explain
    
    Translate complex plans or implementations into junior-level explanations. If you can't explain it simply, you don't understand it.
    
    ## Purpose
    
    Complex explanations often hide unclear thinking, unnecessary complexity, or missing understanding. This skill forces simplification as a correctness check.
    
    ## Trigger
    
    - During review (optional)
    - Before documentation
    - For complex decisions
    - On demand for any artifact
    
    ## Explanation Levels
    
    | Level | Audience | Vocabulary | Max Concepts | Use When |
    |-------|----------|------------|--------------|----------|
    | **Intern** | First day on job | No jargon, concrete examples | 3 | Onboarding docs |
    | **Junior** | 1-2 years experience | Minimal jargon | 5 | Standard docs |
    | **Mid-level** | 3-5 years experience | Some jargon | 8 | Design docs |
    | **Senior** | 5+ years experience | Full jargon | Unlimited | Spec docs |
    
    ## Simplicity Test
    
    If you cannot explain it at the **Junior** level:
    1. Your understanding is incomplete
    2. The design is too complex
    3. Simplicity is needed
    
    ## Related Skills
    
    -  — documentation generation
    -  — includes simplicity check
    - `improvement-discovery` — finds simplification opportunities
