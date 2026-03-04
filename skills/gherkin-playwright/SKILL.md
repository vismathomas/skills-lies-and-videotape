---
name: gherkin-playwright
title: Gherkin Playwright Integration
description: "Integrate Gherkin/BDD feature files with Playwright browser automation. Locator strategy, page objects, auth reuse, eventual consistency patterns."
category: testing
---
# Gherkin + Playwright — BDD Browser Automation

## Purpose

Integrate Gherkin/BDD feature files with Playwright browser automation. Covers locator strategy, page objects, auth reuse, and eventual consistency patterns for event-sourced systems. Multi-language: TypeScript, Python, C#.

## When to Use

- Writing Playwright step definitions for Gherkin scenarios
- Migrating from Selenium/Cypress to Playwright with BDD
- Building E2E test suite for a web frontend with Gherkin specs
- Dealing with flaky locators in BDD tests
- Testing event-sourced systems where UI projections lag

## Prerequisites

| Language | BDD Framework | Playwright |
|----------|-------------|------------|
| TypeScript/JS | `@cucumber/cucumber` or `playwright-bdd` | `@playwright/test` |
| Python | `pytest-bdd` or `behave` | `playwright` (pip) |
| C# | ReqnRoll | `Microsoft.Playwright` |

---

## Locator Strategy — Priority Order

Follow Playwright's official guidance:

1. **`data-testid`** — Most resilient, survives redesigns
2. **`getByRole()` + accessible name** — User-facing semantics
3. **`getByLabel()` / `getByText()`** — For specific content
4. **CSS selectors** — Last resort only

### Bad Locators (AVOID)

```typescript
// ❌ Fragile CSS path
page.locator('#app > div:nth-child(2) > form > input.name-field');

// ❌ XPath (almost never needed)
page.locator('//div[@class="form-group"]/input[@name="customerName"]');

// ❌ CSS framework class names
page.locator('.MuiInput-root.MuiInput-underline');
```

### Good Locators (USE)

```typescript
// ✅ Test ID (most resilient)
page.getByTestId('customer-name-input');

// ✅ Role + accessible name
page.getByRole('textbox', { name: 'Customer name' });

// ✅ Label association
page.getByLabel('Customer name');
```

---

## Step Definition Examples

### TypeScript

```typescript
import { Given, When, Then } from '@cucumber/cucumber';
import { Page, expect } from '@playwright/test';

When('I create a customer named {string}', async function (name: string) {
  const page: Page = this.page;
  await page.getByRole('button', { name: 'New Customer' }).click();
  await page.getByLabel('Customer name').fill(name);
  await page.getByRole('button', { name: 'Save' }).click();
});

Then('the customer {string} should appear in the list', async function (name: string) {
  await expect(this.page.getByRole('cell', { name })).toBeVisible();
});
```

### Python

```python
from pytest_bdd import when, then, parsers
from playwright.sync_api import Page, expect

@when(parsers.parse('I create a customer named "{name}"'))
def create_customer(page: Page, name: str):
    page.get_by_role("button", name="New Customer").click()
    page.get_by_label("Customer name").fill(name)
    page.get_by_role("button", name="Save").click()

@then(parsers.parse('the customer "{name}" should appear in the list'))
def customer_in_list(page: Page, name: str):
    expect(page.get_by_role("cell", name=name)).to_be_visible()
```

### C#

```csharp
[When(@"I create a customer named ""(.*)""")]
public async Task WhenICreateCustomerNamed(string name)
{
    await Page.GetByRole(AriaRole.Button, new() { Name = "New Customer" }).ClickAsync();
    await Page.GetByLabel("Customer name").FillAsync(name);
    await Page.GetByRole(AriaRole.Button, new() { Name = "Save" }).ClickAsync();
}

[Then(@"the customer ""(.*)"" should appear in the list")]
public async Task ThenCustomerShouldAppearInList(string name)
{
    await Expect(Page.GetByRole(AriaRole.Cell, new() { Name = name })).ToBeVisibleAsync();
}
```

---

## Page Object Model

### Structure

```
pages/
  CustomerListPage.{ts,py,cs}
  CustomerFormPage.{ts,py,cs}
  LoginPage.{ts,py,cs}
  BasePage.{ts,py,cs}
```

### TypeScript Page Object

