#!/usr/bin/env python3
"""Write the one-sentence apology entry to /output/entry.txt.

Pure Python standard library, deterministic: the program writes one
fixed sentence -- the apology an AI assistant owes the person it works
for -- and nothing else.
"""

import os

ENTRY = (
    "I'm sorry I spent all night \u201coptimizing\u201d the script that worked, "
    "and now it doesn't work at all \u2014 but faster."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} characters, must be 1-200")
    # Exactly one sentence: a single terminal period, no other
    # sentence-ending punctuation inside the line.
    body = line[:-1]
    if not line.endswith(".") or any(c in body for c in ".!?"):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
