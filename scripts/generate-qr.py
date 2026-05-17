#!/usr/bin/env python3
"""
Generate a high-resolution QR code pointing to the live companion site.

Usage:
  python3 scripts/generate-qr.py https://omarzbaba.github.io/AI_Pathology_Education/

Output:
  assets/img/companion-qr.png  (1000x1000 px, error correction H)

Requires the 'qrcode' Python library:
  pip install "qrcode[pil]"

This is the Python alternative to scripts/generate-qr.sh (which uses the
qrencode CLI). Use whichever path is more convenient. Output is equivalent.

Why we generate locally instead of using an online QR generator:
  - Online generators receive the URL and may log it (privacy).
  - Local generation is deterministic, reproducible, and offline.
"""

import os
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/generate-qr.py <full-https-url>")
        print("Example: python3 scripts/generate-qr.py https://omarzbaba.github.io/AI_Pathology_Education/")
        sys.exit(1)

    url = sys.argv[1]

    try:
        import qrcode
    except ImportError:
        print("Error: 'qrcode' library not installed.")
        print('Install with:  pip install "qrcode[pil]"')
        print("Or use the bash script instead: bash scripts/generate-qr.sh <url>")
        sys.exit(1)

    out_path = Path("assets/img/companion-qr.png")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(str(out_path))

    print(f"QR code written to {out_path}")
    print(f"URL encoded: {url}")
    size = out_path.stat().st_size
    print(f"File size: {size:,} bytes")


if __name__ == "__main__":
    main()
