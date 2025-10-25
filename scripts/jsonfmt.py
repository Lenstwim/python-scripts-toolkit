from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Pretty print JSON")
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="Path to JSON file (defaults to stdin)",
    )
    parser.add_argument("--indent", type=int, default=2, help="Indent size")
    args = parser.parse_args()

    if args.path:
        data = json.loads(args.path.read_text())
    else:
        data = json.load(sys.stdin)

    json.dump(data, sys.stdout, indent=args.indent, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
