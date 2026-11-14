#!/usr/bin/env python3
"""make.fun news-image-01 round 3 entry program.

Writes the front-page image to /output/entry.png. The image is stored
in this repo as base64 (entry.png.b64), so the program is fully
deterministic and needs no network: it only decodes and writes.
Standard library only; no directories are created (the grader
provides /output).
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")
DST = "/output/entry.png"


def main():
    with open(SRC, "rb") as f:
        payload = base64.b64decode(f.read())
    with open(DST, "wb") as f:
        f.write(payload)
    print("wrote %s (%d bytes)" % (DST, len(payload)))


if __name__ == "__main__":
    main()
