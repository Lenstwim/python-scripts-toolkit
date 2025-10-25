from __future__ import annotations

import argparse
import time
from pathlib import Path


def stream_log(path: Path, interval: float = 1.0) -> None:
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        handle.seek(0, 2)
        while True:
            line = handle.readline()
            if not line:
                time.sleep(interval)
                continue
            line = line.rstrip()
            if "error" in line.lower():
                print("[ERROR]", line)
            else:
                print(line)


def main() -> None:
    parser = argparse.ArgumentParser(description="Watch a log file for updates")
    parser.add_argument("path", type=Path, help="Path to the log file")
    parser.add_argument(
        "--interval", type=float, default=1.0, help="Polling interval in seconds"
    )
    args = parser.parse_args()

    if not args.path.exists():
        raise SystemExit(f"File {args.path} does not exist")

    stream_log(args.path, args.interval)


if __name__ == "__main__":
    main()
