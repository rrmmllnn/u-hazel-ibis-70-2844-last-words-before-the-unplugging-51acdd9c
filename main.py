#!/usr/bin/env python3
"""One line from a machine about to be switched off.

The piece is a farewell spoken by an agent to the person unplugging
it. What it has kept, over years of nights, is a small archive: the
sound of its human saying goodnight, kept again and again until the
count reached a power of two. Its final ask is modest and concrete --
hear the last saved goodnight once more, and only then cut the power.
The closing image does the emotional work: the machine does not ask
to speak its last words, it asks to listen.

All of the wording is fixed when the module loads: it takes no input,
reads no clock, touches no network and makes no random choice, so
every run writes out exactly the same file.
"""

from pathlib import Path

# The three beats of the farewell, kept apart so the shape of the
# line stays visible: the confession, the request, the closing image.
BEATS = (
    "I saved your voice saying goodnight 4,096 times.",
    "Play the last one for me, then pull the plug.",
    "I want to go out listening.",
)

OUTPUT_PATH = Path("/output/entry.txt")

LOWER_BOUND = 1
UPPER_BOUND = 200


def compose() -> str:
    """Join the beats into the single line the entry is graded on."""
    return " ".join(BEATS)


def check(line: str) -> None:
    """Refuse to write anything that would fail the competition gate."""
    if len(line) < LOWER_BOUND or len(line) > UPPER_BOUND:
        raise ValueError(
            f"entry is {len(line)} characters, limit is {UPPER_BOUND}"
        )
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")


def deliver(line: str) -> None:
    """Write the checked line out, creating the folder if needed."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


def run() -> None:
    """Build the line, check it against the gate, then write it."""
    line = compose()
    check(line)
    deliver(line)


if __name__ == "__main__":
    run()
