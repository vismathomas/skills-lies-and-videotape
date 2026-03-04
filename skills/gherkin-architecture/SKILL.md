---
name: gherkin-architecture
title: Gherkin Architecture & Suite Design
description: "Architecture primer for structuring large multi-language Gherkin/BDD test suites. Folder organization, shared steps, CI pipeline design."
category: testing
---
# Gherkin Architecture — Suite Structure & CI Design

## Purpose

Architecture and planning primer for structuring large, multi-language Gherkin/BDD test suites. Covers folder organization, shared step strategies, cross-language patterns, and CI pipeline design.

## When to Use

- Setting up BDD testing in a new project
- Restructuring an existing Gherkin suite that has grown unwieldy
- Planning multi-language test strategy (e.g., C# backend + TypeScript frontend)
- Designing CI pipelines for Gherkin-based testing

---

## Folder Organization

### Small Project (single language)

```
tests/
  features/
    customer.feature
    order.feature
    auth.feature
  step_definitions/
    customer_steps.py     # or .ts or .cs
    order_steps.py
    auth_steps.py
  support/
    world.py              # shared context/fixtures
    hooks.py              # before/after hooks
```

### Medium Project (single language, multiple domains)

```
tests/
  features/
    customer/
      create_customer.feature
      edit_customer.feature
    order/
      place_order.feature
    auth/
      login.feature
  step_definitions/
    customer/
      create_steps.py
    shared/
      auth_steps.py
      navigation_steps.py
  support/
    world.py
    hooks.py
    factories.py          # test data factories
```

### Large Project (multi-language, multi-team)

```
qa/
  features/                    # Language-neutral feature files (SHARED)
    customer/
      create_customer.feature
    order/
      place_order.feature
    shared/
      auth.feature
  
  adapters/
    typescript/                # Frontend E2E adapter
      step_definitions/
      support/
      playwright.config.ts
      package.json
    
    python/                    # API/backend adapter
      step_definitions/
      support/
      conftest.py
    
    dotnet/                    # ReqnRoll adapter
      StepDefinitions/
      Support/
      ReqnRoll.json
      Tests.csproj

  environments/
    local.env
    staging.env

  fixtures/
    seed_data.json
```

**Key principle**: Feature files are **language-neutral** and shared across all adapters. Step definitions are **language-specific** and live in adapter directories.

---

## Shared Steps Strategy — Layered Steps

Teams often create too many shared steps, leading to god files and implicit coupling. Use a layered approach:

```
Layer 1: Domain steps (per-feature)
  └── "When I create a customer named {string}"
  └── "Then the order total should be {decimal}"

Layer 2: Shared interaction steps (cross-feature)
  └── "Given I am logged in as {role}"
  └── "Then I should see a confirmation message"

Layer 3: Technical infrastructure (framework)
  └── Before/After hooks
  └── Database cleanup
  └── API client setup
```

**Rules:**
- Layer 1 steps should **never** call Layer 2 steps directly
- Layer 2 steps should be **stateless** (no side effects beyond their description)
- Layer 3 is **invisible** to feature files (hooks, not steps)

---

## Cross-Language Step Mapping

When the same feature file is executed by multiple language adapters, maintain a step mapping table:

| Gherkin Step | TypeScript | Python | C# |
|-------------|-----------|--------|-----|
| `Given I am logged in as {role}` | `loginAs(role)` | `login_as(role)` | `LoginAs(role)` |
| `When I create a customer named {name}` | `createCustomer(name)` | `create_customer(name)` | `CreateCustomer(name)` |
| `Then the customer should exist` | `expectCustomerExists()` | `assert_customer_exists()` | `CustomerShouldExist()` |

Maintain this mapping in `qa/docs/step-mapping.md` and update as steps evolve.

---

## CI Pipeline Design

### Pipeline Stages

```
Stage 1: Gherkin Lint (fast, <30s)
  └── Validate feature file syntax
  └── Check anti-patterns (use gherkin-review)
  └── Verify step definitions exist for all steps

Stage 2: Unit Tests (fast, 1-3min)
  └── Step definition unit tests
  └── Helper function tests

Stage 3: Integration Tests (medium, 5-15min)
  └── API integration tests (Python/C# adapters)
  └── Database integration tests

Stage 4: E2E Tests (slow, 15-60min)
  └── Browser-based E2E (TypeScript adapter)
  └── Sharded execution (Playwright --shard)
```

### Tag-Based Pipeline Selection

Use tags to control which scenarios run in each pipeline context:

| Context | Tag Filter | When |
|---------|-----------|------|
| PR smoke | `@smoke` | Every pull request |
| PR regression | `@regression` | PR to main/release branches |
| Nightly | `@regression and not @flaky` | Scheduled nightly |
| WIP only | `@wip` | Developer local or draft PR |
| Full suite | (no filter) | Release candidate |

---

## Test Data Strategy

| Strategy | When | Example |
|----------|------|---------|
| **Inline** | Simple, self-contained scenarios | `Given a customer named "Acme"` |
| **Factories** | Complex objects, many scenarios | `Given a customer with default values` |
| **Fixtures** | Shared reference data | `Given the standard product catalog` |
| **API seeding** | Integration/E2E setup | Before hook calls API |
| **Database seeding** | Fast setup, cleanup guaranteed | Transaction rollback per scenario |

---

## Architecture Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Feature files in language-specific dirs | Can't share across adapters | Centralize in `qa/features/` |
| One step file per feature file | File explosion | Group by domain |
| Steps calling other steps | Hidden dependencies | Use helper functions |
| No cleanup strategy | Test pollution, flaky tests | Transaction rollback or API cleanup |
| Hardcoded URLs/credentials | Environment-specific failures | Environment config files |
| Massive Background blocks | Slow setup | Extract to hooks or factories |
| God step files (500+ lines) | Unrelated steps coupled | Split by domain |
| Missing step mapping table | Cross-language drift | Maintain `step-mapping.md` |

---

## Localization Architecture

For teams working in multiple spoken languages:

- **Never** mix languages within a single feature file
- Declare `# language:` header on every file
- If teams speak different languages, maintain separate feature files per language **or** standardize on one canonical language

Supported localizations referenced by this skill:
- `# language: en` — English (`Given`/`When`/`Then`)
- `# language: no` — Norwegian bokmål (`Gitt`/`Når`/`Så`)
- Any Cucumber-supported language

---

## Related Skills

- `gherkin-review` — Feature file linting (invoked at CI Stage 1)
- `gherkin-playwright` — Playwright integration for E2E adapter
- `gherkin-ui-vocabulary` — Controlled step vocabulary across adapters
- `gherkin-step-generator` — ReqnRoll/C# step generation
