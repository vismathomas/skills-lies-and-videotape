"""
Refactor all SKILL.md files to remove ao-specific concepts.

Mechanical transforms:
1. YAML frontmatter: strip invokes/invoked_by with ao-* refs, remove state_files block,
   clean name field to remove ao- prefix, keep description/category/source
2. Body: remove .agent/ops/focus.json output sections, constitution.md/focus.json/
   baseline.md/memory.md references, ao CLI commands, ao-* skill cross-references,
   "[AO]" commit prefix, confidence system references
3. Rename skill cross-references to drop ao- prefix
"""
import re
import os
from pathlib import Path

SKILLS_DIR = Path(r"c:\dev\worktrees\mkdocs-template\skills")

# Map of ao-prefixed names to their clean equivalents
RENAME_MAP = {
    "ao-adversary": "adversary",
    "ao-article-verification": "article-verification",
    "ao-astro-docs": "astro-docs",
    "ao-cognitive-load": "cognitive-load",
    "ao-context-map": "context-map",
    "ao-debugging": "debugging",
    "ao-docx": "docx",
    "ao-frontend-design": "frontend-design",
    "ao-gh-actionable-comments": "gh-actionable-comments",
    "ao-gh-pr-info": "gh-pr-info",
    "ao-gherkin-architecture": "gherkin-architecture",
    "ao-gherkin-playwright": "gherkin-playwright",
    "ao-gherkin-review": "gherkin-review",
    "ao-gherkin-step-generator": "gherkin-step-generator",
    "ao-gherkin-ui-alignment": "gherkin-ui-alignment",
    "ao-gherkin-ui-vocabulary": "gherkin-ui-vocabulary",
    "ao-git": "git",
    "ao-git-analysis": "git-analysis",
    "ao-git-story": "git-story",
    "ao-git-worktree": "git-worktree",
    "ao-improvement-discovery": "improvement-discovery",
    "ao-interview": "interview",
    "ao-junior-explain": "junior-explain",
    "ao-markdown-jira": "markdown-jira",
    "ao-mermaid": "mermaid",
    "ao-mkdocs": "mkdocs",
    "ao-narrative-audit": "narrative-audit",
    "ao-plan-preview": "plan-preview",
    "ao-plan-review-import": "plan-review-import",
    "ao-playwright": "playwright",
    "ao-postmortem": "postmortem",
    "ao-potential-discovery": "potential-discovery",
    "ao-pptx": "pptx",
    "ao-project-sections": "project-sections",
    "ao-prove-your-worth": "prove-your-worth",
    "ao-reality-audit": "reality-audit",
    "ao-research": "research",
    "ao-review-response": "review-response",
    "ao-shadow-plan": "shadow-plan",
    "ao-temporal-risk": "temporal-risk",
    "ao-versioning": "versioning",
    "ao-web-artifacts": "web-artifacts",
    "ao-web-assets": "web-assets",
    "ao-youtube-transcript": "youtube-transcript",
}

# Skills that were deleted (Tier 3+4) - references to these should be removed entirely
DELETED_SKILLS = {
    "ao-state", "ao-task", "ao-theme-factory", "ao-baseline", "ao-docs",
    "ao-implementation", "ao-testing", "ao-planning", "ao-critical-review",
    "ao-retrospective", "ao-housekeeping", "ao-canvas-design", "ao-idea",
    "ao-review", "ao-complete", "ao-init", "ao-focus-scan", "ao-recovery",
    "ao-calibrator", "ao-constitution", "ao-confidence-decay", "ao-execute",
    "ao-build", "ao-install", "ao-lint-instructions", "ao-optimize-instructions",
    "ao-auto", "ao-skills-advisor", "ao-skills-sh", "ao-dogfood",
    "ao-epic-analyzer", "ao-issue-merge", "ao-llm-export", "ao-migrate",
    "ao-parallel", "ao-plan-integrate-review", "ao-report", "ao-selective-branch",
    "ao-selective-merge", "ao-skill-fatigue", "ao-spec", "ao-time-report",
    "ao-tools", "ao-update", "ao-usage", "ao-validation", "ao-dependencies",
    "ao-branch-workflow", "ao-guide", "ao-intent-drift", "ao-scope",
    "aoi-usage", "ao-create-python-project", "ao-create-skill",
    "ao-create-technical-docs",
}


