#!/usr/bin/env python3
"""One Line, Big Laugh — entry program.

Writes a single funny line (88 characters, no title/setup) to entry.txt.
Standard library only. Writes only to the output directory (MAKEFUN_OUTPUT_DIR
or /output); never writes to the repository folder.
"""

import os

LINE = 'I told my wife I\'d fix the leak. She said, "That\'s what you said about our marriage."'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
