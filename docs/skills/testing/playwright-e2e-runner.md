---
title: Playwright E2E Test Runner
description: "High-throughput, language-agnostic Playwright E2E execution with eventual-consistency primitives and CI sharding guidance."
---

# Playwright E2E Test Runner

> High-throughput, language-agnostic Playwright E2E execution with eventual-consistency primitives and CI sharding guidance.

:material-tag: `testing`

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/playwright-e2e-runner/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/playwright-e2e-runner/SKILL.md){ .md-button .md-button--primary }

---

Runs stable, fast browser E2E test suites with eventual-consistency primitives and CI sharding guidance. Language-agnostic architecture supporting JS/TS, Python, and C# adapters.

## Usage Examples

### Set up E2E suite

```
Set up a structured Playwright E2E test suite with eventual consistency support for our event-sourced backend.
```

### Configure CI sharding

```
Configure CI to shard our E2E tests across 4 workers with merged reporting.
```

### Define test flows

```
Create suite and flow YAML specs for the checkout workflow.
```

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Playwright E2E Runner
    
    Run stable, fast browser E2E suites against a running frontend for greenfield and brownfield systems.
    
    ## When to use
    
    - You need reliable E2E validation in CI/CD
    - Event-sourced/eventually-consistent backends make fixed sleeps flaky
    - You need sharding and merged reporting to reduce wall-clock duration
    - You support multiple adapter languages (JS/TS, Python, C#)
    
    Use `playwright` for quick ad-hoc scripts. Use this skill for structured suites.
    
    ## Architecture (language-agnostic)
    
    Keep three layers separate:
    1. **Spec layer** (YAML): suite/flow behavior definitions
    2. **Intent layer**: shared step semantics (`navigate`, `act`, `assert`, `eventually`)
    3. **Adapter layer**: thin language-specific implementations
    
    Recommended folders:
    
    - `qa/e2e/suites/` — suite specs (`*.suite.yml`)
    - `qa/e2e/flows/` — flow specs (`*.flow.yml`)
    - `qa/e2e/environments/` — local/ci/staging env templates
    - `qa/e2e/fixtures/` — seeds/test data contracts
    - `qa/e2e/snapshots/` — ARIA/snapshot baselines
    - `qa/outputs/reports|traces|videos|screenshots/` — generated artifacts
    
    ## Core reliability rule: eventually everywhere
    
    Never rely on fixed `sleep` for domain propagation.
    
    Use shared primitive:
    
    ```text
    eventually(assertion, timeout=60s, intervals=[1s, 2s, 10s])
    ```
    
    Adapter mapping:
    - JS/TS: `expect.poll` / `expect().toPass()`
    - Python: polling helper wrapping Playwright assertions
    - C#: retry helper with bounded timeout and interval schedule
    
    ## Locator strategy standard
    
    1. `getByTestId()` (preferred)
    2. `getByRole()` (+ accessible name)
    3. `getByLabel()` / `getByText()`
    4. CSS/XPath only as last resort
    
    ## Auth and artifact policy
    
    - Reuse login state via `playwright/.auth/` (gitignored)
    - Trace: `on-first-retry`
    - Video: `on-first-retry`
    - Screenshot: on failure
    
    ## CI strategy
    
    Primary engine: Playwright Test.
    
    - Shard test run: `--shard=x/y`
    - Use blob/merge reporting for deterministic summary in parallel pipelines
    - Keep smoke suite for PR fast-feedback; full suite in heavier CI stage
    - Works for both GitHub Actions and TeamCity patterns
    
    ## Docker guidance
    
    - Use official Playwright image as runtime base
    - Add project dependencies and adapter runtime tooling
    - Keep browser deps pinned per project lock strategy
    
    ## Completion checklist
    
    - Specs defined (`suite.yml` + `flow.yml`)
    - Eventual consistency paths covered by `eventually`
    - Auth state reuse configured
    - CI sharding + report merge configured
    - Failure artifacts retained
    - No fixed sleeps in critical assertions
