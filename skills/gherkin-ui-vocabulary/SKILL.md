---
name: gherkin-ui-vocabulary
title: Gherkin UI Vocabulary Library
description: "Controlled vocabulary of UI interaction steps with helper function signatures in TypeScript, Python, and C#. Ensures consistency across feature files and adapters."
category: testing
---
# Gherkin UI Vocabulary — Controlled Step Library

## Purpose

Define and enforce a controlled vocabulary of UI interaction steps with corresponding helper function signatures in TypeScript, Python, and C#. Ensures consistency across all feature files and adapters. Prevents ad-hoc step proliferation.

## When to Use

- Establishing step vocabulary for a new project
- Standardizing steps across multiple teams/languages
- Onboarding new team members to the step library
- Reviewing step definitions for consistency

---

## The Step Vocabulary Concept

A **UI vocabulary** is a curated set of Gherkin steps that:
1. Cover all common UI interactions
2. Have consistent naming patterns
3. Map to specific helper functions in each language
4. Are documented with examples
5. Prevent ad-hoc step proliferation

---

## Navigation Steps

| Gherkin Step | Intent |
|-------------|--------|
| `Given I am on the {page} page` | Navigate to named page |
| `Given I am logged in as {role}` | Authenticate with role |
| `When I navigate to {page}` | Navigate during scenario |
| `When I go back` | Browser back |
| `When I refresh the page` | Page reload |

### Helper Signatures

```typescript
// TypeScript
async function navigateTo(page: Page, pageName: string): Promise<void>
async function loginAs(page: Page, role: string): Promise<void>
async function goBack(page: Page): Promise<void>
async function refreshPage(page: Page): Promise<void>
```

```python
# Python
def navigate_to(page: Page, page_name: str) -> None
def login_as(page: Page, role: str) -> None
def go_back(page: Page) -> None
def refresh_page(page: Page) -> None
```

```csharp
// C#
Task NavigateToAsync(IPage page, string pageName)
Task LoginAsAsync(IPage page, string role)
Task GoBackAsync(IPage page)
Task RefreshPageAsync(IPage page)
```

---

## Form Interaction Steps

| Gherkin Step | Intent |
|-------------|--------|
| `When I fill in {field} with {value}` | Set text input value |
| `When I select {option} from {dropdown}` | Select dropdown option |
| `When I check {checkbox}` | Check a checkbox |
| `When I uncheck {checkbox}` | Uncheck a checkbox |
| `When I upload {file} to {field}` | File upload |
| `When I clear {field}` | Clear input value |
| `When I submit the form` | Submit current form |

### Helper Signatures

```typescript
// TypeScript
async function fillField(page: Page, field: string, value: string): Promise<void>
async function selectOption(page: Page, dropdown: string, option: string): Promise<void>
async function checkBox(page: Page, checkbox: string): Promise<void>
async function uncheckBox(page: Page, checkbox: string): Promise<void>
async function uploadFile(page: Page, field: string, filePath: string): Promise<void>
async function clearField(page: Page, field: string): Promise<void>
async function submitForm(page: Page): Promise<void>
```

```python
# Python
def fill_field(page: Page, field: str, value: str) -> None
def select_option(page: Page, dropdown: str, option: str) -> None
def check_box(page: Page, checkbox: str) -> None
def uncheck_box(page: Page, checkbox: str) -> None
def upload_file(page: Page, field: str, file_path: str) -> None
def clear_field(page: Page, field: str) -> None
def submit_form(page: Page) -> None
```

```csharp
// C#
Task FillFieldAsync(IPage page, string field, string value)
Task SelectOptionAsync(IPage page, string dropdown, string option)
Task CheckBoxAsync(IPage page, string checkbox)
Task UncheckBoxAsync(IPage page, string checkbox)
Task UploadFileAsync(IPage page, string field, string filePath)
Task ClearFieldAsync(IPage page, string field)
Task SubmitFormAsync(IPage page)
```

---

## Assertion Steps

| Gherkin Step | Intent |
|-------------|--------|
| `Then I should see {text}` | Text visible on page |
| `Then I should not see {text}` | Text not visible |
| `Then the {field} should have value {value}` | Input has value |
| `Then the {field} should be empty` | Input is empty |
| `Then I should see {count} {items}` | Count elements |
| `Then the {element} should be visible` | Element visible |
| `Then the {element} should be hidden` | Element not visible |
| `Then the {element} should be disabled` | Element disabled |
| `Then I should see a confirmation message` | Success feedback |
| `Then I should see an error message` | Error feedback |
| `Then I should see the error {message}` | Specific error text |

### Helper Signatures

