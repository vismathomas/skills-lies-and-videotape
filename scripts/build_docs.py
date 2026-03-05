#!/usr/bin/env python3
"""
Build MkDocs documentation site from the skills folder.

Reads all SKILL.md and usage.md files from skills/, generates docs pages
under docs/skills/, creates a skills index page, and updates mkdocs.yml nav.

Safe to re-run whenever skills are added, removed, or changed.

Usage:
    uv run scripts/build_docs.py          # generate docs + update nav
    uv run scripts/build_docs.py --serve  # generate docs + launch dev server
    uv run scripts/build_docs.py --build  # generate docs + build static site
"""
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_SRC = ROOT / "skills"
DOCS_DIR = ROOT / "docs"
DOCS_SKILLS = DOCS_DIR / "skills"
DOCS_USER_STORIES = DOCS_DIR / "user-stories"
MKDOCS_YML = ROOT / "mkdocs.yml"

SKIP_DIRS = {"_archived"}
REPO_URL = "https://github.com/vismathomas/skills-lies-and-videotape"

# Category display names and ordering
CATEGORY_META = {
    "analysis":            ("Analysis & Review",            "magnify",          "Audit, review, and analyze code and projects"),
    "review":              ("Review",                       "shield-check",     "Code review, auditing, and verification"),
    "planning":            ("Planning",                     "clipboard-check",  "Plan, preview, and structure implementation work"),
    "git":                 ("Git & Version Control",        "git",              "Git operations, analysis, and history management"),
    "documentation":       ("Documentation",                "book-open-variant","Documentation sites, document generation, and release management"),
    "frontend":            ("Frontend & Design",            "palette",          "UI design, web assets, and visual tooling"),
    "testing":             ("Testing & Browser Automation", "test-tube",        "Browser automation, E2E testing, and BDD/Gherkin"),
    "utility":             ("Utility",                      "wrench",           "General-purpose utility skills"),
}


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter into a dict (simple key: value only)."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    fm_text = content[3:end].strip()
    result = {}
    for line in fm_text.split("\n"):
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            result[key.strip()] = val.strip().strip('"').strip("'")
    return result


def strip_frontmatter(content: str) -> str:
    """Return content after the frontmatter block."""
    if not content.startswith("---"):
        return content
    end = content.find("---", 3)
    if end == -1:
        return content
    return content[end + 3:].lstrip("\n")


def collect_skills() -> list[dict]:
    """Scan skills/ and collect metadata + content for each skill."""
    skills = []
    for d in sorted(SKILLS_SRC.iterdir()):
        if not d.is_dir() or d.name in SKIP_DIRS:
            continue
        skill_file = d / "SKILL.md"
        if not skill_file.exists():
            continue

        content = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        body = strip_frontmatter(content)

        usage_file = d / "usage.md"
        usage_content = ""
        if usage_file.exists():
            usage_raw = usage_file.read_text(encoding="utf-8")
            usage_content = strip_frontmatter(usage_raw)

        folder = d.name
        name = fm.get("name", folder)
        category = fm.get("category", "utility")
        description = fm.get("description", "")
        source = fm.get("source", "")

        # Build a display title: prefer frontmatter title, then auto-generate from name
        title = fm.get("title", name.replace("-", " ").title())

        skills.append({
            "folder": folder,
            "name": name,
            "title": title,
            "category": category,
            "description": description,
            "source": source,
            "body": body,
            "usage_content": usage_content,
        })
    return skills


