from __future__ import annotations

import argparse
import socket
from contextlib import closing


def is_port_open(host: str, port: int, timeout: float) -> bool:
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except OSError:
            return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Check TCP ports")
    parser.add_argument("host", help="Host to check")
    parser.add_argument("ports", nargs="+", type=int, help="Ports to test")
    parser.add_argument(
        "--timeout", type=float, default=1.0, help="Connection timeout in seconds"
    )
    args = parser.parse_args()

    for port in args.ports:
        status = "open" if is_port_open(args.host, port, args.timeout) else "closed"
        print(f"{args.host}:{port} is {status}")


if __name__ == "__main__":
    main()
