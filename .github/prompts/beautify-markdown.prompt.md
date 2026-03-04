---
description: "Beautify plain Markdown for professional GitHub documentation"
tags: [markdown, documentation, formatting, github, enterprise]
---

# Prompt: Beautify Markdown for Professional GitHub Presentation

## Objective
Transform a **plain Markdown text block** into **polished, visually structured Markdown** optimized for **GitHub rendering**.  
The result must look **professional**, **balanced**, and **corporate-ready** — not flashy or emoji-heavy.

---

## Formatting Rules

1. **Headings**
   - Use proper heading hierarchy (`#`, `##`, `###`) with clear titles.
   - Add horizontal rules (`---`) to separate major sections.
   - Avoid decorative or all-caps titles.

2. **Text Emphasis**
   - Use `**bold**` for key terms and `*italic*` for secondary emphasis.
   - Avoid redundant styling or mixed emphasis.

3. **Lists**
   - Use unordered (`-`) and ordered (`1.`) lists for clarity.
   - Nest lists correctly for hierarchical structure.
   - Use checkboxes (`- [ ]`, `- [x]`) only when documenting tasks or states.

4. **Code & Technical Content**
   - Wrap inline code with backticks `` `like this` ``.
   - Use fenced code blocks with language identifiers:
     ```python
     def example():
         pass
     ```
   - Prefer concise examples over long dumps.

5. **Tables**
   - Use tables for structured data when helpful.
     ```markdown
     | Field | Type | Description |
     |--------|------|-------------|
     | id     | int  | Unique identifier |
     ```

6. **Blockquotes**
   - Use for definitions, key takeaways, or referenced material.
     ```markdown
     > Key insight: Consistency improves readability.
     ```

7. **Links and References**
   - Always use `[descriptive text](url)` syntax.
   - For internal documentation, use relative links (`../path/file.md`).

8. **Images and Diagrams**
   - Use `![Alt text](path/to/image.png)` with meaningful alt text.
   - Use Mermaid diagrams for system or flow representations:
     ```mermaid
     graph TD
         A[Input] --> B[Processing]
         B --> C[Output]
     ```

9. **Callouts (GitHub-supported)**
   - Use [GitHub-flavored callouts](https://github.blog/changelog/2022-10-31-markdown-supports-footnotes-alerts/) for emphasis:
     ```markdown
     > [!NOTE]
     > This section describes deployment prerequisites.
     ```

10. **Footnotes**
    - Use for references and sources, not inline explanations:
      ```markdown
      Some statement that needs a reference.[^1]
      [^1]: Reference or link here.
      ```

---

## Output Requirements

- Produce **clean**, **lint-compliant** Markdown (`markdownlint`-friendly).
- Maintain **consistent spacing** and **indentation**.
- Use **semantic** structuring—headings and lists should mirror logical sections.
- Remove unnecessary blank lines or decorative syntax.
- Never use emojis or ASCII art.

---

## Example Input
```markdown
title: System overview
this document shows the main components and how they connect.
we have three main modules, user, api and storage.
```