---
title: Installation & Usage
description: "How to install and use skills with VS Code and GitHub Copilot."
---

# :material-download: Installation & Usage

Skills are standalone Markdown files (`SKILL.md`) that provide domain-specific instructions to AI coding agents like GitHub Copilot. This guide covers how to install them in your project.

## Quick Start

1. **Download** a skill's `SKILL.md` from any skill page
2. **Place it** in your project's `.github/skills/<skill-name>/` folder
3. **Done** — Copilot will automatically discover and use it

## File Structure

Skills should be placed inside your project repository under `.github/skills/`:

```
your-project/
├── .github/
│   ├── copilot-instructions.md      # Global Copilot instructions (optional)
│   └── skills/
│       ├── debugging/
│       │   └── SKILL.md
│       ├── git/
│       │   └── SKILL.md
│       └── playwright/
│           └── SKILL.md
├── src/
└── ...
```

Each skill lives in its own folder named after the skill. The folder must contain a `SKILL.md` file.

## Installing a Single Skill

### Option 1: Download from this site

Every skill page has a **:material-download: Download SKILL.md** button. Click it, then place the file in your project:

```bash
# Create the skill folder
mkdir -p .github/skills/debugging

# Move the downloaded file
mv ~/Downloads/SKILL.md .github/skills/debugging/SKILL.md
```

### Option 2: Copy from GitHub

```bash
# Clone the repo (or use sparse checkout for a single skill)
git clone https://github.com/vismathomas/skills-lies-and-videotape.git

# Copy the skill you want
cp -r skills-lies-and-videotape/skills/debugging .github/skills/debugging
```

### Option 3: Direct download with curl

```bash
mkdir -p .github/skills/debugging
curl -sL https://raw.githubusercontent.com/vismathomas/skills-lies-and-videotape/main/skills/debugging/SKILL.md \
  -o .github/skills/debugging/SKILL.md
```

## Installing All Skills

To install the entire collection:

```bash
# Clone the repo
git clone https://github.com/vismathomas/skills-lies-and-videotape.git

# Copy all skills into your project
cp -r skills-lies-and-videotape/skills/ .github/skills/
```

## How Skills Work in VS Code

### GitHub Copilot Chat

When you use Copilot Chat in VS Code, it automatically discovers `SKILL.md` files under `.github/skills/`. Skills are matched based on their `name`, `description`, and content — Copilot selects the relevant skill(s) for your prompt.

**Example:** If you ask Copilot to "debug why my API returns 500 errors", it will find and apply the `debugging` skill if it's installed.

### Skill Frontmatter

Each `SKILL.md` has YAML frontmatter that helps Copilot understand when to use it:

```yaml
---
name: debugging
title: Systematic Debugging
description: "Systematic debugging approaches for isolating and fixing software defects."
category: utility
---
```

| Field | Purpose |
|-------|---------|
| `name` | Identifier matching the folder name |
| `title` | Human-readable display name |
| `description` | Helps Copilot match the skill to your prompt |
| `category` | Organizational grouping |

### Invoking a Skill Explicitly

You can reference a skill directly in Copilot Chat:

```
Use the debugging skill to analyze why the login test is failing.
```

Or mention it by description:

```
Help me review this PR using adversarial code review techniques.
```

### Global Instructions

You can also reference skills from your project's `copilot-instructions.md`:

```markdown
<!-- .github/copilot-instructions.md -->

## Project Guidelines

- When debugging, follow the systematic debugging skill
- All git operations should follow the safe git operations skill
- Use the gherkin review skill when writing BDD feature files
```

## Tips

- **Start small** — install just the skills relevant to your workflow
- **Commit skills** to your repo so the whole team benefits
- **Customize** — skills are plain Markdown, feel free to adapt them to your project's conventions
- **Combine** — multiple skills can work together (e.g., `gherkin-playwright` + `playwright`)
