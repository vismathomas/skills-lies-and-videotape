---
title: Word Document Generation
description: "Create, read, and edit Word documents (.docx). Use when producing professional documents with formatting, tables of contents, headings, tracked changes, comments, or images."
---

# Word Document Generation

> Create, read, and edit Word documents (.docx). Use when producing professional documents with formatting, tables of contents, headings, tracked changes, comments, or images.

:material-tag: `documentation` · :material-github: [https://github.com/anthropics/skills/tree/main/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx)

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/docx/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/docx/SKILL.md){ .md-button .md-button--primary }

---

Creates, reads, and edits Word documents (.docx). Handles professional documents with formatting, tables of contents, headings, tracked changes, comments, and images.

## Usage Examples

### Create a project report

```
Create a Word document with an executive summary, findings section, and recommendations for the Q1 review.
```

### Extract text from a docx

```
Read and summarize the contents of the requirements.docx file.
```

### Edit an existing document

```
Update the version number and add a new section to proposal.docx.
```

## Credits

Based on: [https://github.com/anthropics/skills/tree/main/skills/docx](https://github.com/anthropics/skills/tree/main/skills/docx)

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # DOCX Creation, Editing, and Analysis
    
    ## Overview
    
    A `.docx` file is a ZIP archive containing XML files. This skill covers the full Word document lifecycle.
    
    ## When to Use
    
    - Creating Word documents (reports, memos, letters, templates)
    - Reading/extracting content from `.docx` files
    - Editing existing Word documents
    - Working with tracked changes or comments
    - Converting content into polished Word output
    - Any request mentioning "Word doc", ".docx", or professional document deliverables
    
    **Do NOT use for**: PDFs (use ), spreadsheets, Google Docs, or general coding tasks.
    
    ## Quick Reference
    
    | Task | Approach |
    |------|----------|
    | Read/analyze content | `pandoc` or unpack for raw XML |
    | Create new document | Use `docx-js` — see Creating New Documents below |
    | Edit existing document | Unpack → edit XML → repack |
    
    ## Dependencies
    
    - **pandoc**: Text extraction (`pandoc document.docx -o output.md`)
    - **docx**: `npm install -g docx` (creating new documents via JavaScript)
    - **LibreOffice**: PDF conversion (optional)
    - **Poppler**: `pdftoppm` for images (optional)
    
    ## Reading Content
    
    ```bash
    # Text extraction with tracked changes
    pandoc --track-changes=all document.docx -o output.md
    
    # Raw XML access (unpack the ZIP)
    mkdir unpacked && cd unpacked && unzip ../document.docx
    ```
    
    ## Creating New Documents
    
    Generate `.docx` files with JavaScript using the `docx` library. Install: `npm install -g docx`
    
    ### Setup
    
    ```javascript
    const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
            ImageRun, Header, Footer, AlignmentType, PageOrientation,
            LevelFormat, TableOfContents, HeadingLevel, BorderStyle,
            WidthType, ShadingType, PageNumber, PageBreak } = require('docx');
    const fs = require('fs');
    
    const doc = new Document({
      sections: [{ children: [/* content */] }]
    });
    
    Packer.toBuffer(doc).then(buffer =>
      fs.writeFileSync("doc.docx", buffer)
    );
    ```
    
    ### Page Size
    
    ```javascript
    // CRITICAL: docx-js defaults to A4, not US Letter
    // Always set page size explicitly
    sections: [{
      properties: {
        page: {
          size: {
            width: 12240,   // 8.5 inches in DXA (1440 DXA = 1 inch)
            height: 15840   // 11 inches in DXA
          },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } // 1 inch margins
        }
      },
      children: [/* content */]
    }]
    ```
    
    | Paper | Width | Height |
    |-------|-------|--------|
    | US Letter | 12,240 | 15,840 |
    | A4 (default) | 11,906 | 16,838 |
    
    **Landscape**: Pass portrait dimensions and set `orientation: PageOrientation.LANDSCAPE` — docx-js swaps width/height internally.
    
    ### Styles (Override Built-in Headings)
    
    ```javascript
    const doc = new Document({
      styles: {
        default: { document: { run: { font: "Arial", size: 24 } } }, // 12pt default
        paragraphStyles: [
          { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal",
            quickFormat: true,
            run: { size: 32, bold: true, font: "Arial" },
            paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 } },
          { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal",
            quickFormat: true,
            run: { size: 28, bold: true, font: "Arial" },
            paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1 } },
        ]
      },
      sections: [{
        children: [
          new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Title")] }),
        ]
      }]
    });
    ```
    
    ### Lists (NEVER use unicode bullets)
    
    ```javascript
    // ❌ WRONG — never manually insert bullet characters
    new Paragraph({ children: [new TextRun("• Item")] })
    
    // ✅ CORRECT — use numbering config with LevelFormat.BULLET
    const doc = new Document({
      numbering: {
        config: [
          { reference: "bullets",
            levels: [{ level: 0, format: LevelFormat.BULLET, text: "•",
              alignment: AlignmentType.LEFT,
              style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
          { reference: "numbers",
            levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.",
              alignment: AlignmentType.LEFT,
              style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
        ]
      },
      sections: [{
        children: [
          new Paragraph({ numbering: { reference: "bullets", level: 0 },
            children: [new TextRun("Bullet item")] }),
          new Paragraph({ numbering: { reference: "numbers", level: 0 },
            children: [new TextRun("Numbered item")] }),
        ]
      }]
    });
    ```
    
    ### Tables
    
    ```javascript
    // CRITICAL: Tables need dual widths — set both columnWidths on table AND width on each cell
    // CRITICAL: Use ShadingType.CLEAR (not SOLID) to prevent black backgrounds
    const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
    const borders = { top: border, bottom: border, left: border, right: border };
    
    new Table({
      width: { size: 9360, type: WidthType.DXA }, // Always use DXA (percentages break in Google Docs)
      columnWidths: [4680, 4680], // Must sum to table width
      rows: [
        new TableRow({
          children: [
            new TableCell({
              borders,
              width: { size: 4680, type: WidthType.DXA },
              shading: { fill: "D5E8F0", type: ShadingType.CLEAR },
              margins: { top: 80, bottom: 80, left: 120, right: 120 },
              children: [new Paragraph({ children: [new TextRun("Cell")] })]
            })
          ]
        })
      ]
    })
    ```
    
    ### Images
    
    ```javascript
    // CRITICAL: type parameter is REQUIRED
    new Paragraph({
      children: [new ImageRun({
        type: "png", // Required: png, jpg, jpeg, gif, bmp, svg
        data: fs.readFileSync("image.png"),
        transformation: { width: 200, height: 150 },
        altText: { title: "Title", description: "Desc", name: "Name" }
      })]
    })
    ```
    
    ### Page Breaks
    
    ```javascript
    new Paragraph({ children: [new PageBreak()] })
    ```
    
    ### Table of Contents
    
    ```javascript
    // CRITICAL: Headings must use HeadingLevel ONLY — no custom styles
    new TableOfContents("Table of Contents", { hyperlink: true, headingStyleRange: "1-3" })
    ```
    
    ### Headers/Footers
    
    ```javascript
    sections: [{
      properties: {
        page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } }
      },
      headers: {
        default: new Header({ children: [new Paragraph({ children: [new TextRun("Header")] })] })
      },
      footers: {
        default: new Footer({ children: [new Paragraph({
          children: [new TextRun("Page "), new TextRun({ children: [PageNumber.CURRENT] })]
        })] })
      },
      children: [/* content */]
    }]
    ```
    
    ### Critical Rules for docx-js
    
    - **Set page size explicitly** — defaults to A4; use US Letter (12240 x 15840 DXA) for US documents
    - **Landscape: pass portrait dimensions** — docx-js swaps internally
    - **Never use `\n`** — use separate Paragraph elements
    - **Never use unicode bullets** — use `LevelFormat.BULLET`
    - **PageBreak must be in Paragraph** — standalone creates invalid XML
    - **ImageRun requires `type`** — always specify png/jpg/etc.
    - **Always set table `width` with DXA** — never `WidthType.PERCENTAGE`
    - **Tables need dual widths** — `columnWidths` array AND cell `width`, both must match
    - **Table width = sum of columnWidths**
    - **Always add cell margins** — `margins: { top: 80, bottom: 80, left: 120, right: 120 }`
    - **Use `ShadingType.CLEAR`** — never SOLID for table shading
    - **TOC requires HeadingLevel only** — no custom styles on heading paragraphs
    - **Override built-in styles** — use exact IDs: "Heading1", "Heading2", etc.
    - **Include `outlineLevel`** — required for TOC (0 for H1, 1 for H2, etc.)
    
    ## Editing Existing Documents
    
    **Follow all 3 steps in order.**
    
    ### Step 1: Unpack
    
    ```bash
    mkdir unpacked && cd unpacked && unzip ../document.docx
    # Or with Python:
    python3 -c "import zipfile; zipfile.ZipFile('document.docx').extractall('unpacked')"
    ```
    
    ### Step 2: Edit XML
    
    Edit files in `unpacked/word/`. Key files:
    - `word/document.xml` — main content
    - `word/styles.xml` — document styles
    - `word/_rels/document.xml.rels` — relationships (images, hyperlinks)
    
    **Use "Claude" as the author** for tracked changes and comments.
    
    **Use smart quotes for new content:**
    
    | Entity | Character |
    |--------|-----------|
    | `&#x2018;` | ' (left single) |
    | `&#x2019;` | ' (right single / apostrophe) |
    | `&#x201C;` | " (left double) |
    | `&#x201D;` | " (right double) |
    
    ### Step 3: Repack
    
    ```bash
    cd unpacked && zip -r ../output.docx . -x ".*"
    ```
    
    ### Tracked Changes XML
    
    **Insertion:**
    ```xml
    <w:ins w:id="1" w:author="Claude" w:date="2025-01-01T00:00:00Z">
      <w:r><w:t>inserted text</w:t></w:r>
    </w:ins>
    ```
    
    **Deletion:**
    ```xml
    <w:del w:id="2" w:author="Claude" w:date="2025-01-01T00:00:00Z">
      <w:r><w:delText>deleted text</w:delText></w:r>
    </w:del>
    ```
    
    **Inside `<w:del>`**: Use `<w:delText>` instead of `<w:t>`.
    
    ### Common Pitfalls
    
    - **Replace entire `<w:r>` elements**: When adding tracked changes, replace the whole `<w:r>...</w:r>` block
    - **Preserve `<w:rPr>` formatting**: Copy the original run's formatting into tracked change runs
    - **Element order in `<w:pPr>`**: `<w:pStyle>`, `<w:numPr>`, `<w:spacing>`, `<w:ind>`, `<w:jc>`, `<w:rPr>` last
    - **Whitespace**: Add `xml:space="preserve"` to `<w:t>` with leading/trailing spaces
    
    ## Output
    
    After document operations, update `project docs`:
    ```markdown
    ## Just did
    - Document: {action} — {filename}
      - Type: {create/edit/read}
      - Format: .docx
    ```
