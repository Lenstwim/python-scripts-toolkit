from __future__ import annotations

import argparse
import secrets
import string


def build_alphabet(use_symbols: bool) -> str:
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += string.punctuation
    return alphabet


def generate_password(length: int, use_symbols: bool) -> str:
    alphabet = build_alphabet(use_symbols)
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate random passwords")
    parser.add_argument("--length", type=int, default=16, help="Password length")
    parser.add_argument(
        "--symbols", action="store_true", help="Include punctuation symbols"
    )
    args = parser.parse_args()

    print(generate_password(args.length, args.symbols))


if __name__ == "__main__":
    main()
