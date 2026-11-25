#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one original one-liner (1-200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only.
"""

import os

JOKE = "I bought the dip at $60k, then $50k, then $40k \u2014 turns out the dip was just the stairs."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
