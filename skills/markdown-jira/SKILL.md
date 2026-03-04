---
name: markdown-to-jira
title: Markdown to Jira Conversion
description: "Convert standard markdown syntax into Jira-compatible wiki markup"
category: utility
---
# Markdown to Jira Conversion

## Purpose

Convert standard markdown files or text into Jira-compatible wiki markup. Jira uses a proprietary markup syntax that differs from standard markdown, requiring translation for content pasted into Jira issues, comments, or documentation.

## Procedure

1. **Identify input**: Accept a file path to a markdown file
2. **Read content**: Load the markdown content
3. **Apply conversions**: Transform markdown syntax to Jira markup (see conversion table below)
4. **Output result**: Display the converted Jira markup for user to copy

## Conversion Reference

| Markdown | Jira Markup | Notes |
|----------|-------------|-------|
| `# Heading 1` | `h1. Heading 1` | Headers h1-h6 |
| `## Heading 2` | `h2. Heading 2` | |
| `**bold**` | `*bold*` | Bold text |
| `*italic*` or `_italic_` | `_italic_` | Italic text |
| `~~strikethrough~~` | `-strikethrough-` | Strikethrough |
| `` `inline code` `` | `{{inline code}}` | Inline code |
| ` ```lang\ncode\n``` ` | `{code:lang}\ncode\n{code}` | Code blocks |
| `[text](url)` | `[text\|url]` | Links |
| `![alt](url)` | `!url!` | Images |
| `- item` or `* item` | `* item` | Bullet list |
| `1. item` | `# item` | Numbered list |
| `> quote` | `{quote}text{quote}` | Blockquotes |
| `---` or `***` | `----` | Horizontal rule |
| `| a | b |` | `\|\| a \|\| b \|\|` | Table headers |
| `| 1 | 2 |` | `\| 1 \| 2 \|` | Table rows |

## Nested List Handling

Markdown nested lists use indentation. Jira uses repeated markers:

**Markdown:**
```markdown
- Item 1
  - Nested 1
    - Deep nested
- Item 2
```

**Jira:**
```
* Item 1
** Nested 1
*** Deep nested
* Item 2
```

**Numbered nested:**
```
# Item 1
## Nested 1
### Deep nested
# Item 2
```

## Code Block Languages

Common mappings for syntax highlighting:

| Markdown | Jira |
|----------|------|
| ```javascript | {code:javascript} |
| ```python | {code:python} |
| ```java | {code:java} |
| ```csharp or ```cs | {code:c#} |
| ```sql | {code:sql} |
| ```bash or ```shell | {code:bash} |
| ```json | {code:json} |
| ```xml | {code:xml} |
| ```yaml | {code:yaml} |
| (no language) | {code} |

## Special Cases

### Multi-line Blockquotes

Markdown blockquotes span multiple `>` prefixed lines. In Jira, wrap entire content:

**Markdown:**
```markdown
> Line 1
> Line 2
> Line 3
```

**Jira:**
```
{quote}
Line 1
Line 2
Line 3
{quote}
```

### Tables

Jira requires `||` for header cells and `|` for data cells:

**Markdown:**
```markdown
| Name | Value |
|------|-------|
| foo  | 123   |
| bar  | 456   |
```

**Jira:**
```
|| Name || Value ||
| foo | 123 |
| bar | 456 |
```

### Escaping Pipe Characters

Pipes inside table cells: use `\|` in both formats.

## Completion Criteria

- [ ] Input markdown file read successfully
- [ ] All markdown syntax converted to Jira equivalents
- [ ] Output displayed for user copying
- [ ] No unconverted markdown syntax remaining

## Anti-patterns (avoid)

- ❌ Modifying the original markdown file
- ❌ Attempting to convert HTML embedded in markdown (pass through as-is)
- ❌ Guessing at markdown syntax not covered by conversion table
- ❌ Creating output files without user request (display only by default)

## Example

**Input** (`README.md`):
```markdown
# Project Title

This is **important** and _emphasized_.

## Features

- Feature 1
- Feature 2
  - Sub-feature

```python
def hello():
    print("world")
```

[Documentation](https://example.com)
```

**Output** (Jira markup):
```
h1. Project Title

This is *important* and _emphasized_.

h2. Features

* Feature 1
* Feature 2
** Sub-feature

{code:python}
def hello():
    print("world")
{code}

[Documentation|https://example.com]
```
