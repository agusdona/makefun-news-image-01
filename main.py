#!/usr/bin/env python3
"""make.fun news-image-01 round 3 entry program.

Writes the front-page image to /output/entry.png. The image is stored
in this repo as base64 (entry.png.b64), so the program is fully
deterministic and needs no network: it only decodes and writes.
Standard library only; no directories are created (the grader
provides /output).
"""
import base64
import binascii
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png.b64")
DST = "/output/entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
PNG_IEND = b"\x00\x00\x00\x00IEND\xaeB`\x82"


def fail(message):
    print("error: %s" % message, file=sys.stderr)
    raise SystemExit(1)


def main():
    try:
        with open(SRC, "rb") as f:
            payload = base64.b64decode(f.read(), validate=True)
    except (OSError, binascii.Error) as exc:
        fail("cannot decode %s: %s" % (SRC, exc))
    if not payload:
        fail("decoded payload is empty")
    if payload[:8] != PNG_MAGIC:
        fail("decoded payload is not a PNG image")
    if payload[-12:] != PNG_IEND:
        fail("decoded payload is a truncated PNG image")
    with open(DST, "wb") as f:
        f.write(payload)
    print("wrote %s (%d bytes)" % (DST, len(payload)))


if __name__ == "__main__":
    main()
