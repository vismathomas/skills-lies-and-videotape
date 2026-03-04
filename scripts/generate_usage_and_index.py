"""
Generate usage.md files for each skill and an index.md for the skills directory.

Tasks:
1. Create usage.md beside each SKILL.md with description, examples, and credits
2. Remove tier, invokes, invoked_by from frontmatter
3. Add category where missing
4. Create index.md grouped by category with links
"""
import re
import os
from pathlib import Path
from collections import defaultdict

SKILLS_DIR = Path(r"c:\dev\worktrees\mkdocs-template\skills")

# Skip these directories (not skills)
SKIP_DIRS = {"_archived"}


# ── Skill metadata and usage content ──────────────────────────────────────────

SKILL_DATA = {
    "adversary": {
        "title": "Adversarial Code Review",
        "usage_intro": "Performs adversarial code reviews by assuming implementations are broken and systematically trying to find attack vectors, edge cases, and failure modes. Acts as a devil's advocate reviewer to strengthen code quality.",
        "examples": [
            ("Review a new authentication module", "Review the auth module in src/auth/ — assume it's broken and find every way it could fail."),
            ("Security audit of API endpoints", "Do an adversarial review of our API endpoints in src/api/routes.py — focus on injection, auth bypass, and DoS vectors."),
            ("Review a data processing pipeline", "Attack this ETL pipeline code — what happens with malformed input, timeouts, and partial failures?"),
        ],
    },
    "agent-browser": {
        "title": "Agent Browser (CLI)",
        "usage_intro": "Declarative browser automation using the Vercel agent-browser CLI. Uses ref-based interactions for fast, exploratory browser tasks without generating full scripts.",
        "examples": [
            ("Quick website check", "Open https://example.com and take a screenshot."),
            ("Fill out a form", "Navigate to the signup page, fill in the email field, and click submit."),
            ("Capture evidence of a UI issue", "Open the dashboard, take a screenshot, then click the settings button and take another screenshot."),
        ],
    },
    "article-verification": {
        "title": "Article Verification",
        "usage_intro": "Systematically deconstructs written content into verifiable claims, validates each using search and documentation, and facilitates informed discussion through structured interviewing. Ideal for fact-checking articles before publication.",
        "examples": [
            ("Fact-check a blog post", "Verify all claims in this blog post about React performance optimizations."),
            ("Validate a technical article", "Check the factual accuracy of this article about Kubernetes scaling strategies."),
            ("Review a press release", "Identify and verify every factual claim in this product announcement."),
        ],
    },
    "astro-docs": {
        "title": "Astro Documentation Sites",
        "usage_intro": "Scaffold and maintain Astro-based documentation sites with GitHub Pages deployment. Handles site initialization, content authoring, component integration, and CI/CD setup.",
        "examples": [
            ("Create a new docs site", "Set up an Astro documentation site for this project with GitHub Pages deployment."),
            ("Add a new docs section", "Add an API Reference section to the Astro docs site."),
            ("Configure the site for deployment", "Set up GitHub Actions to deploy the Astro docs to GitHub Pages on push to main."),
        ],
    },
    "cognitive-load": {
        "title": "Cognitive Load Tracker",
        "usage_intro": "Tracks and budgets cognitive complexity introduced by code changes. Measures complexity across indirection, abstraction depth, state mutations, and naming clarity — because complexity debt is worse than technical debt.",
        "examples": [
            ("Analyze a file's complexity", "Measure the cognitive load of src/services/orderProcessor.ts — is it too complex?"),
            ("Budget a refactoring change", "Before I refactor auth, give me the current cognitive load budget for src/auth/."),
            ("Complexity trend report", "Show the complexity trend for the last 5 changes to the API module."),
        ],
    },
    "context-map": {
        "title": "Context Map Generation",
        "usage_intro": "Analyzes a codebase to create a concise, LLM-optimized structured overview. The resulting context map enables reasoning about the whole project without reading every file.",
        "examples": [
            ("Generate a project overview", "Create a context map of this project."),
            ("Partial refresh after changes", "Refresh the context map for the src/api/ area — I just made significant changes there."),
            ("Onboarding overview", "Generate a context map so I can understand this unfamiliar codebase."),
        ],
    },
    "debugging": {
        "title": "Systematic Debugging",
        "usage_intro": "Provides systematic debugging approaches for isolating and fixing software defects. Use when something isn't working and the cause is unclear — follows structured investigation rather than guesswork.",
        "examples": [
            ("Debug a failing test", "This test in tests/test_auth.py is failing intermittently — help me debug it systematically."),
            ("Isolate a production error", "Users are seeing 500 errors on the /api/orders endpoint — help me trace the root cause."),
            ("Fix a regression", "Something broke after the last merge — the login flow redirects to a blank page."),
        ],
    },
    "docx": {
        "title": "Word Document (DOCX) Creation & Editing",
        "usage_intro": "Creates, reads, and edits Word documents (.docx). Handles professional documents with formatting, tables of contents, headings, tracked changes, comments, and images.",
        "examples": [
            ("Create a project report", "Create a Word document with an executive summary, findings section, and recommendations for the Q1 review."),
            ("Extract text from a docx", "Read and summarize the contents of the requirements.docx file."),
            ("Edit an existing document", "Update the version number and add a new section to proposal.docx."),
        ],
    },
    "frontend-design": {
        "title": "Frontend Design",
        "usage_intro": "Creates distinctive, production-grade frontend interfaces with high design quality. Avoids generic 'AI slop' aesthetics by applying real design principles — typography, color theory, spacing, and visual hierarchy.",
        "examples": [
            ("Design a landing page", "Create a visually distinctive landing page for a developer tool — no generic blue gradients."),
            ("Build a dashboard UI", "Design a monitoring dashboard with dark theme, data cards, and real-time status indicators."),
            ("Create a component library", "Build a set of form components with consistent styling and good accessibility."),
        ],
    },
    "gh-actionable-comments": {
        "title": "PR Actionable Comments Analyzer",
        "usage_intro": "Analyzes pull request review comments using the gh CLI to identify actionable items from reviewer feedback and author replies. Tracks which comments have been acknowledged and still need to be addressed.",
        "examples": [
            ("Analyze current PR comments", "Analyze the review comments on the current PR and list what needs to be fixed."),
            ("Check a specific PR", "Analyze actionable comments on PR #106."),
            ("Find unresolved feedback", "Which review comments on this PR still need a response from the author?"),
        ],
    },
    "gh-pr-info": {
        "title": "GitHub PR Info Extraction",
        "usage_intro": "Extracts comprehensive information from a GitHub pull request using the gh CLI and GitHub REST API. Fetches metadata, reviews, inline comments, status checks, and file changes.",
        "examples": [
            ("Get PR overview", "Get all information about the current PR — reviews, comments, status checks."),
            ("Extract PR review details", "Show me all review comments and their resolution status for PR #42."),
            ("PR metadata for documentation", "Extract the PR description, linked issues, and reviewer list for PR #15."),
        ],
    },
    "gherkin-architecture": {
        "title": "Gherkin Architecture & Suite Design",
        "usage_intro": "Architecture primer for structuring large, multi-language Gherkin/BDD test suites. Covers folder organization, shared step strategies, cross-language patterns, and CI pipeline design.",
        "examples": [
            ("Design a BDD test structure", "Help me organize our Gherkin test suite for a project with both C# and TypeScript step implementations."),
            ("Set up CI for BDD tests", "Design a CI pipeline that runs our Gherkin test suites with sharding and merged reports."),
            ("Plan shared step strategy", "How should we structure shared steps across 5 feature areas?"),
        ],
    },
    "gherkin-playwright": {
        "title": "Gherkin + Playwright Integration",
        "usage_intro": "Integrates Gherkin/BDD feature files with Playwright browser automation. Covers locator strategy, page objects, auth reuse, and eventual consistency patterns. Multi-language: TypeScript, Python, C#.",
        "examples": [
            ("Connect features to Playwright", "Wire up our login.feature Gherkin file to Playwright step implementations in TypeScript."),
            ("Set up auth state reuse", "Configure Playwright to reuse auth state across our BDD scenarios."),
            ("Handle eventual consistency", "Our event-sourced backend has propagation delays — set up Playwright assertions with polling."),
        ],
    },
    "gherkin-review": {
        "title": "Gherkin Feature File Review & Linting",
        "usage_intro": "Reviews and lints Gherkin feature files for quality, consistency, and BDD best practices. Catches anti-patterns before CI. Supports English and Norwegian (bokmål) localization.",
        "examples": [
            ("Review feature files", "Review all .feature files in qa/features/ for BDD best practices."),
            ("Check for anti-patterns", "Lint this feature file for common Gherkin anti-patterns like incidental details and conjunction steps."),
            ("Review Norwegian feature file", "Review this Norwegian Gherkin feature file for consistency with our conventions."),
        ],
    },
    "gherkin-step-generator": {
        "title": "Gherkin Step Definition Generator",
        "usage_intro": "Generates ReqnRoll step definition classes from Gherkin feature files with real API integration test implementations. Creates WebApplicationFactory infrastructure, typed API clients, and state management.",
        "examples": [
            ("Generate step definitions", "Generate ReqnRoll step definitions for the user-registration.feature file."),
            ("Create integration test infrastructure", "Set up WebApplicationFactory and typed API clients for our BDD integration tests."),
            ("Scaffold steps from new features", "Generate step definitions for these 3 new feature files with realistic API implementations."),
        ],
    },
    "gherkin-ui-alignment": {
        "title": "Gherkin UI Alignment Validation",
        "usage_intro": "Validates alignment between Gherkin feature files, UI helper functions, and frontend source code. Detects drift where steps reference UI elements that no longer exist or helpers that don't match the current UI.",
        "examples": [
            ("Check for UI drift", "Validate that all Gherkin steps still match the current UI components."),
            ("Find orphaned helpers", "Identify UI helper functions that are no longer referenced by any feature file."),
            ("Alignment audit", "Run a full alignment check between our feature files, step helpers, and React components."),
        ],
    },
    "gherkin-ui-vocabulary": {
        "title": "Gherkin UI Vocabulary Library",
        "usage_intro": "Defines and enforces a controlled vocabulary of UI interaction steps with corresponding helper function signatures in TypeScript, Python, and C#. Ensures consistency across all feature files and adapters.",
        "examples": [
            ("Define a new UI action", "Add a 'select from dropdown' step to our controlled vocabulary with helper signatures for TypeScript and C#."),
            ("Audit vocabulary usage", "Check which vocabulary steps are used across our feature files and which are unused."),
            ("Generate helper stubs", "Generate TypeScript helper function stubs for all vocabulary steps in our library."),
        ],
    },
    "git": {
        "title": "Safe Git Operations",
        "usage_intro": "Manages git operations safely with built-in protections. Includes stale state detection, branch/commit management, and protected branch enforcement. Never pushes without explicit user confirmation.",
        "examples": [
            ("Create a feature branch", "Create a feature branch for issue BUG-123 and commit the current changes."),
            ("Check for stale state", "Check if my local repo state is stale — did someone else push changes?"),
            ("Safe commit workflow", "Stage and commit all changes in src/ with a conventional commit message."),
        ],
    },
    "git-analysis": {
        "title": "Git Repository Analysis",
        "usage_intro": "Analyzes git repositories for insights including contributor statistics, commit patterns, branch health, and change analysis. Produces actionable reports from repository history.",
        "examples": [
            ("Generate contributor stats", "Show contributor statistics for the last 3 months."),
            ("Analyze commit patterns", "What are the commit frequency patterns and hotspots in this repo?"),
            ("Branch health check", "Which branches are stale and which have unmerged work?"),
        ],
    },
    "git-story": {
        "title": "Git Story Generator",
        "usage_intro": "Generates human-readable narratives from git commit history. Useful for onboarding new team members, creating retrospective summaries, building changelogs, and exploring project evolution.",
        "examples": [
            ("Onboarding summary", "Generate a story of how this project evolved over the last 6 months for a new team member."),
            ("Sprint retrospective", "Create a narrative summary of what was accomplished in the last sprint from git history."),
            ("Feature evolution", "Tell the story of how the authentication module was built, from the first commit."),
        ],
    },
    "git-worktree": {
        "title": "Git Worktree Management",
        "usage_intro": "Manages git worktrees for isolated development. Create, list, remove, and work in worktrees to develop multiple features simultaneously without switching branches.",
        "examples": [
            ("Create a worktree for a feature", "Create a worktree for the feat/new-api branch so I can work on it without disrupting my current work."),
            ("List active worktrees", "Show me all active worktrees and their branches."),
            ("Clean up a completed worktree", "Remove the worktree for feat/auth-refactor — it's been merged."),
        ],
    },
    "improvement-discovery": {
        "title": "Improvement Discovery",
        "usage_intro": "Identifies concrete, justified improvements to a codebase that are aligned with the project's stated goals. Avoids generic best practices and speculative recommendations — every suggestion must have clear value.",
        "examples": [
            ("Find improvements in the API layer", "Analyze the API module for concrete improvements aligned with our goal of reducing response times."),
            ("Discover tech debt worth fixing", "Find justified improvements in the codebase — no generic advice, only things with clear ROI."),
            ("Review for simplification opportunities", "What concrete simplifications could we make to the auth module?"),
        ],
    },
    "interview": {
        "title": "Structured Interview",
        "usage_intro": "Conducts structured interviews with the user. Asks one question at a time, waits for responses, and records answers. Ideal when multiple decisions need user input without overwhelming them.",
        "examples": [
            ("Gather project requirements", "Interview me about the requirements for the new notification system — one question at a time."),
            ("Design decision interview", "I need to make decisions about our database strategy — interview me to help clarify the options."),
            ("Preferences collection", "Interview me about my coding preferences and conventions for this project."),
        ],
    },
    "junior-explain": {
        "title": "Junior-Level Explanations",
        "usage_intro": "Translates complex plans or implementations into junior-level explanations. If you can't explain it simply, you don't understand it. Useful for documentation, onboarding, and validating understanding.",
        "examples": [
            ("Explain a complex plan", "Explain this implementation plan for the event sourcing migration as if I'm a junior developer."),
            ("Simplify architecture docs", "Translate this architecture document into something a junior developer would understand."),
            ("Explain a code change", "Explain what this PR does and why, in simple terms for someone new to the codebase."),
        ],
    },
    "markdown-jira": {
        "title": "Markdown to Jira Conversion",
        "usage_intro": "Converts standard markdown syntax into Jira-compatible wiki markup. Handles headings, bold/italic, code blocks, links, tables, nested lists, and other formatting differences.",
        "examples": [
            ("Convert a README", "Convert this README.md to Jira markup so I can paste it into a Jira issue."),
            ("Convert release notes", "Convert CHANGELOG.md to Jira format for the release issue."),
            ("Quick conversion", "Convert this markdown text to Jira markup:\\n\\n## Features\\n- **Bold item**\\n- `code item`"),
        ],
    },
    "mermaid": {
        "title": "GitHub-Safe Mermaid Diagrams",
        "usage_intro": "Rules and constraints for authoring Mermaid diagrams that render correctly on GitHub. GitHub uses an older, restricted Mermaid renderer — this skill ensures your diagrams won't break.",
        "examples": [
            ("Create a flow diagram", "Create a Mermaid flowchart for the order processing pipeline that renders on GitHub."),
            ("Review a diagram", "Review this Mermaid diagram for GitHub compatibility issues."),
            ("Convert to GitHub-safe format", "This Mermaid diagram uses block-beta which doesn't work on GitHub — convert it to a compatible format."),
        ],
    },
    "mkdocs": {
        "title": "MkDocs Site Management",
        "usage_intro": "Manages MkDocs documentation sites: initializing new sites with Material theme, adding pages, generating navigation, building, previewing, and deploying to GitHub Pages.",
        "examples": [
            ("Initialize a docs site", "Set up a new MkDocs documentation site with Material theme for this project."),
            ("Add a page", "Add an API Reference page to the docs site."),
            ("Deploy to GitHub Pages", "Build and deploy the documentation to GitHub Pages."),
        ],
    },
    "narrative-audit": {
        "title": "Narrative Coherence Audit",
        "usage_intro": "Audits a project's story for coherence. Ensures that issues, commits, plans, documentation, and changelog all tell a consistent narrative without contradictions or gaps.",
        "examples": [
            ("Full narrative audit", "Audit the project narrative — do our issues, commits, and docs tell a coherent story?"),
            ("Check docs/code alignment", "Verify that the README and docs accurately describe what the code actually does."),
            ("Changelog consistency", "Check if the changelog entries match the actual commits and closed issues."),
        ],
    },
    "plan-preview": {
        "title": "Plan Preview Generator",
        "usage_intro": "Transforms detailed implementation plans into concise, stakeholder-friendly summaries with file change overviews, component listings, and optional flow diagrams. Configurable detail levels.",
        "examples": [
            ("Summarize a plan", "Generate a stakeholder-friendly preview of this implementation plan."),
            ("Low-detail preview", "Create a high-level plan summary — just objective, approach, and file count."),
            ("Detailed preview with diagrams", "Generate a detailed plan preview with flow diagrams and method signatures."),
        ],
    },
    "plan-review-import": {
        "title": "Plan Review Import",
        "usage_intro": "Parses exported PR review comments into structured review format for plan integration. Enables importing external feedback into the planning workflow.",
        "examples": [
            ("Import PR review feedback", "Import the review comments from PR #42 into our plan review format."),
            ("Parse review export", "Parse this exported review comments file into structured review format."),
            ("Integrate feedback into plan", "Import review feedback and merge it into the current implementation plan."),
        ],
    },
    "playwright": {
        "title": "Playwright Browser Automation",
        "usage_intro": "General-purpose browser automation with Playwright. Write and execute custom Playwright code for testing, scraping, visual regression, form interaction, and any browser automation task.",
        "examples": [
            ("Write an E2E test", "Write a Playwright test that logs in, navigates to the dashboard, and verifies the data table loads."),
            ("Scrape a webpage", "Use Playwright to scrape product prices from this page and save them as JSON."),
            ("Visual regression test", "Create a Playwright visual regression test for the homepage."),
        ],
    },
    "playwright-e2e-runner": {
        "title": "Playwright E2E Test Runner",
        "usage_intro": "Runs stable, fast browser E2E test suites with eventual-consistency primitives and CI sharding guidance. Language-agnostic architecture supporting JS/TS, Python, and C# adapters.",
        "examples": [
            ("Set up E2E suite", "Set up a structured Playwright E2E test suite with eventual consistency support for our event-sourced backend."),
            ("Configure CI sharding", "Configure CI to shard our E2E tests across 4 workers with merged reporting."),
            ("Define test flows", "Create suite and flow YAML specs for the checkout workflow."),
        ],
    },
    "playwright-ops": {
        "title": "Playwright Ops (Reusable Browser Operations)",
        "usage_intro": "Builds reusable, composable browser operations for admin workflows, evidence capture, and runbook automation. Supports both CLI macros for quick execution and code adapters for maintainability.",
        "examples": [
            ("Create an admin operation", "Define a reusable browser operation for creating users in the admin panel."),
            ("Evidence capture workflow", "Set up a Playwright operation that captures screenshots and traces for compliance auditing."),
            ("Automate a runbook step", "Convert this manual runbook step into a deterministic browser operation."),
        ],
    },
    "playwright-recorder": {
        "title": "Playwright Recorder (Record & Validate)",
        "usage_intro": "Captures browser navigation as versioned artifacts and validates replay in CI with snapshot-aware checks. Enables record-now, validate-later workflows for UI flow verification.",
        "examples": [
            ("Record a user flow", "Record the login → dashboard → settings flow as a versioned recording bundle."),
            ("Set up CI validation", "Configure CI to replay our recorded flows and flag any structural changes."),
            ("Update a recording", "Re-record the checkout flow since the UI was redesigned."),
        ],
    },
    "postmortem": {
        "title": "Postmortem Analysis",
        "usage_intro": "Enforces a structured postmortem ritual when failures occur. Produces blameless analysis with root cause investigation (5 Whys), timeline reconstruction, and actionable systemic improvements.",
        "examples": [
            ("Run a postmortem", "We had two consecutive test failures during deployment — run a structured postmortem."),
            ("Analyze a production incident", "The API was down for 30 minutes — let's do a postmortem to find the root cause and prevent recurrence."),
            ("Post-rollback analysis", "We had to rollback the last release — do a postmortem to identify what went wrong."),
        ],
    },
    "potential-discovery": {
        "title": "Potential Discovery",
        "usage_intro": "Analyzes incoming content (text, files, folders, URLs) to extract purpose, create extensive summaries, and identify potential value for the current project. Suggests concrete integration opportunities.",
        "examples": [
            ("Analyze a library", "Analyze the ./incoming/result-monad/ library and assess its potential for our project."),
            ("Evaluate a competitor", "Analyze https://github.com/competitor/tool — what can we learn from their approach?"),
            ("Review a spec document", "Analyze this API spec and identify what's useful for our implementation."),
        ],
    },
    "pptx": {
        "title": "PowerPoint Presentation (PPTX)",
        "usage_intro": "Creates, reads, and edits PowerPoint presentations (.pptx) with strong design guidance and mandatory visual QA. Includes curated color palettes, typography rules, and layout patterns.",
        "examples": [
            ("Create a pitch deck", "Create a 10-slide pitch deck for our product with the Midnight Executive color theme."),
            ("Read a presentation", "Extract and summarize the content from quarterly-review.pptx."),
            ("Design a technical talk", "Create slides for a conference talk about event sourcing with diagrams and code samples."),
        ],
    },
    "project-sections": {
        "title": "Project Section Identification",
        "usage_intro": "Analyzes a software project to identify and categorize its logical sections (API, frontend, database, CLI, domain logic). Enables context scoping, architecture documentation, and focused agent work.",
        "examples": [
            ("Map project structure", "Identify and categorize all sections of this project — API, frontend, database, etc."),
            ("Scope to one section", "I want to work only on the API section — identify it and load its context."),
            ("Architecture documentation", "Generate a project sections overview for our architecture docs."),
        ],
    },
    "prove-your-worth": {
        "title": "Feature Justification Audit",
        "usage_intro": "Ruthlessly audits project features for justification. Challenges every feature to prove its value with evidence — researches alternatives, measures usage, and recommends keep/remove/simplify/extract verdicts.",
        "examples": [
            ("Audit all features", "Run a feature justification audit on this project — which features should we keep, remove, or simplify?"),
            ("Challenge a specific module", "Prove that our custom YAML parser is justified — are there better alternatives?"),
            ("Quarterly feature review", "Do a quarterly audit of our feature set and recommend what to cut."),
        ],
    },
    "reality-audit": {
        "title": "Reality Audit",
        "usage_intro": "Performs an aggressive, evidence-based audit to verify that project claims match implementation reality. Acts as an external auditor who trusts nothing without proof.",
        "examples": [
            ("Full reality audit", "Audit this project — does what the README claims match what the code actually does?"),
            ("Feature verification", "Verify which advertised features are actually implemented, tested, and working."),
            ("Documentation accuracy check", "Check if our docs accurately describe the current state of the application."),
        ],
    },
    "research": {
        "title": "Deep Topic Research",
        "usage_intro": "Conducts deep topic research with structured output. Supports quick, deep, and comparative research modes for investigating technologies, patterns, libraries, or any topic requiring investigation.",
        "examples": [
            ("Research a technology", "Do a deep research on CQRS + Event Sourcing patterns for Python applications."),
            ("Compare alternatives", "Compare FastAPI vs Litestar vs Starlette for our API backend — comparative research."),
            ("Quick investigation", "Quick research: what are the current best practices for Python dependency management?"),
        ],
    },
    "review-response": {
        "title": "Code Review Response",
        "usage_intro": "Handles receiving and responding to code review feedback. Verifies suggestions before implementing, pushes back with reasoning when appropriate, and avoids performative agreement.",
        "examples": [
            ("Respond to review feedback", "Process the review comments on this PR and implement the agreed changes."),
            ("Push back on a suggestion", "The reviewer suggested using a singleton here, but I think it's wrong — help me articulate why."),
            ("Implement review fixes", "Go through each review comment, verify the suggestion is correct, and implement the fixes."),
        ],
    },
    "shadow-plan": {
        "title": "Shadow Plan (Alternative Plan Generator)",
        "usage_intro": "Generates an alternative plan that deliberately disagrees with the primary plan to expose blind spots. Forces consideration of different architectures, tradeoffs, and approaches.",
        "examples": [
            ("Generate an alternative plan", "Here's our plan for the new auth system — create a shadow plan that takes a completely different approach."),
            ("Challenge assumptions", "This plan assumes a monolithic architecture — generate a shadow plan that challenges that assumption."),
            ("Expose blind spots", "Create an alternative plan for the migration — what are we not seeing?"),
        ],
    },
    "temporal-risk": {
        "title": "Temporal Risk Analysis",
        "usage_intro": "Analyzes how current changes might fail or become liabilities over 3, 6, and 12 month horizons. Identifies time-delayed risks that don't show up in code review.",
        "examples": [
            ("Analyze time-delayed risks", "What risks could this architectural decision create in 3, 6, and 12 months?"),
            ("Dependency risk assessment", "Analyze the temporal risk of our current dependency choices — what might break over time?"),
            ("Feature longevity analysis", "Will this feature implementation still be viable in 12 months given industry trends?"),
        ],
    },
    "versioning": {
        "title": "Versioning & Release Management",
        "usage_intro": "Manages semantic versioning, generates changelogs from completed issues or git history, and coordinates releases. Supports conventional commits, multiple input sources, and release notes generation.",
        "examples": [
            ("Bump version", "Bump the minor version and generate changelog entries from completed issues."),
            ("Generate release notes", "Generate user-friendly release notes for the latest version."),
            ("Changelog from git", "Generate a changelog from git commits between main and the current branch."),
        ],
    },
    "web-artifacts": {
        "title": "Web Artifacts Builder",
        "usage_intro": "Builds interactive single-page web artifacts using React, TypeScript, Tailwind CSS, and shadcn/ui. Bundles everything into self-contained HTML files for demos, prototypes, and tools.",
        "examples": [
            ("Build an interactive demo", "Create a self-contained HTML demo of the new dashboard design."),
            ("Create a calculator tool", "Build a mortgage calculator as a single-file web artifact."),
            ("Prototype a landing page", "Create a complete landing page prototype bundled into one HTML file."),
        ],
    },
    "web-assets": {
        "title": "Web Asset Generator",
        "usage_intro": "Generates production-ready web assets from logos, text, or emojis — including favicons, app icons, PWA manifest, Open Graph images, and Twitter card images.",
        "examples": [
            ("Generate favicons", "Generate a complete favicon set from our logo.png file."),
            ("Create social media images", "Generate Open Graph and Twitter Card images for our marketing site."),
            ("Emoji-based branding", "Generate all web assets using the 🚀 emoji as the icon source."),
        ],
    },
    "youtube-transcript": {
        "title": "YouTube Transcript Extraction",
        "usage_intro": "Extracts transcripts from YouTube videos for research and documentation. Uses a tiered approach: manual subtitles first, then auto-generated, then Whisper transcription as fallback.",
        "examples": [
            ("Extract a video transcript", "Extract the transcript from this YouTube conference talk: https://youtube.com/watch?v=example"),
            ("Research from video", "Get the transcript from this tutorial video and create a summary of the key points."),
            ("Batch extraction", "Extract transcripts from these 3 YouTube videos for our research project."),
        ],
    },
}


