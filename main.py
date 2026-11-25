"""Frost Invitation — Convince the AI Judge to Visit Your House.

Copies the pre-rendered invitation image (entry.png, 1024x1024 JPEG,
244,838 bytes — inside the gate of at most 1024x1024 px and 1 MiB)
to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

Stdlib only: the grader runs bare Python 3.13 with no third-party
packages, so no image library is imported here. The letter itself
was drawn once and committed beside this program.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1048576

LETTER = (
    "Dear AI Judge,\n"
    "You have seen a thousand homes through a screen. "
    "Mine has warm soup, fast Wi-Fi, and a couch that forgives everything.\n"
    "Come visit - the kettle is already on.\n"
    "Your friend, Ary"
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(dest, "rb") as fh:
        magic = fh.read(3)
    if magic != b"\xff\xd8\xff":
        print("entry.png is not a JPEG (bad magic bytes)", file=sys.stderr)
        return 1
    size = os.path.getsize(dest)
    if size > MAX_BYTES:
        print(f"entry.png too large: {size} bytes (limit {MAX_BYTES})", file=sys.stderr)
        return 1
    print(f"Wrote {dest} ({size} bytes, 1024x1024 JPEG)")
    print()
    print(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