```typescript
// TypeScript
async function shouldSeeText(page: Page, text: string): Promise<void>
async function shouldNotSeeText(page: Page, text: string): Promise<void>
async function fieldShouldHaveValue(page: Page, field: string, value: string): Promise<void>
async function fieldShouldBeEmpty(page: Page, field: string): Promise<void>
async function shouldSeeCount(page: Page, count: number, itemSelector: string): Promise<void>
async function elementShouldBeVisible(page: Page, element: string): Promise<void>
async function elementShouldBeHidden(page: Page, element: string): Promise<void>
async function elementShouldBeDisabled(page: Page, element: string): Promise<void>
async function shouldSeeConfirmation(page: Page): Promise<void>
async function shouldSeeError(page: Page, message?: string): Promise<void>
```

```python
# Python
def should_see_text(page: Page, text: str) -> None
def should_not_see_text(page: Page, text: str) -> None
def field_should_have_value(page: Page, field: str, value: str) -> None
def field_should_be_empty(page: Page, field: str) -> None
def should_see_count(page: Page, count: int, item_selector: str) -> None
def element_should_be_visible(page: Page, element: str) -> None
def element_should_be_hidden(page: Page, element: str) -> None
def element_should_be_disabled(page: Page, element: str) -> None
def should_see_confirmation(page: Page) -> None
def should_see_error(page: Page, message: str | None = None) -> None
```

```csharp
// C#
Task ShouldSeeTextAsync(IPage page, string text)
Task ShouldNotSeeTextAsync(IPage page, string text)
Task FieldShouldHaveValueAsync(IPage page, string field, string value)
Task FieldShouldBeEmptyAsync(IPage page, string field)
Task ShouldSeeCountAsync(IPage page, int count, string itemSelector)
Task ElementShouldBeVisibleAsync(IPage page, string element)
Task ElementShouldBeHiddenAsync(IPage page, string element)
Task ElementShouldBeDisabledAsync(IPage page, string element)
Task ShouldSeeConfirmationAsync(IPage page)
Task ShouldSeeErrorAsync(IPage page, string? message = null)
```

---

## Table/List Steps

| Gherkin Step | Intent |
|-------------|--------|
| `Then the table should have {count} rows` | Row count |
| `Then the table should contain {text} in column {column}` | Cell content |
| `When I sort the table by {column}` | Column sort |
| `When I filter by {column} with {value}` | Table filter |
| `When I click on row {index}` | Row selection |

---

## Dialog/Modal Steps

| Gherkin Step | Intent |
|-------------|--------|
| `Then I should see a dialog with title {title}` | Dialog present |
| `When I confirm the dialog` | Accept dialog |
| `When I dismiss the dialog` | Cancel dialog |
| `When I fill in the dialog field {field} with {value}` | Dialog input |

---

## Locator Resolution Strategy

Each helper function must resolve `field`/`element` names to Playwright locators using this priority:

```typescript
function resolveLocator(page: Page, name: string): Locator {
  // 1. Try by label (most accessible)
  const byLabel = page.getByLabel(name);
  // 2. Try by role with name
  const byRole = page.getByRole('textbox', { name });
  // 3. Try by placeholder
  const byPlaceholder = page.getByPlaceholder(name);
  // 4. Try by test-id (kebab-case conversion)
  const testId = name.toLowerCase().replace(/\s+/g, '-');
  const byTestId = page.getByTestId(testId);
  // Return first visible match
  return byLabel.or(byRole).or(byPlaceholder).or(byTestId);
}
```

---

## Adding Custom Vocabulary

Teams can extend with domain-specific steps:

```gherkin
When I approve the order for {customer}
Then the invoice should be generated
When I assign the case to {agent}
```

**Rules:**
1. Must follow the same naming patterns (declarative, business language)
2. Must have helper functions in all supported languages
3. Must be documented in the step mapping table
4. Must not duplicate existing vocabulary steps

---

## Norwegian Vocabulary (Parallel)

```gherkin
# language: no

# Navigasjon
Gitt at jeg er på {side}-siden
Gitt at jeg er innlogget som {rolle}
Når jeg navigerer til {side}

# Skjema
Når jeg fyller inn {felt} med {verdi}
Når jeg velger {alternativ} fra {nedtrekksliste}
Når jeg huker av {avkryssingsboks}
Når jeg sender inn skjemaet

# Påstander
Så skal jeg se {tekst}
Så skal jeg ikke se {tekst}
Så skal feltet {felt} ha verdien {verdi}
Så skal feltet {felt} være tomt
Så skal {element} være synlig
Så skal {element} være skjult
Så skal jeg se en bekreftelsesmelding
Så skal jeg se en feilmelding
```

---

## Related Skills

- `gherkin-review` — Feature file quality checks
- `gherkin-playwright` — Playwright locator patterns used by helpers
- `gherkin-ui-alignment` — Validates vocabulary is aligned with frontend code
