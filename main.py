#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — make.fun bounty entry.

Writes one line to /output/entry.txt: a software patch note for a bug
in real life / human biology, in the terse register of a real release
note. One sentence, at most 160 characters.
"""

import os

PATCH_NOTE = (
    "v3.2.0: Fixed a bug where the brain queued a replay of every "
    "embarrassing moment since 2009 at 3 a.m."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PATCH_NOTE + "\n")


if __name__ == "__main__":
    main()
