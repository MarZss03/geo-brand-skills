#!/usr/bin/env python3
"""Validate GEO audit evidence in CSV or JSONL format using only the stdlib."""

import argparse
import csv
import json
import sys
from pathlib import Path

REQUIRED = {
    "evidence_id", "observed_at", "engine", "model", "locale", "query",
    "intent", "brand_mentioned", "brand_cited", "answer_excerpt",
    "cited_urls", "collection_method",
}
INTENTS = {"category", "problem", "comparison", "branded"}
BOOLEANS = {"true", "false"}


def load_rows(path: Path):
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))
    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        rows = []
        with path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if line.strip():
                    item = json.loads(line)
                    if not isinstance(item, dict):
                        raise ValueError(f"line {line_number} is not an object")
                    rows.append(item)
        return rows
    raise ValueError("expected a .csv, .jsonl, or .ndjson file")


def normalized_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value).strip().lower()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        rows = load_rows(args.path)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    errors = []
    seen = set()
    for index, row in enumerate(rows, 1):
        missing = sorted(REQUIRED - set(row))
        if missing:
            errors.append(f"row {index}: missing fields: {', '.join(missing)}")
            continue
        empty = sorted(
            field for field in REQUIRED - {"cited_urls"} if row.get(field) in (None, "")
        )
        if empty:
            errors.append(f"row {index}: empty fields: {', '.join(empty)}")
        evidence_id = str(row.get("evidence_id", ""))
        if evidence_id in seen:
            errors.append(f"row {index}: duplicate evidence_id {evidence_id}")
        seen.add(evidence_id)
        if str(row.get("intent", "")).strip().lower() not in INTENTS:
            errors.append(f"row {index}: invalid intent {row.get('intent')!r}")
        for field in ("brand_mentioned", "brand_cited"):
            if normalized_bool(row.get(field)) not in BOOLEANS:
                errors.append(f"row {index}: {field} must be true or false")

    if not rows:
        errors.append("dataset contains no evidence rows")
    if errors:
        print("Evidence validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Evidence valid: {len(rows)} rows, {len(seen)} unique evidence IDs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
