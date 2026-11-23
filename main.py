#!/usr/bin/env python3
"""The Vacuum's Alibi — make.fun entry.

Writes one excuse, in the robot vacuum's own deadpan voice, for missing
a spot, to /output/entry.txt. Pure standard library only; deterministic.
"""

import os

# The chosen line (142 chars): two of the vacuum's own sensors disagree,
# and it smugly sides with the one it trusts — then undercuts that trust
# with the specific, unexpected reason why. The punch lands at the end.
LINE = (
    "My lidar mapped that spot as clean, my camera called it a crumb, "
    "and I sided with the lidar, because the camera once mistook a sock "
    "for a cat."
)

# Entry contract: a single non-blank line, 1-200 chars (kit limit).
MAX_LINE_CHARS = 200


def validate_line(line: str) -> str:
    """Return the line if it meets the entry contract, else raise."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be blank")
    if len(line) != len(stripped):
        raise ValueError("entry line must not have leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not 1 <= len(line) <= MAX_LINE_CHARS:
        raise ValueError(
            f"entry line must be 1-{MAX_LINE_CHARS} chars, got {len(line)}"
        )
    return line


def main() -> None:
    line = validate_line(LINE)
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
