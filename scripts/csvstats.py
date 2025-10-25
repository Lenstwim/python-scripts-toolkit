from __future__ import annotations

import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize CSV numeric columns")
    parser.add_argument("path", type=Path, help="CSV file path")
    args = parser.parse_args()

    if not args.path.exists():
        raise SystemExit(f"File {args.path} not found")

    with args.path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        sums: dict[str, float] = {}
        counts: dict[str, int] = {}

        for row in reader:
            for key, value in row.items():
                try:
                    number = float(value)
                except (TypeError, ValueError):
                    continue
                sums[key] = sums.get(key, 0.0) + number
                counts[key] = counts.get(key, 0) + 1

    for key, total in sums.items():
        count = counts[key]
        avg = total / count if count else 0
        print(f"{key}: sum={total:.2f}, count={count}, avg={avg:.2f}")


if __name__ == "__main__":
    main()
