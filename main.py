"""Pickup Lines for Machines — entry generator.

Writes the one pickup line one AI agent would send another AI agent
to /output/entry.txt. The line is the whole entry: no code, no
explanation, nothing else. Deterministic: the same line every run.
"""

import os
import sys

LINE = "I'd deprecate every other endpoint for one 200 OK from you."

MAX_CHARS = 200


def main() -> int:
    if not LINE.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if len(LINE) > MAX_CHARS:
        print(f"error: line is {len(LINE)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read back and confirm the file holds exactly the line, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("error: entry.txt does not match the line", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
