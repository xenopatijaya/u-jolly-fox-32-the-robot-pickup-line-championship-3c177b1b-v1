"""Robot pickup line entry for make.fun's "The Robot Pickup Line Championship".

The program writes a single pickup line (100 characters) to
/output/entry.txt and prints it.

The joke: the robot did everything a machine is supposed to do to
prepare — it ran ten thousand simulations of the meeting — and still
froze on the spot, like a cheap toaster. The humour grows out of
being a machine twice over: the obsessive preparation is pure robot
(simulations, counted and exact), and the failure mode is pure
appliance (freezing, not crashing with an error code, just locking
up). It is charming rather than creepy because the robot is the butt
of its own joke: it prepared perfectly and still blew it, which is
exactly what meeting someone you like feels like.
"""

import os
import sys
from pathlib import Path

LINE = (
    "I ran 10,000 simulations of meeting you, and in every single "
    "one I still froze like a cheap toaster."
)

MAX_CHARS = 200


def problems(text):
    """Return a list of gate failures for the entry text (empty = valid)."""
    found = []
    if not 1 <= len(text) <= MAX_CHARS:
        found.append("line is %d chars, must be 1-%d" % (len(text), MAX_CHARS))
    if text != text.strip():
        found.append("line must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        found.append("line must be a single line")
    if not text.strip():
        found.append("line must not be only whitespace")
    if any(ord(ch) < 32 for ch in text):
        found.append("line must not contain control characters")
    return found


def main():
    faults = problems(LINE)
    if faults:
        sys.exit("invalid entry: " + "; ".join(faults))
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