def parse_frontmatter(content: str):
    """Split content into frontmatter dict-like string and body."""
    if not content.startswith("---"):
        return "", content

    end = content.find("---", 3)
    if end == -1:
        return "", content

    fm = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")
    return fm, body


def clean_frontmatter(fm: str) -> str:
    """Clean YAML frontmatter by removing ao-specific fields."""
    lines = fm.split("\n")
    result = []
    skip_block = False
    skip_indent = 0

    for line in lines:
        stripped = line.strip()

        # Skip state_files block entirely
        if stripped.startswith("state_files:"):
            skip_block = True
            skip_indent = len(line) - len(line.lstrip())
            continue
        if skip_block:
            current_indent = len(line) - len(line.lstrip()) if stripped else skip_indent + 2
            if current_indent > skip_indent or stripped.startswith("read:") or stripped.startswith("write:"):
                continue
            else:
                skip_block = False

        # Clean name field - remove ao- prefix
        if stripped.startswith("name:"):
            name_val = stripped[5:].strip().strip('"').strip("'")
            if name_val.startswith("ao-"):
                name_val = name_val[3:]
            result.append(f"name: {name_val}")
            continue

        # Clean invokes field - remove ao-* entries, keep non-ao entries
        if stripped.startswith("invokes:"):
            invokes_match = re.search(r'\[(.*?)\]', stripped)
            if invokes_match:
                items = [i.strip() for i in invokes_match.group(1).split(",")]
                # Keep items that aren't ao-* or deleted skills
                clean_items = []
                for item in items:
                    item = item.strip()
                    if item in DELETED_SKILLS:
                        continue
                    if item in RENAME_MAP:
                        clean_items.append(RENAME_MAP[item])
                    elif not item.startswith("ao-"):
                        clean_items.append(item)
                if clean_items:
                    result.append(f"invokes: [{', '.join(clean_items)}]")
                else:
                    result.append("invokes: []")
            else:
                result.append("invokes: []")
            continue

        # Clean invoked_by field - remove ao-* entries
        if stripped.startswith("invoked_by:"):
            invoked_match = re.search(r'\[(.*?)\]', stripped)
            if invoked_match:
                items = [i.strip() for i in invoked_match.group(1).split(",")]
                clean_items = []
                for item in items:
                    item = item.strip()
                    if item in DELETED_SKILLS:
                        continue
                    if item in RENAME_MAP:
                        clean_items.append(RENAME_MAP[item])
                    elif not item.startswith("ao-"):
                        clean_items.append(item)
                if clean_items:
                    result.append(f"invoked_by: [{', '.join(clean_items)}]")
                else:
                    result.append("invoked_by: []")
            else:
                result.append("invoked_by: []")
            continue

        # Clean references field - remove .agent/ops paths
        if stripped.startswith("references:"):
            ref_match = re.search(r'\[(.*?)\]', stripped)
            if ref_match:
                items = [i.strip() for i in ref_match.group(1).split(",")]
                clean_items = [i for i in items if ".agent/ops" not in i and ".ao/" not in i]
                if clean_items:
                    result.append(f"references: [{', '.join(clean_items)}]")
                else:
                    result.append("references: []")
            else:
                result.append("references: []")
            continue

        result.append(line)

    return "\n".join(result)


