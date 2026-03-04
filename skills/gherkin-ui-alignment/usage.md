# Gherkin UI Alignment Validation

Validates alignment between Gherkin feature files, UI helper functions, and frontend source code. Detects drift where steps reference UI elements that no longer exist or helpers that don't match the current UI.

## Usage Examples

### Check for UI drift

```
Validate that all Gherkin steps still match the current UI components.
```

### Find orphaned helpers

```
Identify UI helper functions that are no longer referenced by any feature file.
```

### Alignment audit

```
Run a full alignment check between our feature files, step helpers, and React components.
```

## Reference

See [SKILL.md](SKILL.md) for the full technical specification.
