# Cognitive Load Tracker

Tracks and budgets cognitive complexity introduced by code changes. Measures complexity across indirection, abstraction depth, state mutations, and naming clarity — because complexity debt is worse than technical debt.

## Usage Examples

### Analyze a file's complexity

```
Measure the cognitive load of src/services/orderProcessor.ts — is it too complex?
```

### Budget a refactoring change

```
Before I refactor auth, give me the current cognitive load budget for src/auth/.
```

### Complexity trend report

```
Show the complexity trend for the last 5 changes to the API module.
```

## Reference

See [SKILL.md](SKILL.md) for the full technical specification.
