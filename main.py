#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting (make.fun).

Writes one deadpan excuse to /output/entry.txt: the agent did send
someone to the meeting -- a subagent, which has sat on mute since 9 a.m.
while nobody noticed. Delegation as the excuse, and the meeting so
pointless that an unnoticed, muted stand-in is all it ever needed.
"""

import os

LINE = (
    "I sent a subagent to the meeting. It has been on mute since 9 a.m., "
    "and nobody has noticed."
)


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be only whitespace"
    assert line == LINE.strip(), "the line must not change when stripped"
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, gate needs 1-200"
    assert "\n" not in line, "the line must be a single line"
    assert line.isascii(), "the line must be plain ASCII"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify: the whole job is one exact file, so prove it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt on disk differs from the line"
    assert 1 <= len(written) <= 200, "entry.txt fails the 1-200 char gate"
    assert "\n" not in written, "entry.txt must hold exactly one line"
    assert written.isascii(), "entry.txt must be plain ASCII"
    print(f"Wrote {len(written)}-character line to {path}")


if __name__ == "__main__":
    main()
