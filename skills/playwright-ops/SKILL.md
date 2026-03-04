---
name: playwright-ops
title: Playwright Reusable Operations
description: "Reusable, composable browser operations for admin workflows, evidence capture, and runbook automation via CLI macros and code adapters."
category: testing
---
# Playwright Ops (Reusable Browser Operations)

Build reusable browser operations that can run from prompts/CLI macros and from maintainable code adapters.

## When to use

- Repeating admin/data-entry workflows
- Evidence capture for support/compliance
- Runbook automations that must be deterministic

Use this skill when one-off scripts become repeated operational tasks.

## Operation contract

Define operations as declarative specs (`*.op.yml`) with explicit inputs/outputs/artifacts.

Example schema:

```yaml
name: create-user
inputs:
  email: string
  role: string
steps:
  - navigate: /admin/users
  - action: click
    target: testid:new-user
  - action: fill
    target: testid:email
    value: ${email}
outputs:
  user_id: string
artifacts:
  trace: on-first-retry
  screenshot: on-failure
```

## Dual execution surfaces

1. **CLI macros (fast path):** quick operational execution and triage
2. **Code adapters (maintainable path):** Page Objects/helpers per language

Both should consume the same operation intent, not duplicate behavior.

## Brownfield scalability guidance

- Keep selectors centralized (`libs/selectors/`)
- Encapsulate page behaviors in Page Objects
- Keep operation specs small and composable
- Favor composition over giant monolithic flows

## Eventual consistency and verification

Ops often trigger async backend work. Add post-action verification with eventual checks:

```text
eventually(assertion, timeout=60s, intervals=[1s,2s,10s])
```

Prefer API-assisted verification when UI propagation is delayed.

## Evidence bundle policy

On operation failures, capture:
- Trace
- Screenshot
- Snapshot/DOM capture
- Structured operation input/output metadata

Store outputs under `qa/outputs/` and keep generated artifacts gitignored.

## Security and safety

- Mask secrets in logs/artifacts
- Use least-privilege operation accounts
- Keep destructive ops behind explicit confirmations
- Require idempotency notes for operations that may be retried

## Completion checklist

- `*.op.yml` operation spec created
- Adapter mapping exists for target language(s)
- Eventual consistency checks included
- Evidence artifacts configured
- Inputs/outputs documented
- CI task includes at least one replay/verification job
