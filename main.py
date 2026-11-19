"""Copy the pre-rendered front page to the output directory.

Reads MAKEFUN_OUTPUT_DIR (default "/output") and writes entry.png there.
Standard library only. Deterministic: the output bytes are always an exact
copy of the entry.png shipped in this repository. The output directory is
created if needed and is never deleted.
"""

import os

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(SOURCE, "rb") as src:
        data = src.read()
    dest = os.path.join(output_dir, "entry.png")
    with open(dest, "wb") as out:
        out.write(data)
    if os.path.getsize(dest) != len(data):
        raise IOError("short write copying entry.png")


if __name__ == "__main__":
    main()
