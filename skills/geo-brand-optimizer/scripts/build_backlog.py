#!/usr/bin/env python3
"""Build a transparent, priority-sorted Markdown GEO backlog from JSON."""

import argparse
import json
import sys
from pathlib import Path

REQUIRED = {
    "id", "title", "evidence_ids", "problem", "hypothesis", "action", "owner",
    "effort", "expected_impact", "confidence", "evidence_strength",
    "expected_signal", "measurement", "retest_window",
}


def factor(item, field):
    value = item.get(field)
    if not isinstance(value, int) or isinstance(value, bool) or not 1 <= value <= 5:
        raise ValueError(f"{item.get('id', '<unknown>')}: {field} must be an integer from 1 to 5")
    return value


def score(item):
    return round(
        factor(item, "evidence_strength")
        * factor(item, "expected_impact")
        * factor(item, "confidence")
        / factor(item, "effort"),
        2,
    )


def render(items):
    ordered = sorted(items, key=score, reverse=True)
    lines = ["# GEO optimization backlog", "", "Scores sort work; they are not outcome guarantees.", ""]
    for item in ordered:
        evidence = ", ".join(str(value) for value in item["evidence_ids"]) or "none supplied"
        lines.extend([
            f"## {item['id']} — {item['title']}", "",
            f"**Priority score:** {score(item)}  ",
            f"**Factors:** evidence {item['evidence_strength']}/5 · impact {item['expected_impact']}/5 · confidence {item['confidence']}/5 · effort {item['effort']}/5  ",
            f"**Evidence:** {evidence}  ",
            f"**Owner:** {item['owner']}", "",
            f"**Observed problem:** {item['problem']}", "",
            f"**Hypothesis:** {item['hypothesis']}", "",
            f"**Action:** {item['action']}", "",
            f"**Expected signal:** {item['expected_signal']}", "",
            f"**Measurement:** {item['measurement']}", "",
            f"**Retest window:** {item['retest_window']}", "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        items = json.loads(args.path.read_text(encoding="utf-8"))
        if not isinstance(items, list) or not items:
            raise ValueError("input must be a non-empty JSON array")
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("every array item must be an object")
            missing = sorted(REQUIRED - set(item))
            if missing:
                raise ValueError(f"{item.get('id', '<unknown>')}: missing {', '.join(missing)}")
        output = render(items)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