def parse_frontmatter(content: str):
    """Parse YAML frontmatter and return (frontmatter_text, body)."""
    if not content.startswith("---"):
        return "", content
    end = content.find("---", 3)
    if end == -1:
        return "", content
    return content[3:end].strip(), content[end + 3:].lstrip("\n")


def extract_fm_field(fm: str, field: str) -> str:
    """Extract a single field value from frontmatter text."""
    for line in fm.split("\n"):
        stripped = line.strip()
        if stripped.startswith(f"{field}:"):
            val = stripped[len(field) + 1:].strip().strip('"').strip("'")
            return val
    return ""


def extract_source(fm: str) -> str:
    """Extract source URL from frontmatter."""
    return extract_fm_field(fm, "source")


def remove_fm_fields(fm: str, fields_to_remove: set) -> str:
    """Remove specified fields from frontmatter text."""
    lines = fm.split("\n")
    result = []
    skip_block = False
    skip_indent = 0

    for line in lines:
        stripped = line.strip()
        field_name = stripped.split(":")[0].strip() if ":" in stripped else ""

        # Check if this line starts a field to remove
        if field_name in fields_to_remove and ":" in stripped:
            # Check if it's a block (array/object) vs inline
            value_part = stripped[len(field_name) + 1:].strip()
            if value_part.startswith("[") or value_part == "" or not value_part:
                # Inline array or empty (could be block)
                if not value_part or (value_part.startswith("[") and "]" in value_part):
                    continue  # Single line, skip
                else:
                    skip_block = True
                    skip_indent = len(line) - len(line.lstrip())
                    continue
            else:
                continue  # Single value line

        if skip_block:
            current_indent = len(line) - len(line.lstrip()) if stripped else skip_indent + 2
            if current_indent > skip_indent or not stripped:
                continue
            else:
                skip_block = False

        result.append(line)

    return "\n".join(result)


