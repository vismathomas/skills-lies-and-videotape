---
name: web-artifacts
title: Web Artifacts Builder
description: "Build interactive single-page web artifacts using React, TypeScript, Tailwind CSS, and shadcn/ui. Bundles into self-contained HTML files for demos and prototypes."
category: frontend
source: https://github.com/anthropics/skills/tree/main/web-artifacts-builder
---
# Web Artifacts Builder

Build complete, interactive web experiences that bundle into a single HTML file.

## When to Use

- Building interactive demos, prototypes, or proof-of-concepts
- Creating self-contained web tools (calculators, converters, dashboards)
- Generating single-file HTML deliverables
- Rapid UI prototyping with modern stack

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 18+ |
| Language | TypeScript |
| Styling | Tailwind CSS 3+ |
| Components | shadcn/ui |
| Build | Vite |
| Icons | Lucide React |

## Workflow

### Phase 1: Initialize Project

```bash
# Create Vite + React + TypeScript project
npm create vite@latest artifact -- --template react-ts
cd artifact
npm install

# Install Tailwind CSS
npm install -D tailwindcss @tailwindcss/vite

# Install shadcn/ui dependencies
npx shadcn@latest init -d

# Install Lucide icons
npm install lucide-react
```

Configure Tailwind in `vite.config.ts`:
```typescript
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  plugins: [react(), tailwindcss()],
});
```

Add to `src/index.css`:
```css
@import "tailwindcss";
```

### Phase 2: Design

Before writing code, establish a clear design direction:

1. **Purpose**: What does the artifact do? What problem does it solve?
2. **Audience**: Who will use it?
3. **Visual direction**: Choose a theme and aesthetic (invoke frontend-design or )
4. **Key interactions**: Map out user flows

### Phase 3: Implement

#### Component Structure

```
src/
├── App.tsx           # Main layout and routing
├── index.css         # Tailwind + custom styles
├── components/
│   ├── ui/           # shadcn/ui components
│   └── features/     # Feature-specific components
├── hooks/            # Custom React hooks
├── lib/
│   └── utils.ts      # Utility functions
└── types/
    └── index.ts      # TypeScript type definitions
```

#### shadcn/ui Components

Add components as needed:
```bash
npx shadcn@latest add button card input dialog tabs
```

#### Design Guidelines

- **Typography**: Use `font-sans` as base. Create hierarchy with `text-4xl`, `text-2xl`, `text-lg`, `text-sm`
- **Spacing**: Consistent scale — `p-4`, `gap-6`, `space-y-4`. Generous whitespace
- **Colors**: Use Tailwind theme colors. Support dark mode with `dark:` variants
- **Responsive**: Mobile-first. Use `sm:`, `md:`, `lg:` breakpoints
- **Animations**: Subtle. Use `transition-all duration-200`, `animate-in`, `animate-out`
- **Layout**: CSS Grid for page layout, Flexbox for component alignment

#### State Management

- Use React `useState` / `useReducer` for local state
- Use `useContext` for shared state across components
- Avoid external state libraries for single-file artifacts
- Persist user data with `localStorage` when appropriate

### Phase 4: Bundle to Single HTML

Create a build script to inline all assets:

```bash
# Build the project
npm run build

# Bundle into single HTML (inline JS + CSS)
npx vite-plugin-singlefile  # or use custom script below
```

**Custom bundler script** (`bundle.mjs`):
```javascript
import { readFileSync, writeFileSync, readdirSync } from "fs";
import { join } from "path";

const distDir = "./dist";
let html = readFileSync(join(distDir, "index.html"), "utf-8");

// Inline CSS
const cssFiles = readdirSync(join(distDir, "assets")).filter(f => f.endsWith(".css"));
for (const css of cssFiles) {
  const content = readFileSync(join(distDir, "assets", css), "utf-8");
  html = html.replace(
    new RegExp(`<link[^>]*href="/assets/${css}"[^>]*>`),
    `<style>${content}</style>`
  );
}

// Inline JS
const jsFiles = readdirSync(join(distDir, "assets")).filter(f => f.endsWith(".js"));
for (const js of jsFiles) {
  const content = readFileSync(join(distDir, "assets", js), "utf-8");
  html = html.replace(
    new RegExp(`<script[^>]*src="/assets/${js}"[^>]*></script>`),
    `<script type="module">${content}</script>`
  );
}

writeFileSync(join(distDir, "artifact.html"), html);
console.log("Bundled to dist/artifact.html");
```

Alternatively use `vite-plugin-singlefile`:
```bash
npm install -D vite-plugin-singlefile
```

```typescript
// vite.config.ts
import { viteSingleFile } from "vite-plugin-singlefile";

export default defineConfig({
  plugins: [react(), tailwindcss(), viteSingleFile()],
});
```

### Phase 5: Verify

1. **Open** the bundled HTML in a browser — it must work standalone
2. **Check** all interactions work without a dev server
3. **Validate** responsive behavior at mobile/tablet/desktop widths
4. **Confirm** no external requests (fonts, CDNs, APIs) unless intentional

## Anti-Patterns

- **DON'T** use external CDN links — everything must be inlined
- **DON'T** make API calls to services that require auth (artifact must be self-contained)
- **DON'T** use heavy frameworks (Next.js, Remix) — Vite + React is sufficient
- **DON'T** over-engineer — favours simplicity and clarity
- **DON'T** use placeholder data — fill with realistic content

## Common Artifact Types

| Type | Examples | Key Features |
|------|----------|-------------|
| Dashboard | Analytics, monitoring | Charts, cards, filters |
| Tool | Calculator, converter, editor | Input forms, real-time output |
| Portfolio | Personal site, showcase | Sections, animations, images |
| Game | Quiz, puzzle, interactive | State machine, scoring, timer |
| Visualizer | Data viz, algorithm viz | Canvas/SVG, controls |
| Landing Page | Product page, signup | Hero, features, CTA |
