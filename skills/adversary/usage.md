# Adversarial Code Review

Performs adversarial code reviews by assuming implementations are broken and systematically trying to find attack vectors, edge cases, and failure modes. Acts as a devil's advocate reviewer to strengthen code quality.

## Usage Examples

### Review a new authentication module

```
Review the auth module in src/auth/ — assume it's broken and find every way it could fail.
```

### Security audit of API endpoints

```
Do an adversarial review of our API endpoints in src/api/routes.py — focus on injection, auth bypass, and DoS vectors.
```

### Review a data processing pipeline

```
Attack this ETL pipeline code — what happens with malformed input, timeouts, and partial failures?
```

## Reference

See [SKILL.md](SKILL.md) for the full technical specification.
