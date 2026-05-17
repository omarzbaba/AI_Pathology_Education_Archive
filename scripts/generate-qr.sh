#!/usr/bin/env bash
#
# Generate a high-resolution QR code pointing to the live companion site.
# The PNG output is suitable for printing on the final slide of the workshop.
#
# Usage:
#   bash scripts/generate-qr.sh https://omarzbaba.github.io/AI_Pathology_Education/
#
# Output: assets/img/companion-qr.png  (1000x1000 px, error correction H)
#
# Why we generate locally instead of using an online QR generator:
#   - Online generators receive the URL (minor) and may log it (privacy).
#   - Local generation is deterministic, reproducible, and offline.
#
# Requires the 'qrencode' utility:
#   macOS:    brew install qrencode
#   Ubuntu:   sudo apt-get install qrencode

set -euo pipefail

URL="${1:-}"

if [ -z "$URL" ]; then
  echo "Usage: $0 <full-https-url>"
  echo "Example: $0 https://omarzbaba.github.io/AI_Pathology_Education/"
  exit 1
fi

if ! command -v qrencode &> /dev/null; then
  echo "Error: qrencode not installed."
  echo "  macOS:  brew install qrencode"
  echo "  Ubuntu: sudo apt-get install qrencode"
  exit 1
fi

OUT="assets/img/companion-qr.png"
mkdir -p "$(dirname "$OUT")"

qrencode \
  -o "$OUT" \
  -s 20 \
  -l H \
  -m 4 \
  -t PNG \
  "$URL"

echo "QR code written to $OUT"
echo "URL encoded: $URL"
ls -lh "$OUT"
