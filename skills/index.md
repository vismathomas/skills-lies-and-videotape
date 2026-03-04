# Skills Index

A curated collection of AI agent skills for software engineering workflows.

## Overview

| Category | Skills |
|----------|--------|
| [Analysis & Review](#analysis) | 14 |
| [Planning](#planning) | 2 |
| [Git & Version Control](#git) | 5 |
| [Documentation](#docs) | 3 |
| [Document Generation](#document-generation) | 2 |
| [Frontend & Design](#frontend) | 4 |
| [Testing & Browser Automation](#testing) | 11 |
| [Research](#research) | 2 |
| [Utility](#utility) | 5 |

---

## Analysis & Review

### Adversarial Code Review

> Adversarial code reviewer that assumes implementation is wrong and tries to break it conceptually. Finds attack vectors, edge cases, and failure modes.

- **Skill**: [adversary/SKILL.md](adversary/SKILL.md)
- **Usage**: [adversary/usage.md](adversary/usage.md)

### Article Verification

> Systematically deconstruct written content into verifiable claims, validate each using search/documentation, and facilitate informed discussion through structured interviewing.

- **Skill**: [article-verification/SKILL.md](article-verification/SKILL.md)
- **Usage**: [article-verification/usage.md](article-verification/usage.md)

### Cognitive Load Tracker

> Track and budget cognitive complexity introduced by changes. Complexity debt is worse than technical debt.

- **Skill**: [cognitive-load/SKILL.md](cognitive-load/SKILL.md)
- **Usage**: [cognitive-load/usage.md](cognitive-load/usage.md)

### Context Map Generation

> Analyze the codebase to create a concise, LLM-optimized structured overview.

- **Skill**: [context-map/SKILL.md](context-map/SKILL.md)
- **Usage**: [context-map/usage.md](context-map/usage.md)

### Improvement Discovery

> Identifies concrete justified improvements aligned with project goals

- **Skill**: [improvement-discovery/SKILL.md](improvement-discovery/SKILL.md)
- **Usage**: [improvement-discovery/usage.md](improvement-discovery/usage.md)

### Junior-Level Explanations

> Translate complex plans or implementations into junior-level explanations. If you can't explain it simply, you don't understand it.

- **Skill**: [junior-explain/SKILL.md](junior-explain/SKILL.md)
- **Usage**: [junior-explain/usage.md](junior-explain/usage.md)

### Narrative Coherence Audit

> Audit the project's story for coherence. Ensure issues, commits, plans, docs, and changelog tell a consistent narrative.

- **Skill**: [narrative-audit/SKILL.md](narrative-audit/SKILL.md)
- **Usage**: [narrative-audit/usage.md](narrative-audit/usage.md)

### Postmortem Analysis

> Enforces structured postmortem ritual when failures occur. Produces blameless analysis, identifies root causes, and writes durable learnings to memory.

- **Skill**: [postmortem/SKILL.md](postmortem/SKILL.md)
- **Usage**: [postmortem/usage.md](postmortem/usage.md)

### Potential Discovery

> Analyze incoming content (text, files, folders, URLs) to extract purpose, create summaries, and identify potential value for the current project.

- **Skill**: [potential-discovery/SKILL.md](potential-discovery/SKILL.md)
- **Usage**: [potential-discovery/usage.md](potential-discovery/usage.md)

### Project Section Identification

> Identify and map different sections of a software project (API, frontend, database, CLI, domain). Use for context scoping and architecture documentation.

- **Skill**: [project-sections/SKILL.md](project-sections/SKILL.md)
- **Usage**: [project-sections/usage.md](project-sections/usage.md)

### Feature Justification Audit

> Ruthlessly audit project features for justification. Challenge every feature to prove its value with evidence or face removal. Uses MCP tools for research.

- **Skill**: [prove-your-worth/SKILL.md](prove-your-worth/SKILL.md)
- **Usage**: [prove-your-worth/usage.md](prove-your-worth/usage.md)

### Reality Audit

> Aggressive evidence-based audit to verify project claims match implementation reality

- **Skill**: [reality-audit/SKILL.md](reality-audit/SKILL.md)
- **Usage**: [reality-audit/usage.md](reality-audit/usage.md)

### Shadow Plan (Alternative Plan Generator)

> Generate an alternative plan that deliberately disagrees with the primary plan to expose blind spots

- **Skill**: [shadow-plan/SKILL.md](shadow-plan/SKILL.md)
- **Usage**: [shadow-plan/usage.md](shadow-plan/usage.md)

### Temporal Risk Analysis

> Analyze how current changes might fail or become liabilities in 3, 6, or 12 months.

- **Skill**: [temporal-risk/SKILL.md](temporal-risk/SKILL.md)
- **Usage**: [temporal-risk/usage.md](temporal-risk/usage.md)

---

## Planning

### Plan Preview Generator

> Transform implementation plans into concise stakeholder-friendly summaries with file change overviews, component listings, and optional flow diagrams.

- **Skill**: [plan-preview/SKILL.md](plan-preview/SKILL.md)
- **Usage**: [plan-preview/usage.md](plan-preview/usage.md)

### Plan Review Import

> Parse exported PR review comments into structured review format for plan integration

- **Skill**: [plan-review-import/SKILL.md](plan-review-import/SKILL.md)
- **Usage**: [plan-review-import/usage.md](plan-review-import/usage.md)

---

## Git & Version Control

### GitHub PR Info Extraction

> Extract comprehensive information from a GitHub pull request using gh CLI including metadata, reviews, and inline comments

- **Skill**: [gh-pr-info/SKILL.md](gh-pr-info/SKILL.md)
- **Usage**: [gh-pr-info/usage.md](gh-pr-info/usage.md)

### Safe Git Operations

> Manage git operations safely. Includes stale state detection, branch/commit management. Never pushes without explicit user confirmation.

- **Skill**: [git/SKILL.md](git/SKILL.md)
- **Usage**: [git/usage.md](git/usage.md)

### Git Repository Analysis

> Analyze git repository for insights: contributor stats, commit patterns, branch health, and change analysis. Outputs actionable reports.

- **Skill**: [git-analysis/SKILL.md](git-analysis/SKILL.md)
- **Usage**: [git-analysis/usage.md](git-analysis/usage.md)

### Git Story Generator

> Generate narrative summaries from git history for onboarding, retrospectives, changelogs, and exploration. LLM-enhanced when available, works without LLM too.

- **Skill**: [git-story/SKILL.md](git-story/SKILL.md)
- **Usage**: [git-story/usage.md](git-story/usage.md)

### Git Worktree Management

> Manage git worktrees for isolated development. Create, list, remove, and work in worktrees.

- **Skill**: [git-worktree/SKILL.md](git-worktree/SKILL.md)
- **Usage**: [git-worktree/usage.md](git-worktree/usage.md)

---

## Documentation

### Astro Documentation Sites

> Scaffold and maintain Astro-based documentation sites with GitHub Pages deployment

- **Skill**: [astro-docs/SKILL.md](astro-docs/SKILL.md)
- **Usage**: [astro-docs/usage.md](astro-docs/usage.md)

### MkDocs Site Management

> MkDocs documentation site management: initializing, updating, building, and deploying

- **Skill**: [mkdocs/SKILL.md](mkdocs/SKILL.md)
- **Usage**: [mkdocs/usage.md](mkdocs/usage.md)

### Versioning & Release Management

> Manage semantic versioning, changelog generation, and release notes. Auto-generates entries from completed issues or git diff.

- **Skill**: [versioning/SKILL.md](versioning/SKILL.md)
- **Usage**: [versioning/usage.md](versioning/usage.md)

---

## Document Generation

### Word Document (DOCX) Creation & Editing

> Create, read, and edit Word documents (.docx). Use when producing professional documents with formatting, tables of contents, headings, tracked changes, comments, or images.

- **Skill**: [docx/SKILL.md](docx/SKILL.md)
- **Usage**: [docx/usage.md](docx/usage.md)
- **Source**: [https://github.com/anthropics/skills/tree/main/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx)

### PowerPoint Presentation (PPTX)

> Create, read, and edit PowerPoint presentations (.pptx). Use when producing slide decks, pitch decks, or any presentation with design guidance and mandatory visual QA.

- **Skill**: [pptx/SKILL.md](pptx/SKILL.md)
- **Usage**: [pptx/usage.md](pptx/usage.md)
- **Source**: [https://github.com/anthropics/skills/tree/main/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)

---

## Frontend & Design

### Frontend Design

> Create distinctive, production-grade frontend interfaces with high design quality. Avoids generic 'AI slop' aesthetics. Use when building web components, pages, or applications.

- **Skill**: [frontend-design/SKILL.md](frontend-design/SKILL.md)
- **Usage**: [frontend-design/usage.md](frontend-design/usage.md)
- **Source**: [https://github.com/anthropics/skills/tree/main/skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)

### GitHub-Safe Mermaid Diagrams

> GitHub-safe Mermaid diagram rules. Use when writing or reviewing Mermaid charts in Markdown files intended for GitHub rendering.

- **Skill**: [mermaid/SKILL.md](mermaid/SKILL.md)
- **Usage**: [mermaid/usage.md](mermaid/usage.md)

### Web Artifacts Builder

> Build interactive single-page web artifacts using React, TypeScript, Tailwind CSS, and shadcn/ui. Bundles into self-contained HTML files for demos and prototypes.

- **Skill**: [web-artifacts/SKILL.md](web-artifacts/SKILL.md)
- **Usage**: [web-artifacts/usage.md](web-artifacts/usage.md)
- **Source**: [https://github.com/anthropics/skills/tree/main/web-artifacts-builder](https://github.com/anthropics/skills/tree/main/web-artifacts-builder)

### Web Asset Generator

> Generate favicons, app icons, PWA manifest, and social media images (OG/Twitter cards) from logos, text, or emojis. Use when setting up web project branding assets.

- **Skill**: [web-assets/SKILL.md](web-assets/SKILL.md)
- **Usage**: [web-assets/usage.md](web-assets/usage.md)
- **Source**: [https://github.com/alonw0/web-asset-generator](https://github.com/alonw0/web-asset-generator)

---

## Testing & Browser Automation

### Agent Browser (CLI)

> Declarative browser automation via Vercel agent-browser CLI with ref-based interactions for AI agents.

- **Skill**: [agent-browser/SKILL.md](agent-browser/SKILL.md)
- **Usage**: [agent-browser/usage.md](agent-browser/usage.md)

### Gherkin Architecture & Suite Design

> Architecture primer for structuring large multi-language Gherkin/BDD test suites. Folder organization, shared steps, CI pipeline design.

- **Skill**: [gherkin-architecture/SKILL.md](gherkin-architecture/SKILL.md)
- **Usage**: [gherkin-architecture/usage.md](gherkin-architecture/usage.md)

### Gherkin + Playwright Integration

> Integrate Gherkin/BDD feature files with Playwright browser automation. Locator strategy, page objects, auth reuse, eventual consistency patterns.

- **Skill**: [gherkin-playwright/SKILL.md](gherkin-playwright/SKILL.md)
- **Usage**: [gherkin-playwright/usage.md](gherkin-playwright/usage.md)

### Gherkin Feature File Review & Linting

> Review and lint Gherkin feature files for quality, consistency, and BDD best practices. Multi-language (EN/NO). Catches anti-patterns before CI.

- **Skill**: [gherkin-review/SKILL.md](gherkin-review/SKILL.md)
- **Usage**: [gherkin-review/usage.md](gherkin-review/usage.md)

### Gherkin Step Definition Generator

> Generate ReqnRoll step definition classes from Gherkin feature files with real API integration test implementations. Creates WebApplicationFactory infrastructure, typed API clients, and state management.

- **Skill**: [gherkin-step-generator/SKILL.md](gherkin-step-generator/SKILL.md)
- **Usage**: [gherkin-step-generator/usage.md](gherkin-step-generator/usage.md)

### Gherkin UI Alignment Validation

> Validate alignment between Gherkin feature files, UI helper functions, and frontend source code. Detect drift, orphaned references, and dead steps.

- **Skill**: [gherkin-ui-alignment/SKILL.md](gherkin-ui-alignment/SKILL.md)
- **Usage**: [gherkin-ui-alignment/usage.md](gherkin-ui-alignment/usage.md)

### Gherkin UI Vocabulary Library

> Controlled vocabulary of UI interaction steps with helper function signatures in TypeScript, Python, and C#. Ensures consistency across feature files and adapters.

- **Skill**: [gherkin-ui-vocabulary/SKILL.md](gherkin-ui-vocabulary/SKILL.md)
- **Usage**: [gherkin-ui-vocabulary/usage.md](gherkin-ui-vocabulary/usage.md)

### Playwright Browser Automation

> Browser automation with Playwright. Write and execute custom Playwright code for testing, scraping, visual regression, form interaction, and any browser task.

- **Skill**: [playwright/SKILL.md](playwright/SKILL.md)
- **Usage**: [playwright/usage.md](playwright/usage.md)
- **Source**: [https://github.com/lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill)

### Playwright E2E Test Runner

> High-throughput, language-agnostic Playwright E2E execution with eventual-consistency primitives and CI sharding guidance.

- **Skill**: [playwright-e2e-runner/SKILL.md](playwright-e2e-runner/SKILL.md)
- **Usage**: [playwright-e2e-runner/usage.md](playwright-e2e-runner/usage.md)

### Playwright Ops (Reusable Browser Operations)

> Reusable, composable browser operations for admin workflows, evidence capture, and runbook automation via CLI macros and code adapters.

- **Skill**: [playwright-ops/SKILL.md](playwright-ops/SKILL.md)
- **Usage**: [playwright-ops/usage.md](playwright-ops/usage.md)

### Playwright Recorder (Record & Validate)

> Record browser navigation as versioned artifacts and validate replay in CI with snapshot-aware checks.

- **Skill**: [playwright-recorder/SKILL.md](playwright-recorder/SKILL.md)
- **Usage**: [playwright-recorder/usage.md](playwright-recorder/usage.md)

---

## Research

### Deep Topic Research

> Deep topic research with optional issue creation from findings. Use for researching technologies, patterns, libraries, or any topic requiring investigation.

- **Skill**: [research/SKILL.md](research/SKILL.md)
- **Usage**: [research/usage.md](research/usage.md)

### YouTube Transcript Extraction

> Extract transcripts from YouTube videos for research and documentation. Uses open-source tools only (yt-dlp, Whisper).

- **Skill**: [youtube-transcript/SKILL.md](youtube-transcript/SKILL.md)
- **Usage**: [youtube-transcript/usage.md](youtube-transcript/usage.md)
- **Source**: [https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript](https://github.com/michalparkola/tapestry-skills-for-claude-code/tree/main/youtube-transcript)

---

## Utility

### Systematic Debugging

> Systematic debugging approaches for isolating and fixing software defects. Use when something isn't working and the cause is unclear.

- **Skill**: [debugging/SKILL.md](debugging/SKILL.md)
- **Usage**: [debugging/usage.md](debugging/usage.md)

### PR Actionable Comments Analyzer

> Analyze PR review comments using gh CLI to identify actionable items from reviewer feedback and author replies.

- **Skill**: [gh-actionable-comments/SKILL.md](gh-actionable-comments/SKILL.md)
- **Usage**: [gh-actionable-comments/usage.md](gh-actionable-comments/usage.md)

### Structured Interview

> Conduct structured interviews with the user. Use when multiple decisions need user input: ask ONE question at a time, wait for response, record answer, then proceed to next question.

- **Skill**: [interview/SKILL.md](interview/SKILL.md)
- **Usage**: [interview/usage.md](interview/usage.md)

### Markdown to Jira Conversion

> Convert standard markdown syntax into Jira-compatible wiki markup

- **Skill**: [markdown-jira/SKILL.md](markdown-jira/SKILL.md)
- **Usage**: [markdown-jira/usage.md](markdown-jira/usage.md)

### Code Review Response

> Receive and respond to code review feedback. Verify suggestions before implementing, push back with reasoning when appropriate, avoid performative agreement.

- **Skill**: [review-response/SKILL.md](review-response/SKILL.md)
- **Usage**: [review-response/usage.md](review-response/usage.md)

---