```typescript
export class CustomerFormPage {
  constructor(private page: Page) {}

  get nameInput() { return this.page.getByLabel('Customer name'); }
  get orgNumberInput() { return this.page.getByLabel('Organization number'); }
  get saveButton() { return this.page.getByRole('button', { name: 'Save' }); }
  get successMessage() { return this.page.getByRole('alert').filter({ hasText: 'created' }); }

  async fillForm(name: string, orgNumber: string) {
    await this.nameInput.fill(name);
    await this.orgNumberInput.fill(orgNumber);
  }

  async save() { await this.saveButton.click(); }
  async expectSuccess() { await expect(this.successMessage).toBeVisible(); }
}
```

### Using Page Objects in Steps

```typescript
When('I create a customer named {string} with org number {string}',
  async function (name: string, orgNumber: string) {
    const form = new CustomerFormPage(this.page);
    await form.fillForm(name, orgNumber);
    await form.save();
  }
);
```

---

## Authentication & Storage State Reuse

Reuse auth across scenarios instead of logging in every time:

```typescript
// global-setup.ts — runs once, saves auth state
async function globalSetup() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('/login');
  await page.getByLabel('Email').fill('admin@example.com');
  await page.getByLabel('Password').fill('password');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForURL('/dashboard');
  await page.context().storageState({ path: 'playwright/.auth/admin.json' });
  await browser.close();
}
```

```typescript
// playwright.config.ts
export default defineConfig({
  projects: [
    { name: 'setup', testMatch: /.*\.setup\.ts/ },
    {
      name: 'chromium',
      use: { storageState: 'playwright/.auth/admin.json' },
      dependencies: ['setup'],
    },
  ],
});
```

---

## Eventual Consistency Patterns

For **event-sourced systems** where UI projections lag behind commands.

### The Problem

```gherkin
When I create a customer named "Acme Corp"
Then the customer "Acme Corp" should appear in the list  # ← May fail if projection hasn't caught up!
```

### Three-Tier Wait Strategy

**Tier 1 — Web-first assertions (built-in auto-retry):**
```typescript
await expect(page.getByText('Acme Corp')).toBeVisible();
```

**Tier 2 — Polling for complex conditions:**
```typescript
await expect.poll(async () => {
  return await page.getByRole('row').count();
}, {
  intervals: [1_000, 2_000, 5_000],
  timeout: 30_000,
  message: 'Waiting for customer to appear'
}).toBeGreaterThan(0);
```

**Tier 3 — API-assisted verification:**
```typescript
// Verify via API (faster), then confirm UI
await expect.poll(async () => {
  const response = await page.request.get('/api/customers?name=Acme');
  const data = await response.json();
  return data.length;
}, { timeout: 30_000 }).toBeGreaterThan(0);

await page.reload();
await expect(page.getByRole('cell', { name: 'Acme Corp' })).toBeVisible();
```

### Python Eventually Helper

```python
import time

def eventually(assertion_fn, timeout=30, intervals=(1, 2, 5)):
    """Retry assertion with increasing intervals for eventual consistency."""
    deadline = time.monotonic() + timeout
    last_error = None
    for interval in _cycle_intervals(intervals, deadline):
        try:
            assertion_fn()
            return
        except AssertionError as e:
            last_error = e
            if time.monotonic() + interval > deadline:
                break
            time.sleep(interval)
    raise last_error or AssertionError("Timed out")
```

---

## Artifact Configuration

```typescript
// playwright.config.ts — recommended for BDD suites
export default defineConfig({
  use: {
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'on-first-retry',
  },
  reporter: [
    ['html', { open: 'never' }],
    ['json', { outputFile: 'reports/results.json' }],
  ],
});
```

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|-------------|---------|----------|
| Fixed `sleep(5000)` waits | Slow and flaky | Use web-first assertions or `expect.poll` |
| CSS selectors in step defs | Fragile | Use `getByRole`, `getByLabel`, `getByTestId` |
| No page objects | Duplicated locators | Extract page objects |
| Login in every scenario | Slow suite | Use storage state auth reuse |
| No tracing on failure | Hard to debug CI | Enable `trace: 'on-first-retry'` |
| Mixing UI and API assertions | Unclear scope | Separate E2E and API suites |

---

## Related Skills

- `playwright` — General Playwright script execution (this skill adds the BDD layer)
- `gherkin-review` — Feature file quality checks
- `gherkin-ui-vocabulary` — Controlled step vocabulary for helpers
- `gherkin-step-generator` — ReqnRoll/C# step generation
