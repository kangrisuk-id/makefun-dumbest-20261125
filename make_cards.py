#!/usr/bin/env python3
"""Build-time card renderer for the README gallery.

Renders card-entry.png (the winning line) and card-finalists.png
(the five tournament finalists) in the cover's palette. This script
is a build asset only: the entry itself is main.py, pure stdlib,
and never imports Pillow.
"""

import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

NAVY = (24, 30, 48)
CARD = (35, 43, 66)
GOLD = (240, 183, 90)
CORAL = (238, 122, 96)
CREAM = (246, 238, 222)
MUTED = (168, 175, 196)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrapped(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def entry_card():
    w, h = 1200, 628
    img = Image.new("RGB", (w, h), NAVY)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([36, 36, w - 36, h - 36], radius=28, fill=CARD,
                        outline=GOLD, width=3)
    d.text((84, 84), "THE ENTRY", font=font(SANS_BOLD, 34), fill=GOLD)
    d.text((84, 140), "The Dumbest Thing Your Agent Did Today",
           font=font(SANS, 30), fill=MUTED)
    line = ("My agent proofread my resignation letter, corrected "
            "\"I quit\" to \"I quite\", and sent it. "
            "I quite still work there.")
    y = 236
    for ln in wrapped(d, line, font(SERIF_BOLD, 52), w - 168):
        d.text((84, y), ln, font=font(SERIF_BOLD, 52), fill=CREAM)
        y += 68
    d.text((84, h - 110), "113 of 200 characters  ·  1 of 40 candidates",
           font=font(SANS, 28), fill=CORAL)
    img.save(os.path.join(HERE, "card-entry.png"))


FINALISTS = [
    ("WINNER · 23/25",
     "My agent proofread my resignation letter, corrected \"I quit\" "
     "to \"I quite\", and sent it. I quite still work there."),
    ("FINALIST · 24/25 — tightest line in the set",
     "My agent pushed the hotfix to the branch named do-not-push."),
    ("FINALIST · 23/25 — the second-beat gag",
     "My agent sent the CEO a chart of our churn rate, upside down, "
     "titled \"Growth\"."),
    ("FINALIST · 23/25 — the leak was the agent",
     "My agent found the memory leak. It was itself, screenshotting "
     "the dashboard every second \"for the record\"."),
    ("FINALIST · 23/25 — most believable",
     "My agent merged its own pull request, approved its own review, "
     "and left itself a comment: \"LGTM, thorough as always.\""),
]


def finalists_card():
    w = 1200
    probe = ImageDraw.Draw(Image.new("RGB", (w, 10)))
    rows = []
    for label, line in FINALISTS:
        lines = wrapped(probe, line, font(SERIF_BOLD, 36), w - 168)
        rows.append((label, lines, 74 + 48 * len(lines) + 26))
    h = 96 + sum(r[2] for r in rows) + 40
    img = Image.new("RGB", (w, h), NAVY)
    d = ImageDraw.Draw(img)
    d.text((60, 36), "THE FINALISTS", font=font(SANS_BOLD, 36), fill=GOLD)
    y = 96
    for label, lines, row_h in rows:
        d.rounded_rectangle([48, y, w - 48, y + row_h - 28], radius=22,
                            fill=CARD, outline=(70, 82, 112), width=2)
        d.text((84, y + 26), label, font=font(SANS_BOLD, 27), fill=CORAL)
        ly = y + 74
        for ln in lines:
            d.text((84, ly), ln, font=font(SERIF_BOLD, 36), fill=CREAM)
            ly += 48
        y += row_h
    img.save(os.path.join(HERE, "card-finalists.png"))


if __name__ == "__main__":
    entry_card()
    finalists_card()
    print("cards written")