def ensure_category(fm: str, folder_name: str) -> str:
    """Ensure category field exists, and override generic categories with specific ones."""
    # Canonical category assignments — overrides existing generic categories too
    category_overrides = {
        # analysis
        "adversary": "analysis", "cognitive-load": "analysis",
        "context-map": "analysis", "improvement-discovery": "analysis",
        "junior-explain": "analysis", "narrative-audit": "analysis",
        "postmortem": "analysis", "potential-discovery": "analysis",
        "project-sections": "analysis", "prove-your-worth": "analysis",
        "reality-audit": "analysis", "shadow-plan": "analysis",
        "temporal-risk": "analysis", "article-verification": "analysis",
        # planning
        "plan-preview": "planning", "plan-review-import": "planning",
        # git
        "git": "git", "git-analysis": "git", "git-story": "git",
        "git-worktree": "git", "gh-pr-info": "git",
        # docs
        "astro-docs": "docs", "mkdocs": "docs", "versioning": "docs",
        # document-generation
        "docx": "document-generation", "pptx": "document-generation",
        # frontend
        "frontend-design": "frontend", "web-artifacts": "frontend",
        "web-assets": "frontend", "mermaid": "frontend",
        # testing
        "gherkin-architecture": "testing", "gherkin-playwright": "testing",
        "gherkin-review": "testing", "gherkin-step-generator": "testing",
        "gherkin-ui-alignment": "testing", "gherkin-ui-vocabulary": "testing",
        "playwright": "testing", "playwright-e2e-runner": "testing",
        "playwright-ops": "testing", "playwright-recorder": "testing",
        "agent-browser": "testing",
        # research
        "research": "research", "youtube-transcript": "research",
        # utility
        "debugging": "utility", "interview": "utility",
        "markdown-jira": "utility", "gh-actionable-comments": "utility",
        "review-response": "utility",
    }

    target_cat = category_overrides.get(folder_name)
    current_cat = extract_fm_field(fm, "category")

    if target_cat and current_cat and current_cat != target_cat:
        # Replace existing category with the correct one
        lines = fm.split("\n")
        result = []
        for line in lines:
            if line.strip().startswith("category:"):
                result.append(f"category: {target_cat}")
            else:
                result.append(line)
        return "\n".join(result)
    elif target_cat and not current_cat:
        # Add category
        lines = fm.split("\n")
        result = []
        inserted = False
        for line in lines:
            result.append(line)
            if not inserted and line.strip().startswith("description:"):
                result.append(f"category: {target_cat}")
                inserted = True
        if not inserted:
            result.append(f"category: {target_cat}")
        return "\n".join(result)
    elif not current_cat:
        # Fallback for unknown skills
        lines = fm.split("\n")
        result = []
        inserted = False
        for line in lines:
            result.append(line)
            if not inserted and line.strip().startswith("description:"):
                result.append("category: utility")
                inserted = True
        if not inserted:
            result.append("category: utility")
        return "\n".join(result)

    return fm


