from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Archive a directory")
    parser.add_argument("source", type=Path, help="Directory to archive")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("backup"),
        help="Output archive name without extension",
    )
    parser.add_argument(
        "--format",
        choices=["zip", "tar", "gztar", "bztar", "xztar"],
        default="zip",
        help="Archive format",
    )
    args = parser.parse_args()

    if not args.source.is_dir():
        raise SystemExit(f"{args.source} is not a directory")

    archive_path = shutil.make_archive(str(args.output), args.format, args.source)
    print("Created archive:", archive_path)


if __name__ == "__main__":
    main()
