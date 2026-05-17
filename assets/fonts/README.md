# Fonts

Populated in Phase 2 with self-hosted font files. No external font CDN (e.g., Google Fonts) is loaded at runtime — this protects user privacy (no third-party requests on page load) and keeps the Content Security Policy strict.

Phase 2 picks the final font set from:

- **Headings (serif):** Cormorant Garamond, Playfair Display, or EB Garamond
- **Body (sans-serif):** Inter, IBM Plex Sans, or Source Sans 3
- **Code (monospace):** IBM Plex Mono or JetBrains Mono

All three are SIL OFL-licensed and safe to redistribute.
