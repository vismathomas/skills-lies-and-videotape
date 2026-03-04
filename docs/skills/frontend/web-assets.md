---
title: Web Asset Generator
description: "Generate favicons, app icons, PWA manifest, and social media images (OG/Twitter cards) from logos, text, or emojis. Use when setting up web project branding assets."
---

# Web Asset Generator

> Generate favicons, app icons, PWA manifest, and social media images (OG/Twitter cards) from logos, text, or emojis. Use when setting up web project branding assets.

:material-tag: `frontend` · :material-github: [https://github.com/alonw0/web-asset-generator](https://github.com/alonw0/web-asset-generator)

[:material-github: View on GitHub](https://github.com/vismathomas/skills-lies-and-videotape/blob/main/skills/web-assets/SKILL.md){ .md-button }
[:material-download: Download SKILL.md](https://github.com/vismathomas/skills-lies-and-videotape/raw/main/skills/web-assets/SKILL.md){ .md-button .md-button--primary }

---

Generates production-ready web assets from logos, text, or emojis — including favicons, app icons, PWA manifest, Open Graph images, and Twitter card images.

## Usage Examples

### Generate favicons

```
Generate a complete favicon set from our logo.png file.
```

### Create social media images

```
Generate Open Graph and Twitter Card images for our marketing site.
```

### Emoji-based branding

```
Generate all web assets using the 🚀 emoji as the icon source.
```

## Credits

Based on: [https://github.com/alonw0/web-asset-generator](https://github.com/alonw0/web-asset-generator)

---

## Full Specification

??? abstract "SKILL.md — Complete technical specification"

    # Web Asset Generator
    
    Generate production-ready web assets from logos, text, or emojis.
    
    ## When to Use
    
    - Creating favicons for a website
    - Generating PWA/mobile app icons
    - Creating Open Graph images for social sharing
    - Making Twitter card images
    - Setting up `manifest.json` for a PWA
    - Any request for web branding assets (icons, social images)
    
    ## Prerequisites
    
    ```bash
    pip install Pillow
    # Optional: For emoji rendering
    pip install pilmoji 'emoji<2.0.0'
    ```
    
    ## Features
    
    | Asset Type | Sizes | Format |
    |-----------|-------|--------|
    | **Favicons** | 16×16, 32×32, 96×96, favicon.ico | PNG, ICO |
    | **App Icons** | 180×180, 192×192, 512×512 | PNG |
    | **PWA Manifest** | Auto-generated | JSON |
    | **Open Graph** | 1200×630 | PNG |
    | **Twitter Card** | 1200×675 | PNG |
    
    ## Workflow
    
    ### 1. Determine Source
    
    Ask user for input source:
    - **Logo file**: Use existing image file (`.png`, `.svg`, `.jpg`)
    - **Emoji**: Suggest relevant emojis for their project type
    - **Text**: Generate from text/initials with custom colors
    
    ### 2. Generate Favicons
    
    ```python
    from PIL import Image
    
    def generate_favicons(source_image_path, output_dir):
        """Generate favicon set from source image."""
        img = Image.open(source_image_path).convert("RGBA")
        sizes = [16, 32, 48, 96, 180, 192, 512]
    
        for size in sizes:
            resized = img.resize((size, size), Image.Resampling.LANCZOS)
            resized.save(f"{output_dir}/icon-{size}x{size}.png", "PNG")
    
        # Generate favicon.ico (multi-size ICO)
        ico_sizes = [img.resize((s, s), Image.Resampling.LANCZOS) for s in [16, 32, 48]]
        ico_sizes[0].save(f"{output_dir}/favicon.ico", "ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    
        return sizes
    ```
    
    ### 3. Generate Social Images (OG/Twitter)
    
    ```python
    from PIL import Image, ImageDraw, ImageFont
    
    def generate_og_image(output_path, title, bg_color="#1a1a2e", text_color="#ffffff"):
        """Generate Open Graph image (1200x630)."""
        img = Image.new("RGB", (1200, 630), bg_color)
        draw = ImageDraw.Draw(img)
    
        # Use a clean font — try system fonts
        try:
            font = ImageFont.truetype("arial.ttf", 48)
        except:
            font = ImageFont.load_default()
    
        # Center text
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (1200 - text_width) // 2
        y = (630 - text_height) // 2
    
        draw.text((x, y), title, fill=text_color, font=font)
        img.save(output_path, "PNG")
    ```
    
    ### 4. Generate Emoji-Based Assets
    
    ```python
    from PIL import Image, ImageDraw, ImageFont
    
    def generate_emoji_favicon(emoji, output_dir, bg_color="#ffffff"):
        """Generate favicon from emoji character."""
        sizes = [16, 32, 48, 96, 180, 192, 512]
    
        for size in sizes:
            img = Image.new("RGBA", (size, size), bg_color)
            draw = ImageDraw.Draw(img)
    
            # Try to use emoji font
            font_size = int(size * 0.7)
            try:
                font = ImageFont.truetype("seguiemj.ttf", font_size)  # Windows
            except:
                try:
                    font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", font_size)  # macOS
                except:
                    font = ImageFont.load_default()
    
            # Center emoji
            bbox = draw.textbbox((0, 0), emoji, font=font)
            x = (size - (bbox[2] - bbox[0])) // 2
            y = (size - (bbox[3] - bbox[1])) // 2
            draw.text((x, y), emoji, font=font)
    
            img.save(f"{output_dir}/icon-{size}x{size}.png", "PNG")
    ```
    
    ### 5. Generate PWA Manifest
    
    ```python
    import json
    
    def generate_manifest(output_path, name, short_name, theme_color="#1a1a2e", bg_color="#ffffff"):
        """Generate manifest.json for PWA."""
        manifest = {
            "name": name,
            "short_name": short_name,
            "start_url": "/",
            "display": "standalone",
            "theme_color": theme_color,
            "background_color": bg_color,
            "icons": [
                {"src": f"/icons/icon-{s}x{s}.png", "sizes": f"{s}x{s}", "type": "image/png"}
                for s in [48, 96, 180, 192, 512]
            ] + [
                {"src": "/icons/icon-192x192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
                {"src": "/icons/icon-512x512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}
            ]
        }
    
        with open(output_path, "w") as f:
            json.dump(manifest, f, indent=2)
    ```
    
    ### 6. HTML Integration
    
    After generating assets, provide the HTML tags:
    
    ```html
    <!-- Favicons -->
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/icons/icon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/icons/icon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/icons/icon-180x180.png">
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#1a1a2e">
    
    <!-- Open Graph -->
    <meta property="og:image" content="/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="/twitter-card.png">
    ```
    
    ### 7. Framework Auto-Detection
    
    Detect the project framework and provide framework-specific integration:
    
    | Framework | Icon Location | Config File |
    |-----------|--------------|-------------|
    | Next.js | `public/` or `app/` | `next.config.js` |
    | Astro | `public/` | `astro.config.mjs` |
    | Vite/React | `public/` | `index.html` |
    | Angular | `src/assets/` | `angular.json` |
    | Nuxt | `public/` | `nuxt.config.ts` |
    
    ## Validation
    
    After generating assets, validate:
    - [ ] All required sizes generated
    - [ ] File sizes reasonable (< 100KB for icons, < 500KB for social images)
    - [ ] WCAG contrast compliance for text-based images
    - [ ] `manifest.json` valid JSON
    - [ ] HTML tags correctly reference generated files
    
    ## Emoji Suggestions
    
    When user doesn't have a logo, suggest relevant emojis:
    
    | Project Type | Suggestions |
    |-------------|-------------|
    | Tech startup | 🚀 💡 ⚡ 🔮 |
    | E-commerce | 🛍️ 🏪 💳 📦 |
    | Food/Restaurant | 🍽️ 🍕 ☕ 🧁 |
    | Education | 📚 🎓 ✏️ 🧠 |
    | Health/Fitness | 💪 🏃 ❤️ 🧘 |
    | Travel | ✈️ 🌍 🗺️ 🏖️ |
    | Music/Entertainment | 🎵 🎬 🎮 🎨 |
