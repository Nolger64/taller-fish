#!/usr/bin/env python3
"""Genera el código QR que lleva a la página del taller.

Uso:
    python3 tools/make_qr.py https://usuario.github.io/taller-fish/

Sin argumentos usa la URL de ejemplo (TU-USUARIO). Al publicar en GitHub
Pages, ejecuta el comando con tu URL real para regenerar img/qr.png y
img/qr.svg.
"""

from pathlib import Path
import sys

import segno

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_URL = "https://TU-USUARIO.github.io/taller-fish/"


def main() -> None:
    url = (sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL).strip()

    if not url.startswith(("http://", "https://")):
        sys.exit("La URL debe empezar por http:// o https://")

    qr = segno.make(url, error="m")

    (ROOT / "img").mkdir(parents=True, exist_ok=True)
    png = ROOT / "img" / "qr.png"
    svg = ROOT / "img" / "qr.svg"

    qr.save(png, scale=10, border=2, dark="#151a22", light="#ffffff")
    qr.save(svg, scale=10, border=2, dark="#151a22", light="#ffffff")

    print(f"QR generado para: {url}")
    print(f"  - {png.relative_to(ROOT)}")
    print(f"  - {svg.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
