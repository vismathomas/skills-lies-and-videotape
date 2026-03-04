<p align="center">
  <img src="assets/images/logo.png" alt="Skills, Lies and Videotape" width="400">
</p>

# Skills, Lies and Videotape

A curated collection of **48 AI agent skills** for software engineering workflows, organized across **8 categories**.

**[Browse the documentation site →](https://vismathomas.github.io/skills-lies-and-videotape/)**

## Categories

| Category | Skills | Description |
|----------|--------|-------------|
| [Analysis & Review](skills/#analysis) | 6 | Audit, review, and analyze code and projects |
| [Planning](skills/#planning) | 5 | Plan, preview, and structure implementation work |
| [Git & Version Control](skills/#git) | 6 | Git operations, analysis, and history management |
| [Frontend & Design](skills/#frontend) | 4 | UI design, web assets, and visual tooling |
| [Testing & Browser Automation](skills/#testing) | 11 | Browser automation, E2E testing, and BDD/Gherkin |
| [Utility](skills/#utility) | 4 | General-purpose utility skills |
| [Documentation](skills/#documentation) | 5 | Documentation sites, document generation, and release management |
| [Review](skills/#review) | 7 | Code review, auditing, and verification |

## All Skills

| Skill | Category | Description |
|-------|----------|-------------|
| [Adversarial Code Review](skills/adversary/) | Review | Adversarial code reviewer that assumes implementation is wrong and tries to break it |
| [Agent Browser CLI](skills/agent-browser/) | Testing | Declarative browser automation via Vercel agent-browser CLI |
| [Article Verification](skills/article-verification/) | Review | Systematically deconstruct written content into verifiable claims |
| [Astro Documentation Sites](skills/astro-docs/) | Documentation | Scaffold and maintain Astro-based documentation sites |
| [Cognitive Load Tracker](skills/cognitive-load/) | Review | Track and budget cognitive complexity introduced by changes |
| [Context Map Generator](skills/context-map/) | Analysis | Analyze the codebase to create a concise, LLM-optimized structured overview |
| [Systematic Debugging](skills/debugging/) | Utility | Systematic debugging approaches for isolating and fixing software defects |
| [Word Document Generation](skills/docx/) | Documentation | Create, read, and edit Word documents (.docx) |
| [Frontend Design](skills/frontend-design/) | Frontend | Create distinctive, production-grade frontend interfaces |
| [GitHub PR Actionable Comments](skills/gh-actionable-comments/) | Git | Analyze PR review comments using gh CLI to identify actionable items |
| [GitHub Pull-Request Info](skills/gh-pr-info/) | Git | Extract comprehensive information from a GitHub pull request using gh CLI |
| [Gherkin Architecture & Suite Design](skills/gherkin-architecture/) | Testing | Architecture primer for structuring large Gherkin/BDD test suites |
| [Gherkin Playwright Integration](skills/gherkin-playwright/) | Testing | Integrate Gherkin/BDD feature files with Playwright browser automation |
| [Gherkin Feature File Review](skills/gherkin-review/) | Testing | Review and lint Gherkin feature files for quality and consistency |
| [Gherkin Step Definition Generator](skills/gherkin-step-generator/) | Testing | Generate ReqnRoll step definition classes from Gherkin feature files |
| [Gherkin UI Alignment Validation](skills/gherkin-ui-alignment/) | Testing | Validate alignment between Gherkin feature files and frontend |
| [Gherkin UI Vocabulary Library](skills/gherkin-ui-vocabulary/) | Testing | Controlled vocabulary of UI interaction steps with helper function signatures |
| [Safe Git Operations](skills/git/) | Git | Manage git operations safely with stale state detection |
| [Git Repository Analysis](skills/git-analysis/) | Git | Analyze git repository for insights: contributor stats, commit patterns |
| [Git Story Generator](skills/git-story/) | Git | Generate narrative summaries from git history |
| [Git Worktree Management](skills/git-worktree/) | Git | Manage git worktrees for isolated development |
| [Improvement Discovery](skills/improvement-discovery/) | Analysis | Discover improvement opportunities in projects |
| [Structured Interview](skills/interview/) | Planning | Conduct structured interviews with the user |
| [Junior-Level Explanations](skills/junior-explain/) | Planning | Translate complex plans into junior-level explanations |
| [Markdown to Jira Conversion](skills/markdown-jira/) | Utility | Convert standard markdown syntax into Jira-compatible wiki markup |
| [GitHub-Safe Mermaid Diagrams](skills/mermaid/) | Frontend | GitHub-safe Mermaid diagram authoring rules |
| [MkDocs Site Management](skills/mkdocs/) | Documentation | MkDocs documentation site management |
| [Narrative Coherence Audit](skills/narrative-audit/) | Review | Audit the project's story for coherence |
| [Plan Preview Generator](skills/plan-preview/) | Planning | Transform implementation plans into stakeholder-friendly summaries |
| [Plan Review Import](skills/plan-review-import/) | Planning | Parse exported PR review comments into structured review format |
| [Playwright Browser Automation](skills/playwright/) | Testing | Browser automation with Playwright |
| [Playwright E2E Test Runner](skills/playwright-e2e-runner/) | Testing | High-throughput Playwright E2E execution |
| [Playwright Reusable Operations](skills/playwright-ops/) | Testing | Reusable, composable browser operations |
| [Playwright Recorder](skills/playwright-recorder/) | Testing | Record browser navigation as versioned artifacts |
| [Postmortem Analysis](skills/postmortem/) | Analysis | Structured postmortem ritual for failures |
| [Potential Discovery](skills/potential-discovery/) | Analysis | Analyze incoming content to extract purpose and create actionable items |
| [PowerPoint Presentation Generation](skills/pptx/) | Documentation | Create, read, and edit PowerPoint presentations (.pptx) |
| [Project Section Identification](skills/project-sections/) | Analysis | Identify and map different sections of a software project |
| [Feature Justification Audit](skills/prove-your-worth/) | Review | Ruthlessly audit project features for justification |
| [Reality Audit](skills/reality-audit/) | Review | Evidence-based audit to verify project claims match implementation |
| [Deep Topic Research](skills/research/) | Utility | Deep topic research with optional issue creation from findings |
| [Code Review Response](skills/review-response/) | Review | Receive and respond to code review feedback |
| [Shadow Plan Generator](skills/shadow-plan/) | Planning | Generate an alternative plan that deliberately disagrees with the primary plan |
| [Temporal Risk Analysis](skills/temporal-risk/) | Analysis | Analyze how current changes might fail in 3, 6, or 12 months |
| [Versioning & Release Management](skills/versioning/) | Documentation | Manage semantic versioning, changelog generation, and release notes |
| [Web Artifacts Builder](skills/web-artifacts/) | Frontend | Build interactive single-page web artifacts |
| [Web Asset Generator](skills/web-assets/) | Frontend | Generate favicons, app icons, PWA manifest, and social media images |
| [YouTube Transcript Extraction](skills/youtube-transcript/) | Utility | Extract transcripts from YouTube videos |

## Development

### Prerequisites

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/)

### Build the docs site

```bash
uv sync                               # install dependencies
uv run scripts/build_docs.py          # generate docs + update nav
uv run scripts/build_docs.py --serve  # generate + launch dev server
uv run scripts/build_docs.py --build  # generate + build static site
```