def generate_skill_page(skill: dict) -> str:
    """Generate a single skill documentation page combining usage + spec."""
    lines = []

    lines.append(f"---")
    lines.append(f"title: {skill['title']}")
    if skill['description']:
        lines.append(f"description: \"{skill['description']}\"")
    lines.append(f"---")
    lines.append("")
    lines.append(f"# {skill['title']}")
    lines.append("")

    if skill["description"]:
        lines.append(f"> {skill['description']}")
        lines.append("")

    # Metadata badges
    meta_parts = [f":material-tag: `{skill['category']}`"]
    if skill["source"]:
        meta_parts.append(f":material-github: [{skill['source']}]({skill['source']})")
    lines.append(" · ".join(meta_parts))
    lines.append("")

    # GitHub links
    skill_path = f"skills/{skill['folder']}/SKILL.md"
    view_url = f"{REPO_URL}/blob/main/{skill_path}"
    raw_url = f"{REPO_URL}/raw/main/{skill_path}"
    lines.append(f"[:material-github: View on GitHub]({view_url}){{ .md-button }}")
    lines.append(f"[:material-download: Download SKILL.md]({raw_url}){{ .md-button .md-button--primary }}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Usage section (from usage.md) — strip its own title since we already have one
    if skill["usage_content"]:
        usage = skill["usage_content"].strip()
        # Remove the first H1 if it exists (we already have the title)
        usage = re.sub(r"^#\s+.+\n*", "", usage, count=1)
        # Remove "Reference" section that links to SKILL.md (not valid in docs context)
        usage = re.sub(r"##\s+Reference\s*\n+.*?SKILL\.md.*?\n*$", "", usage, flags=re.DOTALL)
        if usage.strip():
            lines.append(usage.strip())
            lines.append("")
            lines.append("---")
            lines.append("")

    # Full specification
    lines.append("## Full Specification")
    lines.append("")
    lines.append("??? abstract \"SKILL.md — Complete technical specification\"")
    lines.append("")
    # Indent the body inside the admonition
    for body_line in skill["body"].rstrip().split("\n"):
        lines.append(f"    {body_line}")
    lines.append("")

    return "\n".join(lines)


def generate_category_index(category_key: str, label: str, icon: str, desc: str, skills: list[dict]) -> str:
    """Generate an index page for a skill category."""
    lines = []
    lines.append(f"---")
    lines.append(f"title: {label}")
    lines.append(f"description: \"{desc}\"")
    lines.append(f"icon: material/{icon}")
    lines.append(f"---")
    lines.append("")
    lines.append(f"# :material-{icon}: {label}")
    lines.append("")
    lines.append(desc)
    lines.append("")
    lines.append(f"**{len(skills)} skills** in this category.")
    lines.append("")

    # Card grid
    lines.append('<div class="grid cards" markdown>')
    lines.append("")
    for skill in sorted(skills, key=lambda s: s["folder"]):
        title = skill["title"]
        desc_short = skill["description"][:120] + "..." if len(skill["description"]) > 120 else skill["description"]
        lines.append(f"-   :material-{icon}:{{ .lg .middle }} **[{title}]({skill['folder']}.md)**")
        lines.append(f"")
        lines.append(f"    ---")
        lines.append(f"")
        if desc_short:
            lines.append(f"    {desc_short}")
            lines.append(f"")
    lines.append("</div>")
    lines.append("")

    return "\n".join(lines)


def generate_skills_index(skills_by_cat: dict[str, list[dict]]) -> str:
    """Generate the top-level skills index page."""
    total = sum(len(v) for v in skills_by_cat.values())

    lines = []
    lines.append("---")
    lines.append("title: Skills, Lies and Videotape")
    lines.append(f"description: \"A curated collection of {total} AI agent skills for software engineering workflows.\"")
    lines.append("---")
    lines.append("")
    lines.append("# :material-bookshelf: Skills, Lies and Videotape")
    lines.append("")
    lines.append(f"A curated collection of **{total} skills** organized across **{len(skills_by_cat)} categories**.")
    lines.append("")

    # Overview cards
    lines.append('<div class="grid cards" markdown>')
    lines.append("")

    for cat_key in CATEGORY_META:
        if cat_key not in skills_by_cat:
            continue
        label, icon, desc = CATEGORY_META[cat_key]
        count = len(skills_by_cat[cat_key])
        lines.append(f"-   :material-{icon}:{{ .lg .middle }} **[{label}]({cat_key}/index.md)**")
        lines.append(f"")
        lines.append(f"    ---")
        lines.append(f"")
        lines.append(f"    {desc}")
        lines.append(f"")
        lines.append(f"    :material-arrow-right: [{count} skills]({cat_key}/index.md)")
        lines.append(f"")

    # Catch categories not in CATEGORY_META
    for cat_key in sorted(skills_by_cat.keys()):
        if cat_key not in CATEGORY_META:
            label = cat_key.replace("-", " ").title()
            count = len(skills_by_cat[cat_key])
            lines.append(f"-   :material-puzzle: **[{label}]({cat_key}/index.md)**")
            lines.append(f"")
            lines.append(f"    ---")
            lines.append(f"")
            lines.append(f"    :material-arrow-right: [{count} skills]({cat_key}/index.md)")
            lines.append(f"")

    lines.append("</div>")
    lines.append("")

    # Quick reference table
    lines.append("## All Skills")
    lines.append("")
    lines.append("| Skill | Category | Description |")
    lines.append("|-------|----------|-------------|")
    all_skills = []
    for cat_skills in skills_by_cat.values():
        all_skills.extend(cat_skills)
    for skill in sorted(all_skills, key=lambda s: s["folder"]):
        cat_label = CATEGORY_META.get(skill["category"], (skill["category"].title(), "", ""))[0]
        desc_short = skill["description"][:80] + "..." if len(skill["description"]) > 80 else skill["description"]
        lines.append(f"| [{skill['title']}]({skill['category']}/{skill['folder']}.md) | {cat_label} | {desc_short} |")
    lines.append("")

    return "\n".join(lines)


def generate_home_page(skills_by_cat: dict[str, list[dict]], user_stories: list[dict] | None = None) -> str:
    """Generate a landing page for the docs site."""
    lines = [
        "---",
        "title: Home",
        "---",
        "",
        '<div style="text-align: center;">',
        '  <img src="assets/images/logo.png" alt="Skills, Lies and Videotape" width="400">',
        "</div>",
        "",
        "# Skills, Lies and Videotape",
        "",
        "A curated library of AI agent skills for software engineering workflows.",
        "",
        '<div class="grid cards" markdown>',
        "",
        "-   :material-download:{ .lg .middle } **[Installation & Usage](installation.md)**",
        "",
        "    ---",
        "",
        "    How to install skills and integrate them into your workflow",
        "",
        "-   :material-bookshelf:{ .lg .middle } **[Skills Library](skills/index.md)**",
        "",
        "    ---",
        "",
    ]

    total = sum(len(v) for v in skills_by_cat.values())
    lines.append(f"    Browse all **{total} skills** across **{len(skills_by_cat)} categories**")
    lines.append("")
    lines.append("</div>")
    lines.append("")

    # Latest user stories
    stories = user_stories or []
    lines.append("## :material-book-account: Latest User Stories")
    lines.append("")
    if stories:
        for story in stories:
            desc = story["description"]
            lines.append(f"- **[{story['title']}](user-stories/{story['file']})** — {desc}")
        lines.append("")
        lines.append("[:material-arrow-right: All user stories](user-stories/index.md)")
    else:
        lines.append("*No stories yet — be the first to contribute!*")
    lines.append("")

    return "\n".join(lines)


def collect_user_stories() -> list[dict]:
    """Scan docs/user-stories/ and collect metadata for manually written pages."""
    stories = []
    if not DOCS_USER_STORIES.exists():
        return stories
    for f in sorted(DOCS_USER_STORIES.iterdir()):
        if not f.is_file() or f.suffix != ".md" or f.name == "index.md":
            continue
        content = f.read_text(encoding="utf-8")
        fm = parse_frontmatter(content)
        title = fm.get("title", f.stem.replace("-", " ").title())
        description = fm.get("description", "")
        category = fm.get("category", "")
        stories.append({
            "file": f.name,
            "title": title,
            "description": description,
            "category": category,
        })
    return stories


def generate_user_stories_index(stories: list[dict]) -> str:
    """Re-generate the user stories index page with a listing of all stories."""
    lines = [
        "---",
        "title: User Stories",
        'description: "Real-world stories, experiences, and workflows from skill users."',
        "icon: material/book-account",
        "---",
        "",
        "# :material-book-account: User Stories",
        "",
        "Real-world stories, experiences, and workflows from skill users.",
        "",
        "Drop a markdown file in this folder to have it automatically appear here. Each page should include frontmatter with `title`, `description`, and optionally `category`.",
        "",
        "---",
        "",
    ]
    if stories:
        lines.append(f"**{len(stories)} {'story' if len(stories) == 1 else 'stories'}** published.")
        lines.append("")
        lines.append("| Story | Description |")
        lines.append("|-------|-------------|")
        for story in stories:
            desc = story["description"][:100] + "..." if len(story["description"]) > 100 else story["description"]
            lines.append(f"| [{story['title']}]({story['file']}) | {desc} |")
        lines.append("")
    else:
        lines.append("*No stories yet — be the first to contribute!*")
        lines.append("")
    return "\n".join(lines)


def build_nav(skills_by_cat: dict[str, list[dict]], user_stories: list[dict] | None = None) -> list:
    """Build the nav structure for mkdocs.yml."""
    skills_nav = [{"Overview": "skills/index.md"}]

    for cat_key in CATEGORY_META:
        if cat_key not in skills_by_cat:
            continue
        label, _, _ = CATEGORY_META[cat_key]
        cat_items = [{"Overview": f"skills/{cat_key}/index.md"}]
        for skill in sorted(skills_by_cat[cat_key], key=lambda s: s["folder"]):
            cat_items.append({skill["title"]: f"skills/{cat_key}/{skill['folder']}.md"})
        skills_nav.append({label: cat_items})

    # Catch uncategorized
    for cat_key in sorted(skills_by_cat.keys()):
        if cat_key not in CATEGORY_META:
            label = cat_key.replace("-", " ").title()
            cat_items = [{"Overview": f"skills/{cat_key}/index.md"}]
            for skill in sorted(skills_by_cat[cat_key], key=lambda s: s["folder"]):
                cat_items.append({skill["title"]: f"skills/{cat_key}/{skill['folder']}.md"})
            skills_nav.append({label: cat_items})

    # User stories nav
    stories_nav_items: list = [{"Overview": "user-stories/index.md"}]
    if user_stories:
        for story in user_stories:
            stories_nav_items.append({story["title"]: f"user-stories/{story['file']}"})

    return [
        {"Home": "index.md"},
        {"Installation & Usage": "installation.md"},
        {"Skills": skills_nav},
        {"User Stories": stories_nav_items},
    ]


def update_mkdocs_yml(nav: list):
    """Update the nav section in mkdocs.yml, preserving everything else."""
    content = MKDOCS_YML.read_text(encoding="utf-8")

    # Remove existing nav section
    content = re.sub(r"\nnav:.*", "", content, flags=re.DOTALL)
    content = content.rstrip() + "\n"

    # Serialize nav as YAML manually (simple recursive)
    def yaml_nav(items, indent=0):
        lines = []
        prefix = "  " * indent
        for item in items:
            if isinstance(item, dict):
                for key, val in item.items():
                    if isinstance(val, str):
                        lines.append(f"{prefix}- {key}: {val}")
                    elif isinstance(val, list):
                        lines.append(f"{prefix}- {key}:")
                        lines.extend(yaml_nav(val, indent + 2))
            elif isinstance(item, str):
                lines.append(f"{prefix}- {item}")
        return lines

    nav_lines = yaml_nav(nav)
    content += "\nnav:\n" + "\n".join(f"  {line}" for line in nav_lines) + "\n"

    MKDOCS_YML.write_text(content, encoding="utf-8")


def main():
    print("=== Collecting skills ===\n")
    skills = collect_skills()
    print(f"  Found {len(skills)} skills\n")

    # Group by category
    skills_by_cat = defaultdict(list)
    for skill in skills:
        skills_by_cat[skill["category"]].append(skill)

    # Clean docs/skills/ for fresh generation
    if DOCS_SKILLS.exists():
        shutil.rmtree(DOCS_SKILLS)
    DOCS_SKILLS.mkdir(parents=True, exist_ok=True)

    # Generate home page
    print("=== Generating pages ===\n")

    # Collect user stories early so we can include them on the home page
    user_stories = collect_user_stories()

    home_page = DOCS_DIR / "index.md"
    home_page.write_text(generate_home_page(skills_by_cat, user_stories), encoding="utf-8")
    print("  ✓ docs/index.md")

    # Generate skills index
    index_content = generate_skills_index(skills_by_cat)
    skills_index = DOCS_SKILLS / "index.md"
    skills_index.write_text(index_content, encoding="utf-8")
    print("  ✓ docs/skills/index.md")

    # Generate category pages and skill pages
    for cat_key, cat_skills in skills_by_cat.items():
        label, icon, desc = CATEGORY_META.get(cat_key, (cat_key.replace("-", " ").title(), "puzzle", ""))
        cat_dir = DOCS_SKILLS / cat_key
        cat_dir.mkdir(parents=True, exist_ok=True)

        # Category index
        cat_index = generate_category_index(cat_key, label, icon, desc, cat_skills)
        (cat_dir / "index.md").write_text(cat_index, encoding="utf-8")
        print(f"  ✓ docs/skills/{cat_key}/index.md ({len(cat_skills)} skills)")

        # Individual skill pages
        for skill in cat_skills:
            page_content = generate_skill_page(skill)
            page_file = cat_dir / f"{skill['folder']}.md"
            page_file.write_text(page_content, encoding="utf-8")

    # Update mkdocs.yml nav
    print("\n=== Updating mkdocs.yml nav ===\n")

    # Generate user stories index
    if user_stories:
        us_index = generate_user_stories_index(user_stories)
        (DOCS_USER_STORIES / "index.md").write_text(us_index, encoding="utf-8")
        print(f"  ✓ docs/user-stories/index.md ({len(user_stories)} stories)")

    nav = build_nav(skills_by_cat, user_stories)
    update_mkdocs_yml(nav)
    print("  ✓ mkdocs.yml nav updated")

    print(f"\n=== Done — {len(skills)} skill pages generated ===\n")

    # Handle CLI flags
    if "--serve" in sys.argv:
        print("Starting dev server...\n")
        subprocess.run([sys.executable, "-m", "mkdocs", "serve"], cwd=ROOT)
    elif "--build" in sys.argv:
        print("Building static site...\n")
        subprocess.run([sys.executable, "-m", "mkdocs", "build"], cwd=ROOT)


if __name__ == "__main__":
    main()
