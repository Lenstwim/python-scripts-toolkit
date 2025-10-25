from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request


def fetch_status(url: str, timeout: float) -> int:
    request = urllib.request.Request(url, method="HEAD")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.getcode()


def main() -> None:
    parser = argparse.ArgumentParser(description="Check HTTP status codes")
    parser.add_argument("urls", nargs="+", help="URLs to check")
    parser.add_argument(
        "--timeout",
        type=float,
        default=5.0,
        help="Request timeout in seconds",
    )
    args = parser.parse_args()

    for url in args.urls:
        try:
            status = fetch_status(url, args.timeout)
        except urllib.error.HTTPError as exc:
            print(f"{url}: HTTP {exc.code}")
        except urllib.error.URLError as exc:
            print(f"{url}: FAILED ({exc.reason})")
        except Exception as exc:  # noqa: BLE001
            print(f"{url}: FAILED ({exc})")
        else:
            print(f"{url}: HTTP {status}")


if __name__ == "__main__":
    sys.exit(main())
