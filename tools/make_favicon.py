#!/usr/bin/env python3
"""Generate raster favicon variants from the assets/img/favicon.svg design.

Draws the same ball emblem with Pillow at 4x resolution and downsamples,
writing:
  - assets/img/favicon-32x32.png
  - assets/img/apple-touch-icon.png (180x180)

Run whenever the emblem design in favicon.svg changes:
    python3 tools/make_favicon.py
"""

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
ACCENT = (79, 70, 229, 255)
WHITE = (255, 255, 255, 255)
SS = 4


def bezier(p0, p1, p2, p3, steps=60):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt**2 * t * p1[0] + 3 * mt * t**2 * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt**2 * t * p1[1] + 3 * mt * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def draw(size):
    s = size * SS
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, s - 1, s - 1], radius=s * 14 // 64, fill=ACCENT)
    r = s * 19 / 64
    cx = cy = s / 2
    w = max(2, round(s * 4 / 64))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=WHITE, width=w)
    lw = max(2, round(s * 3.5 / 64))
    d.line([cx, cy - r, cx, cy + r], fill=WHITE, width=lw)
    d.line([cx - r, cy, cx + r, cy], fill=WHITE, width=lw)
    k = s * 2.5 / 64
    for sx in (-1, 1):
        pts = bezier(
            (cx + sx * (s * 20 / 64), cy - s * 13.4 / 64),
            (cx + sx * (s * 27.5 / 64), cy - s * 8 / 64),
            (cx + sx * (s * 27.5 / 64), cy + s * 8 / 64),
            (cx + sx * (s * 20 / 64), cy + s * 13.4 / 64),
        )
        d.line(pts, fill=WHITE, width=lw, joint="curve")
    return img.resize((size, size), Image.LANCZOS)


draw(32).save(IMG / "favicon-32x32.png")
draw(180).save(IMG / "apple-touch-icon.png")
print("Wrote favicon-32x32.png and apple-touch-icon.png")
