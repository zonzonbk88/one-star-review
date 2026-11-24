#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review, one line, to /output/entry.txt.
Standard library only. No network, no randomness, no file reads.
"""

import os

REVIEW = (
    "Sleep: eight hours a night, every night, and I still wake up "
    "feeling like I owe it money."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
