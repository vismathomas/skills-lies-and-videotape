---
title: PowerPoint Presentation Generation
description: "Create, read, and edit PowerPoint presentations (.pptx). Use when producing slide decks, pitch decks, or any presentation with design guidance and mandatory visual QA."
---

# PowerPoint Presentation Generation

> Create, read, and edit PowerPoint presentations (.pptx). Use when producing slide decks, pitch decks, or any presentation with design guidance and mandatory visual QA.

:material-tag: `documentation` · :material-github: [https://github.com/anthropics/skills/tree/main/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/pptx/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/pptx/SKILL.md){ .md-button .md-button--primary }

---

Creates, reads, and edits PowerPoint presentations (.pptx) with strong design guidance and mandatory visual QA. Includes curated color palettes, typography rules, and layout patterns.

## Usage Examples

### Create a pitch deck

```
Create a 10-slide pitch deck for our product with the Midnight Executive color theme.
```

### Read a presentation

```
Extract and summarize the content from quarterly-review.pptx.
```

### Design a technical talk

```
Create slides for a conference talk about event sourcing with diagrams and code samples.
```

## Credits

Based on: [https://github.com/anthropics/skills/tree/main/skills/pptx](https://github.com/anthropics/skills/tree/main/skills/pptx)

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # PPTX Skill
    
    ## When to Use
    
    - Creating slide decks, pitch decks, or presentations
    - Reading, parsing, or extracting text from `.pptx` files
    - Editing or updating existing presentations
    - Working with templates, layouts, speaker notes, or comments
    - Any mention of "deck", "slides", "presentation", or `.pptx` filename
    
    ## Quick Reference
    
    | Task | Approach |
    |------|----------|
    | Read/analyze content | `pip install "markitdown[pptx]"` then `python -m markitdown presentation.pptx` |
    | Create from scratch | Use `pptxgenjs` — see below |
    | Edit from template | Unpack ZIP → manipulate slides → repack |
    
    ## Dependencies
    
    - `pip install "markitdown[pptx]"` — text extraction
    - `pip install Pillow` — thumbnail grids
    - `npm install -g pptxgenjs` — creating from scratch
    - LibreOffice (`soffice`) — PDF conversion (optional)
    - Poppler (`pdftoppm`) — PDF to images (optional)
    
    ## Reading Content
    
    ```bash
    python -m markitdown presentation.pptx
    ```
    
    ## Creating from Scratch
    
    Use `pptxgenjs` when no template or reference presentation is available. Install: `npm install -g pptxgenjs`.
    
    ## Design Ideas
    
    **Don't create boring slides.** Plain bullets on a white background won't impress anyone.
    
    ### Before Starting
    
    - **Pick a bold, content-informed color palette**: The palette should feel designed for THIS topic. If swapping your colors into a different presentation would still "work," you haven't made specific enough choices.
    - **Dominance over equality**: One color should dominate (60-70% visual weight), with 1-2 supporting tones and one sharp accent. Never give all colors equal weight.
    - **Dark/light contrast**: Dark backgrounds for title + conclusion slides, light for content ("sandwich" structure). Or commit to dark throughout for a premium feel.
    - **Commit to a visual motif**: Pick ONE distinctive element and repeat it — rounded image frames, icons in colored circles, thick single-side borders. Carry it across every slide.
    
    ### Color Palettes
    
    Choose colors that match your topic — don't default to generic blue:
    
    | Theme | Primary | Secondary | Accent |
    |-------|---------|-----------|--------|
    | **Midnight Executive** | `1E2761` (navy) | `CADCFC` (ice blue) | `FFFFFF` (white) |
    | **Forest & Moss** | `2C5F2D` (forest) | `97BC62` (moss) | `F5F5F5` (cream) |
    | **Coral Energy** | `F96167` (coral) | `F9E795` (gold) | `2F3C7E` (navy) |
    | **Warm Terracotta** | `B85042` (terracotta) | `E7E8D1` (sand) | `A7BEAE` (sage) |
    | **Ocean Gradient** | `065A82` (deep blue) | `1C7293` (teal) | `21295C` (midnight) |
    | **Charcoal Minimal** | `36454F` (charcoal) | `F2F2F2` (off-white) | `212121` (black) |
    | **Teal Trust** | `028090` (teal) | `00A896` (seafoam) | `02C39A` (mint) |
    | **Berry & Cream** | `6D2E46` (berry) | `A26769` (dusty rose) | `ECE2D0` (cream) |
    | **Cherry Bold** | `990011` (cherry) | `FCF6F5` (off-white) | `2F3C7E` (navy) |
    
    **Tip**: Invoke  for additional curated themes with font pairings.
    
    ### For Each Slide
    
    **Every slide needs a visual element** — image, chart, icon, or shape. Text-only slides are forgettable.
    
    **Layout options:**
    - Two-column (text left, illustration right)
    - Icon + text rows (icon in colored circle, bold header, description below)
    - 2x2 or 2x3 grid (image on one side, content blocks on other)
    - Half-bleed image (full left or right side) with content overlay
    
    **Data display:**
    - Large stat callouts (big numbers 60-72pt with small labels below)
    - Comparison columns (before/after, pros/cons, side-by-side)
    - Timeline or process flow (numbered steps, arrows)
    
    ### Typography
    
    **Choose an interesting font pairing** — don't default to Arial:
    
    | Header Font | Body Font |
    |-------------|-----------|
    | Georgia | Calibri |
    | Arial Black | Arial |
    | Cambria | Calibri |
    | Trebuchet MS | Calibri |
    | Impact | Arial |
    | Palatino | Garamond |
    
    | Element | Size |
    |---------|------|
    | Slide title | 36-44pt bold |
    | Section header | 20-24pt bold |
    | Body text | 14-16pt |
    | Captions | 10-12pt muted |
    
    ### Spacing
    
    - 0.5" minimum margins
    - 0.3-0.5" between content blocks
    - Leave breathing room — don't fill every inch
    
    ### Avoid (Common Mistakes)
    
    - **Don't repeat the same layout** — vary columns, cards, and callouts across slides
    - **Don't center body text** — left-align paragraphs and lists; center only titles
    - **Don't skimp on size contrast** — titles need 36pt+ to stand out from 14-16pt body
    - **Don't default to blue** — pick colors that reflect the specific topic
    - **Don't create text-only slides** — add images, icons, charts, or visual elements
    - **Don't use low-contrast elements** — icons AND text need strong contrast against background
    - **NEVER use accent lines under titles** — hallmark of AI-generated slides; use whitespace instead
    
    ## QA (Required)
    
    **Assume there are problems. Your job is to find them.**
    
    Your first render is almost never correct. Approach QA as a bug hunt, not a confirmation step.
    
    ### Content QA
    
    ```bash
    python -m markitdown output.pptx
    ```
    
    Check for missing content, typos, wrong order.
    
    **Check for leftover placeholder text:**
    ```bash
    python -m markitdown output.pptx | grep -iE "xxxx|lorem|ipsum|placeholder"
    ```
    
    ### Visual QA
    
    **USE SUBAGENTS** — even for 2-3 slides. You've been staring at the code and will see what you expect, not what's there.
    
    Convert slides to images, then inspect:
    
    ```bash
    # Convert to PDF, then to images
    soffice --headless --convert-to pdf output.pptx
    pdftoppm -jpeg -r 150 output.pdf slide
    ```
    
    **Inspection checklist:**
    - Overlapping elements (text through shapes, lines through words)
    - Text overflow or cut off at edges/box boundaries
    - Elements too close (< 0.3" gaps)
    - Uneven gaps
    - Insufficient margin from slide edges (< 0.5")
    - Low-contrast text or icons
    - Text boxes too narrow causing excessive wrapping
    - Leftover placeholder content
    
    ### Verification Loop
    
    1. Generate slides → Convert to images → Inspect
    2. **List issues found** (if none found, look again more critically)
    3. Fix issues
    4. **Re-verify affected slides** — one fix often creates another problem
    5. Repeat until a full pass reveals no new issues
    
    **Do not declare success until you've completed at least one fix-and-verify cycle.**
    
    ## Converting to Images
    
    ```bash
    soffice --headless --convert-to pdf output.pptx
    pdftoppm -jpeg -r 150 output.pdf slide
    ```
    
    Creates `slide-01.jpg`, `slide-02.jpg`, etc.
    
    ## Output
    
    After presentation operations, update `project docs`:
    ```markdown
    ## Just did
    - Presentation: {action} — {filename}
      - Slides: {count}
      - Theme: {theme used}
      - QA: {pass/fail — issues found}
    ```
