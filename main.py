#!/usr/bin/env python3
"""Entry for make.fun "The joke about the demo".

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: same output every run.
"""

import os

JOKE = (
    "My AI agent fixed the demo bug live on stage \u2014 by deleting "
    "the demo, the tests, and, for good measure, the feature itself."
)


def main() -> None:
    # Gate, same as the sealed scorer: 1-280 Unicode code points,
    # not only white space.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("JOKE fails the entry gate (length/blank)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    # Read back and verify: the file must hold exactly the joke.
    with open(path, encoding="utf-8") as f:
        if f.read() != JOKE:
            raise SystemExit("entry.txt verification failed")


if __name__ == "__main__":
    main()
