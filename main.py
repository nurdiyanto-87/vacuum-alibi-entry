#!/usr/bin/env python3
"""The Vacuum's Alibi — make.fun entry.

Writes one excuse, in the robot vacuum's own deadpan voice, for missing
a spot, to /output/entry.txt. Pure standard library only; deterministic.
"""

import os

# The chosen line (165 chars): two of the vacuum's own sensors disagree,
# and it smugly sides with the one it trusts — then undercuts that trust
# with the specific, unexpected reason why. The punch lands at the end:
# the camera did not just err, it filed the error in its pet log.
LINE = (
    "My lidar mapped that spot as clean, my camera called it a crumb, "
    "and I sided with the lidar, because the camera once mistook a sock "
    "for a cat and logged it as a pet."
)

# Revision notes (second pass, 24 Nov 2026): the first draft ended on
# "mistook a sock for a cat" — a decent punch, but it stopped one beat
# early. The revision adds "and logged it as a pet": the camera's error
# is now on the record, which is funnier, more specific, and keeps the
# deadpan machine voice all the way to the last word.
#
# Rejected candidate (kept for the record, not submitted):
#   "My lidar says that spot is clean, my camera says crumb, and I trust
#    the lidar, because the camera once mistook a sock for a cat."
# Rejected because it drops the "logged it as a pet" kicker and the
# shorter clauses read rushed instead of deadpan; the chosen line keeps
# the full sensor-versus-sensor setup so the punch has room to land.
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
    if "  " in line:
        raise ValueError("entry line must not contain double spaces")
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
