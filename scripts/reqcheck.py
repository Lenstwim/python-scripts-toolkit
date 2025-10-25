from __future__ import annotations

import importlib.util
from pathlib import Path


def parse_requirements(path: Path) -> list[str]:
    if not path.exists():
        print("requirements.txt not found")
        return []
    packages: list[str] = []
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        package = line.split(";")[0].split("[", 1)[0].split("==", 1)[0]
        packages.append(package)
    return packages


def main() -> None:
    requirements = parse_requirements(Path("requirements.txt"))
    if not requirements:
        return

    missing = []
    for package in requirements:
        if importlib.util.find_spec(package) is None:
            missing.append(package)

    if missing:
        print("Missing packages:")
        for pkg in missing:
            print(" -", pkg)
    else:
        print("All required packages are installed.")


if __name__ == "__main__":
    main()
