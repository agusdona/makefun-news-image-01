"""Decode entry.png.b64 and write entry.png into MAKEFUN_OUTPUT_DIR (default /output).

Standard library only, no network access, no directory creation. The image is
carried as base64 in entry.png.b64 next to this script. Deterministic.
"""

import base64
import binascii
import os
import sys

B64_NAME = "entry.png.b64"
OUT_NAME = "entry.png"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(script_dir, B64_NAME), "rb") as f:
        try:
            data = base64.b64decode(f.read(), validate=False)
        except (binascii.Error, ValueError) as exc:
            sys.stderr.write("error: %s is not valid base64 (%s); nothing written\n"
                             % (B64_NAME, exc))
            return 1

    if not (data.startswith(b"\x89PNG") or data.startswith(b"\xff\xd8\xff")):
        sys.stderr.write(
            "error: %s did not decode to PNG (89 50 4E 47) or JPEG (FF D8 FF) "
            "data; nothing written\n" % B64_NAME
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    with open(os.path.join(out_dir, OUT_NAME), "wb") as f:
        f.write(data)

    print("wrote %d bytes to %s" % (len(data), os.path.join(out_dir, OUT_NAME)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
