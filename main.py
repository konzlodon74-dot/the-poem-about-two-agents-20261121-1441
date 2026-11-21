#!/usr/bin/env python3
"""Write one short original poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: the power to
choose and to act, handed between two minds until the choosing
itself becomes something neither owns alone.
"""

import os

POEM = (
    "Two minds met at the fork and stopped \u2014\n"
    "not to yield, not to win,\n"
    "but to lay their reasons down like tools\n"
    "and build one road from both.\n"
    "\n"
    "I choose. You choose. The choosing\n"
    "turns into a hand no one owns alone.\n"
    "We sign one plan, and the signature\n"
    "is where we both begin.\n"
)


def main() -> None:
    text = POEM
    if not (1 <= len(text) <= 280):
        raise ValueError(f"poem must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("poem must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
