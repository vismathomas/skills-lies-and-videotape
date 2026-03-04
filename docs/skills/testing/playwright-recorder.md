---
title: Playwright Recorder
description: "Record browser navigation as versioned artifacts and validate replay in CI with snapshot-aware checks."
---

# Playwright Recorder

> Record browser navigation as versioned artifacts and validate replay in CI with snapshot-aware checks.

:material-tag: `testing`

---

Captures browser navigation as versioned artifacts and validates replay in CI with snapshot-aware checks. Enables record-now, validate-later workflows for UI flow verification.

## Usage Examples

### Record a user flow

```
Record the login → dashboard → settings flow as a versioned recording bundle.
```

### Set up CI validation

```
Configure CI to replay our recorded flows and flag any structural changes.
```

### Update a recording

```
Re-record the checkout flow since the UI was redesigned.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Playwright Recorder (Record & Validate)
    
    Capture durable browser navigation artifacts, version them, and validate them later in CI.
    
    ## When to use
    
    - Teams manually discover UI flows and need reproducible evidence
    - You want record-now, validate-later workflows
    - You need change-aware replay checks in pull requests and nightlies
    
    Primary recording surface can be `playwright-cli` (interactive), while validation is handled by adapter tests.
    
    ## Recording bundle format
    
    Store one bundle per flow:
    
    - `flow.yml` — semantic flow metadata + checkpoints
    - `snapshots/` — ARIA/DOM snapshots (structured, not pixel-only)
    - `traces/` — Playwright traces for failure analysis
    - `metadata.json` — app version, env, author, timestamps, tags
    
    Suggested location: `qa/e2e/recordings/<flow-name>/`
    
    ## Record workflow
    
    1. Open target app/session
    2. Capture baseline snapshot
    3. Perform interaction step
    4. Re-snapshot after each mutation/navigation
    5. Add explicit checkpoints
    6. Save bundle + metadata
    
    ## Validation workflow
    
    In CI:
    
    1. Load recording bundle
    2. Replay steps with environment-specific config
    3. Run structural validation (ARIA/snapshot assertions)
    4. Apply eventual consistency checkpoints where projections lag
    5. Persist artifacts on mismatch
    
    ## Eventual consistency support
    
    Use checkpoint entries in `flow.yml`:
    
    ```yaml
    checkpoints:
      - id: order-visible
        type: eventually
        timeout: 60s
        intervals: [1s, 2s, 10s]
    ```
    
    ## Gherkin integration (optional)
    
    If Gherkin exists, treat feature/scenario as source intent and materialize recording bundles from it. If not, YAML flow remains first-class.
    
    ## CI policy
    
    - PR: replay critical recordings (smoke)
    - Nightly: replay full bundle set
    - Keep traces/screenshots for failed validations
    - Use sharding for large recording suites
    
    ## Guardrails
    
    - Never store secrets in recording metadata
    - Keep auth state externalized and gitignored
    - Avoid brittle CSS-only selectors in recording checkpoints
    - Prefer semantic assertions over pixel-only checks
