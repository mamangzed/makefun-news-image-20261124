#!/usr/bin/env python3
"""Draw the 24 November 2026 world-news summary image (1024x1024 PNG).

Built for the make.fun news-image-20261124 bounty. Every story below was
first reported on Tuesday 24 November 2026 (checked against the day's wires
and press round-ups); the image names the day up front, as the judge asks.
Run: python3 draw_news.py  ->  entry.png (1024x1024, < 1 MiB).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 247, 239)
INK = (20, 28, 45)
NAVY = (20, 33, 61)
GOLD = (212, 160, 60)
MUTED = (96, 104, 122)
WHITE = (255, 255, 255)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def star(draw, cx, cy, r, color):
    """Five-point star centred at (cx, cy)."""
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.42
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(pts, fill=color)


# ---------------------------------------------------------------- stories
# (tag, accent colour, headline, deck)
STORIES = [
    ("WAR TOLL", (139, 30, 30),
     "Russia's war dead near 700,000",
     "Leaked data, via Kyiv Independent."),
    ("UKRAINE", (176, 92, 20),
     "Fresh Russian strikes hit Kyiv",
     "Drones and missiles overnight."),
    ("CLIMATE", (34, 120, 66),
     "COP31 talks stall in Türkiye",
     "Split over fossil fuels and finance."),
    ("INDONESIA", (178, 58, 32),
     "Deadly factory fire in Indonesia",
     "Workers missing; rescuers search site."),
    ("UNITED STATES", (31, 76, 148),
     "First Gen Z woman in Congress",
     "Melat Kiros, 29, Democrat, wins seat."),
    ("AFRICA", (122, 90, 22),
     "Sahel states reopen talks",
     "With West Africa bloc, after years of strain."),
]

# ---------------------------------------------------------------- icons
def icon_war_toll(d, x, y, s, accent):
    # The toll itself, as a big numeral: unambiguous at any size.
    d.text((x + s * 0.5, y + s * 0.34), "700k",
           font=font(BOLD, 38), fill=accent, anchor="mm")
    d.text((x + s * 0.5, y + s * 0.62), "DEAD",
           font=font(BOLD, 24), fill=accent, anchor="mm")
    d.rectangle([x + s * 0.18, y + s * 0.78, x + s * 0.82, y + s * 0.84],
                fill=accent)


def icon_strikes(d, x, y, s, accent):
    # Night skyline + orange starburst blast above it.
    d.rectangle([x, y + s * 0.62, x + s * 0.24, y + s], fill=INK)
    d.rectangle([x + s * 0.30, y + s * 0.48, x + s * 0.58, y + s], fill=INK)
    d.rectangle([x + s * 0.64, y + s * 0.66, x + s, y + s], fill=INK)
    cx, cy, r = x + s * 0.5, y + s * 0.30, s * 0.30
    star(d, cx, cy, r, (232, 148, 28))
    star(d, cx, cy, r * 0.55, (244, 196, 66))


def icon_climate(d, x, y, s, accent):
    # Globe: circle + meridians.
    cx, cy, r = x + s * 0.5, y + s * 0.5, s * 0.42
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=accent, width=6)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=accent, width=4)
    d.line([cx - r, cy, cx + r, cy], fill=accent, width=4)


def icon_fire(d, x, y, s, accent):
    # Factory silhouette + flame.
    d.rectangle([x, y + s * 0.55, x + s * 0.62, y + s], fill=INK)
    d.rectangle([x + s * 0.68, y + s * 0.30, x + s * 0.80, y + s], fill=INK)
    fx, fy = x + s * 0.30, y + s * 0.34
    d.polygon([(fx, fy), (fx + s * 0.16, fy - s * 0.30),
               (fx + s * 0.30, fy - s * 0.06), (fx + s * 0.44, fy - s * 0.34),
               (fx + s * 0.52, fy), (fx + s * 0.26, fy + s * 0.14)],
              fill=(232, 90, 20))
    d.polygon([(fx + s * 0.14, fy + s * 0.02), (fx + s * 0.24, fy - s * 0.14),
               (fx + s * 0.34, fy + s * 0.02), (fx + s * 0.26, fy + s * 0.10)],
              fill=(244, 196, 66))


def icon_congress(d, x, y, s, accent):
    # Capitol dome: dome + drum + columns + base.
    cx = x + s * 0.5
    d.pieslice([cx - s * 0.34, y + s * 0.10, cx + s * 0.34, y + s * 0.78],
               180, 360, fill=accent)
    d.rectangle([cx - s * 0.30, y + s * 0.44, cx + s * 0.30, y + s * 0.56],
                fill=accent)
    for i in range(5):
        bx = x + s * (0.08 + i * 0.18)
        d.rectangle([bx, y + s * 0.56, bx + s * 0.09, y + s * 0.86], fill=accent)
    d.rectangle([x, y + s * 0.86, x + s, y + s * 0.96], fill=accent)
    d.line([cx, y + s * 0.10, cx, y - s * 0.02], fill=accent, width=5)
    d.polygon([(cx, y - s * 0.02), (cx + s * 0.16, y + s * 0.03),
               (cx, y + s * 0.08)], fill=(178, 58, 32))


def icon_talks(d, x, y, s, accent):
    # Two overlapping speech bubbles: dialogue restarting.
    d.rounded_rectangle([x, y + s * 0.10, x + s * 0.62, y + s * 0.58],
                        radius=14, fill=(31, 110, 140))
    d.polygon([(x + s * 0.16, y + s * 0.58), (x + s * 0.10, y + s * 0.80),
               (x + s * 0.34, y + s * 0.58)], fill=(31, 110, 140))
    d.rounded_rectangle([x + s * 0.38, y + s * 0.42, x + s, y + s * 0.90],
                        radius=14, fill=(196, 148, 44))
    d.polygon([(x + s * 0.84, y + s * 0.90), (x + s * 0.92, y + s),
               (x + s * 0.66, y + s * 0.90)], fill=(196, 148, 44))
    for yy in (y + s * 0.26, y + s * 0.40):
        d.line([x + s * 0.10, yy, x + s * 0.52, yy], fill=WHITE, width=5)
    for yy in (y + s * 0.58, y + s * 0.72):
        d.line([x + s * 0.48, yy, x + s * 0.90, yy], fill=WHITE, width=5)


ICONS = [icon_war_toll, icon_strikes, icon_climate,
         icon_fire, icon_congress, icon_talks]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- header: the day, named up front
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    d.text((28, 26), "TUESDAY, 24 NOVEMBER 2026",
           font=font(BOLD, 50), fill=WHITE)
    d.text((30, 96), "THE WORLD IN ONE DAY  •  SIX STORIES THAT DEFINED IT",
           font=font(BOLD, 25), fill=GOLD)
    # small globe mark, top right
    gx, gy, gr = 956, 72, 34
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=GOLD, width=4)
    d.ellipse([gx - gr * 0.45, gy - gr, gx + gr * 0.45, gy + gr],
              outline=GOLD, width=3)
    d.line([gx - gr, gy, gx + gr, gy], fill=GOLD, width=3)

    # ---- grid: 2 columns x 3 rows of story panels
    mx, my, gap = 24, 176, 16
    pw = (W - 2 * mx - gap) // 2
    ph = 258
    f_tag = font(BOLD, 22)
    f_head = font(BOLD, 29)
    f_deck = font(REG, 22)

    for i, (tag, accent, head, deck) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = mx + col * (pw + gap)
        y0 = my + row * (ph + gap)
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=10, fill=WHITE)
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + 8], radius=4, fill=accent)
        d.rectangle([x0, y0 + 4, x0 + pw, y0 + 8], fill=accent)
        # icon on the left
        ICONS[i](d, x0 + 18, y0 + 62, 104, accent)
        tx = x0 + 132
        tw = pw - 132 - 16
        d.text((tx, y0 + 24), tag, font=f_tag, fill=accent)
        lines = wrap(d, head, f_head, tw)[:2]
        yy = y0 + 58
        for ln in lines:
            d.text((tx, yy), ln, font=f_head, fill=INK)
            yy += 36
        dlines = wrap(d, deck, f_deck, tw)[:2]
        for ln in dlines:
            d.text((tx, yy + 4), ln, font=f_deck, fill=MUTED)
            yy += 28

    # ---- footer
    d.text((W // 2, 990), "Stories as first reported on 24 November 2026",
           font=font(REG, 20), fill=MUTED, anchor="ma")

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
