#!/usr/bin/env bash
#
# Downloads the self-hosted WOFF2 font files for the companion site.
#
# Why: the site is configured to load fonts from /assets/fonts/ locally
# (no external font CDN). System-font fallbacks in styles.css mean the
# site still works without these files, but the design isn't quite right
# until they're present.
#
# Run once after cloning the repo:
#   cd assets/fonts && bash download-fonts.sh
#
# Source: Google Fonts hosts the canonical WOFF2 builds at fonts.gstatic.com.
# These specific files were chosen from the @font-face declarations in
# styles.css. URLs are pinned to the v-numbered paths in each font's CSS
# response from fonts.googleapis.com — if Google changes the version,
# update this script and re-run.

set -euo pipefail

cd "$(dirname "$0")"

# Cormorant Garamond
curl -sSL -o cormorant-garamond-400.woff2 \
  "https://fonts.gstatic.com/s/cormorantgaramond/v16/co3bmX5slCNuHLi8bLeY9MK7whWMhyjornFLsS6V7w.woff2"
curl -sSL -o cormorant-garamond-400-italic.woff2 \
  "https://fonts.gstatic.com/s/cormorantgaramond/v16/co3WmX5slCNuHLi8bLeY9MK7whWMhyjQEcpPm9hxxQ.woff2"
curl -sSL -o cormorant-garamond-600.woff2 \
  "https://fonts.gstatic.com/s/cormorantgaramond/v16/co3YmX5slCNuHLi8bLeY9MK7whWMhyjYrFNcsS6V7w.woff2"

# Inter
curl -sSL -o inter-400.woff2 \
  "https://fonts.gstatic.com/s/inter/v18/UcC73FwrK3iLTeHuS_nVMrMxCp50ojIw2yU.woff2"
curl -sSL -o inter-500.woff2 \
  "https://fonts.gstatic.com/s/inter/v18/UcC73FwrK3iLTeHuS_nVMrMxCp50ojIa1iU.woff2"
curl -sSL -o inter-600.woff2 \
  "https://fonts.gstatic.com/s/inter/v18/UcC73FwrK3iLTeHuS_nVMrMxCp50ojIw2qU.woff2"

# JetBrains Mono
curl -sSL -o jetbrains-mono-400.woff2 \
  "https://fonts.gstatic.com/s/jetbrainsmono/v20/tDbY2o-flEEny0FZhsfKu5WU4zr3E_BX0PnT8RD8yKxjPVmUsaaDhw.woff2"

echo "All seven font files downloaded."
ls -lh *.woff2
