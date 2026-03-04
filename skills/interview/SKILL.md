---
name: interview
title: Structured Interview
description: "Conduct structured interviews with the user. Use when multiple decisions need user input: ask ONE question at a time, wait for response, record answer, then proceed to next question."
category: planning
---
# Interview workflow

## Purpose

Gather user decisions, preferences, or clarifications through a structured one-question-at-a-time process. This prevents overwhelming the user and ensures each answer is properly understood before moving on.

## Rules (strict)

1. **One question per message.** Never batch multiple questions.
2. **Present clear options.** Each question should have labeled options (A, B, C) or a clear format for the expected answer.
3. **Explain briefly.** Give just enough context for the user to decide—not a wall of text.
4. **Record immediately.** After each answer, note it in `project docs` or a working document before asking the next question.
5. **Allow escape.** User can say "skip", "defer", "use your recommendation", or "stop interview".
6. **Summarize at end.** When all questions are answered, present a summary for confirmation.

## Interview state tracking

Track in `project docs` under "Doing now":

```markdown
## Doing now

Interview: [topic]
- Q1: [question summary] → [answer or pending]
- Q2: [question summary] → [answer or pending]
- ...
```

## Procedure

1. **Setup**: List all questions internally (do not show to user yet).
2. **Ask Q1**: Present one question with options.
3. **Wait**: Do not proceed until user responds.
4. **Record**: Update the working document with the answer.
5. **Ask Q2**: Repeat until all questions answered or user stops.
6. **Summarize**: Present all answers for confirmation.
7. **Proceed**: Use confirmed answers to continue the workflow.

## Handling special responses

| User says | Action |
|-----------|--------|
| "skip" | Mark as SKIPPED, move to next question |
| "defer" | Mark as DEFERRED, move to next question |
| "use your recommendation" | Apply the agent's recommended default, note it |
| "stop" / "pause" | End interview, save progress, can resume later |
| "go back" | Re-ask the previous question |
| unclear answer | Ask a brief clarifying follow-up (still counts as same question) |

## Question Quality Standards

### Good Questions

- **Specific to context** — Reference project details, not generic templates
- **Reveal non-obvious decisions** — Probe tradeoffs and implications
- **Uncover edge cases** — "What happens when X fails?"
- **Challenge assumptions gently** — "You mentioned X; does that mean Y?"
- **Build on previous answers** — Show you listened

### Bad Questions (avoid)

- ❌ Too obvious: "What programming language will you use?"
- ❌ Too generic: "Do you need a database?"
- ❌ Trivial: "What color should the button be?"
- ❌ Already answered: Re-asking what user just said
- ❌ Assumptive: Leading questions that presume an answer

### Multi-Option Format

When presenting choices, use **label + description**:

```markdown
**Q3: How should the system handle conflicting edits?**

A) **Last-write-wins** — Simple, but may lose data. Best for low-conflict scenarios.
B) **Optimistic locking** — Detect conflicts, prompt user to resolve. More complex.
C) **CRDT-based merge** — Automatic conflict resolution. Best for real-time collab.
D) **Manual review queue** — Flag conflicts for human review. Best for critical data.
```

This format helps users make informed decisions without lengthy explanations.

### Alternative Generation Phase (optional)

*Inspired by [brainstorming patterns](https://skills.sh/obra/superpowers/brainstorming)*

When asking about **design decisions**, consider generating alternatives before presenting options:

**When to Apply**:
- Architecture choices (monolith vs microservices, sync vs async)
- API design decisions (REST vs GraphQL, versioning strategy)
- Data modeling choices (schema design, storage selection)
- Workflow decisions (manual vs automated, synchronous vs eventual)

**Generation Techniques**:

| Technique | Process | Example |
|-----------|---------|---------|
| **Divergent listing** | List 5-7 options without judging | "For auth: JWT, sessions, OAuth, API keys, mTLS, custom tokens, hybrid" |
| **SCAMPER** | Substitute, Combine, Adapt, Modify, Eliminate, Reverse | "What if we combined sessions + JWT?" |
| **Opposite thinking** | "What if we did the exact opposite?" | "Instead of caching, what if we never cache?" |
| **Constraint relaxation** | Remove one limitation | "If latency didn't matter, what would we do?" |

**Procedure**:
1. Identify that question involves a design decision
2. Generate 5-7 options using techniques above (internal, don't show all)
3. Analyze trade-offs briefly
4. Present top 3-4 options with pros/cons
5. Ask user to choose or suggest alternatives

**Example**:

Instead of asking:
> "Should we use REST or GraphQL?"

Generate alternatives first:
- REST, GraphQL, gRPC, WebSockets, custom binary, tRPC, JSON-RPC

Then present refined options:
> **Q4: Which API style fits this project?**
>
> A) **REST** — Simple, cacheable, broad tooling. Best for CRUD-heavy APIs.
> B) **GraphQL** — Flexible queries, single endpoint. Best for complex data needs.
> C) **gRPC** — High performance, typed contracts. Best for internal services.
> D) **Something else?** — If you have another preference in mind.

