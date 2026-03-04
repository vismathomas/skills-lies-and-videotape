---
title: Systematic Debugging
description: "Systematic debugging approaches for isolating and fixing software defects. Use when something isn't working and the cause is unclear."
---

# Systematic Debugging

> Systematic debugging approaches for isolating and fixing software defects. Use when something isn't working and the cause is unclear.

:material-tag: `utility`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/debugging/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/debugging/SKILL.md){ .md-button .md-button--primary }

---

Provides systematic debugging approaches for isolating and fixing software defects. Use when something isn't working and the cause is unclear — follows structured investigation rather than guesswork.

## Usage Examples

### Debug a failing test

```
This test in tests/test_auth.py is failing intermittently — help me debug it systematically.
```

### Isolate a production error

```
Users are seeing 500 errors on the /api/orders endpoint — help me trace the root cause.
```

### Fix a regression

```
Something broke after the last merge — the login flow redirects to a blank page.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Skill: debugging
    
    > Systematic debugging approaches for isolating and fixing software defects
    
    ---
    
    ## Purpose
    
    Systematic problem isolation, root cause analysis, and defect resolution. Use when something isn't working and the cause is unclear.
    
    ---
    
    ## Core Principles
    
    ### 1. Understand Before Acting
    
    - **Reproduce the issue**: Can you consistently trigger the problem?
    - **Define expected vs actual**: What should happen vs what is happening?
    - **Gather context**: When does this occur? Under what conditions?
    - **Recent changes**: What changed before this appeared?
    
    ### 2. Isolate the Problem
    
    - **Binary search**: Comment out half the code, test, repeat
    - **Minimize reproduction**: Create minimal test case
    - **Control variables**: Change one thing at a time
    - **Eliminate noise**: Remove unrelated factors
    
    ### 3. Form Hypotheses
    
    - **State your assumption**: "I believe X is causing Y because..."
    - **Make predictions**: "If my hypothesis is true, then Z should happen"
    - **Test predictions**: Verify or refute each hypothesis
    - **Iterate**: Refine hypothesis based on evidence
    
    ### 4. Fix and Verify
    
    - **Address root cause**: Not just symptoms
    - **Minimize changes**: Smallest fix that resolves the issue
    - **Add tests**: Prevent regression
    - **Verify fix**: Test the specific scenario and related scenarios
    
    ---
    
    ## Systematic Debugging Process
    
    > **Credit**: This 4-phase process is adapted from obra/superpowers by Jesse Vincent (MIT License). See `project docs` Section 4 and obra/superpowers `skills/systematic-debugging/SKILL.md`.
    
    ### Phase 1: Root Cause Investigation
    
    0. **Check existing lessons on this issue** (FIRST)
       - Run  to see if prior debugging attempts left clues
       - Prior lessons often contain root cause hints or dead-end paths to avoid
       - Also check lessons on related issues in the same epic
    
    1. **Read error messages carefully** (don't skip or skim)
       - What does the error actually say?
       - Stack trace analysis - where did it fail?
       - Error codes and their meanings
    
    2. **Reproduce the issue consistently**
       - Can you trigger the problem reliably?
       - Document exact reproduction steps
       - Identify minimal reproduction case
    
    3. **Check recent changes**
       - `git diff` to see what changed
       - When did this start happening?
       - Correlate with recent commits
    
    4. **Gather evidence at component boundaries**
       - Input vs output at each boundary
       - HTTP request/response logs
       - Database queries and results
       - API contract violations
    
    5. **Trace data flow backward**
       - Start from the error point
       - Work backwards through the call stack
       - Identify where data diverges from expected
    
    ### Phase 2: Pattern Analysis
    
    1. **Find working examples in codebase**
       - Where does similar code work?
       - What's different about the failing case?
       - Copy working patterns
    
    2. **Compare against references**
       - Documentation examples
       - Library/API reference
       - Stack Overflow/issue trackers
    
    3. **Identify differences**
       - Configuration differences
       - Data type mismatches
       - Missing initialization
       - API version differences
    
    4. **Understand dependencies**
       - What does this code depend on?
       - Are dependencies satisfied?
       - Version compatibility issues
    
    ### Phase 3: Hypothesis and Testing
    
    1. **Form single, specific hypothesis**
       - "I believe X is causing Y because Z"
       - Make it falsifiable - what would prove it wrong?
       - Avoid multiple explanations - pick one
    
    2. **Test with minimal change**
       - Change ONE thing at a time
       - Verify hypothesis with logging or instrumentation
       - Don't implement full fix yet
    
    3. **Verify before continuing**
       - Did the test confirm or refute your hypothesis?
       - If refuted, form new hypothesis
       - If confirmed, proceed to Phase 4
    
    ### Phase 4: Implementation
    
    1. **Create failing test that reproduces bug** (MANDATORY)
       - Test must fail for the exact bug being fixed
       - Run it and confirm it fails
       - This proves you're testing the right thing
    
    2. **Implement single fix for root cause**
       - Address the root cause, not symptoms
       - Minimal change that fixes the bug
       - Don't add unnecessary complexity
    
    3. **Verify fix works**
       - Failing test now passes
       - No regressions introduced
       - Run full test suite if available
    
    4. **If 3+ fixes fail → question architecture**
       - If you've tried 3+ fixes and none work:
       - The architecture or design may be the problem
       - Stop and ask: "Should we reconsider the approach?"
    
    ---
    
    ## Debugging by Symptom
    
    ### "It Works on My Machine"
    
    | Check | Action |
    |-------|--------|
    | Environment differences | Python versions, OS, dependencies |
    | Uncommitted config | Local settings, .env files |
    | Race conditions | Timing-dependent issues |
    | Data differences | Test with production data subset |
    | Resource constraints | Production may have different limits |
    
    ### Intermittent Failures
    
    | Check | Action |
    |-------|--------|
    | Shared state | Global variables, singletons, caches |
    | Timing | Race conditions, timeouts, async issues |
    | Randomness | Random seeds, shuffling, sampling |
    | Resource cleanup | Are resources properly released? |
    | External dependencies | Network calls, third-party services |
    
    ### Performance Degradation
    
    | Check | Action |
    |-------|--------|
    | Profile first | Measure before optimizing |
    | O(n²) | Nested loops, repeated work |
    | I/O | Database queries, file reads, network |
    | Memory | Leaks, large objects, excessive allocations |
    | Caching | Repeated expensive operations |
    
    ### Memory Leaks
    
    | Check | Action |
    |-------|--------|
    | Profile memory | Track allocations over time |
    | Circular references | GC can't collect cycles |
    | Event listeners | Detached handlers keeping objects alive |
    | Caches | Growing without bounds |
    | Static collections | Accumulating entries |
    
    ### Deadlocks
    
    | Check | Action |
    |-------|--------|
    | Lock order | Identify held locks, acquisition order |
    | Cycles | A waits for B, B waits for A |
    | Timeouts | Are operations waiting indefinitely? |
    | Hold-and-wait | Holding one lock while waiting for another |
    
    ---
    
    ## Tool-Specific Guidance
    
    ### Print/Log Statements
    
    ```python
    # Strategic placement with unique markers
    print(f"[DEBUG-001] user_id={user_id}, state={state}")
    
    # Include enough context
    logger.debug(f"Processing item {i}/{total}: {item.id}")
    
    # Remove after debugging!
    ```
    
    ### Debugger
    
    - Set breakpoints at suspicious locations, not everywhere
    - Watch expressions for specific variables
    - Check call stack to understand how you got here
    - Step carefully through suspicious code
    
    ### Tests for Debugging
    
    - Write failing test that captures bug reproduction
    - Use `git bisect` to find when bug was introduced
    - Mock external dependencies to isolate
    - Property-based testing finds edge cases
    
    ---
    
    ## Anti-Patterns to Avoid
    
    | Anti-Pattern | Problem | Better Approach |
    |--------------|---------|-----------------|
    | **Shotgun debugging** | Random changes hoping something works | Form hypothesis, test, refine |
    | **Symptom treatment** | Adding error handling to hide failures | Fix underlying cause |
    | **Assuming** | "This variable can't be null" | Add assertion to verify |
    | **Overcomplicating** | Complex debugging infrastructure | Start simple, add tools as needed |
    | **Ignoring evidence** | Dismissing data that doesn't fit | Revise hypothesis to explain all |
    
    ---
    
    ## Debugging Checklist
    
    Before declaring "debugged":
    
    - [ ] Root cause identified, not just symptom treated
    - [ ] Failing test created and confirmed to fail (MANDATORY)
    - [ ] Single fix implemented for root cause
    - [ ] Fix verified - failing test now passes
    - [ ] No regressions (run full test suite if available)
    - [ ] Related code checked for same issue
    - [ ] Documentation updated if needed
    - [ ] Fix verified in realistic scenario
    
    ## Fix Attempts Tracking (MANDATORY)
    
    Track fix attempts to detect architectural issues:
    
    ```
    ## Debug Session: [Issue Description]
    
    **Fix Attempt 1**: [Date]
    - Hypothesis: [Your theory]
    - Fix: [What you tried]
    - Result: [Pass/Fail]
    
    **Fix Attempt 2**: [Date]
    - Hypothesis: [Refined theory]
    - Fix: [What you tried]
    - Result: [Pass/Fail]
    
    **Fix Attempt 3**: [Date]
    - Hypothesis: [Further refinement]
    - Fix: [What you tried]
    - Result: [Pass/Fail]
    
    ⚠️ 3+ FIX ATTEMPTS FAILED
    
    Consider:
    - Is the architecture or design the problem?
    - Should we question assumptions?
    - Stop and ask: "Should we reconsider the approach?"
    ```
    
    **Rule**: If 3+ fix attempts fail, STOP and question architecture before continuing.
    
    ---
    
    ## When to Escalate
    
    Consider asking for help if:
    
    - After 2 hours without progress
    - Issue is in unfamiliar technology stack
    - Problem involves complex distributed systems
    - Security implications
    - Production outage
    - Going in circles (revisiting same hypotheses)
    
    ---
    
    ## Recording Debug Sessions
    
    Track in `project docs`:
    
    ```markdown
    ## Debugging: [Issue Description]
    
    **Symptom**: [What's happening]
    **Expected**: [What should happen]
    **Reproduction**: [Steps to trigger]
    
    ### Hypotheses
    1. [Hypothesis] → [TESTED: result]
    2. [Hypothesis] → [PENDING]
    
    ### Evidence Gathered
    - Log at X showed Y
    - Variable Z had value W
    
    ### Resolution
    [Root cause and fix applied]
    ```
