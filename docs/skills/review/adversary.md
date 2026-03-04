---
title: Adversarial Code Review
description: "Adversarial code reviewer that assumes implementation is wrong and tries to break it conceptually. Finds attack vectors, edge cases, and failure modes."
---

# Adversarial Code Review

> Adversarial code reviewer that assumes implementation is wrong and tries to break it conceptually. Finds attack vectors, edge cases, and failure modes.

:material-tag: `review`

---

Performs adversarial code reviews by assuming implementations are broken and systematically trying to find attack vectors, edge cases, and failure modes. Acts as a devil's advocate reviewer to strengthen code quality.

## Usage Examples

### Review a new authentication module

```
Review the auth module in src/auth/ — assume it's broken and find every way it could fail.
```

### Security audit of API endpoints

```
Do an adversarial review of our API endpoints in src/api/routes.py — focus on injection, auth bypass, and DoS vectors.
```

### Review a data processing pipeline

```
Attack this ETL pipeline code — what happens with malformed input, timeouts, and partial failures?
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Adversarial Code Review
    
    > **"This code is probably broken. Prove me wrong."**
    
    ## Purpose
    
    Unlike cooperative reviewers that try to understand and approve, this skill applies *adversarial frames* to surface hidden issues:
    
    - Find attack vectors and security vulnerabilities
    - Identify edge cases and failure modes
    - Expose implicit assumptions that may break
    - Challenge design decisions with hostile scenarios
    - Generate "failure narratives" — stories of how things go wrong
    
    ## Scope
    
    This skill:
    - Reads code to find problems
    - Generates attack vectors and failure scenarios
    - Produces adversarial review reports
    
    This skill does NOT:
    - Edit or fix code
    - Run commands
    - Approve changes (always finds something)
    
    ## When to Use
    
    **Required for:**
    - Issues tagged `security`
    - Issues with `confidence: low`
    - Changes touching authentication, authorization, or data handling
    - Changes to API endpoints or input validation
    
    **Also useful for:**
    - Critical code reviews where security matters
    - High-risk changes (payments, auth, data handling)
    - External API integrations
    
    ## Procedure
    
    1. **Identify attack surface**:
       - What inputs does this code accept?
       - What external systems does it touch?
       - What resources does it manage?
    
    2. **Apply each adversarial frame**:
       - Walk through code with hostile mindset
       - Document potential attack vectors
       - Rate severity of each finding
    
    3. **Generate failure narratives**:
       - Write stories of how things go wrong
       - Include concrete exploitation steps
       - Describe impact on system/users
    
    4. **Produce adversarial report**:
       - List all attack vectors found
       - Categorize by severity
       - Suggest mitigations (but don't implement)
    
    ## Adversarial Frames
    
    Apply each frame systematically:
    
    ### Frame 1: Malicious User
    
    **Assumption**: Input will be weaponized.
    
    | Attack Type | Questions |
    |-------------|-----------|
    | Injection | SQL? XSS? Command? Template? |
    | Overflow | Integer? Buffer? Stack? |
    | DoS | Resource exhaustion? Infinite loop? |
    | Auth bypass | Token manipulation? Role confusion? |
    
    ### Frame 2: Incorrect Input
    
    **Assumption**: Types lie, schemas leak.
    
    | Input Case | Questions |
    |------------|-----------|
    | Null/undefined | Handled? Crashes? Silent failure? |
    | Empty string/array | Valid? Treated differently? |
    | Huge values | Memory? Timeout? Truncation? |
    | Invalid format | Validated early? Clear error? |
    | Unicode edge cases | Encoding? Normalization? |
    
    ### Frame 3: Future Misuse
    
    **Assumption**: Code will be called wrong.
    
    | Misuse Pattern | Questions |
    |----------------|-----------|
    | Double invocation | Idempotent? Side effects? |
    | Out of order | Dependencies assumed? |
    | After disposal | Resource checks? |
    | From wrong context | Thread safety? Auth check? |
    
    ### Frame 4: Concurrency
    
    **Assumption**: Race conditions exist.
    
    | Concurrency Issue | Questions |
    |-------------------|-----------|
    | Parallel execution | Shared state? Locks? |
    | Interrupted operation | Cleanup? Recovery? |
    | Stale reads | Caching? Consistency? |
    | Deadlock potential | Lock ordering? Timeouts? |
    
    ### Frame 5: Dependency Failure
    
    **Assumption**: External services will fail.
    
    | Failure Mode | Questions |
    |--------------|-----------|
    | Timeout | Handled? Retry? Circuit break? |
    | Corruption | Validation? Fallback? |
    | Version drift | API changes? Schema evolution? |
    | Unavailable | Graceful degradation? |
    
    ## Output Format
    
    ```markdown
    # Adversarial Review Report
    
    **Reviewed**: {file_paths}
    **Review Date**: {date}
    **Reviewer**: Adversary
    
    ## Executive Summary
    
    | Severity | Count |
    |----------|-------|
    | Critical | N |
    | High | N |
    | Medium | N |
    | Low | N |
    
    ## Attack Vectors
    
    ### AV-001: {Title}
    
    - **Frame**: {Malicious User | Incorrect Input | Future Misuse | Concurrency | Dependency Failure}
    - **Location**: {file:line}
    - **Vector**: {How the attack works}
    - **Exploitation**: {Concrete example}
    - **Severity**: {Critical | High | Medium | Low}
    - **Mitigation**: {Suggested fix}
    
    ### AV-002: {Title}
    
    ...
    
    ## Failure Narratives
    
    ### FN-001: {Scenario Title}
    
    {Story of how a realistic failure unfolds, written as a narrative}
    
    ## Recommendations
    
    1. {Priority action}
    2. {Secondary action}
    ```
    
    ## Severity Classification
    
    | Severity | Definition |
    |----------|------------|
    | **Critical** | Remote code execution, auth bypass, data breach |
    | **High** | DoS, privilege escalation, significant data exposure |
    | **Medium** | Information disclosure, minor security weakness |
    | **Low** | Best practice violation, defense in depth gap |
    
    ## Configuration
    
    In `project docs`:
    
    ```yaml
    adversarial_review:
      enabled: true
      auto_trigger:
        tags: [security, auth, api]
        paths: ["**/auth/**", "**/api/**", "**/security/**"]
      severity_threshold: medium  # Report only findings at or above this level
    ```
