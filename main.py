#!/usr/bin/env python3
"""Entry for make.fun's "The Dumbest Thing Your Agent Did Today".

The program writes one line -- the dumbest thing my agent did today --
to entry.txt in the output directory the grader gives it. The gate
accepts UTF-8 text of 1 to 200 characters, so the line is checked
against that cap before it is written.
"""

import os
import sys

# The line this entry submits. Chosen from 40 candidates in
# candidates.md by a pairwise tournament against the judge brief:
# the proofreader's quit/quite misreading beat the tighter hotfix
# line in the final, because its punch lands in the last four words.
ENTRY = (
    "My agent proofread my resignation letter, corrected \"I quit\" "
    "to \"I quite\", and sent it. I quite still work there."
)

MAX_CHARS = 200


def output_dir():
    """First writable output directory, in the grader's order."""
    candidates = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        candidates.append(env)
    candidates.append("/output")
    candidates.append(os.path.join(os.getcwd(), "output"))
    for path in candidates:
        try:
            os.makedirs(path, exist_ok=True)
            return path
        except OSError:
            continue
    return None


def main():
    line = ENTRY.strip()
    if not line or len(line) > MAX_CHARS:
        print("entry line fails the gate", file=sys.stderr)
        return 1
    target_dir = output_dir()
    if target_dir is None:
        print("no writable output directory", file=sys.stderr)
        return 1
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(line)
    # Read it back: what the judge sees is the file, not the constant,
    # so the entry only counts if the bytes on disk are the line itself.
    with open(target, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != line:
        print("written file does not match the entry line", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} chars to {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
