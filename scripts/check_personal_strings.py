"""Refuse les chaines personnelles (chemins, comptes locaux, dossiers temporaires) dans le depot.

Usage : python scripts/check_personal_strings.py [--root .] [--exclude chemin ...]
Code de sortie 1 si une occurrence est trouvee. Les motifs sont volontairement
courts et generiques ; ajouter un motif = une ligne dans PATTERNS.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

PATTERNS = [
    re.compile(r"[A-Za-z]:\\Users\\"),
    re.compile(r"\bASUS\b"),
    re.compile(r"Temp\\claude"),
    re.compile(r"/Users/[a-z]"),
    re.compile(r"sk-ant-[A-Za-z0-9_-]{8,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
]
SELF = Path(__file__).resolve()


def tracked_files(root: Path) -> list[Path]:
    out = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True
    ).stdout
    return [root / p.decode("utf-8") for p in out.split(b"\0") if p]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--exclude", nargs="*", default=[])
    args = parser.parse_args(argv)
    root = args.root.resolve()
    excluded = [(root / e).resolve() for e in args.exclude]
    hits = 0
    for path in tracked_files(root):
        if path.resolve() == SELF or any(path.resolve().is_relative_to(e) for e in excluded):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for pat in PATTERNS:
                if pat.search(line):
                    hits += 1
                    print(f"{path.relative_to(root)}:{lineno}: motif {pat.pattern!r}")
    print(f"check_personal_strings : {hits} occurrence(s)")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