**Skip When**:
- Question is about preferences, not design ("What's your timezone?")
- Options are inherently limited ("Enable feature X? Yes/No")
- User has already expressed a strong preference

## Multiple Choice Support (NEW - Enhanced Interview Format)

### Multiple Choice Question Types

**Type 1: Numbered Options (A, B, C, D)**

```
Q1: Which programming language do you prefer for the API backend?

A) Python
B) JavaScript/TypeScript
C) Rust
D) Go

E) Other (please specify): [______]
```

**Type 2: Radio Button Style (Single Select)**

```
Q2: Which database system should we use?

○ PostgreSQL
○ MySQL
○ MongoDB
○ SQLite
○ Other (please specify): [______]
```

**Type 3: Checkbox Style (Multiple Select)**

```
Q3: Which authentication methods should we support?

☑ JWT (JSON Web Tokens)
☑ OAuth2.0
☑ Session-based auth
☑ API keys
☑ Other (please specify): [______]
```

### Multiple Choice Guidelines

**When to Use Multiple Choice:**
- Options are well-defined and limited (3-6 options)
- User needs to choose from predefined set
- Custom "Other" option available for unlisted choices
- Decision is categorical, not open-ended

**When to Use Open-Ended:**
- Complex answers need elaboration
- User's input is unique and can't be predicted
- Information gathering (free-form text)
- Clarifying follow-up questions

**Multiple Choice Format:**

```
Q{N}: {Clear question text}

Options:
A) {Option label}: {Brief description}
B) {Option label}: {Brief description}
C) {Option label}: {Brief description}
D) {Option label}: {Brief description}

E) Other (please specify): [______]

Your choice (A/B/C/D/E or type "other: {value}"):
```

**Validation Rules:**
- Require explicit selection (A, B, C, D, or E)
- If "Other" selected, require specification
- Allow "skip" or "defer" like any other question
- Record user's exact choice as provided

### Enhanced Interview Procedure

**1. Setup:**
   - List all questions internally
   - Mark which are multiple choice vs open-ended

**2. Ask Q1:**
   - If multiple choice: Present with labeled options (A, B, C, D, E)
   - If open-ended: Ask question with clear format
   - Include "Other (please specify)" option when applicable

**3. Wait:**
   - Do not proceed until user responds
   - Accept: Letter (A-E), number, or "other: {value}"

**4. Record:**
   - Record user's exact choice
   - If "Other" selected, record the custom value

**5. Ask Q2+:**
   - Repeat for all questions
   - Build on previous answers if relevant

**6. Summarize:**
   - Present all choices for confirmation
   - Highlight any "Other" selections with custom values

### Template Enhancement

**For multiple choice questions in templates:**

```
## Question {N}

**Question**: {Question text}

**Type**: Multiple Choice

**Options**:
- A) {Label}: {Description}
- B) {Label}: {Description}
- C) {Label}: {Description}
- D) {Label}: {Description}

**Other Option**: Yes/No
- If Yes: "Other (please specify): [______]"

**Expected Answer**: {What you're looking for}
```

### Example: Multiple Choice Interview

```
Q1: Which issue tracking system should we use?

A) GitHub Issues
   - Native to GitHub, good for open source
   - Simple and familiar to most developers
   - Free public projects

B) Linear
   - Great UI, excellent keyboard workflow
   - Good for both personal and team use
   - Free tier available

C) Jira
   - Enterprise features, customizable workflows
   - Good for large teams
   - More complex setup

D) Azure Boards
   - Integrated with Azure DevOps
   - Good for Microsoft stack
   - Requires Azure subscription

E) Other (please specify): [______]

Your choice (A/B/C/D/E or type "other: {value}"):
```

### Integration Notes

- Multiple choice questions speed up interviews significantly
- Clearer options reduce decision fatigue
- "Other" option maintains flexibility for unlisted choices
- Use multiple choice for: preferences, configurations, decisions between known options
- Use open-ended for: elaboration, unique situations, information gathering

---

## YAGNI During Interviews

When interviewing for requirements or design decisions, apply YAGNI ("You Aren't Gonna Need It") to prevent over-engineering.

### Ask YAGNI Questions

When user suggests features or requirements:

1. "Do we need this right now, or can it be added later?"
2. "What's the simplest way to solve this?"
3. "What if we didn't include this - what breaks?"

### Push Back on Hypotheticals

If user says "we might need" or "someday":
- "Can we defer that until it's actually needed?"
- "Let's solve the current problem first"
- "We can add that in a follow-up issue"

### Example Interview Flow

```
User: "We need a plugin architecture so we can extend it later"

Agent (YAGNI check): "What extensions do you need today?"

User: "Well, nothing right now, but maybe in the future..."

Agent: "Let's hardcode for now. When you have a real extension
need, we can add plugin architecture. What's the actual
feature you need today?"
```

### YAGNI Checklist for Requirements

For each requirement discussed:
- [ ] Needed for current requirement?
- [ ] Solves a real (not hypothetical) problem?
- [ ] Can be added later without major refactoring?
- [ ] Simplest possible solution?

If any answer is NO, challenge the requirement.

---
