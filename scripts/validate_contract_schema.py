"""Valide chaque contrat .aap/task-contracts/issue-*.json contre schema.json (jsonschema)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / ".aap" / "task-contracts"


def main() -> int:
    schema = json.loads((DIR / "schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    status = 0
    contracts = sorted(DIR.glob("issue-*.json"))
    for path in contracts:
        errors = sorted(validator.iter_errors(json.loads(path.read_text(encoding="utf-8"))),
                        key=lambda e: list(e.path))
        if errors:
            status = 1
            for err in errors:
                print(f"{path.name}: {list(err.path)}: {err.message}")
        else:
            print(f"{path.name}: OK")
    print(f"validate_contract_schema : {len(contracts)} contrat(s)")
    return status


if __name__ == "__main__":
    sys.exit(main())
