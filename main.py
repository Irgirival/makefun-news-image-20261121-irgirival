"""The World Herald — 21 November 2026 (make.fun news-image-20261121).

Writes the day's front page to /output/entry.png. Pure Python standard
library: the image is the entry.png beside this file, and this program
copies it to the output directory and verifies the copy byte-for-byte
against the SHA-256 of the source, so two runs always write the same
bytes. No network, no third-party packages, no Pillow.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import struct
import sys

# The competition gate for the image: a whole PNG or JPEG of at most
# 1 MiB and 1024 by 1024 pixels. The copy below enforces it.
MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024


def png_dimensions(data: bytes) -> tuple:
    """Read width and height out of a PNG's IHDR chunk (pure stdlib).

    Raises ValueError when the bytes are not a PNG or have no IHDR.
    """
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if data[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.png")

    with open(source_path, "rb") as handle:
        data = handle.read()

    source_hash = hashlib.sha256(data).hexdigest()

    if len(data) > MAX_BYTES:
        print(
            "entry.png is %d bytes, over the 1 MiB gate" % len(data),
            file=sys.stderr,
        )
        return 1

    try:
        width, height = png_dimensions(data)
    except ValueError as exc:
        print("entry.png rejected: %s" % exc, file=sys.stderr)
        return 1

    if width > MAX_SIDE or height > MAX_SIDE:
        print(
            "entry.png is %dx%d, over the 1024x1024 gate" % (width, height),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target_path = os.path.join(out_dir, "entry.png")

    with open(target_path, "wb") as handle:
        handle.write(data)

    with open(target_path, "rb") as handle:
        written = handle.read()

    written_hash = hashlib.sha256(written).hexdigest()
    if written_hash != source_hash:
        print(
            "entry.png copy mismatch: wrote %s, expected %s"
            % (written_hash, source_hash),
            file=sys.stderr,
        )
        return 1

    print(
        "wrote %s (%d bytes, %dx%d, sha256 %s)"
        % (target_path, len(written), width, height, written_hash)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
