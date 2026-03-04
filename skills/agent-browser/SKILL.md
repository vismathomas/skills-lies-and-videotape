---
name: agent-browser
title: Agent Browser CLI
description: "Declarative browser automation via Vercel agent-browser CLI with ref-based interactions for AI agents."
category: testing
---
# Agent Browser (CLI-first)

Use Vercel `agent-browser` for browser automation when you want **CLI commands instead of generated scripts**.

## When to use

- Fast exploratory browser checks
- Ref-based interaction flows (`@e1`, `@e2`, ...)
- Agent-driven browser tasks with minimal code generation
- Screenshot/video capture and quick interaction replay

Use `playwright` instead when you need complex reusable code-heavy automation suites.

## Platform constraints (mandatory)

- `agent-browser` supports: **Linux / WSL / macOS**
- Native Windows shells are not supported directly
- If unavailable, fall back to `playwright`

## Install & verify

Upstream project reference: https://github.com/vercel-labs/agent-browser

```bash
npm install -g agent-browser
agent-browser install --with-deps
agent-browser --help
```

## Core workflow

1. Open target page
2. Take interactive snapshot
3. Interact by element refs
4. Re-snapshot after navigation or DOM mutation
5. Validate expected state

### Example flow

```bash
agent-browser open "https://example.com"
agent-browser snapshot -i
agent-browser click @e1
agent-browser fill @e2 "hello"
agent-browser snapshot -i
```

## Critical rules

- **Re-snapshot frequently**: refs can become stale after page changes
- Use `--json` for machine-readable outputs in automation chains
- Prefer session naming for parallel workflows (`--session <name>`)
- Keep commands small and deterministic

## Quick command map

- Navigation: `open`, `back`, `forward`, `reload`
- Snapshot: `snapshot -i`
- Interactions: `click`, `fill`, `type`, `press`, `select`, `check`
- Evidence: `screenshot`, `record start`, `record stop`
- Waits: `wait @ref`, `wait --text`, `wait --url`, `wait --load`
- State: `cookies`, `storage`, `state save`, `state load`
- Network: `network route`, `network requests`
- Tabs/sessions: `tab *`, `--session <name>`

## Integration notes

- Pairs well with  for E2E validation stages
- Can be used as browser-engine layer in multi-phase E2E workflows
- For script-centric or Windows-native automation, use `playwright`
