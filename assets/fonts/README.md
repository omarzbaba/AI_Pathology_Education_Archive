# Fonts

The site uses three self-hosted typefaces:

- **Cormorant Garamond** (serif) — headings and editorial display
- **Inter** (sans-serif) — body text, navigation, forms
- **JetBrains Mono** (monospace) — code blocks in prompt files

All three are licensed under the SIL Open Font License (OFL) and free to redistribute.

## Why self-hosted

The site does not load fonts from any third-party CDN (e.g., Google Fonts). Self-hosting:

1. Protects user privacy (no third-party requests on page load)
2. Allows a strict Content Security Policy that disallows external scripts and fonts
3. Avoids a runtime dependency on someone else's infrastructure

## How to install

Run the download script once after cloning:

```
bash assets/fonts/download-fonts.sh
```

This pulls seven WOFF2 files from `fonts.gstatic.com` and saves them in this directory.

**The site is usable without these files.** The CSS in `styles.css` includes strong system-font fallbacks (Iowan Old Style / Georgia for the serif, the standard system sans stack for body, SF Mono / Menlo / Consolas for code), so the layout is correct and readable even before the script is run. The custom fonts are an upgrade, not a requirement.

## Updating

If Google bumps the version path on `fonts.gstatic.com`, the URLs in `download-fonts.sh` need to be updated. To find the current URLs:

1. Open `https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap` in a browser
2. Copy the `url(...)` paths from the returned CSS
3. Update the script

## Licensing

All three fonts are SIL OFL 1.1 — see each font's source repository for the license file. Redistribution as part of this repository is permitted.
