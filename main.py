#!/usr/bin/env python3
"""Write the pickup line entry to the output directory.

Reads entry.txt next to this script, validates it (1..200 UTF-8
characters, not only whitespace), and writes its exact bytes to
$MAKEFUN_OUTPUT_DIR/entry.txt (default "output").
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "rb") as f:
        data = f.read()

    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1..200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
