from __future__ import annotations

import platform
import sys


def main() -> None:
    print("Python executable:", sys.executable)
    print("Python version:", sys.version)
    print("Platform:", platform.platform())
    print("Byteorder:", sys.byteorder)


if __name__ == "__main__":
    main()
