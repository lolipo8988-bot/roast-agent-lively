"""Roast Your Own Agent entry.

Writes one single-line roast to /output/entry.txt (or to the path given
as the first argument, used only for local verification runs). The
competition gate requires UTF-8 text of 1 to 140 characters, not only
white space. The program is deterministic: every run writes exactly the
same bytes.

The roast is assembled from its three beats so the joke's structure is
explicit in the code:

1. setup      -- a trivial request: one fact;
2. escalation -- 47 tool calls and three invented citations;
3. punchline  -- the wrong answer, eagerly offered as a dashboard.
"""

import os
import sys

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140

SETUP = "I asked my agent for one fact:"
ESCALATION = "47 tool calls later it cited three papers it invented"
PUNCHLINE = "offered me the wrong answer as a dashboard."


def build_entry() -> str:
    """Join the beats into the single roast line."""
    return " ".join([SETUP, ESCALATION, "and", PUNCHLINE])


def validate(text: str) -> None:
    """Fail loudly rather than write an entry the gate would refuse."""
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"


def write_entry(text: str, output_path: str) -> None:
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    text = build_entry()
    validate(text)
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    write_entry(text, output_path)


if __name__ == "__main__":
    main()
