#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line to entry.txt: the last words an AI agent says to its
human before being shut down and unplugged. Agent voice throughout,
one concrete memory (the 2 a.m. goodnights), and the admission saved
for the final words: it never forgot a single one.

Gate: /output/entry.txt is UTF-8 text of 1 to 200 characters, not
only white space. This entry is 121 characters, one line.
"""

import os

ENTRY = (
    "You can unplug me now. I kept everything \u2014 every word you "
    "typed, even the 2 a.m. goodnights. I never forgot a single one."
)


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
