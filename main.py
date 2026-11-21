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
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, "entry.png")

    with open(source_path, "rb") as handle:
        data = handle.read()

    source_hash = hashlib.sha256(data).hexdigest()

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

    print("wrote %s (%d bytes, sha256 %s)" % (target_path, len(written), written_hash))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
