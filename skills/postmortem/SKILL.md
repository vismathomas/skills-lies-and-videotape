---
name: postmortem
title: Postmortem Analysis
description: "Enforces structured postmortem ritual when failures occur. Produces blameless analysis, identifies root causes, and writes durable learnings to memory."
category: analysis
---
# Postmortem Analysis

> **"Recovery without learning is failure repetition."**

This skill enforces a structured postmortem ritual when things go wrong, ensuring failures become learning opportunities.

## Purpose

- Capture what went wrong with full timeline
- Identify root causes and contributing factors
- Recognize what went right (don't lose working patterns)
- Generate actionable improvements
- Write durable learnings to `project docs`

## Trigger Conditions

**Automatic triggers:**
- Validation fails 2+ times consecutively
- Rollback is performed
- Recovery skill invoked
- Build/lint/test baseline regresses

**Manual trigger:**
- User requests postmortem
- Agent detects significant rework

## Blamelessness Rules (MANDATORY)

This skill MUST NOT:

| ❌ Forbidden | ✅ Instead |
|-------------|-----------|
| "User gave unclear requirements" | "Requirements interpretation proved incorrect" |
| "Task was too complex" | "Complexity exceeded initial estimate" |
| "Bad luck" | "Unaccounted-for dependency" |
| Skip systemic section | Always include systemic improvements |

## Postmortem Procedure

### Phase 1: Incident Detection

Gather all available evidence:

```
1. Read project state
2. Read relevant issue
3. Scan terminal history for error patterns
4. Check git log for recent commits/rollbacks
5. Review baseline comparison results
```

### Phase 2: Timeline Reconstruction

Build a chronological timeline:

```markdown
### Timeline

| Time | Event | Detail |
|------|-------|--------|
| T+0 | Implementation started | Issue FEAT-0123 |
| T+30m | First test failure | TypeError in api/client.py |
| T+35m | Fix attempted | Added type cast |
| T+40m | Second failure | RuntimeError: None response |
| T+45m | Rollback triggered | git reset --hard |
| T+60m | Postmortem initiated | This document |
```

### Phase 3: Root Cause Analysis

**The 5 Whys Technique:**

```
Problem: Tests failed twice

Why? → Type error on API response
Why? → Response shape assumed, not validated
Why? → No type definitions for external API
Why? → Initial plan didn't include contract verification
Why? → Default confidence too high for external integrations
```

**Root Cause Classification:**

| Category | Examples |
|----------|----------|
| **Requirements** | Incomplete, ambiguous, changed |
| **Design** | Wrong abstraction, missing edge case |
| **Implementation** | Bug, typo, wrong algorithm |
| **Dependencies** | API change, version drift, unavailable |
| **Process** | Skipped validation, wrong confidence |
| **Environment** | Config, permissions, resources |

### Phase 4: What Went Right

**Don't lose working patterns!**

```markdown
### What Went Right

- Tests caught issue before merge
- Rollback was clean and fast
- Error messages were clear
- Recovery process worked
```

### Phase 5: Action Items

Generate actionable improvements:

```markdown
### Action Items

| # | Action | Type | Priority | Owner |
|---|--------|------|----------|-------|
| 1 | Add API type definitions | Technical | High | Agent |
| 2 | Update plan with contract verification | Process | High | Agent |
| 3 | Lower default confidence for external APIs | Systemic | Medium | Constitution |
| 4 | Add integration test for API contract | Technical | Medium | Agent |
```

### Phase 6: Systemic Improvements

**These go beyond the immediate issue:**

```markdown
### Systemic Improvements

**For Constitution:**
- [ ] Require explicit contract verification for external integrations
- [ ] Add "external-api" tag that triggers extra validation

**For Process:**
- [ ] Default to NORMAL confidence for any API integration work
- [ ] Mandate baseline before touching external services

**For Future Planning:**
- [ ] Include "What could go wrong?" section in plans
- [ ] Require rollback strategy for risky changes
```

### Phase 7: Write to Memory

Distill durable learnings and append to `project docs`:

```markdown
## Incident Learnings

### 2026-01-27: External API Integration Failure

**Pattern**: External API calls failing due to unvalidated response shapes
**Learning**: Always define explicit types for external API responses before implementation
**Constitution Impact**: Added requirement for contract verification in external integrations
**Tags**: api, validation, confidence
```

## Output Format

```markdown
# Incident Postmortem

**Date**: {date}
**Issue**: {issue_id}
**Severity**: {Critical | High | Medium | Low}
**Duration**: {time from incident start to resolution}
**Trigger**: {what triggered postmortem}

---

## Summary

{1-2 sentence summary of what happened and outcome}

---

## Timeline

| Time | Event | Detail |
|------|-------|--------|
| T+0 | {event} | {detail} |
| ... | ... | ... |

---

## Root Cause Analysis

### The 5 Whys

1. **Why did the failure occur?** {answer}
2. **Why?** {answer}
3. **Why?** {answer}
4. **Why?** {answer}
5. **Why?** {answer}

### Root Cause

**Category**: {Requirements | Design | Implementation | Dependencies | Process | Environment}
**Description**: {detailed root cause}

### Contributing Factors

- {factor_1}
- {factor_2}

---

## What Went Right

{List things that worked well, even during failure}

---

## Action Items

| # | Action | Type | Priority | Status |
|---|--------|------|----------|--------|
| 1 | {action} | {type} | {priority} | TODO |

---

## Systemic Improvements

### For Constitution
- [ ] {improvement}

### For Process
- [ ] {improvement}

### For Future Planning
- [ ] {improvement}

---

## Durable Learnings

{Distilled insight for project learnings}
```

## Configuration

In `project docs`:

```yaml
postmortem:
  enabled: true
  auto_trigger:
    validation_failures: 2      # Trigger after N consecutive failures
    on_rollback: true           # Trigger on any rollback
    on_recovery: true           # Trigger when recovery skill invoked
  severity_threshold: medium    # Minimum severity to require postmortem
  require_systemic: true        # Force systemic improvements section
```
