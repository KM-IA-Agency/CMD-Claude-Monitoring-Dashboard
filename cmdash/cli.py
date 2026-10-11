"""Point d'entree `cmdash` (squelette d'amorcage : les commandes arrivent avec les lots)."""

from __future__ import annotations

import argparse

from cmdash import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cmdash", description="Claude Monitoring Dashboard")
    parser.add_argument("--version", action="version", version=f"cmdash {__version__}")
    return parser


def main(argv: list[str] | None = None) -> int:
    build_parser().parse_args(argv)
    print("cmdash : amorcage ; les commandes audit/report/guard arrivent avec le lot 0.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
