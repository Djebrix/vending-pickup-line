"""Vending Machine Pickup Line — one line, written to entry.txt.

Stdlib only, no network. Deterministic: same line every run.
"""

import os

LINE = (
    "Press B7 — my coil's been saving your favorite just for you, "
    "and I've been humming your name in quarters all day."
)

assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
