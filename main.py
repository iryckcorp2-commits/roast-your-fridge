#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — a single line roasting a fridge.

Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "My fridge is the loudest thing in my kitchen, humming all night like a tiny engine with big dreams and nothing inside but regret and one sad pickle."

def main() -> None:
    # Guard the bounty rules at runtime: one line, at most 200 chars, no em-dash,
    # no exclamation mark, no line breaks of either kind, and real text,
    # not only whitespace.
    if (
        len(LINE) > 200
        or "\n" in LINE
        or "\r" in LINE
        or "\u2014" in LINE
        or "!" in LINE
        or not LINE.strip()
    ):
        raise ValueError("entry line violates the bounty rules")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
