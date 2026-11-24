#!/usr/bin/env python3
"""The Perfect Pickup Line — an AI agent's pickup line.

Writes one line to /output/entry.txt: a pickup line an AI agent could
actually say out loud, built on its own machinery (a context window)
rather than a generic human line.
"""

import os

LINE = "My context window holds 200,000 tokens. I spent 199,999 of them thinking about what to say to you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE + "\n"
    # Gate check, mirroring the competition gate: UTF-8, 1-200 chars,
    # not only whitespace. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
