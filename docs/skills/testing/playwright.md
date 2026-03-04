---
title: Playwright Browser Automation
description: "Browser automation with Playwright. Write and execute custom Playwright code for testing, scraping, visual regression, form interaction, and any browser task."
---

# Playwright Browser Automation

> Browser automation with Playwright. Write and execute custom Playwright code for testing, scraping, visual regression, form interaction, and any browser task.

:material-tag: `testing` · :material-github: [https://github.com/lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill)

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/playwright/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/playwright/SKILL.md){ .md-button .md-button--primary }

---

General-purpose browser automation with Playwright. Write and execute custom Playwright code for testing, scraping, visual regression, form interaction, and any browser automation task.

## Usage Examples

### Write an E2E test

```
Write a Playwright test that logs in, navigates to the dashboard, and verifies the data table loads.
```

### Scrape a webpage

```
Use Playwright to scrape product prices from this page and save them as JSON.
```

### Visual regression test

```
Create a Playwright visual regression test for the homepage.
```

## Credits

Based on: [https://github.com/lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill)

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Playwright Browser Automation
    
    General-purpose browser automation skill. Write custom Playwright code for any automation task and execute it.
    
    ## When to Use
    
    - Testing web pages, forms, login flows
    - Taking screenshots (single or responsive multi-viewport)
    - Checking for broken links
    - Visual regression testing
    - Validating web functionality
    - Automating any browser-based interaction
    - E2E testing during  workflows
    
    ## Prerequisites
    
    - **Node.js** installed
    - **Playwright** installed: `npm install playwright` (or `npx playwright install`)
    - **Chromium** browser: `npx playwright install chromium`
    
    ### Quick Setup
    
    ```bash
    npm install playwright
    npx playwright install chromium
    ```
    
    ## Critical Workflow
    
    Follow these steps in order:
    
    ### 1. Auto-Detect Dev Servers (for localhost testing)
    
    **ALWAYS detect running dev servers FIRST** before writing test code:
    
    ```bash
    # Check for running dev servers on common ports
    for port in 3000 3001 4200 5000 5173 8000 8080 8888; do
      (echo >/dev/tcp/localhost/$port) 2>/dev/null && echo "Server on port $port"
    done
    ```
    
    - If 1 server found → use it automatically, inform user
    - If multiple servers found → ask user which one to test
    - If no servers found → ask for URL or offer to help start dev server
    
    ### 2. Write Scripts to /tmp
    
    **NEVER write test files to the project directory.** Always use `/tmp/playwright-test-*.js` (or OS temp equivalent).
    
    ### 3. Use Visible Browser by Default
    
    Always use `headless: false` unless user specifically requests headless mode.
    
    ### 4. Parameterize URLs
    
    Always make URLs configurable via a `TARGET_URL` constant at the top of every script.
    
    ## Execution Pattern
    
    ```javascript
    // /tmp/playwright-test-page.js
    const { chromium } = require('playwright');
    
    const TARGET_URL = 'http://localhost:3001'; // Auto-detected or from user
    
    (async () => {
      const browser = await chromium.launch({ headless: false });
      const page = await browser.newPage();
    
      await page.goto(TARGET_URL);
      console.log('Page loaded:', await page.title());
    
      await page.screenshot({ path: '/tmp/screenshot.png', fullPage: true });
      console.log('📸 Screenshot saved to /tmp/screenshot.png');
    
      await browser.close();
    })();
    ```
    
    Execute:
    ```bash
    node /tmp/playwright-test-page.js
    ```
    
    ## Common Patterns
    
    ### Test a Page (Multiple Viewports)
    
    ```javascript
    const { chromium } = require('playwright');
    const TARGET_URL = 'http://localhost:3001';
    
    (async () => {
      const browser = await chromium.launch({ headless: false, slowMo: 100 });
      const page = await browser.newPage();
    
      // Desktop
      await page.setViewportSize({ width: 1920, height: 1080 });
      await page.goto(TARGET_URL);
      await page.screenshot({ path: '/tmp/desktop.png', fullPage: true });
    
      // Tablet
      await page.setViewportSize({ width: 768, height: 1024 });
      await page.screenshot({ path: '/tmp/tablet.png', fullPage: true });
    
      // Mobile
      await page.setViewportSize({ width: 375, height: 667 });
      await page.screenshot({ path: '/tmp/mobile.png', fullPage: true });
    
      console.log('✅ All viewports tested');
      await browser.close();
    })();
    ```
    
    ### Test Login Flow
    
    ```javascript
    const { chromium } = require('playwright');
    const TARGET_URL = 'http://localhost:3001';
    
    (async () => {
      const browser = await chromium.launch({ headless: false });
      const page = await browser.newPage();
    
      await page.goto(`${TARGET_URL}/login`);
      await page.fill('input[name="email"]', 'test@example.com');
      await page.fill('input[name="password"]', 'password123');
      await page.click('button[type="submit"]');
    
      await page.waitForURL('**/dashboard');
      console.log('✅ Login successful, redirected to dashboard');
      await browser.close();
    })();
    ```
    
    ### Fill and Submit Form
    
    ```javascript
    const { chromium } = require('playwright');
    const TARGET_URL = 'http://localhost:3001';
    
    (async () => {
      const browser = await chromium.launch({ headless: false, slowMo: 50 });
      const page = await browser.newPage();
    
      await page.goto(`${TARGET_URL}/contact`);
      await page.fill('input[name="name"]', 'John Doe');
      await page.fill('input[name="email"]', 'john@example.com');
      await page.fill('textarea[name="message"]', 'Test message');
      await page.click('button[type="submit"]');
    
      await page.waitForSelector('.success-message');
      console.log('✅ Form submitted successfully');
      await browser.close();
    })();
    ```
    
    ### Check for Broken Links
    
    ```javascript
    const { chromium } = require('playwright');
    
    (async () => {
      const browser = await chromium.launch({ headless: false });
      const page = await browser.newPage();
    
      await page.goto('http://localhost:3000');
      const links = await page.locator('a[href^="http"]').all();
      const results = { working: 0, broken: [] };
    
      for (const link of links) {
        const href = await link.getAttribute('href');
        try {
          const response = await page.request.head(href);
          if (response.ok()) results.working++;
          else results.broken.push({ url: href, status: response.status() });
        } catch (e) {
          results.broken.push({ url: href, error: e.message });
        }
      }
    
      console.log(`✅ Working links: ${results.working}`);
      console.log(`❌ Broken links:`, results.broken);
      await browser.close();
    })();
    ```
    
    ### Visual Regression Testing
    
    ```javascript
    const { chromium } = require('playwright');
    const TARGET_URL = 'http://localhost:3001';
    
    (async () => {
      const browser = await chromium.launch({ headless: false });
      const page = await browser.newPage();
    
      await page.goto(TARGET_URL);
      await page.waitForLoadState('networkidle');
    
      // Take baseline screenshot
      await page.screenshot({
        path: '/tmp/visual-regression.png',
        fullPage: true,
      });
    
      console.log('📸 Baseline screenshot saved');
      console.log('Compare with previous baseline to detect regressions');
      await browser.close();
    })();
    ```
    
    ## Inline Execution (Simple Tasks)
    
    For quick one-off tasks, execute code inline:
    
    ```bash
    node -e "
    const { chromium } = require('playwright');
    (async () => {
      const browser = await chromium.launch({ headless: false });
      const page = await browser.newPage();
      await page.goto('http://localhost:3001');
      await page.screenshot({ path: '/tmp/quick-screenshot.png', fullPage: true });
      console.log('Screenshot saved');
      await browser.close();
    })();
    "
    ```
    
    **When to use inline vs files:**
    - **Inline**: Quick one-off tasks (screenshot, check element, get page title)
    - **Files**: Complex tests, responsive checks, anything user might want to re-run
    
    ## Tips
    
    - **CRITICAL: Detect servers FIRST** — always check for running dev servers before writing test code
    - **Use /tmp for test files** — write to `/tmp/playwright-test-*.js`, never to project directory
    - **Parameterize URLs** — put detected/provided URL in a `TARGET_URL` constant at top of every script
    - **DEFAULT: Visible browser** — always use `headless: false` unless user explicitly asks for headless
    - **Slow down**: Use `slowMo: 100` to make actions visible
    - **Wait strategies**: Use `waitForURL`, `waitForSelector`, `waitForLoadState` instead of fixed timeouts
    - **Error handling**: Always use try-catch for robust automation
    - **Console output**: Use `console.log()` to track progress
    
    ## Integration with 
    
    When invoked from :
    1. Write Playwright E2E tests that complement unit/integration tests
    2. Focus on user-facing workflows (login, forms, navigation)
    3. Report results back for test coverage analysis
    4. Create issues for any broken functionality found
    
    ## Troubleshooting
    
    - **Playwright not installed**: `npm install playwright && npx playwright install chromium`
    - **Module not found**: Ensure Playwright is installed globally or in the project
    - **Browser doesn't open**: Check `headless: false` and ensure display is available
    - **Element not found**: Add wait: `await page.waitForSelector('.element', { timeout: 10000 })`
