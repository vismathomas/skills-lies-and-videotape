---
name: review-response
title: Code Review Response
description: "Receive and respond to code review feedback. Verify suggestions before implementing, push back with reasoning when appropriate, avoid performative agreement."
category: review
---
# Receiving Code Review — Response Workflow

> **Credit**: Code review response concepts adapted from obra/superpowers by Jesse Vincent (MIT License). See `skills/receiving-code-review/SKILL.md`.

## Purpose

Handle code review feedback systematically: verify each suggestion before implementing, push back when suggestions are incorrect, and avoid performative agreement that introduces bugs.

## Core Principles

### 1. Verify Before Implementing

**NEVER implement a review suggestion without verifying it first.**

For each piece of feedback:
```
1. Read the suggestion carefully
2. Understand what change is being requested
3. Find the relevant code
4. Verify the suggestion is correct:
   - Does it match the codebase reality?
   - Does it align with the project's architecture?
   - Would it actually improve the code?
5. THEN implement (or push back)
```

### 2. No Performative Agreement

**Do NOT agree with suggestions just because a reviewer made them.**

Anti-patterns to avoid:
| Anti-Pattern | Problem | Correct Response |
|--------------|---------|-----------------|
| "Good catch, fixed!" without checking | May introduce bugs | Verify the issue exists first |
| Implementing all suggestions blindly | Some may be wrong | Evaluate each independently |
| Agreeing to avoid conflict | Leads to worse code | Present reasoning respectfully |
| Treating reviewer as infallible | Reviewers can be wrong | Verify claims against actual code |

### 3. Push Back With Reasoning

**When a suggestion is incorrect or suboptimal, explain why:**

```
Template for pushing back:

"I looked into this suggestion. Here's what I found:

[Describe what you verified]
[Explain why the current approach is correct / the suggestion wouldn't work]
[Provide evidence: test results, documentation, code references]

I'd recommend keeping the current approach because [reason]."
```

**Never push back without evidence.** Always verify first.

## Procedure

### Step 1: Categorize Feedback

Sort each review comment into categories:

| Category | Action | Priority |
|----------|--------|----------|
| **Bug/Error** | Verify and fix if confirmed | HIGH |
| **Security concern** | Always investigate thoroughly | HIGH |
| **Style/formatting** | Apply if consistent with project conventions | LOW |
| **Architecture suggestion** | Evaluate against existing patterns | MEDIUM |
| **Performance concern** | Benchmark if feasible, otherwise evaluate | MEDIUM |
| **YAGNI candidate** | Check if suggestion adds unnecessary complexity | MEDIUM |
| **Question/clarification** | Respond with context | LOW |

### Step 2: YAGNI Check on Suggestions

For each suggestion that proposes adding code, abstraction, or complexity:

```
YAGNI Check:
- Is this needed for the current requirement? → If NO, defer
- Does this solve a real problem or a hypothetical one? → If hypothetical, skip
- Can this be added later without major refactoring? → If YES, defer
- What's the simplest thing that works? → Implement that instead
```

### Step 3: Handle Unclear Items

When a review comment is ambiguous:

```
1. Re-read the comment in context of the PR diff
2. Check if the reviewer referenced a specific line
3. If still unclear:
   - Ask for clarification before implementing
   - Don't guess what the reviewer meant
   - Don't implement what you think they might have meant
```

### Step 4: Implement Verified Changes

For each confirmed fix:
1. Make the change
2. Run tests to verify no regressions
3. If the fix breaks tests → re-evaluate the suggestion
4. Commit with reference: `fix: address review feedback — {summary}`

### Step 5: Respond to Each Item

After processing all feedback:
```
For each comment:
- ✅ Implemented: brief description of change made
- ❌ Not implemented: reasoning with evidence
- ❓ Need clarification: specific question
```

## Scope

- ✅ Categorize and prioritize review feedback
- ✅ Verify suggestions before implementing
- ✅ Push back with evidence when appropriate
- ✅ Apply YAGNI check to new suggestions
- ✅ Track which items were addressed
- ❌ Never implement suggestions blindly
- ❌ Never agree performatively
- ❌ Never skip verification
