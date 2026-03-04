# BUG Debug Template

Use this template when debugging BUG issues. Follow the 4-phase systematic debugging process.

## Issue Details

**Issue ID**: {ISSUE-ID}
**Title**: {Bug Title}
**Created**: {Date}

## Phase 1: Root Cause Investigation

### Error Messages
```
[Paste error messages here]
```

### Stack Trace Analysis
- Entry point: {function/line}
- Error origin: {where it started}
- Propagation path: {call stack}

### Reproduction Steps
1. {Step 1}
2. {Step 2}
3. {Step 3}

### Recent Changes (git diff)
```bash
[git diff output]
```

### Data Flow Trace
- Input: {what comes in}
- Processing: {what happens}
- Expected output: {what should happen}
- Actual output: {what actually happens}
- Divergence point: {where it goes wrong}

## Phase 2: Pattern Analysis

### Working Examples Found
- {Similar working code in codebase}
- Location: {file/function}

### Comparison with References
- Documentation says: {what docs say}
- Our code does: {what we do}
- Difference: {what's different}

### Dependencies Check
- Library version: {version}
- API compatibility: {yes/no}
- Configuration: {settings used}

## Phase 3: Hypothesis and Testing

### Hypothesis 1
- Theory: {what you think causes it}
- Prediction: {if theory is true, X will happen}
- Test: {what you tested}
- Result: ✅ Confirmed / ❌ Refuted

### Hypothesis 2 (if needed)
- Theory: {refined theory}
- Prediction: {if theory is true, Y will happen}
- Test: {what you tested}
- Result: ✅ Confirmed / ❌ Refuted

## Phase 4: Implementation

### Failing Test (MANDATORY)
```python/any
[Code for failing test]
```
- Test created: [Date]
- Test run result: ❌ FAIL (expected)
- This proves we're testing the right thing

### Fix Attempt 1
- Fix: {what you changed}
- Test result: ❌ FAIL / ✅ PASS

### Fix Attempt 2 (if needed)
- Fix: {what you changed}
- Test result: ❌ FAIL / ✅ PASS

### Fix Attempt 3 (if needed)
- Fix: {what you changed}
- Test result: ❌ FAIL / ✅ PASS

⚠️ **IF 3+ ATTEMPTS FAIL**: Question architecture - is the design the problem?

### Final Fix
- Root cause: {what was actually wrong}
- Fix applied: {final solution}
- Test result: ✅ PASS
- No regressions: {yes/no}

## Verification

- [ ] Failing test created and confirmed to fail
- [ ] Root cause identified (not just symptom treated)
- [ ] Fix addresses root cause
- [ ] Failing test now passes
- [ ] No regressions introduced
- [ ] Similar code checked for same issue

## Resolution

**Fixed on**: {Date}
**Duration**: {Time spent debugging}
**Root Cause**: {Summary of actual problem}
**Fix**: {Summary of solution}
**Test Added**: {Test file/function}

## Follow-up Issues

- [ ] Related: {ISSUE-ID} - {description}