def clean_body(body: str) -> str:
    """Clean body text by removing ao-specific content."""

    # Remove focus.json output sections at the end
    # Pattern: "## Output\n\nUpdate `.agent/ops/focus.json`:" followed by a code block
    body = re.sub(
        r'\n## Output\s*\n\n(?:After[^\n]*\n\n)?Update [`\']?\.agent/ops/focus\.json[`\']?:\s*\n```(?:markdown|md)?\n.*?```\s*$',
        '',
        body,
        flags=re.DOTALL
    )

    # Also catch "## Output\n\nUpdate focus.json:" variant
    body = re.sub(
        r'\n## Output\s*\n\n(?:After[^\n]*\n\n)?Update\s+focus\.json:\s*\n```(?:markdown|md)?\n.*?```\s*$',
        '',
        body,
        flags=re.DOTALL
    )

    # Remove lines about .agent/ops/ paths (but not entire sections)
    body = re.sub(r'Default location: `\.agent/ops/[^`]*`\s*\n?', '', body)

    # Replace inline references to .agent/ops/ paths
    body = re.sub(r'`\.agent/ops/[^`]*`', '`project docs`', body)
    body = re.sub(r'\.agent/ops/', '', body)

    # Remove constitution.md references
    body = re.sub(r'`?constitution\.md`?\s*(?:configuration|config|constraints?|limits?|rules?)?\s*', '', body)
    
    # Remove focus.json tracking references  
    body = re.sub(r'Track(?:ing)?\s+(?:in\s+)?`?focus\.json`?\s*[:\.]?\s*\n?', '', body)

    # Remove "[AO]" commit prefix references
    body = re.sub(r'\[AO\]\s*', '', body)
    body = re.sub(r'`\[AO\]`\s*', '', body)

    # Replace ao-* skill references in body text with clean names
    for ao_name, clean_name in sorted(RENAME_MAP.items(), key=lambda x: -len(x[0])):
        # Replace backtick-wrapped references
        body = body.replace(f"`{ao_name}`", f"`{clean_name}`")
        # Replace plain text references (word boundary)
        body = re.sub(rf'\b{re.escape(ao_name)}\b', clean_name, body)

    # Remove references to deleted skills
    for skill in DELETED_SKILLS:
        body = re.sub(rf'`{re.escape(skill)}`', '', body)
        body = re.sub(rf'\b{re.escape(skill)}\b', '', body)

    # Remove "invoke ao-state" type instructions
    body = re.sub(r'[Ii]nvoke\s+\w+-\w+\s+(?:to|for|when)\s+[^\n]*\n?', '', body)

    # Clean ao CLI commands
    body = re.sub(r'`ao\s+[^`]+`', '', body)
    body = re.sub(r'\bao\s+(?:ls|issue|log|lesson|version|scope)\s+[^\n]*\n?', '', body)

    # Remove "Agent: ao-*" labels
    body = re.sub(r'Agent:\s*ao-\w+\s*\n?', '', body)

    # Clean up confidence level references tied to ao system
    body = re.sub(r'confidence\s*(?:level|score|budget|threshold)s?\s*(?:from|in|per)\s*(?:constitution|baseline)\s*[^\n]*\n?', '', body, flags=re.IGNORECASE)

    # Clean up "AO" in titles while preserving content
    body = re.sub(r'# AO\s+', '# ', body)
    body = re.sub(r'## AO\s+', '## ', body)

    # Remove double blank lines created by removals
    body = re.sub(r'\n{3,}', '\n\n', body)

    return body.rstrip() + '\n'


def process_skill(skill_dir: Path):
    """Process a single SKILL.md file."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return

    content = skill_file.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    if fm:
        fm = clean_frontmatter(fm)
        body = clean_body(body)
        new_content = f"---\n{fm}\n---\n{body}"
    else:
        body = clean_body(content)
        new_content = body

    skill_file.write_text(new_content, encoding="utf-8")
    print(f"  Processed: {skill_dir.name}")


def rename_folders():
    """Rename ao-prefixed folders to clean names."""
    renamed = []
    for ao_name, clean_name in RENAME_MAP.items():
        old_path = SKILLS_DIR / ao_name
        new_path = SKILLS_DIR / clean_name
        if old_path.exists():
            if new_path.exists():
                print(f"  CONFLICT: {clean_name} already exists, skipping {ao_name}")
                continue
            old_path.rename(new_path)
            renamed.append((ao_name, clean_name))
            print(f"  Renamed: {ao_name} -> {clean_name}")
    return renamed


def main():
    print("=== Refactoring SKILL.md files ===\n")

    # Process all skill directories
    for d in sorted(SKILLS_DIR.iterdir()):
        if d.is_dir():
            process_skill(d)

    print("\n=== Renaming folders ===\n")
    renamed = rename_folders()

    print(f"\n=== Done: {len(renamed)} folders renamed ===")


if __name__ == "__main__":
    main()
