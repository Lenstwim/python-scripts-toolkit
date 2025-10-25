from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def compute_hash(path: Path, chunk_size: int = 8192) -> str:
    sha256 = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            sha256.update(chunk)
    return sha256.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute file SHA256 hash")
    parser.add_argument("path", type=Path, help="File to hash")
    args = parser.parse_args()

    if not args.path.is_file():
        raise SystemExit(f"{args.path} is not a file")

    print(compute_hash(args.path))


if __name__ == "__main__":
    main()