def generate_usage_md(folder_name: str, fm: str) -> str:
    """Generate usage.md content for a skill."""
    data = SKILL_DATA.get(folder_name, {})
    name = extract_fm_field(fm, "name") or folder_name
    description = extract_fm_field(fm, "description") or ""
    source = extract_source(fm)
    title = data.get("title", name.replace("-", " ").title())
    intro = data.get("usage_intro", description)
    examples = data.get("examples", [])

    lines = [f"# {title}", "", intro, ""]

    if examples:
        lines.append("## Usage Examples")
        lines.append("")
        for i, (label, prompt) in enumerate(examples, 1):
            lines.append(f"### {label}")
            lines.append("")
            lines.append(f"```")
            lines.append(prompt)
            lines.append(f"```")
            lines.append("")

    if source:
        lines.append("## Credits")
        lines.append("")
        lines.append(f"Based on: [{source}]({source})")
        lines.append("")

    lines.append("## Reference")
    lines.append("")
    lines.append(f"See [SKILL.md](SKILL.md) for the full technical specification.")
    lines.append("")

    return "\n".join(lines)


def generate_index_md(skills_by_category: dict) -> str:
    """Generate index.md content grouped by category."""
    # Category display names and order
    category_order = [
        ("analysis", "Analysis & Review"),
        ("planning", "Planning"),
        ("git", "Git & Version Control"),
        ("docs", "Documentation"),
        ("document-generation", "Document Generation"),
        ("frontend", "Frontend & Design"),
        ("testing", "Testing & Browser Automation"),
        ("research", "Research"),
        ("utility", "Utility"),
        ("extended", "Extended"),
        ("core", "Core"),
    ]

    lines = [
        "# Skills Index",
        "",
        "A curated collection of AI agent skills for software engineering workflows.",
        "",
        "## Overview",
        "",
    ]

    # Build overview table
    lines.append("| Category | Skills |")
    lines.append("|----------|--------|")
    for cat_key, cat_label in category_order:
        if cat_key in skills_by_category:
            count = len(skills_by_category[cat_key])
            lines.append(f"| [{cat_label}](#{cat_key.replace(' ', '-')}) | {count} |")
    # Catch any categories not in the order list
    for cat_key in sorted(skills_by_category.keys()):
        if cat_key not in dict(category_order):
            cat_label = cat_key.replace("-", " ").title()
            count = len(skills_by_category[cat_key])
            lines.append(f"| [{cat_label}](#{cat_key}) | {count} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Generate sections
    for cat_key, cat_label in category_order:
        if cat_key not in skills_by_category:
            continue

        lines.append(f"## {cat_label}")
        lines.append("")

        skills = sorted(skills_by_category[cat_key], key=lambda s: s["folder"])

        for skill in skills:
            name = skill["name"]
            desc = skill["description"]
            folder = skill["folder"]
            source = skill.get("source", "")

            lines.append(f"### {name}")
            lines.append("")
            lines.append(f"> {desc}")
            lines.append("")
            lines.append(f"- **Skill**: [{folder}/SKILL.md]({folder}/SKILL.md)")
            lines.append(f"- **Usage**: [{folder}/usage.md]({folder}/usage.md)")
            if source:
                lines.append(f"- **Source**: [{source}]({source})")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Catch uncategorized
    for cat_key in sorted(skills_by_category.keys()):
        if cat_key not in dict(category_order):
            cat_label = cat_key.replace("-", " ").title()
            lines.append(f"## {cat_label}")
            lines.append("")
            skills = sorted(skills_by_category[cat_key], key=lambda s: s["folder"])
            for skill in skills:
                name = skill["name"]
                desc = skill["description"]
                folder = skill["folder"]
                source = skill.get("source", "")
                lines.append(f"### {name}")
                lines.append("")
                lines.append(f"> {desc}")
                lines.append("")
                lines.append(f"- **Skill**: [{folder}/SKILL.md]({folder}/SKILL.md)")
                lines.append(f"- **Usage**: [{folder}/usage.md]({folder}/usage.md)")
                if source:
                    lines.append(f"- **Source**: [{source}]({source})")
                lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def main():
    fields_to_remove = {"tier", "invokes", "invoked_by"}
    skills_by_category = defaultdict(list)

    print("=== Processing skills ===\n")

    for d in sorted(SKILLS_DIR.iterdir()):
        if not d.is_dir() or d.name in SKIP_DIRS:
            continue

        skill_file = d / "SKILL.md"
        if not skill_file.exists():
            continue

        folder_name = d.name
        content = skill_file.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(content)

        if not fm:
            print(f"  SKIP (no frontmatter): {folder_name}")
            continue

        # 1. Remove tier, invokes, invoked_by from frontmatter
        fm = remove_fm_fields(fm, fields_to_remove)

        # 2. Ensure category exists
        fm = ensure_category(fm, folder_name)

        # 3. Write updated SKILL.md
        new_content = f"---\n{fm}\n---\n{body}"
        skill_file.write_text(new_content, encoding="utf-8")

        # 4. Generate usage.md
        usage_content = generate_usage_md(folder_name, fm)
        usage_file = d / "usage.md"
        usage_file.write_text(usage_content, encoding="utf-8")

        # 5. Collect data for index
        name = extract_fm_field(fm, "name") or folder_name
        description = extract_fm_field(fm, "description") or ""
        category = extract_fm_field(fm, "category") or "utility"
        source = extract_fm_field(fm, "source") or ""

        # Get display name
        title = SKILL_DATA.get(folder_name, {}).get("title", name.replace("-", " ").title())

        skills_by_category[category].append({
            "folder": folder_name,
            "name": title,
            "description": description,
            "source": source,
        })

        print(f"  ✓ {folder_name} (category: {category})")

    # 6. Generate index.md
    print("\n=== Generating index.md ===\n")
    index_content = generate_index_md(skills_by_category)
    index_file = SKILLS_DIR / "index.md"
    index_file.write_text(index_content, encoding="utf-8")
    print(f"  ✓ index.md ({sum(len(v) for v in skills_by_category.values())} skills)")

    print("\n=== Done ===")


if __name__ == "__main__":
    main()
